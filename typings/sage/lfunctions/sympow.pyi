from _typeshed import Incomplete
from sage.misc.pager import pager as pager
from sage.misc.verbose import verbose as verbose
from sage.rings.integer import Integer as Integer
from sage.structure.sage_object import SageObject as SageObject

class Sympow(SageObject):
    """
    Watkins Symmetric Power `L`-function Calculator.

    Type ``sympow.[tab]`` for a list of useful commands
    that are implemented using the command line interface, but return
    objects that make sense in Sage.

    You can also use the complete command-line interface of sympow via
    this class. Type ``sympow.help()`` for a list of
    commands and how to call them.
    """
    def __call__(self, args):
        """
        Used to call sympow with given args
        """
    def L(self, E, n, prec):
        """
        Return `L(\\mathrm{Sym}^{(n)}(E, \\text{edge}))` to prec digits of
        precision, where edge is the *right* edge. Here `n` must be
        even.

        INPUT:

        - ``E`` -- elliptic curve

        - ``n`` -- even integer

        - ``prec`` -- integer

        OUTPUT: real number to prec digits of precision as a string

        .. NOTE::

           Before using this function for the first time for a given
           `n`, you may have to type ``sympow('-new_data n')``,
           where ``n`` is replaced by your value of `n`.

        If you would like to see the extensive output sympow prints when
        running this function, just type ``set_verbose(2)``.

        EXAMPLES:

        These examples only work if you run ``sympow -new_data 2`` in a
        Sage shell first. Alternatively, within Sage, execute::

            sage: sympow('-new_data 2')  # not tested

        This command precomputes some data needed for the following
        examples. ::

            sage: a = sympow.L(EllipticCurve('11a'), 2, 16)  # not tested
            sage: a                                          # not tested
            '1.057599244590958E+00'
            sage: RR(a)                                      # not tested
            1.05759924459096
        """
    def Lderivs(self, E, n, prec, d):
        """
        Return `0`-th to `d`-th derivatives of
        `L(\\mathrm{Sym}^{(n)}(E,s)` to prec digits of precision, where
        `s` is the right edge if `n` is even and the center
        if `n` is odd.

        INPUT:

        - ``E`` -- elliptic curve

        - ``n`` -- integer (even or odd)

        - ``prec`` -- integer

        - ``d`` -- integer

        OUTPUT: string, exactly as output by sympow

        .. NOTE::

           To use this function you may have to run a few commands
           like ``sympow('-new_data 1d2')``, each which takes a
           few minutes. If this function fails it will indicate what commands
           have to be run.

        EXAMPLES::

            sage: print(sympow.Lderivs(EllipticCurve('11a'), 1, 16, 2))  # not tested
            ...
             1n0: 2.538418608559107E-01
             1w0: 2.538418608559108E-01
             1n1: 1.032321840884568E-01
             1w1: 1.059251499158892E-01
             1n2: 3.238743180659171E-02
             1w2: 3.414818600982502E-02
        """
    def modular_degree(self, E):
        """
        Return the modular degree of the elliptic curve E, assuming the
        Stevens conjecture.

        INPUT:

        - ``E`` -- elliptic curve over Q

        OUTPUT:

        - ``integer`` -- modular degree

        EXAMPLES: We compute the modular degrees of the lowest known
        conductor curves of the first few ranks::

            sage: sympow.modular_degree(EllipticCurve('11a'))
            1
            sage: sympow.modular_degree(EllipticCurve('37a'))
            2
            sage: sympow.modular_degree(EllipticCurve('389a'))
            40
            sage: sympow.modular_degree(EllipticCurve('5077a'))
            1984
            sage: sympow.modular_degree(EllipticCurve([1, -1, 0, -79, 289]))
            334976
        """
    def analytic_rank(self, E):
        """
        Return the analytic rank and leading `L`-value of the
        elliptic curve `E`.

        INPUT:

        - ``E`` -- elliptic curve over Q

        OUTPUT:

        - ``integer`` -- analytic rank

        - ``string`` -- leading coefficient (as string)


        .. NOTE::

           The analytic rank is *not* computed provably correctly in general.

        .. NOTE::

           In computing the analytic rank we consider
           `L^{(r)}(E,1)` to be `0` if
           `L^{(r)}(E,1)/\\Omega_E > 0.0001`.

        EXAMPLES: We compute the analytic ranks of the lowest known
        conductor curves of the first few ranks::

            sage: sympow.analytic_rank(EllipticCurve('11a'))
            (0, '2.53842e-01')
            sage: sympow.analytic_rank(EllipticCurve('37a'))
            (1, '3.06000e-01')
            sage: sympow.analytic_rank(EllipticCurve('389a'))
            (2, '7.59317e-01')
            sage: sympow.analytic_rank(EllipticCurve('5077a'))
            (3, '1.73185e+00')
            sage: sympow.analytic_rank(EllipticCurve([1, -1, 0, -79, 289]))
            (4, '8.94385e+00')
            sage: sympow.analytic_rank(EllipticCurve([0, 0, 1, -79, 342]))  # long time
            (5, '3.02857e+01')
            sage: sympow.analytic_rank(EllipticCurve([1, 1, 0, -2582, 48720]))  # long time
            (6, '3.20781e+02')
            sage: sympow.analytic_rank(EllipticCurve([0, 0, 0, -10012, 346900]))  # long time
            (7, '1.32517e+03')
        """
    def new_data(self, n) -> None:
        """
        Pre-compute data files needed for computation of `n`-th symmetric
        powers.
        """
    def help(self) -> None: ...

sympow: Incomplete
