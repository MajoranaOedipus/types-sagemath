from sage.algebras.lie_algebras.lie_algebra import FinitelyGeneratedLieAlgebra as FinitelyGeneratedLieAlgebra, InfinitelyGeneratedLieAlgebra as InfinitelyGeneratedLieAlgebra
from sage.algebras.lie_algebras.lie_algebra_element import LieAlgebraElement as LieAlgebraElement
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.modules import Modules as Modules
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.set import Set as Set
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators

class LieAlgebraRegularVectorFields(InfinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    The Lie algebra of regular vector fields on `\\CC^{\\times}`.

    This is the Lie algebra with basis `\\{d_i\\}_{i \\in \\ZZ}` and subject
    to the relations

    .. MATH::

        [d_i, d_j] = (i - j) d_{i+j}.

    This is also known as the Witt (Lie) algebra.

    .. NOTE::

        This differs from some conventions (e.g., [Ka1990]_), where
        we have `d'_i \\mapsto -d_i`.

    REFERENCES:

    - :wikipedia:`Witt_algebra`

    .. SEEALSO::

        :class:`WittLieAlgebra_charp`
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: TestSuite(L).run()
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.lie_algebra_generators()
            Lazy family (generator map(i))_{i in Integer Ring}
        """
    def bracket_on_basis(self, i, j):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``
        where ``x < y``.

        (This particular implementation actually does not require
        ``x < y``.)

        EXAMPLES::

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.bracket_on_basis(2, -2)
            4*d[0]
            sage: L.bracket_on_basis(2, 4)
            -2*d[6]
            sage: L.bracket_on_basis(4, 4)
            0
        """
    def degree_on_basis(self, i):
        """
        Return the degree of the basis element indexed by ``i``,
        which is ``i``.

        EXAMPLES::

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.degree_on_basis(2)
            2
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.regular_vector_fields(QQ)
            sage: L.some_elements()
            [d[0], d[2], d[-2], d[-1] + d[0] - 3*d[1]]
        """
    class Element(LieAlgebraElement): ...

class WittLieAlgebra_charp(FinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    The `p`-Witt Lie algebra over a ring `R` in which
    `p \\cdot 1_R = 0`.

    Let `R` be a ring and `p` be a positive integer such that
    `p \\cdot 1_R = 0`. The `p`-Witt Lie algebra over `R` is
    the Lie algebra with basis `\\{d_0, d_1, \\ldots, d_{p-1}\\}`
    and subject to the relations

    .. MATH::

        [d_i, d_j] = (i - j) d_{i+j},

    where the `i+j` on the right hand side is identified with its
    remainder modulo `p`.

    .. SEEALSO::

        :class:`LieAlgebraRegularVectorFields`
    """
    def __init__(self, R, p) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.pwitt(GF(5), 5); L
            The 5-Witt Lie algebra over Finite Field of size 5
            sage: TestSuite(L).run()

        We skip the grading test as we need to be able to echelonize a
        matrix over the base ring as part of the test::

            sage: L = lie_algebras.pwitt(Zmod(6), 6)
            sage: TestSuite(L).run(skip='_test_grading')
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: L = lie_algebras.pwitt(Zmod(5), 5)
            sage: L.lie_algebra_generators()
            Finite family {0: d[0], 1: d[1], 2: d[2], 3: d[3], 4: d[4]}
        """
    def bracket_on_basis(self, i, j):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``
        where ``x < y``.

        (This particular implementation actually does not require
        ``x < y``.)

        EXAMPLES::

            sage: L = lie_algebras.pwitt(Zmod(5), 5)
            sage: L.bracket_on_basis(2, 3)
            4*d[0]
            sage: L.bracket_on_basis(3, 2)
            d[0]
            sage: L.bracket_on_basis(2, 2)
            0
            sage: L.bracket_on_basis(1, 3)
            3*d[4]
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.pwitt(Zmod(5), 5)
            sage: L.some_elements()
            [d[0], d[2], d[3], d[0] + 2*d[1] + d[4]]
        """
    def degree_on_basis(self, i):
        """
        Return the degree of the basis element indexed by ``i``,
        which is ``i`` mod `p`.

        EXAMPLES::

            sage: L = lie_algebras.pwitt(Zmod(5), 5)
            sage: L.degree_on_basis(7)
            2
            sage: L.degree_on_basis(2).parent()
            Ring of integers modulo 5
        """
    class Element(LieAlgebraElement): ...

class VirasoroAlgebra(InfinitelyGeneratedLieAlgebra, IndexedGenerators):
    """
    The Virasoro algebra.

    This is the Lie algebra with basis `\\{d_i\\}_{i \\in \\ZZ} \\cup \\{c\\}`
    and subject to the relations

    .. MATH::

        [d_i, d_j] = (i - j) d_{i+j} + \\frac{1}{12}(i^3 - i) \\delta_{i,-j} c

    and

    .. MATH::

        [d_i, c] = 0.

    (Here, it is assumed that the base ring `R` has `2` invertible.)

    This is the universal central extension `\\widetilde{\\mathfrak{d}}` of
    the Lie algebra `\\mathfrak{d}` of
    :class:`regular vector fields <LieAlgebraRegularVectorFields>`
    on `\\CC^{\\times}`.

    EXAMPLES::

        sage: d = lie_algebras.VirasoroAlgebra(QQ)

    REFERENCES:

    - :wikipedia:`Virasoro_algebra`
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: TestSuite(d).run()
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the generators of ``self`` as a Lie algebra.

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: d.lie_algebra_generators()
            Lazy family (generator map(i))_{i in Integer Ring}
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: B = d.basis(); B
            Lazy family (basis map(i))_{i in Disjoint union of
                                        Family ({'c'}, Integer Ring)}
            sage: B['c']
            c
            sage: B[3]
            d[3]
            sage: B[-15]
            d[-15]
        """
    def d(self, i):
        """
        Return the element `d_i` in ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: L.d(2)
            d[2]
        """
    def c(self):
        """
        The central element `c` in ``self``.

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: d.c()
            c
        """
    def bracket_on_basis(self, i, j):
        """
        Return the bracket of basis elements indexed by ``x`` and ``y``
        where ``x < y``.

        (This particular implementation actually does not require
        ``x < y``.)

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: d.bracket_on_basis('c', 2)
            0
            sage: d.bracket_on_basis(2, -2)
            4*d[0] + 1/2*c
        """
    def degree_on_basis(self, i):
        """
        Return the degree of the basis element indexed by ``i``,
        which is ``i`` and `0` for ``'c'``.

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: d.degree_on_basis(2)
            2
            sage: d.c().degree()
            0
            sage: (d.c() + d.basis()[0]).is_homogeneous()
            True
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: d = lie_algebras.VirasoroAlgebra(QQ)
            sage: d.some_elements()
            [d[0], d[2], d[-2], c, d[-1] + d[0] - 1/2*d[1] + c]
        """
    def chargeless_representation(self, a, b):
        """
        Return the chargeless representation of ``self`` with
        parameters ``a`` and ``b``.

        .. SEEALSO::

            :class:`~sage.algebras.lie_algebras.virasoro.ChargelessRepresentation`

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: L.chargeless_representation(3, 2)
            Chargeless representation (3, 2) of
             The Virasoro algebra over Rational Field
        """
    def verma_module(self, c, h):
        """
        Return the Verma module with central charge ``c`` and
        conformal (or highest) weight ``h``.

        .. SEEALSO::

            :class:`~sage.algebras.lie_algebras.virasoro.VermaModule`

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: L.verma_module(3, 2)
            Verma module with charge 3 and conformal weight 2 of
             The Virasoro algebra over Rational Field
        """
    class Element(LieAlgebraElement): ...

class ChargelessRepresentation(CombinatorialFreeModule):
    """
    A chargeless representation of the Virasoro algebra.

    Let `L` be the Virasoro algebra over the field `F` of
    characteristic `0`. For `\\alpha, \\beta \\in R`, we denote `V_{a,b}`
    as the `(a, b)`-*chargeless representation* of `L`, which is the
    `F`-span of `\\{v_k \\mid k \\in \\ZZ\\}` with `L` action

    .. MATH::

        \\begin{aligned}
        d_n \\cdot v_k & = (a n + b - k) v_{n+k},
        \\\\ c \\cdot v_k & = 0,
        \\end{aligned}

    This comes from the action of `d_n = -t^{n+1} \\frac{d}{dt}` on
    `F[t, t^{-1}]` (recall that `L` is the central extension of the
    :class:`algebra of derivations <LieAlgebraRegularVectorFields>`
    of `F[t, t^{-1}]`), where

    .. MATH::

        V_{a,b} = F[t, t^{-1}] t^{a-b} (dt)^{-a}

    and `v_k = t^{a-b+k} (dz)^{-a}`.

    The chargeless representations are either irreducible or
    contains exactly two simple subquotients, one of which is the
    trivial representation and the other is `F[t, t^{-1}] / F`.
    The non-trivial simple subquotients are called the
    *intermediate series*.

    The module `V_{a,b}` is irreducible if and only if
    `a \\neq 0, -1` or `b \\notin \\ZZ`. When `a = 0` and `b \\in \\ZZ`,
    then there exists a subrepresentation isomorphic to the trivial
    representation. If `a = -1` and `b \\in \\ZZ`, then there exists
    a subrepresentation `V` such that `V_{a,b} / V` is isomorphic
    to `K \\frac{dt}{t}` and `V` is irreducible.

    In characteristic `p`, the non-trivial simple subquotient
    is isomorphic to `F[t, t^{-1}] / F[t^p, t^{-p}]`. For
    `p \\neq 2,3`, then the action is given as above.

    EXAMPLES:

    We first construct the irreducible `V_{1/2, 3/4}` and do some
    basic computations::

        sage: L = lie_algebras.VirasoroAlgebra(QQ)
        sage: M = L.chargeless_representation(1/2, 3/4)
        sage: d = L.basis()
        sage: v = M.basis()
        sage: d[3] * v[2]
        1/4*v[5]
        sage: d[3] * v[-1]
        13/4*v[2]
        sage: (d[3] - d[-2]) * (v[-1] + 1/2*v[0] - v[4])
        -3/4*v[-3] + 1/8*v[-2] - v[2] + 9/8*v[3] + 7/4*v[7]

    We construct the reducible `V_{0,2}` and the trivial
    subrepresentation given by the span of `v_2`. We verify
    this for `\\{d_i \\mid -10 \\leq i < 10\\}`::

        sage: M = L.chargeless_representation(0, 2)
        sage: v = M.basis()
        sage: all(d[i] * v[2] == M.zero() for i in range(-10, 10))
        True

    REFERENCES:

    - [Mat1992]_
    - [IK2010]_
    """
    def __init__(self, V, a, b) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.chargeless_representation(1/2, 3/4)
            sage: TestSuite(M).run()
        """
    def parameters(self):
        """
        Return the parameters `(a, b)` of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.chargeless_representation(1/2, 3/4)
            sage: M.parameters()
            (1/2, 3/4)
        """
    def virasoro_algebra(self):
        """
        Return the Virasoro algebra ``self`` is a representation of.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.chargeless_representation(1/2, 3/4)
            sage: M.virasoro_algebra() is L
            True
        """
    def degree_on_basis(self, i):
        """
        Return the degree of the basis element indexed by ``i``,
        which is `i`.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.chargeless_representation(1/2, 3/4)
            sage: M.degree_on_basis(-3)
            -3
        """
    class Element(CombinatorialFreeModule.Element): ...

class VermaModule(CombinatorialFreeModule):
    """
    A Verma module of the Virasoro algebra.

    The Virasoro algebra admits a triangular decomposition

    .. MATH::

        V_- \\oplus R d_0 \\oplus R \\hat{c} \\oplus V_+,

    where `V_-` (resp. `V_+`) is the span of `\\{d_i \\mid i < 0\\}`
    (resp. `\\{d_i \\mid i > 0\\}`). We can construct the *Verma module*
    `M_{c,h}` as the induced representation of the `R d_0 \\oplus
    R \\hat{c} \\oplus V_+` representation `R_{c,H} = Rv`, where

    .. MATH::

        V_+ v = 0, \\qquad \\hat{c} v = c v, \\qquad d_0 v = h v.

    Therefore, we have a basis of `M_{c,h}`

    .. MATH::

        \\{ L_{i_1} \\cdots L_{i_k} v \\mid i_1 \\leq \\cdots \\leq i_k < 0 \\}.

    Moreover, the Verma modules are the free objects in the category of
    highest weight representations of `V` and are indecomposable.
    The Verma module `M_{c,h}` is irreducible for generic values of `c`
    and `h` and when it is reducible, the quotient by the maximal
    submodule is the unique irreducible highest weight representation
    `V_{c,h}`.

    EXAMPLES:

    We construct a Verma module and do some basic computations::

        sage: L = lie_algebras.VirasoroAlgebra(QQ)
        sage: M = L.verma_module(3, 0)
        sage: d = L.basis()
        sage: v = M.highest_weight_vector()
        sage: d[3] * v
        0
        sage: d[-3] * v
        d[-3]*v
        sage: d[-1] * (d[-3] * v)
        2*d[-4]*v + d[-3]*d[-1]*v
        sage: d[2] * (d[-1] * (d[-3] * v))
        12*d[-2]*v + 5*d[-1]*d[-1]*v

    We verify that `d_{-1} v` is a singular vector for
    `\\{d_i \\mid 1 \\leq i < 20\\}`::

        sage: w = M.basis()[-1]; w
        d[-1]*v
        sage: all(d[i] * w == M.zero() for i in range(1,20))
        True

    We also verify a singular vector for `V_{-2,1}`::

        sage: M = L.verma_module(-2, 1)
        sage: B = M.basis()
        sage: w = B[-1,-1] - 2 * B[-2]
        sage: d = L.basis()
        sage: all(d[i] * w == M.zero() for i in range(1,20))
        True

    REFERENCES:

    - :wikipedia:`Virasoro_algebra#Representation_theory`
    """
    @staticmethod
    def __classcall_private__(cls, V, c, h):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(3, 1/2)
            sage: M2 = L.verma_module(int(3), 1/2)
            sage: M is M2
            True
        """
    def __init__(self, V, c, h) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(3, 1/2)
            sage: TestSuite(M).run()
        """
    def central_charge(self):
        """
        Return the central charge of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(3, 0)
            sage: M.central_charge()
            3
        """
    def conformal_weight(self):
        """
        Return the conformal weight of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(3, 0)
            sage: M.conformal_weight()
            3
        """
    def virasoro_algebra(self):
        """
        Return the Virasoro algebra ``self`` is a representation of.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(1/2, 3/4)
            sage: M.virasoro_algebra() is L
            True
        """
    @cached_method
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(-2/7, 3)
            sage: M.highest_weight_vector()
            v
        """
    def degree_on_basis(self, d):
        """
        Return the degree of the basis element indexed by ``d``, which
        is the sum of the entries of ``d``.

        EXAMPLES::

            sage: L = lie_algebras.VirasoroAlgebra(QQ)
            sage: M = L.verma_module(-2/7, 3)
            sage: M.degree_on_basis((-3,-3,-1))
            -7
        """
    class Element(CombinatorialFreeModule.Element): ...
