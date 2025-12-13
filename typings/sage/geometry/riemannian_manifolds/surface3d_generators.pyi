from _typeshed import Incomplete
from sage.functions.hyperbolic import cosh as cosh, tanh as tanh
from sage.functions.log import log as log
from sage.functions.trig import cos as cos, sin as sin, tan as tan
from sage.geometry.riemannian_manifolds.parametrized_surface3d import ParametrizedSurface3D as ParametrizedSurface3D
from sage.symbolic.constants import pi as pi
from sage.symbolic.ring import var as var

class SurfaceGenerators:
    """
    A class consisting of generators for several common parametrized surfaces
    in 3D.
    """
    @staticmethod
    def Catenoid(c: int = 1, name: str = 'Catenoid'):
        """
        Return a catenoid surface, with parametric representation.

        .. MATH::

            \\begin{aligned}
              x(u, v) & = c \\cosh(v/c) \\cos(u); \\\\\n              y(u, v) & = c \\cosh(v/c) \\sin(u); \\\\\n              z(u, v) & = v.
            \\end{aligned}

        INPUT:

        - ``c`` -- surface parameter

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Catenoid`.

        EXAMPLES::

            sage: cat = surfaces.Catenoid(); cat
            Parametrized surface ('Catenoid') with equation (cos(u)*cosh(v), cosh(v)*sin(u), v)
            sage: cat.plot()                                                            # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Crosscap(r: int = 1, name: str = 'Crosscap'):
        """
        Return a crosscap surface, with parametrization.

        .. MATH::

            \\begin{aligned}
              x(u, v) & = r(1 + \\cos(v)) \\cos(u); \\\\\n              y(u, v) & = r(1 + \\cos(v)) \\sin(u); \\\\\n              z(u, v) & = - r\\tanh(u - \\pi) \\sin(v).
            \\end{aligned}

        INPUT:

        - ``r`` -- surface parameter

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Cross-cap`.

        EXAMPLES::

            sage: crosscap = surfaces.Crosscap(); crosscap
            Parametrized surface ('Crosscap') with equation ((cos(v) + 1)*cos(u), (cos(v) + 1)*sin(u), -sin(v)*tanh(-pi + u))
            sage: crosscap.plot()                                                       # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Dini(a: int = 1, b: int = 1, name: str = "Dini's surface"):
        """
        Return Dini's surface, with parametrization.

        .. MATH::

            \\begin{aligned}
              x(u, v) & = a \\cos(u)\\sin(v); \\\\\n              y(u, v) & = a \\sin(u)\\sin(v); \\\\\n              z(u, v) & = u + \\log(\\tan(v/2)) + \\cos(v).
            \\end{aligned}

        INPUT:

        - ``a``, ``b`` -- surface parameters

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Dini%27s_surface`.

        EXAMPLES::

            sage: dini = surfaces.Dini(a=3, b=4); dini
            Parametrized surface ('Dini's surface') with equation (3*cos(u)*sin(v), 3*sin(u)*sin(v), 4*u + 3*cos(v) + 3*log(tan(1/2*v)))
            sage: dini.plot()                                                           # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Ellipsoid(center=(0, 0, 0), axes=(1, 1, 1), name: str = 'Ellipsoid'):
        """
        Return an ellipsoid centered at ``center`` whose semi-principal axes
        have lengths given by the components of ``axes``. The
        parametrization of the ellipsoid is given by

        .. MATH::

            \\begin{aligned}
              x(u, v) & = x_0 + a \\cos(u) \\cos(v); \\\\\n              y(u, v) & = y_0 + b \\sin(u) \\cos(v); \\\\\n              z(u, v) & = z_0 + c \\sin(v).
            \\end{aligned}

        INPUT:

        - ``center`` -- 3-tuple; coordinates of the center of the ellipsoid

        - ``axes`` -- 3-tuple; lengths of the semi-principal axes

        - ``name`` -- string; name of the ellipsoid

        For more information, see :wikipedia:`Ellipsoid`.

        EXAMPLES::

            sage: ell = surfaces.Ellipsoid(axes=(1, 2, 3)); ell
            Parametrized surface ('Ellipsoid') with equation (cos(u)*cos(v), 2*cos(v)*sin(u), 3*sin(v))
            sage: ell.plot()                                                            # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Enneper(name: str = "Enneper's surface"):
        """
        Return Enneper's surface, with parametrization.

        .. MATH::

            \\begin{aligned}
              x(u, v) & = u(1 - u^2/3 + v^2)/3; \\\\\n              y(u, v) & = -v(1 - v^2/3 + u^2)/3; \\\\\n              z(u, v) & = (u^2 - v^2)/3.
            \\end{aligned}

        INPUT:

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Enneper_surface`.

        EXAMPLES::

            sage: enn = surfaces.Enneper(); enn
            Parametrized surface ('Enneper's surface') with equation (-1/9*(u^2 - 3*v^2 - 3)*u, -1/9*(3*u^2 - v^2 + 3)*v, 1/3*u^2 - 1/3*v^2)
            sage: enn.plot()                                                            # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Helicoid(h: int = 1, name: str = 'Helicoid'):
        """
        Return a helicoid surface, with parametrization.

        .. MATH::

            \\begin{aligned}
              x(\\rho, \\theta) & = \\rho \\cos(\\theta); \\\\\n              y(\\rho, \\theta) & = \\rho \\sin(\\theta); \\\\\n              z(\\rho, \\theta) & = h\\theta/(2\\pi).
            \\end{aligned}

        INPUT:

        - ``h`` -- distance along the z-axis between two
          successive turns of the helicoid

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Helicoid`.

        EXAMPLES::

            sage: helicoid = surfaces.Helicoid(h=2); helicoid
            Parametrized surface ('Helicoid') with equation (rho*cos(theta), rho*sin(theta), theta/pi)
            sage: helicoid.plot()                                                       # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Klein(r: int = 1, name: str = 'Klein bottle'):
        '''
        Return the Klein bottle, in the figure-8 parametrization given by

        .. MATH::

            \\begin{aligned}
              x(u, v) & = (r + \\cos(u/2)\\cos(v) - \\sin(u/2)\\sin(2v)) \\cos(u); \\\\\n              y(u, v) & = (r + \\cos(u/2)\\cos(v) - \\sin(u/2)\\sin(2v)) \\sin(u); \\\\\n              z(u, v) & = \\sin(u/2)\\cos(v) + \\cos(u/2)\\sin(2v).
            \\end{aligned}

        INPUT:

        - ``r`` -- radius of the "figure-8" circle

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Klein_bottle`.

        EXAMPLES::

            sage: klein = surfaces.Klein(); klein
            Parametrized surface (\'Klein bottle\') with equation (-(sin(1/2*u)*sin(2*v) - cos(1/2*u)*sin(v) - 1)*cos(u), -(sin(1/2*u)*sin(2*v) - cos(1/2*u)*sin(v) - 1)*sin(u), cos(1/2*u)*sin(2*v) + sin(1/2*u)*sin(v))
            sage: klein.plot()                                                          # needs sage.plot
            Graphics3d Object
        '''
    @staticmethod
    def MonkeySaddle(name: str = 'Monkey saddle'):
        """
        Return a monkey saddle surface, with equation

        .. MATH::

            z = x^3 - 3xy^2.

        INPUT:

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Monkey_saddle`.

        EXAMPLES::

            sage: saddle = surfaces.MonkeySaddle(); saddle
            Parametrized surface ('Monkey saddle') with equation (u, v, u^3 - 3*u*v^2)
            sage: saddle.plot()                                                         # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Paraboloid(a: int = 1, b: int = 1, c: int = 1, elliptic: bool = True, name=None):
        """
        Return a paraboloid with equation.

        .. MATH::

            \\frac{z}{c} = \\pm \\frac{x^2}{a^2} + \\frac{y^2}{b^2}

        When the plus sign is selected, the paraboloid is elliptic. Otherwise
        the surface is a hyperbolic paraboloid.

        INPUT:

        - ``a``, ``b``, ``c`` -- surface parameters

        - ``elliptic`` -- boolean (default: ``True``); whether to create an
          elliptic or hyperbolic paraboloid

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Paraboloid`.

        EXAMPLES::

            sage: epar = surfaces.Paraboloid(1, 3, 2); epar
            Parametrized surface ('Elliptic paraboloid') with equation (u, v, 2*u^2 + 2/9*v^2)
            sage: epar.plot()                                                           # needs sage.plot
            Graphics3d Object

            sage: hpar = surfaces.Paraboloid(2, 3, 1, elliptic=False); hpar
            Parametrized surface ('Hyperbolic paraboloid') with equation (u, v, -1/4*u^2 + 1/9*v^2)
            sage: hpar.plot()                                                           # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Sphere(center=(0, 0, 0), R: int = 1, name: str = 'Sphere'):
        """
        Return a sphere of radius ``R`` centered at ``center``.

        INPUT:

        - ``center`` -- 3-tuple; center of the sphere

        - ``R`` -- radius of the sphere

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Sphere`.

        EXAMPLES::

            sage: sphere = surfaces.Sphere(center=(0, 1, -1), R=2); sphere
            Parametrized surface ('Sphere') with equation (2*cos(u)*cos(v), 2*cos(v)*sin(u) + 1, 2*sin(v) - 1)
            sage: sphere.plot()                                                         # needs sage.plot
            Graphics3d Object

        Note that the radius of the sphere can be negative. The surface thus
        obtained is equal to the sphere (or part thereof) with positive radius,
        whose coordinate functions have been multiplied by -1. Compare for
        instant the first octant of the unit sphere with positive radius::

            sage: octant1 = surfaces.Sphere(R=1); octant1
            Parametrized surface ('Sphere') with equation (cos(u)*cos(v), cos(v)*sin(u), sin(v))
            sage: octant1.plot((0, pi/2), (0, pi/2))                                    # needs sage.plot
            Graphics3d Object

        with the first octant of the unit sphere with negative radius::

            sage: octant2 = surfaces.Sphere(R=-1); octant2
            Parametrized surface ('Sphere') with equation (-cos(u)*cos(v), -cos(v)*sin(u), -sin(v))
            sage: octant2.plot((0, pi/2), (0, pi/2))                                    # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def Torus(r: int = 2, R: int = 3, name: str = 'Torus'):
        """
        Return a torus obtained by revolving a circle of radius ``r`` around
        a coplanar axis ``R`` units away from the center of the circle. The
        parametrization used is

        .. MATH::

            \\begin{aligned}
              x(u, v) & = (R + r \\cos(v)) \\cos(u); \\\\\n              y(u, v) & = (R + r \\cos(v)) \\sin(u); \\\\\n              z(u, v) & = r \\sin(v).
            \\end{aligned}

        INPUT:

        - ``r``, ``R`` -- minor and major radius of the torus

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Torus`.

        EXAMPLES::

            sage: torus = surfaces.Torus(); torus
            Parametrized surface ('Torus') with equation ((2*cos(v) + 3)*cos(u), (2*cos(v) + 3)*sin(u), 2*sin(v))
            sage: torus.plot()                                                          # needs sage.plot
            Graphics3d Object
        """
    @staticmethod
    def WhitneyUmbrella(name: str = "Whitney's umbrella"):
        """
        Return Whitney's umbrella, with parametric representation

        .. MATH::

            x(u, v) = uv, \\quad y(u, v) = u, \\quad z(u, v) = v^2.

        INPUT:

        - ``name`` -- string; name of the surface

        For more information, see :wikipedia:`Whitney_umbrella`.

        EXAMPLES::

            sage: whitney = surfaces.WhitneyUmbrella(); whitney
            Parametrized surface ('Whitney's umbrella') with equation (u*v, u, v^2)
            sage: whitney.plot()                                                        # needs sage.plot
            Graphics3d Object
        """

surfaces: Incomplete
