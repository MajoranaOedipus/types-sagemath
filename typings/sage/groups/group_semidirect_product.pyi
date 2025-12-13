from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.groups import Groups as Groups
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.cartesian_product import CartesianProduct as CartesianProduct

class GroupSemidirectProductElement(CartesianProduct.Element):
    """
    Element class for :class:`GroupSemidirectProduct`.
    """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: L = RootSystem(['A',2]).root_lattice()
            sage: from sage.groups.group_exp import GroupExp
            sage: EL = GroupExp()(L)
            sage: W = L.weyl_group(prefix='s')
            sage: def twist(w, v):
            ....:     return EL(w.action(v.value))
            sage: G = GroupSemidirectProduct(W, EL, twist, prefix1='t')
            sage: g = G.an_element(); g
            s1*s2 * t[2*alpha[1] + 2*alpha[2]]
            sage: g.inverse()
            s2*s1 * t[2*alpha[1]]
        """
    def to_opposite(self):
        """
        Send an element to its image in the opposite semidirect product.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: L = RootSystem(['A',2]).root_lattice(); L
            Root lattice of the Root system of type ['A', 2]
            sage: from sage.groups.group_exp import GroupExp
            sage: EL = GroupExp()(L)
            sage: W = L.weyl_group(prefix='s'); W
            Weyl Group of type ['A', 2]
            (as a matrix group acting on the root lattice)
            sage: def twist(w, v):
            ....:     return EL(w.action(v.value))
            sage: G = GroupSemidirectProduct(W, EL, twist, prefix1='t'); G
            Semidirect product of Weyl Group of type ['A', 2] (as a matrix
            group acting on the root lattice) acting on Multiplicative form of
            Root lattice of the Root system of type ['A', 2]
            sage: mu = L.an_element(); mu
            2*alpha[1] + 2*alpha[2]
            sage: w = W.an_element(); w
            s1*s2
            sage: g = G((w,EL(mu))); g
            s1*s2 * t[2*alpha[1] + 2*alpha[2]]
            sage: g.to_opposite()
            t[-2*alpha[1]] * s1*s2
            sage: g.to_opposite().parent()
            Semidirect product of
             Multiplicative form of Root lattice of the Root system of type ['A', 2]
             acted upon by Weyl Group of type ['A', 2]
              (as a matrix group acting on the root lattice)
        """

class GroupSemidirectProduct(CartesianProduct):
    """
    Return the semidirect product of the groups ``G`` and ``H`` using the
    homomorphism ``twist``.

    INPUT:

    - ``G``, ``H`` -- multiplicative groups
    - ``twist`` -- (default: ``None``) a function defining
      a homomorphism (see below)
    - ``act_to_right`` -- boolean (default: ``True``)
    - ``prefix0`` -- string (default: ``None``)
    - ``prefix1`` -- string (default: ``None``)
    - ``print_tuple`` -- boolean (default: ``False``)
    - ``category`` -- a category (default: ``Groups()``)

    A semidirect product of groups `G` and `H` is a group structure on
    the Cartesian product `G \\times H` whose product agrees with that
    of `G` on `G \\times 1_H` and with that of `H` on `1_G \\times H`,
    such that either `1_G \\times H` or `G \\times 1_H` is a normal
    subgroup. In the former case, the group is denoted `G \\ltimes H`
    and in the latter, `G \\rtimes H`.

    If ``act_to_right`` is ``True``, this indicates the group `G \\ltimes H`
    in which `G` acts on `H` by automorphisms. In this case there is a
    group homomorphism `\\phi \\in \\mathrm{Hom}(G, \\mathrm{Aut}(H))` such that

    .. MATH::

        g h g^{-1} = \\phi(g)(h).

    The homomorphism `\\phi` is specified by the input ``twist``, which
    syntactically is the function `G\\times H\\to H` defined by

    .. MATH::

        twist(g,h) = \\phi(g)(h).

    The product on `G \\ltimes H` is defined by

    .. MATH::

        \\begin{aligned}
        (g_1,h_1)(g_2,h_2) &= g_1 h_1 g_2 h_2 \\\\\n        &= g_1 g_2 g_2^{-1} h_1 g_2 h_2 \\\\\n        &= (g_1g_2, twist(g_2^{-1}, h_1) h_2)
        \\end{aligned}

    If ``act_to_right`` is ``False``, the group `G \\rtimes H` is specified by
    a homomorphism `\\psi\\in \\mathrm{Hom}(H,\\mathrm{Aut}(G))` such that

    .. MATH::

        h g h^{-1} = \\psi(h)(g)

    Then ``twist`` is the function `H\\times G\\to G` defined by

    .. MATH::

       twist(h,g) = \\psi(h)(g).

    so that the product in `G \\rtimes H` is defined by

    .. MATH::

        \\begin{aligned}
        (g_1,h_1)(g_2,h_2) &= g_1 h_1 g_2 h_2 \\\\\n        &= g_1 h_1 g_2 h_1^{-1} h_1 h_2 \\\\\n        &= (g_1 twist(h_1,g_2), h_1 h_2)
        \\end{aligned}

    If ``prefix0`` (resp. ``prefixl``) is not ``None`` then it is used
    as a wrapper for printing elements of ``G`` (resp. ``H``). If
    ``print_tuple`` is ``True`` then elements are printed in the style
    `(g,h)` and otherwise in the style `g * h`.

    EXAMPLES::

        sage: G = GL(2,QQ)
        sage: V = QQ^2
        sage: EV = GroupExp()(V)  # make a multiplicative version of V
        sage: def twist(g, v):
        ....:     return EV(g*v.value)
        sage: H = GroupSemidirectProduct(G, EV, twist=twist, prefix1='t'); H
        Semidirect product of General Linear Group of degree 2
        over Rational Field acting on Multiplicative form of Vector space
        of dimension 2 over Rational Field
        sage: x = H.an_element(); x
        t[(1, 0)]
        sage: x^2
        t[(2, 0)]

        sage: # needs sage.rings.number_field
        sage: cartan_type = CartanType(['A',2])
        sage: W = WeylGroup(cartan_type, prefix='s')
        sage: def twist(w, v):
        ....:     return w*v*(~w)
        sage: WW = GroupSemidirectProduct(W, W, twist=twist, print_tuple=True)
        sage: s = Family(cartan_type.index_set(), lambda i: W.simple_reflection(i))
        sage: y = WW((s[1],s[2])); y
        (s1, s2)
        sage: y^2
        (1, s2*s1)
        sage: y.inverse()
        (s1, s1*s2*s1)

    .. TODO::

        - Functorial constructor for semidirect products for various categories
        - Twofold Direct product as a special case of semidirect product
    """
    def __init__(self, G, H, twist=None, act_to_right: bool = True, prefix0=None, prefix1=None, print_tuple: bool = False, category=...) -> None:
        """

        EXAMPLES::

            sage: def twist(x, y):
            ....:     return y
            sage: import __main__
            sage: __main__.twist = twist
            sage: G = GroupSemidirectProduct(WeylGroup(['A',2],prefix='s'),
            ....:                            WeylGroup(['A',3],prefix='t'), twist)
            sage: TestSuite(G).run()

        The ``__main__`` business is a trick to pass the pickling test.
        """
    def act_to_right(self):
        """
        Return ``True`` if the left factor acts on the right factor and
        ``False`` if the right factor acts on the left factor.

        EXAMPLES::

            sage: def twist(x, y):
            ....:     return y
            sage: GroupSemidirectProduct(WeylGroup(['A',2],prefix='s'),
            ....:                        WeylGroup(['A',3],prefix='t'), twist).act_to_right()
            True
        """
    @cached_method
    def one(self):
        """
        The identity element of the semidirect product group.

        EXAMPLES::

            sage: G = GL(2,QQ)
            sage: V = QQ^2
            sage: EV = GroupExp()(V)  # make a multiplicative version of V
            sage: def twist(g, v):
            ....:     return EV(g*v.value)
            sage: one = GroupSemidirectProduct(G, EV, twist=twist, prefix1='t').one(); one
            1
            sage: one.cartesian_projection(0)
            [1 0]
            [0 1]
            sage: one.cartesian_projection(1)
            (0, 0)
        """
    def group_generators(self):
        """
        Return generators of ``self``.

        EXAMPLES::

            sage: twist = lambda x,y: y
            sage: import __main__
            sage: __main__.twist = twist
            sage: EZ = GroupExp()(ZZ)
            sage: GroupSemidirectProduct(EZ, EZ, twist, print_tuple=True).group_generators()
            ((1, 0), (0, 1))
        """
    def product(self, x, y):
        """
        The product of elements `x` and `y` in the semidirect product group.

        EXAMPLES::

            sage: G = GL(2,QQ)
            sage: V = QQ^2
            sage: EV = GroupExp()(V)  # make a multiplicative version of V
            sage: def twist(g, v):
            ....:     return EV(g*v.value)
            sage: S = GroupSemidirectProduct(G, EV, twist=twist, prefix1='t')
            sage: g = G([[2,1],[3,1]]); g
            [2 1]
            [3 1]
            sage: v = EV.an_element(); v
            (1, 0)
            sage: x = S((g,v)); x
            [2 1]
            [3 1] * t[(1, 0)]
            sage: x*x # indirect doctest
            [7 3]
            [9 4] * t[(0, 3)]
        """
    @cached_method
    def opposite_semidirect_product(self):
        """
        Create the same semidirect product but with the positions of the groups exchanged.

        EXAMPLES::

            sage: G = GL(2,QQ)
            sage: L = QQ^2
            sage: EL = GroupExp()(L)
            sage: H = GroupSemidirectProduct(G, EL, prefix1='t',
            ....:                            twist=lambda g,v: EL(g*v.value)); H
            Semidirect product of General Linear Group of degree 2
            over Rational Field acting on Multiplicative form of Vector space
            of dimension 2 over Rational Field
            sage: h = H((Matrix([[0,1],[1,0]]), EL.an_element())); h
            [0 1]
            [1 0] * t[(1, 0)]
            sage: Hop = H.opposite_semidirect_product(); Hop
            Semidirect product of Multiplicative form of Vector space
            of dimension 2 over Rational Field acted upon by
            General Linear Group of degree 2 over Rational Field
            sage: hop = h.to_opposite(); hop
            t[(0, 1)] * [0 1]
            [1 0]
            sage: hop in Hop
            True
        """
    def construction(self) -> None:
        """
        Return ``None``.

        This overrides the construction functor inherited from
        ``CartesianProduct``.

        EXAMPLES::

            sage: def twist(x, y):
            ....:     return y
            sage: H = GroupSemidirectProduct(WeylGroup(['A',2],prefix='s'),
            ....:                            WeylGroup(['A',3],prefix='t'), twist)
            sage: H.construction()
        """
