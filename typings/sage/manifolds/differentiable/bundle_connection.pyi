from sage.manifolds.differentiable.vector_bundle import DifferentiableVectorBundle as DifferentiableVectorBundle
from sage.rings.integer import Integer as Integer
from sage.structure.mutability import Mutability as Mutability
from sage.structure.sage_object import SageObject as SageObject

class BundleConnection(SageObject, Mutability):
    """
    An instance of this class represents a bundle connection `\\nabla` on a
    smooth vector bundle `E \\to M`.

    INPUT:

    - ``vbundle`` -- the vector bundle on which the connection is defined
      (must be an instance of class
      :class:`~sage.manifolds.differentiable.vector_bundle.DifferentiableVectorBundle`)
    - ``name`` -- name given to the bundle connection
    - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the bundle
      connection; if ``None``, it is set to ``name``

    EXAMPLES:

    Define a bundle connection on a rank 2 vector bundle over some
    3-dimensional smooth manifold::

        sage: M = Manifold(3, 'M', start_index=1)
        sage: X.<x,y,z> = M.chart()
        sage: E = M.vector_bundle(2, 'E')
        sage: e = E.local_frame('e') # standard frame for E
        sage: nab = E.bundle_connection('nabla'); nab
        Bundle connection nabla on the Differentiable real vector bundle E -> M
         of rank 2 over the base space 3-dimensional differentiable manifold M

    First, let us initialize all connection 1-forms w.r.t. the frame ``e`` to
    zero::

        sage: nab[e, :] = [[0, 0], [0, 0]]

    This line can be shortened by the following::

        sage: nab[e, :] = 0  # initialize to zero

    The connection 1-forms are now initialized being differential 1-forms::

        sage: nab[e, 1, 1].parent()
        Free module Omega^1(M) of 1-forms on the 3-dimensional differentiable
         manifold M
        sage: nab[e, 1, 1].display()
        connection (1,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = 0

    Now, we want to specify some nonzero entries::

        sage: nab[e, 1, 2][:] = [x*z, y*z, z^2]
        sage: nab[e, 2, 1][:] = [x, x^2, x^3]
        sage: nab[e, 1, 1][:] = [x+z, y-z, x*y*z]
        sage: nab.display()
        connection (1,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = (x + z) dx + (y - z) dy + x*y*z dz
        connection (1,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = x*z dx + y*z dy + z^2 dz
        connection (2,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = x dx + x^2 dy + x^3 dz

    Notice, when we omit the frame, the default frame of the vector bundle is
    assumed (in this case ``e``)::

        sage: nab[2, 2].display()
        connection (2,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = 0

    The same holds for the assignment::

        sage: nab[1, 2] = 0
        sage: nab[e, 1, 2].display()
        connection (1,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = 0

    Keep noticed that item assignments for bundle connections only copy the
    right-hand-side and never create a binding to the original instance::

        sage: omega = M.one_form('omega')
        sage: omega[:] = [x*z, y*z, z^2]
        sage: nab[1, 2] = omega
        sage: nab[1, 2] == omega
        True
        sage: nab[1, 2] is omega
        False

    Hence, this is therefore equivalent to::

        sage: nab[2, 2].copy_from(omega)

    Preferably, we use :meth:`set_connection_form` to specify the connection
    1-forms::

        sage: nab[:] = 0  # re-initialize to zero
        sage: nab.set_connection_form(1, 2)[:] = [x*z, y*z, z^2]
        sage: nab.set_connection_form(2, 1)[:] = [x, x^2, x^3]
        sage: nab[1, 2].display()
        connection (1,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = x*z dx + y*z dy + z^2 dz
        sage: nab[2, 1].display()
        connection (2,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = x dx + x^2 dy + x^3 dz

    .. NOTE::

        Notice that item assignments and :meth:`set_connection_form` delete
        the connection 1-forms w.r.t. other frames for consistency reasons. To
        avoid this behavior, :meth:`add_connection_form` must be used instead.

    In conclusion, the connection 1-forms of a bundle connection are mutable
    until the connection itself is set immutable::

        sage: nab.set_immutable()
        sage: nab[1, 2] = omega
        Traceback (most recent call last):
        ...
        ValueError: object is immutable; please change a copy instead

    By definition, a bundle connection acts on vector fields and sections::

        sage: v = M.vector_field((x^2,y^2,z^2), name='v'); v.display()
        v = x^2 ∂/∂x + y^2 ∂/∂y + z^2 ∂/∂z
        sage: s = E.section((x-y^2, -z), name='s'); s.display()
        s = (-y^2 + x) e_1 - z e_2
        sage: nab_vs = nab(v, s); nab_vs
        Section nabla_v(s) on the 3-dimensional differentiable manifold M with
         values in the real vector bundle E of rank 2
        sage: nab_vs.display()
        nabla_v(s) = (-x^3*z^3 - 2*y^3 + x^2 - (x^2*y^2 + x^3)*z) e_1 +
         (-(y^2 - x)*z^4 - (x^3*y^2 + y^5 - x^4 - x*y^3)*z - z^2) e_2

    The bundle connection action certainly obeys the defining formula for
    the connection 1-forms::

        sage: vframe = X.frame()
        sage: all(nab(vframe[k], e[i]) == sum(nab[e, i, j](vframe[k])*e[j]
        ....:                                 for j in E.irange())
        ....:     for i in E.irange() for k in M.irange())
        True

    The connection 1-forms are computed automatically for different frames::

        sage: f = E.local_frame('f', ((1+x^2)*e[1], e[1]-e[2]))
        sage: nab.display(frame=f)
        connection (1,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (f_1,f_2)) = ((x^3 + x)*z + 2*x)/(x^2 + 1) dx + y*z dy + z^2 dz
        connection (1,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (f_1,f_2)) = -(x^3 + x)*z dx - (x^2 + 1)*y*z dy -
          (x^2 + 1)*z^2 dz
        connection (2,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (f_1,f_2)) = (x*z - x)/(x^2 + 1) dx -
          (x^2 - y*z)/(x^2 + 1) dy - (x^3 - z^2)/(x^2 + 1) dz
        connection (2,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (f_1,f_2)) = -x*z dx - y*z dy - z^2 dz

    The new connection 1-forms obey the defining formula, too::

        sage: all(nab(vframe[k], f[i]) == sum(nab[f, i, j](vframe[k])*f[j]
        ....:                                 for j in E.irange())
        ....:     for i in E.irange() for k in M.irange())
        True

    After the connection has been specified, the curvature 2-forms can be
    derived::

        sage: Omega = nab.curvature_form
        sage: for i in E.irange():
        ....:     for j in E.irange():
        ....:         print(Omega(i ,j, e).display())
        curvature (1,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = -(x^3 - x*y)*z dx∧dy + (-x^4*z + x*z^2) dx∧dz +
          (-x^3*y*z + x^2*z^2) dy∧dz
        curvature (1,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = -x dx∧dz - y dy∧dz
        curvature (2,1) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = 2*x dx∧dy + 3*x^2 dx∧dz
        curvature (2,2) of bundle connection nabla w.r.t. Local frame
         (E|_M, (e_1,e_2)) = (x^3 - x*y)*z dx∧dy + (x^4*z - x*z^2) dx∧dz +
          (x^3*y*z - x^2*z^2) dy∧dz

    The derived forms certainly obey the structure equations, see
    :meth:`curvature_form` for details::

        sage: omega = nab.connection_form
        sage: check = []
        sage: for i in E.irange():  # long time
        ....:     for j in E.irange():
        ....:         check.append(Omega(i,j,e) == \\\n        ....:                       omega(i,j,e).exterior_derivative() + \\\n        ....:         sum(omega(k,j,e).wedge(omega(i,k,e))
        ....:             for k in E.irange()))
        sage: check  # long time
        [True, True, True, True]
    """
    def __init__(self, vbundle, name, latex_name=None) -> None:
        """
        Construct a bundle connection.

        TESTS::

            sage: M = Manifold(3, 'M')
            sage: E = M.vector_bundle(2, 'E')
            sage: from sage.manifolds.differentiable.bundle_connection \\\n            ....:                                       import BundleConnection
            sage: nab = BundleConnection(E, 'nabla', latex_name=r'\\nabla')
            sage: nab
            Bundle connection nabla on the Differentiable real vector bundle
             E -> M of rank 2 over the base space 3-dimensional differentiable
             manifold M
            sage: X.<x,y,z> = M.chart()
            sage: e = E.local_frame('e')
            sage: nab[:] = 0
            sage: nab.set_connection_form(1, 0)[:] = [x*z, y*z, z^2]
            sage: TestSuite(nab).run()
        """
    def __eq__(self, other):
        """
        Comparison (equality) operator.

        INPUT:

        - ``other`` -- a bundle connection

        OUTPUT: ``True`` if ``self`` is equal to ``other`` and ``False`` otherwise

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')  # standard frame for E
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab[:] = 0
            sage: nab[0, 1][:] = [x^2, x]
            sage: nab[1, 0][:] = [y^2, y]
            sage: nab1 = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab1[:] = 0
            sage: (nab1 == nab) or (nab == nab1)
            False
            sage: nab1[0, 1][:] = [x, x^2]
            sage: nab1[1, 0][:] = [y, y^2]
            sage: (nab1 == nab) or (nab == nab1)
            False
            sage: nab1[0, 1][:] = [x^2, x]
            sage: nab1[1, 0][:] = [y^2, y]
            sage: (nab1 == nab) and (nab == nab1)
            True
        """
    def __ne__(self, other):
        """
        Inequality operator.

        INPUT:

        - ``other`` -- an affine connection

        OUTPUT:

        - ``True`` if ``self`` is different from ``other`` and ``False``
          otherwise

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')  # standard frame for E
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab[:] = 0
            sage: nab[0, 1][:] = [x^2, x]
            sage: nab[1, 0][:] = [y^2, y]
            sage: nab1 = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab1[:] = 0
            sage: (nab1 != nab) and (nab != nab1)
            True
            sage: nab1[0, 1][:] = [x, x^2]
            sage: nab1[1, 0][:] = [y, y^2]
            sage: (nab1 != nab) and (nab != nab1)
            True
            sage: nab1[0, 1][:] = [x^2, x]
            sage: nab1[1, 0][:] = [y^2, y]
            sage: (nab1 != nab) or (nab != nab1)
            False
        """
    def vector_bundle(self):
        """
        Return the vector bundle on which the bundle connection is defined.

        OUTPUT:

        - instance of class
          :class:`~sage.manifolds.differentiable.vector_bundle.DifferentiableVectorBundle`
          representing the vector bundle on which ``self`` is defined.

        EXAMPLES::

            sage: M = Manifold(3, 'M', start_index=1)
            sage: c_xyz.<x,y,z> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: nab = E.bundle_connection('nabla', r'\\nabla')
            sage: nab.vector_bundle()
            Differentiable real vector bundle E -> M of rank 2 over the base
             space 3-dimensional differentiable manifold M
        """
    def connection_forms(self, frame=None):
        """
        Return the connection forms relative to the given frame.

        If `e` is a local frame on `E`, we have

        .. MATH::

            \\nabla e_i = \\sum^n_{j=1} e_j \\otimes \\omega^j_i ,

        and the corresponding `n \\times n`-matrix `(\\omega^j_i)_{i,j}`
        consisting of one forms is called *connection matrix of* `\\nabla` *with
        respect to* `e`.

        If the connection coefficients are not known already, they are computed
        from the above formula.

        INPUT:

        - ``frame`` -- (default: ``None``) local frame relative to which the
          connection forms are required; if none is provided, the
          vector bundle's default frame is assumed

        OUTPUT:

        - connection forms relative to the frame ``frame``, as a dictionary
          with tuples `(i, j)` as key and one forms as instances of
          :class:`~sage.manifolds.differentiable.diff_form` as value
          representing the matrix entries.

        EXAMPLES:

        Connection forms of a bundle connection on a rank 2 vector bundle
        over a 3-dimensional manifold::

            sage: M = Manifold(3, 'M', start_index=1)
            sage: c_xyz.<x,y,z> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: nab = E.bundle_connection('nabla', r'\\nabla')
            sage: nab[:] = 0  # initialize curvature forms
            sage: forms = nab.connection_forms()
            sage: [forms[k] for k in sorted(forms)]
            [1-form connection (1,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 3-dimensional differentiable
             manifold M,
            1-form connection (1,2) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 3-dimensional differentiable
             manifold M,
            1-form connection (2,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 3-dimensional differentiable
             manifold M,
            1-form connection (2,2) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 3-dimensional differentiable
             manifold M]
        """
    def connection_form(self, i, j, frame=None):
        """
        Return the connection 1-form corresponding to the given index and
        local frame.

        .. SEEALSO::

            Consult :meth:`connection_forms` for detailed information.

        INPUT:

        - ``i``, ``j`` -- indices identifying the 1-form `\\omega^j_i`
        - ``frame`` -- (default: ``None``) local frame relative to which the
          connection 1-forms are defined; if ``None``, the default frame of the
          vector bundle's corresponding section module is assumed.

        OUTPUT:

        - the 1-form `\\omega^j_i`, as an instance of
          :class:`~sage.manifolds.differentiable.diff_form.DiffForm`

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # standard frame for E
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab.set_connection_form(0, 1)[:] = [x^2, x]
            sage: nab.set_connection_form(1, 0)[:] = [y^2, y]
            sage: nab.connection_form(0, 1).display()
            connection (0,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = x^2 dx + x dy
            sage: nab.connection_form(1, 0).display()
            connection (1,0) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = y^2 dx + y dy
        """
    def __call__(self, v, s):
        """
        Action of the connection on a vector field and local section.

        INPUT:

        - ``v`` -- a vector field `v` on the base space
        - ``s`` -- a local section `s`

        OUTPUT: local section `\\nabla_v s`

        TESTS::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab[:] = 0
            sage: nab[1,2][1] = x*y
            sage: v = M.vector_field('v')
            sage: v[:] = [-y, x]
            sage: s = E.section('s')
            sage: s[:] = [y, -x]
            sage: nab.__call__(v, s)
            Section nabla_v(s) on the 2-dimensional differentiable manifold M
             with values in the real vector bundle E of rank 2
        """
    def add_connection_form(self, i, j, frame=None):
        """
        Return the connection form `\\omega^j_i` in a given frame for
        assignment.

        See method :meth:`connection_forms` for details about the definition of
        the connection forms.

        To delete the connection forms in other frames, use the method
        :meth:`set_connection_form` instead.

        INPUT:

        - ``i``, ``j`` -- indices identifying the 1-form `\\omega^j_i`
        - ``frame`` -- (default: ``None``) local frame in which the connection
          1-form is defined; if ``None``, the default frame of the vector
          bundle is assumed.

        .. WARNING::

            If the connection has already forms in other frames, it is the
            user's responsibility to make sure that the 1-forms to be added
            are consistent with them.

        OUTPUT:

        - connection 1-form `\\omega^j_i` in the given frame, as an instance of
          the class :class:`~sage.manifolds.differentiable.diff_form.DiffForm`;
          if such connection 1-form did not exist previously, it is created.
          See method :meth:`connection_forms` for the storage convention of the
          connection 1-forms.

        EXAMPLES::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # standard frame for E
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab.add_connection_form(0, 1, frame=e)[:] = [x^2, x]
            sage: nab[e, 0, 1].display()
            connection (0,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = x^2 dx + x dy

        Since ``e`` is the vector bundle's default local frame, its mention may
        be omitted::

            sage: nab.add_connection_form(1, 0)[:] = [y^2, y]
            sage: nab[1, 0].display()
            connection (1,0) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = y^2 dx + y dy

        Adding connection 1-forms w.r.t. to another local frame::

            sage: f = E.local_frame('f')
            sage: nab.add_connection_form(1, 1, frame=f)[:] = [x, y]
            sage: nab[f, 1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (f_0,f_1)) = x dx + y dy

        The forms w.r.t. the frame ``e`` have been kept::

            sage: nab[e, 0, 1].display()
            connection (0,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = x^2 dx + x dy

        To delete them, use the method :meth:`set_connection_form` instead.
        """
    def set_connection_form(self, i, j, frame=None):
        """
        Return the connection form `\\omega^j_i` in a given frame for
        assignment.

        See method :meth:`connection_forms` for details about the definition of
        the connection forms.

        The connection forms with respect to other frames are deleted,
        in order to avoid any inconsistency. To keep them, use the method
        :meth:`add_connection_form` instead.

        INPUT:

        - ``i``, ``j`` -- indices identifying the 1-form `\\omega^j_i`
        - ``frame`` -- (default: ``None``) local frame in which the connection
          1-form is defined; if ``None``, the default frame of the vector
          bundle is assumed.

        OUTPUT:

        - connection 1-form `\\omega^j_i` in the given frame, as an instance of
          the class :class:`~sage.manifolds.differentiable.diff_form.DiffForm`;
          if such connection 1-form did not exist previously, it is created.
          See method :meth:`connection_forms` for the storage convention of the
          connection 1-forms.

        EXAMPLES:

        Setting the connection forms of a bundle connection w.r.t. some local
        frame::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # standard frame for E
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: nab.set_connection_form(0, 1)[:] = [x^2, x]
            sage: nab[0, 1].display()
            connection (0,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = x^2 dx + x dy

        Since ``e`` is the vector bundle's default local frame, its mention may
        be omitted::

            sage: nab.set_connection_form(1, 0)[:] = [y^2, y]
            sage: nab[1, 0].display()
            connection (1,0) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_0,e_1)) = y^2 dx + y dy

        Setting connection 1-forms w.r.t. to another local frame::

            sage: f = E.local_frame('f')
            sage: nab.set_connection_form(1, 1, frame=f)[:] = [x, y]
            sage: nab[f, 1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (f_0,f_1)) = x dx + y dy

        The forms w.r.t. the frame ``e`` have been deleted::

            sage: nab[e, 0, 1].display()
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components in
             the Local frame (E|_M, (f_0,f_1))

        To keep them, use the method :meth:`add_connection_form` instead.
        """
    def del_other_forms(self, frame=None) -> None:
        """
        Delete all the connection forms but those corresponding to ``frame``.

        INPUT:

        - ``frame`` -- (default: ``None``) local frame, the connection forms
          w.r.t. which are to be kept; if ``None``, the default frame of the
          vector bundle is assumed.

        EXAMPLES:

        We first create two sets of connection forms::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: e = E.local_frame('e')
            sage: nab.set_connection_form(1, 1, frame=e)[:] = [x^2, x]
            sage: f = E.local_frame('f')
            sage: nab.add_connection_form(1, 1, frame=f)[:] = [y^2, y]
            sage: nab[e, 1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy
            sage: nab[f, 1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (f_1,f_2)) = y^2 dx + y dy

        Let us delete the connection forms w.r.t. all frames except for
        frame ``e``::

            sage: nab.del_other_forms(e)
            sage: nab[e, 1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy

        The connection forms w.r.t. frame ``e`` have indeed been
        deleted::

            sage: nab[f, :]
            Traceback (most recent call last):
            ...
            ValueError: no basis could be found for computing the components in
             the Local frame (E|_M, (e_1,e_2))
        """
    def curvature_form(self, i, j, frame=None):
        """
        Return the curvature 2-form corresponding to the given index and local
        frame.

        The *curvature 2-forms* with respect to the frame `e` are the 2-forms
        `\\Omega^j_i` given by the formula

        .. MATH::

            \\Omega^j_i = \\mathrm{d} \\omega^j_i + \\sum^n_{k=1} \\omega^j_k
                \\wedge \\omega^k_i

        INPUT:

        - ``i``, ``j`` -- indices identifying the 2-form `\\Omega^j_i`
        - ``frame`` -- (default: ``None``) local frame relative to which the
          curvature 2-forms are defined; if ``None``, the default frame
          of the vector bundle is assumed.

        OUTPUT:

        - the 2-form `\\Omega^j_i`, as an instance of
          :class:`~sage.manifolds.differentiable.diff_form.DiffForm`

        EXAMPLES::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(1, 'E')
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: e = E.local_frame('e')
            sage: nab.set_connection_form(1, 1)[:] = [x^2, x]
            sage: curv = nab.curvature_form(1, 1); curv
            2-form curvature (1,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1)) on the 2-dimensional differentiable manifold M
            sage: curv.display()
            curvature (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1)) = dx∧dy
        """
    def __hash__(self):
        """
        Hash function.

        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla')
            sage: hash(nab)
            Traceback (most recent call last):
            ...
            ValueError: object is mutable; please make it immutable first
            sage: nab.set_immutable()
            sage: hash(nab) == nab.__hash__()
            True

        Let us check that ``nab`` can be used as a dictionary key::

            sage: {nab: 1}[nab]
            1
        """
    def __getitem__(self, args):
        """
        Return a component of ``self`` with respect to some frame.

        INPUT:

        - ``args`` -- list of indices defining the component; if ``[:]`` is
          provided, all the components are returned

        TESTS::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: nab = E.bundle_connection('nabla')
            sage: e = E.local_frame('e')
            sage: nab[:] = 0
            sage: nab[1, 2][:] = [x^2, x]
            sage: nab[1, 1][:] = [y, y]
            sage: nab[1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = y dx + y dy
            sage: nab[e, 1, 2].display()
            connection (1,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy
            sage: nab[e, :]
            [[1-form connection (1,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M,
             1-form connection (1,2) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M],
             [1-form connection (2,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M,
             1-form connection (2,2) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M]]
            sage: nab[:]
            [[1-form connection (1,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M,
             1-form connection (1,2) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M],
             [1-form connection (2,1) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M,
             1-form connection (2,2) of bundle connection nabla w.r.t. Local
             frame (E|_M, (e_1,e_2)) on the 2-dimensional differentiable
             manifold M]]
        """
    def __setitem__(self, args, value) -> None:
        """
        Set the components of ``self`` corresponding to the given indices.

        INPUT:

        - ``args`` -- list of indices (usually a pair of integers); if ``[:]``
          is provided, all the components are set
        - ``value`` -- the value to be set or a list of values if
          ``args = [:]``

        TESTS::

            sage: M = Manifold(2, 'M', start_index=1)
            sage: X.<x,y> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: nab = E.bundle_connection('nabla')
            sage: e = E.local_frame('e')
            sage: a = M.one_form([x^2, x], name='a')
            sage: a.display()
            a = x^2 dx + x dy
            sage: nab[:] = 0
            sage: nab[1, 1] = a
            sage: nab[1, 1].display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy
            sage: nab[e, 2, 2] = a
            sage: nab[e, 2, 2].display()
            connection (2,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy
            sage: nab[:] = [[0, 0], [a, a]]
            sage: nab[e, 2, 1].display()
            connection (2,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy
            sage: nab[e, :] = [[a, a], [0, 0]]
            sage: nab[e, 1, 2].display()
            connection (1,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + x dy
        """
    def display(self, frame=None, vector_frame=None, chart=None, only_nonzero: bool = True):
        """
        Display all the connection 1-forms w.r.t. to a given local frame, one
        per line.

        The output is either text-formatted (console mode) or LaTeX-formatted
        (notebook mode).

        INPUT:

        - ``frame`` -- (default: ``None``) local frame of the vector bundle
          relative to which the connection 1-forms are defined; if ``None``,
          the default frame of the bundle is used
        - ``vector_frame`` -- (default: ``None``) vector frame of the manifold
          relative to which the connection 1-forms should be displayed; if
          ``None``, the default frame of the local frame's domain is used
        - ``chart`` -- (default: ``None``) chart specifying the coordinate
          expression of the connection 1-forms; if ``None``,
          the default chart of the domain of ``frame`` is used
        - ``only_nonzero`` -- boolean (default: ``True``); if ``True``, only
          nonzero connection coefficients are displayed

        EXAMPLES:

        Set connection 1-forms::

            sage: M = Manifold(3, 'M', start_index=1)
            sage: X.<x,y,z> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e') # standard frame for E
            sage: nab = E.bundle_connection('nabla', latex_name=r'\\nabla'); nab
            Bundle connection nabla on the Differentiable real vector bundle
             E -> M of rank 2 over the base space 3-dimensional differentiable
             manifold M
            sage: nab[:] = 0
            sage: nab[1, 1][:] = [x, y, z]
            sage: nab[2, 2][:] = [x^2, y^2, z^2]

        By default, only the nonzero connection coefficients are displayed::

            sage: nab.display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x dx + y dy + z dz
            connection (2,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + y^2 dy + z^2 dz
            sage: latex(nab.display())
            \\begin{array}{lcl} \\omega^1_{\\ \\, 1} = x \\mathrm{d} x +
             y \\mathrm{d} y + z \\mathrm{d} z \\\\ \\omega^2_{\\ \\, 2} = x^{2}
             \\mathrm{d} x + y^{2} \\mathrm{d} y + z^{2} \\mathrm{d} z \\end{array}

        By default, the displayed connection 1-forms are those w.r.t.
        the default frame of the vector bundle. The aforementioned is
        therefore equivalent to::

            sage: nab.display(frame=E.default_frame())
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x dx + y dy + z dz
            connection (2,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + y^2 dy + z^2 dz

        Moreover, the connection 1-forms are displayed w.r.t. the default
        vector frame on the local frame's domain, i.e.::

            sage: domain = e.domain()
            sage: nab.display(vector_frame=domain.default_frame())
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x dx + y dy + z dz
            connection (2,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + y^2 dy + z^2 dz

        By default, the parameter ``only_nonzero`` is set to ``True``.
        Otherwise, the connection 1-forms being zero are shown as well::

            sage: nab.display(only_nonzero=False)
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x dx + y dy + z dz
            connection (1,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = 0
            connection (2,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = 0
            connection (2,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + y^2 dy + z^2 dz
        """
    def copy(self, name, latex_name=None):
        """
        Return an exact copy of ``self``.

        INPUT:

        - ``name`` -- name given to the copy
        - ``latex_name`` -- (default: ``None``) LaTeX symbol to denote the
          copy; if none is provided, the LaTeX symbol is set to ``name``

        .. NOTE::

            The name and the derived quantities are not copied.

        EXAMPLES::

            sage: M = Manifold(3, 'M', start_index=1)
            sage: X.<x,y,z> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: nab = E.bundle_connection('nabla')
            sage: nab.set_connection_form(1, 1)[:] = [x^2, x-z, y^3]
            sage: nab.set_connection_form(1, 2)[:] = [1, x, z*y^3]
            sage: nab.set_connection_form(2, 1)[:] = [1, 2, 3]
            sage: nab.set_connection_form(2, 2)[:] = [0, 0, 0]
            sage: nab.display()
            connection (1,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + (x - z) dy + y^3 dz
            connection (1,2) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = dx + x dy + y^3*z dz
            connection (2,1) of bundle connection nabla w.r.t. Local frame
             (E|_M, (e_1,e_2)) = dx + 2 dy + 3 dz
            sage: nab_copy = nab.copy('nablo'); nab_copy
            Bundle connection nablo on the Differentiable real vector bundle
             E -> M of rank 2 over the base space 3-dimensional differentiable
             manifold M
            sage: nab is nab_copy
            False
            sage: nab == nab_copy
            True
            sage: nab_copy.display()
            connection (1,1) of bundle connection nablo w.r.t. Local frame
             (E|_M, (e_1,e_2)) = x^2 dx + (x - z) dy + y^3 dz
            connection (1,2) of bundle connection nablo w.r.t. Local frame
             (E|_M, (e_1,e_2)) = dx + x dy + y^3*z dz
            connection (2,1) of bundle connection nablo w.r.t. Local frame
             (E|_M, (e_1,e_2)) = dx + 2 dy + 3 dz
        """
    def set_immutable(self) -> None:
        """
        Set ``self`` and all restrictions of ``self`` immutable.

        EXAMPLES:

        An affine connection can be set immutable::

            sage: M = Manifold(3, 'M', start_index=1)
            sage: X.<x,y,z> = M.chart()
            sage: E = M.vector_bundle(2, 'E')
            sage: e = E.local_frame('e')
            sage: nab = E.bundle_connection('nabla')
            sage: nab.set_connection_form(1, 1)[:] = [x^2, x-z, y^3]
            sage: nab.set_connection_form(1, 2)[:] = [1, x, z*y^3]
            sage: nab.set_connection_form(2, 1)[:] = [1, 2, 3]
            sage: nab.set_connection_form(2, 2)[:] = [0, 0, 0]
            sage: nab.is_immutable()
            False
            sage: nab.set_immutable()
            sage: nab.is_immutable()
            True

        The coefficients of immutable elements cannot be changed::

            sage: f = E.local_frame('f')
            sage: nab.add_connection_form(1, 1, frame=f)[:] = [x, y, z]
            Traceback (most recent call last):
            ...
            ValueError: object is immutable; please change a copy instead
        """
