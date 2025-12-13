from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.functor import Functor as Functor
from sage.categories.groups import Groups as Groups
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class GroupExp(Functor):
    """
    A functor that converts a commutative additive group into an isomorphic
    multiplicative group.

    More precisely, given a commutative additive group `G`, define the exponential
    of `G` to be the isomorphic group with elements denoted
    `e^g` for every `g \\in G` and but with product in multiplicative notation

    .. MATH::

        e^g e^h = e^{g+h} \\qquad\\text{for all $g,h \\in G$.}

    The class :class:`GroupExp` implements the sage functor which sends a commutative
    additive group `G` to its exponential.

    The creation of an instance of the functor :class:`GroupExp` requires no input::

        sage: E = GroupExp(); E
        Functor from Category of commutative additive groups to Category of groups

    The :class:`GroupExp` functor (denoted `E` in the examples) can be applied to two kinds of input.
    The first is a commutative additive group. The output is its exponential.
    This is accomplished by :meth:`_apply_functor`::

        sage: EZ = E(ZZ); EZ
        Multiplicative form of Integer Ring

    Elements of the exponentiated group can be created and manipulated as follows::

        sage: x = EZ(-3); x
        -3
        sage: x.parent()
        Multiplicative form of Integer Ring
        sage: EZ(-1) * EZ(6) == EZ(5)
        True
        sage: EZ(3)^(-1)
        -3
        sage: EZ.one()
        0

    The second kind of input the :class:`GroupExp` functor accepts, is a homomorphism of commutative additive groups.
    The output is the multiplicative form of the homomorphism. This is achieved by :meth:`_apply_functor_to_morphism`::

        sage: L = RootSystem(['A',2]).ambient_space()
        sage: EL = E(L)
        sage: W = L.weyl_group(prefix='s')
        sage: s2 = W.simple_reflection(2)
        sage: def my_action(mu):
        ....:     return s2.action(mu)
        sage: from sage.categories.morphism import SetMorphism
        sage: from sage.categories.homset import Hom
        sage: f = SetMorphism(Hom(L, L, CommutativeAdditiveGroups()), my_action)
        sage: F = E(f); F
        Generic endomorphism of
         Multiplicative form of Ambient space of the Root system of type ['A', 2]
        sage: v = L.an_element(); v
        (2, 2, 3)
        sage: y = F(EL(v)); y
        (2, 3, 2)
        sage: y.parent()
        Multiplicative form of Ambient space of the Root system of type ['A', 2]
    """
    def __init__(self) -> None:
        """
        Initialize the :class:`GroupExp` functor.

        EXAMPLES::

            sage: F = GroupExp()
            sage: F.domain()
            Category of commutative additive groups
            sage: F.codomain()
            Category of groups
        """

class GroupExpElement(ElementWrapper, MultiplicativeGroupElement):
    """
    An element in the exponential of a commutative additive group.

    INPUT:

    - ``self`` -- the exponentiated group element being created
    - ``parent`` -- the exponential group (parent of ``self``)
    - ``x`` -- the commutative additive group element being wrapped to form ``self``

    EXAMPLES::

        sage: from sage.groups.group_exp import GroupExpElement
        sage: G = QQ^2
        sage: EG = GroupExp()(G)
        sage: z = GroupExpElement(EG, vector(QQ, (1, -3))); z
        (1, -3)
        sage: z.parent()
        Multiplicative form of Vector space of dimension 2 over Rational Field
        sage: EG(vector(QQ, (1, -3))) == z
        True
    """
    def __init__(self, parent, x) -> None:
        '''
        EXAMPLES::

            sage: G = QQ^2
            sage: EG = GroupExp()(G)
            sage: x = EG.an_element(); x
            (1, 0)
            sage: TestSuite(x).run(skip="_test_category")

        See the documentation of :meth:`sage.structure.element_wrapper.ElementWrapper.__init__`
        for the reason behind skipping the category test.
        '''
    def __invert__(self):
        """
        Invert the element ``self``.

        EXAMPLES::

            sage: EZ = GroupExp()(ZZ)
            sage: EZ(-3).inverse()  # indirect doctest
            3
        """
    def __mul__(self, x):
        """
        Multiply ``self`` by `x`.

        EXAMPLES::

            sage: G = GroupExp()(ZZ)
            sage: x = G(2)
            sage: x.__mul__(G(3))
            5
            sage: G.product(G(2), G(3))
            5
        """

class GroupExp_Class(UniqueRepresentation, Parent):
    """
    The multiplicative form of a commutative additive group.

    INPUT:

    - ``G`` -- a commutative additive group

    OUTPUT: the multiplicative form of `G`

    EXAMPLES::

        sage: GroupExp()(QQ)
        Multiplicative form of Rational Field
    """
    def __init__(self, G) -> None:
        '''

        EXAMPLES::

            sage: EG = GroupExp()(QQ^2)
            sage: TestSuite(EG).run(skip="_test_elements")
        '''
    def one(self):
        """
        Return the identity element of the multiplicative group.

        EXAMPLES::

            sage: G = GroupExp()(ZZ^2)
            sage: G.one()
            (0, 0)
            sage: x = G.an_element(); x
            (1, 0)
            sage: x == x * G.one()
            True
        """
    def product(self, x, y):
        """
        Return the product of `x` and `y` in the multiplicative group.

        EXAMPLES::

            sage: G = GroupExp()(ZZ)
            sage: G.product(G(2),G(7))
            9
            sage: x = G(2)
            sage: x.__mul__(G(7))
            9
        """
    def group_generators(self):
        """
        Return generators of ``self``.

        EXAMPLES::

            sage: GroupExp()(ZZ).group_generators()
            (1,)
        """
