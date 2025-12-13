from sage.categories.modules import Modules as Modules
from sage.manifolds.differentiable.diff_form import DiffForm as DiffForm
from sage.manifolds.differentiable.diff_map import DiffMap as DiffMap
from sage.manifolds.differentiable.manifold import DifferentiableManifold as DifferentiableManifold
from sage.manifolds.differentiable.vectorfield import VectorField as VectorField, VectorFieldParal as VectorFieldParal
from sage.manifolds.scalarfield import ScalarField as ScalarField
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule as FiniteRankFreeModule
from sage.tensor.modules.reflexive_module import ReflexiveModule_base as ReflexiveModule_base
from typing import Literal, overload

class VectorFieldModule(UniqueRepresentation, ReflexiveModule_base):
    """
    Module of vector fields along a differentiable manifold `U`
    with values on a differentiable manifold `M`, via a differentiable
    map `U \\rightarrow M`.

    Given a differentiable map

    .. MATH::

        \\Phi:\\  U \\longrightarrow M,

    the *vector field module* `\\mathfrak{X}(U,\\Phi)` is the set of
    all vector fields of the type

    .. MATH::

        v:\\ U  \\longrightarrow TM

    (where `TM` is the tangent bundle of `M`) such that

    .. MATH::

        \\forall p \\in U,\\ v(p) \\in T_{\\Phi(p)}M,

    where `T_{\\Phi(p)}M` is the tangent space to `M` at the point `\\Phi(p)`.

    The set `\\mathfrak{X}(U,\\Phi)` is a module over `C^k(U)`, the ring
    (algebra) of differentiable scalar fields on `U` (see
    :class:`~sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra`).
    Furthermore, it is a Lie algebroid under the Lie bracket (cf.
    :wikipedia:`Lie_algebroid`)

    .. MATH::

        [X, Y] = X \\circ Y - Y \\circ X

    over the scalarfields if `\\Phi` is the identity map. That is to say
    the Lie bracket is antisymmetric, bilinear over the base field,
    satisfies the Jacobi identity, and `[X, fY] = X(f) Y + f[X, Y]`.

    The standard case of vector fields *on* a differentiable manifold
    corresponds to `U = M` and `\\Phi = \\mathrm{Id}_M`; we then denote
    `\\mathfrak{X}(M,\\mathrm{Id}_M)` by merely `\\mathfrak{X}(M)`. Other common
    cases are `\\Phi` being an immersion and `\\Phi` being a curve in `M`
    (`U` is then an open interval of `\\RR`).

    .. NOTE::

        If `M` is parallelizable, the class :class:`VectorFieldFreeModule`
        should be used instead.

    INPUT:

    - ``domain`` -- differentiable manifold `U` along which the
      vector fields are defined
    - ``dest_map`` -- (default: ``None``) destination map
      `\\Phi:\\ U \\rightarrow M`
      (type: :class:`~sage.manifolds.differentiable.diff_map.DiffMap`);
      if ``None``, it is assumed that `U = M` and `\\Phi` is the identity
      map of `M` (case of vector fields *on* `M`)

    EXAMPLES:

    Module of vector fields on the 2-sphere::

        sage: M = Manifold(2, 'M') # the 2-dimensional sphere S^2
        sage: U = M.open_subset('U') # complement of the North pole
        sage: c_xy.<x,y> = U.chart() # stereographic coordinates from the North pole
        sage: V = M.open_subset('V') # complement of the South pole
        sage: c_uv.<u,v> = V.chart() # stereographic coordinates from the South pole
        sage: M.declare_union(U,V)   # S^2 is the union of U and V
        sage: xy_to_uv = c_xy.transition_map(c_uv, (x/(x^2+y^2), y/(x^2+y^2)),
        ....:                 intersection_name='W', restrictions1= x^2+y^2!=0,
        ....:                 restrictions2= u^2+v^2!=0)
        sage: uv_to_xy = xy_to_uv.inverse()
        sage: XM = M.vector_field_module() ; XM
        Module X(M) of vector fields on the 2-dimensional differentiable
         manifold M

    `\\mathfrak{X}(M)` is a module over the algebra `C^k(M)`::

        sage: XM.category()
        Category of modules over Algebra of differentiable scalar fields on the
         2-dimensional differentiable manifold M
        sage: XM.base_ring() is M.scalar_field_algebra()
        True

    `\\mathfrak{X}(M)` is not a free module::

        sage: isinstance(XM, FiniteRankFreeModule)
        False

    because `M = S^2` is not parallelizable::

        sage: M.is_manifestly_parallelizable()
        False

    On the contrary, the module of vector fields on `U` is a free module,
    since `U` is parallelizable (being a coordinate domain)::

        sage: XU = U.vector_field_module()
        sage: isinstance(XU, FiniteRankFreeModule)
        True
        sage: U.is_manifestly_parallelizable()
        True

    The zero element of the module::

        sage: z = XM.zero() ; z
        Vector field zero on the 2-dimensional differentiable manifold M
        sage: z.display(c_xy.frame())
        zero = 0
        sage: z.display(c_uv.frame())
        zero = 0

    The module `\\mathfrak{X}(M)` coerces to any module of vector fields defined
    on a subdomain of `M`, for instance `\\mathfrak{X}(U)`::

        sage: XU.has_coerce_map_from(XM)
        True
        sage: XU.coerce_map_from(XM)
        Coercion map:
          From: Module X(M) of vector fields on the 2-dimensional
           differentiable manifold M
          To:   Free module X(U) of vector fields on the Open subset U of the
           2-dimensional differentiable manifold M

    The conversion map is actually the restriction of vector fields defined
    on `M` to `U`.
    """
    Element = VectorField
    def __init__(self, domain: DifferentiableManifold, dest_map: DiffMap | None = None) -> None:
        """
        Construct the module of vector fields taking values on a (a priori)
        non-parallelizable differentiable manifold.

        TESTS::

            sage: M = Manifold(2, 'M') # the 2-dimensional sphere S^2
            sage: U = M.open_subset('U') # complement of the North pole
            sage: c_xy.<x,y> = U.chart() # stereographic coordinates from the North pole
            sage: V = M.open_subset('V') # complement of the South pole
            sage: c_uv.<u,v> = V.chart() # stereographic coordinates from the South pole
            sage: M.declare_union(U,V)   # S^2 is the union of U and V
            sage: xy_to_uv = c_xy.transition_map(c_uv, (x/(x^2+y^2), y/(x^2+y^2)),
            ....:                intersection_name='W', restrictions1= x^2+y^2!=0,
            ....:                restrictions2= u^2+v^2!=0)
            sage: from sage.manifolds.differentiable.vectorfield_module import VectorFieldModule
            sage: XM = VectorFieldModule(M, dest_map=M.identity_map()); XM
            Module X(M) of vector fields on the 2-dimensional differentiable
             manifold M
            sage: XM is M.vector_field_module()
            True
            sage: TestSuite(XM).run(skip='_test_elements')

        In the above test suite, _test_elements is skipped because of the
        _test_pickling error of the elements (to be fixed in class
        TensorField)
        """
    def domain(self) -> DifferentiableManifold:
        """
        Return the domain of the vector fields in this module.

        If the module is `\\mathfrak{X}(U,\\Phi)`, returns the domain `U` of
        `\\Phi`.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
          representing the domain of the vector fields that belong to this
          module

        EXAMPLES::

            sage: M = Manifold(5, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.domain()
            5-dimensional differentiable manifold M
            sage: U = Manifold(2, 'U')
            sage: Phi = U.diff_map(M, name='Phi')
            sage: XU = U.vector_field_module(dest_map=Phi)
            sage: XU.domain()
            2-dimensional differentiable manifold U
        """
    def ambient_domain(self) -> DifferentiableManifold:
        """
        Return the manifold in which the vector fields of this module take
        their values.

        If the module is `\\mathfrak{X}(U,\\Phi)`, returns the codomain `M` of
        `\\Phi`.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
          representing the manifold in which the vector fields of this
          module take their values

        EXAMPLES::

            sage: M = Manifold(5, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.ambient_domain()
            5-dimensional differentiable manifold M
            sage: U = Manifold(2, 'U')
            sage: Phi = U.diff_map(M, name='Phi')
            sage: XU = U.vector_field_module(dest_map=Phi)
            sage: XU.ambient_domain()
            5-dimensional differentiable manifold M
        """
    def destination_map(self):
        """
        Return the differential map associated to this module.

        The differential map associated to this module is the map

        .. MATH::

            \\Phi:\\  U \\longrightarrow M

        such that this module is the set `\\mathfrak{X}(U,\\Phi)` of all
        vector fields of the type

        .. MATH::

            v:\\ U  \\longrightarrow TM

        (where `TM` is the tangent bundle of `M`) such that

        .. MATH::

            \\forall p \\in U,\\ v(p) \\in T_{\\Phi(p)}M,

        where `T_{\\Phi(p)}M` is the tangent space to `M` at the
        point `\\Phi(p)`.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.diff_map.DiffMap`
          representing the differential map `\\Phi`

        EXAMPLES::

            sage: M = Manifold(5, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.destination_map()
            Identity map Id_M of the 5-dimensional differentiable manifold M
            sage: U = Manifold(2, 'U')
            sage: Phi = U.diff_map(M, name='Phi')
            sage: XU = U.vector_field_module(dest_map=Phi)
            sage: XU.destination_map()
            Differentiable map Phi from the 2-dimensional differentiable
             manifold U to the 5-dimensional differentiable manifold M
        """
    def tensor_module(self, k, l, *, sym=None, antisym=None):
        """
        Return the module of type-`(k,l)` tensors on ``self``.

        INPUT:

        - ``k`` -- nonnegative integer; the contravariant rank,
          the tensor type being `(k,l)`
        - ``l`` -- nonnegative integer; the covariant rank,
          the tensor type being `(k,l)`

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.tensorfield_module.TensorFieldModule`
          representing the module `T^{(k,l)}(U,\\Phi)` of type-`(k,l)`
          tensors on the vector field module

        EXAMPLES:

        A tensor field module on a 2-dimensional differentiable manifold::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.tensor_module(1,2)
            Module T^(1,2)(M) of type-(1,2) tensors fields on the 2-dimensional
             differentiable manifold M

        The special case of tensor fields of type (1,0)::

            sage: XM.tensor_module(1,0)
            Module X(M) of vector fields on the 2-dimensional differentiable
             manifold M

        The result is cached::

            sage: XM.tensor_module(1,2) is XM.tensor_module(1,2)
            True
            sage: XM.tensor_module(1,0) is XM
            True

        See
        :class:`~sage.manifolds.differentiable.tensorfield_module.TensorFieldModule`
        for more examples and documentation.
        """
    def exterior_power(self, p):
        """
        Return the `p`-th exterior power of ``self``.

        If the vector field module ``self`` is `\\mathfrak{X}(U,\\Phi)`,
        its `p`-th exterior power is the set `A^p(U, \\Phi)` of
        `p`-vector fields along `U` with values on `\\Phi(U)`. It is a
        module over `C^k(U)`, the ring (algebra) of differentiable
        scalar fields on `U`.

        INPUT:

        - ``p`` -- nonnegative integer

        OUTPUT:

        - for `p=0`, the base ring, i.e. `C^k(U)`
        - for `p=1`, the vector field module ``self``, since
          `A^1(U, \\Phi) = \\mathfrak{X}(U,\\Phi)`
        - for `p \\geq 2`, instance of
          :class:`~sage.manifolds.differentiable.multivector_module.MultivectorModule`
          representing the module `A^p(U,\\Phi)`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.exterior_power(2)
            Module A^2(M) of 2-vector fields on the 2-dimensional
             differentiable manifold M
            sage: XM.exterior_power(1)
            Module X(M) of vector fields on the 2-dimensional
             differentiable manifold M
            sage: XM.exterior_power(1) is XM
            True
            sage: XM.exterior_power(0)
            Algebra of differentiable scalar fields on the 2-dimensional
             differentiable manifold M
            sage: XM.exterior_power(0) is M.scalar_field_algebra()
            True

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.multivector_module.MultivectorModule`
            for more examples and documentation.
        """
    def dual_exterior_power(self, p):
        """
        Return the `p`-th exterior power of the dual of the vector field
        module.

        If the vector field module is `\\mathfrak{X}(U,\\Phi)`, the
        `p`-th exterior power of its dual is the set `\\Omega^p(U, \\Phi)`
        of `p`-forms along `U` with values on `\\Phi(U)`. It is a module
        over `C^k(U)`, the ring (algebra) of differentiable scalar
        fields on `U`.

        INPUT:

        - ``p`` -- nonnegative integer

        OUTPUT:

        - for `p=0`, the base ring, i.e. `C^k(U)`
        - for `p \\geq 1`, instance of
          :class:`~sage.manifolds.differentiable.diff_form_module.DiffFormModule`
          representing the module `\\Omega^p(U,\\Phi)`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.dual_exterior_power(2)
            Module Omega^2(M) of 2-forms on the 2-dimensional differentiable
             manifold M
            sage: XM.dual_exterior_power(1)
            Module Omega^1(M) of 1-forms on the 2-dimensional differentiable
             manifold M
            sage: XM.dual_exterior_power(1) is XM.dual()
            True
            sage: XM.dual_exterior_power(0)
            Algebra of differentiable scalar fields on the 2-dimensional
             differentiable manifold M
            sage: XM.dual_exterior_power(0) is M.scalar_field_algebra()
            True

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.diff_form_module.DiffFormModule`
            for more examples and documentation.
        """
    def dual(self):
        """
        Return the dual module.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.dual()
            Module Omega^1(M) of 1-forms on the 2-dimensional differentiable
             manifold M
        """
    def general_linear_group(self):
        """
        Return the general linear group of ``self``.

        If the vector field module is `\\mathfrak{X}(U,\\Phi)`, the *general
        linear group* is the group `\\mathrm{GL}(\\mathfrak{X}(U,\\Phi))` of
        automorphisms of `\\mathfrak{X}(U, \\Phi)`. Note that an automorphism
        of `\\mathfrak{X}(U,\\Phi)` can also be viewed as a *field* along `U`
        of automorphisms of the tangent spaces of `M \\supset \\Phi(U)`.

        OUTPUT:

        - instance of class
          :class:`~sage.manifolds.differentiable.automorphismfield_group.AutomorphismFieldGroup`
          representing `\\mathrm{GL}(\\mathfrak{X}(U,\\Phi))`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.general_linear_group()
            General linear group of the Module X(M) of vector fields on the
             2-dimensional differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.automorphismfield_group.AutomorphismFieldGroup`
            for more examples and documentation.
        """
    def tensor(self, *args, **kwds):
        """
        Construct a tensor field on the domain of ``self`` or a tensor product
        of ``self`` with other modules.

        If ``args`` consist of other parents, just delegate to :meth:`tensor_product`.

        Otherwise, construct a tensor (i.e., a tensor field on the domain of
        the vector field module) from the following input.

        INPUT:

        - ``tensor_type`` -- pair (k,l) with k being the contravariant rank
          and l the covariant rank
        - ``name`` -- (string; default: ``None``) name given to the tensor
        - ``latex_name`` -- (string; default: ``None``) LaTeX symbol to denote
          the tensor; if none is provided, the LaTeX symbol is set to ``name``
        - ``sym`` -- (default: ``None``) a symmetry or a list of symmetries
          among the tensor arguments: each symmetry is described by a tuple
          containing the positions of the involved arguments, with the
          convention position=0 for the first argument; for instance:

          * ``sym=(0,1)`` for a symmetry between the 1st and 2nd arguments
          * ``sym=[(0,2),(1,3,4)]`` for a symmetry between the 1st and 3rd
            arguments and a symmetry between the 2nd, 4th and 5th arguments

        - ``antisym`` -- (default: ``None``) antisymmetry or list of
          antisymmetries among the arguments, with the same convention
          as for ``sym``
        - ``specific_type`` -- (default: ``None``) specific subclass of
          :class:`~sage.manifolds.differentiable.tensorfield.TensorField` for
          the output

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.tensorfield.TensorField`
          representing the tensor defined on the vector field module with the
          provided characteristics

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.tensor((1,2), name='t')
            Tensor field t of type (1,2) on the 2-dimensional differentiable
             manifold M
            sage: XM.tensor((1,0), name='a')
            Vector field a on the 2-dimensional differentiable manifold M
            sage: XM.tensor((0,2), name='a', antisym=(0,1))
            2-form a on the 2-dimensional differentiable manifold M

        Delegation to :meth:`tensor_product`::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.tensor(XM)
            Module T^(2,0)(M) of type-(2,0) tensors fields on the 2-dimensional differentiable manifold M
            sage: XM.tensor(XM, XM.dual(), XM)
            Module T^(3,1)(M) of type-(3,1) tensors fields on the 2-dimensional differentiable manifold M
            sage: XM.tensor(XM).tensor(XM.dual().tensor(XM.dual()))
            Traceback (most recent call last):
            ...
            AttributeError: 'TensorFieldModule_with_category' object has no attribute '_basis_sym'...

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.tensorfield.TensorField`
            for more examples and documentation.
        """
    def alternating_contravariant_tensor(self, degree, name=None, latex_name=None):
        """
        Construct an alternating contravariant tensor on the vector
        field module ``self``.

        An alternating contravariant tensor on ``self`` is actually a
        multivector field along the differentiable manifold `U` over
        which ``self`` is defined.

        INPUT:

        - ``degree`` -- degree of the alternating contravariant tensor
          (i.e. its tensor rank)
        - ``name`` -- (default: ``None``) string; name given to the
          alternating contravariant tensor
        - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
          denote the alternating contravariant tensor; if none is
          provided, the LaTeX symbol is set to ``name``

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.multivectorfield.MultivectorField`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.alternating_contravariant_tensor(2, name='a')
            2-vector field a on the 2-dimensional differentiable
             manifold M

        An alternating contravariant tensor of degree 1 is simply
        a vector field::

            sage: XM.alternating_contravariant_tensor(1, name='a')
            Vector field a on the 2-dimensional differentiable
             manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.multivectorfield.MultivectorField`
            for more examples and documentation.
        """
    @overload
    def alternating_form(self, degree: Literal[0], name=None, latex_name=None) -> ScalarField: ...
    def linear_form(self, name=None, latex_name=None):
        """
        Construct a linear form on the vector field module.

        A linear form on the vector field module is actually a field
        of linear forms (i.e. a 1-form) along the differentiable
        manifold `U` over which the vector field module is defined.

        INPUT:

        - ``name`` -- (string; optional) name given to the linear form
        - ``latex_name`` -- (string; optional) LaTeX symbol to denote
          the linear form; if none is provided, the LaTeX symbol is
          set to ``name``

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.diff_form.DiffForm`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.linear_form()
            1-form on the 2-dimensional differentiable manifold M
            sage: XM.linear_form(name='a')
            1-form a on the 2-dimensional differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.diff_form.DiffForm`
            for more examples and documentation.
        """
    def automorphism(self, name=None, latex_name=None):
        """
        Construct an automorphism of the vector field module.

        An automorphism of the vector field module is actually a field
        of tangent-space automorphisms along the differentiable manifold
        `U` over which the vector field module is defined.

        INPUT:

        - ``name`` -- (string; optional) name given to the automorphism
        - ``latex_name`` -- (string; optional) LaTeX symbol to denote
          the automorphism; if none is provided, the LaTeX symbol is
          set to ``name``

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.automorphismfield.AutomorphismField`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.automorphism()
            Field of tangent-space automorphisms on the 2-dimensional
             differentiable manifold M
            sage: XM.automorphism(name='a')
            Field of tangent-space automorphisms a on the 2-dimensional
             differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.automorphismfield.AutomorphismField`
            for more examples and documentation.
        """
    @cached_method
    def identity_map(self):
        """
        Construct the identity map on the vector field module.

        The identity map on the vector field module is actually a field
        of tangent-space identity maps along the differentiable manifold
        `U` over which the vector field module is defined.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.automorphismfield.AutomorphismField`

        EXAMPLES:

        Get the identity map on a vector field module::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: Id = XM.identity_map(); Id
            Field of tangent-space identity maps on the 2-dimensional
             differentiable manifold M

        If the identity should be renamed, one has to create a copy::

            sage: Id.set_name('1')
            Traceback (most recent call last):
            ...
            ValueError: the name of an immutable element cannot be changed
            sage: one = Id.copy('1'); one
            Field of tangent-space automorphisms 1 on the 2-dimensional
             differentiable manifold M
        """
    @cached_method
    def zero(self):
        """
        Return the zero of ``self``.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.zero()
            Vector field zero on the 2-dimensional differentiable
             manifold M
        """
    def metric(self, name: str, signature: int | None = None, latex_name: str | None = None):
        """
        Construct a metric (symmetric bilinear
        form) on the current vector field module.

        A metric of the vector field module is actually a
        field of tangent-space non-degenerate symmetric bilinear forms along
        the manifold `U` on which the vector field module is defined.

        INPUT:

        - ``name`` -- string; name given to the metric
        - ``signature`` -- integer (default: ``None``); signature `S` of the
          metric: `S = n_+ - n_-`, where `n_+` (resp. `n_-`) is the number of
          positive terms (resp. number of negative terms) in any diagonal
          writing of the metric components; if ``signature`` is not provided,
          `S` is set to the manifold's dimension (Riemannian signature)
        - ``latex_name`` -- (string; default: ``None``) LaTeX symbol to denote
          the metric; if ``None``, it is formed from ``name``

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`
          representing the defined pseudo-Riemannian metric.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: XM = M.vector_field_module()
            sage: XM.metric('g')
            Riemannian metric g on the 2-dimensional differentiable manifold M
            sage: XM.metric('g', signature=0)
            Lorentzian metric g on the 2-dimensional differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`
            for more documentation.
        """
    def symplectic_form(self, name: str | None = None, latex_name: str | None = None):
        """
        Construct a symplectic form on the current vector field module.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.symplectic_form.SymplecticForm`

        EXAMPLES:

        Symplectic form on the 2-sphere::

            sage: M = manifolds.Sphere(2, coordinates='stereographic')
            sage: XM = M.vector_field_module()
            sage: omega = XM.symplectic_form(name='omega', latex_name=r'\\omega')
            sage: omega
            Symplectic form omega on the 2-sphere S^2 of radius 1 smoothly
             embedded in the Euclidean space E^3
        """
    def poisson_tensor(self, name: str | None = None, latex_name: str | None = None):
        """
        Construct a Poisson tensor on the current vector field module.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.poisson_tensor.PoissonTensorField`

        EXAMPLES:

        Poisson tensor on the 2-sphere::

            sage: M = manifolds.Sphere(2, coordinates='stereographic')
            sage: XM = M.vector_field_module()
            sage: varpi = XM.poisson_tensor(name='varpi', latex_name=r'\\varpi')
            sage: varpi
            2-vector field varpi on the 2-sphere S^2 of radius 1 smoothly embedded in the Euclidean space E^3
        """

class VectorFieldFreeModule(FiniteRankFreeModule):
    """
    Free module of vector fields along a differentiable manifold `U` with
    values on a parallelizable manifold `M`, via a differentiable map
    `U \\rightarrow M`.

    Given a differentiable map

    .. MATH::

        \\Phi:\\ U \\longrightarrow M

    the *vector field module* `\\mathfrak{X}(U,\\Phi)` is the set of all vector
    fields of the type

    .. MATH::

        v:\\ U  \\longrightarrow TM

    (where `TM` is the tangent bundle of `M`) such that

    .. MATH::

        \\forall p \\in U,\\ v(p) \\in T_{\\Phi(p)} M,

    where `T_{\\Phi(p)} M` is the tangent space to `M` at the point `\\Phi(p)`.

    Since `M` is parallelizable, the set `\\mathfrak{X}(U,\\Phi)` is a
    free module over `C^k(U)`, the ring (algebra) of differentiable
    scalar fields on `U` (see
    :class:`~sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra`).
    In fact, it carries the structure of a finite-dimensional Lie algebroid
    (cf. :wikipedia:`Lie_algebroid`).

    The standard case of vector fields *on* a differentiable manifold
    corresponds to `U=M` and `\\Phi = \\mathrm{Id}_M`; we then denote
    `\\mathfrak{X}(M,\\mathrm{Id}_M)` by merely `\\mathfrak{X}(M)`. Other common
    cases are `\\Phi` being an immersion and `\\Phi` being a curve in `M` (`U` is
    then an open interval of `\\RR`).

    .. NOTE::

        If `M` is not parallelizable, the class :class:`VectorFieldModule`
        should be used instead, for `\\mathfrak{X}(U,\\Phi)` is no longer a
        free module.

    INPUT:

    - ``domain`` -- differentiable manifold `U` along which the vector fields
      are defined
    - ``dest_map`` -- (default: ``None``) destination map
      `\\Phi:\\ U \\rightarrow M`
      (type: :class:`~sage.manifolds.differentiable.diff_map.DiffMap`); if
      ``None``, it is assumed that `U=M` and `\\Phi` is the identity map of
      `M` (case of vector fields *on* `M`)

    EXAMPLES:

    Module of vector fields on `\\RR^2`::

        sage: M = Manifold(2, 'R^2')
        sage: cart.<x,y> = M.chart()  # Cartesian coordinates on R^2
        sage: XM = M.vector_field_module() ; XM
        Free module X(R^2) of vector fields on the 2-dimensional differentiable
         manifold R^2
        sage: XM.category()
        Category of finite dimensional modules
         over Algebra of differentiable scalar fields
         on the 2-dimensional differentiable manifold R^2
        sage: XM.base_ring() is M.scalar_field_algebra()
        True

    Since `\\RR^2` is obviously parallelizable, ``XM`` is a free module::

        sage: isinstance(XM, FiniteRankFreeModule)
        True

    Some elements::

        sage: XM.an_element().display()
        2 ∂/∂x + 2 ∂/∂y
        sage: XM.zero().display()
        zero = 0
        sage: v = XM([-y,x]) ; v
        Vector field on the 2-dimensional differentiable manifold R^2
        sage: v.display()
        -y ∂/∂x + x ∂/∂y

    An example of module of vector fields with a destination map `\\Phi`
    different from the identity map, namely a mapping
    `\\Phi: I \\rightarrow \\RR^2`, where `I` is an open interval of `\\RR`::

        sage: I = Manifold(1, 'I')
        sage: canon.<t> = I.chart('t:(0,2*pi)')
        sage: Phi = I.diff_map(M, coord_functions=[cos(t), sin(t)], name='Phi',
        ....:                      latex_name=r'\\Phi') ; Phi
        Differentiable map Phi from the 1-dimensional differentiable manifold
         I to the 2-dimensional differentiable manifold R^2
        sage: Phi.display()
        Phi: I → R^2
           t ↦ (x, y) = (cos(t), sin(t))
        sage: XIM = I.vector_field_module(dest_map=Phi) ; XIM
        Free module X(I,Phi) of vector fields along the 1-dimensional
         differentiable manifold I mapped into the 2-dimensional differentiable
         manifold R^2
        sage: XIM.category()
        Category of finite dimensional modules
         over Algebra of differentiable scalar fields
         on the 1-dimensional differentiable manifold I

    The rank of the free module `\\mathfrak{X}(I,\\Phi)` is the dimension
    of the manifold `\\RR^2`, namely two::

        sage: XIM.rank()
        2

    A basis of it is induced by the coordinate vector frame of `\\RR^2`::

        sage: XIM.bases()
        [Vector frame (I, (∂/∂x,∂/∂y)) with values on the 2-dimensional
         differentiable manifold R^2]

    Some elements of this module::

        sage: XIM.an_element().display()
        2 ∂/∂x + 2 ∂/∂y
        sage: v = XIM([t, t^2]) ; v
        Vector field along the 1-dimensional differentiable manifold I with
         values on the 2-dimensional differentiable manifold R^2
        sage: v.display()
        t ∂/∂x + t^2 ∂/∂y

    The test suite is passed::

        sage: TestSuite(XIM).run()

    Let us introduce an open subset of `J\\subset I` and the vector field module
    corresponding to the restriction of `\\Phi` to it::

        sage: J = I.open_subset('J', coord_def={canon: t<pi})
        sage: XJM = J.vector_field_module(dest_map=Phi.restrict(J)); XJM
        Free module X(J,Phi) of vector fields along the Open subset J of the
         1-dimensional differentiable manifold I mapped into the 2-dimensional
         differentiable manifold R^2

    We have then::

        sage: XJM.default_basis()
        Vector frame (J, (∂/∂x,∂/∂y)) with values on the 2-dimensional
         differentiable manifold R^2
        sage: XJM.default_basis() is XIM.default_basis().restrict(J)
        True
        sage: v.restrict(J)
        Vector field along the Open subset J of the 1-dimensional
         differentiable manifold I with values on the 2-dimensional
         differentiable manifold R^2
        sage: v.restrict(J).display()
        t ∂/∂x + t^2 ∂/∂y

    Let us now consider the module of vector fields on the circle `S^1`; we
    start by constructing the `S^1` manifold::

        sage: M = Manifold(1, 'S^1')
        sage: U = M.open_subset('U')  # the complement of one point
        sage: c_t.<t> =  U.chart('t:(0,2*pi)') # the standard angle coordinate
        sage: V = M.open_subset('V') # the complement of the point t=pi
        sage: M.declare_union(U,V)   # S^1 is the union of U and V
        sage: c_u.<u> = V.chart('u:(0,2*pi)') # the angle t-pi
        sage: t_to_u = c_t.transition_map(c_u, (t-pi,), intersection_name='W',
        ....:                     restrictions1 = t!=pi, restrictions2 = u!=pi)
        sage: u_to_t = t_to_u.inverse()
        sage: W = U.intersection(V)

    `S^1` cannot be covered by a single chart, so it cannot be covered by
    a coordinate frame. It is however parallelizable and we introduce a global
    vector frame as follows. We notice that on their common subdomain, `W`,
    the coordinate vectors `\\partial/\\partial t` and `\\partial/\\partial u`
    coincide, as we can check explicitly::

        sage: c_t.frame()[0].display(c_u.frame().restrict(W))
        ∂/∂t = ∂/∂u

    Therefore, we can extend `\\partial/\\partial t` to all `V` and hence to all
    `S^1`, to form a vector field on `S^1` whose components w.r.t. both
    `\\partial/\\partial t` and `\\partial/\\partial u` are 1::

        sage: e = M.vector_frame('e')
        sage: U.set_change_of_frame(e.restrict(U), c_t.frame(),
        ....:                       U.tangent_identity_field())
        sage: V.set_change_of_frame(e.restrict(V), c_u.frame(),
        ....:                       V.tangent_identity_field())
        sage: e[0].display(c_t.frame())
        e_0 = ∂/∂t
        sage: e[0].display(c_u.frame())
        e_0 = ∂/∂u

    Equipped with the frame `e`, the manifold `S^1` is manifestly
    parallelizable::

        sage: M.is_manifestly_parallelizable()
        True

    Consequently, the module of vector fields on `S^1` is a free module::

        sage: XM = M.vector_field_module() ; XM
        Free module X(S^1) of vector fields on the 1-dimensional differentiable
         manifold S^1
        sage: isinstance(XM, FiniteRankFreeModule)
        True
        sage: XM.category()
        Category of finite dimensional modules
         over Algebra of differentiable scalar fields
         on the 1-dimensional differentiable manifold S^1
        sage: XM.base_ring() is M.scalar_field_algebra()
        True

    The zero element::

        sage: z = XM.zero() ; z
        Vector field zero on the 1-dimensional differentiable manifold S^1
        sage: z.display()
        zero = 0
        sage: z.display(c_t.frame())
        zero = 0

    The module `\\mathfrak{X}(S^1)` coerces to any module of vector fields
    defined on a subdomain of `S^1`, for instance `\\mathfrak{X}(U)`::

        sage: XU = U.vector_field_module() ; XU
        Free module X(U) of vector fields on the Open subset U of the
         1-dimensional differentiable manifold S^1
        sage: XU.has_coerce_map_from(XM)
        True
        sage: XU.coerce_map_from(XM)
        Coercion map:
          From: Free module X(S^1) of vector fields on the 1-dimensional
           differentiable manifold S^1
          To:   Free module X(U) of vector fields on the Open subset U of the
           1-dimensional differentiable manifold S^1

    The conversion map is actually the restriction of vector fields defined
    on `S^1` to `U`.

    The Sage test suite for modules is passed::

        sage: TestSuite(XM).run()
    """
    Element = VectorFieldParal
    def __init__(self, domain, dest_map=None) -> None:
        """
        Construct the free module of vector fields with values on a
        parallelizable manifold.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: from sage.manifolds.differentiable.vectorfield_module \\\n            ....:                                  import VectorFieldFreeModule
            sage: XM = VectorFieldFreeModule(M, dest_map=M.identity_map()); XM
            Free module X(M) of vector fields on the 2-dimensional
             differentiable manifold M
            sage: XM is M.vector_field_module()
            True
            sage: TestSuite(XM).run()
        """
    def domain(self) -> DifferentiableManifold:
        """
        Return the domain of the vector fields in ``self``.

        If the module is `\\mathfrak{X}(U, \\Phi)`, returns the domain `U`
        of `\\Phi`.

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
          representing the domain of the vector fields that belong to this
          module

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: X.<x,y,z> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.domain()
            3-dimensional differentiable manifold M
            sage: U = Manifold(2, 'U')
            sage: Y.<u,v> = U.chart()
            sage: Phi = U.diff_map(M, {(Y,X): [u+v, u-v, u*v]}, name='Phi')
            sage: XU = U.vector_field_module(dest_map=Phi)
            sage: XU.domain()
            2-dimensional differentiable manifold U
        """
    def ambient_domain(self) -> DifferentiableManifold:
        """
        Return the manifold in which the vector fields of ``self``
        take their values.

        If the module is `\\mathfrak{X}(U, \\Phi)`, returns the codomain `M`
        of `\\Phi`.

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
          representing the manifold in which the vector fields of ``self``
          take their values

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: X.<x,y,z> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.ambient_domain()
            3-dimensional differentiable manifold M
            sage: U = Manifold(2, 'U')
            sage: Y.<u,v> = U.chart()
            sage: Phi = U.diff_map(M, {(Y,X): [u+v, u-v, u*v]}, name='Phi')
            sage: XU = U.vector_field_module(dest_map=Phi)
            sage: XU.ambient_domain()
            3-dimensional differentiable manifold M
        """
    def destination_map(self) -> DiffMap:
        """
        Return the differential map associated to ``self``.

        The differential map associated to this module is the map

        .. MATH::

            \\Phi:\\  U \\longrightarrow M

        such that this module is the set `\\mathfrak{X}(U,\\Phi)` of all vector
        fields of the type

        .. MATH::

            v:\\ U  \\longrightarrow TM

        (where `TM` is the tangent bundle of `M`) such that

        .. MATH::

            \\forall p \\in U,\\ v(p) \\in T_{\\Phi(p)} M,

        where `T_{\\Phi(p)} M` is the tangent space to `M` at the
        point `\\Phi(p)`.

        OUTPUT:

        - a :class:`~sage.manifolds.differentiable.diff_map.DiffMap`
          representing the differential map `\\Phi`

        EXAMPLES::

            sage: M = Manifold(3, 'M')
            sage: X.<x,y,z> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.destination_map()
            Identity map Id_M of the 3-dimensional differentiable manifold M
            sage: U = Manifold(2, 'U')
            sage: Y.<u,v> = U.chart()
            sage: Phi = U.diff_map(M, {(Y,X): [u+v, u-v, u*v]}, name='Phi')
            sage: XU = U.vector_field_module(dest_map=Phi)
            sage: XU.destination_map()
            Differentiable map Phi from the 2-dimensional differentiable
             manifold U to the 3-dimensional differentiable manifold M
        """
    def tensor_module(self, k, l, *, sym=None, antisym=None):
        """
        Return the free module of all tensors of type `(k, l)` defined
        on ``self``.

        INPUT:

        - ``k`` -- nonnegative integer; the contravariant rank,
          the tensor type being `(k, l)`
        - ``l`` -- nonnegative integer; the covariant rank,
          the tensor type being `(k, l)`

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.tensorfield_module.TensorFieldFreeModule`
          representing the free module of type-`(k,l)` tensors on the
          vector field module

        EXAMPLES:

        A tensor field module on a 2-dimensional differentiable manifold::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.tensor_module(1,2)
            Free module T^(1,2)(M) of type-(1,2) tensors fields on the
             2-dimensional differentiable manifold M

        The special case of tensor fields of type (1,0)::

            sage: XM.tensor_module(1,0)
            Free module X(M) of vector fields on the 2-dimensional
             differentiable manifold M

        The result is cached::

            sage: XM.tensor_module(1,2) is XM.tensor_module(1,2)
            True
            sage: XM.tensor_module(1,0) is XM
            True

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.tensorfield_module.TensorFieldFreeModule`
            for more examples and documentation.
        """
    def exterior_power(self, p):
        """
        Return the `p`-th exterior power of ``self``.

        If the vector field module ``self`` is `\\mathfrak{X}(U,\\Phi)`,
        its `p`-th exterior power is the set `A^p(U, \\Phi)` of
        `p`-vector fields along `U` with values on `\\Phi(U)`. It is a
        free module over `C^k(U)`, the ring (algebra) of differentiable
        scalar fields on `U`.

        INPUT:

        - ``p`` -- nonnegative integer

        OUTPUT:

        - for `p=0`, the base ring, i.e. `C^k(U)`
        - for `p=1`, the vector field free module ``self``, since
          `A^1(U, \\Phi) = \\mathfrak{X}(U,\\Phi)`
        - for `p \\geq 2`, instance of
          :class:`~sage.manifolds.differentiable.multivector_module.MultivectorFreeModule`
          representing the module `A^p(U,\\Phi)`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.exterior_power(2)
            Free module A^2(M) of 2-vector fields on the 2-dimensional
             differentiable manifold M
            sage: XM.exterior_power(1)
            Free module X(M) of vector fields on the 2-dimensional
             differentiable manifold M
            sage: XM.exterior_power(1) is XM
            True
            sage: XM.exterior_power(0)
            Algebra of differentiable scalar fields on the 2-dimensional
             differentiable manifold M
            sage: XM.exterior_power(0) is M.scalar_field_algebra()
            True

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.multivector_module.MultivectorFreeModule`
            for more examples and documentation.
        """
    def dual_exterior_power(self, p):
        """
        Return the `p`-th exterior power of the dual of ``self``.

        If the vector field module ``self`` is `\\mathfrak{X}(U,\\Phi)`,
        the `p`-th exterior power of its dual is the set
        `\\Omega^p(U, \\Phi)` of `p`-forms along `U` with values on
        `\\Phi(U)`. It is a free module over `C^k(U)`, the ring (algebra)
        of differentiable scalar fields on `U`.

        INPUT:

        - ``p`` -- nonnegative integer

        OUTPUT:

        - for `p=0`, the base ring, i.e. `C^k(U)`
        - for `p \\geq 1`, a
          :class:`~sage.manifolds.differentiable.diff_form_module.DiffFormFreeModule`
          representing the module `\\Omega^p(U,\\Phi)`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.dual_exterior_power(2)
            Free module Omega^2(M) of 2-forms on the 2-dimensional
             differentiable manifold M
            sage: XM.dual_exterior_power(1)
            Free module Omega^1(M) of 1-forms on the 2-dimensional differentiable manifold M
            sage: XM.dual_exterior_power(1) is XM.dual()
            True
            sage: XM.dual_exterior_power(0)
            Algebra of differentiable scalar fields on the 2-dimensional
             differentiable manifold M
            sage: XM.dual_exterior_power(0) is M.scalar_field_algebra()
            True

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.diff_form_module.DiffFormFreeModule`
            for more examples and documentation.
        """
    def general_linear_group(self):
        """
        Return the general linear group of ``self``.

        If the vector field module is `\\mathfrak{X}(U,\\Phi)`, the *general
        linear group* is the group `\\mathrm{GL}(\\mathfrak{X}(U,\\Phi))` of
        automorphisms of `\\mathfrak{X}(U,\\Phi)`. Note that an automorphism of
        `\\mathfrak{X}(U,\\Phi)` can also be viewed as a *field* along `U` of
        automorphisms of the tangent spaces of `V=\\Phi(U)`.

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.automorphismfield_group.AutomorphismFieldParalGroup`
          representing `\\mathrm{GL}(\\mathfrak{X}(U,\\Phi))`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.general_linear_group()
            General linear group of the Free module X(M) of vector fields on
             the 2-dimensional differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.automorphismfield_group.AutomorphismFieldParalGroup`
            for more examples and documentation.
        """
    def basis(self, symbol=None, latex_symbol=None, from_frame=None, indices=None, latex_indices=None, symbol_dual=None, latex_symbol_dual=None):
        """
        Define a basis of ``self``.

        A basis of the vector field module is actually a vector frame along
        the differentiable manifold `U` over which the vector field module
        is defined.

        If the basis specified by the given symbol already exists, it is
        simply returned.
        If no argument is provided the module's default basis is returned.

        INPUT:

        - ``symbol`` -- (default: ``None``) either a string, to be used as a
          common base for the symbols of the elements of the basis, or a
          tuple of strings, representing the individual symbols of the
          elements of the basis
        - ``latex_symbol`` -- (default: ``None``) either a string, to be used
          as a common base for the LaTeX symbols of the elements of the basis,
          or a tuple of strings, representing the individual LaTeX symbols
          of the elements of the basis; if ``None``, ``symbol`` is used in
          place of ``latex_symbol``
        - ``from_frame`` -- (default: ``None``) vector frame `\\tilde{e}`
          on the codomain `M` of the destination map `\\Phi` of ``self``;
          the returned basis `e` is then such that for all `p \\in U`,
          we have `e(p) = \\tilde{e}(\\Phi(p))`
        - ``indices`` -- (default: ``None``; used only if ``symbol`` is a
          single string) tuple of strings representing the indices
          labelling the elements of the basis; if ``None``, the indices will be
          generated as integers within the range declared on ``self``
        - ``latex_indices`` -- (default: ``None``) tuple of strings
          representing the indices for the LaTeX symbols of the elements of
          the basis; if ``None``, ``indices`` is used instead
        - ``symbol_dual`` -- (default: ``None``) same as ``symbol`` but for the
          dual basis; if ``None``, ``symbol`` must be a string and is used
          for the common base of the symbols of the elements of the dual basis
        - ``latex_symbol_dual`` -- (default: ``None``) same as ``latex_symbol``
          but for the dual basis

        OUTPUT:

        - a :class:`~sage.manifolds.differentiable.vectorframe.VectorFrame`
          representing a basis on ``self``

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: e = XM.basis('e'); e
            Vector frame (M, (e_0,e_1))

        See :class:`~sage.manifolds.differentiable.vectorframe.VectorFrame`
        for more examples and documentation.
        """
    def tensor_from_comp(self, tensor_type, comp, name=None, latex_name=None):
        """
        Construct a tensor on ``self`` from a set of components.

        The tensor is actually a tensor field along the differentiable
        manifold `U` over which the vector field module is defined.
        The tensor symmetries are deduced from those of the components.

        INPUT:

        - ``tensor_type`` -- pair `(k,l)` with `k` being the contravariant
          rank and `l` the covariant rank
        - ``comp`` -- :class:`~sage.tensor.modules.comp.Components`;
          the tensor components in a given basis
        - ``name`` -- string (default: ``None``); name given to the tensor
        - ``latex_name`` -- string (default: ``None``); LaTeX symbol to denote
          the tensor; if ``None``, the LaTeX symbol is set to ``name``

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.tensorfield_paral.TensorFieldParal`
          representing the tensor defined on the vector field module with the
          provided characteristics

        EXAMPLES:

        A 2-dimensional set of components transformed into a type-`(1,1)`
        tensor field::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: XM = M.vector_field_module()
            sage: from sage.tensor.modules.comp import Components
            sage: comp = Components(M.scalar_field_algebra(), X.frame(), 2,
            ....:                   output_formatter=XM._output_formatter)
            sage: comp[:] = [[1+x, -y], [x*y, 2-y^2]]
            sage: t = XM.tensor_from_comp((1,1), comp, name='t'); t
            Tensor field t of type (1,1) on the 2-dimensional differentiable
             manifold M
            sage: t.display()
            t = (x + 1) ∂/∂x⊗dx - y ∂/∂x⊗dy + x*y ∂/∂y⊗dx + (-y^2 + 2) ∂/∂y⊗dy

        The same set of components transformed into a type-`(0,2)`
        tensor field::

            sage: t = XM.tensor_from_comp((0,2), comp, name='t'); t
            Tensor field t of type (0,2) on the 2-dimensional differentiable
             manifold M
            sage: t.display()
            t = (x + 1) dx⊗dx - y dx⊗dy + x*y dy⊗dx + (-y^2 + 2) dy⊗dy
        """
    def sym_bilinear_form(self, name=None, latex_name=None):
        """
        Construct a symmetric bilinear form on ``self``.

        A symmetric bilinear form on the vector field module is
        actually a field of tangent-space symmetric bilinear forms
        along the differentiable manifold `U` over which the vector
        field module is defined.

        INPUT:

        - ``name`` -- string (default: ``None``); name given to the
          symmetric bilinear form
        - ``latex_name`` -- string (default: ``None``); LaTeX symbol to
          denote the symmetric bilinear form; if ``None``, the LaTeX
          symbol is set to ``name``

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.tensorfield_paral.TensorFieldParal`
          of tensor type `(0,2)` and symmetric

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.sym_bilinear_form(name='a')
            Field of symmetric bilinear forms a on the 2-dimensional
             differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.tensorfield_paral.TensorFieldParal`
            for more examples and documentation.
        """
    def metric(self, name, signature=None, latex_name=None):
        """
        Construct a pseudo-Riemannian metric (nondegenerate symmetric bilinear
        form) on the current vector field module.

        A pseudo-Riemannian metric of the vector field module is actually a
        field of tangent-space non-degenerate symmetric bilinear forms along
        the manifold `U` on which the vector field module is defined.

        INPUT:

        - ``name`` -- string; name given to the metric
        - ``signature`` -- integer (default: ``None``); signature `S` of the
          metric: `S = n_+ - n_-`, where `n_+` (resp. `n_-`) is the number of
          positive terms (resp. number of negative terms) in any diagonal
          writing of the metric components; if ``signature`` is not provided,
          `S` is set to the manifold's dimension (Riemannian signature)
        - ``latex_name`` -- (string; default: ``None``) LaTeX symbol to denote
          the metric; if ``None``, it is formed from ``name``

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetricParal`
          representing the defined pseudo-Riemannian metric.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: XM.metric('g')
            Riemannian metric g on the 2-dimensional differentiable manifold M
            sage: XM.metric('g', signature=0)
            Lorentzian metric g on the 2-dimensional differentiable manifold M

        .. SEEALSO::

            :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetricParal`
            for more documentation.
        """
    def symplectic_form(self, name: str | None = None, latex_name: str | None = None):
        """
        Construct a symplectic form on the current vector field module.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.symplectic_form.SymplecticFormParal`

        EXAMPLES:

        Standard symplectic form on `\\RR^2`::

            sage: M.<q, p> = EuclideanSpace(2)
            sage: omega = M.vector_field_module().symplectic_form('omega', r'\\omega')
            sage: omega.set_comp()[1,2] = -1
            sage: omega.display()
            omega = -dq∧dp
        """
    def poisson_tensor(self, name: str | None = None, latex_name: str | None = None):
        """
        Construct a Poisson tensor on the current vector field module.

        OUTPUT:

        - instance of
          :class:`~sage.manifolds.differentiable.poisson_tensor.PoissonTensorFieldParal`

        EXAMPLES:

        Standard Poisson tensor on `\\RR^2`::

            sage: M.<q, p> = EuclideanSpace(2)
            sage: poisson = M.vector_field_module().poisson_tensor('varpi')
            sage: poisson.set_comp()[1,2] = -1
            sage: poisson.display()
            varpi = -e_q∧e_p
        """
