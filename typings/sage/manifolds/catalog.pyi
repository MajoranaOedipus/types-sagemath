def Minkowski(positive_spacelike: bool = True, names=None):
    """
    Generate a Minkowski space of dimension 4.

    By default the signature is set to `(- + + +)`, but can be changed to
    `(+ - - -)` by setting the optional argument ``positive_spacelike`` to
    ``False``. The shortcut operator ``.<,>`` can be used to
    specify the coordinates.

    INPUT:

    - ``positive_spacelike`` -- boolean (default: ``True``); if ``False``, then
      the spacelike vectors yield a negative sign (i.e., the signature
      is `(+ - - - )`)
    - ``names`` -- (default: ``None``) name of the coordinates,
      automatically set by the shortcut operator

    OUTPUT:

    - Lorentzian manifold of dimension 4 with (flat) Minkowskian metric

    EXAMPLES::

        sage: M.<t, x, y, z> = manifolds.Minkowski()
        sage: M.metric()[:]
        [-1  0  0  0]
        [ 0  1  0  0]
        [ 0  0  1  0]
        [ 0  0  0  1]

        sage: M.<t, x, y, z> = manifolds.Minkowski(False)
        sage: M.metric()[:]
        [ 1  0  0  0]
        [ 0 -1  0  0]
        [ 0  0 -1  0]
        [ 0  0  0 -1]
    """
def Kerr(m: int = 1, a: int = 0, coordinates: str = 'BL', names=None):
    """
    Generate a Kerr spacetime.

    A Kerr spacetime is a 4 dimensional manifold describing a rotating black
    hole. Two coordinate systems are implemented: Boyer-Lindquist and Kerr
    (3+1 version).

    The shortcut operator ``.<,>`` can be used to specify the coordinates.

    INPUT:

    - ``m`` -- (default: ``1``) mass of the black hole in natural units
      (`c=1`, `G=1`)
    - ``a`` -- (default: ``0``) angular momentum in natural units; if set to
      ``0``, the resulting spacetime corresponds to a Schwarzschild black hole
    - ``coordinates`` -- (default: ``'BL'``) either ``'BL'`` for
      Boyer-Lindquist coordinates or ``'Kerr'`` for Kerr coordinates (3+1
      version)
    - ``names`` -- (default: ``None``) name of the coordinates,
      automatically set by the shortcut operator

    OUTPUT: Lorentzian manifold

    EXAMPLES::

        sage: m, a = var('m, a')
        sage: K = manifolds.Kerr(m, a)
        sage: K
        4-dimensional Lorentzian manifold M
        sage: K.atlas()
        [Chart (M, (t, r, th, ph))]

    The Kerr metric in Boyer-Lindquist coordinates (cf. :wikipedia:`Kerr_metric`)::

        sage: K.metric().display()
        g = (2*m*r/(a^2*cos(th)^2 + r^2) - 1) dt⊗dt
         - 2*a*m*r*sin(th)^2/(a^2*cos(th)^2 + r^2) dt⊗dph
         + (a^2*cos(th)^2 + r^2)/(a^2 - 2*m*r + r^2) dr⊗dr
         + (a^2*cos(th)^2 + r^2) dth⊗dth
         - 2*a*m*r*sin(th)^2/(a^2*cos(th)^2 + r^2) dph⊗dt
         + (2*a^2*m*r*sin(th)^2/(a^2*cos(th)^2 + r^2) + a^2 + r^2)*sin(th)^2 dph⊗dph

    The Schwarzschild spacetime with the mass parameter set to 1::

        sage: K.<t, r, th, ph> = manifolds.Kerr()
        sage: K
        4-dimensional Lorentzian manifold M
        sage: K.metric().display()
        g = (2/r - 1) dt⊗dt + r^2/(r^2 - 2*r) dr⊗dr
         + r^2 dth⊗dth + r^2*sin(th)^2 dph⊗dph
        sage: K.default_chart().coord_range()
        t: (-oo, +oo); r: (0, +oo); th: (0, pi); ph: [-pi, pi] (periodic)


    The Kerr spacetime in Kerr coordinates::

        sage: m, a = var('m, a')
        sage: K.<t, r, th, ph> = manifolds.Kerr(m, a, coordinates='Kerr')
        sage: K
        4-dimensional Lorentzian manifold M
        sage: K.atlas()
        [Chart (M, (t, r, th, ph))]
        sage: K.metric().display()
        g = (2*m*r/(a^2*cos(th)^2 + r^2) - 1) dt⊗dt
         + 2*m*r/(a^2*cos(th)^2 + r^2) dt⊗dr
         - 2*a*m*r*sin(th)^2/(a^2*cos(th)^2 + r^2) dt⊗dph
         + 2*m*r/(a^2*cos(th)^2 + r^2) dr⊗dt
         + (2*m*r/(a^2*cos(th)^2 + r^2) + 1) dr⊗dr
         - a*(2*m*r/(a^2*cos(th)^2 + r^2) + 1)*sin(th)^2 dr⊗dph
         + (a^2*cos(th)^2 + r^2) dth⊗dth
         - 2*a*m*r*sin(th)^2/(a^2*cos(th)^2 + r^2) dph⊗dt
         - a*(2*m*r/(a^2*cos(th)^2 + r^2) + 1)*sin(th)^2 dph⊗dr
         + (2*a^2*m*r*sin(th)^2/(a^2*cos(th)^2 + r^2)
         + a^2 + r^2)*sin(th)^2 dph⊗dph
        sage: K.default_chart().coord_range()
        t: (-oo, +oo); r: (0, +oo); th: (0, pi); ph: [-pi, pi] (periodic)
    """
def Torus(R: int = 2, r: int = 1, names=None):
    """
    Generate a 2-dimensional torus embedded in Euclidean space.

    The shortcut operator ``.<,>`` can be used to specify the coordinates.

    INPUT:

    - ``R`` -- (default: ``2``) distance form the center to the
      center of the tube
    - ``r`` -- (default: ``1``) radius of the tube
    - ``names`` -- (default: ``None``) name of the coordinates,
      automatically set by the shortcut operator

    OUTPUT: Riemannian manifold

    EXAMPLES::

        sage: T.<theta, phi> = manifolds.Torus(3, 1)
        sage: T
        2-dimensional Riemannian submanifold T embedded in the Euclidean
         space E^3
        sage: T.atlas()
        [Chart (T, (theta, phi))]
        sage: T.embedding().display()
        T → E^3
           (theta, phi) ↦ (X, Y, Z) = ((cos(theta) + 3)*cos(phi),
                                          (cos(theta) + 3)*sin(phi),
                                          sin(theta))
        sage: T.metric().display()
        gamma = dtheta⊗dtheta + (cos(theta)^2 + 6*cos(theta) + 9) dphi⊗dphi
    """
def RealProjectiveSpace(dim: int = 2):
    """
    Generate projective space of dimension ``dim`` over the reals.

    This is the topological space of lines through the origin in
    `\\RR^{d+1}`. The standard atlas consists of `d+2` charts, which sends
    the set `U_i = \\{[x_1, x_2, \\ldots, x_{d+1}] : x_i \\neq 0 \\}` to
    `k^{d}` by dividing by `x_i` and omitting the `i`-th coordinate
    `x_i/x_i = 1`.

    INPUT:

    - ``dim`` -- (default: ``2``) the dimension of projective space

    OUTPUT: ``P`` -- the projective space `\\Bold{RP}^d` where `d =` ``dim``

    EXAMPLES::

        sage: RP2 = manifolds.RealProjectiveSpace(); RP2
        2-dimensional topological manifold RP2
        sage: latex(RP2)
        \\mathbb{RP}^{2}

        sage: C0, C1, C2 = RP2.top_charts()
        sage: p = RP2.point((2,0), chart = C0)
        sage: q = RP2.point((0,3), chart = C0)
        sage: p in C0.domain()
        True
        sage: p in C1.domain()
        True
        sage: C1(p)
        (1/2, 0)
        sage: p in C2.domain()
        False
        sage: q in C0.domain()
        True
        sage: q in C1.domain()
        False
        sage: q in C2.domain()
        True
        sage: C2(q)
        (1/3, 0)

        sage: r = RP2.point((2,3))
        sage: r in C0.domain() and r in C1.domain() and r in C2.domain()
        True
        sage: C0(r)
        (2, 3)
        sage: C1(r)
        (1/2, 3/2)
        sage: C2(r)
        (1/3, 2/3)

        sage: p = RP2.point((2,3), chart = C1)
        sage: p in C0.domain() and p in C1.domain() and p in C2.domain()
        True
        sage: C0(p)
        (1/2, 3/2)
        sage: C2(p)
        (2/3, 1/3)

        sage: RP1 = manifolds.RealProjectiveSpace(1); RP1
        1-dimensional topological manifold RP1
        sage: C0, C1 = RP1.top_charts()
        sage: p, q = RP1.point((2,)), RP1.point((0,))
        sage: p in C0.domain()
        True
        sage: p in C1.domain()
        True
        sage: q in C0.domain()
        True
        sage: q in C1.domain()
        False
        sage: C1(p)
        (1/2,)

        sage: p, q = RP1.point((3,), chart = C1), RP1.point((0,), chart = C1)
        sage: p in C0.domain()
        True
        sage: q in C0.domain()
        False
        sage: C0(p)
        (1/3,)
    """
