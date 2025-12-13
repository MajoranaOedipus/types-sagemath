from sage.categories.modules import Modules as Modules
from sage.manifolds.differentiable.automorphismfield import AutomorphismField as AutomorphismField, AutomorphismFieldParal as AutomorphismFieldParal
from sage.manifolds.differentiable.diff_form import DiffForm as DiffForm, DiffFormParal as DiffFormParal
from sage.manifolds.differentiable.multivectorfield import MultivectorField as MultivectorField, MultivectorFieldParal as MultivectorFieldParal
from sage.manifolds.differentiable.tensorfield import TensorField as TensorField
from sage.manifolds.differentiable.tensorfield_paral import TensorFieldParal as TensorFieldParal
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.tensor.modules.reflexive_module import ReflexiveModule_tensor as ReflexiveModule_tensor
from sage.tensor.modules.tensor_free_module import TensorFreeModule as TensorFreeModule

class TensorFieldModule(UniqueRepresentation, ReflexiveModule_tensor):
    """
    Module of tensor fields of a given type `(k,l)` along a differentiable
    manifold `U` with values on a differentiable manifold `M`, via a
    differentiable map `U \\rightarrow M`.

    Given two nonnegative integers `k` and `l` and a differentiable map

    .. MATH::

        \\Phi:\\ U \\longrightarrow M,

    the *tensor field module* `T^{(k,l)}(U,\\Phi)` is the set of all tensor
    fields of the type

    .. MATH::

        t:\\ U  \\longrightarrow T^{(k,l)} M

    (where `T^{(k,l)} M` is the tensor bundle of type `(k,l)` over `M`) such
    that

    .. MATH::

        t(p) \\in T^{(k,l)}(T_{\\Phi(p)}M)

    for all `p \\in U`, i.e. `t(p)` is a tensor of type `(k,l)` on the
    tangent vector space `T_{\\Phi(p)} M`. The set `T^{(k,l)}(U,\\Phi)`
    is a module over `C^k(U)`, the ring (algebra) of differentiable
    scalar fields on `U` (see
    :class:`~sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra`).

    The standard case of tensor fields *on* a differentiable manifold
    corresponds to `U = M` and `\\Phi = \\mathrm{Id}_M`; we then denote
    `T^{(k,l)}(M,\\mathrm{Id}_M)` by merely `T^{(k,l)}(M)`. Other common
    cases are `\\Phi` being an immersion and `\\Phi` being a curve in `M`
    (`U` is then an open interval of `\\RR`).

    .. NOTE::

        If `M` is parallelizable, the class :class:`TensorFieldFreeModule`
        should be used instead.

    INPUT:

    - ``vector_field_module`` -- module `\\mathfrak{X}(U,\\Phi)` of vector
      fields along `U` associated with the map `\\Phi: U \\rightarrow M`
    - ``tensor_type`` -- pair `(k,l)` with `k` being the contravariant
      rank and `l` the covariant rank

    EXAMPLES:

    Module of type-`(2,0)` tensor fields on the 2-sphere::

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
        sage: W = U.intersection(V)
        sage: T20 = M.tensor_field_module((2,0)); T20
        Module T^(2,0)(M) of type-(2,0) tensors fields on the 2-dimensional
         differentiable manifold M

    `T^{(2,0)}(M)` is a module over the algebra `C^k(M)`::

        sage: T20.category()
        Category of tensor products of modules over Algebra of differentiable scalar fields
         on the 2-dimensional differentiable manifold M
        sage: T20.base_ring() is M.scalar_field_algebra()
        True

    `T^{(2,0)}(M)` is not a free module::

        sage: from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule_abstract
        sage: isinstance(T20, FiniteRankFreeModule_abstract)
        False

    because `M = S^2` is not parallelizable::

        sage: M.is_manifestly_parallelizable()
        False

    On the contrary, the module of type-`(2,0)` tensor fields on `U` is a
    free module, since `U` is parallelizable (being a coordinate domain)::

        sage: T20U = U.tensor_field_module((2,0))
        sage: isinstance(T20U, FiniteRankFreeModule_abstract)
        True
        sage: U.is_manifestly_parallelizable()
        True

    The zero element::

        sage: z = T20.zero() ; z
        Tensor field zero of type (2,0) on the 2-dimensional differentiable
         manifold M
        sage: z is T20(0)
        True
        sage: z[c_xy.frame(),:]
        [0 0]
        [0 0]
        sage: z[c_uv.frame(),:]
        [0 0]
        [0 0]

    The module `T^{(2,0)}(M)` coerces to any module of type-`(2,0)` tensor
    fields defined on some subdomain of `M`, for instance `T^{(2,0)}(U)`::

        sage: T20U.has_coerce_map_from(T20)
        True

    The reverse is not true::

        sage: T20.has_coerce_map_from(T20U)
        False

    The coercion::

        sage: T20U.coerce_map_from(T20)
        Coercion map:
          From: Module T^(2,0)(M) of type-(2,0) tensors fields on the 2-dimensional differentiable manifold M
          To:   Free module T^(2,0)(U) of type-(2,0) tensors fields on the Open subset U of the 2-dimensional differentiable manifold M

    The coercion map is actually the *restriction* of tensor fields defined
    on `M` to `U`::

        sage: t = M.tensor_field(2,0, name='t')
        sage: eU = c_xy.frame() ; eV = c_uv.frame()
        sage: t[eU,:] = [[2,0], [0,-3]]
        sage: t.add_comp_by_continuation(eV, W, chart=c_uv)
        sage: T20U(t)  # the conversion map in action
        Tensor field t of type (2,0) on the Open subset U of the 2-dimensional
         differentiable manifold M
        sage: T20U(t) is t.restrict(U)
        True

    There is also a coercion map from fields of tangent-space automorphisms to
    tensor fields of type-`(1,1)`::

        sage: T11 = M.tensor_field_module((1,1)) ; T11
        Module T^(1,1)(M) of type-(1,1) tensors fields on the 2-dimensional
         differentiable manifold M
        sage: GL = M.automorphism_field_group() ; GL
        General linear group of the Module X(M) of vector fields on the
         2-dimensional differentiable manifold M
        sage: T11.has_coerce_map_from(GL)
        True

    Explicit call to the coercion map::

        sage: a = GL.one() ; a
        Field of tangent-space identity maps on the 2-dimensional
         differentiable manifold M
        sage: a.parent()
        General linear group of the Module X(M) of vector fields on the
         2-dimensional differentiable manifold M
        sage: ta = T11.coerce(a) ; ta
        Tensor field Id of type (1,1) on the 2-dimensional differentiable
         manifold M
        sage: ta.parent()
        Module T^(1,1)(M) of type-(1,1) tensors fields on the 2-dimensional
         differentiable manifold M
        sage: ta[eU,:]  # ta on U
        [1 0]
        [0 1]
        sage: ta[eV,:]  # ta on V
        [1 0]
        [0 1]

    TESTS::

        sage: T11.tensor_factors()
        [Module X(M) of vector fields on the 2-dimensional differentiable manifold M,
        Module Omega^1(M) of 1-forms on the 2-dimensional differentiable manifold M]
    """
    Element = TensorField
    def __init__(self, vector_field_module, tensor_type, category=None) -> None:
        """
        Construct a module of tensor fields taking values on a (a priori) not
        parallelizable differentiable manifold.

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
            sage: XM = M.vector_field_module()
            sage: from sage.manifolds.differentiable.tensorfield_module import TensorFieldModule
            sage: T21 = TensorFieldModule(XM, (2,1)); T21
            Module T^(2,1)(M) of type-(2,1) tensors fields on the 2-dimensional
             differentiable manifold M
            sage: T21 is M.tensor_field_module((2,1))
            True
            sage: TestSuite(T21).run(skip='_test_elements')

        In the above test suite, ``_test_elements`` is skipped because of the
        ``_test_pickling`` error of the elements (to be fixed in
        :class:`~sage.manifolds.differentiable.tensorfield.TensorField`)
        """
    def base_module(self):
        """
        Return the vector field module on which ``self`` is constructed.

        OUTPUT:

        - a
          :class:`~sage.manifolds.differentiable.vectorfield_module.VectorFieldModule`
          representing the module on which ``self`` is defined

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: T13 = M.tensor_field_module((1,3))
            sage: T13.base_module()
            Module X(M) of vector fields on the 2-dimensional differentiable
             manifold M
            sage: T13.base_module() is M.vector_field_module()
            True
            sage: T13.base_module().base_ring()
            Algebra of differentiable scalar fields on the 2-dimensional
             differentiable manifold M
        """
    def tensor_type(self):
        """
        Return the tensor type of ``self``.

        OUTPUT: pair `(k,l)` of nonnegative integers such that the tensor
        fields belonging to this module are of type `(k,l)`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: T13 = M.tensor_field_module((1,3))
            sage: T13.tensor_type()
            (1, 3)
            sage: T20 = M.tensor_field_module((2,0))
            sage: T20.tensor_type()
            (2, 0)
        """
    @cached_method
    def zero(self):
        """
        Return the zero of ``self``.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: U = M.open_subset('U'); V = M.open_subset('V')
            sage: c_xy.<x,y> = U.chart(); c_uv.<u,v> = V.chart()
            sage: M.declare_union(U,V)
            sage: T20 = M.tensor_field_module((2,0))
            sage: T20.zero()
            Tensor field zero of type (2,0) on the
             2-dimensional differentiable manifold M
        """

class TensorFieldFreeModule(TensorFreeModule):
    """
    Free module of tensor fields of a given type `(k,l)` along a
    differentiable manifold `U` with values on a parallelizable manifold `M`,
    via a differentiable map `U \\rightarrow M`.

    Given two nonnegative integers `k` and `l` and a differentiable map

    .. MATH::

        \\Phi:\\ U \\longrightarrow M,

    the *tensor field module* `T^{(k,l)}(U, \\Phi)` is the set of all tensor
    fields of the type

    .. MATH::

        t:\\ U \\longrightarrow T^{(k,l)} M

    (where `T^{(k,l)}M` is the tensor bundle of type `(k,l)` over `M`)
    such that

    .. MATH::

        t(p) \\in T^{(k,l)}(T_{\\Phi(p)}M)

    for all `p \\in U`, i.e. `t(p)` is a tensor of type `(k,l)` on the
    tangent vector space `T_{\\Phi(p)}M`. Since `M` is parallelizable,
    the set `T^{(k,l)}(U,\\Phi)` is a free module over `C^k(U)`, the
    ring (algebra) of differentiable scalar fields on `U` (see
    :class:`~sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra`).

    The standard case of tensor fields *on* a differentiable manifold
    corresponds to `U = M` and `\\Phi = \\mathrm{Id}_M`; we then denote
    `T^{(k,l)}(M,\\mathrm{Id}_M)` by merely `T^{(k,l)}(M)`. Other common cases
    are `\\Phi` being an immersion and `\\Phi` being a curve in `M` (`U` is then
    an open interval of `\\RR`).

    .. NOTE::

        If `M` is not parallelizable, the class :class:`TensorFieldModule`
        should be used instead, for `T^{(k,l)}(U,\\Phi)` is no longer a
        free module.

    INPUT:

    - ``vector_field_module`` -- free module `\\mathfrak{X}(U,\\Phi)` of vector
      fields along `U` associated with the map `\\Phi: U \\rightarrow M`
    - ``tensor_type`` -- pair `(k,l)` with `k` being the contravariant rank
      and `l` the covariant rank

    EXAMPLES:

    Module of type-`(2,0)` tensor fields on `\\RR^3`::

        sage: M = Manifold(3, 'R^3')
        sage: c_xyz.<x,y,z> = M.chart()  # Cartesian coordinates
        sage: T20 = M.tensor_field_module((2,0)) ; T20
        Free module T^(2,0)(R^3) of type-(2,0) tensors fields on the
         3-dimensional differentiable manifold R^3

    `T^{(2,0)}(\\RR^3)` is a module over the algebra `C^k(\\RR^3)`::

        sage: T20.category()
        Category of tensor products of finite dimensional modules over
         Algebra of differentiable scalar fields on the 3-dimensional differentiable manifold R^3
        sage: T20.base_ring() is M.scalar_field_algebra()
        True

    `T^{(2,0)}(\\RR^3)` is a free module::

        sage: from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule_abstract
        sage: isinstance(T20, FiniteRankFreeModule_abstract)
        True

    because `M = \\RR^3` is parallelizable::

        sage: M.is_manifestly_parallelizable()
        True

    The zero element::

        sage: z = T20.zero() ; z
        Tensor field zero of type (2,0) on the 3-dimensional differentiable
         manifold R^3
        sage: z[:]
        [0 0 0]
        [0 0 0]
        [0 0 0]

    A random element::

        sage: t = T20.an_element() ; t
        Tensor field of type (2,0) on the 3-dimensional differentiable
         manifold R^3
        sage: t[:]
        [2 0 0]
        [0 0 0]
        [0 0 0]

    The module `T^{(2,0)}(\\RR^3)` coerces to any module of type-`(2,0)`
    tensor fields defined on some subdomain of `\\RR^3`::

        sage: U = M.open_subset('U', coord_def={c_xyz: x>0})
        sage: T20U = U.tensor_field_module((2,0))
        sage: T20U.has_coerce_map_from(T20)
        True
        sage: T20.has_coerce_map_from(T20U)  # the reverse is not true
        False
        sage: T20U.coerce_map_from(T20)
        Coercion map:
          From: Free module T^(2,0)(R^3) of type-(2,0) tensors fields on the 3-dimensional differentiable manifold R^3
          To:   Free module T^(2,0)(U) of type-(2,0) tensors fields on the Open subset U of the 3-dimensional differentiable manifold R^3

    The coercion map is actually the *restriction* of tensor fields defined
    on `\\RR^3` to `U`.

    There is also a coercion map from fields of tangent-space automorphisms to
    tensor fields of type `(1,1)`::

        sage: T11 = M.tensor_field_module((1,1)) ; T11
        Free module T^(1,1)(R^3) of type-(1,1) tensors fields on the
         3-dimensional differentiable manifold R^3
        sage: GL = M.automorphism_field_group() ; GL
        General linear group of the Free module X(R^3) of vector fields on the
         3-dimensional differentiable manifold R^3
        sage: T11.has_coerce_map_from(GL)
        True

    An explicit call to this coercion map is::

        sage: id = GL.one() ; id
        Field of tangent-space identity maps on the 3-dimensional
         differentiable manifold R^3
        sage: tid = T11(id) ; tid
        Tensor field Id of type (1,1) on the 3-dimensional differentiable
         manifold R^3
        sage: tid[:]
        [1 0 0]
        [0 1 0]
        [0 0 1]
    """
    Element = TensorFieldParal
    def __init__(self, vector_field_module, tensor_type) -> None:
        """
        Construct a module of tensor fields taking values on a
        parallelizable differentiable manifold.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()  # makes M parallelizable
            sage: XM = M.vector_field_module()
            sage: from sage.manifolds.differentiable.tensorfield_module import TensorFieldFreeModule
            sage: T12 = TensorFieldFreeModule(XM, (1,2)); T12
            Free module T^(1,2)(M) of type-(1,2) tensors fields on the
             2-dimensional differentiable manifold M
            sage: T12 is M.tensor_field_module((1,2))
            True
            sage: TestSuite(T12).run()
        """
