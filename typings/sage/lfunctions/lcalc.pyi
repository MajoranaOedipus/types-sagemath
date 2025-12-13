from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.pager import pager as pager
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

prec: int

class LCalc(SageObject):
    '''
    Rubinstein\'s `L`-functions Calculator.

    Type ``lcalc.[tab]`` for a list of useful commands that
    are implemented using the command line interface, but return
    objects that make sense in Sage. For each command the possible
    inputs for the `L`-function are:


    - ``"`` -- (default) the Riemann zeta function

    - ``\'tau\'`` -- the L function of the Ramanujan delta function

    - ``E`` -- an elliptic curve over `\\QQ`; defines `L(E,s)`

    You can also use the complete command-line interface of
    Rubinstein\'s `L`-functions calculations program via this
    class. Type ``lcalc.help()`` for a list of commands and
    how to call them.
    '''
    def __call__(self, args): ...
    def help(self) -> None: ...
    def zeros(self, n, L: str = ''):
        """
        Return the imaginary parts of the first `n` nontrivial
        zeros of the `L`-function in the upper half plane, as
        32-bit reals.

        INPUT:

        - ``n`` -- integer

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        This function also checks the Riemann Hypothesis and makes sure no
        zeros are missed. This means it looks for several dozen zeros to
        make sure none have been missed before outputting any zeros at all,
        so takes longer than
        ``self.zeros_of_zeta_in_interval(...)``.

        EXAMPLES::

            sage: lcalc.zeros(4)                           # long time
            [14.1347251, 21.0220396, 25.0108576, 30.4248761]
            sage: lcalc.zeros(5, L='--tau')                # long time
            [9.22237940, 13.9075499, 17.4427770, 19.6565131, 22.3361036]
            sage: lcalc.zeros(3, EllipticCurve('37a'))     # long time
            [0.000000000, 5.00317001, 6.87039122]
        """
    def zeros_in_interval(self, x, y, stepsize, L: str = ''):
        """
        Return the imaginary parts of (most of) the nontrivial zeros of the
        `L`-function on the line `\\Re(s)=1/2` with positive
        imaginary part between `x` and `y`, along with a
        technical quantity for each.

        INPUT:

        - ``x, y, stepsize`` -- positive floating point numbers

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        OUTPUT: list of pairs (zero, S(T)).

        Rubinstein writes: The first column outputs the imaginary part of
        the zero, the second column a quantity related to `S(T)`
        (it increases roughly by 2 whenever a sign change, i.e. pair of
        zeros, is missed). Higher up the critical strip you should use a
        smaller stepsize so as not to miss zeros.

        EXAMPLES::

            sage: lcalc.zeros_in_interval(10, 30, 0.1)
            [(14.1347251, 0.184672916), (21.0220396, -0.0677893290), (25.0108576, -0.0555872781)]
        """
    def value(self, s, L: str = ''):
        """
        Return `L(s)` for `s` a complex number.

        INPUT:

        - ``s`` -- complex number

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        EXAMPLES::

            sage: I = CC.0
            sage: lcalc.value(0.5 + 100*I)
            2.69261989 - 0.0203860296*I

        Note, Sage can also compute zeta at complex numbers (using the PARI
        C library)::

            sage: (0.5 + 100*I).zeta()
            2.69261988568132 - 0.0203860296025982*I
        """
    def values_along_line(self, s0, s1, number_samples, L: str = ''):
        """
        Return values of `L(s)` at ``number_samples``
        equally-spaced sample points along the line from `s_0` to
        `s_1` in the complex plane.

        INPUT:

        - ``s0, s1`` -- complex numbers

        - ``number_samples`` -- integer

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        OUTPUT: list of pairs `(s, L(s))`, where the `s` are equally spaced
        sampled points on the line from `s_0` to `s_1`

        EXAMPLES::

            sage: I = CC.0
            sage: values = lcalc.values_along_line(0.5, 0.5+20*I, 5)
            sage: values[0][0] # abs tol 1e-8
            0.5
            sage: values[0][1] # abs tol 1e-8
            -1.46035451 + 0.0*I
            sage: values[1][0] # abs tol 1e-8
            0.5 + 4.0*I
            sage: values[1][1] # abs tol 1e-8
            0.606783764 + 0.0911121400*I
            sage: values[2][0] # abs tol 1e-8
            0.5 + 8.0*I
            sage: values[2][1] # abs tol 1e-8
            1.24161511 + 0.360047588*I
            sage: values[3][0] # abs tol 1e-8
            0.5 + 12.0*I
            sage: values[3][1] # abs tol 1e-8
            1.01593665 - 0.745112472*I
            sage: values[4][0] # abs tol 1e-8
            0.5 + 16.0*I
            sage: values[4][1] # abs tol 1e-8
            0.938545408 + 1.21658782*I

        Sometimes warnings are printed (by lcalc) when this command is
        run::

            sage: E = EllipticCurve('389a')
            sage: values = E.lseries().values_along_line(0.5, 3, 5)
            sage: values[0][0] # abs tol 1e-8
            0.0
            sage: values[0][1] # abs tol 1e-8
            0.209951303  + 0.0*I
            sage: values[1][0] # abs tol 1e-8
            0.5
            sage: values[1][1] # abs tol 1e-8
            0.0  + 0.0*I
            sage: values[2][0] # abs tol 1e-8
            1.0
            sage: values[2][1] # abs tol 1e-8
            0.133768433 - 0.0*I
            sage: values[3][0] # abs tol 1e-8
            1.5
            sage: values[3][1] # abs tol 1e-8
            0.360092864 - 0.0*I
            sage: values[4][0] # abs tol 1e-8
            2.0
            sage: values[4][1] # abs tol 1e-8
            0.552975867 + 0.0*I
        """
    def twist_values(self, s, dmin, dmax, L: str = ''):
        """
        Return values of `L(s, \\chi_k)` for each quadratic
        character `\\chi_k` whose discriminant `d` satisfies
        `d_{\\min} \\leq d \\leq d_{\\max}`.

        INPUT:

        - ``s`` -- complex numbers

        - ``dmin`` -- integer

        - ``dmax`` -- integer

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        OUTPUT: list of pairs `(d, L(s,\\chi_d))`

        EXAMPLES::

            sage: values = lcalc.twist_values(0.5, -10, 10)
            sage: values[0][0]
            -8
            sage: values[0][1] # abs tol 1e-8
            1.10042141 + 0.0*I
            sage: values[1][0]
            -7
            sage: values[1][1] # abs tol 1e-8
            1.14658567 + 0.0*I
            sage: values[2][0]
            -4
            sage: values[2][1] # abs tol 1e-8
            0.667691457 + 0.0*I
            sage: values[3][0]
            -3
            sage: values[3][1] # abs tol 1e-8
            0.480867558 + 0.0*I
            sage: values[4][0]
            5
            sage: values[4][1] # abs tol 1e-8
            0.231750947 + 0.0*I
            sage: values[5][0]
            8
            sage: values[5][1] # abs tol 1e-8
            0.373691713 + 0.0*I
        """
    def twist_zeros(self, n, dmin, dmax, L: str = ''):
        """
        Return first `n` real parts of nontrivial zeros for each
        quadratic character `\\chi_k` whose discriminant `d` satisfies
        `d_{\\min} \\leq d \\leq d_{\\max}`.

        INPUT:

        - ``n`` -- integer

        - ``dmin`` -- integer

        - ``dmax`` -- integer

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        OUTPUT: dictionary; keys are the discriminants `d`, and values are list
        of corresponding zeros

        EXAMPLES::

            sage: lcalc.twist_zeros(3, -3, 6)
            {-3: [8.03973716, 11.2492062, 15.7046192], 5: [6.64845335, 9.83144443, 11.9588456]}
        """
    def analytic_rank(self, L: str = ''):
        """
        Return the analytic rank of the `L`-function at the central
        critical point.

        INPUT:

        - ``L`` -- defines `L`-function (default: Riemann zeta function)

        OUTPUT: integer

        .. NOTE::

           Of course this is not provably correct in general, since it
           is an open problem to compute analytic ranks provably
           correctly in general.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: lcalc.analytic_rank(E)
            1
        """

lcalc: Incomplete
