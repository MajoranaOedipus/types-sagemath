from sage.manifolds.differentiable.curve import DifferentiableCurve as DifferentiableCurve
from sage.manifolds.differentiable.diff_map import DiffMap as DiffMap
from sage.manifolds.differentiable.integrated_curve import IntegratedAutoparallelCurve as IntegratedAutoparallelCurve, IntegratedCurve as IntegratedCurve, IntegratedGeodesic as IntegratedGeodesic
from sage.manifolds.manifold_homset import TopologicalManifoldHomset as TopologicalManifoldHomset

class DifferentiableManifoldHomset(TopologicalManifoldHomset):
    """
    Set of differentiable maps between two differentiable manifolds.

    Given two differentiable manifolds `M` and `N` over a topological field `K`,
    the class :class:`DifferentiableManifoldHomset` implements the set
    `\\mathrm{Hom}(M,N)` of morphisms (i.e. differentiable maps)
    `M\\rightarrow N`.

    This is a Sage *parent* class, whose *element* class is
    :class:`~sage.manifolds.differentiable.diff_map.DiffMap`.

    INPUT:

    - ``domain`` -- differentiable manifold `M` (domain of the morphisms),
      as an instance of
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
    - ``codomain`` -- differentiable manifold `N` (codomain of the morphisms),
      as an instance of
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`
    - ``name`` -- (default: ``None``) string; name given to the homset; if
      ``None``, Hom(M,N) will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote the
      homset; if ``None``, `\\mathrm{Hom}(M,N)` will be used

    EXAMPLES:

    Set of differentiable maps between a 2-dimensional differentiable manifold
    and a 3-dimensional one::

        sage: M = Manifold(2, 'M')
        sage: X.<x,y> = M.chart()
        sage: N = Manifold(3, 'N')
        sage: Y.<u,v,w> = N.chart()
        sage: H = Hom(M, N) ; H
        Set of Morphisms from 2-dimensional differentiable manifold M to
         3-dimensional differentiable manifold N in Category of smooth
         manifolds over Real Field with 53 bits of precision
        sage: type(H)
        <class 'sage.manifolds.differentiable.manifold_homset.DifferentiableManifoldHomset_with_category'>
        sage: H.category()
        Category of homsets of topological spaces
        sage: latex(H)
        \\mathrm{Hom}\\left(M,N\\right)
        sage: H.domain()
        2-dimensional differentiable manifold M
        sage: H.codomain()
        3-dimensional differentiable manifold N

    An element of ``H`` is a differentiable map from ``M`` to ``N``::

        sage: H.Element
        <class 'sage.manifolds.differentiable.diff_map.DiffMap'>
        sage: f = H.an_element() ; f
        Differentiable map from the 2-dimensional differentiable manifold M to the
         3-dimensional differentiable manifold N
        sage: f.display()
        M → N
           (x, y) ↦ (u, v, w) = (0, 0, 0)

    The test suite is passed::

        sage: TestSuite(H).run()

    When the codomain coincides with the domain, the homset is a set of
    *endomorphisms* in the category of differentiable manifolds::

        sage: E = Hom(M, M) ; E
        Set of Morphisms from 2-dimensional differentiable manifold M to
         2-dimensional differentiable manifold M in Category of smooth
         manifolds over Real Field with 53 bits of precision
        sage: E.category()
        Category of endsets of topological spaces
        sage: E.is_endomorphism_set()
        True
        sage: E is End(M)
        True

    In this case, the homset is a monoid for the law of morphism composition::

        sage: E in Monoids()
        True

    This was of course not the case for ``H = Hom(M, N)``::

        sage: H in Monoids()
        False

    The identity element of the monoid is of course the identity map of ``M``::

        sage: E.one()
        Identity map Id_M of the 2-dimensional differentiable manifold M
        sage: E.one() is M.identity_map()
        True
        sage: E.one().display()
        Id_M: M → M
           (x, y) ↦ (x, y)

    The test suite is passed by ``E``::

        sage: TestSuite(E).run()

    This test suite includes more tests than in the case of ``H``, since ``E``
    has some extra structure (monoid).
    """
    Element = DiffMap
    def __init__(self, domain, codomain, name=None, latex_name=None) -> None:
        """
        TESTS::

            sage: M = Manifold(2, 'M')
            sage: X.<x,y> = M.chart()
            sage: N = Manifold(3, 'N')
            sage: Y.<u,v,w> = N.chart()
            sage: H = Hom(M, N) ; H
            Set of Morphisms from 2-dimensional differentiable manifold M to
             3-dimensional differentiable manifold N in Category of smooth
             manifolds over Real Field with 53 bits of precision
            sage: TestSuite(H).run()

        Test for an endomorphism set::

            sage: E = Hom(M, M) ; E
            Set of Morphisms from 2-dimensional differentiable manifold M to
             2-dimensional differentiable manifold M in Category of smooth
             manifolds over Real Field with 53 bits of precision
            sage: TestSuite(E).run()
        """

class DifferentiableCurveSet(DifferentiableManifoldHomset):
    '''
    Set of differentiable curves in a differentiable manifold.

    Given an open interval `I` of `\\RR` (possibly `I = \\RR`) and
    a differentiable manifold `M` over `\\RR`, this is the set
    `\\mathrm{Hom}(I,M)` of morphisms (i.e. differentiable curves) `I \\to M`.

    INPUT:

    - ``domain`` --
      :class:`~sage.manifolds.differentiable.examples.real_line.OpenInterval`
      if an open interval `I \\subset \\RR` (domain of the morphisms),
      or :class:`~sage.manifolds.differentiable.examples.real_line.RealLine`
      if `I = \\RR`
    - ``codomain`` --
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
      differentiable manifold `M` (codomain of the morphisms)
    - ``name`` -- (default: ``None``) string; name given to the set of
      curves; if ``None``, ``Hom(I, M)`` will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
      the set of curves; if ``None``, `\\mathrm{Hom}(I,M)` will be used

    EXAMPLES:

    Set of curves `\\RR \\longrightarrow M`, where `M` is a 2-dimensional
    manifold::

        sage: M = Manifold(2, \'M\')
        sage: X.<x,y> = M.chart()
        sage: R.<t> = manifolds.RealLine() ; R
        Real number line ℝ
        sage: H = Hom(R, M) ; H
        Set of Morphisms from Real number line ℝ to 2-dimensional
         differentiable manifold M in Category of smooth manifolds over Real
         Field with 53 bits of precision
        sage: H.category()
        Category of homsets of topological spaces
        sage: latex(H)
        \\mathrm{Hom}\\left(\\Bold{R},M\\right)
        sage: H.domain()
        Real number line ℝ
        sage: H.codomain()
        2-dimensional differentiable manifold M

    An element of ``H`` is a curve in ``M``::

        sage: c = H.an_element(); c
        Curve in the 2-dimensional differentiable manifold M
        sage: c.display()
        ℝ → M
           t ↦ (x, y) = (1/(t^2 + 1) - 1/2, 0)

    The test suite is passed::

        sage: TestSuite(H).run()

    The set of curves `(0,1) \\longrightarrow U`, where `U` is an open
    subset of `M`::

        sage: I = R.open_interval(0, 1) ; I
        Real interval (0, 1)
        sage: U = M.open_subset(\'U\', coord_def={X: x^2+y^2<1}) ; U
        Open subset U of the 2-dimensional differentiable manifold M
        sage: H = Hom(I, U) ; H
        Set of Morphisms from Real interval (0, 1) to Open subset U of the
         2-dimensional differentiable manifold M in Join of Category of
         subobjects of sets and Category of smooth manifolds over Real Field
         with 53 bits of precision

    An element of ``H`` is a curve in ``U``::

        sage: c = H.an_element() ; c
        Curve in the Open subset U of the 2-dimensional differentiable
         manifold M
        sage: c.display()
        (0, 1) → U
           t ↦ (x, y) = (1/(t^2 + 1) - 1/2, 0)

    The set of curves `\\RR \\longrightarrow \\RR` is a set of (manifold)
    endomorphisms::

        sage: E = Hom(R, R) ; E
        Set of Morphisms from Real number line ℝ to Real number line ℝ in
         Category of smooth connected manifolds over Real Field with 53 bits of
         precision
        sage: E.category()
        Category of endsets of topological spaces
        sage: E.is_endomorphism_set()
        True
        sage: E is End(R)
        True

    It is a monoid for the law of morphism composition::

        sage: E in Monoids()
        True

    The identity element of the monoid is the identity map of `\\RR`::

        sage: E.one()
        Identity map Id_ℝ of the Real number line ℝ
        sage: E.one() is R.identity_map()
        True
        sage: E.one().display()
        Id_ℝ: ℝ → ℝ
           t ↦ t

    A "typical" element of the monoid::

        sage: E.an_element().display()
        ℝ → ℝ
           t ↦ 1/(t^2 + 1) - 1/2

    The test suite is passed by ``E``::

        sage: TestSuite(E).run()

    Similarly, the set of curves `I \\longrightarrow I` is a monoid, whose
    elements are (manifold) endomorphisms::

        sage: EI = Hom(I, I) ; EI
        Set of Morphisms from Real interval (0, 1) to Real interval (0, 1) in
         Join of Category of subobjects of sets and Category of smooth manifolds
         over Real Field with 53 bits of precision and Category of connected
         manifolds over Real Field with 53 bits of precision
        sage: EI.category()
        Category of endsets of subobjects of sets and topological spaces
        sage: EI is End(I)
        True
        sage: EI in Monoids()
        True

    The identity element and a "typical" element of this monoid::

        sage: EI.one()
        Identity map Id_(0, 1) of the Real interval (0, 1)
        sage: EI.one().display()
        Id_(0, 1): (0, 1) → (0, 1)
           t ↦ t
        sage: EI.an_element().display()
        (0, 1) → (0, 1)
           t ↦ 1/2/(t^2 + 1) + 1/4

    The test suite is passed by ``EI``::

        sage: TestSuite(EI).run()
    '''
    Element = DifferentiableCurve
    def __init__(self, domain, codomain, name=None, latex_name=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: M = Manifold(3, 'M')
            sage: X.<x,y,z> = M.chart()
            sage: R.<t> = manifolds.RealLine()
            sage: H = Hom(R, M); H
            Set of Morphisms from Real number line ℝ to 3-dimensional
             differentiable manifold M in Category of smooth manifolds over
             Real Field with 53 bits of precision
            sage: TestSuite(H).run()
            sage: Hom(R, M) is Hom(R, M)
            True
            sage: H = Hom(R, R); H
            Set of Morphisms from Real number line ℝ to Real number line ℝ in
             Category of smooth connected manifolds over Real Field with 53 bits
             of precision
            sage: TestSuite(H).run()
            sage: I = R.open_interval(-1, 2)
            sage: H = Hom(I, M); H
            Set of Morphisms from Real interval (-1, 2) to 3-dimensional
             differentiable manifold M in Category of smooth manifolds over Real
             Field with 53 bits of precision
            sage: TestSuite(H).run()
            sage: H = Hom(I, I); H
            Set of Morphisms from Real interval (-1, 2) to Real interval (-1, 2)
             in Join of Category of subobjects of sets and Category of smooth
             manifolds over Real Field with 53 bits of precision and Category of
             connected manifolds over Real Field with 53 bits of precision
            sage: TestSuite(H).run()
        """

class IntegratedCurveSet(DifferentiableCurveSet):
    '''
    Set of integrated curves in a differentiable manifold.

    INPUT:

    - ``domain`` --
      :class:`~sage.manifolds.differentiable.examples.real_line.OpenInterval`
      open interval `I \\subset \\RR` with finite boundaries (domain of
      the morphisms)
    - ``codomain`` --
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
      differentiable manifold `M` (codomain of the morphisms)
    - ``name`` -- (default: ``None``) string; name given to the set of
      integrated curves; if ``None``, ``Hom_integrated(I, M)`` will be
      used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to
      denote the set of integrated curves; if ``None``,
      `\\mathrm{Hom_{integrated}}(I,M)` will be used

    EXAMPLES:

    This parent class needs to be imported::

        sage: from sage.manifolds.differentiable.manifold_homset import IntegratedCurveSet

    Integrated curves are only allowed to be defined on an interval with
    finite bounds.
    This forbids to define an instance of this parent class whose domain
    has infinite bounds::

        sage: M = Manifold(2, \'M\')
        sage: X.<x,y> = M.chart()
        sage: R.<t> = manifolds.RealLine()
        sage: H = IntegratedCurveSet(R, M)
        Traceback (most recent call last):
        ...
        ValueError: both boundaries of the interval defining the domain
         of a Homset of integrated curves need to be finite

    An instance whose domain is an interval with finite bounds allows to
    build an integrated curve defined on the interval::

        sage: I = R.open_interval(-1, 2)
        sage: H = IntegratedCurveSet(I, M) ; H
        Set of Morphisms from Real interval (-1, 2) to 2-dimensional
         differentiable manifold M in Category of homsets of topological spaces
         which actually are integrated curves
        sage: eqns_rhs = [1,1]
        sage: vels = X.symbolic_velocities()
        sage: t = var(\'t\')
        sage: p = M.point((3,4))
        sage: Tp = M.tangent_space(p)
        sage: v = Tp((1,2))
        sage: c = H(eqns_rhs, vels, t, v, name=\'c\') ; c
        Integrated curve c in the 2-dimensional differentiable
         manifold M

    A "typical" element of ``H`` is a curve in ``M``::

        sage: d = H.an_element(); d
        Integrated curve in the 2-dimensional differentiable manifold M
        sage: sys = d.system(verbose=True)
        Curve in the 2-dimensional differentiable manifold M integrated
         over the Real interval (-1, 2) as a solution to the following
         system, written with respect to Chart (M, (x, y)):
        <BLANKLINE>
        Initial point: Point on the 2-dimensional differentiable
         manifold M with coordinates [0, 0] with respect to Chart (M, (x, y))
        Initial tangent vector: Tangent vector at Point on the
         2-dimensional differentiable manifold M with components
         [1/4, 0] with respect to Chart (M, (x, y))
        <BLANKLINE>
        d(x)/dt = Dx
        d(y)/dt = Dy
        d(Dx)/dt = -1/4*sin(t + 1)
        d(Dy)/dt = 0
        <BLANKLINE>

    The test suite is passed::

        sage: TestSuite(H).run()

    More generally, an instance of this class may be defined with
    abstract bounds `(a,b)`::

        sage: [a,b] = var(\'a b\')
        sage: J = R.open_interval(a, b)
        sage: H = IntegratedCurveSet(J, M) ; H
        Set of Morphisms from Real interval (a, b) to 2-dimensional
         differentiable manifold M in Category of homsets of topological spaces
         which actually are integrated curves

    A "typical" element of ``H`` is a curve in ``M``::

        sage: f = H.an_element(); f
        Integrated curve in the 2-dimensional differentiable manifold M
        sage: sys = f.system(verbose=True)
        Curve in the 2-dimensional differentiable manifold M integrated
         over the Real interval (a, b) as a solution to the following
         system, written with respect to Chart (M, (x, y)):
        <BLANKLINE>
        Initial point: Point on the 2-dimensional differentiable
         manifold M with coordinates [0, 0] with respect to Chart (M, (x, y))
        Initial tangent vector: Tangent vector at Point on the
         2-dimensional differentiable manifold M with components
         [1/4, 0] with respect to Chart (M, (x, y))
        <BLANKLINE>
        d(x)/dt = Dx
        d(y)/dt = Dy
        d(Dx)/dt = -1/4*sin(-a + t)
        d(Dy)/dt = 0
        <BLANKLINE>

    Yet, even in the case of abstract bounds, considering any of them to
    be infinite is still prohibited since no numerical integration could
    be performed::

        sage: f.solve(parameters_values={a:-1, b:+oo})
        Traceback (most recent call last):
        ...
        ValueError: both boundaries of the interval need to be finite

    The set of integrated curves `J \\longrightarrow J` is a set of
    numerical (manifold) endomorphisms::

        sage: H = IntegratedCurveSet(J, J); H
        Set of Morphisms from Real interval (a, b) to Real interval
         (a, b) in Category of endsets of subobjects of sets and
         topological spaces which actually are integrated curves
        sage: H.category()
        Category of endsets of subobjects of sets and topological spaces

    It is a monoid for the law of morphism composition::

        sage: H in Monoids()
        True

    Although it is a monoid, no identity map is implemented via the
    ``one`` method of this class or any of its subclasses.
    This is justified by the lack of relevance of the identity map
    within the framework of this parent class and its subclasses, whose
    purpose is mainly devoted to numerical issues (therefore, the user
    is left free to set a numerical version of the identity if needed)::

        sage: H.one()
        Traceback (most recent call last):
        ...
        ValueError: the identity is not implemented for integrated
         curves and associated subclasses

    A "typical" element of the monoid::

        sage: g = H.an_element() ; g
        Integrated curve in the Real interval (a, b)
        sage: sys = g.system(verbose=True)
        Curve in the Real interval (a, b) integrated over the Real
         interval (a, b) as a solution to the following system, written
         with respect to Chart ((a, b), (t,)):
        <BLANKLINE>
        Initial point: Point on the Real number line ℝ with coordinates
         [0] with respect to Chart ((a, b), (t,))
        Initial tangent vector: Tangent vector at Point on the Real
         number line ℝ with components [1/4] with respect to
         Chart ((a, b), (t,))
        <BLANKLINE>
        d(t)/ds = Dt
        d(Dt)/ds = -1/4*sin(-a + s)
        <BLANKLINE>

    The test suite is passed, tests ``_test_one`` and ``_test_prod`` being
    skipped for reasons mentioned above::

        sage: TestSuite(H).run(skip=["_test_one", "_test_prod"])
    '''
    Element = IntegratedCurve
    def __init__(self, domain, codomain, name=None, latex_name=None) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: from sage.manifolds.differentiable.manifold_homset import IntegratedCurveSet
            sage: M = Manifold(3, \'M\')
            sage: X.<x,y,z> = M.chart()
            sage: R.<t> = manifolds.RealLine()
            sage: H = IntegratedCurveSet(R, M)
            Traceback (most recent call last):
            ...
            ValueError: both boundaries of the interval defining the
             domain of a Homset of integrated curves need to be finite
            sage: I = R.open_interval(-1, 2)
            sage: H = IntegratedCurveSet(I, M) ; H
            Set of Morphisms from Real interval (-1, 2) to 3-dimensional
             differentiable manifold M in Category of homsets of topological
             spaces which actually are integrated curves
            sage: TestSuite(H).run()
            sage: H = IntegratedCurveSet(I, I); H
            Set of Morphisms from Real interval (-1, 2) to Real interval
             (-1, 2) in Category of endsets of subobjects of sets and
             topological spaces which actually are integrated curves
            sage: TestSuite(H).run(skip=["_test_one", "_test_prod"])
        '''
    def one(self) -> None:
        """
        Raise an error refusing to provide the identity element.
        This overrides the ``one`` method of class
        :class:`~sage.manifolds.manifold_homset.TopologicalManifoldHomset`,
        which would actually raise an error as well, due to lack of option
        ``is_identity`` in ``element_constructor`` method of ``self``.

        TESTS::

            sage: from sage.manifolds.differentiable.manifold_homset import IntegratedCurveSet
            sage: M = Manifold(3, 'M')
            sage: X.<x,y,z> = M.chart()
            sage: R.<t> = manifolds.RealLine()
            sage: I = R.open_interval(-1, 2)
            sage: H = IntegratedCurveSet(I, M)
            sage: H.one()
            Traceback (most recent call last):
            ...
            TypeError: Set of Morphisms from Real interval (-1, 2) to
             3-dimensional differentiable manifold M in Category of homsets of
             topological spaces which actually are integrated curves is not a
             monoid
            sage: H = IntegratedCurveSet(I, I)
            sage: H.one()
            Traceback (most recent call last):
            ...
            ValueError: the identity is not implemented for integrated
             curves and associated subclasses
        """

class IntegratedAutoparallelCurveSet(IntegratedCurveSet):
    '''
    Set of integrated autoparallel curves in a differentiable manifold.

    INPUT:

    - ``domain`` --
      :class:`~sage.manifolds.differentiable.examples.real_line.OpenInterval`
      open interval `I \\subset \\RR` with finite boundaries (domain of
      the morphisms)
    - ``codomain`` --
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
      differentiable manifold `M` (codomain of the morphisms)
    - ``name`` -- (default: ``None``) string; name given to the set of
      integrated autoparallel curves; if ``None``,
      ``Hom_autoparallel(I, M)`` will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
      the set of integrated autoparallel curves; if ``None``,
      `\\mathrm{Hom_{autoparallel}}(I,M)` will be used

    EXAMPLES:

    This parent class needs to be imported::

        sage: from sage.manifolds.differentiable.manifold_homset import IntegratedAutoparallelCurveSet

    Integrated autoparallel curves are only allowed to be defined on an
    interval with finite bounds.
    This forbids to define an instance of this parent class whose domain
    has infinite bounds::

        sage: M = Manifold(2, \'M\')
        sage: X.<x,y> = M.chart()
        sage: R.<t> = manifolds.RealLine()
        sage: H = IntegratedAutoparallelCurveSet(R, M)
        Traceback (most recent call last):
        ...
        ValueError: both boundaries of the interval defining the domain
         of a Homset of integrated autoparallel curves need to be finite

    An instance whose domain is an interval with finite bounds allows to
    build a curve that is autoparallel with respect to a connection
    defined on the codomain::

        sage: I = R.open_interval(-1, 2)
        sage: H = IntegratedAutoparallelCurveSet(I, M) ; H
        Set of Morphisms from Real interval (-1, 2) to 2-dimensional
         differentiable manifold M in Category of homsets of topological spaces
         which actually are integrated autoparallel curves with respect to a
         certain affine connection
        sage: nab = M.affine_connection(\'nabla\')
        sage: nab[0,1,0], nab[0,0,1] = 1,2
        sage: nab.torsion()[:]
        [[[0, -1], [1, 0]], [[0, 0], [0, 0]]]
        sage: t = var(\'t\')
        sage: p = M.point((3,4))
        sage: Tp = M.tangent_space(p)
        sage: v = Tp((1,2))
        sage: c = H(nab, t, v, name=\'c\') ; c
        Integrated autoparallel curve c in the 2-dimensional
         differentiable manifold M

    A "typical" element of ``H`` is an autoparallel curve in ``M``::

        sage: d = H.an_element(); d
        Integrated autoparallel curve in the 2-dimensional
         differentiable manifold M
        sage: sys = d.system(verbose=True)
        Autoparallel curve in the 2-dimensional differentiable manifold
         M equipped with Affine connection nab on the 2-dimensional
         differentiable manifold M, and integrated over the Real
         interval (-1, 2) as a solution to the following equations,
         written with respect to Chart (M, (x, y)):
        <BLANKLINE>
        Initial point: Point on the 2-dimensional differentiable
         manifold M with coordinates [0, -1/2] with respect to
         Chart (M, (x, y))
        Initial tangent vector: Tangent vector at Point on the
         2-dimensional differentiable manifold M with components
         [-1/6/(e^(-1) - 1), 1/3] with respect to Chart (M, (x, y))
        <BLANKLINE>
        d(x)/dt = Dx
        d(y)/dt = Dy
        d(Dx)/dt = -Dx*Dy
        d(Dy)/dt = 0
        <BLANKLINE>

    The test suite is passed::

        sage: TestSuite(H).run()

    For any open interval `J` with finite bounds `(a,b)`, all curves are
    autoparallel with respect to any connection.
    Therefore, the set of autoparallel curves `J \\longrightarrow J` is a
    set of numerical (manifold) endomorphisms that is a monoid for the
    law of morphism composition::

        sage: [a,b] = var(\'a b\')
        sage: J = R.open_interval(a, b)
        sage: H = IntegratedAutoparallelCurveSet(J, J); H
        Set of Morphisms from Real interval (a, b) to Real interval
         (a, b) in Category of endsets of subobjects of sets and
         topological spaces which actually are integrated autoparallel
         curves with respect to a certain affine connection
        sage: H.category()
        Category of endsets of subobjects of sets and topological spaces
        sage: H in Monoids()
        True

    Although it is a monoid, no identity map is implemented via the
    ``one`` method of this class or its subclass devoted to geodesics.
    This is justified by the lack of relevance of the identity map
    within the framework of this parent class and its subclass, whose
    purpose is mainly devoted to numerical issues (therefore, the user
    is left free to set a numerical version of the identity if needed)::

        sage: H.one()
        Traceback (most recent call last):
        ...
        ValueError: the identity is not implemented for integrated
         curves and associated subclasses

    A "typical" element of the monoid::

        sage: g = H.an_element() ; g
        Integrated autoparallel curve in the Real interval (a, b)
        sage: sys = g.system(verbose=True)
        Autoparallel curve in the Real interval (a, b) equipped with
         Affine connection nab on the Real interval (a, b), and
         integrated over the Real interval (a, b) as a solution to the
         following equations, written with respect to Chart ((a, b), (t,)):
        <BLANKLINE>
        Initial point: Point on the Real number line ℝ with coordinates
         [0] with respect to Chart ((a, b), (t,))
        Initial tangent vector: Tangent vector at Point on the Real
         number line ℝ with components
         [-(e^(1/2) - 1)/(a - b)] with respect to
         Chart ((a, b), (t,))
        <BLANKLINE>
        d(t)/ds = Dt
        d(Dt)/ds = -Dt^2
        <BLANKLINE>

    The test suite is passed, tests ``_test_one`` and ``_test_prod`` being
    skipped for reasons mentioned above::

        sage: TestSuite(H).run(skip=["_test_one", "_test_prod"])
    '''
    Element = IntegratedAutoparallelCurve
    def __init__(self, domain, codomain, name=None, latex_name=None) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: from sage.manifolds.differentiable.manifold_homset import IntegratedAutoparallelCurveSet
            sage: M = Manifold(3, \'M\')
            sage: X.<x,y,z> = M.chart()
            sage: R.<t> = manifolds.RealLine()
            sage: H = IntegratedAutoparallelCurveSet(R, M)
            Traceback (most recent call last):
            ...
            ValueError: both boundaries of the interval defining the
             domain of a Homset of integrated autoparallel curves need
             to be finite
            sage: I = R.open_interval(-1, 2)
            sage: H = IntegratedAutoparallelCurveSet(I, M) ; H
            Set of Morphisms from Real interval (-1, 2) to 3-dimensional
             differentiable manifold M in Category of homsets of topological
             spaces which actually are integrated autoparallel curves with
             respect to a certain affine connection
            sage: TestSuite(H).run()
            sage: H = IntegratedAutoparallelCurveSet(I, I); H
            Set of Morphisms from Real interval (-1, 2) to Real interval
             (-1, 2) in Category of endsets of subobjects of sets and
             topological spaces which actually are integrated
             autoparallel curves with respect to a certain affine connection
            sage: TestSuite(H).run(skip=["_test_one", "_test_prod"])
        '''

class IntegratedGeodesicSet(IntegratedAutoparallelCurveSet):
    '''
    Set of integrated geodesic in a differentiable manifold.

    INPUT:

    - ``domain`` --
      :class:`~sage.manifolds.differentiable.examples.real_line.OpenInterval`
      open interval `I \\subset \\RR` with finite boundaries (domain of
      the morphisms)
    - ``codomain`` --
      :class:`~sage.manifolds.differentiable.manifold.DifferentiableManifold`;
      differentiable manifold `M` (codomain of the morphisms)
    - ``name`` -- (default: ``None``) string; name given to the set of
      integrated geodesics; if ``None``, ``Hom_geodesic(I, M)`` will be used
    - ``latex_name`` -- (default: ``None``) string; LaTeX symbol to denote
      the set of integrated geodesics; if ``None``,
      `\\mathrm{Hom_{geodesic}}(I,M)` will be used

    EXAMPLES:

    This parent class needs to be imported::

        sage: from sage.manifolds.differentiable.manifold_homset import IntegratedGeodesicSet

    Integrated geodesics are only allowed to be defined on an interval
    with finite bounds.
    This forbids to define an instance of this parent class whose domain
    has infinite bounds::

        sage: M = Manifold(2, \'M\')
        sage: X.<x,y> = M.chart()
        sage: R.<t> = manifolds.RealLine()
        sage: H = IntegratedGeodesicSet(R, M)
        Traceback (most recent call last):
        ...
        ValueError: both boundaries of the interval defining the domain
         of a Homset of integrated geodesics need to be finite

    An instance whose domain is an interval with finite bounds allows to
    build a geodesic with respect to a metric defined on the codomain::

        sage: I = R.open_interval(-1, 2)
        sage: H = IntegratedGeodesicSet(I, M) ; H
        Set of Morphisms from Real interval (-1, 2) to 2-dimensional
         differentiable manifold M in Category of homsets of topological spaces
         which actually are integrated geodesics with respect to a certain
         metric
        sage: g = M.metric(\'g\')
        sage: g[0,0], g[1,1], g[0,1] = 1, 1, 2
        sage: t = var(\'t\')
        sage: p = M.point((3,4))
        sage: Tp = M.tangent_space(p)
        sage: v = Tp((1,2))
        sage: c = H(g, t, v, name=\'c\') ; c
        Integrated geodesic c in the 2-dimensional differentiable
         manifold M

    A "typical" element of ``H`` is a geodesic in ``M``::

        sage: d = H.an_element(); d
        Integrated geodesic in the 2-dimensional differentiable
         manifold M
        sage: sys = d.system(verbose=True)
        Geodesic in the 2-dimensional differentiable manifold M equipped
         with Riemannian metric g on the 2-dimensional differentiable
         manifold M, and integrated over the Real interval (-1, 2) as a
         solution to the following geodesic equations, written
         with respect to Chart (M, (x, y)):
        <BLANKLINE>
        Initial point: Point on the 2-dimensional differentiable
         manifold M with coordinates [0, 0] with respect to
         Chart (M, (x, y))
        Initial tangent vector: Tangent vector at Point on the
         2-dimensional differentiable manifold M with components
         [1/3*e^(1/2) - 1/3, 0] with respect to Chart (M, (x, y))
        <BLANKLINE>
        d(x)/dt = Dx
        d(y)/dt = Dy
        d(Dx)/dt = -Dx^2
        d(Dy)/dt = 0

    The test suite is passed::

        sage: TestSuite(H).run()

    For any open interval `J` with finite bounds `(a,b)`, all curves are
    geodesics with respect to any metric.
    Therefore, the set of geodesics `J \\longrightarrow J` is a set of
    numerical (manifold) endomorphisms that is a monoid for the law of
    morphism composition::

        sage: [a,b] = var(\'a b\')
        sage: J = R.open_interval(a, b)
        sage: H = IntegratedGeodesicSet(J, J); H
        Set of Morphisms from Real interval (a, b) to Real interval
         (a, b) in Category of endsets of subobjects of sets and
         topological spaces which actually are integrated geodesics
         with respect to a certain metric
        sage: H.category()
        Category of endsets of subobjects of sets and topological spaces
        sage: H in Monoids()
        True

    Although it is a monoid, no identity map is implemented via the
    ``one`` method of this class.
    This is justified by the lack of relevance of the identity map
    within the framework of this parent class, whose purpose is mainly
    devoted to numerical issues (therefore, the user is left free to set
    a numerical version of the identity if needed)::

        sage: H.one()
        Traceback (most recent call last):
        ...
        ValueError: the identity is not implemented for integrated
         curves and associated subclasses

    A "typical" element of the monoid::

        sage: g = H.an_element() ; g
        Integrated geodesic in the Real interval (a, b)
        sage: sys = g.system(verbose=True)
        Geodesic in the Real interval (a, b) equipped with Riemannian
         metric g on the Real interval (a, b), and integrated over the
         Real interval (a, b) as a solution to the following geodesic
         equations, written with respect to Chart ((a, b), (t,)):
        <BLANKLINE>
        Initial point: Point on the Real number line ℝ with coordinates
         [0] with respect to Chart ((a, b), (t,))
        Initial tangent vector: Tangent vector at Point on the Real
         number line ℝ with components [-(e^(1/2) - 1)/(a - b)]
         with respect to Chart ((a, b), (t,))
        <BLANKLINE>
        d(t)/ds = Dt
        d(Dt)/ds = -Dt^2
        <BLANKLINE>

    The test suite is passed, tests ``_test_one`` and ``_test_prod`` being
    skipped for reasons mentioned above::

        sage: TestSuite(H).run(skip=["_test_one", "_test_prod"])
    '''
    Element = IntegratedGeodesic
    def __init__(self, domain, codomain, name=None, latex_name=None) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: from sage.manifolds.differentiable.manifold_homset import IntegratedGeodesicSet
            sage: M = Manifold(3, \'M\')
            sage: X.<x,y,z> = M.chart()
            sage: R.<t> = manifolds.RealLine()
            sage: H = IntegratedGeodesicSet(R, M)
            Traceback (most recent call last):
            ...
            ValueError: both boundaries of the interval defining the
             domain of a Homset of integrated geodesics need to be
             finite
            sage: I = R.open_interval(-1, 2)
            sage: H = IntegratedGeodesicSet(I, M) ; H
            Set of Morphisms from Real interval (-1, 2) to 3-dimensional
             differentiable manifold M in Category of homsets of topological
             spaces which actually are integrated geodesics with respect to a
             certain metric
            sage: TestSuite(H).run()
            sage: H = IntegratedGeodesicSet(I, I); H
            Set of Morphisms from Real interval (-1, 2) to Real interval
             (-1, 2) in Category of endsets of subobjects of sets and
             topological spaces which actually are integrated geodesics
             with respect to a certain metric
            sage: TestSuite(H).run(skip=["_test_one", "_test_prod"])
        '''
