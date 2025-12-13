from sage.categories.algebras import Algebras as Algebras
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import is_even as is_even
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as RecursivelyEnumeratedSet

class WeylCharacterRing(CombinatorialFreeModule):
    '''
    A class for rings of Weyl characters.

    Let `K` be a compact Lie group, which we assume is semisimple and
    simply-connected. Its complexified Lie algebra `L` is the Lie algebra of a
    complex analytic Lie group `G`. The following three categories are
    equivalent: finite-dimensional representations of `K`; finite-dimensional
    representations of `L`; and finite-dimensional analytic representations of
    `G`. In every case, there is a parametrization of the irreducible
    representations by their highest weight vectors. For this theory of Weyl,
    see (for example):

    * Adams, *Lectures on Lie groups*
    * Broecker and Tom Dieck, *Representations of Compact Lie groups*
    * Bump, *Lie Groups*
    * Fulton and Harris, *Representation Theory*
    * Goodman and Wallach, *Representations and Invariants of the Classical Groups*
    * Hall, *Lie Groups, Lie Algebras and Representations*
    * Humphreys, *Introduction to Lie Algebras and their representations*
    * Procesi, *Lie Groups*
    * Samelson, *Notes on Lie Algebras*
    * Varadarajan, *Lie groups, Lie algebras, and their representations*
    * Zhelobenko, *Compact Lie Groups and their Representations*.

    Computations that you can do with these include computing their
    weight multiplicities, products (thus decomposing the tensor
    product of a representation into irreducibles) and branching
    rules (restriction to a smaller group).

    There is associated with `K`, `L` or `G` as above a lattice, the weight
    lattice, whose elements (called weights) are characters of a Cartan
    subgroup or subalgebra. There is an action of the Weyl group `W` on
    the lattice, and elements of a fixed fundamental domain for `W`, the
    positive Weyl chamber, are called dominant. There is for each
    representation a unique highest dominant weight that occurs with
    nonzero multiplicity with respect to a certain partial order, and
    it is called the highest weight vector.

    EXAMPLES::

        sage: L = RootSystem("A2").ambient_space()
        sage: [fw1,fw2] = L.fundamental_weights()
        sage: R = WeylCharacterRing([\'A\',2], prefix=\'R\')
        sage: [R(1),R(fw1),R(fw2)]
        [R(0,0,0), R(1,0,0), R(1,1,0)]

    Here ``R(1)``, ``R(fw1)``, and ``R(fw2)`` are irreducible representations
    with highest weight vectors `0`, `\\Lambda_1`, and `\\Lambda_2` respectively
    (the first two fundamental weights).

    For type `A` (also `G_2`, `F_4`, `E_6` and `E_7`) we will take as the
    weight lattice not the weight lattice of the semisimple group, but for a
    larger one. For type `A`, this means we are concerned with the
    representation theory of `K = U(n)` or `G = GL(n, \\CC)` rather than `SU(n)`
    or `SU(n, \\CC)`. This is useful since the representation theory of `GL(n)`
    is ubiquitous, and also since we may then represent the fundamental
    weights (in :mod:`sage.combinat.root_system.root_system`) by vectors
    with integer entries. If you are only interested in `SL(3)`, say, use
    ``WeylCharacterRing([\'A\',2])`` as above but be aware that ``R([a,b,c])``
    and ``R([a+1,b+1,c+1])`` represent the same character of `SL(3)` since
    ``R([1,1,1])`` is the determinant.

    For more information, see the thematic tutorial *Lie Methods and
    Related Combinatorics in Sage*, available at:

    https://doc.sagemath.org/html/en/thematic_tutorials/lie.html
    '''
    @staticmethod
    def __classcall__(cls, ct, base_ring=..., prefix=None, style: str = 'lattice', k=None, conjugate: bool = False, cyclotomic_order=None, fusion_labels=None, inject_variables: bool = False):
        '''
        TESTS::

            sage: R = WeylCharacterRing("G2", style=\'coroots\')
            sage: R.cartan_type() is CartanType("G2")
            True
            sage: R.base_ring() is ZZ
            True
        '''
    def __init__(self, ct, base_ring=..., prefix=None, style: str = 'lattice', k=None, conjugate: bool = False, cyclotomic_order=None, fusion_labels=None, inject_variables: bool = False) -> None:
        '''
        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: TestSuite(A2).run()
        '''
    @cached_method
    def ambient(self):
        '''
        Return the weight ring of ``self``.

        EXAMPLES::

            sage: WeylCharacterRing("A2").ambient()
            The Weight ring attached to The Weyl Character Ring of Type A2 with Integer Ring coefficients
        '''
    def lift_on_basis(self, irr):
        '''
        Expand the basis element indexed by the weight ``irr`` into the
        weight ring of ``self``.

        INPUT:

        - ``irr`` -- a dominant weight

        This is used to implement :meth:`lift`.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: v = A2._space([2,1,0]); v
            (2, 1, 0)
            sage: A2.lift_on_basis(v)
            2*a2(1,1,1) + a2(1,2,0) + a2(1,0,2) + a2(2,1,0) + a2(2,0,1) + a2(0,1,2) + a2(0,2,1)

        This is consistent with the analogous calculation with symmetric
        Schur functions::

            sage: s = SymmetricFunctions(QQ).s()
            sage: s[2,1].expand(3)
            x0^2*x1 + x0*x1^2 + x0^2*x2 + 2*x0*x1*x2 + x1^2*x2 + x0*x2^2 + x1*x2^2
        '''
    def demazure_character(self, hwv, word, debug: bool = False):
        '''
        Compute the Demazure character.

        INPUT:

        - ``hwv`` -- a (usually dominant) weight
        - ``word`` -- a Weyl group word

        Produces the Demazure character with highest weight ``hwv`` and
        ``word`` as an element of the weight ring. Only available if
        ``style="coroots"``. The Demazure operators are also available as
        methods of :class:`WeightRing` elements, and as methods of crystals.
        Given a
        :class:`~sage.combinat.crystals.tensor_product.CrystalOfTableaux`
        with given highest weight vector, the Demazure method on the
        crystal will give the equivalent of this method, except that
        the Demazure character of the crystal is given as a sum of
        monomials instead of an element of the :class:`WeightRing`.

        See :meth:`WeightRing.Element.demazure` and
        :meth:`sage.categories.classical_crystals.ClassicalCrystals.ParentMethods.demazure_character`

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2",style=\'coroots\')
            sage: h = sum(A2.fundamental_weights()); h
            (2, 1, 0)
            sage: A2.demazure_character(h,word=[1,2])
            a2(0,0) + a2(-2,1) + a2(2,-1) + a2(1,1) + a2(-1,2)
            sage: A2.demazure_character((1,1),word=[1,2])
            a2(0,0) + a2(-2,1) + a2(2,-1) + a2(1,1) + a2(-1,2)
        '''
    @lazy_attribute
    def lift(self):
        '''
        The embedding of ``self`` into its weight ring.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: A2.lift
            Generic morphism:
              From: The Weyl Character Ring of Type A2 with Integer Ring coefficients
              To:   The Weight ring attached to The Weyl Character Ring of Type A2 with Integer Ring coefficients

        ::

            sage: x = -A2(2,1,1) - A2(2,2,0) + A2(3,1,0)
            sage: A2.lift(x)
            a2(1,3,0) + a2(1,0,3) + a2(3,1,0) + a2(3,0,1) + a2(0,1,3) + a2(0,3,1)

        As a shortcut, you may also do::

            sage: x.lift()
            a2(1,3,0) + a2(1,0,3) + a2(3,1,0) + a2(3,0,1) + a2(0,1,3) + a2(0,3,1)

        Or even::

            sage: a2 = WeightRing(A2)
            sage: a2(x)
            a2(1,3,0) + a2(1,0,3) + a2(3,1,0) + a2(3,0,1) + a2(0,1,3) + a2(0,3,1)
        '''
    @lazy_attribute
    def retract(self):
        '''
        The partial inverse map from the weight ring into ``self``.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: a2 = WeightRing(A2)
            sage: A2.retract
            Generic morphism:
              From: The Weight ring attached to The Weyl Character Ring of Type A2 with Integer Ring coefficients
              To:   The Weyl Character Ring of Type A2 with Integer Ring coefficients

        ::

            sage: v = A2._space([3,1,0]); v
            (3, 1, 0)
            sage: chi = a2.sum_of_monomials(v.orbit()); chi
            a2(1,3,0) + a2(1,0,3) + a2(3,1,0) + a2(3,0,1) + a2(0,1,3) + a2(0,3,1)
            sage: A2.retract(chi)
            -A2(2,1,1) - A2(2,2,0) + A2(3,1,0)

        The input should be invariant::

            sage: A2.retract(a2.monomial(v))
            Traceback (most recent call last):
            ...
            ValueError: multiplicity dictionary may not be Weyl group invariant

        As a shortcut, you may use conversion::

            sage: A2(chi)
            -A2(2,1,1) - A2(2,2,0) + A2(3,1,0)
            sage: A2(a2.monomial(v))
            Traceback (most recent call last):
            ...
            ValueError: multiplicity dictionary may not be Weyl group invariant
        '''
    def __call__(self, *args):
        '''
        Construct an element of ``self``.

        The input can either be an object that can be coerced or
        converted into ``self`` (an element of ``self``, of the base
        ring, of the weight ring), or a dominant weight. In the later
        case, the basis element indexed by that weight is returned.

        To specify the weight, you may give it explicitly. Alternatively,
        you may give a tuple of integers. Normally these are the
        components of the vector in the standard realization of
        the weight lattice as a vector space. Alternatively, if
        the ring is constructed with ``style = "coroots"``, you may
        specify the weight by giving a set of integers, one for each
        fundamental weight; the weight is then the linear combination
        of the fundamental weights with these coefficients.

        As a syntactical shorthand, for tuples of length at least two,
        the parenthesis may be omitted.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: [A2(x) for x in [-2,-1,0,1,2]]
            [-2*A2(0,0,0), -A2(0,0,0), 0, A2(0,0,0), 2*A2(0,0,0)]
            sage: [A2(2,1,0), A2([2,1,0]), A2(2,1,0)== A2([2,1,0])]
            [A2(2,1,0), A2(2,1,0), True]
            sage: A2([2,1,0]) == A2(2,1,0)
            True
            sage: l = -2*A2(0,0,0) - A2(1,0,0) + A2(2,0,0) + 2*A2(3,0,0)
            sage: [l in A2, A2(l) == l]
            [True, True]
            sage: P.<q> = QQ[]
            sage: A2 = WeylCharacterRing([\'A\',2], base_ring = P)
            sage: [A2(x) for x in [-2,-1,0,1,2,-2*q,-q,q,2*q,(1-q)]]
            [-2*A2(0,0,0), -A2(0,0,0), 0, A2(0,0,0), 2*A2(0,0,0), -2*q*A2(0,0,0), -q*A2(0,0,0),
            q*A2(0,0,0), 2*q*A2(0,0,0), (-q+1)*A2(0,0,0)]
            sage: R.<q> = ZZ[]
            sage: A2 = WeylCharacterRing([\'A\',2], base_ring = R, style=\'coroots\')
            sage: q*A2(1)
            q*A2(0,0)
            sage: [A2(x) for x in [-2,-1,0,1,2,-2*q,-q,q,2*q,(1-q)]]
            [-2*A2(0,0), -A2(0,0), 0, A2(0,0), 2*A2(0,0), -2*q*A2(0,0), -q*A2(0,0), q*A2(0,0), 2*q*A2(0,0), (-q+1)*A2(0,0)]
        '''
    def product_on_basis(self, a, b):
        """
        Compute the tensor product of two irreducible representations ``a``
        and ``b``.

        EXAMPLES::

            sage: D4 = WeylCharacterRing(['D',4])
            sage: spin_plus = D4(1/2,1/2,1/2,1/2)
            sage: spin_minus = D4(1/2,1/2,1/2,-1/2)
            sage: spin_plus * spin_minus # indirect doctest
            D4(1,0,0,0) + D4(1,1,1,0)
            sage: spin_minus * spin_plus
            D4(1,0,0,0) + D4(1,1,1,0)

        Uses the Brauer-Klimyk method.
        """
    def dot_reduce(self, a):
        '''
        Auxiliary function for :meth:`product_on_basis`.

        Return a pair `[\\epsilon, b]` where `b` is a dominant weight and
        `\\epsilon` is 0, 1 or -1. To describe `b`, let `w` be an element of
        the Weyl group such that `w(a + \\rho)` is dominant. If
        `w(a + \\rho) - \\rho` is dominant, then `\\epsilon` is the sign of
        `w` and `b` is `w(a + \\rho) - \\rho`. Otherwise, `\\epsilon` is zero.

        INPUT:

        - ``a`` -- a weight

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: weights = sorted(A2(2,1,0).weight_multiplicities().keys(), key=str); weights
            [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
            sage: [A2.dot_reduce(x) for x in weights]
            [[0, (0, 0, 0)], [-1, (1, 1, 1)], [-1, (1, 1, 1)], [1, (1, 1, 1)], [0, (0, 0, 0)], [0, (0, 0, 0)], [1, (2, 1, 0)]]
        '''
    def affine_reflect(self, wt, k: int = 0):
        '''
        Return the reflection of wt in the hyperplane `\\theta`.

        Optionally, this also shifts by a multiple `k` of `\\theta`.

        INPUT:

        - ``wt`` -- a weight
        - ``k`` -- (optional) a positive integer

        EXAMPLES::

            sage: B22 = FusionRing("B2",2)
            sage: fw = B22.fundamental_weights(); fw
            Finite family {1: (1, 0), 2: (1/2, 1/2)}
            sage: [B22.affine_reflect(x,2) for x in fw]
            [(2, 1), (3/2, 3/2)]
        '''
    def some_elements(self):
        '''
        Return some elements of ``self``.

        EXAMPLES::

            sage: WeylCharacterRing("A3").some_elements()
            [A3(1,0,0,0), A3(1,1,0,0), A3(1,1,1,0)]
        '''
    def one_basis(self):
        '''
        Return the index of 1 in ``self``.

        EXAMPLES::

            sage: WeylCharacterRing("A3").one_basis()
            (0, 0, 0, 0)
            sage: WeylCharacterRing("A3").one()
            A3(0,0,0,0)
        '''
    def base_ring(self):
        """
        Return the base ring of ``self``.

        EXAMPLES::

            sage: R = WeylCharacterRing(['A',3], base_ring = CC); R.base_ring()
            Complex Field with 53 bits of precision
        """
    def irr_repr(self, hwv):
        '''
        Return a string representing the irreducible character with highest
        weight vector ``hwv``.

        EXAMPLES::

            sage: B3 = WeylCharacterRing("B3")
            sage: [B3.irr_repr(v) for v in B3.fundamental_weights()]
            [\'B3(1,0,0)\', \'B3(1,1,0)\', \'B3(1/2,1/2,1/2)\']
            sage: B3 = WeylCharacterRing("B3", style=\'coroots\')
            sage: [B3.irr_repr(v) for v in B3.fundamental_weights()]
            [\'B3(1,0,0)\', \'B3(0,1,0)\', \'B3(0,0,1)\']
        '''
    def level(self, wt):
        '''
        Return the level of the weight, defined to be the value of
        the weight on the coroot associated with the highest root.

        EXAMPLES::

            sage: R = FusionRing("F4",2); [R.level(x) for x in R.fundamental_weights()]
            [2, 3, 2, 1]
            sage: [CartanType("F4~").dual().a()[x] for x in [1..4]]
            [2, 3, 2, 1]
        '''
    def cartan_type(self):
        '''
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: WeylCharacterRing("A2").cartan_type()
            [\'A\', 2]
        '''
    def fundamental_weights(self):
        '''
        Return the fundamental weights.

        EXAMPLES::

            sage: WeylCharacterRing("G2").fundamental_weights()
            Finite family {1: (1, 0, -1), 2: (2, -1, -1)}
        '''
    def simple_roots(self):
        '''
        Return the simple roots.

        EXAMPLES::

            sage: WeylCharacterRing("G2").simple_roots()
            Finite family {1: (0, 1, -1), 2: (1, -2, 1)}
        '''
    def simple_coroots(self):
        '''
        Return the simple coroots.

        EXAMPLES::

            sage: WeylCharacterRing("G2").simple_coroots()
            Finite family {1: (0, 1, -1), 2: (1/3, -2/3, 1/3)}
        '''
    def highest_root(self):
        '''
        Return the highest root.

        EXAMPLES::

            sage: WeylCharacterRing("G2").highest_root()
             (2, -1, -1)
        '''
    def positive_roots(self):
        '''
        Return the positive roots.

        EXAMPLES::

            sage: WeylCharacterRing("G2").positive_roots()
            [(0, 1, -1), (1, -2, 1), (1, -1, 0), (1, 0, -1), (1, 1, -2), (2, -1, -1)]
        '''
    def dynkin_diagram(self):
        '''
        Return the Dynkin diagram of ``self``.

        EXAMPLES::

            sage: WeylCharacterRing("E7").dynkin_diagram()
                    O 2
                    |
                    |
            O---O---O---O---O---O
            1   3   4   5   6   7
            E7
        '''
    def extended_dynkin_diagram(self):
        '''
        Return the extended Dynkin diagram, which is the Dynkin diagram
        of the corresponding untwisted affine type.

        EXAMPLES::

            sage: WeylCharacterRing("E7").extended_dynkin_diagram()
                        O 2
                        |
                        |
            O---O---O---O---O---O---O
            0   1   3   4   5   6   7
            E7~
        '''
    def rank(self):
        '''
        Return the rank.

        EXAMPLES::

            sage: WeylCharacterRing("G2").rank()
            2
        '''
    def space(self):
        """
        Return the weight space associated to ``self``.

        EXAMPLES::

            sage: WeylCharacterRing(['E',8]).space()
            Ambient space of the Root system of type ['E', 8]
        """
    def char_from_weights(self, mdict):
        '''
        Construct a Weyl character from an invariant linear combination
        of weights.

        INPUT:

        - ``mdict`` -- dictionary mapping weights to coefficients,
          and representing a linear combination of weights which
          shall be invariant under the action of the Weyl group

        OUTPUT: the corresponding Weyl character

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: v = A2._space([3,1,0]); v
            (3, 1, 0)
            sage: d = dict([(x,1) for x in v.orbit()]); d
            {(1, 3, 0): 1,
             (1, 0, 3): 1,
             (3, 1, 0): 1,
             (3, 0, 1): 1,
             (0, 1, 3): 1,
             (0, 3, 1): 1}
            sage: A2.char_from_weights(d)
            -A2(2,1,1) - A2(2,2,0) + A2(3,1,0)
        '''
    def adjoint_representation(self):
        '''
        Return the adjoint representation as an element of the WeylCharacterRing.

        EXAMPLES::

            sage: G2 = WeylCharacterRing("G2",style=\'coroots\')
            sage: G2.adjoint_representation()
            G2(0,1)
        '''
    def maximal_subgroups(self):
        '''
        This method is only available if the Cartan type of
        ``self`` is irreducible and of rank no greater than 8.
        This method produces a list of the maximal subgroups
        of ``self``, up to (possibly outer) automorphisms. Each line
        in the output gives the Cartan type of a maximal subgroup
        followed by a command that creates the branching rule.

        EXAMPLES::

            sage: WeylCharacterRing("E6").maximal_subgroups()
            D5:branching_rule("E6","D5","levi")
            C4:branching_rule("E6","C4","symmetric")
            F4:branching_rule("E6","F4","symmetric")
            A2:branching_rule("E6","A2","miscellaneous")
            G2:branching_rule("E6","G2","miscellaneous")
            A2xG2:branching_rule("E6","A2xG2","miscellaneous")
            A1xA5:branching_rule("E6","A1xA5","extended")
            A2xA2xA2:branching_rule("E6","A2xA2xA2","extended")

        Note that there are other embeddings of (for example
        `A_2` into `E_6` as nonmaximal subgroups. These
        embeddings may be constructed by composing branching
        rules through various subgroups.

        Once you know which maximal subgroup you are interested
        in, to create the branching rule, you may either
        paste the command to the right of the colon from the
        above output onto the command line, or alternatively
        invoke the related method :meth:`maximal_subgroup`::

            sage: branching_rule("E6","G2","miscellaneous")
            miscellaneous branching rule E6 => G2
            sage: WeylCharacterRing("E6").maximal_subgroup("G2")
            miscellaneous branching rule E6 => G2

        It is believed that the list of maximal subgroups is complete, except that some
        subgroups may be not be invariant under outer automorphisms. It is reasonable
        to want a list of maximal subgroups that is complete up to conjugation,
        but to obtain such a list you may have to apply outer automorphisms.
        The group of outer automorphisms modulo inner automorphisms is isomorphic
        to the group of symmetries of the Dynkin diagram, and these are available
        as branching rules. The following example shows that while
        a branching rule from `D_4` to `A_1\\times C_2` is supplied,
        another different one may be obtained by composing it with the
        triality automorphism of `D_4`::

            sage: [D4,A1xC2]=[WeylCharacterRing(x,style=\'coroots\') for x in ["D4","A1xC2"]]
            sage: fw = D4.fundamental_weights()
            sage: b = D4.maximal_subgroup("A1xC2")
            sage: [D4(fw).branch(A1xC2,rule=b) for fw in D4.fundamental_weights()]
            [A1xC2(1,1,0),
            A1xC2(2,0,0) + A1xC2(2,0,1) + A1xC2(0,2,0),
            A1xC2(1,1,0),
            A1xC2(2,0,0) + A1xC2(0,0,1)]
            sage: b1 = branching_rule("D4","D4","triality")*b
            sage: [D4(fw).branch(A1xC2,rule=b1) for fw in D4.fundamental_weights()]
            [A1xC2(1,1,0),
            A1xC2(2,0,0) + A1xC2(2,0,1) + A1xC2(0,2,0),
            A1xC2(2,0,0) + A1xC2(0,0,1),
            A1xC2(1,1,0)]
        '''
    def maximal_subgroup(self, ct):
        '''
        Return a branching rule or a list of branching rules.

        INPUT:

        - ``ct`` -- the Cartan type of a maximal subgroup of ``self``

        In rare cases where there is
        more than one maximal subgroup (up to outer automorphisms)
        with the given Cartan type, the function returns a list of
        branching rules.

        EXAMPLES::

            sage: WeylCharacterRing("E7").maximal_subgroup("A2")
            miscellaneous branching rule E7 => A2
            sage: WeylCharacterRing("E7").maximal_subgroup("A1")
            [iii branching rule E7 => A1, iv branching rule E7 => A1]

        For more information, see the related method :meth:`maximal_subgroups`.
        '''
    class Element(CombinatorialFreeModule.Element):
        """
        A class for Weyl characters.
        """
        def cartan_type(self):
            '''
            Return the Cartan type of ``self``.

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2")
                sage: A2([1,0,0]).cartan_type()
                [\'A\', 2]
            '''
        def degree(self):
            """
            Return the degree of ``self``.

            This is the dimension of the associated module.

            EXAMPLES::

                sage: B3 = WeylCharacterRing(['B',3])
                sage: [B3(x).degree() for x in B3.fundamental_weights()]
                [7, 21, 8]
            """
        def branch(self, S, rule: str = 'default'):
            """
            Return the restriction of the character to the subalgebra.

            If no rule is specified, we will try to specify one.

            INPUT:

            - ``S`` -- a Weyl character ring for a Lie subgroup or subalgebra

            - ``rule`` -- a branching rule

            See :func:`~sage.combinat.root_system.branching_rules.branch_weyl_character`
            for more information about branching rules.

            EXAMPLES::

                sage: B3 = WeylCharacterRing(['B',3])
                sage: A2 = WeylCharacterRing(['A',2])
                sage: [B3(w).branch(A2,rule='levi') for w in B3.fundamental_weights()]
                [A2(0,0,0) + A2(1,0,0) + A2(0,0,-1),
                A2(0,0,0) + A2(1,0,0) + A2(1,1,0) + A2(1,0,-1) + A2(0,-1,-1) + A2(0,0,-1),
                A2(-1/2,-1/2,-1/2) + A2(1/2,-1/2,-1/2) + A2(1/2,1/2,-1/2) + A2(1/2,1/2,1/2)]
            """
        def dual(self):
            '''
            The involution that replaces a representation with
            its contragredient. (For Fusion rings, this is the
            conjugation map.)

            EXAMPLES::

                sage: A3 = WeylCharacterRing("A3", style=\'coroots\')
                sage: A3(1,0,0)^2
                A3(0,1,0) + A3(2,0,0)
                sage: (A3(1,0,0)^2).dual()
                A3(0,1,0) + A3(0,0,2)
            '''
        def highest_weight(self):
            '''
            Return the parametrizing dominant weight
            of an irreducible character.

            This method is only available for basis elements.

            EXAMPLES::

                sage: G2 = WeylCharacterRing("G2", style=\'coroots\')
                sage: [x.highest_weight() for x in [G2(1,0),G2(0,1)]]
                [(1, 0, -1), (2, -1, -1)]
            '''
        def __pow__(self, n):
            '''
            Return the `n`-th power of ``self``.

            We override the method in :mod:`sage.monoids.monoids` since
            using the Brauer-Klimyk algorithm, it is more efficient to
            compute ``a*(a*(a*a))`` than ``(a*a)*(a*a)``.

            EXAMPLES::

                sage: B4 = WeylCharacterRing("B4",style=\'coroots\')
                sage: spin = B4(0,0,0,1)
                sage: [spin^k for k in [0,1,3]]
                [B4(0,0,0,0), B4(0,0,0,1), 5*B4(0,0,0,1) + 4*B4(1,0,0,1) + 3*B4(0,1,0,1) + 2*B4(0,0,1,1) + B4(0,0,0,3)]
                sage: spin^-1
                Traceback (most recent call last):
                ...
                ValueError: cannot invert self (= B4(0,0,0,1))
                sage: x = 2 * B4.one(); x
                2*B4(0,0,0,0)
                sage: x^-3
                1/8*B4(0,0,0,0)
            '''
        def is_irreducible(self):
            """
            Return whether ``self`` is an irreducible character.

            EXAMPLES::

                sage: B3 = WeylCharacterRing(['B',3])
                sage: [B3(x).is_irreducible() for x in B3.fundamental_weights()]
                [True, True, True]
                sage: sum(B3(x) for x in B3.fundamental_weights()).is_irreducible()
                False
            """
        @cached_method
        def symmetric_power(self, k):
            '''
            Return the `k`-th symmetric power of ``self``.

            INPUT:

            - ``k`` -- nonnegative integer

            The algorithm is based on the
            identity `k h_k = \\sum_{r=1}^k p_k h_{k-r}` relating the power-sum
            and complete symmetric polynomials. Applying this to the
            eigenvalues of an element of the parent Lie group in the
            representation ``self``, the `h_k` become symmetric powers and
            the `p_k` become Adams operations, giving an efficient recursive
            implementation.

            EXAMPLES::

                sage: B3 = WeylCharacterRing("B3",style=\'coroots\')
                sage: spin = B3(0,0,1)
                sage: spin.symmetric_power(6)
                B3(0,0,0) + B3(0,0,2) + B3(0,0,4) + B3(0,0,6)
            '''
        @cached_method
        def exterior_power(self, k):
            '''
            Return the `k`-th exterior power of ``self``.

            INPUT:

            - ``k`` -- nonnegative integer

            The algorithm is based on the
            identity `k e_k = \\sum_{r=1}^k (-1)^{k-1} p_k e_{k-r}` relating the
            power-sum and elementary symmetric polynomials. Applying this to
            the eigenvalues of an element of the parent Lie group in the
            representation ``self``, the `e_k` become exterior powers and
            the `p_k` become Adams operations, giving an efficient recursive
            implementation.

            EXAMPLES::

                sage: B3 = WeylCharacterRing("B3",style=\'coroots\')
                sage: spin = B3(0,0,1)
                sage: spin.exterior_power(6)
                B3(1,0,0) + B3(0,1,0)
            '''
        def adams_operator(self, r):
            '''
            Return the `r`-th Adams operation of ``self``.

            INPUT:

            - ``r`` -- positive integer

            This is a virtual character,
            whose weights are the weights of ``self``, each multiplied by `r`.

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2")
                sage: A2(1,1,0).adams_operator(3)
                A2(2,2,2) - A2(3,2,1) + A2(3,3,0)
            '''
        adams_operation = adams_operator
        def symmetric_square(self):
            '''
            Return the symmetric square of the character.

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2",style=\'coroots\')
                sage: A2(1,0).symmetric_square()
                A2(2,0)
            '''
        def exterior_square(self):
            '''
            Return the exterior square of the character.

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2",style=\'coroots\')
                sage: A2(1,0).exterior_square()
                A2(0,1)
            '''
        def frobenius_schur_indicator(self):
            '''
            Return:

            - `1` if the representation is real (orthogonal)

            - `-1` if the representation is quaternionic (symplectic)

            - `0` if the representation is complex (not self dual)

            The Frobenius-Schur indicator of a character `\\chi`
            of a compact group `G` is the Haar integral over the
            group of `\\chi(g^2)`. Its value is 1, -1 or 0. This
            method computes it for irreducible characters of
            compact Lie groups by checking whether the symmetric
            and exterior square characters contain the trivial
            character.

            .. TODO::

                Try to compute this directly without actually calculating
                the full symmetric and exterior squares.

            EXAMPLES::

                sage: B2 = WeylCharacterRing("B2",style=\'coroots\')
                sage: B2(1,0).frobenius_schur_indicator()
                 1
                sage: B2(0,1).frobenius_schur_indicator()
                 -1
            '''
        def weight_multiplicities(self):
            '''
            Return the dictionary of weight multiplicities for the Weyl
            character ``self``.

            The character does not have to be irreducible.

            EXAMPLES::

                sage: B2 = WeylCharacterRing("B2",style=\'coroots\')
                sage: B2(0,1).weight_multiplicities()
                {(-1/2, -1/2): 1, (-1/2, 1/2): 1, (1/2, -1/2): 1, (1/2, 1/2): 1}
            '''
        def inner_product(self, other):
            '''
            Compute the inner product with another character.

            The irreducible characters are an orthonormal basis with respect
            to the usual inner product of characters, interpreted as functions
            on a compact Lie group, by Schur orthogonality.

            INPUT:

            - ``other`` -- another character

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2")
                sage: [f1,f2] = A2.fundamental_weights()
                sage: r1 = A2(f1)*A2(f2); r1
                A2(1,1,1) + A2(2,1,0)
                sage: r2 = A2(f1)^3; r2
                A2(1,1,1) + 2*A2(2,1,0) + A2(3,0,0)
                sage: r1.inner_product(r2)
                3
            '''
        def invariant_degree(self):
            '''
            Return the multiplicity of the trivial representation in ``self``.

            Multiplicities of other irreducibles may be obtained
            using :meth:`multiplicity`.

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2",style=\'coroots\')
                sage: rep = A2(1,0)^2*A2(0,1)^2; rep
                2*A2(0,0) + A2(0,3) + 4*A2(1,1) + A2(3,0) + A2(2,2)
                sage: rep.invariant_degree()
                2
            '''
        def multiplicity(self, other):
            '''
            Return the multiplicity of the irreducible ``other`` in ``self``.

            INPUT:

            - ``other`` -- an irreducible character

            EXAMPLES::

                sage: B2 = WeylCharacterRing("B2",style=\'coroots\')
                sage: rep = B2(1,1)^2; rep
                B2(0,0) + B2(1,0) + 2*B2(0,2) + B2(2,0) + 2*B2(1,2) + B2(0,4) + B2(3,0) + B2(2,2)
                sage: rep.multiplicity(B2(0,2))
                2
            '''

def irreducible_character_freudenthal(hwv, debug: bool = False):
    '''
    Return the dictionary of multiplicities for the irreducible
    character with highest weight `\\lambda`.

    The weight multiplicities are computed by the Freudenthal multiplicity
    formula. The algorithm is based on recursion relation that is stated,
    for example, in Humphrey\'s book on Lie Algebras. The multiplicities are
    invariant under the Weyl group, so to compute them it would be sufficient
    to compute them for the weights in the positive Weyl chamber. However
    after some testing it was found to be faster to compute every
    weight using the recursion, since the use of the Weyl group is
    expensive in its current implementation.

    INPUT:

    - ``hwv`` -- a dominant weight in a weight lattice

    - ``L`` -- the ambient space

    EXAMPLES::

        sage: WeylCharacterRing("A2")(2,1,0).weight_multiplicities() # indirect doctest
        {(1, 1, 1): 2, (1, 2, 0): 1, (1, 0, 2): 1, (2, 1, 0): 1,
         (2, 0, 1): 1, (0, 1, 2): 1, (0, 2, 1): 1}
    '''

class WeightRing(CombinatorialFreeModule):
    """
    The weight ring, which is the group algebra over a weight lattice.

    A Weyl character may be regarded as an element of the weight ring.
    In fact, an element of the weight ring is an element of the
    :class:`Weyl character ring <WeylCharacterRing>` if and only if it is
    invariant under the action of the Weyl group.

    The advantage of the weight ring over the Weyl character ring
    is that one may conduct calculations in the weight ring that
    involve sums of weights that are not Weyl group invariant.

    EXAMPLES::

        sage: A2 = WeylCharacterRing(['A',2])
        sage: a2 = WeightRing(A2)
        sage: wd = prod(a2(x/2)-a2(-x/2) for x in a2.space().positive_roots()); wd
        a2(-1,1,0) - a2(-1,0,1) - a2(1,-1,0) + a2(1,0,-1) + a2(0,-1,1) - a2(0,1,-1)
        sage: chi = A2([5,3,0]); chi
        A2(5,3,0)
        sage: a2(chi)
        a2(1,2,5) + 2*a2(1,3,4) + 2*a2(1,4,3) + a2(1,5,2) + a2(2,1,5)
        + 2*a2(2,2,4) + 3*a2(2,3,3) + 2*a2(2,4,2) + a2(2,5,1) + 2*a2(3,1,4)
        + 3*a2(3,2,3) + 3*a2(3,3,2) + 2*a2(3,4,1) + a2(3,5,0) + a2(3,0,5)
        + 2*a2(4,1,3) + 2*a2(4,2,2) + 2*a2(4,3,1) + a2(4,4,0) + a2(4,0,4)
        + a2(5,1,2) + a2(5,2,1) + a2(5,3,0) + a2(5,0,3) + a2(0,3,5)
        + a2(0,4,4) + a2(0,5,3)
        sage: a2(chi)*wd
        -a2(-1,3,6) + a2(-1,6,3) + a2(3,-1,6) - a2(3,6,-1) - a2(6,-1,3) + a2(6,3,-1)
        sage: sum((-1)^w.length()*a2([6,3,-1]).weyl_group_action(w) for w in a2.space().weyl_group())
        -a2(-1,3,6) + a2(-1,6,3) + a2(3,-1,6) - a2(3,6,-1) - a2(6,-1,3) + a2(6,3,-1)
        sage: a2(chi)*wd == sum((-1)^w.length()*a2([6,3,-1]).weyl_group_action(w) for w in a2.space().weyl_group())
        True
    """
    @staticmethod
    def __classcall__(cls, parent, prefix=None):
        '''
        TESTS::

            sage: A3 = WeylCharacterRing("A3", style=\'coroots\')
            sage: a3 = WeightRing(A3)
            sage: a3.cartan_type(), a3.base_ring(), a3.parent()
            ([\'A\', 3], Integer Ring, The Weyl Character Ring of Type A3 with Integer Ring coefficients)
        '''
    def __init__(self, parent, prefix) -> None:
        '''
        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: a2 = WeightRing(A2)
            sage: TestSuite(a2).run()

        TESTS::

            sage: A1xA1 = WeylCharacterRing("A1xA1")
            sage: a1xa1 = WeightRing(A1xA1)
            sage: TestSuite(a1xa1).run()
            sage: a1xa1.an_element()
            a1xa1(2,2,3,0)
        '''
    def __call__(self, *args):
        """
        Construct an element of ``self``.

        The input can either be an object that can be coerced or
        converted into ``self`` (an element of ``self``, of the base
        ring, of the weight ring), or a dominant weight. In the later
        case, the basis element indexed by that weight is returned.

        To specify the weight, you may give it explicitly. Alternatively,
        you may give a tuple of integers. Normally these are the
        components of the vector in the standard realization of
        the weight lattice as a vector space. Alternatively, if
        the ring is constructed with style='coroots', you may
        specify the weight by giving a set of integers, one for each
        fundamental weight; the weight is then the linear combination
        of the fundamental weights with these coefficients.

        As a syntactical shorthand, for tuples of length at least two,
        the parenthesis may be omitted.

        EXAMPLES::

            sage: a2 = WeightRing(WeylCharacterRing(['A',2]))
            sage: a2(-1)
            -a2(0,0,0)
        """
    def product_on_basis(self, a, b):
        '''
        Return the product of basis elements indexed by ``a`` and ``b``.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: a2 = WeightRing(A2)
            sage: a2(1,0,0) * a2(0,1,0) # indirect doctest
            a2(1,1,0)
        '''
    def some_elements(self):
        '''
        Return some elements of ``self``.

        EXAMPLES::

            sage: A3 = WeylCharacterRing("A3")
            sage: a3 = WeightRing(A3)
            sage: a3.some_elements()
            [a3(1,0,0,0), a3(1,1,0,0), a3(1,1,1,0)]
        '''
    def one_basis(self):
        '''
        Return the index of `1`.

        EXAMPLES::

            sage: A3 = WeylCharacterRing("A3")
            sage: WeightRing(A3).one_basis()
            (0, 0, 0, 0)
            sage: WeightRing(A3).one()
            a3(0,0,0,0)
        '''
    def parent(self):
        '''
        Return the parent Weyl character ring.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: a2 = WeightRing(A2)
            sage: a2.parent()
            The Weyl Character Ring of Type A2 with Integer Ring coefficients
            sage: a2.parent() == A2
            True
        '''
    def weyl_character_ring(self):
        '''
        Return the parent Weyl Character Ring.

        A synonym for ``self.parent()``.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: a2 = WeightRing(A2)
            sage: a2.weyl_character_ring()
            The Weyl Character Ring of Type A2 with Integer Ring coefficients
        '''
    def cartan_type(self):
        '''
        Return the Cartan type.

        EXAMPLES::

            sage: A2 = WeylCharacterRing("A2")
            sage: WeightRing(A2).cartan_type()
            [\'A\', 2]
        '''
    def space(self):
        """
        Return the weight space realization associated to ``self``.

        EXAMPLES::

            sage: E8 = WeylCharacterRing(['E',8])
            sage: e8 = WeightRing(E8)
            sage: e8.space()
            Ambient space of the Root system of type ['E', 8]
        """
    def fundamental_weights(self):
        '''
        Return the fundamental weights.

        EXAMPLES::

            sage: WeightRing(WeylCharacterRing("G2")).fundamental_weights()
            Finite family {1: (1, 0, -1), 2: (2, -1, -1)}
        '''
    def simple_roots(self):
        '''
        Return the simple roots.

        EXAMPLES::

            sage: WeightRing(WeylCharacterRing("G2")).simple_roots()
            Finite family {1: (0, 1, -1), 2: (1, -2, 1)}
        '''
    def positive_roots(self):
        '''
        Return the positive roots.

        EXAMPLES::

            sage: WeightRing(WeylCharacterRing("G2")).positive_roots()
            [(0, 1, -1), (1, -2, 1), (1, -1, 0), (1, 0, -1), (1, 1, -2), (2, -1, -1)]
        '''
    def wt_repr(self, wt):
        '''
        Return a string representing the irreducible character with
        highest weight vector ``wt``.

        Uses coroot notation if the associated
        Weyl character ring is defined with ``style="coroots"``.

        EXAMPLES::

            sage: G2 = WeylCharacterRing("G2")
            sage: [G2.ambient().wt_repr(x) for x in G2.fundamental_weights()]
            [\'g2(1,0,-1)\', \'g2(2,-1,-1)\']
            sage: G2 = WeylCharacterRing("G2",style=\'coroots\')
            sage: [G2.ambient().wt_repr(x) for x in G2.fundamental_weights()]
            [\'g2(1,0)\', \'g2(0,1)\']
        '''
    class Element(CombinatorialFreeModule.Element):
        """
        A class for weight ring elements.
        """
        def cartan_type(self):
            '''
            Return the Cartan type.

            EXAMPLES::

                sage: A2 = WeylCharacterRing("A2")
                sage: a2 = WeightRing(A2)
                sage: a2([0,1,0]).cartan_type()
                [\'A\', 2]
            '''
        def weyl_group_action(self, w):
            """
            Return the action of the Weyl group element ``w`` on ``self``.

            EXAMPLES::

                sage: G2 = WeylCharacterRing(['G',2])
                sage: g2 = WeightRing(G2)
                sage: L = g2.space()
                sage: [fw1, fw2] = L.fundamental_weights()
                sage: sum(g2(fw2).weyl_group_action(w) for w in L.weyl_group())
                2*g2(-2,1,1) + 2*g2(-1,-1,2) + 2*g2(-1,2,-1) + 2*g2(1,-2,1) + 2*g2(1,1,-2) + 2*g2(2,-1,-1)
            """
        def character(self):
            """
            Assuming that ``self`` is invariant under the Weyl group, this will
            express it as a linear combination of characters. If ``self`` is
            not Weyl group invariant, this method will not terminate.

            EXAMPLES::

                sage: A2 = WeylCharacterRing(['A',2])
                sage: a2 = WeightRing(A2)
                sage: W = a2.space().weyl_group()
                sage: mu = a2(2,1,0)
                sage: nu = sum(mu.weyl_group_action(w) for w in W) ; nu
                a2(1,2,0) + a2(1,0,2) + a2(2,1,0) + a2(2,0,1) + a2(0,1,2) + a2(0,2,1)
                sage: nu.character()
                -2*A2(1,1,1) + A2(2,1,0)
            """
        def scale(self, k):
            '''
            Multiply a weight by `k`.

            The operation is extended by linearity to the weight ring.

            INPUT:

            - ``k`` -- nonzero integer

            EXAMPLES::

                sage: g2 = WeylCharacterRing("G2",style=\'coroots\').ambient()
                sage: g2(2,3).scale(2)
                g2(4,6)
            '''
        def shift(self, mu):
            '''
            Add `\\mu` to any weight.

            Extended by linearity to the weight ring.

            INPUT:

            - ``mu`` -- a weight

            EXAMPLES::

                sage: g2 = WeylCharacterRing("G2",style=\'coroots\').ambient()
                sage: [g2(1,2).shift(fw) for fw in g2.fundamental_weights()]
                [g2(2,2), g2(1,3)]
            '''
        def demazure(self, w, debug: bool = False):
            '''
            Return the result of applying the Demazure operator `\\partial_w`
            to ``self``.

            INPUT:

            - ``w`` -- a Weyl group element, or its reduced word

            If `w = s_i` is a simple reflection, the operation `\\partial_w`
            sends the weight `\\lambda` to

            .. MATH::

                \\frac{\\lambda - s_i \\cdot \\lambda + \\alpha_i}{1 + \\alpha_i},

            where the numerator is divisible the denominator in the weight
            ring. This is extended by multiplicativity to all `w` in the
            Weyl group.

            EXAMPLES::

                sage: B2 = WeylCharacterRing("B2",style=\'coroots\')
                sage: b2 = WeightRing(B2)
                sage: b2(1,0).demazure([1])
                b2(1,0) + b2(-1,2)
                sage: b2(1,0).demazure([2])
                b2(1,0)
                sage: r = b2(1,0).demazure([1,2]); r
                b2(1,0) + b2(-1,2)
                sage: r.demazure([1])
                b2(1,0) + b2(-1,2)
                sage: r.demazure([2])
                b2(0,0) + b2(1,0) + b2(1,-2) + b2(-1,2)
            '''
        def demazure_lusztig(self, i, v):
            '''
            Return the result of applying the Demazure-Lusztig operator
            `T_i` to ``self``.

            INPUT:

            - ``i`` -- an element of the index set (or a reduced word or
              Weyl group element)
            - ``v`` -- an element of the base ring

            If `R` is the parent WeightRing, the Demazure-Lusztig operator
            `T_i` is the linear map `R \\to R` that sends (for a weight
            `\\lambda`) `R(\\lambda)` to

            .. MATH::

                (R(\\alpha_i)-1)^{-1} \\bigl(R(\\lambda) - R(s_i\\lambda)
                - v(R(\\lambda) - R(\\alpha_i + s_i \\lambda)) \\bigr)

            where the numerator is divisible by the denominator in `R`.
            The Demazure-Lusztig operators give a representation of the
            Iwahori--Hecke algebra associated to the Weyl group. See

            * Lusztig, Equivariant `K`-theory and representations of Hecke
              algebras, Proc. Amer. Math. Soc. 94 (1985), no. 2, 337-342.
            * Cherednik, *Nonsymmetric Macdonald polynomials*. IMRN 10,
              483-515 (1995).

            In the examples, we confirm the braid and quadratic relations
            for type `B_2`.

            EXAMPLES::

                sage: P.<v> = PolynomialRing(QQ)
                sage: B2 = WeylCharacterRing("B2",style=\'coroots\',base_ring=P); b2 = B2.ambient()
                sage: def T1(f): return f.demazure_lusztig(1, v)
                sage: def T2(f): return f.demazure_lusztig(2, v)
                sage: T1(T2(T1(T2(b2(1,-1)))))
                (v^2-v)*b2(0,-1) + v^2*b2(-1,1)
                sage: [T1(T1(f))==(v-1)*T1(f)+v*f for f in [b2(0,0), b2(1,0), b2(2,3)]]
                [True, True, True]
                sage: [T1(T2(T1(T2(b2(i,j))))) == T2(T1(T2(T1(b2(i,j))))) for i in [-2..2] for j in [-1,1]]
                [True, True, True, True, True, True, True, True, True, True]

            Instead of an index `i` one may use a reduced word or
            Weyl group element::

                sage: b2(1,0).demazure_lusztig([2,1],v)==T2(T1(b2(1,0)))
                True
                sage: W = B2.space().weyl_group(prefix=\'s\')
                sage: [s1,s2]=W.simple_reflections()
                sage: b2(1,0).demazure_lusztig(s2*s1,v)==T2(T1(b2(1,0)))
                True
            '''
