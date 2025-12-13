from sage.dynamics.arithmetic_dynamics.generic_ds import DynamicalSystem as DynamicalSystem
from sage.dynamics.arithmetic_dynamics.projective_ds import DynamicalSystem_projective as DynamicalSystem_projective
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.schemes.product_projective.morphism import ProductProjectiveSpaces_morphism_ring as ProductProjectiveSpaces_morphism_ring

class DynamicalSystem_product_projective(DynamicalSystem, ProductProjectiveSpaces_morphism_ring):
    """
    The class of dynamical systems on products of projective spaces.

    .. WARNING::

        You should not create objects of this class directly because
        no type or consistency checking is performed. The preferred
        method to construct such dynamical systems is to use
        :func:`~sage.dynamics.arithmetic_dynamics.generic_ds.DynamicalSystem_projective`
        function.

    INPUT:

    - ``polys`` -- list of `n_1 + \\cdots + n_r` multi-homogeneous polynomials, all
      of which should have the same parent

    - ``domain`` -- a projective scheme embedded in
      `P^{n_1-1} \\times \\cdots \\times P^{n_r-1}`

    EXAMPLES::

        sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
        sage: DynamicalSystem_projective([x^2, y^2, z^2, w^2, u^2], domain=T)
        Dynamical System of Product of projective spaces P^2 x P^1 over Rational Field
          Defn: Defined by sending (x : y : z , w : u) to (x^2 : y^2 : z^2 , w^2 : u^2).
    """
    def __init__(self, polys, domain) -> None:
        """
        The Python constructor.

        See :class:`DynamicalSystem` for details.

        EXAMPLES::

            sage: T.<x,y,w,u> = ProductProjectiveSpaces([1, 1], QQ)
            sage: DynamicalSystem_projective([x^2, y^2, w^2, u^2], domain=T)
            Dynamical System of Product of projective spaces P^1 x P^1 over Rational Field
              Defn: Defined by sending (x : y , w : u) to
                    (x^2 : y^2 , w^2 : u^2).
        """
    def nth_iterate(self, P, n, normalize: bool = False):
        """
        Return the ``n``-th iterate of ``P`` by this dynamical system.

        If ``normalize`` is ``True``, then the coordinates are
        automatically normalized.

        .. TODO:: Is there a more efficient way to do this?

        INPUT:

        - ``P`` -- a point in ``self.domain()``

        - ``n`` -- positive integer

        - ``normalize`` -- boolean (default: ``False``)

        OUTPUT: a point in ``self.codomain()``

        EXAMPLES::

            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], QQ)
            sage: f = DynamicalSystem_projective([a^3, b^3 + a*b^2, x^2, y^2 - z^2, z*y],
            ....:                                domain=Z)
            sage: P = Z([1, 1, 1, 1, 1])
            sage: f.nth_iterate(P, 3)
            (1/1872 : 1 , 1 : 1 : 0)

        ::

            sage: Z.<a,b,x,y> = ProductProjectiveSpaces([1, 1], ZZ)
            sage: f = DynamicalSystem_projective([a*b, b^2, x^3 - y^3, y^2*x], domain=Z)
            sage: P = Z([2, 6, 2, 4])
            sage: f.nth_iterate(P, 2, normalize=True)
            (1 : 3 , 407 : 112)
        """
    def orbit(self, P, N, **kwds):
        """
        Return the orbit of `P` by this dynamical system.

        Let `F` be this dynamical system. If `N` is an integer return `[P,F(P),\\ldots,F^N(P)]`.

        If `N` is a list or tuple `N = [m, k]` return
        `[F^m(P),\\ldots,F^k(P)]`.  Automatically normalize the points
        if ``normalize`` is ``True``. Perform the checks on point
        initialize if ``check`` is ``True``.

        INPUT:

        - ``P`` -- a point in ``self.domain()``

        - ``N`` -- nonnegative integer or list or tuple of two nonnegative integers

        kwds:

        - ``check`` -- boolean (default: ``True``)

        - ``normalize`` -- boolean (default: ``False``)

        OUTPUT: list of points in ``self.codomain()``

        EXAMPLES::

            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1, 2], QQ)
            sage: f = DynamicalSystem_projective([a^3, b^3 + a*b^2, x^2, y^2 - z^2, z*y],
            ....:                                domain=Z)
            sage: P = Z([1, 1, 1, 1, 1])
            sage: f.orbit(P, 3)
            [(1 : 1 , 1 : 1 : 1), (1/2 : 1 , 1 : 0 : 1),
             (1/12 : 1 , -1 : 1 : 0), (1/1872 : 1 , 1 : 1 : 0)]

        ::

            sage: Z.<a,b,x,y> = ProductProjectiveSpaces([1, 1], ZZ)
            sage: f = DynamicalSystem_projective([a*b, b^2, x^3 - y^3, y^2*x], domain=Z)
            sage: P = Z([2, 6, 2, 4])
            sage: f.orbit(P, 3, normalize=True)
            [(1 : 3 , 1 : 2), (1 : 3 , -7 : 4),
             (1 : 3 , 407 : 112), (1 : 3 , 66014215 : 5105408)]
        """
    def nth_iterate_map(self, n):
        """
        Return the ``n``-th iterate of this dynamical system.

        ALGORITHM:

        Uses a form of successive squaring to reduce computations.


        .. TODO:: This could be improved.

        INPUT:

        - ``n`` -- positive integer

        OUTPUT: a dynamical system of products of projective spaces

        EXAMPLES::

            sage: Z.<a,b,x,y,z> = ProductProjectiveSpaces([1 , 2], QQ)
            sage: f = DynamicalSystem_projective([a^3, b^3, x^2, y^2, z^2], domain=Z)
            sage: f.nth_iterate_map(3)
            Dynamical System of Product of projective spaces P^1 x P^2 over
            Rational Field
              Defn: Defined by sending (a : b , x : y : z) to
                    (a^27 : b^27 , x^8 : y^8 : z^8).
        """

class DynamicalSystem_product_projective_field(DynamicalSystem_product_projective): ...

class DynamicalSystem_product_projective_finite_field(DynamicalSystem_product_projective_field):
    def cyclegraph(self):
        """
        Return the digraph of all orbits of this morphism mod `p`.

        OUTPUT: a digraph

        EXAMPLES::

            sage: P.<a,b,c,d> = ProductProjectiveSpaces(GF(3), [1,1])
            sage: f = DynamicalSystem_projective([a^2, b^2, c^2, d^2], domain=P)
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 16 vertices

        ::

            sage: P.<a,b,c,d> = ProductProjectiveSpaces(GF(5), [1,1])
            sage: f = DynamicalSystem_projective([a^2, b^2, c, d], domain=P)
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 36 vertices

        ::

            sage: P.<a,b,c,d,e> = ProductProjectiveSpaces(GF(2), [1,2])
            sage: f = DynamicalSystem_projective([a^2, b^2, c, d, e], domain=P)
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 21 vertices

        .. TODO:: Dynamical systems for subschemes of product projective spaces needs work.
                  Thus this is not implemented for subschemes.
        """
