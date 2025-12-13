from sage.manifolds.chart import Chart as Chart
from sage.manifolds.differentiable.diff_map import DiffMap as DiffMap
from sage.manifolds.differentiable.manifold import DifferentiableManifold as DifferentiableManifold
from sage.manifolds.differentiable.tensorfield import TensorField as TensorField
from sage.parallel.decorate import parallel as parallel
from sage.parallel.parallelism import Parallelism as Parallelism
from sage.symbolic.expression import Expression as Expression
from sage.symbolic.ring import SR as SR
from sage.tensor.modules.comp import Components as Components
from sage.tensor.modules.free_module_tensor import FreeModuleTensor as FreeModuleTensor

class TensorFieldParal(FreeModuleTensor, TensorField):
    """
    Tensor field along a differentiable manifold, with values on a
    parallelizable manifold.

    An instance of this class is a tensor field along a differentiable
    manifold `U` with values on a parallelizable manifold `M`, via a
    differentiable map `\\Phi: U \\rightarrow M`. More precisely, given two
    nonnegative integers `k` and `l` and a differentiable map

    .. MATH::

        \\Phi:\\ U \\longrightarrow M,

    a *tensor field of type* `(k,l)` *along* `U` *with values on* `M` is
    a differentiable map

    .. MATH::

        t:\\ U  \\longrightarrow T^{(k,l)}M

    (where `T^{(k,l)}M` is the tensor bundle of type `(k,l)` over `M`) such
    that

    .. MATH::

        t(p) \\in T^{(k,l)}(T_q M)

    for all `p \\in U`, i.e. `t(p)` is a tensor of type `(k,l)` on the
    tangent space `T_q M` at the point `q=\\Phi(p)`. That is to say
    a multilinear map

    .. MATH::

        t(p):\\ \\underbrace{T_q^*M\\times\\cdots\\times T_q^*M}_{k\\ \\; \\text{times}}
        \\times \\underbrace{T_q M\\times\\cdots\\times T_q M}_{l\\ \\; \\text{times}}
        \\longrightarrow K,

    where `T_q^* M` is the dual vector space to `T_q M` and `K` is the
    topological field over which the manifold `M` is defined.
    The integer `k+l` is called the *tensor rank*.

    The standard case of a tensor field *on* a differentiable manifold
    corresponds to `U=M` and `\\Phi = \\mathrm{Id}_M`. Other common cases
    are `\\Phi` being an immersion and `\\Phi` being a curve in `M`
    (`U` is then an open interval of `\\RR`).

    .. NOTE::

        If `M` is not parallelizable, the class
        :class:`~sage.manifolds.differentiable.tensorfield.TensorField`
        should be used instead.

    INPUT:

    - ``vector_field_module`` -- free module `\\mathfrak{X}(U,\\Phi)` of vector
      fields along `U` associated with the map `\\Phi: U \\rightarrow M` (cf.
      :class:`~sage.manifolds.differentiable.vectorfield_module.VectorFieldFreeModule`)
    - ``tensor_type`` -- pair `(k,l)` with `k` being the contravariant rank
      and `l` the covariant rank
    - ``name`` -- (default: ``None``) name given to the tensor field
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the tensor
      field; if none is provided, the LaTeX symbol is set to ``name``
    - ``sym`` -- (default: ``None``) a symmetry or a list of symmetries among
      the tensor arguments: each symmetry is described by a tuple containing
      the positions of the involved arguments, with the convention position=0
      for the first argument; for instance:

      * ``sym=(0,1)`` for a symmetry between the 1st and 2nd arguments
      * ``sym=[(0,2),(1,3,4)]`` for a symmetry between the 1st and 3rd
        arguments and a symmetry between the 2nd, 4th and 5th arguments

    - ``antisym`` -- (default: ``None``) antisymmetry or list of
      antisymmetries among the arguments, with the same convention
      as for ``sym``

    EXAMPLES:

    A tensor field of type `(2,0)` on a 3-dimensional parallelizable
    manifold::

        sage: M = Manifold(3, 'M')
        sage: c_xyz.<x,y,z> = M.chart()  # makes M parallelizable
        sage: t = M.tensor_field(2, 0, name='T') ; t
        Tensor field T of type (2,0) on the 3-dimensional differentiable
         manifold M

    Tensor fields are considered as elements of a module over the ring
    `C^k(M)` of scalar fields on `M`::

        sage: t.parent()
        Free module T^(2,0)(M) of type-(2,0) tensors fields on the
         3-dimensional differentiable manifold M
        sage: t.parent().base_ring()
        Algebra of differentiable scalar fields on the 3-dimensional
         differentiable manifold M

    The components with respect to the manifold's default frame are
    set or read by means of square brackets::

        sage: e = M.vector_frame('e') ; M.set_default_frame(e)
        sage: for i in M.irange():
        ....:     for j in M.irange():
        ....:         t[i,j] = (i+1)**(j+1)
        sage: [[ t[i,j] for j in M.irange()] for i in M.irange()]
        [[1, 1, 1], [2, 4, 8], [3, 9, 27]]

    A shortcut for the above is using ``[:]``::

        sage: t[:]
        [ 1  1  1]
        [ 2  4  8]
        [ 3  9 27]

    The components with respect to another frame are set via the method
    :meth:`set_comp` and read via the method :meth:`comp`; both return an
    instance of :class:`~sage.tensor.modules.comp.Components`::

        sage: f = M.vector_frame('f')  # a new frame defined on M, in addition to e
        sage: t.set_comp(f)[0,0] = -3
        sage: t.comp(f)
        2-indices components w.r.t. Vector frame (M, (f_0,f_1,f_2))
        sage: t.comp(f)[0,0]
        -3
        sage: t.comp(f)[:]  # the full list of components
        [-3  0  0]
        [ 0  0  0]
        [ 0  0  0]

    To avoid any inconsistency between the various components, the method
    :meth:`set_comp` deletes the components in other frames.
    Accordingly, the components in the frame ``e`` have been deleted::

        sage: t._components
        {Vector frame (M, (f_0,f_1,f_2)): 2-indices components w.r.t. Vector
         frame (M, (f_0,f_1,f_2))}

    To keep the other components, one must use the method :meth:`add_comp`::

        sage: t = M.tensor_field(2, 0, name='T')  # let us restart
        sage: t[0,0] = 2                   # sets the components in the frame e

    We now set the components in the frame f with add_comp::

        sage: t.add_comp(f)[0,0] = -3

    The components w.r.t. frame e have been kept::

        sage: t._components  # random (dictionary output)
        {Vector frame (M, (e_0,e_1,e_2)): 2-indices components w.r.t. Vector frame (M, (e_0,e_1,e_2)),
         Vector frame (M, (f_0,f_1,f_2)): 2-indices components w.r.t. Vector frame (M, (f_0,f_1,f_2))}

    The basic properties of a tensor field are::

        sage: t.domain()
        3-dimensional differentiable manifold M
        sage: t.tensor_type()
        (2, 0)

    Symmetries and antisymmetries are declared via the keywords ``sym`` and
    ``antisym``. For instance, a rank-6 covariant tensor that is symmetric
    with respect to its 1st and 3rd arguments and antisymmetric with respect
    to the 2nd, 5th and 6th arguments is set up as follows::

        sage: a = M.tensor_field(0, 6, name='T', sym=(0,2), antisym=(1,4,5))
        sage: a[0,0,1,0,1,2] = 3
        sage: a[1,0,0,0,1,2] # check of the symmetry
        3
        sage: a[0,1,1,0,0,2], a[0,1,1,0,2,0] # check of the antisymmetry
        (-3, 3)

    Multiple symmetries or antisymmetries are allowed; they must then be
    declared as a list. For instance, a rank-4 covariant tensor that is
    antisymmetric with respect to its 1st and 2nd arguments and with
    respect to its 3rd and 4th argument must be declared as::

        sage: r = M.tensor_field(0, 4, name='T', antisym=[(0,1), (2,3)])
        sage: r[0,1,2,0] = 3
        sage: r[1,0,2,0] # first antisymmetry
        -3
        sage: r[0,1,0,2] # second antisymmetry
        -3
        sage: r[1,0,0,2] # both antisymmetries acting
        3

    Tensor fields of the same type can be added and subtracted::

        sage: a = M.tensor_field(2, 0)
        sage: a[0,0], a[0,1], a[0,2] = (1,2,3)
        sage: b = M.tensor_field(2, 0)
        sage: b[0,0], b[1,1], b[2,2], b[0,2] = (4,5,6,7)
        sage: s = a + 2*b ; s
        Tensor field of type (2,0) on the 3-dimensional differentiable
         manifold M
        sage: a[:], (2*b)[:], s[:]
        (
        [1 2 3]  [ 8  0 14]  [ 9  2 17]
        [0 0 0]  [ 0 10  0]  [ 0 10  0]
        [0 0 0], [ 0  0 12], [ 0  0 12]
        )
        sage: s = a - b ; s
        Tensor field of type (2,0) on the 3-dimensional differentiable
         manifold M
        sage: a[:], b[:], s[:]
        (
        [1 2 3]  [4 0 7]  [-3  2 -4]
        [0 0 0]  [0 5 0]  [ 0 -5  0]
        [0 0 0], [0 0 6], [ 0  0 -6]
        )

    Symmetries are preserved by the addition whenever it is possible::

        sage: a = M.tensor_field(2, 0, sym=(0,1))
        sage: a[0,0], a[0,1], a[0,2] = (1,2,3)
        sage: s = a + b
        sage: a[:], b[:], s[:]
        (
        [1 2 3]  [4 0 7]  [ 5  2 10]
        [2 0 0]  [0 5 0]  [ 2  5  0]
        [3 0 0], [0 0 6], [ 3  0  6]
        )
        sage: a.symmetries()
        symmetry: (0, 1);  no antisymmetry
        sage: b.symmetries()
        no symmetry;  no antisymmetry
        sage: s.symmetries()
        no symmetry;  no antisymmetry

    Let us now make b symmetric::

        sage: b = M.tensor_field(2, 0, sym=(0,1))
        sage: b[0,0], b[1,1], b[2,2], b[0,2] = (4,5,6,7)
        sage: s = a + b
        sage: a[:], b[:], s[:]
        (
        [1 2 3]  [4 0 7]  [ 5  2 10]
        [2 0 0]  [0 5 0]  [ 2  5  0]
        [3 0 0], [7 0 6], [10  0  6]
        )
        sage: s.symmetries()  # s is symmetric because both a and b are
        symmetry: (0, 1);  no antisymmetry

    The tensor product is taken with the operator ``*``::

        sage: c = a*b ; c
        Tensor field of type (4,0) on the 3-dimensional differentiable
         manifold M
        sage: c.symmetries()  # since a and b are both symmetric, a*b has two symmetries:
        symmetries: [(0, 1), (2, 3)];  no antisymmetry

    The tensor product of two fully contravariant tensors is not
    symmetric in general::

        sage: a*b == b*a
        False

    The tensor product of a fully contravariant tensor by a fully
    covariant one is symmetric::

        sage: d = M.diff_form(2)  # a fully covariant tensor field
        sage: d[0,1], d[0,2], d[1,2] = (3, 2, 1)
        sage: s = a*d ; s
        Tensor field of type (2,2) on the 3-dimensional differentiable
         manifold M
        sage: s.symmetries()
        symmetry: (0, 1);  antisymmetry: (2, 3)
        sage: s1 = d*a ; s1
        Tensor field of type (2,2) on the 3-dimensional differentiable
         manifold M
        sage: s1.symmetries()
        symmetry: (0, 1);  antisymmetry: (2, 3)
        sage: d*a == a*d
        True

    Example of tensor field associated with a non-trivial differentiable
    map `\\Phi`: tensor field along a curve in `M`::

        sage: R = Manifold(1, 'R')  # R as a 1-dimensional manifold
        sage: T.<t> = R.chart()  # canonical chart on R
        sage: Phi = R.diff_map(M, [cos(t), sin(t), t], name='Phi') ; Phi
        Differentiable map Phi from the 1-dimensional differentiable manifold R
         to the 3-dimensional differentiable manifold M
        sage: h = R.tensor_field(2, 0, name='h', dest_map=Phi) ; h
        Tensor field h of type (2,0) along the 1-dimensional differentiable
         manifold R with values on the 3-dimensional differentiable manifold M
        sage: h.parent()
        Free module T^(2,0)(R,Phi) of type-(2,0) tensors fields along the
         1-dimensional differentiable manifold R mapped into the 3-dimensional
         differentiable manifold M
        sage: h[0,0], h[0,1], h[2,0] = 1+t, t^2, sin(t)
        sage: h.display()
        h = (t + 1) ∂/∂x⊗∂/∂x + t^2 ∂/∂x⊗∂/∂y + sin(t) ∂/∂z⊗∂/∂x
    """
    def __init__(self, vector_field_module, tensor_type, name=None, latex_name=None, sym=None, antisym=None) -> None:
        """
        Construct a tensor field.

        TESTS:

        Construction via ``parent.element_class``, and not via a direct call
        to ``TensorFieldParal``, to fit with the category framework::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: XM = M.vector_field_module()
            sage: T02 = M.tensor_field_module((0,2))
            sage: t = T02.element_class(XM, (0,2), name='t'); t
            Tensor field t of type (0,2) on the 2-dimensional differentiable
             manifold M
            sage: t[:] = [[1+x^2, x*y], [0, 1+y^2]]
            sage: t.display()
            t = (x^2 + 1) dx⊗dx + x*y dx⊗dy + (y^2 + 1) dy⊗dy
            sage: t.parent()
            Free module T^(0,2)(M) of type-(0,2) tensors fields on the
             2-dimensional differentiable manifold M
            sage: TestSuite(t).run()
        """
    def set_comp(self, basis=None):
        """
        Return the components of the tensor field in a given vector frame
        for assignment.

        The components with respect to other frames on the same domain are
        deleted, in order to avoid any inconsistency. To keep them, use the
        method :meth:`add_comp` instead.

        INPUT:

        - ``basis`` -- (default: ``None``) vector frame in which the
          components are defined; if none is provided, the components are
          assumed to refer to the tensor field domain's default frame

        OUTPUT:

        - components in the given frame, as an instance of the
          class :class:`~sage.tensor.modules.comp.Components`; if such
          components did not exist previously, they are created

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: e_xy = X.frame()
            sage: t = M.tensor_field(1,1, name='t')
            sage: t.set_comp(e_xy)
            2-indices components w.r.t. Coordinate frame (M, (∂/∂x,∂/∂y))
            sage: t.set_comp(e_xy)[1,0] = 2
            sage: t.display(e_xy)
            t = 2 ∂/∂y⊗dx

        Setting components in a new frame (``e``)::

            sage: e = M.vector_frame('e')
            sage: t.set_comp(e)
            2-indices components w.r.t. Vector frame (M, (e_0,e_1))
            sage: t.set_comp(e)[0,1] = x
            sage: t.display(e)
            t = x e_0⊗e^1

        The components with respect to the frame ``e_xy`` have be erased::

            sage: t.display(e_xy)
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components
             in the Coordinate frame (M, (∂/∂x,∂/∂y))

        Setting components in a frame defined on a subdomain deletes
        previously defined components as well::

            sage: U = M.open_subset('U', coord_def={X: x>0})
            sage: f = U.vector_frame('f')
            sage: t.set_comp(f)
            2-indices components w.r.t. Vector frame (U, (f_0,f_1))
            sage: t.set_comp(f)[0,1] = 1+y
            sage: t.display(f)
            t = (y + 1) f_0⊗f^1
            sage: t.display(e)
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components
             in the Vector frame (M, (e_0,e_1))
        """
    def add_comp(self, basis=None):
        """
        Return the components of the tensor field in a given vector frame
        for assignment.

        The components with respect to other frames on the same domain are
        kept. To delete them, use the method :meth:`set_comp` instead.

        INPUT:

        - ``basis`` -- (default: ``None``) vector frame in which the
          components are defined; if none is provided, the components are
          assumed to refer to the tensor field domain's default frame

        OUTPUT:

        - components in the given frame, as an instance of the
          class :class:`~sage.tensor.modules.comp.Components`; if such
          components did not exist previously, they are created

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: e_xy = X.frame()
            sage: t = M.tensor_field(1,1, name='t')
            sage: t.add_comp(e_xy)
            2-indices components w.r.t. Coordinate frame (M, (∂/∂x,∂/∂y))
            sage: t.add_comp(e_xy)[1,0] = 2
            sage: t.display(e_xy)
            t = 2 ∂/∂y⊗dx

        Adding components with respect to a new frame (``e``)::

            sage: e = M.vector_frame('e')
            sage: t.add_comp(e)
            2-indices components w.r.t. Vector frame (M, (e_0,e_1))
            sage: t.add_comp(e)[0,1] = x
            sage: t.display(e)
            t = x e_0⊗e^1

        The components with respect to the frame ``e_xy`` are kept::

            sage: t.display(e_xy)
            t = 2 ∂/∂y⊗dx

        Adding components in a frame defined on a subdomain::

            sage: U = M.open_subset('U', coord_def={X: x>0})
            sage: f = U.vector_frame('f')
            sage: t.add_comp(f)
            2-indices components w.r.t. Vector frame (U, (f_0,f_1))
            sage: t.add_comp(f)[0,1] = 1+y
            sage: t.display(f)
            t = (y + 1) f_0⊗f^1

        The components previously defined are kept::

            sage: t.display(e_xy)
            t = 2 ∂/∂y⊗dx
            sage: t.display(e)
            t = x e_0⊗e^1
        """
    def comp(self, basis=None, from_basis=None) -> Components:
        """
        Return the components in a given vector frame.

        If the components are not known already, they are computed by the
        tensor change-of-basis formula from components in another vector frame.

        INPUT:

        - ``basis`` -- (default: ``None``) vector frame in which the components
          are required; if none is provided, the components are assumed to
          refer to the tensor field domain's default frame
        - ``from_basis`` -- (default: ``None``) vector frame from which the
          required components are computed, via the tensor change-of-basis
          formula, if they are not known already in the basis ``basis``

        OUTPUT:

        - components in the vector frame ``basis``, as an instance of the
          class :class:`~sage.tensor.modules.comp.Components`

        EXAMPLES::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: t = M.tensor_field(1,2, name='t')
            sage: t[1,2,1] = x*y
            sage: t.comp(X.frame())
            3-indices components w.r.t. Coordinate frame (M, (∂/∂x,∂/∂y))
            sage: t.comp()  # the default frame is X.frame()
            3-indices components w.r.t. Coordinate frame (M, (∂/∂x,∂/∂y))
            sage: t.comp()[:]
            [[[0, 0], [x*y, 0]], [[0, 0], [0, 0]]]
            sage: e = M.vector_frame('e')
            sage: t[e, 2,1,1] = x-3
            sage: t.comp(e)
            3-indices components w.r.t. Vector frame (M, (e_1,e_2))
            sage: t.comp(e)[:]
            [[[0, 0], [0, 0]], [[x - 3, 0], [0, 0]]]
        """
    def lie_derivative(self, vector):
        """
        Compute the Lie derivative with respect to a vector field.

        INPUT:

        - ``vector`` -- vector field with respect to which the
          Lie derivative is to be taken

        OUTPUT:

        - the tensor field that is the Lie derivative of ``self``
          with respect to ``vector``

        EXAMPLES:

        Lie derivative of a vector::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: c_xy.<x,y> = M.chart()
            sage: v = M.vector_field(-y, x, name='v')
            sage: w = M.vector_field(2*x+y, x*y)
            sage: w.lie_derivative(v)
            Vector field on the 2-dimensional differentiable manifold M
            sage: w.lie_derivative(v).display()
            ((x - 2)*y + x) ∂/∂x + (x^2 - y^2 - 2*x - y) ∂/∂y

        The result is cached::

            sage: w.lie_derivative(v) is w.lie_derivative(v)
            True

        An alias is ``lie_der``::

            sage: w.lie_der(v) is w.lie_derivative(v)
            True

        The Lie derivative is antisymmetric::

            sage: w.lie_der(v) == -v.lie_der(w)
            True

        For vectors, it coincides with the commutator::

            sage: f = M.scalar_field(x^3 + x*y^2)
            sage: w.lie_der(v)(f).display()
            M → ℝ
            (x, y) ↦ -(x + 2)*y^3 + 3*x^3 - x*y^2 + 5*(x^3 - 2*x^2)*y
            sage: w.lie_der(v)(f) == v(w(f)) - w(v(f))  # rhs = commutator [v,w] acting on f
            True

        Lie derivative of a 1-form::

            sage: om = M.one_form(y^2*sin(x), x^3*cos(y))
            sage: om.lie_der(v)
            1-form on the 2-dimensional differentiable manifold M
            sage: om.lie_der(v).display()
            (-y^3*cos(x) + x^3*cos(y) + 2*x*y*sin(x)) dx
             + (-x^4*sin(y) - 3*x^2*y*cos(y) - y^2*sin(x)) dy

        Parallel computation::

            sage: Parallelism().set('tensor', nproc=2)
            sage: om.lie_der(v)
            1-form on the 2-dimensional differentiable manifold M
            sage: om.lie_der(v).display()
            (-y^3*cos(x) + x^3*cos(y) + 2*x*y*sin(x)) dx
             + (-x^4*sin(y) - 3*x^2*y*cos(y) - y^2*sin(x)) dy
            sage: Parallelism().set('tensor', nproc=1)  # switch off parallelization

        Check of Cartan identity::

            sage: om.lie_der(v) == (v.contract(0, om.exterior_derivative(), 0)
            ....:                   + om(v).exterior_derivative())
            True
        """
    lie_der = lie_derivative
    def restrict(self, subdomain: DifferentiableManifold, dest_map: DiffMap | None = None):
        """
        Return the restriction of ``self`` to some subdomain.

        If the restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` --
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
          open subset `U` of the tensor field domain `S`
        - ``dest_map`` --
          :class:`~sage.manifolds.differentiable.diff_map.DiffMap`
          (default: ``None``); destination map
          `\\Psi:\\ U \\rightarrow V`, where `V` is an open subset
          of the manifold `M` where the tensor field takes it values;
          if ``None``, the restriction of `\\Phi` to `U` is used, `\\Phi`
          being the differentiable map `S \\rightarrow M` associated
          with the tensor field

        OUTPUT: instance of :class:`TensorFieldParal` representing the restriction

        EXAMPLES:

        Restriction of a vector field defined on `\\RR^2` to a disk::

            sage: M = Manifold(2, 'R^2')
            sage: c_cart.<x,y> = M.chart() # Cartesian coordinates on R^2
            sage: v = M.vector_field(x+y, -1+x^2, name='v')
            sage: D = M.open_subset('D') # the unit open disc
            sage: c_cart_D = c_cart.restrict(D, x^2+y^2<1)
            sage: v_D = v.restrict(D) ; v_D
            Vector field v on the Open subset D of the 2-dimensional
             differentiable manifold R^2
            sage: v_D.display()
            v = (x + y) ∂/∂x + (x^2 - 1) ∂/∂y

        The symbolic expressions of the components with respect to
        Cartesian coordinates are equal::

            sage: bool( v_D[1].expr() == v[1].expr() )
            True

        but neither the chart functions representing the components (they are
        defined on different charts)::

            sage: v_D[1] == v[1]
            False

        nor the scalar fields representing the components (they are
        defined on different open subsets)::

            sage: v_D[[1]] == v[[1]]
            False

        The restriction of the vector field to its own domain is of
        course itself::

            sage: v.restrict(M) is v
            True
        """
    def __call__(self, *args):
        """
        The tensor field acting on 1-forms and vector fields as
        a multilinear map.

        In the particular case of tensor field of type `(1,1)`, the action
        can be on a single vector field, the tensor field being identified
        to a field of tangent-space endomorphisms. The output is then a
        vector field.

        INPUT:

        - ``*args`` -- list of `k` 1-forms and `l` vector fields, ``self``
          being a tensor of type `(k,l)`

        OUTPUT:

        - either the scalar field resulting from the action of ``self`` on
          the 1-forms and vector fields passed as arguments or the vector
          field resulting from the action of ``self`` as a field of
          tangent-space endomorphisms (case of a type-`(1,1)` tensor field)

        TESTS:

        Action of a tensor field of type-`(1,1)`::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: t = M.tensor_field(1,1, [[1+x, 2], [y, -x^2]], name='t')
            sage: v = M.vector_field(-y, x, name='v')
            sage: a = M.one_form(3, 1-y, name='a')
            sage: s = t.__call__(a,v); s
            Scalar field t(a,v) on the 2-dimensional differentiable manifold M
            sage: s.display()
            t(a,v): M → ℝ
               (x, y) ↦ -x^3 + y^3 + (x^3 - 3*x - 3)*y - y^2 + 6*x
            sage: s.coord_function() == sum(sum(t[i,j]*a[i]*v[j] for j in [0..1])
            ....:                           for i in [0..1])
            True
            sage: s == t(a,v)  # indirect doctest
            True

        The tensor field acting on vector field, as a field of tangent-space
        endomorphisms::

            sage: s = t.__call__(v); s
            Vector field t(v) on the 2-dimensional differentiable manifold M
            sage: s.display()
            t(v) = (-(x + 1)*y + 2*x) ∂/∂x + (-x^3 - y^2) ∂/∂y
            sage: s[0] == t[0,0]*v[0] + t[0,1]*v[1]
            True
            sage: s[1] == t[1,0]*v[0] + t[1,1]*v[1]
            True
            sage: s == t(v)  # indirect doctest
            True
        """
    def contract(self, *args: int | TensorField) -> TensorFieldParal:
        """
        Contraction with another tensor field, on one or more indices.

        INPUT:

        - ``pos1`` -- positions of the indices in ``self`` involved in the
          contraction; ``pos1`` must be a sequence of integers, with 0 standing
          for the first index position, 1 for the second one, etc. If ``pos1``
          is not provided, a single contraction on the last index position of
          ``self`` is assumed
        - ``other`` -- the tensor field to contract with
        - ``pos2`` -- positions of the indices in ``other`` involved in the
          contraction, with the same conventions as for ``pos1``. If ``pos2``
          is not provided, a single contraction on the first index position of
          ``other`` is assumed

        OUTPUT:

        - tensor field resulting from the contraction at the positions
          ``pos1`` and ``pos2`` of ``self`` with ``other``

        EXAMPLES:

        Contraction of a tensor field of type `(2,0)` with a tensor
        field of type `(1,1)`::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: a = M.tensor_field(2,0, [[1+x, 2], [y, -x^2]], name='a')
            sage: b = M.tensor_field(1,1, [[-y, 1], [x, x+y]], name='b')
            sage: s = a.contract(0, b, 1); s
            Tensor field of type (2,0) on the 2-dimensional differentiable manifold M
            sage: s.display()
            -x*y ∂/∂x⊗∂/∂x + (x^2 + x*y + y^2 + x) ∂/∂x⊗∂/∂y
             + (-x^2 - 2*y) ∂/∂y⊗∂/∂x + (-x^3 - x^2*y + 2*x) ∂/∂y⊗∂/∂y

        Check::

            sage: all(s[ind] == sum(a[k, ind[0]]*b[ind[1], k] for k in [0..1])
            ....:     for ind in M.index_generator(2))
            True

        The same contraction with repeated index notation::

            sage: s == a['^ki']*b['^j_k']
            True

        Contraction on the second index of ``a``::

            sage: s = a.contract(1, b, 1); s
            Tensor field of type (2,0) on the 2-dimensional differentiable manifold M
            sage: s.display()
            (-(x + 1)*y + 2) ∂/∂x⊗∂/∂x + (x^2 + 3*x + 2*y) ∂/∂x⊗∂/∂y
             + (-x^2 - y^2) ∂/∂y⊗∂/∂x + (-x^3 - (x^2 - x)*y) ∂/∂y⊗∂/∂y

        Check::

            sage: all(s[ind] == sum(a[ind[0], k]*b[ind[1], k] for k in [0..1])
            ....:     for ind in M.index_generator(2))
            True

        The same contraction with repeated index notation::

            sage: s == a['^ik']*b['^j_k']
            True

        .. SEEALSO::

            :meth:`sage.manifolds.differentiable.tensorfield.TensorField.contract`
            for more examples.
        """
    def __mul__(self, other):
        """
        Tensor product (or multiplication of the right by a scalar).

        INPUT:

        - ``other`` -- a tensor field, on the same manifold as ``self`` (or an
          object that can be coerced to a scalar field on the same manifold
          as ``self``)

        OUTPUT:

        - the tensor field resulting from the tensor product of ``self``
          with ``other`` (or from the product ``other * self`` if ``other``
          is a scalar)

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: a = M.tensor_field(0,2, [[1+x, 2], [y, -x^2]], name='a')

        Tensor product with another tensor field::

            sage: v = M.vector_field(-y, x, name='v')
            sage: s = a.__mul__(v); s
            Tensor field a⊗v of type (1,2) on the 2-dimensional differentiable
             manifold M
            sage: s.display()
            a⊗v = -(x + 1)*y ∂/∂x⊗dx⊗dx - 2*y ∂/∂x⊗dx⊗dy - y^2 ∂/∂x⊗dy⊗dx
             + x^2*y ∂/∂x⊗dy⊗dy + (x^2 + x) ∂/∂y⊗dx⊗dx + 2*x ∂/∂y⊗dx⊗dy
             + x*y ∂/∂y⊗dy⊗dx - x^3 ∂/∂y⊗dy⊗dy
            sage: all(s[ind] == v[ind[0]] * a[ind[1],ind[2]]
            ....:     for ind in M.index_generator(3))
            True

        Multiplication on the right by a scalar field::

            sage: f = M.scalar_field({X: x+y}, name='f')
            sage: s = a.__mul__(f); s
            Tensor field f*a of type (0,2) on the 2-dimensional differentiable
             manifold M
            sage: s.display()
            f*a = (x^2 + (x + 1)*y + x) dx⊗dx + (2*x + 2*y) dx⊗dy
             + (x*y + y^2) dy⊗dx + (-x^3 - x^2*y) dy⊗dy
            sage: s == f*a
            True
        """
    def display_comp(self, frame=None, chart=None, coordinate_labels: bool = True, only_nonzero: bool = True, only_nonredundant: bool = False):
        """
        Display the tensor components with respect to a given frame,
        one per line.

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        INPUT:

        - ``frame`` -- (default: ``None``) vector frame with respect to which
          the tensor field components are defined; if ``None``, then

          * if ``chart`` is not ``None``, the coordinate frame associated to
            ``chart`` is used
          * otherwise, the default basis of the vector field module on which
            the tensor field is defined is used

        - ``chart`` -- (default: ``None``) chart specifying the coordinate
          expression of the components; if ``None``, the default chart of the
          tensor field domain is used
        - ``coordinate_labels`` -- boolean (default: ``True``); if ``True``,
          coordinate symbols are used by default (instead of integers) as
          index labels whenever ``frame`` is a coordinate frame
        - ``only_nonzero`` -- boolean (default: ``True``); if ``True``, only
          nonzero components are displayed
        - ``only_nonredundant`` -- boolean (default: ``False``); if ``True``,
          only nonredundant components are displayed in case of symmetries

        EXAMPLES:

        Display of the components of a type-`(2,1)` tensor field on a
        2-dimensional manifold::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: t = M.tensor_field(2, 1, name='t', sym=(0,1))
            sage: t[0,0,0], t[0,1,0], t[1,1,1] = x+y, x*y, -3
            sage: t.display_comp()
            t^xx_x = x + y
            t^xy_x = x*y
            t^yx_x = x*y
            t^yy_y = -3

        By default, only the non-vanishing components are displayed;
        to see all the components, the argument ``only_nonzero`` must
        be set to ``False``::

            sage: t.display_comp(only_nonzero=False)
            t^xx_x = x + y
            t^xx_y = 0
            t^xy_x = x*y
            t^xy_y = 0
            t^yx_x = x*y
            t^yx_y = 0
            t^yy_x = 0
            t^yy_y = -3

        ``t`` being symmetric with respect to its first two indices, one
        may ask to skip the components that can be deduced by symmetry::

            sage: t.display_comp(only_nonredundant=True)
            t^xx_x = x + y
            t^xy_x = x*y
            t^yy_y = -3

        Instead of coordinate labels, one may ask for integers::

            sage: t.display_comp(coordinate_labels=False)
            t^00_0 = x + y
            t^01_0 = x*y
            t^10_0 = x*y
            t^11_1 = -3

        Display in a frame different from the default one (note that
        since ``f`` is not a coordinate frame, integer are used to
        label the indices)::

            sage: a = M.automorphism_field()
            sage: a[:] = [[1+y^2, 0], [0, 2+x^2]]
            sage: f = X.frame().new_frame(a, 'f')
            sage: t.display_comp(frame=f)
            t^00_0 = (x + y)/(y^2 + 1)
            t^01_0 = x*y/(x^2 + 2)
            t^10_0 = x*y/(x^2 + 2)
            t^11_1 = -3/(x^2 + 2)

        Display with respect to a chart different from the default one::

            sage: Y.<u,v> = M.chart()
            sage: X_to_Y = X.transition_map(Y, [x+y, x-y])
            sage: Y_to_X = X_to_Y.inverse()
            sage: t.display_comp(chart=Y)
            t^uu_u = 1/4*u^2 - 1/4*v^2 + 1/2*u - 3/2
            t^uu_v = 1/4*u^2 - 1/4*v^2 + 1/2*u + 3/2
            t^uv_u = 1/2*u + 3/2
            t^uv_v = 1/2*u - 3/2
            t^vu_u = 1/2*u + 3/2
            t^vu_v = 1/2*u - 3/2
            t^vv_u = -1/4*u^2 + 1/4*v^2 + 1/2*u - 3/2
            t^vv_v = -1/4*u^2 + 1/4*v^2 + 1/2*u + 3/2

        Note that the frame defining the components is the coordinate frame
        associated with chart ``Y``, i.e. we have::

            sage: str(t.display_comp(chart=Y)) == str(t.display_comp(frame=Y.frame(), chart=Y))
            True

        Display of the components with respect to a specific frame, expressed
        in terms of a specific chart::

            sage: t.display_comp(frame=f, chart=Y)
            t^00_0 = 4*u/(u^2 - 2*u*v + v^2 + 4)
            t^01_0 = (u^2 - v^2)/(u^2 + 2*u*v + v^2 + 8)
            t^10_0 = (u^2 - v^2)/(u^2 + 2*u*v + v^2 + 8)
            t^11_1 = -12/(u^2 + 2*u*v + v^2 + 8)
        """
    def at(self, point):
        """
        Value of ``self`` at a point of its domain.

        If the current tensor field is

        .. MATH::

            t:\\ U  \\longrightarrow T^{(k,l)} M

        associated with the differentiable map

        .. MATH::

            \\Phi:\\ U \\longrightarrow M,

        where `U` and `M` are two manifolds (possibly `U = M` and
        `\\Phi = \\mathrm{Id}_M`), then for any point `p\\in U`, `t(p)` is
        a tensor on the tangent space to `M` at the point `\\Phi(p)`.

        INPUT:

        - ``point`` -- :class:`~sage.manifolds.point.ManifoldPoint`
          point `p` in the domain of the tensor field `U`

        OUTPUT:

        - :class:`~sage.tensor.modules.free_module_tensor.FreeModuleTensor`
          representing the tensor `t(p)` on the tangent vector space
          `T_{\\Phi(p)} M`

        EXAMPLES:

        Vector in a tangent space of a 2-dimensional manifold::

            sage: M = Manifold(2, 'M')
            sage: c_xy.<x,y> = M.chart()
            sage: p = M.point((-2,3), name='p')
            sage: v = M.vector_field(y, x^2, name='v')
            sage: v.display()
            v = y ∂/∂x + x^2 ∂/∂y
            sage: vp = v.at(p) ; vp
            Tangent vector v at Point p on the 2-dimensional differentiable
             manifold M
            sage: vp.parent()
            Tangent space at Point p on the 2-dimensional differentiable
             manifold M
            sage: vp.display()
            v = 3 ∂/∂x + 4 ∂/∂y

        A 1-form gives birth to a linear form in the tangent space::

            sage: w = M.one_form(-x, 1+y, name='w')
            sage: w.display()
            w = -x dx + (y + 1) dy
            sage: wp = w.at(p) ; wp
            Linear form w on the Tangent space at Point p on the 2-dimensional
             differentiable manifold M
            sage: wp.parent()
            Dual of the Tangent space at Point p on the 2-dimensional
             differentiable manifold M
            sage: wp.display()
            w = 2 dx + 4 dy

        A tensor field of type `(1,1)` yields a tensor of type `(1,1)`
        in the tangent space::

            sage: t = M.tensor_field(1, 1, name='t')
            sage: t[0,0], t[0,1], t[1,1] = 1+x, x*y, 1-y
            sage: t.display()
            t = (x + 1) ∂/∂x⊗dx + x*y ∂/∂x⊗dy + (-y + 1) ∂/∂y⊗dy
            sage: tp = t.at(p) ; tp
            Type-(1,1) tensor t on the Tangent space at Point p on the
             2-dimensional differentiable manifold M
            sage: tp.parent()
            Free module of type-(1,1) tensors on the Tangent space at Point p
             on the 2-dimensional differentiable manifold M
            sage: tp.display()
            t = -∂/∂x⊗dx - 6 ∂/∂x⊗dy - 2 ∂/∂y⊗dy

        A 2-form yields an alternating form of degree 2 in the tangent space::

            sage: a = M.diff_form(2, name='a')
            sage: a[0,1] = x*y
            sage: a.display()
            a = x*y dx∧dy
            sage: ap = a.at(p) ; ap
            Alternating form a of degree 2 on the Tangent space at Point p on
             the 2-dimensional differentiable manifold M
            sage: ap.parent()
            2nd exterior power of the dual of the Tangent space at Point p on
             the 2-dimensional differentiable manifold M
            sage: ap.display()
            a = -6 dx∧dy

        Example with a non trivial map `\\Phi`::

            sage: U = Manifold(1, 'U')  # (0,2*pi) as a 1-dimensional manifold
            sage: T.<t> = U.chart(r't:(0,2*pi)')  # canonical chart on U
            sage: Phi = U.diff_map(M, [cos(t), sin(t)], name='Phi',
            ....:                  latex_name=r'\\Phi')
            sage: v = U.vector_field(1+t, t^2, name='v', dest_map=Phi) ; v
            Vector field v along the 1-dimensional differentiable manifold U
             with values on the 2-dimensional differentiable manifold M
            sage: v.display()
            v = (t + 1) ∂/∂x + t^2 ∂/∂y
            sage: p = U((pi/6,))
            sage: vp = v.at(p) ; vp
            Tangent vector v at Point on the 2-dimensional differentiable
             manifold M
            sage: vp.parent() is M.tangent_space(Phi(p))
            True
            sage: vp.display()
            v = (1/6*pi + 1) ∂/∂x + 1/36*pi^2 ∂/∂y
        """
    def along(self, mapping):
        """
        Return the tensor field deduced from ``self`` via a differentiable map,
        the codomain of which is included in the domain of ``self``.

        More precisely, if ``self`` is a tensor field `t` on `M` and if
        `\\Phi: U \\rightarrow M` is a differentiable map from some
        differentiable manifold `U` to `M`, the returned object is
        a tensor field `\\tilde t` along `U` with values on `M` such that

        .. MATH::

           \\forall p \\in U,\\  \\tilde t(p) = t(\\Phi(p)).

        INPUT:

        - ``mapping`` -- differentiable map `\\Phi: U \\rightarrow M`

        OUTPUT: tensor field `\\tilde t` along `U` defined above

        EXAMPLES:

        Let us consider the map `\\Phi` between the interval `U=(0,2\\pi)` and
        the Euclidean plane `M=\\RR^2` defining the lemniscate of Gerono::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: t = var('t', domain='real')
            sage: Phi = M.curve({X: [sin(t), sin(2*t)/2]}, (t, 0, 2*pi),
            ....:               name='Phi')
            sage: U = Phi.domain(); U
            Real interval (0, 2*pi)

        and a vector field on `M`::

            sage: v = M.vector_field(-y , x, name='v')

        We have then::

            sage: vU = v.along(Phi); vU
            Vector field v along the Real interval (0, 2*pi) with values on
             the 2-dimensional differentiable manifold M
            sage: vU.display()
            v = -cos(t)*sin(t) ∂/∂x + sin(t) ∂/∂y
            sage: vU.parent()
            Free module X((0, 2*pi),Phi) of vector fields along the Real
             interval (0, 2*pi) mapped into the 2-dimensional differentiable
             manifold M
            sage: vU.parent() is Phi.tangent_vector_field().parent()
            True

        We check that the defining relation `\\tilde t(p) = t(\\Phi(p))` holds::

            sage: p = U(t)  # a generic point of U
            sage: vU.at(p) == v.at(Phi(p))
            True

        Case of a tensor field of type ``(0,2)``::

            sage: a = M.tensor_field(0, 2)
            sage: a[0,0], a[0,1], a[1,1] = x+y, x*y, x^2-y^2
            sage: aU = a.along(Phi); aU
            Tensor field of type (0,2) along the Real interval (0, 2*pi) with
             values on the 2-dimensional differentiable manifold M
            sage: aU.display()
            (cos(t) + 1)*sin(t) dx⊗dx + cos(t)*sin(t)^2 dx⊗dy + sin(t)^4 dy⊗dy
            sage: aU.parent()
            Free module T^(0,2)((0, 2*pi),Phi) of type-(0,2) tensors fields
             along the Real interval (0, 2*pi) mapped into the 2-dimensional
             differentiable manifold M
            sage: aU.at(p) == a.at(Phi(p))
            True
        """
    def series_expansion(self, symbol: Expression, order: int) -> list[TensorFieldParal]:
        '''
        Expand the tensor field in power series with respect to a small
        parameter.

        If the small parameter is `\\epsilon` and `T` is ``self``, the
        power series expansion to order `n` is

        .. MATH::

            T = T_0 + \\epsilon T_1 + \\epsilon^2 T_2 + \\cdots + \\epsilon^n T_n
                + O(\\epsilon^{n+1}),

        where `T_0, T_1, \\ldots, T_n` are `n+1` tensor fields of the same
        tensor type as ``self`` and do not depend upon `\\epsilon`.

        INPUT:

        - ``symbol`` -- symbolic variable (the "small parameter" `\\epsilon`)
          with respect to which the components of ``self`` are expanded in
          power series
        - ``order`` -- integer; the order `n` of the expansion, defined as the
          degree of the polynomial representing the truncated power series in
          ``symbol``

        OUTPUT:

        - list of the tensor fields `T_i` (size ``order+1``)

        EXAMPLES::

            sage: M = Manifold(4, \'M\', structure=\'Lorentzian\')
            sage: C.<t,x,y,z> = M.chart()
            sage: e = var(\'e\')
            sage: g = M.metric()
            sage: h1 = M.tensor_field(0,2,sym=(0,1))
            sage: h2 = M.tensor_field(0,2,sym=(0,1))
            sage: g[0, 0], g[1, 1], g[2, 2], g[3, 3] = -1, 1, 1, 1
            sage: h1[0, 1], h1[1, 2], h1[2, 3] = 1, 1, 1
            sage: h2[0, 2], h2[1, 3] = 1, 1
            sage: g.set(g + e*h1 + e^2*h2)
            sage: g_ser = g.series_expansion(e, 2); g_ser
            [Field of symmetric bilinear forms on the 4-dimensional Lorentzian manifold M,
             Field of symmetric bilinear forms on the 4-dimensional Lorentzian manifold M,
             Field of symmetric bilinear forms on the 4-dimensional Lorentzian manifold M]
            sage: g_ser[0][:]
            [-1  0  0  0]
            [ 0  1  0  0]
            [ 0  0  1  0]
            [ 0  0  0  1]
            sage: g_ser[1][:]
            [0 1 0 0]
            [1 0 1 0]
            [0 1 0 1]
            [0 0 1 0]
            sage: g_ser[2][:]
            [0 0 1 0]
            [0 0 0 1]
            [1 0 0 0]
            [0 1 0 0]
            sage: all([g_ser[1] == h1, g_ser[2] == h2])
            True
        '''
    def truncate(self, symbol, order):
        '''
        Return the tensor field truncated at a given order in the power series
        expansion with respect to some small parameter.

        If the small parameter is `\\epsilon` and `T` is ``self``, the
        power series expansion to order `n` is

        .. MATH::

            T = T_0 + \\epsilon T_1 + \\epsilon^2 T_2 + \\cdots + \\epsilon^n T_n
                + O(\\epsilon^{n+1}),

        where `T_0, T_1, \\ldots, T_n` are `n+1` tensor fields of the same
        tensor type as ``self`` and do not depend upon `\\epsilon`.

        INPUT:

        - ``symbol`` -- symbolic variable (the "small parameter" `\\epsilon`)
          with respect to which the components of ``self`` are expanded in
          power series
        - ``order`` -- integer; the order `n` of the expansion, defined as the
          degree of the polynomial representing the truncated power series in
          ``symbol``

        OUTPUT:

        - the tensor field
          `T_0 + \\epsilon T_1 + \\epsilon^2 T_2 + \\cdots + \\epsilon^n T_n`

        EXAMPLES::

            sage: M = Manifold(4, \'M\', structure=\'Lorentzian\')
            sage: C.<t,x,y,z> = M.chart()
            sage: e = var(\'e\')
            sage: g = M.metric()
            sage: h1 = M.tensor_field(0,2,sym=(0,1))
            sage: h2 = M.tensor_field(0,2,sym=(0,1))
            sage: g[0, 0], g[1, 1], g[2, 2], g[3, 3] = -1, 1, 1, 1
            sage: h1[0, 1], h1[1, 2], h1[2, 3] = 1, 1, 1
            sage: h2[0, 2], h2[1, 3] = 1, 1
            sage: g.set(g + e*h1 + e^2*h2)
            sage: g[:]
            [ -1   e e^2   0]
            [  e   1   e e^2]
            [e^2   e   1   e]
            [  0 e^2   e   1]
            sage: g.truncate(e, 1)[:]
            [-1  e  0  0]
            [ e  1  e  0]
            [ 0  e  1  e]
            [ 0  0  e  1]
        '''
    def set_calc_order(self, symbol: Expression, order: int, truncate: bool = False):
        '''
        Trigger a power series expansion with respect to a small parameter in
        computations involving the tensor field.

        This property is propagated by usual operations. The internal
        representation must be ``SR`` for this to take effect.

        If the small parameter is `\\epsilon` and `T` is ``self``, the
        power series expansion to order `n` is

        .. MATH::

            T = T_0 + \\epsilon T_1 + \\epsilon^2 T_2 + \\cdots + \\epsilon^n T_n
                + O(\\epsilon^{n+1}),

        where `T_0, T_1, \\ldots, T_n` are `n+1` tensor fields of the same
        tensor type as ``self`` and do not depend upon `\\epsilon`.

        INPUT:

        - ``symbol`` -- symbolic variable (the "small parameter" `\\epsilon`)
          with respect to which the components of ``self`` are expanded in
          power series
        - ``order`` -- integer; the order `n` of the expansion, defined as the
          degree of the polynomial representing the truncated power series in
          ``symbol``
        - ``truncate`` -- boolean (default: ``False``); determines whether the
          components of ``self`` are replaced by their expansions to the
          given order

        EXAMPLES::

            sage: M = Manifold(4, \'M\', structure=\'Lorentzian\')
            sage: C.<t,x,y,z> = M.chart()
            sage: e = var(\'e\')
            sage: g = M.metric()
            sage: h1 = M.tensor_field(0, 2, sym=(0,1))
            sage: h2 = M.tensor_field(0, 2, sym=(0,1))
            sage: g[0, 0], g[1, 1], g[2, 2], g[3, 3] = -1, 1, 1, 1
            sage: h1[0, 1], h1[1, 2], h1[2, 3] = 1, 1, 1
            sage: h2[0, 2], h2[1, 3] = 1, 1
            sage: g.set(g + e*h1 + e^2*h2)
            sage: g.set_calc_order(e, 1)
            sage: g[:]
            [ -1   e e^2   0]
            [  e   1   e e^2]
            [e^2   e   1   e]
            [  0 e^2   e   1]
            sage: g.set_calc_order(e, 1, truncate=True)
            sage: g[:]
            [-1  e  0  0]
            [ e  1  e  0]
            [ 0  e  1  e]
            [ 0  0  e  1]
        '''
