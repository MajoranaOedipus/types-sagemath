from sage.manifolds.differentiable.diff_form import DiffForm as DiffForm, DiffFormParal as DiffFormParal
from sage.manifolds.differentiable.diff_map import DiffMap as DiffMap
from sage.manifolds.differentiable.manifold import DifferentiableManifold as DifferentiableManifold
from sage.manifolds.differentiable.poisson_tensor import PoissonTensorField as PoissonTensorField
from sage.manifolds.differentiable.scalarfield import DiffScalarField as DiffScalarField
from sage.manifolds.differentiable.tensorfield import TensorField as TensorField
from sage.manifolds.differentiable.tensorfield_paral import TensorFieldParal as TensorFieldParal
from sage.manifolds.differentiable.vectorfield import VectorField as VectorField
from sage.manifolds.differentiable.vectorfield_module import VectorFieldModule as VectorFieldModule
from sage.symbolic.expression import Expression as Expression

class SymplecticForm(DiffForm):
    """
    A symplectic form on a differentiable manifold.

    An instance of this class is a closed nondegenerate differential `2`-form `\\omega`
    on a differentiable manifold `M` over `\\RR`.

    In particular, at each point `m \\in M`, `\\omega_m` is a bilinear map of the type:

    .. MATH::

        \\omega_m:\\ T_m M \\times T_m M  \\to \\RR,

    where `T_m M` stands for the tangent space to the
    manifold `M` at the point `m`, such that `\\omega_m` is skew-symmetric:
    `\\forall u,v \\in T_m M, \\ \\omega_m(v,u) = - \\omega_m(u,v)`
    and nondegenerate:
    `(\\forall v \\in T_m M,\\ \\ \\omega_m(u,v) = 0) \\Longrightarrow u=0`.

    .. NOTE::

        If `M` is parallelizable, the class :class:`SymplecticFormParal`
        should be used instead.

    INPUT:

    - ``manifold`` -- module `\\mathfrak{X}(M)` of vector fields on the
      manifold `M`, or the manifold `M` itself
    - ``name`` -- (default: ``omega``) name given to the symplectic form
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
      symplectic form; if ``None``, it is formed from ``name``

    EXAMPLES:

    A symplectic form on the 2-sphere::

        sage: M.<x,y> = manifolds.Sphere(2, coordinates='stereographic')
        sage: stereoN = M.stereographic_coordinates(pole='north')
        sage: stereoS = M.stereographic_coordinates(pole='south')
        sage: omega = M.symplectic_form(name='omega', latex_name=r'\\omega')
        sage: omega
        Symplectic form omega on the 2-sphere S^2 of radius 1 smoothly embedded
         in the Euclidean space E^3

    ``omega`` is initialized by providing its single nonvanishing component
    w.r.t. the vector frame associated to ``stereoN``, which is the default
    frame on ``M``::

        sage: omega[1, 2] = 1/(1 + x^2 + y^2)^2

    The components w.r.t. the vector frame associated to ``stereoS`` are
    obtained thanks to the method
    :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.add_comp_by_continuation`::

        sage: omega.add_comp_by_continuation(stereoS.frame(),
        ....:                  stereoS.domain().intersection(stereoN.domain()))
        sage: omega.display()
        omega = (x^2 + y^2 + 1)^(-2) dx∧dy
        sage: omega.display(stereoS)
        omega = -1/(xp^4 + yp^4 + 2*(xp^2 + 1)*yp^2 + 2*xp^2 + 1) dxp∧dyp

    ``omega`` is an exact 2-form (this is trivial here, since ``M`` is
    2-dimensional)::

        sage: diff(omega).display()
        domega = 0
    """
    def __init__(self, manifold: DifferentiableManifold | VectorFieldModule, name: str | None = None, latex_name: str | None = None) -> None:
        """
        Construct a symplectic form.

        TESTS::

            sage: from sage.manifolds.differentiable.symplectic_form import SymplecticForm
            sage: M = manifolds.Sphere(2, coordinates='stereographic')
            sage: omega = SymplecticForm(M, name='omega', latex_name=r'\\omega')
            sage: omega
            Symplectic form omega on the 2-sphere S^2 of radius 1 smoothly
             embedded in the Euclidean space E^3
        """
    def restrict(self, subdomain: DifferentiableManifold, dest_map: DiffMap | None = None) -> DiffForm:
        """
        Return the restriction of the symplectic form to some subdomain.

        If the restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` -- open subset `U` of the symplectic form's domain
        - ``dest_map`` -- (default: ``None``) smooth destination map
          `\\Phi:\\ U \\to V`, where `V` is a subdomain of the symplectic form's domain
          If ``None``, the restriction of the initial vector field module is used.

        OUTPUT: the restricted symplectic form

        EXAMPLES::

            sage: M = Manifold(6, 'M')
            sage: omega = M.symplectic_form()
            sage: U = M.open_subset('U')
            sage: omega.restrict(U)
            2-form omega on the Open subset U of the 6-dimensional differentiable manifold M
        """
    @staticmethod
    def wrap(form: DiffForm, name: str | None = None, latex_name: str | None = None) -> SymplecticForm:
        """
        Define the symplectic form from a differential form.

        INPUT:

        - ``form`` -- differential `2`-form

        EXAMPLES:

        Volume form on the sphere as a symplectic form::

            sage: from sage.manifolds.differentiable.symplectic_form import SymplecticForm
            sage: M = manifolds.Sphere(2, coordinates='stereographic')
            sage: vol_form = M.induced_metric().volume_form()                   # long time
            sage: omega = SymplecticForm.wrap(vol_form, 'omega', r'\\omega')     # long time
            sage: omega.display()                                               # long time
            omega = -4/(y1^4 + y2^4 + 2*(y1^2 + 1)*y2^2 + 2*y1^2 + 1) dy1∧dy2
        """
    def poisson(self, expansion_symbol: Expression | None = None, order: int = 1) -> PoissonTensorField:
        """
        Return the Poisson tensor associated with the symplectic form.

        INPUT:

        - ``expansion_symbol`` -- (default: ``None``) symbolic variable; if
          specified, the inverse will be expanded in power series with respect
          to this variable (around its zero value)
        - ``order`` -- integer (default: 1); the order of the expansion
          if ``expansion_symbol`` is not ``None``; the *order* is defined as
          the degree of the polynomial representing the truncated power series
          in ``expansion_symbol``; currently only first order inverse is
          supported

        If ``expansion_symbol`` is set, then the zeroth order symplectic form must be
        invertible. Moreover, subsequent calls to this method will return
        a cached value, even when called with the default value (to enable
        computation of derived quantities). To reset, use :meth:`_del_derived`.

        OUTPUT:

        - the Poisson tensor, as an instance of
          :meth:`~sage.manifolds.differentiable.poisson_tensor.PoissonTensorField`

        EXAMPLES:

        Poisson tensor of `2`-dimensional symplectic vector space::

            sage: M = manifolds.StandardSymplecticSpace(2)
            sage: omega = M.symplectic_form()
            sage: poisson = omega.poisson(); poisson
            2-vector field poisson_omega on the Standard symplectic space R2
            sage: poisson.display()
            poisson_omega = -e_q∧e_p
        """
    def hamiltonian_vector_field(self, function: DiffScalarField) -> VectorField:
        """
        The Hamiltonian vector field `X_f` generated by a function `f: M \\to \\RR`.

        The Hamiltonian vector field is defined by

        .. MATH::

            X_f \\lrcorner \\omega + df = 0.

        INPUT:

        - ``function`` -- the function generating the Hamiltonian vector field

        EXAMPLES::

            sage: M = manifolds.StandardSymplecticSpace(2)
            sage: omega = M.symplectic_form()
            sage: f = M.scalar_field({ chart: function('f')(*chart[:]) for chart in M.atlas() }, name='f')
            sage: f.display()
            f: R2 → ℝ
               (q, p) ↦ f(q, p)
            sage: Xf = omega.hamiltonian_vector_field(f)
            sage: Xf.display()
            Xf = d(f)/dp e_q - d(f)/dq e_p
        """
    def flat(self, vector_field: VectorField) -> DiffForm:
        """
        Return the image of the given differential form under the
        map `\\omega^\\flat: T M \\to T^*M` defined by

        .. MATH::

            <\\omega^\\flat(X), Y> = \\omega_m (X, Y)

        for all `X, Y \\in T_m M`.

        In indices, `X_i = \\omega_{ji} X^j`.

        INPUT:

        - ``vector_field`` -- the vector field to calculate its flat of

        EXAMPLES::

            sage: M = manifolds.StandardSymplecticSpace(2)
            sage: omega = M.symplectic_form()
            sage: X = M.vector_field_module().an_element()
            sage: X.set_name('X')
            sage: X.display()
            X = 2 e_q + 2 e_p
            sage: omega.flat(X).display()
            X_flat = 2 dq - 2 dp
        """
    def sharp(self, form: DiffForm) -> VectorField:
        """
        Return the image of the given differential form under the map
        `\\omega^\\sharp: T^* M \\to TM` defined by

        .. MATH::

            \\omega (\\omega^\\sharp(\\alpha), X) = \\alpha(X)

        for all `X \\in T_m M` and `\\alpha \\in T^*_m M`.
        The sharp map is inverse to the flat map.

        In indices, `\\alpha^i = \\varpi^{ij} \\alpha_j`, where `\\varpi` is
        the Poisson tensor associated with the symplectic form.

        INPUT:

        - ``form`` -- the differential form to calculate its sharp of

        EXAMPLES::

            sage: M = manifolds.StandardSymplecticSpace(2)
            sage: omega = M.symplectic_form()
            sage: X = M.vector_field_module().an_element()
            sage: alpha = omega.flat(X)
            sage: alpha.set_name('alpha')
            sage: alpha.display()
            alpha = 2 dq - 2 dp
            sage: omega.sharp(alpha).display()
            alpha_sharp = 2 e_q + 2 e_p
        """
    def poisson_bracket(self, f: DiffScalarField, g: DiffScalarField) -> DiffScalarField:
        """
        Return the Poisson bracket

        .. MATH::

            \\{f, g\\} = \\omega(X_f, X_g)

        of the given functions.

        INPUT:

        - ``f`` -- function inserted in the first slot
        - ``g`` -- function inserted in the second slot

        EXAMPLES::

            sage: M.<q, p> = EuclideanSpace(2)
            sage: poisson = M.poisson_tensor('varpi')
            sage: poisson.set_comp()[1,2] = -1
            sage: f = M.scalar_field({ chart: function('f')(*chart[:]) for chart in M.atlas() }, name='f')
            sage: g = M.scalar_field({ chart: function('g')(*chart[:]) for chart in M.atlas() }, name='g')
            sage: poisson.poisson_bracket(f, g).display()
            poisson(f, g): E^2 → ℝ
               (q, p) ↦ d(f)/dp*d(g)/dq - d(f)/dq*d(g)/dp
        """
    def volume_form(self, contra: int = 0) -> TensorField:
        """
        Liouville volume form `\\frac{1}{n!}\\omega^n` associated with the
        symplectic form `\\omega`, where `2n` is the dimension of the manifold.

        INPUT:

        - ``contra`` -- (default: 0) number of contravariant indices of the
          returned tensor

        OUTPUT:

        - if ``contra = 0``: volume form associated with the symplectic form
        - if ``contra = k``, with `1\\leq k \\leq n`, the tensor field of type
          (k,n-k) formed from `\\epsilon` by raising the first k indices with
          the symplectic form (see method
          :meth:`~sage.manifolds.differentiable.tensorfield.TensorField.up`)

        EXAMPLES:

        Volume form on `\\RR^4`::

            sage: M = manifolds.StandardSymplecticSpace(4)
            sage: omega = M.symplectic_form()
            sage: vol = omega.volume_form() ; vol
            4-form mu_omega on the Standard symplectic space R4
            sage: vol.display()
            mu_omega = dq1∧dp1∧dq2∧dp2
        """
    def hodge_star(self, pform: DiffForm) -> DiffForm:
        """
        Compute the Hodge dual of a differential form with respect to the
        symplectic form.

        See :meth:`~sage.manifolds.differentiable.diff_form.DiffForm.hodge_dual`
        for the definition and more details.

        INPUT:

        - ``pform`` -- a `p`-form `A`; must be an instance of
          :class:`~sage.manifolds.differentiable.scalarfield.DiffScalarField`
          for `p=0` and of
          :class:`~sage.manifolds.differentiable.diff_form.DiffForm` or
          :class:`~sage.manifolds.differentiable.diff_form.DiffFormParal`
          for `p\\geq 1`.

        OUTPUT:

        - the `(n-p)`-form `*A`

        EXAMPLES:

        Hodge dual of any form on the symplectic vector space `R^2`::

            sage: M = manifolds.StandardSymplecticSpace(2)
            sage: omega = M.symplectic_form()
            sage: a = M.one_form(1, 0, name='a')
            sage: omega.hodge_star(a).display()
            *a = dq
            sage: b = M.one_form(0, 1, name='b')
            sage: omega.hodge_star(b).display()
            *b = dp
            sage: f = M.scalar_field(1, name='f')
            sage: omega.hodge_star(f).display()
            *f = -dq∧dp
            sage: omega.hodge_star(omega).display()
            *omega: R2 → ℝ
               (q, p) ↦ 1
        """
    def on_forms(self, first: DiffForm, second: DiffForm) -> DiffScalarField:
        """
        Return the contraction of the two forms with respect to the symplectic form.

        The symplectic form `\\omega` gives rise to a bilinear form,
        also denoted by `\\omega` on the space of `1`-forms by

        .. MATH::
            \\omega(\\alpha, \\beta) = \\omega(\\alpha^\\sharp, \\beta^\\sharp),

        where `\\alpha^\\sharp` is the dual of `\\alpha` with respect to `\\omega`, see
        :meth:`~sage.manifolds.differentiable.tensor_field.TensorField.up`.
        This bilinear form induces a bilinear form on the space of all forms determined
        by its value on decomposable elements as:

        .. MATH::
            \\omega(\\alpha_1 \\wedge \\ldots \\wedge\\alpha_p, \\beta_1 \\wedge \\ldots \\wedge\\beta_p)
            = det(\\omega(\\alpha_i, \\beta_j)).

        INPUT:

        - ``first`` -- a `p`-form `\\alpha`
        - ``second`` -- a `p`-form `\\beta`

        OUTPUT:

        - the scalar field `\\omega(\\alpha, \\beta)`

        EXAMPLES:

            sage: M = manifolds.StandardSymplecticSpace(2)
            sage: omega = M.symplectic_form()
            sage: a = M.one_form(1, 0, name='a')
            sage: b = M.one_form(0, 1, name='b')
            sage: omega.on_forms(a, b).display()
            R2 → ℝ
            (q, p) ↦ -1
        """

class SymplecticFormParal(SymplecticForm, DiffFormParal):
    '''
    A symplectic form on a parallelizable manifold.

    .. NOTE::

        If `M` is not parallelizable, the class :class:`SymplecticForm`
        should be used instead.

    INPUT:

    - ``manifold`` -- module `\\mathfrak{X}(M)` of vector fields on the
      manifold `M`, or the manifold `M` itself
    - ``name`` -- (default: ``omega``) name given to the symplectic form
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
      symplectic form; if ``None``, it is formed from ``name``

    EXAMPLES:

    Standard symplectic form on `\\RR^2`::

        sage: M.<q, p> = EuclideanSpace(name=\'R2\', latex_name=r"\\mathbb{R}^2")
        sage: omega = M.symplectic_form(name=\'omega\', latex_name=r\'\\omega\')
        sage: omega
        Symplectic form omega on the Euclidean plane R2
        sage: omega.set_comp()[1,2] = -1
        sage: omega.display()
        omega = -dq∧dp
    '''
    def __init__(self, manifold: VectorFieldModule | DifferentiableManifold, name: str | None, latex_name: str | None = None) -> None:
        """
        Construct a symplectic form.

        TESTS::

            sage: from sage.manifolds.differentiable.symplectic_form import SymplecticFormParal
            sage: M = EuclideanSpace(2)
            sage: omega = SymplecticFormParal(M, name='omega', latex_name=r'\\omega')
            sage: omega
            Symplectic form omega on the Euclidean plane E^2
        """
    def restrict(self, subdomain: DifferentiableManifold, dest_map: DiffMap | None = None) -> SymplecticFormParal:
        '''
        Return the restriction of the symplectic form to some subdomain.

        If the restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` -- open subset `U` of the symplectic form\'s domain
        - ``dest_map`` -- (default: ``None``) smooth destination map
          `\\Phi:\\ U \\rightarrow V`, where `V` is a subdomain of the symplectic form\'s domain.
          If ``None``, the restriction of the initial vector field module is used.

        OUTPUT: the restricted symplectic form

        EXAMPLES:

        Restriction of the standard symplectic form on `\\RR^2` to the upper half plane::

            sage: from sage.manifolds.differentiable.symplectic_form import SymplecticFormParal
            sage: M = EuclideanSpace(2, "R2", r"\\mathbb{R}^2", symbols=r"q:q p:p")
            sage: X.<q, p> = M.chart()
            sage: omega = SymplecticFormParal(M, \'omega\', r\'\\omega\')
            sage: omega[1,2] = -1
            sage: U = M.open_subset(\'U\', coord_def={X: q>0})
            sage: omegaU = omega.restrict(U); omegaU
            Symplectic form omega on the Open subset U of the Euclidean plane R2
            sage: omegaU.display()
            omega = -dq∧dp
        '''
    def poisson(self, expansion_symbol: Expression | None = None, order: int = 1) -> TensorFieldParal:
        '''
        Return the Poisson tensor associated with the symplectic form.

        INPUT:

        - ``expansion_symbol`` -- (default: ``None``) symbolic variable; if
          specified, the inverse will be expanded in power series with respect
          to this variable (around its zero value)
        - ``order`` -- integer (default: 1); the order of the expansion
          if ``expansion_symbol`` is not ``None``; the *order* is defined as
          the degree of the polynomial representing the truncated power series
          in ``expansion_symbol``; currently only first order inverse is
          supported

        If ``expansion_symbol`` is set, then the zeroth order symplectic form must be
        invertible. Moreover, subsequent calls to this method will return
        a cached value, even when called with the default value (to enable
        computation of derived quantities). To reset, use :meth:`_del_derived`.

        OUTPUT:

        - the Poisson tensor, , as an instance of
          :meth:`~sage.manifolds.differentiable.poisson_tensor.PoissonTensorFieldParal`

        EXAMPLES:

        Poisson tensor of `2`-dimensional symplectic vector space::

            sage: from sage.manifolds.differentiable.symplectic_form import SymplecticFormParal
            sage: M.<q, p> = EuclideanSpace(2, "R2", r"\\mathbb{R}^2", symbols=r"q:q p:p")
            sage: omega = SymplecticFormParal(M, \'omega\', r\'\\omega\')
            sage: omega[1,2] = -1
            sage: poisson = omega.poisson(); poisson
            2-vector field poisson_omega on the Euclidean plane R2
            sage: poisson.display()
            poisson_omega = -e_q∧e_p
        '''
