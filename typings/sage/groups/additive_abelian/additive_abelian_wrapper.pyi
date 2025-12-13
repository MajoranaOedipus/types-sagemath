from . import additive_abelian_group as addgp
from sage.categories.morphism import Morphism as Morphism
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import parent as parent
from sage.structure.sequence import Sequence as Sequence

class UnwrappingMorphism(Morphism):
    """
    The embedding into the ambient group. Used by the coercion framework.
    """
    def __init__(self, domain) -> None:
        """
        EXAMPLES::

            sage: G = AdditiveAbelianGroupWrapper(QQbar,                                # needs sage.rings.number_field
            ....:                                 [sqrt(QQbar(2)), sqrt(QQbar(3))], [0, 0])
            sage: F = QQbar.coerce_map_from(G); F                                       # needs sage.rings.number_field
            Generic morphism:
              From: Additive abelian group isomorphic to Z + Z embedded in Algebraic Field
              To:   Algebraic Field
            sage: type(F)                                                               # needs sage.rings.number_field
            <class 'sage.groups.additive_abelian.additive_abelian_wrapper.UnwrappingMorphism'>
        """

class AdditiveAbelianGroupWrapperElement(addgp.AdditiveAbelianGroupElement):
    """
    An element of an :class:`AdditiveAbelianGroupWrapper`.
    """
    def __init__(self, parent, vector, element=None, check: bool = False) -> None:
        """
        EXAMPLES::

            sage: from sage.groups.additive_abelian.additive_abelian_wrapper import AdditiveAbelianGroupWrapper
            sage: G = AdditiveAbelianGroupWrapper(QQbar,                                # needs sage.rings.number_field
            ....:                                 [sqrt(QQbar(2)), sqrt(QQbar(3))], [0, 0])
            sage: G.0  # indirect doctest                                               # needs sage.rings.number_field
            1.414213562373095?
        """
    def element(self):
        """
        Return the underlying object that this element wraps.

        EXAMPLES::

            sage: T = EllipticCurve('65a').torsion_subgroup().gen(0)                    # needs sage.schemes
            sage: T; type(T)                                                            # needs sage.schemes
            (0 : 0 : 1)
            <class 'sage.schemes.elliptic_curves.ell_torsion.EllipticCurveTorsionSubgroup_with_category.element_class'>
            sage: T.element(); type(T.element())                                        # needs sage.schemes
            (0 : 0 : 1)
            <class 'sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_number_field'>
        """

class AdditiveAbelianGroupWrapper(addgp.AdditiveAbelianGroup_fixed_gens):
    """
    This class is used to wrap a subgroup of an existing
    additive abelian group as a new additive abelian group.

    EXAMPLES::

        sage: G2 = AdditiveAbelianGroupWrapper(Zmod(42), [2], [21]); G2
        Additive abelian group isomorphic to Z/21 embedded in Ring of integers modulo 42
        sage: G6 = AdditiveAbelianGroupWrapper(Zmod(42), [6], [7]); G6
        Additive abelian group isomorphic to Z/7 embedded in Ring of integers modulo 42
        sage: G = AdditiveAbelianGroupWrapper(Zmod(42), [21,14,6], [2,3,7]); G
        Additive abelian group isomorphic to Z/2 + Z/3 + Z/7 embedded in
         Ring of integers modulo 42
        sage: G.invariants()
        (42,)

    ::

        sage: AdditiveAbelianGroupWrapper(QQbar, [sqrt(2), sqrt(3)], [0, 0])            # needs sage.rings.number_field sage.symbolic
        Additive abelian group isomorphic to Z + Z embedded in Algebraic Field

    ::

        sage: EllipticCurve(GF(419**2), [1,0]).abelian_group()  # indirect doctest      # needs sage.rings.finite_rings sage.schemes
        Additive abelian group isomorphic to Z/420 + Z/420 embedded in
         Abelian group of points on Elliptic Curve
          defined by y^2 = x^3 + x over Finite Field in z2 of size 419^2
    """
    Element = AdditiveAbelianGroupWrapperElement
    def __init__(self, universe, gens, invariants) -> None:
        """
        EXAMPLES::

            sage: AdditiveAbelianGroupWrapper(QQbar,  # indirect doctest                # needs sage.rings.number_field
            ....:                             [sqrt(QQbar(2)), sqrt(QQbar(3))], [0, 0])
            Additive abelian group isomorphic to Z + Z embedded in Algebraic Field
        """
    def universe(self):
        """
        The ambient group in which this abelian group lives.

        EXAMPLES::

            sage: G = AdditiveAbelianGroupWrapper(QQbar,                                # needs sage.rings.number_field
            ....:                                 [sqrt(QQbar(2)), sqrt(QQbar(3))],
            ....:                                 [0, 0])
            sage: G.universe()                                                          # needs sage.rings.number_field
            Algebraic Field
        """
    def generator_orders(self):
        """
        The orders of the generators with which this group was initialised.
        (Note that these are not necessarily a minimal set of generators.)
        Generators of infinite order are returned as 0. Compare
        ``self.invariants()``, which returns the orders of a minimal set of
        generators.

        EXAMPLES::

            sage: V = Zmod(6)**2
            sage: G = AdditiveAbelianGroupWrapper(V, [2*V.0, 3*V.1], [3, 2])
            sage: G.generator_orders()
            (3, 2)
            sage: G.invariants()
            (6,)
        """
    def discrete_exp(self, v):
        """
        Given a list (or other iterable) of length equal to the number of
        generators of this group, compute the element of the ambient group
        with those exponents in terms of the generators of ``self``.

        EXAMPLES::

            sage: G = AdditiveAbelianGroupWrapper(QQbar,                                # needs sage.rings.number_field
            ....:                                 [sqrt(QQbar(2)), -1], [0, 0])
            sage: v = G.discrete_exp([3, 5]); v                                         # needs sage.rings.number_field
            -0.7573593128807148?
            sage: v.parent() is QQbar                                                   # needs sage.rings.number_field
            True

        This method is an inverse of :meth:`discrete_log`::

            sage: orders = [2, 2*3, 2*3*5, 2*3*5*7, 2*3*5*7*11]
            sage: G = AdditiveAbelianGroup(orders)
            sage: A = AdditiveAbelianGroupWrapper(G.0.parent(), G.gens(), orders)
            sage: el = A.random_element()
            sage: A.discrete_exp(A.discrete_log(el)) == el
            True

        TESTS:

        Check that :meth:`_discrete_exp` still works (for now)::

            sage: A._discrete_exp(list(range(1,6)))
            doctest:warning ...
            DeprecationWarning: _discrete_exp is deprecated. ...
            (1, 2, 3, 4, 5)
        """
    def discrete_log(self, x, gens=None):
        """
        Given an element of the ambient group, attempt to express it in terms
        of the generators of this group or the given generators of a subgroup.

        ALGORITHM:

        This reduces to p-groups, then calls :func:`_discrete_log_pgroup` which
        implements a basic version of the recursive algorithm from [Suth2008]_.

        AUTHORS:

        - Lorenz Panny (2017)

        EXAMPLES::

            sage: G = AdditiveAbelianGroup([2, 2*3, 2*3*5, 2*3*5*7, 2*3*5*7*11])
            sage: A = AdditiveAbelianGroupWrapper(G.0.parent(), G.gens(),
            ....:                                 [g.order() for g in G.gens()])
            sage: A.discrete_log(A.discrete_exp([1,5,23,127,539]))
            (1, 5, 23, 127, 539)

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<t> = GF(1009**2, modulus=x**2+11); E = EllipticCurve(j=F(940))     # needs sage.rings.finite_rings sage.schemes
            sage: P, Q = E(900*t + 228, 974*t + 185), E(1007*t + 214, 865*t + 802)      # needs sage.rings.finite_rings sage.schemes
            sage: E.abelian_group().discrete_log(123 * P + 777 * Q, [P, Q])             # needs sage.rings.finite_rings sage.schemes
            (123, 777)

        ::

            sage: V = Zmod(8)**2
            sage: G = AdditiveAbelianGroupWrapper(V, [[2,2],[4,0]], [4, 2])
            sage: G.discrete_log(V([6, 2]))
            (1, 1)
            sage: G.discrete_log(V([6, 4]))
            Traceback (most recent call last):
            ...
            ValueError: not in group

        ::

            sage: G = AdditiveAbelianGroupWrapper(QQbar, [sqrt(2)], [0])                # needs sage.rings.number_field sage.symbolic
            sage: G.discrete_log(QQbar(2*sqrt(2)))                                      # needs sage.rings.number_field sage.symbolic
            Traceback (most recent call last):
            ...
            NotImplementedError: No black-box discrete log for infinite abelian groups

        TESTS:

        Check that :meth:`_discrete_log` still works (for now)::

            sage: orders = [2, 2*3, 2*3*5, 2*3*5*7, 2*3*5*7*11]
            sage: G = AdditiveAbelianGroup(orders)
            sage: A = AdditiveAbelianGroupWrapper(G.0.parent(), G.gens(), orders)
            sage: A._discrete_log(sum(i*g for i,g in enumerate(G.gens(),1)))
            doctest:warning ...
            DeprecationWarning: _discrete_log is deprecated. ...
            (1, 2, 3, 4, 5)
        """
    def torsion_subgroup(self, n=None):
        """
        Return the `n`-torsion subgroup of this additive abelian group
        when `n` is given, and the torsion subgroup otherwise.

        The [`n`-]torsion subgroup consists of all elements whose order
        is finite [and divides `n`].

        EXAMPLES::

            sage: ords = [2, 2*3, 2*3*5, 0, 2*3*5*7, 2*3*5*7*11]
            sage: G = AdditiveAbelianGroup(ords)
            sage: A = AdditiveAbelianGroupWrapper(G.0.parent(), G.gens(), ords)
            sage: T = A.torsion_subgroup(5)
            sage: T
            Additive abelian group isomorphic to Z/5 + Z/5 + Z/5 embedded in
             Additive abelian group isomorphic to Z/2 + Z/6 + Z/30 + Z + Z/210 + Z/2310
            sage: T.gens()
            ((0, 0, 6, 0, 0, 0), (0, 0, 0, 0, 42, 0), (0, 0, 0, 0, 0, 462))

        ::

            sage: # needs sage.rings.finite_rings sage.schemes
            sage: E = EllipticCurve(GF(487^2), [311,205])
            sage: T = E.abelian_group().torsion_subgroup(42); T
            Additive abelian group isomorphic to Z/42 + Z/6 embedded in
             Abelian group of points on Elliptic Curve
              defined by y^2 = x^3 + 311*x + 205 over Finite Field in z2 of size 487^2
            sage: [P.order() for P in T.gens()]
            [42, 6]

        ::

            sage: # needs sage.schemes
            sage: E = EllipticCurve('574i1')
            sage: pts = [E(103,172), E(61,18)]
            sage: assert pts[0].order() == 7 and pts[1].order() == infinity
            sage: M = AdditiveAbelianGroupWrapper(pts[0].parent(), pts, [7,0]); M
            Additive abelian group isomorphic to Z/7 + Z embedded in
             Abelian group of points on Elliptic Curve defined by
              y^2 + x*y + y = x^3 - x^2 - 19353*x + 958713 over Rational Field
            sage: M.torsion_subgroup()
            Additive abelian group isomorphic to Z/7 embedded in
             Abelian group of points on Elliptic Curve defined by
              y^2 + x*y + y = x^3 - x^2 - 19353*x + 958713 over Rational Field
            sage: M.torsion_subgroup(7)
            Additive abelian group isomorphic to Z/7 embedded in
             Abelian group of points on Elliptic Curve defined by
              y^2 + x*y + y = x^3 - x^2 - 19353*x + 958713 over Rational Field
            sage: M.torsion_subgroup(5)
            Trivial group embedded in Abelian group of points on Elliptic Curve
             defined by y^2 + x*y + y = x^3 - x^2 - 19353*x + 958713 over Rational Field

        AUTHORS:

        - Lorenz Panny (2022)
        """
    @staticmethod
    def from_generators(gens, universe=None):
        """
        This method constructs the subgroup generated by a sequence
        of *finite-order* elements in an additive abelian group.

        The elements need not be independent, hence this can be used
        to perform tasks such as finding relations between some given
        elements of an abelian group, computing the structure of the
        generated subgroup, enumerating all elements of the subgroup,
        and solving discrete-logarithm problems.

        EXAMPLES::

            sage: G = AdditiveAbelianGroup([15, 30, 45])
            sage: gs = [G((1,2,3)), G((4,5,6)), G((7,7,7)), G((3,2,1))]
            sage: H = AdditiveAbelianGroupWrapper.from_generators(gs); H
            Additive abelian group isomorphic to Z/90 + Z/15 embedded in
             Additive abelian group isomorphic to Z/15 + Z/30 + Z/45
            sage: H.gens()
            ((12, 13, 14), (1, 26, 21))

        TESTS:

        Random testing::

            sage: invs = []
            sage: while not 1 < prod(invs) < 10^4:
            ....:     invs = [randrange(1,100) for _ in range(randrange(1,20))]
            sage: G = AdditiveAbelianGroup(invs)
            sage: gs = [G.random_element() for _ in range(randrange(1,10))]
            sage: H = AdditiveAbelianGroupWrapper.from_generators(gs)
            sage: os = H.generator_orders()
            sage: vecs = cartesian_product_iterator(list(map(range, os)))
            sage: els = {sum(i*g for i,g in zip(vec, H.gens())) for vec in vecs}
            sage: len(els) == prod(os)
            True
        """

def basis_from_generators(gens, ords=None):
    """
    Given a generating set of some finite abelian group
    (additively written), compute and return a basis of
    the group.

    .. NOTE::

        A *basis* of a finite abelian group is a generating
        set `\\{g_1, \\ldots, g_n\\}` such that each element of the
        group can be written as a unique linear combination
        `\\alpha_1 g_1 + \\cdots + \\alpha_n g_n` with each
        `\\alpha_i \\in \\{0, \\ldots, \\mathrm{ord}(g_i)-1\\}`.

    ALGORITHM: [Suth2007]_, Algorithm 9.1 & Remark 9.1

    EXAMPLES::

        sage: # needs sage.groups sage.rings.finite_rings
        sage: from sage.groups.additive_abelian.additive_abelian_wrapper import basis_from_generators
        sage: E = EllipticCurve(GF(31337^6,'a'), j=37)
        sage: E.order()
        946988065073788930380545280
        sage: (R,S), (ordR,ordS) = basis_from_generators(E.gens())
        sage: ordR, ordS
        (313157428926517503432720, 3024)
        sage: R.order() == ordR
        True
        sage: S.order() == ordS
        True
        sage: ordR * ordS == E.order()
        True
        sage: R.weil_pairing(S, ordR).multiplicative_order() == ordS
        True
        sage: E.abelian_group().invariants()
        (3024, 313157428926517503432720)
    """
