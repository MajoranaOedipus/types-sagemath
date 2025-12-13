from sage.manifolds.differentiable.affine_connection import AffineConnection as AffineConnection
from sage.manifolds.differentiable.vectorframe import CoordFrame as CoordFrame
from sage.parallel.decorate import parallel as parallel
from sage.parallel.parallelism import Parallelism as Parallelism

class LeviCivitaConnection(AffineConnection):
    '''
    Levi-Civita connection on a pseudo-Riemannian manifold.

    Let `M` be a differentiable manifold of class `C^\\infty` (smooth manifold)
    over `\\RR` endowed with a pseudo-Riemannian metric `g`.
    Let `C^\\infty(M)` be the algebra of smooth functions
    `M\\rightarrow \\RR` (cf.
    :class:`~sage.manifolds.differentiable.scalarfield_algebra.DiffScalarFieldAlgebra`)
    and let `\\mathfrak{X}(M)` be the `C^\\infty(M)`-module of vector fields on
    `M` (cf.
    :class:`~sage.manifolds.differentiable.vectorfield_module.VectorFieldModule`).
    The *Levi-Civita connection associated with* `g` is the unique operator

    .. MATH::

        \\begin{array}{cccc}
        \\nabla: & \\mathfrak{X}(M)\\times \\mathfrak{X}(M) & \\longrightarrow &
                 \\mathfrak{X}(M) \\\\\n                & (u,v) & \\longmapsto & \\nabla_u v
        \\end{array}

    that

    - is `\\RR`-bilinear, i.e. is bilinear when considering `\\mathfrak{X}(M)` as
      a vector space over `\\RR`
    - is `C^\\infty(M)`-linear w.r.t. the first argument:
      `\\forall f\\in C^\\infty(M),\\ \\nabla_{fu} v = f\\nabla_u v`
    - obeys Leibniz rule w.r.t. the second argument:
      `\\forall f\\in C^\\infty(M),\\ \\nabla_u (f v) = \\mathrm{d}f(u)\\, v + f  \\nabla_u v`
    - is torsion-free
    - is compatible with `g`:
      `\\forall (u,v,w)\\in \\mathfrak{X}(M)^3,\\ u(g(v,w)) = g(\\nabla_u v, w) + g(v, \\nabla_u w)`

    The Levi-Civita connection `\\nabla` gives birth to the *covariant derivative
    operator* acting on tensor fields, denoted by the same symbol:

    .. MATH::

        \\begin{array}{cccc}
        \\nabla: &  T^{(k,l)}(M) & \\longrightarrow & T^{(k,l+1)}(M)\\\\\n                & t & \\longmapsto & \\nabla t
        \\end{array}

    where `T^{(k,l)}(M)` stands for the `C^\\infty(M)`-module of tensor fields
    of type `(k,l)` on `M` (cf.
    :class:`~sage.manifolds.differentiable.tensorfield_module.TensorFieldModule`),
    with the convention `T^{(0,0)}(M):=C^\\infty(M)`.
    For a vector field `v`,  the covariant derivative `\\nabla v` is a
    type-(1,1) tensor field such that

    .. MATH::

        \\forall u \\in\\mathfrak{X}(M), \\   \\nabla_u v = \\nabla v(., u)

    More generally for any tensor field `t\\in T^{(k,l)}(M)`, we have

    .. MATH::

        \\forall u \\in\\mathfrak{X}(M), \\   \\nabla_u t = \\nabla t(\\ldots, u)


    .. NOTE::

        The above convention means that, in terms of index notation,
        the "derivation index" in `\\nabla t` is the *last* one:

        .. MATH::

            \\nabla_c t^{a_1\\ldots a_k}_{\\quad\\quad b_1\\ldots b_l} =
                (\\nabla t)^{a_1\\ldots a_k}_{\\quad\\quad b_1\\ldots b_l c}


    INPUT:

    - ``metric`` -- the metric `g` defining the Levi-Civita connection, as an
      instance of class
      :class:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric`
    - ``name`` -- name given to the connection
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
      connection
    - ``init_coef`` -- boolean (default: ``True``); determines whether the Christoffel
      symbols are initialized (in the top charts on the domain, i.e.
      disregarding the subcharts)

    EXAMPLES:

    Levi-Civita connection associated with the Euclidean metric on `\\RR^3`
    expressed in spherical coordinates::

        sage: forget() # for doctests only
        sage: M = Manifold(3, \'R^3\', start_index=1)
        sage: c_spher.<r,th,ph> = M.chart(r\'r:(0,+oo) th:(0,pi):\\theta ph:(0,2*pi):\\phi\')
        sage: g = M.metric(\'g\')
        sage: g[1,1], g[2,2], g[3,3] = 1, r^2 , (r*sin(th))^2
        sage: g.display()
        g = dr⊗dr + r^2 dth⊗dth + r^2*sin(th)^2 dph⊗dph
        sage: nab = g.connection(name=\'nabla\', latex_name=r\'\\nabla\') ; nab
        Levi-Civita connection nabla associated with the Riemannian metric g on
         the 3-dimensional differentiable manifold R^3

    Let us check that the connection is compatible with the metric::

        sage: Dg = nab(g) ; Dg
        Tensor field nabla(g) of type (0,3) on the 3-dimensional
         differentiable manifold R^3
        sage: Dg == 0
        True

    and that it is torsionless::

        sage: nab.torsion() == 0
        True

    As a check, let us enforce the computation of the torsion::

        sage: sage.manifolds.differentiable.affine_connection.AffineConnection.torsion(nab) == 0
        True

    The connection coefficients in the manifold\'s default frame are Christoffel
    symbols, since the default frame is a coordinate frame::

        sage: M.default_frame()
        Coordinate frame (R^3, (∂/∂r,∂/∂th,∂/∂ph))
        sage: nab.coef()
        3-indices components w.r.t. Coordinate frame (R^3, (∂/∂r,∂/∂th,∂/∂ph)),
         with symmetry on the index positions (1, 2)

    We note that the Christoffel symbols are symmetric with respect to their
    last two indices (positions (1,2)); their expression is::

        sage: nab.coef()[:]  # display as a array
        [[[0, 0, 0], [0, -r, 0], [0, 0, -r*sin(th)^2]],
         [[0, 1/r, 0], [1/r, 0, 0], [0, 0, -cos(th)*sin(th)]],
         [[0, 0, 1/r], [0, 0, cos(th)/sin(th)], [1/r, cos(th)/sin(th), 0]]]
        sage: nab.display()  # display only the non-vanishing symbols
        Gam^r_th,th = -r
        Gam^r_ph,ph = -r*sin(th)^2
        Gam^th_r,th = 1/r
        Gam^th_th,r = 1/r
        Gam^th_ph,ph = -cos(th)*sin(th)
        Gam^ph_r,ph = 1/r
        Gam^ph_th,ph = cos(th)/sin(th)
        Gam^ph_ph,r = 1/r
        Gam^ph_ph,th = cos(th)/sin(th)
        sage: nab.display(only_nonredundant=True)  # skip redundancy due to symmetry
        Gam^r_th,th = -r
        Gam^r_ph,ph = -r*sin(th)^2
        Gam^th_r,th = 1/r
        Gam^th_ph,ph = -cos(th)*sin(th)
        Gam^ph_r,ph = 1/r
        Gam^ph_th,ph = cos(th)/sin(th)

    The same display can be obtained via the function
    :meth:`~sage.manifolds.differentiable.metric.PseudoRiemannianMetric.christoffel_symbols_display`
    acting on the metric::

        sage: g.christoffel_symbols_display(chart=c_spher)
        Gam^r_th,th = -r
        Gam^r_ph,ph = -r*sin(th)^2
        Gam^th_r,th = 1/r
        Gam^th_ph,ph = -cos(th)*sin(th)
        Gam^ph_r,ph = 1/r
        Gam^ph_th,ph = cos(th)/sin(th)
    '''
    def __init__(self, metric, name, latex_name=None, init_coef: bool = True) -> None:
        """
        Construct a Levi-Civita connection.

        TESTS:

        Levi-Civita connection of the hyperbolic plane::

            sage: M = Manifold(2, 'M')
            sage: X.<r,ph> = M.chart(r'r:(0,+oo) ph:(0,2*pi)')
            sage: g = M.metric('g')
            sage: g[0,0], g[1,1] = 1/(1+r^2), r^2
            sage: from sage.manifolds.differentiable.levi_civita_connection \\\n            ....:                                   import LeviCivitaConnection
            sage: nab = LeviCivitaConnection(g, 'nabla', latex_name=r'\\nabla')
            sage: nab
            Levi-Civita connection nabla associated with the Riemannian metric
             g on the 2-dimensional differentiable manifold M
            sage: TestSuite(nab).run()
        """
    def restrict(self, subdomain):
        """
        Return the restriction of the connection to some subdomain.

        If such restriction has not been defined yet, it is constructed here.

        INPUT:

        - ``subdomain`` -- open subset `U` of the connection's domain (must be
          an instance of
          :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`)

        OUTPUT:

        - instance of :class:`LeviCivitaConnection` representing the
          restriction.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: g = M.metric('g')
            sage: g[0,0], g[1,1] = 1+y^2, 1+x^2
            sage: nab = g.connection()
            sage: nab[:]
            [[[0, y/(y^2 + 1)], [y/(y^2 + 1), -x/(y^2 + 1)]],
             [[-y/(x^2 + 1), x/(x^2 + 1)], [x/(x^2 + 1), 0]]]
            sage: U = M.open_subset('U', coord_def={X: x>0})
            sage: nabU = nab.restrict(U); nabU
            Levi-Civita connection nabla_g associated with the Riemannian
             metric g on the Open subset U of the 2-dimensional differentiable
             manifold M
            sage: nabU[:]
            [[[0, y/(y^2 + 1)], [y/(y^2 + 1), -x/(y^2 + 1)]],
             [[-y/(x^2 + 1), x/(x^2 + 1)], [x/(x^2 + 1), 0]]]

        Let us check that the restriction is the connection compatible with the
        restriction of the metric::

            sage: nabU(g.restrict(U)).display()
            nabla_g(g) = 0
        """
    def coef(self, frame=None):
        """
        Return the connection coefficients relative to the given frame.

        `n` being the manifold's dimension, the connection coefficients
        relative to the vector frame `(e_i)` are the `n^3` scalar fields
        `\\Gamma^k_{\\ \\, ij}` defined by

        .. MATH::

            \\nabla_{e_j} e_i = \\Gamma^k_{\\ \\, ij} e_k

        If the connection coefficients are not known already, they are computed

         * as Christoffel symbols if the frame `(e_i)` is a coordinate frame
         * from the above formula otherwise

        INPUT:

        - ``frame`` -- (default: ``None``) vector frame relative to which the
          connection coefficients are required; if none is provided, the
          domain's default frame is assumed

        OUTPUT:

        - connection coefficients relative to the frame ``frame``, as an
          instance of the class :class:`~sage.tensor.modules.comp.Components`
          with 3 indices ordered as `(k,i,j)`; for Christoffel symbols,
          an instance of the subclass
          :class:`~sage.tensor.modules.comp.CompWithSym` is returned.

        EXAMPLES:

        Christoffel symbols of the Levi-Civita connection associated to
        the Euclidean metric on `\\RR^3` expressed in spherical coordinates::

            sage: M = Manifold(3, 'R^3', start_index=1)
            sage: c_spher.<r,th,ph> = M.chart(r'r:(0,+oo) th:(0,pi):\\theta ph:(0,2*pi):\\phi')
            sage: g = M.metric('g')
            sage: g[1,1], g[2,2], g[3,3] = 1, r^2 , (r*sin(th))^2
            sage: g.display()
            g = dr⊗dr + r^2 dth⊗dth + r^2*sin(th)^2 dph⊗dph
            sage: nab = g.connection()
            sage: gam = nab.coef() ; gam
            3-indices components w.r.t. Coordinate frame (R^3, (∂/∂r,∂/∂th,∂/∂ph)),
             with symmetry on the index positions (1, 2)
            sage: gam[:]
            [[[0, 0, 0], [0, -r, 0], [0, 0, -r*sin(th)^2]],
            [[0, 1/r, 0], [1/r, 0, 0], [0, 0, -cos(th)*sin(th)]],
            [[0, 0, 1/r], [0, 0, cos(th)/sin(th)], [1/r, cos(th)/sin(th), 0]]]

        The only nonzero Christoffel symbols::

            sage: gam[1,2,2], gam[1,3,3]
            (-r, -r*sin(th)^2)
            sage: gam[2,1,2], gam[2,3,3]
            (1/r, -cos(th)*sin(th))
            sage: gam[3,1,3], gam[3,2,3]
            (1/r, cos(th)/sin(th))

        Connection coefficients of the same connection with respect to the
        orthonormal frame associated to spherical coordinates::

            sage: ch_basis = M.automorphism_field()
            sage: ch_basis[1,1], ch_basis[2,2], ch_basis[3,3] = 1, 1/r, 1/(r*sin(th))
            sage: e = c_spher.frame().new_frame(ch_basis, 'e')
            sage: gam_e = nab.coef(e) ; gam_e
            3-indices components w.r.t. Vector frame (R^3, (e_1,e_2,e_3))
            sage: gam_e[:]
            [[[0, 0, 0], [0, -1/r, 0], [0, 0, -1/r]],
            [[0, 1/r, 0], [0, 0, 0], [0, 0, -cos(th)/(r*sin(th))]],
            [[0, 0, 1/r], [0, 0, cos(th)/(r*sin(th))], [0, 0, 0]]]

        The only nonzero connection coefficients::

            sage: gam_e[1,2,2], gam_e[2,1,2]
            (-1/r, 1/r)
            sage: gam_e[1,3,3], gam_e[3,1,3]
            (-1/r, 1/r)
            sage: gam_e[2,3,3], gam_e[3,2,3]
            (-cos(th)/(r*sin(th)), cos(th)/(r*sin(th)))
        """
    def torsion(self):
        """
        Return the connection's torsion tensor (identically zero for a
        Levi-Civita connection).

        See
        :meth:`sage.manifolds.differentiable.affine_connection.AffineConnection.torsion`
        for the general definition of the torsion tensor.

        OUTPUT:

        - the torsion tensor `T`, as a vanishing instance of
          :class:`~sage.manifolds.differentiable.tensorfield.TensorField`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: g = M.metric('g')
            sage: g[0,0], g[1,1] = 1+y^2, 1+x^2
            sage: nab = g.connection()
            sage: t = nab.torsion(); t
            Tensor field of type (1,2) on the 2-dimensional differentiable
             manifold M

        The torsion of a Levi-Civita connection is always zero::

            sage: t.display()
            0
        """
    def riemann(self, name=None, latex_name=None):
        '''
        Return the Riemann curvature tensor of the connection.

        This method redefines
        :meth:`sage.manifolds.differentiable.affine_connection.AffineConnection.riemann`
        to take into account the symmetry of the Riemann tensor for a
        Levi-Civita connection.

        The Riemann curvature tensor is the tensor field `R` of type (1,3)
        defined by

        .. MATH::

            R(\\omega, w, u, v) = \\left\\langle \\omega, \\nabla_u \\nabla_v w
                - \\nabla_v \\nabla_u w - \\nabla_{[u, v]} w \\right\\rangle

        for any 1-form  `\\omega`  and any vector fields `u`, `v` and `w`.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the Riemann tensor;
          if none, it is set to "Riem(g)", where "g" is the metric\'s name
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          Riemann tensor; if none, it is set to "\\\\mathrm{Riem}(g)", where "g"
          is the metric\'s name

        OUTPUT:

        - the Riemann curvature tensor `R`, as an instance of
          :class:`~sage.manifolds.differentiable.tensorfield.TensorField`

        EXAMPLES:

        Riemann tensor of the Levi-Civita connection associated with the
        metric of the hyperbolic plane (Poincaré disk model)::

            sage: M = Manifold(2, \'M\', start_index=1)
            sage: X.<x,y> = M.chart(\'x:(-1,1) y:(-1,1)\', coord_restrictions=lambda x,y: x^2+y^2<1)
            ....:   # Cartesian coord. on the Poincaré disk
            sage: g = M.metric(\'g\')
            sage: g[1,1], g[2,2] = 4/(1-x^2-y^2)^2, 4/(1-x^2-y^2)^2
            sage: nab = g.connection()
            sage: riem = nab.riemann(); riem
            Tensor field Riem(g) of type (1,3) on the 2-dimensional
             differentiable manifold M
            sage: riem.display_comp()
            Riem(g)^x_yxy = -4/(x^4 + y^4 + 2*(x^2 - 1)*y^2 - 2*x^2 + 1)
            Riem(g)^x_yyx = 4/(x^4 + y^4 + 2*(x^2 - 1)*y^2 - 2*x^2 + 1)
            Riem(g)^y_xxy = 4/(x^4 + y^4 + 2*(x^2 - 1)*y^2 - 2*x^2 + 1)
            Riem(g)^y_xyx = -4/(x^4 + y^4 + 2*(x^2 - 1)*y^2 - 2*x^2 + 1)

        The same computation parallelized on 2 cores::

            sage: Parallelism().set(nproc=2)
            sage: riem_backup = riem
            sage: g = M.metric(\'g\')
            sage: g[1,1], g[2,2] = 4/(1-x^2-y^2)^2, 4/(1-x^2-y^2)^2
            sage: nab = g.connection()
            sage: riem = nab.riemann(); riem
            Tensor field Riem(g) of type (1,3) on the 2-dimensional
             differentiable manifold M
            sage: riem == riem_backup
            True
            sage: Parallelism().set(nproc=1)  # switch off parallelization
        '''
    def ricci(self, name=None, latex_name=None):
        '''
        Return the connection\'s Ricci tensor.

        This method redefines
        :meth:`sage.manifolds.differentiable.affine_connection.AffineConnection.ricci`
        to take into account the symmetry of the Ricci tensor for a
        Levi-Civita connection.

        The Ricci tensor is the tensor field `Ric` of type (0,2)
        defined from the Riemann curvature tensor `R` by

        .. MATH::

            Ric(u, v) = R(e^i, u, e_i, v)

        for any vector fields `u` and `v`, `(e_i)` being any vector frame and
        `(e^i)` the dual coframe.

        INPUT:

        - ``name`` -- (default: ``None``) name given to the Ricci tensor;
          if none, it is set to "Ric(g)", where "g" is the metric\'s name
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          Ricci tensor; if none, it is set to "\\\\mathrm{Ric}(g)", where "g"
          is the metric\'s name

        OUTPUT:

        - the Ricci tensor `Ric`, as an instance of
          :class:`~sage.manifolds.differentiable.tensorfield.TensorField` of tensor
          type (0,2) and symmetric

        EXAMPLES:

        Ricci tensor of the standard connection on the 2-dimensional sphere::

            sage: M = Manifold(2, \'S^2\', start_index=1)
            sage: c_spher.<th,ph> = M.chart(r\'th:(0,pi):\\theta ph:(0,2*pi):\\phi\')
            sage: g = M.metric(\'g\')
            sage: g[1,1], g[2,2] = 1, sin(th)^2
            sage: g.display() # standard metric on S^2:
            g = dth⊗dth + sin(th)^2 dph⊗dph
            sage: nab = g.connection() ; nab
            Levi-Civita connection nabla_g associated with the Riemannian
             metric g on the 2-dimensional differentiable manifold S^2
            sage: ric = nab.ricci() ; ric
            Field of symmetric bilinear forms Ric(g) on the 2-dimensional
             differentiable manifold S^2
            sage: ric.display()
            Ric(g) = dth⊗dth + sin(th)^2 dph⊗dph

        Checking that the Ricci tensor of the Levi-Civita connection associated
        to Schwarzschild metric is identically zero (as a solution of the
        Einstein equation)::

            sage: M = Manifold(4, \'M\')
            sage: c_BL.<t,r,th,ph> = M.chart(r\'t r:(0,+oo) th:(0,pi):\\theta ph:(0,2*pi):\\phi\') # Schwarzschild-Droste coordinates
            sage: g = M.lorentzian_metric(\'g\')
            sage: m = var(\'m\')  # mass in Schwarzschild metric
            sage: g[0,0], g[1,1] = -(1-2*m/r), 1/(1-2*m/r)
            sage: g[2,2], g[3,3] = r^2, (r*sin(th))^2
            sage: g.display()
            g = (2*m/r - 1) dt⊗dt - 1/(2*m/r - 1) dr⊗dr + r^2 dth⊗dth
             + r^2*sin(th)^2 dph⊗dph
            sage: nab = g.connection() ; nab
            Levi-Civita connection nabla_g associated with the Lorentzian
             metric g on the 4-dimensional differentiable manifold M
            sage: ric = nab.ricci() ; ric
            Field of symmetric bilinear forms Ric(g) on the 4-dimensional
             differentiable manifold M
            sage: ric == 0
            True
        '''
