from _typeshed import Incomplete
from sage.arith.functions import lcm as lcm
from sage.arith.misc import GCD as GCD, algebraic_dependency as algebraic_dependency
from sage.ext.fast_callable import fast_callable as fast_callable
from sage.graphs.graph import Graph as Graph
from sage.groups.matrix_gps.finitely_generated import MatrixGroup as MatrixGroup
from sage.groups.perm_gps.permgroup_named import SymmetricGroup as SymmetricGroup
from sage.matrix.constructor import Matrix as Matrix
from sage.matrix.special import block_matrix as block_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.functional import numerical_approx as numerical_approx
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_integer import IntegerLattice as IntegerLattice
from sage.numerical.gauss_legendre import integrate_vector as integrate_vector, integrate_vector_N as integrate_vector_N
from sage.rings.complex_mpfr import CDF as CDF, ComplexField as ComplexField
from sage.rings.function_field.constructor import FunctionField as FunctionField
from sage.rings.function_field.divisor import FunctionFieldDivisor as FunctionFieldDivisor
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField
from sage.schemes.curves.constructor import Curve as Curve

def voronoi_ghost(cpoints, n: int = 6, CC=...):
    """
    Convert a set of complex points to a list of real tuples `(x,y)`, and
    appends n points in a big circle around them.

    The effect is that, with n >= 3, a Voronoi decomposition will have only
    finite cells around the original points. Furthermore, because the extra
    points are placed on a circle centered on the average of the given points,
    with a radius 3/2 times the largest distance between the center and the
    given points, these finite cells form a simply connected region.

    INPUT:

    - ``cpoints`` -- list of complex numbers

    OUTPUT:

    A list of real tuples `(x,y)` consisting of the original points and a set of
    points which surround them.

    EXAMPLES::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import voronoi_ghost
        sage: L = [1 + 1*I, 1 - 1*I, -1 + 1*I, -1 - 1*I]
        sage: voronoi_ghost(L)  # abs tol 1e-6
        [(1.0, 1.0),
         (1.0, -1.0),
         (-1.0, 1.0),
         (-1.0, -1.0),
         (2.121320343559643, 0.0),
         (1.0606601717798216, 1.8371173070873836),
         (-1.060660171779821, 1.8371173070873839),
         (-2.121320343559643, 2.59786816870648e-16),
         (-1.0606601717798223, -1.8371173070873832),
         (1.06066017177982, -1.8371173070873845)]
    """
def bisect(L, t):
    """
    Find position in a sorted list using bisection.

    Given a list `L = [(t_0,...),(t_1,...),...(t_n,...)]` with increasing `t_i`,
    find the index i such that `t_i <= t < t_{i+1}` using bisection. The rest of
    the tuple is available for whatever use required.

    INPUT:

    - ``L`` -- list of tuples such that the first term of each tuple is a real
      number between 0 and 1. These real numbers must be increasing

    - ``t`` -- real number between `t_0` and `t_n`

    OUTPUT: integer i, giving the position in L where t would be in

    EXAMPLES:

    Form a list of the desired form, and pick a real number between 0 and 1::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import bisect
        sage: L = [(0.0, 'a'), (0.3, 'b'), (0.7, 'c'), (0.8, 'd'), (0.9, 'e'), (1.0, 'f')]
        sage: t = 0.5
        sage: bisect(L,t)
        1

    Another example which demonstrates that if t is equal to one of the t_i, it
    returns that index::

        sage: L = [(0.0, 'a'), (0.1, 'b'), (0.45, 'c'), (0.5, 'd'), (0.65, 'e'), (1.0, 'f')]
        sage: t = 0.5
        sage: bisect(L,t)
        3
    """
def numerical_inverse(C):
    """
    Compute numerical inverse of a matrix via LU decomposition.

    INPUT:

    - ``C`` -- a real or complex invertible square matrix

    EXAMPLES::

        sage: C = matrix(CC, 3, 3, [-4.5606e-31 + 1.2326e-31*I,
        ....:                       -0.21313 + 0.24166*I,
        ....:                       -3.4513e-31 + 0.16111*I,
        ....:                       -1.0175 + 9.8608e-32*I,
        ....:                       0.30912 + 0.19962*I,
        ....:                       -4.9304e-32 + 0.39923*I,
        ....:                       0.96793 - 3.4513e-31*I,
        ....:                       -0.091587 + 0.19276*I,
        ....:                       3.9443e-31 + 0.38552*I])
        sage: from sage.schemes.riemann_surfaces.riemann_surface import numerical_inverse
        sage: 3e-16 < (C^-1*C-C^0).norm() < 1e-15
        True
        sage: (numerical_inverse(C)*C-C^0).norm() < 3e-16
        True
    """

class ConvergenceError(ValueError):
    '''
    Error object suitable for raising and catching when Newton iteration fails.

    EXAMPLES::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import ConvergenceError
        sage: raise ConvergenceError("test")
        Traceback (most recent call last):
        ...
        ConvergenceError: test
        sage: isinstance(ConvergenceError(),ValueError)
        True
    '''

def differential_basis_baker(f):
    """
    Compute a differential basis for a curve that is nonsingular outside (1:0:0),(0:1:0),(0:0:1).

    Baker's theorem tells us that if a curve has its singularities at the coordinate vertices and meets
    some further easily tested genericity criteria,
    then we can read off a basis for the regular differentials from the interior of the
    Newton polygon spanned by the monomials. While this theorem only applies to special plane curves
    it is worth implementing because the analysis is relatively cheap and it applies to a lot of
    commonly encountered curves (e.g., curves given by a hyperelliptic model). Other advantages include
    that we can do the computation over any exact base ring (the alternative Singular based method for
    computing the adjoint ideal requires the rationals), and that we can avoid being affected by subtle bugs
    in the Singular code.

    ``None`` is returned when ``f`` does not describe a curve of the relevant type. If ``f`` is of the relevant
    type, but is of genus `0` then ``[]`` is returned (which are both False values, but they are not equal).

    INPUT:

    - ``f`` -- a bivariate polynomial

    EXAMPLES::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import differential_basis_baker
        sage: R.<x,y> = QQ[]
        sage: f = x^3 + y^3 + x^5*y^5
        sage: differential_basis_baker(f)
        [y^2, x*y, x*y^2, x^2, x^2*y, x^2*y^2, x^2*y^3, x^3*y^2, x^3*y^3]
        sage: f = y^2 - (x-3)^2*x
        sage: differential_basis_baker(f) is None
        True
        sage: differential_basis_baker(x^2+y^2-1)
        []

    TESTS::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import differential_basis_baker
        sage: R.<x,y> = QQ[]
        sage: f = y^12 - x*(x - 1)^7
        sage: differential_basis_baker(f) is None
        True
    """
def find_closest_element(item, lst):
    """
    Return the index of the closest element of a list.

    Given ``List`` and ``item``, return the index of the element ``l`` of ``List``
    which minimises ``(item-l).abs()``. If there are multiple such elements, the
    first is returned.

    INPUT:

    - ``item`` -- value to minimize the distance to over the list

    - ``lst`` -- list to look for closest element in

    EXAMPLES::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import find_closest_element
        sage: i = 5
        sage: l = list(range(10))
        sage: i == find_closest_element(i, l)
        True

    Note that this method does no checks on the input, but will fail for inputs
    where the absolute value or subtraction do not make sense.
    """
def reparameterize_differential_minpoly(minpoly, z0):
    """
    Rewrites a minimal polynomial to write is around `z_0`.

    Given a minimal polynomial `m(z,g)`, where `g` corresponds to a differential
    on the surface (that is, it is represented as a rational function, and
    implicitly carries a factor `dz`), we rewrite the minpoly in terms of
    variables `\\bar{z}, \\bar{g}` s.t now `\\bar{z}=0 \\Leftrightarrow z=z_0`.

    INPUT:

    - ``minpoly`` -- a polynomial in two variables, where the first variable
      corresponds to the base coordinate on the Riemann surface
    - ``z0`` -- complex number or infinity; the point about which to
      reparameterize

    OUTPUT: a polynomial in two variables giving the reparameterize minimal polynomial

    EXAMPLES:

    On the curve given by `w^2 - z^3 + 1 = 0`, we have differential
    `\\frac{dz}{2w} = \\frac{dz}{2\\sqrt{z^3-1}}`
    with minimal polynomial `g^2(z^3-1) - 1/4=0`. We can make the substitution
    `\\bar{z}=z^{-1}` to parameterise the differential about `z=\\infty` as

    .. MATH::

        \\frac{-\\bar{z}^{-2} d\\bar{z}}{2\\sqrt{\\bar{z}^{-3}-1}} = \\frac{-d\\bar{z}}{2\\sqrt{\\bar{z}(1-\\bar{z}^3)}}.

    Hence the transformed differential should have minimal polynomial
    `\\bar{g}^2 \\bar{z} (1 - \\bar{z}^3) - 1/4 = 0`, and we can check this::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface, reparameterize_differential_minpoly
        sage: R.<z,w> = QQ[]
        sage: S = RiemannSurface(w^2-z^3+1)
        sage: minpoly = S._cohomology_basis_bounding_data[1][0][2]
        sage: z0 = Infinity
        sage: reparameterize_differential_minpoly(minpoly, z0)
        -zbar^4*gbar^2 + zbar*gbar^2 - 1/4

    We can further check that reparameterising about `0` is the identity
    operation::

        sage: reparameterize_differential_minpoly(minpoly, 0)(*minpoly.parent().gens()) == minpoly
        True

    .. NOTE::

        As part of the routine, when reparameterising about infinity, a
        rational function is reduced and then the numerator is taken. Over
        an inexact ring this is numerically unstable, and so it is advisable
        to only reparameterize about infinity over an exact ring.
    """

class RiemannSurface:
    """
    Construct a Riemann Surface. This is specified by the zeroes of a bivariate
    polynomial with rational coefficients `f(z,w) = 0`.

    INPUT:

    - ``f`` -- a bivariate polynomial with rational coefficients. The surface is
      interpreted as the covering space of the coordinate plane in the first
      variable.

    - ``prec`` -- the desired precision of computations on the surface in bits
      (default: 53)

    - ``certification`` -- boolean (default: ``True``); value indicating
      whether homotopy continuation is certified or not. Uncertified
      homotopy continuation can be faster.

    - ``differentials`` -- (default: ``None``) if specified, provides a list
      of polynomials `h` such that `h/(df/dw) dz` is a regular
      differential on the Riemann surface. This is taken as a basis of
      the regular differentials, so the genus is assumed to be equal
      to the length of this list. The results from the homology basis
      computation are checked against this value.  Providing this
      parameter makes the computation independent from Singular.  For
      a nonsingular plane curve of degree `d`, an appropriate set is
      given by the monomials of degree up to `d-3`.

    - ``integration_method`` -- (default: ``'rigorous'``). String specifying the
      integration method to use when calculating the integrals of differentials.
      The options are ``'heuristic'`` and ``'rigorous'``, the latter of
      which is often the most efficient.

    EXAMPLES::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
        sage: R.<z,w> = QQ[]
        sage: f = w^2 - z^3 + 1
        sage: RiemannSurface(f)
        Riemann surface defined by polynomial f = -z^3 + w^2 + 1 = 0, with 53 bits of precision

    Another Riemann surface with 100 bits of precision::

        sage: S = RiemannSurface(f, prec=100); S
        Riemann surface defined by polynomial f = -z^3 + w^2 + 1 = 0, with 100 bits of precision
        sage: S.riemann_matrix()^6 #abs tol 0.00000001
        [1.0000000000000000000000000000 - 1.1832913578315177081175928479e-30*I]

    We can also work with Riemann surfaces that are defined over fields with a
    complex embedding, but since the current interface for computing genus and
    regular differentials in Singular presently does not support extensions of
    `\\QQ`, we need to specify a description of the differentials ourselves. We give
    an example of a CM elliptic curve::

        sage: Qt.<t> = QQ[]
        sage: K.<a> = NumberField(t^2-t+3,embedding=CC(0.5+1.6*I))
        sage: R.<x,y> = K[]
        sage: f = y^2 + y - (x^3 + (1-a)*x^2 - (2+a)*x - 2)
        sage: S = RiemannSurface(f, prec=100, differentials=[1])
        sage: A = S.endomorphism_basis()
        sage: len(A)
        2
        sage: all(len(T.minpoly().roots(K)) > 0 for T in A)
        True

    The ``'heuristic'`` integration method uses the method ``integrate_vector``
    defined in ``sage.numerical.gauss_legendre`` to compute integrals of differentials.
    As mentioned there, this works by iteratively doubling the number of nodes
    used in the quadrature, and uses a heuristic based on the rate at which the
    result is seemingly converging to estimate the error. The ``'rigorous'``
    method uses results from [Neu2018]_, and bounds the algebraic integrands on
    circular domains using Cauchy's form of the remainder in Taylor approximation
    coupled to Fujiwara's bound on polynomial roots (see Bruin-DisneyHogg-Gao,
    in preparation). Note this method of bounding on circular domains is also
    implemented in :meth:`_compute_delta`. The net result of this bounding is
    that one can know (an upper bound on) the number of nodes required to achieve
    a certain error. This means that for any given integral, assuming that the
    same number of nodes is required by both methods in order to achieve the
    desired error (not necessarily true in practice), approximately half
    the number of integrand evaluations are required. When the required number
    of nodes is high, e.g. when the precision required is high, this can make
    the ``'rigorous'`` method much faster. However, the ``'rigorous'`` method does
    not benefit as much from the caching of the ``nodes`` method over multiple
    integrals. The result of this is that, for calls of :meth:`matrix_of_integral_values`
    if the computation is 'fast', the heuristic method may outperform the
    rigorous method, but for slower computations the rigorous method can be much
    faster::

        sage: f = z*w^3 + z^3 + w
        sage: p = 53
        sage: Sh = RiemannSurface(f, prec=p, integration_method='heuristic')
        sage: Sr = RiemannSurface(f, prec=p, integration_method='rigorous')
        sage: from sage.numerical.gauss_legendre import nodes
        sage: import time
        sage: nodes.cache.clear()
        sage: ct = time.time()
        sage: Rh = Sh.riemann_matrix()
        sage: ct1 = time.time()-ct
        sage: nodes.cache.clear()
        sage: ct = time.time()
        sage: Rr = Sr.riemann_matrix()
        sage: ct2 = time.time()-ct
        sage: ct2/ct1  # random
        1.2429363969691192

    Note that for the above curve, the branch points are evenly distributed, and
    hence the implicit assumptions in the heuristic method are more sensible,
    meaning that a higher precision is required to see the heuristic method
    being significantly slower than the rigorous method. For a worse conditioned
    curve, this effect is more pronounced::

        sage: q = 1 / 10
        sage: f = y^2 - (x^2 - 2*x + 1 + q^2) * (x^2 + 2*x + 1 + q^2)
        sage: p = 500
        sage: Sh = RiemannSurface(f, prec=p, integration_method='heuristic')
        sage: Sr = RiemannSurface(f, prec=p, integration_method='rigorous')
        sage: nodes.cache.clear()
        sage: Rh = Sh.riemann_matrix()  # long time (8 seconds)
        sage: nodes.cache.clear()
        sage: Rr = Sr.riemann_matrix()  # long time (1 seconds)

    This disparity in timings can get increasingly worse, and testing has shown
    that even for random quadrics the heuristic method can be as bad as 30 times
    slower.

    TESTS:

    This elliptic curve has a relatively poorly conditioned set of branch
    points, so it challenges the path choice a bit. The code just verifies that
    the period is quadratic, because the curve has CM, but really the test is
    that the computation completes at all.::

        sage: prec = 50
        sage: Qx.<t> = QQ[]
        sage: CC = ComplexField(prec)
        sage: g = t^2-t-1
        sage: phiCC = g.roots(CC)[1][0]
        sage: K.<phi> = NumberField(g, embedding=phiCC)
        sage: R.<X,Y> = K[]
        sage: f = Y^2+X*Y+phi*Y-(X^3-X^2-2*phi*X+phi)
        sage: S = RiemannSurface(f,prec=prec, differentials=[1])
        sage: tau = S.riemann_matrix()[0, 0]
        sage: tau.algebraic_dependency(6).degree() == 2
        True
    """
    f: Incomplete
    genus: Incomplete
    degree: Incomplete
    branch_locus: Incomplete
    voronoi_diagram: Incomplete
    def __init__(self, f, prec: int = 53, certification: bool = True, differentials=None, integration_method: str = 'rigorous') -> None:
        """
        TESTS::

            sage: R.<z,w> = QQ[]
            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: S = RiemannSurface(w^2 - z^3 + 1)
            sage: TestSuite(S).run() #not tested; Unclear what pickling strategy is best.
        """
    def w_values(self, z0):
        """
        Return the points lying on the surface above ``z0``.

        INPUT:

        - ``z0`` -- complex number; a point in the complex z-plane

        OUTPUT:

        A set of complex numbers corresponding to solutions of `f(z_0,w) = 0`.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 - z^4 + 1
            sage: S = RiemannSurface(f)

        Find the w-values above the origin, i.e. the solutions of `w^2 + 1 = 0`::

            sage: S.w_values(0)  # abs tol 1e-14
            [-1.00000000000000*I, 1.00000000000000*I]

        Note that typically the method returns a list of length ``self.degree``,
        but that at ramification points, this may no longer be true::

            sage: S.w_values(1)  # abs tol 1e-14
            [0.000000000000000]
        """
    @cached_method
    def downstairs_edges(self):
        """
        Compute the edgeset of the Voronoi diagram.

        OUTPUT:

        A list of integer tuples corresponding to edges between vertices in the
        Voronoi diagram.

        EXAMPLES:

        Form a Riemann surface, one with a particularly simple branch locus::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 + z^3 - z^2
            sage: S = RiemannSurface(f)

        Compute the edges::

            sage: S.downstairs_edges()
            [(0, 1), (0, 5), (1, 4), (2, 3), (2, 4), (3, 5), (4, 5)]

        This now gives an edgeset which one could use to form a graph.

        .. NOTE::

            The numbering of the vertices is given by the Voronoi package.
        """
    def downstairs_graph(self):
        """
        Return the Voronoi decomposition as a planar graph.

        The result of this routine can be useful to interpret the labelling of
        the vertices. See also :meth:`upstairs_graph`.

        OUTPUT: the Voronoi decomposition as a graph, with appropriate planar embedding

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 - z^4 + 1
            sage: S = RiemannSurface(f)
            sage: S.downstairs_graph()
            Graph on 11 vertices
        """
    @cached_method
    def upstairs_graph(self):
        """
        Return the graph of the upstairs edges.

        This method can be useful for generating paths in the surface between points labelled
        by upstairs vertices, and verifying that a homology basis is likely computed correctly.
        See also :meth:`downstairs_graph`.

        OUTPUT:

        The homotopy-continued Voronoi decomposition as a graph, with appropriate 3D embedding.

        EXAMPLES::

            sage: R.<z,w> = QQ[]
            sage: S = Curve(w^2-z^4+1).riemann_surface()
            sage: G = S.upstairs_graph(); G
            Graph on 22 vertices
            sage: G.genus()
            1
            sage: G.is_connected()
            True
        """
    def homotopy_continuation(self, edge):
        """
        Perform homotopy continuation along an edge of the Voronoi diagram using
        Newton iteration.

        INPUT:

        - ``edge`` -- tuple ``(z_start, z_end)`` indicating the straight line
          over which to perform the homotopy continuation

        OUTPUT:

        A list containing the initialised continuation data. Each entry in the
        list contains: the `t` values that entry corresponds to, a list of
        complex numbers corresponding to the points which are reached when
        continued along the edge when traversing along the direction of the
        edge, and a value ``epsilon`` giving the minimumdistance between the
        fibre values divided by 3. The ordering of these points indicates how
        they have been permuted due to the weaving of the curve.

        EXAMPLES:

        We check that continued values along an edge correspond (up to the
        appropriate permutation) to what is stored. Note that the permutation
        was originally computed from this data::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = z^3*w + w^3 + z
            sage: S = RiemannSurface(f)
            sage: edge1 = sorted(S.edge_permutations())[0]
            sage: sigma = S.edge_permutations()[edge1]
            sage: edge = [S._vertices[i] for i in edge1]
            sage: continued_values = S.homotopy_continuation(edge)[-1][1]
            sage: stored_values = S.w_values(S._vertices[edge1[1]])
            sage: all(abs(continued_values[i]-stored_values[sigma(i)]) < 1e-8 for i in range(3))
            True
        """
    @cached_method
    def upstairs_edges(self):
        """
        Compute the edgeset of the lift of the downstairs graph onto the Riemann
        surface.

        OUTPUT:

        An edgeset between vertices (i, j), where i corresponds to the i-th
        point in the Voronoi diagram vertices, and j is the j-th w-value
        associated with that point.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 + z^3 - z^2
            sage: S = RiemannSurface(f)
            sage: edgeset = S.upstairs_edges()
            sage: len(edgeset) == S.degree*len(S.downstairs_edges())
            True
            sage: {(v[0],w[0]) for v,w in edgeset} == set(S.downstairs_edges())
            True
        """
    @cached_method
    def edge_permutations(self) -> dict:
        """
        Compute the permutations of branches associated to each edge.

        Over the vertices of the Voronoi decomposition around the branch locus,
        we label the fibres. By following along an edge, the lifts of the edge
        induce a permutation of that labelling.

        OUTPUT:

        A dictionary with as keys the edges of the Voronoi decomposition and as
        values the corresponding permutations.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 + z^2+1
            sage: S = RiemannSurface(f)
            sage: S.edge_permutations()
            {(0, 2): (),
             (0, 4): (),
             (1, 2): (),
             (1, 3): (0,1),
             (1, 6): (),
             (2, 0): (),
             (2, 1): (),
             (2, 5): (0,1),
             (3, 1): (0,1),
             (3, 4): (),
             (4, 0): (),
             (4, 3): (),
             (5, 2): (0,1),
             (5, 7): (),
             (6, 1): (),
             (6, 7): (),
             (7, 5): (),
             (7, 6): ()}
        """
    @cached_method
    def monodromy_group(self):
        """
        Compute local monodromy generators of the Riemann surface.

        For each branch point, the local monodromy is encoded by a permutation.
        The permutations returned correspond to positively oriented loops around
        each branch point, with a fixed base point. This means the generators
        are properly conjugated to ensure that together they generate the global
        monodromy. The list has an entry for every finite point stored in
        ``self.branch_locus``, plus an entry for the ramification above infinity.

        OUTPUT:

        A list of permutations, encoding the local monodromy at each branch
        point.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z, w> = QQ[]
            sage: f = z^3*w + w^3 + z
            sage: S = RiemannSurface(f)
            sage: G = S.monodromy_group(); G
            [(0,1,2), (0,1), (0,2), (1,2), (1,2), (1,2), (0,1), (0,2), (0,2)]

        The permutations give the local monodromy generators for the branch
        points::

            sage: list(zip(S.branch_locus + [unsigned_infinity], G)) #abs tol 0.0000001
            [(0.000000000000000, (0,1,2)),
             (-1.31362670141929, (0,1)),
             (-0.819032851784253 - 1.02703471138023*I, (0,2)),
             (-0.819032851784253 + 1.02703471138023*I, (1,2)),
             (0.292309440469772 - 1.28069133740100*I, (1,2)),
             (0.292309440469772 + 1.28069133740100*I, (1,2)),
             (1.18353676202412 - 0.569961265016465*I, (0,1)),
             (1.18353676202412 + 0.569961265016465*I, (0,2)),
             (Infinity, (0,2))]

        We can check the ramification by looking at the cycle lengths and verify
        it agrees with the Riemann-Hurwitz formula::

            sage: 2*S.genus-2 == -2*S.degree + sum(e-1 for g in G for e in g.cycle_type())
            True
        """
    @cached_method
    def homology_basis(self):
        """
        Compute the homology basis of the Riemann surface.

        OUTPUT:

        A list of paths `L = [P_1, \\dots, P_n]`. Each path `P_i` is of the form
        `(k, [p_1 ... p_m, p_1])`, where `k` is the number of times to traverse
        the path (if negative, to traverse it backwards), and the `p_i` are
        vertices of the upstairs graph.

        EXAMPLES:

        In this example, there are two paths that form the homology basis::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: g = w^2 - z^4 + 1
            sage: S = RiemannSurface(g)
            sage: S.homology_basis()  # random
            [[(1, [(3, 1), (5, 0), (9, 0), (10, 0), (2, 0), (4, 0),
                (7, 1), (10, 1), (3, 1)])],
             [(1, [(8, 0), (6, 0), (7, 0), (10, 0), (2, 0), (4, 0),
                (7, 1), (10, 1), (9, 1), (8, 0)])]]

        In order to check that the answer returned above is reasonable, we
        test some basic properties. We express the faces of the downstairs graph
        as ZZ-linear combinations of the edges and check that the projection
        of the homology basis upstairs projects down to independent linear
        combinations of an even number of faces::

            sage: dg = S.downstairs_graph()
            sage: edges = dg.edges(sort=True)
            sage: E = ZZ^len(edges)
            sage: edge_to_E = { e[:2]: E.gen(i) for i,e in enumerate(edges)}
            sage: edge_to_E.update({ (e[1],e[0]): -E.gen(i) for i,e in enumerate(edges)})
            sage: face_span = E.submodule([sum(edge_to_E[e] for e in f) for f in dg.faces()])
            sage: def path_to_E(path):
            ....:     k,P = path
            ....:     return k*sum(edge_to_E[(P[i][0],P[i+1][0])] for i in range(len(P)-1))
            sage: hom_basis = [sum(path_to_E(p) for p in loop) for loop in S.homology_basis()]
            sage: face_span.submodule(hom_basis).rank()
            2
            sage: [sum(face_span.coordinate_vector(b))%2 for b in hom_basis]
            [0, 0]
        """
    def make_zw_interpolator(self, upstairs_edge, initial_continuation=None):
        """
        Given a downstairs edge for which continuation data has been initialised,
        return a function that computes `z(t), w(t)` , where `t` in `[0,1]` is a
        parametrization of the edge.

        INPUT:

        - ``upstairs_edge`` -- tuple ``((z_start, sb), (z_end,))`` giving the
          start and end values of the base coordinate along the straight-line
          path and the starting branch
        - ``initial_continuation`` -- list (optional);  output of
          ``homotopy_continuation`` initialising the continuation data

        OUTPUT:

        A tuple ``(g, d)``, where ``g`` is the function that computes the interpolation
        along the edge and ``d`` is the difference of the z-values of the end and
        start point.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 - z^4 + 1
            sage: S = RiemannSurface(f)
            sage: _ = S.homology_basis()
            sage: u_edge = [(0, 0), (1, 0)]
            sage: d_edge = tuple(u[0] for u in u_edge)
            sage: u_edge = [(S._vertices[i], j) for i, j in u_edge]
            sage: initial_continuation = S._L[d_edge]
            sage: g, d = S.make_zw_interpolator(u_edge, initial_continuation)
            sage: all(f(*g(i*0.1)).abs() < 1e-13 for i in range(10))
            True
            sage: abs((g(1)[0]-g(0)[0]) - d) < 1e-13
            True

        .. NOTE::

            The interpolator returned by this method can effectively hang if
            either ``z_start`` or ``z_end`` are branchpoints. In these situations
            it is better to take a different approach rather than continue to use
            the interpolator.
        """
    def simple_vector_line_integral(self, upstairs_edge, differentials):
        """
        Perform vectorized integration along a straight path.

        INPUT:

        - ``upstairs_edge`` -- tuple; either a pair of integer tuples
          corresponding to an edge of the upstairs graph, or a tuple
          ``((z_start, sb), (z_end, ))`` as in the input of
          ``make_zw_interpolator``

        - ``differentials`` -- list of polynomials; a polynomial `g`
          represents the differential `g(z,w)/(df/dw) dz` where `f(z,w)=0` is
          the equation defining the Riemann surface

        OUTPUT: a complex number, the value of the line integral

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 - z^4 + 1
            sage: S = RiemannSurface(f); S
            Riemann surface defined by polynomial f = -z^4 + w^2 + 1 = 0, with 53 bits of precision

        Since we make use of data from homotopy continuation, we need to compute
        the necessary data::

            sage: M = S.riemann_matrix()
            sage: differentials = S.cohomology_basis()
            sage: S.simple_vector_line_integral([(0, 0), (1, 0)], differentials) #abs tol 0.00000001
            (1.14590610929717e-16 - 0.352971844594760*I)

        .. NOTE::

            Uses data that :meth:`homology_basis` initializes, and may give incorrect
            values if :meth:`homology_basis` has not initialized them. In practice
            it is more efficient to set ``differentials`` to a fast-callable version
            of differentials to speed up execution.
        """
    def cohomology_basis(self, option: int = 1):
        """
        Compute the cohomology basis of this surface.

        INPUT:

        - ``option`` -- presently, this routine uses Singular's ``adjointIdeal``
          and passes the ``option`` parameter on. Legal values are 1, 2, 3 ,4,
          where 1 is the default. See the Singular documentation for the
          meaning. The backend for this function may change, and support for
          this parameter may disappear.

        OUTPUT:

        This returns a list of polynomials `g` representing the holomorphic
        differentials `g/(df/dw) dz`, where `f(z,w)=0` is the equation
        specifying the Riemann surface.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = z^3*w + w^3 + z
            sage: S = RiemannSurface(f)
            sage: S.cohomology_basis()
            [1, w, z]
        """
    def rigorous_line_integral(self, upstairs_edge, differentials, bounding_data):
        """
        Perform vectorized integration along a straight path.

        Using the error bounds for Gauss-Legendre integration found in [Neu2018]_
        and a method for bounding an algebraic integrand on a circular domains
        using Cauchy's form of the remainder in Taylor approximation coupled to
        Fujiwara's bound on polynomial roots (see Bruin-DisneyHogg-Gao, in
        preparation), this method calculates (semi-)rigorously the integral of a
        list of differentials along an edge of the upstairs graph.

        INPUT:

        - ``upstairs_edge`` -- tuple; either a pair of integer tuples
          corresponding to an edge of the upstairs graph, or a tuple
          ``((z_start, sb), (z_end, ))`` as in the input of
          ``make_zw_interpolator``

        - ``differentials`` -- list of polynomials; a polynomial `g`
          represents the differential `g(z,w)/(df/dw) dz` where `f(z,w)=0` is
          the equation defining the Riemann surface

        - ``bounding_data`` -- tuple containing the data required for bounding
          the integrands. This should be in the form of the output from
          :meth:`_bounding_data`.

        OUTPUT: a complex number, the value of the line integral

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = w^2 - z^4 + 1
            sage: S = RiemannSurface(f); S
            Riemann surface defined by polynomial f = -z^4 + w^2 + 1 = 0, with 53 bits of precision

        Since we make use of data from homotopy continuation, we need to compute
        the necessary data::

            sage: _ = S.homology_basis()
            sage: differentials = S.cohomology_basis()
            sage: bounding_data = S._bounding_data(differentials)
            sage: S.rigorous_line_integral([(0,0), (1,0)], differentials, bounding_data)  # abs tol 1e-10
            (1.80277751848459e-16 - 0.352971844594760*I)

        .. NOTE::

            Uses data that ``homology_basis`` initializes, and may give incorrect
            values if :meth:`homology_basis` has not initialized them.

            Note also that the data of the differentials is contained within
            ``bounding_data``. It is, however, still advantageous to have this
            be a separate argument, as it lets the user supply a fast-callable
            version of the differentials, to significantly speed up execution
            of the integrand calls, and not have to re-calculate these
            fast-callables for every run of the function. This is also the benefit
            of representing the  differentials as a polynomial over a known
            common denominator.

        .. TODO::

            Note that bounding_data contains the information of the integrands,
            so one may want to check for consistency between ``bounding_data``
            and ``differentials``. If so one would not want to do so at the
            expense of speed.

            Moreover, the current implementation bounds along a line by
            splitting it up into segments, each of which can be covered entirely
            by a single circle, and then placing inside that the ellipse
            required to bound as per [Neu2018]_. This is reliably more efficient
            than the heuristic method, especially in poorly-conditioned cases
            where discriminant points are close together around the edges, but
            in the case where the branch locus is well separated, it can require
            slightly more nodes than necessary. One may want to include a method
            here to transition in this regime to an algorithm that covers the
            entire line with one ellipse, then bounds along that ellipse with
            multiple circles.
        """
    def matrix_of_integral_values(self, differentials, integration_method: str = 'heuristic'):
        """
        Compute the path integrals of the given differentials along the homology
        basis.

        The returned answer has a row for each differential. If the Riemann
        surface is given by the equation `f(z,w)=0`, then the differentials are
        encoded by polynomials g, signifying the differential `g(z,w)/(df/dw)
        dz`.

        INPUT:

        - ``differentials`` -- list of polynomials

        - ``integration_method`` -- (default: ``'heuristic'``) string specifying
          the integration method to use. The options are ``'heuristic'`` and
          ``'rigorous'``.

        OUTPUT:

        A matrix, one row per differential, containing the values of the path
        integrals along the homology basis of the Riemann surface.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(x^3 + y^3 + 1)
            sage: B = S.cohomology_basis()
            sage: m = S.matrix_of_integral_values(B)
            sage: parent(m)
            Full MatrixSpace of 1 by 2 dense matrices over Complex Field with 53 bits of precision
            sage: (m[0,0]/m[0,1]).algebraic_dependency(3).degree() # curve is CM, so the period is quadratic
            2

        .. NOTE::

            If ``differentials is self.cohomology_basis()``, the calculations
            of the integrals along the edges are written to ``self._integral_dict``.
            This is as this data will be required when computing the Abel-Jacobi
            map, and so it is helpful to have is stored rather than recomputing.
        """
    @cached_method
    def period_matrix(self):
        """
        Compute the period matrix of the surface.

        OUTPUT: a matrix of complex values

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = z^3*w + w^3 + z
            sage: S = RiemannSurface(f, prec=30)
            sage: M = S.period_matrix()

        The results are highly arbitrary, so it is hard to check if the result
        produced is correct. The closely related ``riemann_matrix`` is somewhat
        easier to test.::

            sage: parent(M)
            Full MatrixSpace of 3 by 6 dense matrices
             over Complex Field with 30 bits of precision
            sage: M.rank()
            3

        One can check that the two methods give similar answers::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: f = y^2 - x^3 + 1
            sage: S = RiemannSurface(f, integration_method='rigorous')
            sage: T = RiemannSurface(f, integration_method='heuristic')
            sage: RM_S = S.riemann_matrix()
            sage: RM_T = T.riemann_matrix()
            sage: (RM_S-RM_T).norm() < 1e-10
            True
        """
    def riemann_matrix(self):
        """
        Compute the Riemann matrix.

        OUTPUT: a matrix of complex values

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<z,w> = QQ[]
            sage: f = z^3*w + w^3 + z
            sage: S = RiemannSurface(f, prec=60)
            sage: M = S.riemann_matrix()

        The Klein quartic has a Riemann matrix with values in a quadratic
        field::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 - x + 2)
            sage: all(len(m.algebraic_dependency(6).roots(K)) > 0 for m in M.list())
            True
        """
    def plot_paths(self):
        """
        Make a graphical representation of the integration paths.

        This returns a two dimensional plot containing the branch points (in red) and
        the integration paths (obtained from the Voronoi cells of the branch
        points). The integration paths are plotted by plotting the points that
        have been computed for homotopy continuation, so the density gives an
        indication of where numerically sensitive features occur.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - x^3 - x)
            sage: S.plot_paths()                                                        # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        """
    def plot_paths3d(self, thickness: float = 0.01):
        """
        Return the homology basis as a graph in 3-space.

        The homology basis of the surface is constructed by taking the Voronoi
        cells around the branch points and taking the inverse image of the edges
        on the Riemann surface. If the surface is given by the equation
        `f(z,w)`, the returned object gives the image of this graph in 3-space
        with coordinates `\\left(\\operatorname{Re}(z), \\operatorname{Im}(z),
        \\operatorname{Im}(w)\\right)`.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - x^3 - x)
            sage: S.plot_paths3d()                                                      # needs sage.plot
            Graphics3d Object
        """
    def endomorphism_basis(self, b=None, r=None):
        """
        Numerically compute a `\\ZZ`-basis for the endomorphism ring.

        Let `\\left(I | M \\right)` be the normalized period matrix (`M` is the
        `g\\times g` :meth:`riemann_matrix`). We consider the system of matrix
        equations `MA + C = (MB + D)M` where `A, B, C, D` are `g\\times g`
        integer matrices.  We determine small integer (near) solutions using LLL
        reductions.  These solutions are returned as `2g \\times 2g` integer
        matrices obtained by stacking `\\left(D | B\\right)` on top of `\\left(C |
        A\\right)`.

        INPUT:

        - ``b`` -- integer (default provided); the equation coefficients are
          scaled by `2^b` before rounding to integers

        - ``r`` -- integer (default: ``b/4``); solutions that have all
          coefficients smaller than `2^r` in absolute value are reported as
          actual solutions

        OUTPUT:

        A list of `2g \\times 2g` integer matrices that, for large enough ``r``
        and ``b-r``, generate the endomorphism ring.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(x^3 + y^3 + 1)
            sage: B = S.endomorphism_basis(); B #random
            [
            [1 0]  [ 0 -1]
            [0 1], [ 1  1]
            ]
            sage: sorted([b.minpoly().disc() for b in B])
            [-3, 1]
        """
    def homomorphism_basis(self, other, b=None, r=None):
        '''
        Numerically compute a `\\ZZ`-basis for module of homomorphisms to a given
        complex torus.

        Given another complex torus (given as the analytic Jacobian of a Riemann
        surface), numerically compute a basis for the homomorphism module. The
        answer is returned as a list of `2g \\times 2g` integer matrices `T=(D, B; C, A)`
        such that if the columns of `(I|M_1)` generate the lattice defining the
        Jacobian of the Riemann surface and the columns of `(I|M_2)` do this for
        the codomain, then approximately we have `(I|M_2)T=(D+M_2C)(I|M_1)`, i.e., up
        to a choice of basis for `\\CC^g` as a complex vector space, we we
        realize `(I|M_1)` as a sublattice of `(I|M_2)`.

        INPUT:

        - ``b`` -- integer (default provided); the equation coefficients are
          scaled by `2^b` before rounding to integers

        - ``r`` -- integer (default: ``b/4``); solutions that have all
          coefficients smaller than `2^r` in absolute value are reported as
          actual solutions

        OUTPUT:

        A list of `2g \\times 2g` integer matrices that, for large enough ``r``
        and ``b-r``, generate the homomorphism module.

        EXAMPLES::

            sage: S1 = EllipticCurve("11a1").riemann_surface()
            sage: S2 = EllipticCurve("11a3").riemann_surface()
            sage: [m.det() for m in S1.homomorphism_basis(S2)]
            [5]
        '''
    def tangent_representation_numerical(self, Rs, other=None):
        """
        Compute the numerical tangent representations corresponding to the
        homology representations in ``Rs``.

        The representations on homology ``Rs`` have to be given with respect to
        the symplectic homology basis of the Jacobian of ``self`` and ``other``.
        Such matrices can for example be obtained via
        :meth:`endomorphism_basis`.

        Let `P` and `Q` be the period matrices of ``self`` and ``other``. Then
        for a homology representation `R`, the corresponding tangential
        representation `T` satisfies `T P = Q R`.

        INPUT:

        - ``Rs`` -- set of matrices on homology to be converted to their
          tangent representations

        - ``other`` -- (default: ``self``) the codomain; another Riemann
          surface

        OUTPUT: the numerical tangent representations of the matrices in ``Rs``

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: A.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - (x^6 + 2*x^4 + 4*x^2 + 8), prec = 100)
            sage: P = S.period_matrix()
            sage: Rs = S.endomorphism_basis()
            sage: Ts = S.tangent_representation_numerical(Rs)
            sage: all(((T*P - P*R).norm() < 2^(-80)) for [T, R] in zip(Ts, Rs))
            True
        """
    def tangent_representation_algebraic(self, Rs, other=None, epscomp=None):
        """
        Compute the algebraic tangent representations corresponding to the
        homology representations in ``Rs``.

        The representations on homology ``Rs`` have to be given with respect to
        the symplectic homology basis of the Jacobian of ``self`` and ``other``.
        Such matrices can for example be obtained via
        :meth:`endomorphism_basis`.

        Let `P` and `Q` be the period matrices of ``self`` and ``other``. Then
        for a homology representation `R`, the corresponding tangential
        representation `T` satisfies `T P = Q R`.

        INPUT:

        - ``Rs`` -- set of matrices on homology to be converted to their
          tangent representations

        - ``other`` -- (default: ``self``) the codomain; another Riemann
          surface

        - ``epscomp`` -- real number (default: ``2^(-prec + 30)``). Used to
          determine whether a complex number is close enough to a root of a
          polynomial.

        OUTPUT: the algebraic tangent representations of the matrices in ``Rs``

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: A.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - (x^6 + 2*x^4 + 4*x^2 + 8), prec = 100)
            sage: Rs = S.endomorphism_basis()
            sage: Ts = S.tangent_representation_algebraic(Rs)
            sage: Ts[0].base_ring().maximal_order().discriminant() == 8
            True
        """
    def rosati_involution(self, R):
        """
        Compute the Rosati involution of an endomorphism.

        The endomorphism in question should be given by its homology
        representation with respect to the symplectic basis of the Jacobian.

        INPUT:

        - ``R`` -- integral matrix

        OUTPUT: the result of applying the Rosati involution to ``R``

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: A.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - (x^6 + 2*x^4 + 4*x^2 + 8), prec = 100)
            sage: Rs = S.endomorphism_basis()
            sage: S.rosati_involution(S.rosati_involution(Rs[1])) == Rs[1]
            True
        """
    def symplectic_isomorphisms(self, other=None, hom_basis=None, b=None, r=None):
        """
        Numerically compute symplectic isomorphisms.

        INPUT:

        - ``other`` -- (default: ``self``) the codomain; another Riemann
          surface

        - ``hom_basis`` -- (default: ``None``) a `\\ZZ`-basis of the
          homomorphisms from ``self`` to ``other``, as obtained from
          :meth:`homomorphism_basis`. If you have already calculated this
          basis, it saves time to pass it via this keyword argument. Otherwise
          the method will calculate it.

        - ``b`` -- integer (default provided); as for
          :meth:`homomorphism_basis`, and used in its invocation if
          (re)calculating said basis

        - ``r`` -- integer (default: ``b/4``);  as for
          :meth:`homomorphism_basis`, and used in its invocation if
          (re)calculating said basis

        OUTPUT:

        This returns the combinations of the elements of
        :meth:`homomorphism_basis` that correspond to symplectic
        isomorphisms between the Jacobians of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: f = y^2 - (x^6 + 2*x^4 + 4*x^2 + 8)
            sage: X = RiemannSurface(f, prec=100)
            sage: P = X.period_matrix()
            sage: g = y^2 - (x^6 + x^4 + x^2 + 1)
            sage: Y = RiemannSurface(g, prec=100)
            sage: Q = Y.period_matrix()
            sage: Rs = X.symplectic_isomorphisms(Y)
            sage: Ts = X.tangent_representation_numerical(Rs, other = Y)
            sage: test1 = all(((T*P - Q*R).norm() < 2^(-80)) for [T, R] in zip(Ts, Rs))
            sage: test2 = all(det(R) == 1 for R in Rs)
            sage: test1 and test2
            True
        """
    def symplectic_automorphism_group(self, endo_basis=None, b=None, r=None):
        """
        Numerically compute the symplectic automorphism group as a permutation
        group.

        INPUT:

        - ``endo_basis`` -- (default: ``None``) a `\\ZZ`-basis of the
          endomorphisms of ``self``, as obtained from
          :meth:`endomorphism_basis`. If you have already calculated this
          basis, it saves time to pass it via this keyword argument. Otherwise
          the method will calculate it.

        - ``b`` -- integer (default provided); as for
          :meth:`homomorphism_basis`, and used in its invocation if
          (re)calculating said basis

        - ``r`` -- integer (default: ``b/4``);  as for
          :meth:`homomorphism_basis`, and used in its invocation if
          (re)calculating said basis

        OUTPUT:

        The symplectic automorphism group of the Jacobian of the Riemann
        surface. The automorphism group of the Riemann surface itself can be
        recovered from this; if the curve is hyperelliptic, then it is
        identical, and if not, then one divides out by the central element
        corresponding to multiplication by -1.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: A.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - (x^6 + 2*x^4 + 4*x^2 + 8), prec = 100)
            sage: G = S.symplectic_automorphism_group()
            sage: G.as_permutation_group().is_isomorphic(DihedralGroup(4))
            True
        """
    def __add__(self, other):
        """
        Return the disjoint union of the Riemann surface and the other argument.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface, RiemannSurfaceSum
            sage: R.<x,y> = QQ[]
            sage: S1 = RiemannSurface(y^2-x^3-x-1)
            sage: S1+S1
            Riemann surface sum with period lattice of rank 4
        """
    def abel_jacobi(self, divisor, verbose: bool = False):
        """
        Return the Abel-Jacobi map of ``divisor``.

        Return a representative of the Abel-Jacobi map of a divisor with basepoint
        ``self._basepoint``.

        INPUT:

        - ``divisor`` -- list. A list with each entry a tuple of the form ``(v, P)``,
          where ``v`` is the valuation of the divisor at point ``P``, ``P`` as per
          the input to :meth:`_aj_based`.

        - ``verbose`` -- logical (default: ``False``); whether to report the progress
          of the computation, in terms of how many elements of the list ``divisor``
          have been completed

        OUTPUT: a vector of length ``self.genus``

        EXAMPLES:

        We can test that the Abel-Jacobi map between two branchpoints of a
        superelliptic curve of degree `p` is a `p`-torsion point in the Jacobian::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: p = 4
            sage: S = RiemannSurface(y^p-x^4+1, prec=100)
            sage: divisor = [(-1, (-1, 0)), (1, (1, 0))]
            sage: AJ = S.abel_jacobi(divisor)  # long time (15 seconds)
            sage: AJxp = [p*z for z in AJ]  # long time
            sage: bool(S.reduce_over_period_lattice(AJxp).norm()<1e-7)  # long time
            True
        """
    def reduce_over_period_lattice(self, vector, method: str = 'ip', b=None, r=None, normalised: bool = False):
        """
        Reduce a vector over the period lattice.

        Given a vector of length ``self.genus``, this method returns a vector
        in the same orbit of the period lattice that is short. There are two
        possible methods, ``'svp'`` which returns a certified shortest vector,
        but can be much slower for higher genus curves, and ``'ip'``, which is
        faster but not guaranteed to return the shortest vector. In general the
        latter will perform well when the lattice basis vectors are of similar
        size.

        INPUT:

        - ``vector`` -- vector. A vector of length ``self.genus`` to reduce over
          the lattice

        - ``method`` -- string (default: ``'ip'``) specifying the method
          to use to reduce the vector; the options are ``'ip'`` and ``'svp'``

        - ``b`` -- integer (default provided); as for
          :meth:`homomorphism_basis`, and used in its invocation if
          (re)calculating said basis

        - ``r`` -- integer (default: ``b/4``);  as for
          :meth:`homomorphism_basis`, and used in its invocation if
          (re)calculating said basis

        - ``normalised`` -- logical (default: ``False``); whether to use the
          period matrix with the differentials normalised s.t. the `A`-matrix
          is the identity.

        OUTPUT:

        Complex vector of length ``self.genus`` in the same orbit as ``vector``
        in the lattice.

        EXAMPLES:

        We can check that the lattice basis vectors themselves are reduced to
        zero::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2 - x^5 + 1)
            sage: epsilon = S._RR(2)^(-S._prec+1)
            sage: for vector in S.period_matrix().columns():
            ....:     print(bool(S.reduce_over_period_lattice(vector).norm()<epsilon))
            True
            True
            True
            True

        We can also check that the method ``'svp'`` always gives a smaller norm
        than ``'ip'``::

            sage: for vector in S.period_matrix().columns():
            ....:     n1 = S.reduce_over_period_lattice(vector).norm()
            ....:     n2 = S.reduce_over_period_lattice(vector, method='svp').norm()
            ....:     print(bool(n2<=n1))
            True
            True
            True
            True
        """
    def curve(self):
        """
        Return the curve from which this Riemann surface is obtained.

        Riemann surfaces explicitly obtained from a curve return that same object.
        For others, the curve is constructed and cached, so that an identical curve is
        returned upon subsequent calls.

        OUTPUT: curve from which Riemann surface is obtained

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: C = Curve( y^3+x^3-1)
            sage: S = C.riemann_surface()
            sage: S.curve() is C
            True
        """
    def places_at_branch_locus(self):
        """
        Return the places above the branch locus.

        Return a list of the of places above the branch locus. This must be
        done over the base ring, and so the places are given in terms of the
        factors of the discriminant. Currently, this method only works when
        ``self._R.base_ring() == QQ`` as for other rings, the function field
        for ``Curve(self.f)`` is not implemented. To go from these divisors to
        a divisor list, see :meth:`divisor_to_divisor_list`.

        OUTPUT:

        List of places of the functions field ``Curve(self.f).function_field()``.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(25*(x^4+y^4+1) - 34*(x^2*y^2+x^2+y^2))
            sage: S.places_at_branch_locus()
            [Place (x - 2, (x - 2)*y, y^2 - 17/5, y^3 - 17/5*y),
             Place (x + 2, (x + 2)*y, y^2 - 17/5, y^3 - 17/5*y),
             Place (x - 1/2, (x - 1/2)*y, y^2 - 17/20, y^3 - 17/20*y),
             Place (x + 1/2, (x + 1/2)*y, y^2 - 17/20, y^3 - 17/20*y),
             Place (x^4 - 34/25*x^2 + 1, y, y^2, y^3),
             Place (x^4 - 34/25*x^2 + 1, (x^4 - 34/25*x^2 + 1)*y, y^2 - 34/25*x^2 - 34/25, y^3 + (-34/25*x^2 - 34/25)*y)]
        """
    def strong_approximation(self, divisor, S):
        """
        Apply the method of strong approximation to a divisor.

        As described in [Neu2018]_, apply the method of strong approximation to
        ``divisor`` with list of places to avoid ``S``. Currently, this method
        only works when ``self._R.base_ring() == QQ`` as for other rings, the function
        field for ``Curve(self.f)`` is not implemented.

        INPUT:

        - ``divisor`` -- an element of ``Curve(self.f).function_field().divisor_group()``

        - ``S`` -- list of places to avoid

        OUTPUT:

        A tuple ``(D, B)``, where ``D`` is a new divisor, linearly equivalent
        to ``divisor``, but not intersecting ``S``, and ``B`` is a list of tuples
        ``(v, b)`` where ``b`` are the functions giving the linear equivalence,
        added with multiplicity ``v``.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2-x^3+1)
            sage: avoid = Curve(S.f).places_at_infinity()
            sage: D = 1*avoid[0]
            sage: S.strong_approximation(D, avoid)
            (- Place (x - 2, (x - 2)*y)
              + Place (x - 1, y)
              + Place (x^2 + x + 1, y),
             [(1, (1/(x - 2))*y)])
        """
    def divisor_to_divisor_list(self, divisor, eps=None):
        """
        Turn a divisor into a list for :meth:`abel_jacobi`.

        Given ``divisor`` in ``Curve(self.f).function_field().divisor_group()``,
        consisting of places above finite points in the base, return an equivalent
        divisor list suitable for input into :meth:`abel_jacboi`.

        INPUT:

        - ``divisor`` -- an element of ``Curve(self.f).function_field().divisor_group()``
        - ``eps`` -- real number (optional); tolerance used to determine whether a complex
          number is close enough to a root of a polynomial

        OUTPUT:

        A list with elements of the form ``(v, (z, w))`` representing the finite places.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
            sage: R.<x,y> = QQ[]
            sage: S = RiemannSurface(y^2-x^3+1)
            sage: D = sum(S.places_at_branch_locus())
            sage: S.divisor_to_divisor_list(D)
            [(1, (1.00000000000000, 0.000000000000000)),
             (1, (-0.500000000000000 - 0.866025403784439*I, 0.000000000000000)),
             (1, (-0.500000000000000 + 0.866025403784439*I, 0.000000000000000))]

        .. TODO::

            Currently this method can only handle places above finite points in
            the base. It would be useful to extend this to allow for places at
            infinity.
        """

def integer_matrix_relations(M1, M2, b=None, r=None):
    """
    Determine integer relations between complex matrices.

    Given two square matrices with complex entries of size `g`, `h` respectively,
    numerically determine an (approximate) `\\ZZ`-basis for the `2g \\times 2h` matrices
    with integer entries of the shape `(D, B; C, A)` such that `B+M_1*A=(D+M_1*C)*M2`.
    By considering real and imaginary parts separately we obtain `2gh` equations
    with real coefficients in `4gh` variables. We scale the coefficients by a
    constant `2^b` and round them to integers, in order to obtain an integer
    system of equations. Standard application of LLL allows us to determine near
    solutions.

    The user can specify the parameter `b`, but by default the system will
    choose a `b` based on the size of the coefficients and the precision with
    which they are given.

    INPUT:

    - ``M1`` -- square complex valued matrix

    - ``M2`` -- square complex valued matrix of same size as ``M1``

    - ``b`` -- integer (default provided); the equation coefficients are scaled
      by `2^b` before rounding to integers

    - ``r`` -- integer (default: ``b/4``); the vectors found by LLL that satisfy
      the scaled equations to within `2^r` are reported as solutions

    OUTPUT:

    A list of `2g \\times 2h` integer matrices that, for large enough `r`, `b-r`,
    generate the `\\ZZ`-module of relevant transformations.

    EXAMPLES::

        sage: from sage.schemes.riemann_surfaces.riemann_surface import integer_matrix_relations
        sage: M1 = M2 = matrix(CC, 2, 2, [CC(d).sqrt() for d in [2,-3,-3,-6]])
        sage: T = integer_matrix_relations(M1,M2)
        sage: id = parent(M1)(1)
        sage: M1t = [id.augment(M1) * t for t in T]
        sage: [((m[:,:2]^(-1)*m)[:,2:]-M2).norm() < 1e-13 for m in M1t]
        [True, True]
    """

class RiemannSurfaceSum(RiemannSurface):
    """
    Represent the disjoint union of finitely many Riemann surfaces.

    Rudimentary class to represent disjoint unions of Riemann surfaces. Exists
    mainly (and this is the only functionality actually implemented) to
    represents direct products of the complex tori that arise as analytic
    Jacobians of Riemann surfaces.

    INPUT:

    - ``L`` -- list of RiemannSurface objects

    EXAMPLES::

        sage: _.<x> = QQ[]
        sage: SC = HyperellipticCurve(x^6-2*x^4+3*x^2-7).riemann_surface(prec=60)
        sage: S1 = HyperellipticCurve(x^3-2*x^2+3*x-7).riemann_surface(prec=60)
        sage: S2 = HyperellipticCurve(1-2*x+3*x^2-7*x^3).riemann_surface(prec=60)
        sage: len(SC.homomorphism_basis(S1+S2))
        2
    """
    genus: Incomplete
    PM: Incomplete
    tau: Incomplete
    def __init__(self, L) -> None:
        """
        TESTS::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface, RiemannSurfaceSum
            sage: R.<x,y> = QQ[]
            sage: S1 = RiemannSurface(y^2-x^3-x-1)
            sage: S2 = RiemannSurface(y^2-x^3-x-5)
            sage: S = RiemannSurfaceSum([S1,S2])
            sage: S.riemann_matrix() == S1.riemann_matrix().block_sum(S2.riemann_matrix())
            True
        """
    def period_matrix(self):
        """
        Return the period matrix of the surface.

        This is just the diagonal block matrix constructed from the period
        matrices of the constituents.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface, RiemannSurfaceSum
            sage: R.<x,y> = QQ[]
            sage: S1 = RiemannSurface(y^2-x^3-x-1)
            sage: S2 = RiemannSurface(y^2-x^3-x-5)
            sage: S = RiemannSurfaceSum([S1,S2])
            sage: S1S2 = S1.period_matrix().block_sum(S2.period_matrix())
            sage: S.period_matrix() == S1S2[[0,1],[0,2,1,3]]
            True
        """
    def riemann_matrix(self):
        """
        Return the normalized period matrix of the surface.

        This is just the diagonal block matrix constructed from the Riemann
        matrices of the constituents.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface, RiemannSurfaceSum
            sage: R.<x,y> = QQ[]
            sage: S1 = RiemannSurface(y^2-x^3-x-1)
            sage: S2 = RiemannSurface(y^2-x^3-x-5)
            sage: S = RiemannSurfaceSum([S1,S2])
            sage: S.riemann_matrix() == S1.riemann_matrix().block_sum(S2.riemann_matrix())
            True
        """
    def __add__(self, other):
        """
        Return the disjoint union of the Riemann surface and the other argument.

        EXAMPLES::

            sage: from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface, RiemannSurfaceSum
            sage: R.<x,y> = QQ[]
            sage: S1 = RiemannSurface(y^2-x^3-x-1)
            sage: S1+S1+S1
            Riemann surface sum with period lattice of rank 6
        """
