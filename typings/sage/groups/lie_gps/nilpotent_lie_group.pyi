from sage.algebras.lie_algebras.structure_coefficients import LieAlgebraWithStructureCoefficients as LieAlgebraWithStructureCoefficients
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.lie_groups import LieGroups as LieGroups
from sage.groups.group import Group as Group
from sage.manifolds.differentiable.manifold import DifferentiableManifold as DifferentiableManifold
from sage.manifolds.structure import DifferentialStructure as DifferentialStructure, RealDifferentialStructure as RealDifferentialStructure
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.modules.free_module_element import vector as vector
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.symbolic.ring import SR as SR

class NilpotentLieGroup(Group, DifferentiableManifold):
    """
    A nilpotent Lie group.

    INPUT:

    - ``L`` -- the Lie algebra of the Lie group; must be a finite
      dimensional nilpotent Lie algebra with basis over a topological
      field, e.g. `\\QQ` or `\\RR`
    - ``name`` -- string; name (symbol) given to the Lie group

    Two types of exponential coordinates are defined on any
    nilpotent Lie group using the basis of the Lie algebra,
    see :meth:`chart_exp1` and :meth:`chart_exp2`.

    EXAMPLES:

    Creation of a nilpotent Lie group::

        sage: L = lie_algebras.Heisenberg(QQ, 1)
        sage: G = L.lie_group(); G
        Lie group G of Heisenberg algebra of rank 1 over Rational Field

    Giving a different name to the group::

        sage: L.lie_group('H')
        Lie group H of Heisenberg algebra of rank 1 over Rational Field

    Elements can be created using the exponential map::

        sage: p,q,z = L.basis()
        sage: g = G.exp(p); g
        exp(p1)
        sage: h = G.exp(q); h
        exp(q1)

    Lie group multiplication has the usual product syntax::

        sage: k = g*h; k
        exp(p1 + q1 + 1/2*z)

    The identity element is given by :meth:`one`::

        sage: e = G.one(); e
        exp(0)
        sage: e*k == k and k*e == k
        True

    The default coordinate system is exponential coordinates of the first kind::

        sage: G.default_chart() == G.chart_exp1()
        True
        sage: G.chart_exp1()
        Chart (G, (x_0, x_1, x_2))

    Changing the default coordinates to exponential coordinates of the second
    kind will change how elements are printed::

        sage: G.set_default_chart(G.chart_exp2())
        sage: k
        exp(z)exp(q1)exp(p1)
        sage: G.set_default_chart(G.chart_exp1())
        sage: k
        exp(p1 + q1 + 1/2*z)

    The frames of left- or right-invariant vector fields are created using
    :meth:`left_invariant_frame` and :meth:`right_invariant_frame`::

        sage: X = G.left_invariant_frame(); X
        Vector frame (G, (X_0,X_1,X_2))
        sage: X[0]
        Vector field X_0 on the Lie group G of Heisenberg algebra of rank 1 over Rational Field

    A vector field can be displayed with respect to a coordinate frame::

        sage: exp1_frame = G.chart_exp1().frame()
        sage: exp2_frame = G.chart_exp2().frame()
        sage: X[0].display(exp1_frame)
        X_0 = ∂/∂x_0 - 1/2*x_1 ∂/∂x_2
        sage: X[0].display(exp2_frame)
        X_0 = ∂/∂y_0
        sage: X[1].display(exp1_frame)
        X_1 = ∂/∂x_1 + 1/2*x_0 ∂/∂x_2
        sage: X[1].display(exp2_frame)
        X_1 = ∂/∂y_1 + x_0 ∂/∂y_2

    Defining a left translation by a generic point::

        sage: g = G.point([var('a'), var('b'), var('c')]); g
        exp(a*p1 + b*q1 + c*z)
        sage: L_g = G.left_translation(g); L_g
        Diffeomorphism of the Lie group G of Heisenberg algebra of rank 1 over Rational Field
        sage: L_g.display()
        G → G
           (x_0, x_1, x_2) ↦ (a + x_0, b + x_1, -1/2*b*x_0 + 1/2*a*x_1 + c + x_2)
           (x_0, x_1, x_2) ↦ (y_0, y_1, y_2) = (a + x_0, b + x_1,
                                                1/2*a*b + 1/2*(2*a + x_0)*x_1 + c + x_2)
           (y_0, y_1, y_2) ↦ (x_0, x_1, x_2) = (a + y_0, b + y_1,
                                                -1/2*b*y_0 + 1/2*(a - y_0)*y_1 + c + y_2)
           (y_0, y_1, y_2) ↦ (a + y_0, b + y_1, 1/2*a*b + a*y_1 + c + y_2)

    Verifying the left-invariance of the left-invariant frame::

        sage: x = G(G.chart_exp1()[:])
        sage: L_g.differential(x)(X[0].at(x)) == X[0].at(L_g(x))
        True
        sage: L_g.differential(x)(X[1].at(x)) == X[1].at(L_g(x))
        True
        sage: L_g.differential(x)(X[2].at(x)) == X[2].at(L_g(x))
        True

    An element of the Lie algebra can be extended to a left or right invariant
    vector field::

        sage: X_L = G.left_invariant_extension(p + 3*q); X_L
        Vector field p1 + 3*q1 on the Lie group G of Heisenberg algebra of rank 1 over Rational Field
        sage: X_L.display(exp1_frame)
        p1 + 3*q1 = ∂/∂x_0 + 3 ∂/∂x_1 + (3/2*x_0 - 1/2*x_1) ∂/∂x_2
        sage: X_R = G.right_invariant_extension(p + 3*q)
        sage: X_R.display(exp1_frame)
        p1 + 3*q1 = ∂/∂x_0 + 3 ∂/∂x_1 + (-3/2*x_0 + 1/2*x_1) ∂/∂x_2

    The nilpotency step of the Lie group is the nilpotency step of its algebra.
    Nilpotency for Lie groups means that group commutators that are longer than
    the nilpotency step vanish::

        sage: G.step()
        2
        sage: g = G.exp(p); h = G.exp(q)
        sage: c = g*h*~g*~h; c
        exp(z)
        sage: g*c*~g*~c
        exp(0)
    """
    def __init__(self, L, name, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: L = lie_algebras.Heisenberg(QQ, 2)
            sage: G = L.lie_group()
            sage: TestSuite(G).run()
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return a tuple of elements whose one-parameter subgroups generate
        the Lie group.

        EXAMPLES::

            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: G = L.lie_group()
            sage: G.gens()
            (exp(p1), exp(q1), exp(z))
        """
    def lie_algebra(self):
        """
        Return the Lie algebra of ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: G.lie_algebra() == L
            True
        """
    def step(self):
        """
        Return the nilpotency step of ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 2, step=4)
            sage: G = L.lie_group()
            sage: G.step()
            4
        """
    def chart_exp1(self):
        """
        Return the chart of exponential coordinates of the first kind.

        Exponential coordinates of the first kind are

        .. MATH ::

            \\exp(x_1X_1 + \\cdots + x_nX_n) \\mapsto (x_1, \\ldots, x_n).

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: G.chart_exp1()
            Chart (G, (x_1, x_2, x_12))
        """
    @cached_method
    def chart_exp2(self):
        """
        Return the chart of exponential coordinates of the second kind.

        Exponential coordinates of the second kind are

        .. MATH ::

            \\exp(x_nX_n) \\cdots \\exp(x_1X_1) \\mapsto (x_1, \\ldots, x_n).

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: G.chart_exp2()
            Chart (G, (y_1, y_2, y_12))
        """
    def exp(self, X):
        """
        Return the group element `exp(X)`.

        INPUT:

        - ``X`` -- an element of the Lie algebra of ``self``

        EXAMPLES::

            sage: L.<X,Y,Z> = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: G.exp(X)
            exp(X)
            sage: G.exp(Y)
            exp(Y)
            sage: G.exp(X + Y)
            exp(X + Y)
        """
    def log(self, x):
        """
        Return the logarithm of the element ``x`` of ``self``.

        INPUT:

        - ``x`` -- an element of ``self``

        The logarithm is by definition the inverse of :meth:`exp`.

        If the Lie algebra of ``self`` does not admit symbolic coefficients,
        the logarithm is not defined for abstract, i.e. symbolic, points.

        EXAMPLES:

        The logarithm is the inverse of the exponential::

            sage: L.<X,Y,Z> = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: G.log(G.exp(X)) == X
            True
            sage: G.log(G.exp(X)*G.exp(Y))
            X + Y + 1/2*Z

        The logarithm is not defined for abstract (symbolic) points::

            sage: g = G.point([var('a'), 1, 2]); g
            exp(a*X + Y + 2*Z)
            sage: G.log(g)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert a to a rational
        """
    def one(self):
        """
        Return the identity element of ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, 2, step=4)
            sage: G = L.lie_group()
            sage: G.one()
            exp(0)
        """
    def left_translation(self, g):
        """
        Return the left translation by ``g`` as an automorphism of ``self``.

        The left translation by `g` on a Lie group `G` is the map

        .. MATH::

            G \\to G, \\qquad
            h \\mapsto gh.

        INPUT:

        - ``g`` -- an element of ``self``

        EXAMPLES:

        A left translation in the Heisenberg group::

            sage: H = lie_algebras.Heisenberg(QQ, 1)
            sage: p,q,z = H.basis()
            sage: G = H.lie_group()
            sage: g = G.exp(p)
            sage: L_g = G.left_translation(g); L_g
            Diffeomorphism of the Lie group G of Heisenberg algebra of rank 1 over Rational Field
            sage: L_g.display(chart1=G.chart_exp1(), chart2=G.chart_exp1())
            G → G
                (x_0, x_1, x_2) ↦ (x_0 + 1, x_1, 1/2*x_1 + x_2)

        Left translation by a generic element::

            sage: h = G.point([var('a'), var('b'), var('c')])
            sage: L_h = G.left_translation(h)
            sage: L_h.display(chart1=G.chart_exp1(), chart2=G.chart_exp1())
            G → G
               (x_0, x_1, x_2) ↦ (a + x_0, b + x_1, -1/2*b*x_0 + 1/2*a*x_1 + c + x_2)
        """
    def left_invariant_frame(self, **kwds):
        """
        Return the frame of left-invariant vector fields of ``self``.

        The labeling of the frame and the dual frame can be customized using
        keyword parameters as described in
        :meth:`sage.manifolds.differentiable.manifold.DifferentiableManifold.vector_frame`.

        EXAMPLES:

        The default left-invariant frame::

            sage: L = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: livf = G.left_invariant_frame(); livf
            Vector frame (G, (X_1,X_2,X_12))
            sage: coord_frame = G.chart_exp1().frame()
            sage: livf[0].display(coord_frame)
            X_1 = ∂/∂x_1 - 1/2*x_2 ∂/∂x_12
            sage: livf[1].display(coord_frame)
            X_2 = ∂/∂x_2 + 1/2*x_1 ∂/∂x_12
            sage: livf[2].display(coord_frame)
            X_12 = ∂/∂x_12

        Examples of custom labeling for the frame::

            sage: G.left_invariant_frame(symbol='Y')
            Vector frame (G, (Y_1,Y_2,Y_12))
            sage: G.left_invariant_frame(symbol='Z', indices=None)
            Vector frame (G, (Z_0,Z_1,Z_2))
            sage: G.left_invariant_frame(symbol='W', indices=('a','b','c'))
            Vector frame (G, (W_a,W_b,W_c))
        """
    livf = left_invariant_frame
    def left_invariant_extension(self, X, name=None):
        """
        Return the left-invariant vector field that has the value ``X``
        at the identity.

        INPUT:

        - ``X`` -- an element of the Lie algebra of ``self``
        - ``name`` -- (optional) a string to use as a name for the vector field;
          if nothing is given, the name of the vector ``X`` is used

        EXAMPLES:

        A left-invariant extension in the Heisenberg group::

            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: p, q, z = L.basis()
            sage: H = L.lie_group('H')
            sage: X = H.left_invariant_extension(p); X
            Vector field p1 on the Lie group H of Heisenberg algebra of rank 1 over Rational Field
            sage: X.display(H.chart_exp1().frame())
            p1 = ∂/∂x_0 - 1/2*x_1 ∂/∂x_2

        Default vs. custom naming for the invariant vector field::

            sage: Y = H.left_invariant_extension(p + q); Y
            Vector field p1 + q1 on the Lie group H of Heisenberg algebra of rank 1 over Rational Field
            sage: Z = H.left_invariant_extension(p + q, 'Z'); Z
            Vector field Z on the Lie group H of Heisenberg algebra of rank 1 over Rational Field
        """
    def right_translation(self, g):
        """
        Return the right translation by ``g`` as an automorphism of ``self``.

        The right translation by `g` on a Lie group `G` is the map

        .. MATH::

            G \\to G, \\qquad
            h\\mapsto hg.

        INPUT:

        - ``g`` -- an element of ``self``

        EXAMPLES:

        A right translation in the Heisenberg group::

            sage: H = lie_algebras.Heisenberg(QQ, 1)
            sage: p,q,z = H.basis()
            sage: G = H.lie_group()
            sage: g = G.exp(p)
            sage: R_g = G.right_translation(g); R_g
            Diffeomorphism of the Lie group G of Heisenberg algebra of rank 1 over Rational Field
            sage: R_g.display(chart1=G.chart_exp1(), chart2=G.chart_exp1())
            G → G
               (x_0, x_1, x_2) ↦ (x_0 + 1, x_1, -1/2*x_1 + x_2)

        Right translation by a generic element::

            sage: h = G.point([var('a'), var('b'), var('c')])
            sage: R_h = G.right_translation(h)
            sage: R_h.display(chart1=G.chart_exp1(), chart2=G.chart_exp1())
            G → G
               (x_0, x_1, x_2) ↦ (a + x_0, b + x_1, 1/2*b*x_0 - 1/2*a*x_1 + c + x_2)
        """
    def right_invariant_frame(self, **kwds):
        """
        Return the frame of right-invariant vector fields of ``self``.

        The labeling of the frame and the dual frame can be customized using
        keyword parameters as described in
        :meth:`sage.manifolds.differentiable.manifold.DifferentiableManifold.vector_frame`.

        EXAMPLES:

        The default right-invariant frame::

            sage: L = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: rivf = G.right_invariant_frame(); rivf
            Vector frame (G, (XR_1,XR_2,XR_12))
            sage: coord_frame = G.chart_exp1().frame()
            sage: rivf[0].display(coord_frame)
            XR_1 = ∂/∂x_1 + 1/2*x_2 ∂/∂x_12
            sage: rivf[1].display(coord_frame)
            XR_2 = ∂/∂x_2 - 1/2*x_1 ∂/∂x_12
            sage: rivf[2].display(coord_frame)
            XR_12 = ∂/∂x_12

        Examples of custom labeling for the frame::

            sage: G.right_invariant_frame(symbol='Y')
            Vector frame (G, (Y_1,Y_2,Y_12))
            sage: G.right_invariant_frame(symbol='Z', indices=None)
            Vector frame (G, (Z_0,Z_1,Z_2))
            sage: G.right_invariant_frame(symbol='W', indices=('a','b','c'))
            Vector frame (G, (W_a,W_b,W_c))
        """
    rivf = right_invariant_frame
    def right_invariant_extension(self, X, name=None):
        """
        Return the right-invariant vector field that has the value ``X``
        at the identity.

        INPUT:

        - ``X`` -- an element of the Lie algebra of ``self``
        - ``name`` -- (optional) a string to use as a name for the vector field;
          if nothing is given, the name of the vector ``X`` is used

        EXAMPLES:

        A right-invariant extension in the Heisenberg group::

            sage: L = lie_algebras.Heisenberg(QQ, 1)
            sage: p, q, z = L.basis()
            sage: H = L.lie_group('H')
            sage: X = H.right_invariant_extension(p); X
            Vector field p1 on the Lie group H of Heisenberg algebra of rank 1 over Rational Field
            sage: X.display(H.chart_exp1().frame())
            p1 = ∂/∂x_0 + 1/2*x_1 ∂/∂x_2

        Default vs. custom naming for the invariant vector field::

            sage: Y = H.right_invariant_extension(p + q); Y
            Vector field p1 + q1 on the Lie group H of Heisenberg algebra of rank 1 over Rational Field
            sage: Z = H.right_invariant_extension(p + q, 'Z'); Z
            Vector field Z on the Lie group H of Heisenberg algebra of rank 1 over Rational Field
        """
    def conjugation(self, g):
        """
        Return the conjugation by ``g`` as an automorphism of ``self``.

        The conjugation by `g` on a Lie group `G` is the map

        .. MATH::

            G \\to G, \\qquad
            h \\mapsto ghg^{-1}.

        INPUT:

        - ``g`` -- an element of ``self``

        EXAMPLES:

        A generic conjugation in the Heisenberg group::

            sage: H = lie_algebras.Heisenberg(QQ, 1)
            sage: p,q,z = H.basis()
            sage: G = H.lie_group()
            sage: g = G.point([var('a'), var('b'), var('c')])
            sage: C_g = G.conjugation(g); C_g
            Diffeomorphism of the Lie group G of Heisenberg algebra of rank 1 over Rational Field
            sage: C_g.display(chart1=G.chart_exp1(), chart2=G.chart_exp1())
            G → G
               (x_0, x_1, x_2) ↦ (x_0, x_1, -b*x_0 + a*x_1 + x_2)
        """
    def adjoint(self, g):
        """
        Return the adjoint map as an automorphism
        of the Lie algebra of ``self``.

        INPUT:

        - ``g`` -- an element of ``self``

        For a Lie group element `g`, the adjoint map `\\operatorname{Ad}_g` is
        the map on the Lie algebra `\\mathfrak{g}` given by the differential
        of the conjugation by `g` at the identity.

        If the Lie algebra of ``self`` does not admit symbolic coefficients,
        the adjoint is not in general defined for abstract points.

        EXAMPLES:

        An example of an adjoint map::

            sage: L = LieAlgebra(QQ, 2, step=3)
            sage: G = L.lie_group()
            sage: g = G.exp(L.basis().list()[0]); g
            exp(X_1)
            sage: Ad_g = G.adjoint(g); Ad_g
            Lie algebra endomorphism of Free Nilpotent Lie algebra on 5
            generators (X_1, X_2, X_12, X_112, X_122) over Rational Field
              Defn: X_1 |--> X_1
                    X_2 |--> X_2 + X_12 + 1/2*X_112
                    X_12 |--> X_12 + X_112
                    X_112 |--> X_112
                    X_122 |--> X_122

        Usually the adjoint map of a symbolic point is not defined::

            sage: L = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: g = G.point([var('a'), var('b'), var('c')]); g
            exp(a*X_1 + b*X_2 + c*X_12)
            sage: G.adjoint(g)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert -b to a rational

        However, if the adjoint map is independent from the symbolic terms,
        the map is still well defined::

            sage: g = G.point([0, 0, var('a')]); g
            exp(a*X_12)
            sage: G.adjoint(g)
            Lie algebra endomorphism of Free Nilpotent Lie algebra on 3 generators (X_1, X_2, X_12) over Rational Field
              Defn: X_1 |--> X_1
                    X_2 |--> X_2
                    X_12 |--> X_12
        """
    class Element(DifferentiableManifold.Element, MultiplicativeGroupElement):
        """
        A base class for an element of a Lie group.

        EXAMPLES:

        Elements of the  group are printed in the default
        exponential coordinates::

            sage: L.<X,Y,Z> = LieAlgebra(QQ, 2, step=2)
            sage: G = L.lie_group()
            sage: g = G.exp(2*X + 3*Z); g
            exp(2*X + 3*Z)
            sage: h = G.point([ var('a'), var('b'), 0]); h
            exp(a*X + b*Y)
            sage: G.set_default_chart(G.chart_exp2())
            sage: g
            exp(3*Z)exp(2*X)
            sage: h
            exp(1/2*a*b*Z)exp(b*Y)exp(a*X)

        Multiplication of two elements uses the usual product syntax::

            sage: G.exp(Y)*G.exp(X)
            exp(Y)exp(X)
            sage: G.exp(X)*G.exp(Y)
            exp(Z)exp(Y)exp(X)
            sage: G.set_default_chart(G.chart_exp1())
            sage: G.exp(X)*G.exp(Y)
            exp(X + Y + 1/2*Z)
        """
        def __init__(self, parent, **kwds) -> None:
            """
            Initialize ``self``.

            TESTS::

                sage: L.<X,Y,Z> = LieAlgebra(QQ, 2, step=2)
                sage: G = L.lie_group()
                sage: g = G.exp(X)
                sage: TestSuite(g).run()
            """
        def __invert__(self):
            """
            Return the inverse of ``self``.

            EXAMPLES::

                sage: L.<X,Y,Z> = LieAlgebra(QQ, 2, step=2)
                sage: G = L.lie_group('H')
                sage: g = G.point([var('a'), var('b'), var('c')]); g
                exp(a*X + b*Y + c*Z)
                sage: ~g
                exp((-a)*X + (-b)*Y + (-c)*Z)
                sage: g*~g
                exp(0)
            """
