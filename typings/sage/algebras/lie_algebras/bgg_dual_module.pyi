from sage.algebras.lie_algebras.verma_module import ModulePrinting as ModulePrinting
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.monoids import Monoids as Monoids
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.data_structures.blas_dict import iaxpy as iaxpy
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid, IndexedMonoid as IndexedMonoid
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators
from sage.structure.parent import Parent as Parent
from typing import Self

class BGGDualModule(CombinatorialFreeModule):
    """
    The dual module `M^{\\vee}` in the BGG Category `\\mathcal{O}`.

    Let `\\tau` be the transpose map of a semisimple (finite dimensional)
    Lie algebra `\\mathfrak{g}` over a field `R`. Let `M \\in \\mathcal{O}`.
    The *BGG dual module* is the `R`-module `M^{\\vee} :=
    \\bigoplus_{\\lambda} M_{\\lambda}^*` which has a `U(\\mathfrak{g})`-module
    structure given by

    .. MATH::

        x \\cdot \\phi(v) := \\phi(\\tau(x) \\cdot v),

    which is also a weight module with the same grading as `M`.

    The basis we chose to work with here is the natural dual basis to the
    distinguished basis `B` of `M`. That is, we define the dual function
    to `b` as `\\phi_b(c) = \\delta_{bc}`.

    EXAMPLES::

        sage: g = LieAlgebra(QQ, cartan_type=['A', 1])
        sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
        sage: M = g.verma_module(2*La[1])
        sage: Mc = M.dual()
        sage: B = Mc.basis()
        sage: it = iter(B)
        sage: elts = [next(it) for _ in range(7)]; elts
        [v[2*Lambda[1]]^*,
         f[-alpha[1]]*v[2*Lambda[1]]^*,
         f[-alpha[1]]^2*v[2*Lambda[1]]^*,
         f[-alpha[1]]^3*v[2*Lambda[1]]^*,
         f[-alpha[1]]^4*v[2*Lambda[1]]^*,
         f[-alpha[1]]^5*v[2*Lambda[1]]^*,
         f[-alpha[1]]^6*v[2*Lambda[1]]^*]
        sage: e, h, f = g.pbw_basis().algebra_generators()
        sage: [f * vec for vec in elts]
        [2*f[-alpha[1]]*v[2*Lambda[1]]^*,
         2*f[-alpha[1]]^2*v[2*Lambda[1]]^*,
         0,
         -4*f[-alpha[1]]^4*v[2*Lambda[1]]^*,
         -10*f[-alpha[1]]^5*v[2*Lambda[1]]^*,
         -18*f[-alpha[1]]^6*v[2*Lambda[1]]^*,
         -28*f[-alpha[1]]^7*v[2*Lambda[1]]^*]
        sage: [e * vec for vec in elts]
        [0,
         v[2*Lambda[1]]^*,
         f[-alpha[1]]*v[2*Lambda[1]]^*,
         f[-alpha[1]]^2*v[2*Lambda[1]]^*,
         f[-alpha[1]]^3*v[2*Lambda[1]]^*,
         f[-alpha[1]]^4*v[2*Lambda[1]]^*,
         f[-alpha[1]]^5*v[2*Lambda[1]]^*]
        sage: [h * vec for vec in elts]
        [2*v[2*Lambda[1]]^*,
         0,
         -2*f[-alpha[1]]^2*v[2*Lambda[1]]^*,
         -4*f[-alpha[1]]^3*v[2*Lambda[1]]^*,
         -6*f[-alpha[1]]^4*v[2*Lambda[1]]^*,
         -8*f[-alpha[1]]^5*v[2*Lambda[1]]^*,
         -10*f[-alpha[1]]^6*v[2*Lambda[1]]^*]

    REFERENCES:

    - [Humphreys08]_
    """
    def __init__(self, module) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 2])
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = g.verma_module(2*La[1] + La[2])
            sage: Mc = M.dual()
            sage: TestSuite(Mc).run()

            sage: M = g.verma_module(2/3*La[1] - 3/5*La[2])
            sage: Mc = M.dual()
            sage: TestSuite(Mc).run()
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the basis element indexed by ``m``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['D', 5])
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = g.verma_module(La[1] + La[4] - 1/3*La[5])
            sage: Mc = M.dual()
            sage: elt = Mc.an_element(); elt
            f[-alpha[5]]^2*f[-alpha[4]]^2*f[-alpha[3]]^3*v[Lambda[1] + Lambda[4] - 1/3*Lambda[5]]^*
             + 2*f[-alpha[5]]*v[Lambda[1] + Lambda[4] - 1/3*Lambda[5]]^*
             + 3*f[-alpha[4]]*v[Lambda[1] + Lambda[4] - 1/3*Lambda[5]]^*
             + v[Lambda[1] + Lambda[4] - 1/3*Lambda[5]]^*
            sage: [M.degree_on_basis(m) for m in elt.support()]
            [Lambda[1] + 3*Lambda[2] - 2*Lambda[3] - 4/3*Lambda[5],
             Lambda[1] + Lambda[4] - 1/3*Lambda[5],
             Lambda[1] + Lambda[3] + Lambda[4] - 7/3*Lambda[5],
             Lambda[1] + Lambda[3] - Lambda[4] - 1/3*Lambda[5]]
        """
    def highest_weight(self):
        """
        Return the highest weight of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 7])
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = g.verma_module(2*La[1] + 5/3*La[4] - 3*La[6])
            sage: Mc = M.dual()
            sage: Mc.highest_weight()
            2*Lambda[1] + 5/3*Lambda[4] - 3*Lambda[6]
        """
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self`` (assuming the
        defining module defines such a vector).

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 1])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = g.verma_module(2*La[1])
            sage: Mc = M.dual()
            sage: Mc.highest_weight_vector()
            v[2*Lambda[1]]^*
        """
    def lie_algebra(self):
        """
        Return the underlying Lie algebra of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 3])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = g.verma_module(2*La[1] + La[3])
            sage: Mc = M.dual()
            sage: Mc.lie_algebra() is g
            True
        """
    def dual(self):
        """
        Return the dual module of ``self``.

        In Category `\\mathcal{O}`, we have `(M^{\\vee})^{\\vee} \\cong M`, so
        we return the defining module `M` of `M^{\\vee}`.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['F', 4])
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = g.verma_module(La[1] - 5/3*La[2] + 3*La[4])
            sage: Mc = M.dual()
            sage: Mc.dual() is M
            True
        """
    class Element(CombinatorialFreeModule.Element): ...

class SimpleModuleIndices(IndexedFreeAbelianMonoid):
    """
    The indices of the basis for a simple `U(\\mathfrak{g})`-module.

    .. NOTE::

        The current implementation assumes the Lie algebra `\\mathfrak{g}`
        is finite dimensional.
    """
    @staticmethod
    def __classcall__(cls, simple, prefix: str = 'f', **kwds):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[3])
            sage: from sage.algebras.lie_algebras.bgg_dual_module import SimpleModuleIndices
            sage: SimpleModuleIndices(L) is L._indices
            True
        """
    def __init__(self, simple, prefix, category=None, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: I = g.simple_module(2*La[1] + La[2]).indices()
            sage: TestSuite(I).run()

            sage: I = g.simple_module(2*La[1] - 1/3*La[2]).indices()
            sage: TestSuite(I).run(max_runs=150)  # long time
        """
    def weight_space_basis(self, mu):
        """
        Return the indices of the ``mu`` weight space basis elements.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: P = g.cartan_type().root_system().weight_lattice()
            sage: La = P.fundamental_weights()
            sage: al = P.simple_roots()
            sage: wt = -3*La[1] + 3*La[2]
            sage: I = g.simple_module(wt).indices()
            sage: I.weight_space_basis(wt)
            [1]
            sage: I.weight_space_basis(wt - al[1])
            [f[-alpha[1]]]
            sage: I.weight_space_basis(wt - al[2])
            [f[-alpha[2]]]
            sage: I.weight_space_basis(wt - al[1] - al[2])
            [f[-alpha[1] - alpha[2]], f[-alpha[2]]*f[-alpha[1]]]
            sage: I.weight_space_basis(wt - 4*al[1])
            [f[-alpha[1]]^4]
            sage: I.weight_space_basis(wt - 4*al[2])
            []
        """
    def __contains__(self, m) -> bool:
        """
        Check if ``m`` is contained in ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1])
            sage: I = L.indices()
            sage: I.one() in I
            True
            sage: it = iter(I)
            sage: for _ in range(3):
            ....:     elt = next(it)
            ....:     print(elt, elt in I)
            1 True
            f[-alpha[1]] True
            f[-alpha[1] - alpha[2]] True
            sage: gens = list(I.gens()); gens
            [f[-alpha[2]],
             f[-alpha[1]],
             f[-alpha[1] - alpha[2]],
             f[-2*alpha[1] - alpha[2]],
             f[-3*alpha[1] - alpha[2]],
             f[-3*alpha[1] - 2*alpha[2]]]
            sage: gens[1] in I
            True
            sage: gens[0] * gens[1] in I
            False
            sage: gens[2] in I
            True
            sage: gens[0]^10 in I
            False
            sage: gens[5]^6 * gens[2]^10 in I
            False
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[2])
            sage: I = L.indices()
            sage: list(I)
            [1, f[-alpha[2]], f[-alpha[1] - alpha[2]], f[-alpha[1] - 2*alpha[2]]]

            sage: L = g.simple_module(La[1]-La[2])
            sage: I = L.indices()
            sage: it = iter(I)
            sage: [next(it) for _ in range(6)]
            [1, f[-alpha[2]], f[-alpha[1]], f[-alpha[1] - alpha[2]],
             f[-alpha[1] - 2*alpha[2]], f[-alpha[2]]^2]
        """
    @cached_method
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1]+La[4])
            sage: L._indices.cardinality()
            51975
        """

class SimpleModule(ModulePrinting, CombinatorialFreeModule):
    """
    Return the simple module `L_{\\lambda}` as the image of the natural
    morphism `\\phi: M_{\\lambda} \\to M_{\\lambda}^{\\vee}`.
    """
    @staticmethod
    def __classcall_private__(cls, g, weight, *args, **kwds):
        """
        Normalize input to ensure a unique representation and return
        the correct type.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: type(g.simple_module(La[1] + La[2]))
            <class 'sage.algebras.lie_algebras.bgg_dual_module.FiniteDimensionalSimpleModule_with_category'>
            sage: type(g.simple_module(La[1] - La[2]))
            <class 'sage.algebras.lie_algebras.bgg_dual_module.SimpleModule_with_category'>
            sage: type(g.simple_module(La[1] + 3/2*La[2]))
            <class 'sage.algebras.lie_algebras.bgg_dual_module.SimpleModule_with_category'>
        """
    def __init__(self, g, weight, prefix: str = 'f', basis_key=None, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[2])
            sage: TestSuite(L).run()

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] - La[2])
            sage: TestSuite(L).run()
        """
    def ambient(self):
        """
        Return the ambient module of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(2*La[1])
            sage: L.ambient()
            BGG Dual of Verma module with highest weight 2*Lambda[1] of
             Lie algebra of ['G', 2] in the Chevalley basis
        """
    @lazy_attribute
    def lift(self):
        """
        Return the lift map of ``self`` to the ambient dual Verma module.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1])
            sage: [L.lift(b) for b in L.basis()]  # long time
            [v[Lambda[1]]^*,
             f[-alpha[1]]*v[Lambda[1]]^*,
             f[-alpha[2]]*f[-alpha[1]]*v[Lambda[1]]^* - f[-alpha[1] - alpha[2]]*v[Lambda[1]]^*,
             f[-alpha[1]]*f[-alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + f[-2*alpha[1] - alpha[2]]*v[Lambda[1]]^*,
             f[-alpha[1]]^2*f[-alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + f[-alpha[1]]*f[-2*alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + 1/2*f[-3*alpha[1] - alpha[2]]*v[Lambda[1]]^*,
             f[-alpha[2]]*f[-alpha[1]]^2*f[-alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + f[-alpha[2]]*f[-alpha[1]]*f[-2*alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + 1/2*f[-alpha[2]]*f[-3*alpha[1] - alpha[2]]*v[Lambda[1]]^*
              - f[-alpha[1] - alpha[2]]*f[-2*alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + 1/2*f[-3*alpha[1] - 2*alpha[2]]*v[Lambda[1]]^*,
             f[-alpha[1]]*f[-alpha[1] - alpha[2]]*f[-2*alpha[1] - alpha[2]]*v[Lambda[1]]^*
              - 1/2*f[-alpha[1]]*f[-3*alpha[1] - 2*alpha[2]]*v[Lambda[1]]^*
              - 1/2*f[-alpha[1] - alpha[2]]*f[-3*alpha[1] - alpha[2]]*v[Lambda[1]]^*
              + f[-2*alpha[1] - alpha[2]]^2*v[Lambda[1]]^*]
        """
    def retract(self, x):
        """
        Return the retraction of ``x`` in ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(2*La[1])
            sage: L.retract(L.lift(sum(L.basis())))
            f[-alpha[1]]^2*u[2*Lambda[1]] + f[-alpha[1]]*f[-alpha[1] - alpha[2]]*u[2*Lambda[1]]
             + f[-alpha[1] - alpha[2]]^2*u[2*Lambda[1]] + f[-alpha[1]]*u[2*Lambda[1]]
             + f[-alpha[1] - alpha[2]]*u[2*Lambda[1]] + u[2*Lambda[1]]
            sage: B = list(L.basis())
            sage: L.retract(3/2*L.lift(B[0]) - L.lift(B[2]) - 10/3*L.lift(B[3]))
            -10/3*f[-alpha[1]]^2*u[2*Lambda[1]]
             - f[-alpha[1] - alpha[2]]*u[2*Lambda[1]]
             + 3/2*u[2*Lambda[1]]
        """
    def dual(self) -> Self:
        """
        Return the dual module of ``self``, which is ``self`` since simple
        modules are self-dual.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 4])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(2*La[1] + 3*La[4])
            sage: L.dual() is L
            True
        """
    def highest_weight(self):
        """
        Return the highest weight of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.so(QQ, 7)
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[2])
            sage: L.highest_weight()
            Lambda[1] + Lambda[2]
        """
    @cached_method
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.sp(QQ, 6)
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[2])
            sage: L.highest_weight_vector()
            u[Lambda[1] + Lambda[2]]
        """
    def lie_algebra(self):
        """
        Return the underlying Lie algebra of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.so(QQ, 9)
            sage: La = g.cartan_type().root_system().weight_space().fundamental_weights()
            sage: L = g.simple_module(La[3] - 1/2*La[1])
            sage: L.lie_algebra()
            Lie algebra of ['B', 4] in the Chevalley basis
        """
    def pbw_basis(self):
        """
        Return the PBW basis of the underlying Lie algebra
        used to define ``self``.

        EXAMPLES::

            sage: g = lie_algebras.so(QQ, 8)
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[2] - 2*La[3])
            sage: L.pbw_basis()
            Universal enveloping algebra of Lie algebra of ['D', 4] in the Chevalley basis
             in the Poincare-Birkhoff-Witt basis
        """
    def homogeneous_component_basis(self, mu):
        """
        Return a basis for the ``mu`` weight space of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: P = g.cartan_type().root_system().weight_lattice()
            sage: La = P.fundamental_weights()
            sage: la = La[1] + La[2]
            sage: L = g.simple_module(la)
            sage: from itertools import product
            sage: al = P.simple_roots()
            sage: for wts in product(range(4), repeat=2):
            ....:     mu = la - wts[0] * al[1] - wts[1] * al[2]
            ....:     print(mu)
            ....:     print(L.homogeneous_component_basis(mu))
            Lambda[1] + Lambda[2]
            Family (u[Lambda[1] + Lambda[2]],)
            2*Lambda[1] - Lambda[2]
            Family (f[-alpha[2]]*u[Lambda[1] + Lambda[2]],)
            3*Lambda[1] - 3*Lambda[2]
            Family ()
            4*Lambda[1] - 5*Lambda[2]
            Family ()
            -Lambda[1] + 2*Lambda[2]
            Family (f[-alpha[1]]*u[Lambda[1] + Lambda[2]],)
            0
            Family (f[-alpha[1] - alpha[2]]*u[Lambda[1] + Lambda[2]], f[-alpha[2]]*f[-alpha[1]]*u[Lambda[1] + Lambda[2]])
            Lambda[1] - 2*Lambda[2]
            Family (f[-alpha[2]]*f[-alpha[1] - alpha[2]]*u[Lambda[1] + Lambda[2]],)
            2*Lambda[1] - 4*Lambda[2]
            Family ()
            -3*Lambda[1] + 3*Lambda[2]
            Family ()
            -2*Lambda[1] + Lambda[2]
            Family (f[-alpha[1]]*f[-alpha[1] - alpha[2]]*u[Lambda[1] + Lambda[2]],)
            -Lambda[1] - Lambda[2]
            Family (f[-alpha[1] - alpha[2]]^2*u[Lambda[1] + Lambda[2]],)
            -3*Lambda[2]
            Family ()
            -5*Lambda[1] + 4*Lambda[2]
            Family ()
            -4*Lambda[1] + 2*Lambda[2]
            Family ()
            -3*Lambda[1]
            Family ()
            -2*Lambda[1] - 2*Lambda[2]
            Family ()
        """
    weight_space_basis = homogeneous_component_basis
    class Element(CombinatorialFreeModule.Element): ...

class FiniteDimensionalSimpleModule(SimpleModule):
    """
    A finite dimensional simple module.
    """
    def bgg_resolution(self):
        """
        Return the BGG resolution of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: L = g.simple_module(La[1] + La[2])
            sage: L.bgg_resolution()
            BGG resolution of Simple module with highest weight Lambda[1] + Lambda[2]
             of Lie algebra of ['A', 2] in the Chevalley basis
        """
