from sage.categories.homset import Hom as Hom, Homset as Homset
from sage.categories.modules import Modules as Modules
from sage.categories.morphism import Morphism as Morphism
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.richcmp import richcmp as richcmp

class ModulePrinting:
    """
    Helper mixin class for printing the module vectors.
    """
    def __init__(self, vector_name: str = 'v') -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.verma_module import ModulePrinting
            sage: MP = ModulePrinting()
            sage: TestSuite(MP).run(skip="_test_pickling")
        '''

class VermaModule(ModulePrinting, CombinatorialFreeModule):
    """
    A Verma module.

    Let `\\lambda` be a weight and `\\mathfrak{g}` be a Kac--Moody Lie
    algebra with a fixed Borel subalgebra `\\mathfrak{b} = \\mathfrak{h}
    \\oplus \\mathfrak{g}^+`. The *Verma module* `M_{\\lambda}` is a
    `U(\\mathfrak{g})`-module given by

    .. MATH::

        M_{\\lambda} := U(\\mathfrak{g}) \\otimes_{U(\\mathfrak{b})} F_{\\lambda},

    where `F_{\\lambda}` is the `U(\\mathfrak{b})` module such that
    `h \\in U(\\mathfrak{h})` acts as multiplication by
    `\\langle \\lambda, h \\rangle` and `U(\\mathfrak{g}^+) F_{\\lambda} = 0`.

    INPUT:

    - ``g`` -- a Lie algebra
    - ``weight`` -- a weight

    EXAMPLES::

        sage: L = lie_algebras.sl(QQ, 3)
        sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
        sage: M = L.verma_module(2*La[1] + 3*La[2])
        sage: pbw = M.pbw_basis()
        sage: E1,E2,F1,F2,H1,H2 = [pbw(g) for g in L.gens()]
        sage: v = M.highest_weight_vector()
        sage: x = F2^3 * F1 * v
        sage: x
        f[-alpha[2]]^3*f[-alpha[1]]*v[2*Lambda[1] + 3*Lambda[2]]
        sage: F1 * x
        f[-alpha[2]]^3*f[-alpha[1]]^2*v[2*Lambda[1] + 3*Lambda[2]]
         + 3*f[-alpha[2]]^2*f[-alpha[1]]*f[-alpha[1] - alpha[2]]*v[2*Lambda[1] + 3*Lambda[2]]
        sage: E1 * x
        2*f[-alpha[2]]^3*v[2*Lambda[1] + 3*Lambda[2]]
        sage: H1 * x
        3*f[-alpha[2]]^3*f[-alpha[1]]*v[2*Lambda[1] + 3*Lambda[2]]
        sage: H2 * x
        -2*f[-alpha[2]]^3*f[-alpha[1]]*v[2*Lambda[1] + 3*Lambda[2]]

    REFERENCES:

    - :wikipedia:`Verma_module`
    """
    def __init__(self, g, weight, basis_key=None, prefix: str = 'f', **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + 4*La[2])
            sage: TestSuite(M).run()
            sage: M = L.verma_module(La[1] - 2*La[2])
            sage: TestSuite(M).run()

            sage: L = lie_algebras.sp(QQ, 4)
            sage: La = L.cartan_type().root_system().ambient_space().fundamental_weights()
            sage: M = L.verma_module(-1/2*La[1] + 3/7*La[2])
            sage: TestSuite(M).run()
        """
    def lie_algebra(self):
        """
        Return the underlying Lie algebra of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.so(QQ, 9)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = L.verma_module(La[3] - 1/2*La[1])
            sage: M.lie_algebra()
            Lie algebra of ['B', 4] in the Chevalley basis
        """
    def pbw_basis(self):
        """
        Return the PBW basis of the underlying Lie algebra
        used to define ``self``.

        EXAMPLES::

            sage: L = lie_algebras.so(QQ, 8)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[2] - 2*La[3])
            sage: M.pbw_basis()
            Universal enveloping algebra of Lie algebra of ['D', 4] in the Chevalley basis
             in the Poincare-Birkhoff-Witt basis
        """
    poincare_birkhoff_witt_basis = pbw_basis
    @cached_method
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sp(QQ, 6)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] - 3*La[2])
            sage: M.highest_weight_vector()
            v[Lambda[1] - 3*Lambda[2]]
        """
    def gens(self) -> tuple:
        """
        Return the generators of ``self`` as a `U(\\mathfrak{g})`-module.

        EXAMPLES::

            sage: L = lie_algebras.sp(QQ, 6)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] - 3*La[2])
            sage: M.gens()
            (v[Lambda[1] - 3*Lambda[2]],)
        """
    def highest_weight(self):
        """
        Return the highest weight of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.so(QQ, 7)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = L.verma_module(4*La[1] - 3/2*La[2])
            sage: M.highest_weight()
            4*Lambda[1] - 3/2*Lambda[2]
        """
    def dual(self):
        """
        Return the dual module `M(\\lambda)^{\\vee}` in Category `\\mathcal{O}`.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 2)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = L.verma_module(2*La[1])
            sage: Mc = M.dual()

            sage: Mp = L.verma_module(-2*La[1])
            sage: Mp.dual() is Mp
            True
        """
    def degree_on_basis(self, m):
        """
        Return the degree (or weight) of the basis element indexed by ``m``.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(2*La[1] + 3*La[2])
            sage: v = M.highest_weight_vector()
            sage: M.degree_on_basis(v.leading_support())
            2*Lambda[1] + 3*Lambda[2]

            sage: pbw = M.pbw_basis()
            sage: G = list(pbw.gens())
            sage: f1, f2 = L.f()
            sage: x = pbw(f1.bracket(f2)) * pbw(f1) * v
            sage: x.degree()
            -Lambda[1] + 3*Lambda[2]
        """
    def contravariant_form(self, x, y):
        """
        Return the contravariant form of ``x`` and ``y``.

        Let `C(x, y)` denote the (universal) contravariant form on
        `U(\\mathfrak{g})`. Then the contravariant form on `M(\\lambda)` is
        given by evaluating `C(x, y) \\in U(\\mathfrak{h})` at `\\lambda`.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 1])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = g.verma_module(2*La[1])
            sage: U = M.pbw_basis()
            sage: v = M.highest_weight_vector()
            sage: e, h, f = U.algebra_generators()
            sage: elts = [f^k * v for k in range(8)]; elts
            [v[2*Lambda[1]], f[-alpha[1]]*v[2*Lambda[1]],
             f[-alpha[1]]^2*v[2*Lambda[1]], f[-alpha[1]]^3*v[2*Lambda[1]],
             f[-alpha[1]]^4*v[2*Lambda[1]], f[-alpha[1]]^5*v[2*Lambda[1]],
             f[-alpha[1]]^6*v[2*Lambda[1]], f[-alpha[1]]^7*v[2*Lambda[1]]]
            sage: matrix([[M.contravariant_form(x, y) for x in elts] for y in elts])
            [1 0 0 0 0 0 0 0]
            [0 2 0 0 0 0 0 0]
            [0 0 4 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
        """
    def is_singular(self):
        """
        Return if ``self`` is a singular Verma module.

        A Verma module `M_{\\lambda}` is *singular* if there does not
        exist a dominant weight `\\tilde{\\lambda}` that is in the dot
        orbit of `\\lambda`. We call a Verma module *regular* otherwise.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: M.is_singular()
            False
            sage: M = L.verma_module(La[1] - La[2])
            sage: M.is_singular()
            True
            sage: M = L.verma_module(2*La[1] - 10*La[2])
            sage: M.is_singular()
            False
            sage: M = L.verma_module(-2*La[1] - 2*La[2])
            sage: M.is_singular()
            False
            sage: M = L.verma_module(-4*La[1] - La[2])
            sage: M.is_singular()
            True
        """
    def is_simple(self):
        """
        Return if ``self`` is a simple module.

        A Verma module `M_{\\lambda}` is simple if and only if `\\lambda`
        is *Verma antidominant* in the sense

        .. MATH::

            \\langle \\lambda + \\rho, \\alpha^{\\vee} \\rangle \\notin \\ZZ_{>0}

        for all positive roots `\\alpha`.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: L.verma_module(La[1] + La[2]).is_simple()
            False
            sage: L.verma_module(-La[1] - La[2]).is_simple()
            True
            sage: L.verma_module(3/2*La[1] + 1/2*La[2]).is_simple()
            False
            sage: L.verma_module(3/2*La[1] + 1/3*La[2]).is_simple()
            True
            sage: L.verma_module(-3*La[1] + 2/3*La[2]).is_simple()
            True
        """
    def is_projective(self):
        """
        Return if ``self`` is a projective module in Category `\\mathcal{O}`.

        A Verma module `M_{\\lambda}` is projective (in Category `\\mathcal{O}`
        if and only if `\\lambda` is *Verma dominant* in the sense

        .. MATH::

            \\langle \\lambda + \\rho, \\alpha^{\\vee} \\rangle \\notin \\ZZ_{<0}

        for all positive roots `\\alpha`.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: L.verma_module(La[1] + La[2]).is_projective()
            True
            sage: L.verma_module(-La[1] - La[2]).is_projective()
            True
            sage: L.verma_module(3/2*La[1] + 1/2*La[2]).is_projective()
            True
            sage: L.verma_module(3/2*La[1] + 1/3*La[2]).is_projective()
            True
            sage: L.verma_module(-3*La[1] + 2/3*La[2]).is_projective()
            False
        """
    def homogeneous_component_basis(self, d):
        """
        Return a basis for the ``d``-th homogeneous component of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: P = L.cartan_type().root_system().weight_lattice()
            sage: La = P.fundamental_weights()
            sage: al = P.simple_roots()
            sage: mu = 2*La[1] + 3*La[2]
            sage: M = L.verma_module(mu)
            sage: M.homogeneous_component_basis(mu - al[2])
            [f[-alpha[2]]*v[2*Lambda[1] + 3*Lambda[2]]]
            sage: M.homogeneous_component_basis(mu - 3*al[2])
            [f[-alpha[2]]^3*v[2*Lambda[1] + 3*Lambda[2]]]
            sage: M.homogeneous_component_basis(mu - 3*al[2] - 2*al[1])
            [f[-alpha[2]]*f[-alpha[1] - alpha[2]]^2*v[2*Lambda[1] + 3*Lambda[2]],
             f[-alpha[2]]^2*f[-alpha[1]]*f[-alpha[1] - alpha[2]]*v[2*Lambda[1] + 3*Lambda[2]],
             f[-alpha[2]]^3*f[-alpha[1]]^2*v[2*Lambda[1] + 3*Lambda[2]]]
            sage: M.homogeneous_component_basis(mu - La[1])
            Family ()
        """
    weight_space_basis = homogeneous_component_basis
    class Element(CombinatorialFreeModule.Element): ...

class VermaModuleMorphism(Morphism):
    """
    A morphism of a Verma module to another module in Category `\\mathcal{O}`.
    """
    def __init__(self, parent, scalar) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([1,2]))
            sage: phi = Hom(Mp, M).natural_map()
            sage: TestSuite(phi).run()
        """
    def is_injective(self):
        """
        Return if ``self`` is injective or not.

        A morphism `\\phi : M \\to M'` from a Verma module `M` to another
        Verma module `M'` is injective if and only if `\\dim \\hom(M, M') = 1`
        and `\\phi \\neq 0`. If `M'` is a dual Verma or simple module, then
        the result is not injective.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([1,2]))
            sage: Mpp = L.verma_module(M.highest_weight().dot_action([1,2]) + La[1])
            sage: phi = Hom(Mp, M).natural_map()
            sage: phi.is_injective()
            True
            sage: (0 * phi).is_injective()
            False
            sage: psi = Hom(Mpp, Mp).natural_map()
            sage: psi.is_injective()
            False
        """
    def is_surjective(self):
        """
        Return if ``self`` is surjective or not.

        A morphism `\\phi : M \\to M'` from a Verma module `M` to another
        Verma module `M'` is surjective if and only if the domain is
        equal to the codomain and it is not the zero morphism.

        If `M'` is a simple module, then this surjective if and only if
        `\\dim \\hom(M, M') = 1` and `\\phi \\neq 0`.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([1,2]))
            sage: phi = Hom(M, M).natural_map()
            sage: phi.is_surjective()
            True
            sage: (0 * phi).is_surjective()
            False
            sage: psi = Hom(Mp, M).natural_map()
            sage: psi.is_surjective()
            False
        """
    def image(self):
        """
        Return the image of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = g.verma_module(La[1] + 2*La[2])
            sage: Mp = g.verma_module(La[1] + 3*La[2])
            sage: phi = Hom(M, Mp).natural_map()
            sage: phi.image()
            Free module generated by {} over Rational Field
            sage: Mc = M.dual()
            sage: phi = Hom(M, Mc).natural_map()
            sage: L = phi.image(); L
            Simple module with highest weight Lambda[1] + 2*Lambda[2] of
             Lie algebra of ['B', 2] in the Chevalley basis
            sage: psi = Hom(M, L).natural_map()
            sage: psi.image()
            Simple module with highest weight Lambda[1] + 2*Lambda[2] of
             Lie algebra of ['B', 2] in the Chevalley basis
        """

class VermaModuleHomset(Homset):
    """
    The set of morphisms from a Verma module to another module in
    Category `\\mathcal{O}` considered as `U(\\mathfrak{g})`-representations.

    This currently assumes the codomain is a Verma module, its dual,
    or a simple module.

    Let `M_{w \\cdot \\lambda}` and `M_{w' \\cdot \\lambda'}` be
    Verma modules, `\\cdot` is the dot action, and `\\lambda + \\rho`,
    `\\lambda' + \\rho` are dominant weights. Then we have

    .. MATH::

        \\dim \\hom(M_{w \\cdot \\lambda}, M_{w' \\cdot \\lambda'}) = 1

    if and only if `\\lambda = \\lambda'` and `w' \\leq w` in Bruhat
    order. Otherwise the homset is 0 dimensional.

    If the codomain is a dual Verma module `M_{\\mu}^{\\vee}`, then the
    homset is `\\delta_{\\lambda\\mu}` dimensional. When `\\mu = \\lambda`,
    the image is the simple module `L_{\\lambda}`.
    """
    def __call__(self, x, **options):
        """
        Construct a morphism in this homset from ``x`` if possible.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([1,2]))
            sage: Mpp = L.verma_module(M.highest_weight().dot_action([1,2,1]))
            sage: phi = Hom(Mp, M).natural_map()
            sage: Hom(Mpp, M)(phi)
            Verma module morphism:
              From: Verma module with highest weight -3*Lambda[1] - 3*Lambda[2]
                     of Lie algebra of ['A', 2] in the Chevalley basis
              To:   Verma module with highest weight Lambda[1] + Lambda[2]
                     of Lie algebra of ['A', 2] in the Chevalley basis
              Defn: v[-3*Lambda[1] - 3*Lambda[2]] |-->
                     f[-alpha[2]]^4*f[-alpha[1]]^4*v[Lambda[1] + Lambda[2]]
                       + 8*f[-alpha[2]]^3*f[-alpha[1]]^3*f[-alpha[1] - alpha[2]]*v[Lambda[1] + Lambda[2]]
                       + 12*f[-alpha[2]]^2*f[-alpha[1]]^2*f[-alpha[1] - alpha[2]]^2*v[Lambda[1] + Lambda[2]]

            sage: psi = Hom(Mpp, Mp).natural_map()
            sage: Hom(Mpp, M)(psi)
            Verma module morphism:
              From: Verma module with highest weight -3*Lambda[1] - 3*Lambda[2]
                     of Lie algebra of ['A', 2] in the Chevalley basis
              To:   Verma module with highest weight Lambda[1] + Lambda[2]
                     of Lie algebra of ['A', 2] in the Chevalley basis
              Defn: v[-3*Lambda[1] - 3*Lambda[2]] |-->
                     f[-alpha[2]]^4*f[-alpha[1]]^4*v[Lambda[1] + Lambda[2]]
                      + 8*f[-alpha[2]]^3*f[-alpha[1]]^3*f[-alpha[1] - alpha[2]]*v[Lambda[1] + Lambda[2]]
                      + 12*f[-alpha[2]]^2*f[-alpha[1]]^2*f[-alpha[1] - alpha[2]]^2*v[Lambda[1] + Lambda[2]]
        """
    def highest_weight_image(self):
        """
        Return the image of the highest weight vector of the domain
        in the codomain.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['C', 3])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = g.verma_module(La[1] + 2*La[3])
            sage: Mc = M.dual()
            sage: H = Hom(M, Mc)
            sage: H.highest_weight_image()
            v[Lambda[1] + 2*Lambda[3]]^*
            sage: L = H.natural_map().image()
            sage: Hp = Hom(M, L)
            sage: Hp.highest_weight_image()
            u[Lambda[1] + 2*Lambda[3]]
        """
    @cached_method
    def singular_vector(self):
        """
        Return the singular vector in the codomain corresponding
        to the domain's highest weight element or ``None`` if no
        such element exists.

        ALGORITHM:

        We essentially follow the algorithm laid out in [deG2005]_.
        We split the main computation into two cases. If there exists
        an `i` such that `\\langle \\lambda + \\rho, \\alpha_i^{\\vee}
        \\rangle = m > 0` (i.e., the weight `\\lambda` is `i`-dominant
        with respect to the dot action), then we use the `\\mathfrak{sl}_2`
        relation on `M_{s_i \\cdot \\lambda} \\to M_{\\lambda}` to
        construct the singular vector `f_i^m v_{\\lambda}`. Otherwise
        we find the shortest root `\\alpha` such that `\\langle \\lambda
        + \\rho, \\alpha^{\\vee} \\rangle > 0` and explicitly compute the
        kernel with respect to the weight basis elements. We iterate
        this until we reach `\\mu`.

        EXAMPLES::

            sage: L = lie_algebras.sp(QQ, 6)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: la = La[1] - La[3]
            sage: mu = la.dot_action([1,2])
            sage: M = L.verma_module(la)
            sage: Mp = L.verma_module(mu)
            sage: H = Hom(Mp, M)
            sage: v = H.singular_vector(); v
            f[-alpha[2]]*f[-alpha[1]]^3*v[Lambda[1] - Lambda[3]]
             + 3*f[-alpha[1]]^2*f[-alpha[1] - alpha[2]]*v[Lambda[1] - Lambda[3]]
            sage: v.degree() == Mp.highest_weight()
            True

        ::

            sage: L = LieAlgebra(QQ, cartan_type=['F', 4])
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: la = La[1] + La[2] - La[3]
            sage: mu = la.dot_action([1,2,3,2])
            sage: M = L.verma_module(la)
            sage: Mp = L.verma_module(mu)
            sage: H = Hom(Mp, M)
            sage: v = H.singular_vector()
            sage: pbw = M.pbw_basis()
            sage: E = [pbw(e) for e in L.e()]
            sage: all(e * v == M.zero() for e in E)  # long time
            True
            sage: v.degree() == Mp.highest_weight()
            True

        When `w \\cdot \\lambda \\notin \\lambda + Q^-`, there does not
        exist a singular vector::

            sage: L = lie_algebras.sl(QQ, 4)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: la = 3/7*La[1] - 1/2*La[3]
            sage: mu = la.dot_action([1,2])
            sage: M = L.verma_module(la)
            sage: Mp = L.verma_module(mu)
            sage: H = Hom(Mp, M)
            sage: H.singular_vector() is None
            True

        When we need to apply a non-simple reflection, we can compute
        the singular vector (see :issue:`36793`)::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: La = g.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = g.verma_module((0*La[1]).dot_action([1]))
            sage: Mp = g.verma_module((0*La[1]).dot_action([1,2]))
            sage: H = Hom(Mp, M)
            sage: v = H.singular_vector(); v
            1/2*f[-alpha[2]]*f[-alpha[1]]*v[-2*Lambda[1] + Lambda[2]]
             + f[-alpha[1] - alpha[2]]*v[-2*Lambda[1] + Lambda[2]]
            sage: pbw = M.pbw_basis()
            sage: E = [pbw(e) for e in g.e()]
            sage: all(e * v == M.zero() for e in E)
            True
            sage: v.degree() == Mp.highest_weight()
            True

        TESTS::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: al = L.cartan_type().root_system().root_lattice().simple_roots()
            sage: M = L.verma_module(La[1] + La[2])
            sage: pbw = M.pbw_basis()
            sage: E = {i: pbw(L.e(i)) for i in L.cartan_type().index_set()}
            sage: all(not E[i] * Hom(L.verma_module(mu), M).singular_vector()
            ....:     for i in L.cartan_type().index_set()
            ....:     for mu in M.highest_weight().dot_orbit())
            True
        """
    @cached_method
    def natural_map(self):
        '''
        Return the "natural map" of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([2]))
            sage: H = Hom(Mp, M)
            sage: H.natural_map()
            Verma module morphism:
              From: Verma module with highest weight 3*Lambda[1] - 3*Lambda[2]
                     of Lie algebra of [\'A\', 2] in the Chevalley basis
              To:   Verma module with highest weight Lambda[1] + Lambda[2]
                     of Lie algebra of [\'A\', 2] in the Chevalley basis
              Defn: v[3*Lambda[1] - 3*Lambda[2]] |-->
                     f[-alpha[2]]^2*v[Lambda[1] + Lambda[2]]

            sage: Mp = L.verma_module(La[1] + 2*La[2])
            sage: H = Hom(Mp, M)
            sage: H.natural_map()
            Verma module morphism:
              From: Verma module with highest weight Lambda[1] + 2*Lambda[2]
                     of Lie algebra of [\'A\', 2] in the Chevalley basis
              To:   Verma module with highest weight Lambda[1] + Lambda[2]
                     of Lie algebra of [\'A\', 2] in the Chevalley basis
              Defn: v[Lambda[1] + 2*Lambda[2]] |--> 0
        '''
    @cached_method
    def zero(self):
        """
        Return the zero morphism of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sp(QQ, 6)
            sage: La = L.cartan_type().root_system().weight_space().fundamental_weights()
            sage: M = L.verma_module(La[1] + 2/3*La[2])
            sage: Mp = L.verma_module(La[2] - La[3])
            sage: H = Hom(Mp, M)
            sage: H.zero()
            Verma module morphism:
              From: Verma module with highest weight Lambda[2] - Lambda[3]
                     of Lie algebra of ['C', 3] in the Chevalley basis
              To:   Verma module with highest weight Lambda[1] + 2/3*Lambda[2]
                     of Lie algebra of ['C', 3] in the Chevalley basis
              Defn: v[Lambda[2] - Lambda[3]] |--> 0
        """
    def dimension(self):
        """
        Return the dimension of ``self`` (as a vector space over
        the base ring).

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([2]))
            sage: H = Hom(Mp, M)
            sage: H.dimension()
            1

            sage: Mp = L.verma_module(La[1] + 2*La[2])
            sage: H = Hom(Mp, M)
            sage: H.dimension()
            0
        """
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: L = lie_algebras.sl(QQ, 3)
            sage: La = L.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: M = L.verma_module(La[1] + La[2])
            sage: Mp = L.verma_module(M.highest_weight().dot_action([2]))
            sage: H = Hom(Mp, M)
            sage: list(H.basis()) == [H.natural_map()]
            True

            sage: Mp = L.verma_module(La[1] + 2*La[2])
            sage: H = Hom(Mp, M)
            sage: H.basis()
            Family ()
        """
    Element = VermaModuleMorphism
