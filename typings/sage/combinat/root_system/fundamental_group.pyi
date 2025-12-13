from sage.categories.category import Category as Category
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.groups import Groups as Groups
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family, LazyFamily as LazyFamily
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def FundamentalGroupOfExtendedAffineWeylGroup(cartan_type, prefix: str = 'pi', general_linear=None):
    '''
    Factory for the fundamental group of an extended affine Weyl group.

    INPUT:

    - ``cartan_type`` -- a Cartan type that is either affine or finite, with the latter being a
      shorthand for the untwisted affinization
    - ``prefix`` -- (default: ``\'pi\'``) string that labels the elements of the group
    - ``general_linear`` -- (default: ``None``, meaning ``False``) In untwisted
      type `A`, if ``True``, use the universal central extension

    .. RUBRIC:: Fundamental group

    Associated to each affine Cartan type `\\tilde{X}` is an extended affine Weyl group `E`.
    Its subgroup of length-zero elements is called the fundamental group `F`.
    The group `F` can be identified with a subgroup of the group of automorphisms of the
    affine Dynkin diagram. As such, every element of `F` can be viewed as a permutation of the
    set `I` of affine Dynkin nodes.

    Let `0 \\in I` be the distinguished affine node; it is the one whose removal produces the
    associated finite Cartan type (call it `X`). A node `i \\in I` is called *special*
    if some automorphism of the affine Dynkin diagram, sends `0` to `i`.
    The node `0` is always special due to the identity automorphism.
    There is a bijection of the set of special nodes with the fundamental group. We denote the
    image of `i` by `\\pi_i`. The structure of `F` is determined as follows.

    - `\\tilde{X}` is untwisted -- `F` is isomorphic to `P^\\vee/Q^\\vee` where `P^\\vee` and `Q^\\vee` are the
      coweight and coroot lattices of type `X`. The group `P^\\vee/Q^\\vee` consists of the cosets `\\omega_i^\\vee + Q^\\vee`
      for special nodes `i`, where `\\omega_0^\\vee = 0` by convention. In this case the special nodes `i`
      are the *cominuscule* nodes, the ones such that `\\omega_i^\\vee(\\alpha_j)` is `0` or `1` for all `j\\in I_0 = I \\setminus \\{0\\}`.
      For `i` special, addition by `\\omega_i^\\vee+Q^\\vee` permutes `P^\\vee/Q^\\vee` and therefore permutes the set of special nodes.
      This permutation extends uniquely to an automorphism of the affine Dynkin diagram.
    - `\\tilde{X}` is dual untwisted -- (that is, the dual of `\\tilde{X}` is untwisted) `F` is isomorphic to `P/Q`
      where `P` and `Q` are the weight and root lattices of type `X`. The group `P/Q` consists of the cosets
      `\\omega_i + Q` for special nodes `i`, where `\\omega_0 = 0` by convention. In this case the special nodes `i`
      are the *minuscule* nodes, the ones such that `\\alpha_j^\\vee(\\omega_i)` is `0` or `1` for all `j \\in I_0`.
      For `i` special, addition by `\\omega_i+Q` permutes `P/Q` and therefore permutes the set of special nodes.
      This permutation extends uniquely to an automorphism of the affine Dynkin diagram.
    - `\\tilde{X}` is mixed -- (that is, not of the above two types) `F` is the trivial group.

    EXAMPLES::

        sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
        sage: F = FundamentalGroupOfExtendedAffineWeylGroup([\'A\',3,1]); F
        Fundamental group of type [\'A\', 3, 1]
        sage: F.cartan_type().dynkin_diagram()
        0
        O-------+
        |       |
        |       |
        O---O---O
        1   2   3
        A3~
        sage: F.special_nodes()
        (0, 1, 2, 3)
        sage: F(1)^2
        pi[2]
        sage: F(1)*F(2)
        pi[3]
        sage: F(3)^(-1)
        pi[1]

        sage: F = FundamentalGroupOfExtendedAffineWeylGroup("B3"); F
        Fundamental group of type [\'B\', 3, 1]
        sage: F.cartan_type().dynkin_diagram()
            O 0
            |
            |
        O---O=>=O
        1   2   3
        B3~
        sage: F.special_nodes()
        (0, 1)

        sage: F = FundamentalGroupOfExtendedAffineWeylGroup("C2"); F
        Fundamental group of type [\'C\', 2, 1]
        sage: F.cartan_type().dynkin_diagram()
        O=>=O=<=O
        0   1   2
        C2~
        sage: F.special_nodes()
        (0, 2)

        sage: F = FundamentalGroupOfExtendedAffineWeylGroup("D4"); F
        Fundamental group of type [\'D\', 4, 1]
        sage: F.cartan_type().dynkin_diagram()
            O 4
            |
            |
        O---O---O
        1   |2  3
            |
            O 0
        D4~
        sage: F.special_nodes()
        (0, 1, 3, 4)
        sage: (F(4), F(4)^2)
        (pi[4], pi[0])

        sage: F = FundamentalGroupOfExtendedAffineWeylGroup("D5"); F
        Fundamental group of type [\'D\', 5, 1]
        sage: F.cartan_type().dynkin_diagram()
          0 O   O 5
            |   |
            |   |
        O---O---O---O
        1   2   3   4
        D5~
        sage: F.special_nodes()
        (0, 1, 4, 5)
        sage: (F(5), F(5)^2, F(5)^3, F(5)^4)
        (pi[5], pi[1], pi[4], pi[0])
        sage: F = FundamentalGroupOfExtendedAffineWeylGroup("E6"); F
        Fundamental group of type [\'E\', 6, 1]
        sage: F.cartan_type().dynkin_diagram()
                O 0
                |
                |
                O 2
                |
                |
        O---O---O---O---O
        1   3   4   5   6
        E6~
        sage: F.special_nodes()
        (0, 1, 6)
        sage: F(1)^2
        pi[6]

        sage: F = FundamentalGroupOfExtendedAffineWeylGroup([\'D\',4,2]); F
        Fundamental group of type [\'C\', 3, 1]^*
        sage: F.cartan_type().dynkin_diagram()
        O=<=O---O=>=O
        0   1   2   3
        C3~*
        sage: F.special_nodes()
        (0, 3)

    We also implement a fundamental group for `GL_n`. It is defined to be the group of integers, which is the
    covering group of the fundamental group Z/nZ for affine `SL_n`::

        sage: F = FundamentalGroupOfExtendedAffineWeylGroup([\'A\',2,1], general_linear=True); F
        Fundamental group of GL(3)
        sage: x = F.an_element(); x
        pi[5]
        sage: x*x
        pi[10]
        sage: x.inverse()
        pi[-5]
        sage: wt = F.cartan_type().classical().root_system().ambient_space().an_element(); wt
        (2, 2, 3)
        sage: x.act_on_classical_ambient(wt)
        (2, 3, 2)
        sage: w = WeylGroup(F.cartan_type(),prefix=\'s\').an_element(); w
        s0*s1*s2
        sage: x.act_on_affine_weyl(w)
        s2*s0*s1
    '''

class FundamentalGroupElement(MultiplicativeGroupElement):
    def __init__(self, parent, x) -> None:
        """
        This should not be called directly.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: x = FundamentalGroupOfExtendedAffineWeylGroup(['A',4,1], prefix='f').an_element()
            sage: TestSuite(x).run()
        """
    def value(self):
        """
        Return the special node which indexes the special automorphism ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',4,1], prefix='f')
            sage: F.special_nodes()
            (0, 1, 2, 3, 4)
            sage: x = F(4); x
            f[4]
            sage: x.value()
            4
        """
    def __invert__(self):
        """
        Return the inverse element of ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: F(1).inverse()   # indirect doctest
            pi[3]
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['E',6,1], prefix='f')
            sage: F(1).inverse()
            f[6]
        """
    def act_on_affine_weyl(self, w):
        """
        Act by ``self`` on the element `w` of the affine Weyl group.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: W = WeylGroup(F.cartan_type(),prefix='s')
            sage: w = W.from_reduced_word([2,3,0])
            sage: F(1).act_on_affine_weyl(w).reduced_word()
            [3, 0, 1]
        """
    def act_on_affine_lattice(self, wt):
        """
        Act by ``self`` on the element ``wt`` of an affine root/weight lattice realization.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: wt = RootSystem(F.cartan_type()).weight_lattice().an_element(); wt
            2*Lambda[0] + 2*Lambda[1] + 3*Lambda[2]
            sage: F(3).act_on_affine_lattice(wt)
            2*Lambda[0] + 3*Lambda[1] + 2*Lambda[3]

        .. WARNING::

            Doesn't work on ambient spaces.
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS:

        Check that :issue:`36121` is fixed::

            sage: W = ExtendedAffineWeylGroup('A4')
            sage: fun = W.fundamental_group().an_element()
            sage: hash(fun) == hash(fun.value())
            True
        """

class FundamentalGroupOfExtendedAffineWeylGroup_Class(UniqueRepresentation, Parent):
    """
    The group of length zero elements in the extended affine Weyl group.
    """
    Element = FundamentalGroupElement
    def __init__(self, cartan_type, prefix, finite: bool = True) -> None:
        """

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: F in Groups().Commutative().Finite()
            True
            sage: TestSuite(F).run()
        """
    @cached_method
    def one(self):
        """
        Return the identity element of the fundamental group.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: F.one()
            pi[0]
        """
    def product(self, x, y):
        """
        Return the product of `x` and `y`.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: F.special_nodes()
            (0, 1, 2, 3)
            sage: F(2)*F(3)
            pi[1]
            sage: F(1)*F(3)^(-1)
            pi[2]
        """
    def cartan_type(self):
        """
        The Cartan type of ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1]).cartan_type()
            ['A', 3, 1]
        """
    def special_nodes(self):
        """
        Return the special nodes of ``self``.

        See :meth:`sage.combinat.root_system.cartan_type.special_nodes()`.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['D',4,1]).special_nodes()
            (0, 1, 3, 4)
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1]).special_nodes()
            (0, 1, 2)
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['C',3,1]).special_nodes()
            (0, 3)
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['D',4,2]).special_nodes()
            (0, 3)
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True).special_nodes()
            Integer Ring
        """
    def group_generators(self):
        """
        Return a tuple of generators of the fundamental group.

        .. WARNING::

            This returns the entire group, a necessary behavior because it
            is used in :meth:`__iter__`.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['E',6,1],prefix='f').group_generators()
            Finite family {0: f[0], 1: f[1], 6: f[6]}
        """
    def __iter__(self):
        """
        Return the iterator for ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['E',6,1],prefix='f')
            sage: [x for x in F] # indirect doctest
            [f[0], f[1], f[6]]
        """
    @cached_method
    def index_set(self):
        """
        The node set of the affine Cartan type of ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1]).index_set()
            (0, 1, 2)
        """
    def action(self, i):
        """
        Return a function which permutes the affine Dynkin node set by the `i`-th special automorphism.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1])
            sage: [[(i, j, F.action(i)(j)) for j in F.index_set()] for i in F.special_nodes()]
            [[(0, 0, 0), (0, 1, 1), (0, 2, 2)], [(1, 0, 1), (1, 1, 2), (1, 2, 0)], [(2, 0, 2), (2, 1, 0), (2, 2, 1)]]
            sage: G = FundamentalGroupOfExtendedAffineWeylGroup(['D',4,1])
            sage: [[(i, j, G.action(i)(j)) for j in G.index_set()] for i in G.special_nodes()]
            [[(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4)], [(1, 0, 1), (1, 1, 0), (1, 2, 2), (1, 3, 4), (1, 4, 3)], [(3, 0, 3), (3, 1, 4), (3, 2, 2), (3, 3, 0), (3, 4, 1)], [(4, 0, 4), (4, 1, 3), (4, 2, 2), (4, 3, 1), (4, 4, 0)]]
        """
    def dual_node(self, i):
        """
        Return the node that indexes the inverse of the `i`-th element.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',4,1])
            sage: [(i, F.dual_node(i)) for i in F.special_nodes()]
            [(0, 0), (1, 4), (2, 3), (3, 2), (4, 1)]
            sage: G = FundamentalGroupOfExtendedAffineWeylGroup(['E',6,1])
            sage: [(i, G.dual_node(i)) for i in G.special_nodes()]
            [(0, 0), (1, 6), (6, 1)]
            sage: H = FundamentalGroupOfExtendedAffineWeylGroup(['D',5,1])
            sage: [(i, H.dual_node(i)) for i in H.special_nodes()]
            [(0, 0), (1, 1), (4, 5), (5, 4)]
        """
    def reduced_word(self, i):
        """
        Return a reduced word for the finite Weyl group element associated with the `i`-th special automorphism.

        More precisely, for each special node `i`, ``self.reduced_word(i)`` is a reduced word for
        the element `v` in the finite Weyl group such that in the extended affine Weyl group,
        the `i`-th special automorphism is equal to `t v` where `t` is a translation element.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',3,1])
            sage: [(i, F.reduced_word(i)) for i in F.special_nodes()]
            [(0, ()), (1, (1, 2, 3)), (2, (2, 1, 3, 2)), (3, (3, 2, 1))]
        """

class FundamentalGroupGLElement(FundamentalGroupElement):
    def act_on_classical_ambient(self, wt):
        """
        Act by ``self`` on the classical ambient weight vector ``wt``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True)
            sage: f = F.an_element(); f
            pi[5]
            sage: la = F.cartan_type().classical().root_system().ambient_space().an_element(); la
            (2, 2, 3)
            sage: f.act_on_classical_ambient(la)
            (2, 3, 2)
        """

class FundamentalGroupGL(FundamentalGroupOfExtendedAffineWeylGroup_Class):
    """
    Fundamental group of `GL_n`. It is just the integers with extra privileges.
    """
    Element = FundamentalGroupGLElement
    def __init__(self, cartan_type, prefix: str = 'pi') -> None:
        """

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True)
            sage: F in Groups().Commutative().Infinite()
            True
            sage: TestSuite(F).run()
        """
    @cached_method
    def one(self):
        """
        Return the identity element of the fundamental group.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True).one()
            pi[0]
        """
    def product(self, x, y):
        """
        Return the product of `x` and `y`.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True)
            sage: F.special_nodes()
            Integer Ring
            sage: F(2)*F(3)
            pi[5]
            sage: F(1)*F(3)^(-1)
            pi[-2]
        """
    def family(self):
        """
        The family associated with the set of special nodes.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: fam = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True).family() # indirect doctest
            sage: fam
            Lazy family (<lambda>(i))_{i in Integer Ring}
            sage: fam[-3]
            -3
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True).some_elements()
            [pi[-2], pi[2], pi[5]]
        """
    def group_generators(self):
        """
        Return group generators for ``self``.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True).group_generators()
            (pi[1],)
        """
    def action(self, i):
        """
        The action of the `i`-th automorphism on the affine Dynkin node set.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True)
            sage: F.action(4)(2)
            0
            sage: F.action(-4)(2)
            1
        """
    def dual_node(self, i):
        """
        The node whose special automorphism is inverse to that of `i`.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True)
            sage: F.dual_node(2)
            -2
        """
    @cached_method
    def reduced_word(self, i):
        """
        A reduced word for the finite permutation part of the
        special automorphism indexed by `i`.

        More precisely, return a reduced word for the finite Weyl group element `u`
        where `i`-th automorphism (expressed in the extended affine Weyl group)
        has the form `t u` where `t` is a translation element.

        EXAMPLES::

            sage: from sage.combinat.root_system.fundamental_group import FundamentalGroupOfExtendedAffineWeylGroup
            sage: F = FundamentalGroupOfExtendedAffineWeylGroup(['A',2,1], general_linear=True)
            sage: F.reduced_word(10)
            (1, 2)
        """
