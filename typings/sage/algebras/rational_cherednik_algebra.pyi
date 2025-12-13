from sage.categories.algebras import Algebras as Algebras
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.root_system.cartan_matrix import CartanMatrix as CartanMatrix
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family

class RationalCherednikAlgebra(CombinatorialFreeModule):
    """
    A rational Cherednik algebra.

    Let `k` be a field. Let `W` be a complex reflection group acting on
    a vector space `\\mathfrak{h}` (over `k`). Let `\\mathfrak{h}^*` denote
    the corresponding dual vector space. Let `\\cdot` denote the
    natural action of `w` on `\\mathfrak{h}` and `\\mathfrak{h}^*`. Let
    `\\mathcal{S}` denote the set of reflections of `W` and  `\\alpha_s`
    and `\\alpha_s^{\\vee}` are the associated root and coroot of `s`. Let
    `c = (c_s)_{s \\in W}` such that `c_s = c_{tst^{-1}}` for all `t \\in W`.

    The *rational Cherednik algebra* is the `k`-algebra
    `H_{c,t}(W) = T(\\mathfrak{h} \\oplus \\mathfrak{h}^*) \\otimes kW` with
    parameters `c, t \\in k` that is subject to the relations:

    .. MATH::

        \\begin{aligned}
        w \\alpha & = (w \\cdot \\alpha) w,
        \\\\ \\alpha^{\\vee} w & = w (w^{-1} \\cdot \\alpha^{\\vee}),
        \\\\ \\alpha \\alpha^{\\vee} & = \\alpha^{\\vee} \\alpha
        + t \\langle \\alpha^{\\vee}, \\alpha \\rangle
        + \\sum_{s \\in \\mathcal{S}} c_s \\frac{\\langle \\alpha^{\\vee},
        \\alpha_s \\rangle \\langle \\alpha^{\\vee}_s, \\alpha \\rangle}{
        \\langle \\alpha^{\\vee}, \\alpha \\rangle} s,
        \\end{aligned}

    where `w \\in W` and `\\alpha \\in \\mathfrak{h}` and
    `\\alpha^{\\vee} \\in \\mathfrak{h}^*`.

    INPUT:

    - ``ct`` -- a finite Cartan type
    - ``c`` -- the parameters `c_s` given as an element or a tuple, where
      the first entry is the one for the long roots and (for
      non-simply-laced types) the second is for the short roots
    - ``t`` -- the parameter `t`
    - ``base_ring`` -- (optional) the base ring
    - ``prefix`` -- (default: ``('a', 's', 'ac')``) the prefixes

    .. TODO::

        Implement a version for complex reflection groups.

    REFERENCES:

    - [GGOR2003]_
    - [EM2001]_
    """
    @staticmethod
    def __classcall_private__(cls, ct, c: int = 1, t=None, base_ring=None, prefix=('a', 's', 'ac')):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: R1 = algebras.RationalCherednik(['B',2], 1, 1, QQ)
            sage: R2 = algebras.RationalCherednik(CartanType(['B',2]), [1,1], 1, QQ, ('a', 's', 'ac'))
            sage: R1 is R2
            True
        """
    def __init__(self, ct, c, t, base_ring, prefix) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: k = QQ['c,t']
            sage: R = algebras.RationalCherednik(['A',2], k.gen(0), k.gen(1))
            sage: TestSuite(R).run()  # long time
        """
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: list(R.algebra_generators())
            [a1, a2, s1, s2, ac1, ac2]
        """
    @cached_method
    def one_basis(self):
        """
        Return the index of the element `1`.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: R.one_basis()
            (1, 1, 1)
        """
    def product_on_basis(self, left, right):
        """
        Return ``left`` multiplied by ``right`` in ``self``.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: a2 = R.algebra_generators()['a2']
            sage: ac1 = R.algebra_generators()['ac1']
            sage: a2 * ac1  # indirect doctest
            a2*ac1
            sage: ac1 * a2
            -I + a2*ac1 - s1 - s2 + 1/2*s1*s2*s1
            sage: x = R.an_element()
            sage: [y * x for y in R.some_elements()]
            [0,
             3*ac1 + 2*s1 + a1,
             9*ac1^2 + 10*I + 6*a1*ac1 + 6*s1 + 3/2*s2 + 3/2*s1*s2*s1 + a1^2,
             3*a1*ac1 + 2*a1*s1 + a1^2,
             3*a2*ac1 + 2*a2*s1 + a1*a2,
             3*s1*ac1 + 2*I - a1*s1,
             3*s2*ac1 + 2*s2*s1 + a1*s2 + a2*s2,
             3*ac1^2 - 2*s1*ac1 + 2*I + a1*ac1 + 2*s1 + 1/2*s2 + 1/2*s1*s2*s1,
             3*ac1*ac2 + 2*s1*ac1 + 2*s1*ac2 - I + a1*ac2 - s1 - s2 + 1/2*s1*s2*s1]
            sage: [x * y for y in R.some_elements()]
            [0,
             3*ac1 + 2*s1 + a1,
             9*ac1^2 + 10*I + 6*a1*ac1 + 6*s1 + 3/2*s2 + 3/2*s1*s2*s1 + a1^2,
             6*I + 3*a1*ac1 + 6*s1 + 3/2*s2 + 3/2*s1*s2*s1 - 2*a1*s1 + a1^2,
             -3*I + 3*a2*ac1 - 3*s1 - 3*s2 + 3/2*s1*s2*s1 + 2*a1*s1 + 2*a2*s1 + a1*a2,
             -3*s1*ac1 + 2*I + a1*s1,
             3*s2*ac1 + 3*s2*ac2 + 2*s1*s2 + a1*s2,
             3*ac1^2 + 2*s1*ac1 + a1*ac1,
             3*ac1*ac2 + 2*s1*ac2 + a1*ac2]
        """
    def degree_on_basis(self, m):
        """
        Return the degree on the monomial indexed by ``m``.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: [R.degree_on_basis(g.leading_support())
            ....:  for g in R.algebra_generators()]
            [1, 1, 0, 0, -1, -1]
        """
    @cached_method
    def trivial_idempotent(self):
        """
        Return the trivial idempotent of ``self``.

        Let `e = |W|^{-1} \\sum_{w \\in W} w` is the trivial idempotent.
        Thus `e^2 = e` and `eW = We`. The trivial idempotent is used
        in the construction of the spherical Cherednik algebra from
        the rational Cherednik algebra by `U_{c,t}(W) = e H_{c,t}(W) e`.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: R.trivial_idempotent()
            1/6*I + 1/6*s1 + 1/6*s2 + 1/6*s2*s1 + 1/6*s1*s2 + 1/6*s1*s2*s1
        """
    @cached_method
    def deformed_euler(self):
        """
        Return the element `eu_k`.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: R.deformed_euler()
            2*I + 2/3*a1*ac1 + 1/3*a1*ac2 + 1/3*a2*ac1 + 2/3*a2*ac2
             + s1 + s2 + s1*s2*s1
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: R = algebras.RationalCherednik(['A',2], 1, 1, QQ)
            sage: R.some_elements()
            [0, I, 3*ac1 + 2*s1 + a1, a1, a2, s1, s2, ac1, ac2]
        """
