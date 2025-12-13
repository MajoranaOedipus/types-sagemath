import _cython_3_2_1
from sage.categories.category import RRR as RRR, pi as pi
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.rings.complex_mpfr import CCC as CCC, ComplexField as ComplexField
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

Lfunction_from_character: _cython_3_2_1.cython_function_or_method
Lfunction_from_elliptic_curve: _cython_3_2_1.cython_function_or_method

class Lfunction:
    """Lfunction(name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 55)

                Initialization of `L`-function objects.
                See derived class for details, this class is not supposed to be
                instantiated directly.

                EXAMPLES::

                    sage: from sage.libs.lcalc.lcalc_Lfunction import *
                    sage: Lfunction_from_character(DirichletGroup(5)[1])
                    L-function with complex Dirichlet coefficients
        """
    @overload
    def compute_rank(self) -> Any:
        """Lfunction.compute_rank(self)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 227)

        Compute the analytic rank (the order of vanishing at the center) of
        of the `L`-function.

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2] # This is a quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: L.compute_rank()
            0

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: E = EllipticCurve([-82,0])
            sage: L = Lfunction_from_elliptic_curve(E, number_of_coeffs=40000)
            sage: L.compute_rank()
            3"""
    @overload
    def compute_rank(self) -> Any:
        """Lfunction.compute_rank(self)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 227)

        Compute the analytic rank (the order of vanishing at the center) of
        of the `L`-function.

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2] # This is a quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: L.compute_rank()
            0

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: E = EllipticCurve([-82,0])
            sage: L = Lfunction_from_elliptic_curve(E, number_of_coeffs=40000)
            sage: L.compute_rank()
            3"""
    @overload
    def compute_rank(self) -> Any:
        """Lfunction.compute_rank(self)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 227)

        Compute the analytic rank (the order of vanishing at the center) of
        of the `L`-function.

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2] # This is a quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: L.compute_rank()
            0

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: E = EllipticCurve([-82,0])
            sage: L = Lfunction_from_elliptic_curve(E, number_of_coeffs=40000)
            sage: L.compute_rank()
            3"""
    def find_zeros(self, T1, T2, stepsize) -> Any:
        """Lfunction.find_zeros(self, T1, T2, stepsize)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 269)

        Finds zeros on critical line between ``T1`` and ``T2`` using step size
        of stepsize. This function might miss zeros if step size is too
        large. This function computes the zeros of the `L`-function by using
        change in signs of areal valued function whose zeros coincide with
        the zeros of `L`-function.

        Use :meth:`find_zeros_via_N` for slower but more rigorous computation.

        INPUT:

        - ``T1`` -- a real number giving the lower bound
        - ``T2`` -- a real number giving the upper bound
        - ``stepsize`` -- step size to be used for the zero search

        OUTPUT: list of the imaginary parts of the zeros which were found

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2] # This is a quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: L.find_zeros(5,15,.1)
            [6.64845334472..., 9.83144443288..., 11.9588456260...]
            sage: L = Lfunction_from_character(chi, type='double')
            sage: L.find_zeros(1,15,.1)
            [6.64845334472..., 9.83144443288..., 11.9588456260...]

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[1]
            sage: L = Lfunction_from_character(chi, type='complex')
            sage: L.find_zeros(-8,8,.1)
            [-4.13290370521..., 6.18357819545...]

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: L = Lfunction_Zeta()
            sage: L.find_zeros(10,29.1,.1)
            [14.1347251417..., 21.0220396387..., 25.0108575801...]"""
    def find_zeros_via_N(self, count=..., start=..., max_refine=..., rank=...) -> Any:
        """Lfunction.find_zeros_via_N(self, count=0, start=0, max_refine=1025, rank=-1)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 331)

        Find ``count`` zeros (in order of increasing magnitude) and output
        their imaginary parts. This function verifies that no zeros
        are missed, and that all values output are indeed zeros.

        If this `L`-function is self-dual (if its Dirichlet coefficients
        are real, up to a tolerance of 1e-6), then only the zeros with
        positive imaginary parts are output. Their conjugates, which
        are also zeros, are not output.

        INPUT:

        - ``count`` -- number of zeros to be found
        - ``start`` -- (default: 0) how many initial zeros to skip
        - ``max_refine`` -- when some zeros are found to be missing, the step
          size used to find zeros is refined. max_refine gives an upper limit
          on when lcalc should give up. Use default value unless you know
          what you are doing.
        - ``rank`` -- integer (default: -1); analytic rank of the `L`-function.
          If -1 is passed, then we attempt to compute it. (Use default if in
          doubt)

        OUTPUT: list of the imaginary parts of the zeros that have been found

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2] #This is a quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: L.find_zeros_via_N(3)
            [6.64845334472..., 9.83144443288..., 11.9588456260...]
            sage: L = Lfunction_from_character(chi, type='double')
            sage: L.find_zeros_via_N(3)
            [6.64845334472..., 9.83144443288..., 11.9588456260...]

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[1]
            sage: L = Lfunction_from_character(chi, type='complex')
            sage: zeros = L.find_zeros_via_N(3)
            sage: (zeros[0] - (-4.13290370521286)).abs() < 1e-8
            True
            sage: (zeros[1]  - 6.18357819545086).abs() < 1e-8
            True
            sage: (zeros[2]  - 8.45722917442320).abs() < 1e-8
            True

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: L = Lfunction_Zeta()
            sage: L.find_zeros_via_N(3)
            [14.1347251417..., 21.0220396387..., 25.0108575801...]"""
    def hardy_z_function(self, s) -> Any:
        """Lfunction.hardy_z_function(self, s)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 185)

        Compute the Hardy Z-function of the `L`-function at s.

        INPUT:

        - ``s`` -- a complex number with imaginary part between -0.5 and 0.5

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2]  # Quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: (L.hardy_z_function(0) - 0.231750947504).abs() < 1e-8
            True
            sage: L.hardy_z_function(0.5).imag().abs() < 1e-8
            True

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[1]
            sage: L = Lfunction_from_character(chi, type='complex')
            sage: (L.hardy_z_function(0) - 0.793967590477).abs() < 1e-8
            True
            sage: L.hardy_z_function(0.5).imag().abs() < 1e-8
            True

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: E = EllipticCurve([-82,0])
            sage: L = Lfunction_from_elliptic_curve(E, number_of_coeffs=40000)
            sage: (L.hardy_z_function(2.1) - (-0.006431791768)).abs() < 1e-8
            True"""
    def value(self, s, derivative=...) -> Any:
        """Lfunction.value(self, s, derivative=0)

        File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 129)

        Compute the value of the `L`-function at ``s``.

        INPUT:

        - ``s`` -- a complex number
        - ``derivative`` -- integer (default: 0);  the derivative to be evaluated
        - ``rotate`` -- boolean (default: ``False``); if True, this returns the value of the
          Hardy Z-function (sometimes called the Riemann-Siegel Z-function or
          the Siegel Z-function)

        EXAMPLES::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[2] # This is a quadratic character
            sage: L = Lfunction_from_character(chi, type='int')
            sage: (L.value(0.5) - 0.231750947504016).abs() < 1e-8
            True
            sage: v = L.value(0.2 + 0.4*I)
            sage: (v - (0.102558603193 + 0.190840777924*I)).abs() < 1e-8
            True
            sage: L = Lfunction_from_character(chi, type='double')
            sage: (L.value(0.6) - 0.274633355856345).abs() < 1e-8
            True
            sage: v = L.value(0.6 + I)
            sage: (v - (0.362258705721 + 0.43388825062*I)).abs() < 1e-8
            True

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: chi = DirichletGroup(5)[1]
            sage: L = Lfunction_from_character(chi, type='complex')
            sage: v = L.value(0.5)
            sage: (v - (0.763747880117 + 0.21696476751*I)).abs() < 1e-8
            True
            sage: v = L.value(0.6 + 5*I)
            sage: (v - (0.702723260619 - 1.10178575243*I)).abs() < 1e-8
            True

        ::

            sage: from sage.libs.lcalc.lcalc_Lfunction import *
            sage: L = Lfunction_Zeta()
            sage: (L.value(0.5) + 1.46035450880).abs() < 1e-8
            True
            sage: v = L.value(0.4 + 0.5*I)
            sage: (v - (-0.450728958517 - 0.780511403019*I)).abs() < 1e-8
            True"""

class Lfunction_C(Lfunction):
    """Lfunction_C(name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue)

    File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 702)

    The ``Lfunction_C`` class is used to represent `L`-functions
    with complex Dirichlet Coefficients. We assume that `L`-functions
    satisfy the following functional equation.

    .. MATH::

        \\Lambda(s) = \\omega Q^s \\overline{\\Lambda(1-\\bar s)}

    where

    .. MATH::

        \\Lambda(s) = Q^s \\left( \\prod_{j=1}^a \\Gamma(\\kappa_j s + \\gamma_j) \\right) L(s)

    See (23) in :arxiv:`math/0412181`

    INPUT:

    - ``what_type_L`` -- integer; this should be set to 1 if the coefficients are
      periodic and 0 otherwise

    - ``dirichlet_coefficient`` -- list of Dirichlet coefficients of the
      `L`-function. Only first `M` coefficients are needed if they are periodic.

    - ``period`` -- if the coefficients are periodic, this should be the
      period of the coefficients

    - ``Q`` -- see above

    - ``OMEGA`` -- see above

    - ``kappa`` -- list of the values of `\\kappa_j` in the functional equation

    - ``gamma`` -- list of the values of `\\gamma_j` in the functional equation

    - ``pole`` -- list of the poles of `L`-function

    - ``residue`` -- list of the residues of the `L`-function

    .. NOTE::

        If an `L`-function satisfies `\\Lambda(s) = \\omega Q^s \\Lambda(k-s)`,
        by replacing `s` by `s+(k-1)/2`, one can get it in the form we need."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 749)

                Initialize an `L`-function with complex coefficients.

                EXAMPLES::

                    sage: from sage.libs.lcalc.lcalc_Lfunction import *
                    sage: chi = DirichletGroup(5)[1]
                    sage: L=Lfunction_from_character(chi, type='complex')
                    sage: type(L)
                    <class 'sage.libs.lcalc.lcalc_Lfunction.Lfunction_C'>
        """

class Lfunction_D(Lfunction):
    """Lfunction_D(name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue)

    File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 565)

    The ``Lfunction_D`` class is used to represent `L`-functions
    with real Dirichlet coefficients. We assume that `L`-functions
    satisfy the following functional equation.

    .. MATH::

        \\Lambda(s) = \\omega Q^s \\overline{\\Lambda(1-\\bar s)}

    where

    .. MATH::

        \\Lambda(s) = Q^s \\left( \\prod_{j=1}^a \\Gamma(\\kappa_j s + \\gamma_j) \\right) L(s)

    See (23) in :arxiv:`math/0412181`

    INPUT:

    - ``what_type_L`` -- integer; this should be set to 1 if the coefficients are
      periodic and 0 otherwise

    - ``dirichlet_coefficient`` -- list of Dirichlet coefficients of the
      `L`-function. Only first `M` coefficients are needed if they are periodic.

    - ``period`` -- if the coefficients are periodic, this should be the
      period of the coefficients

    - ``Q`` -- see above

    - ``OMEGA`` -- see above

    - ``kappa`` -- list of the values of `\\kappa_j` in the functional equation

    - ``gamma`` -- list of the values of `\\gamma_j` in the functional equation

    - ``pole`` -- list of the poles of `L`-function

    - ``residue`` -- list of the residues of the `L`-function

    .. NOTE::

        If an `L`-function satisfies `\\Lambda(s) = \\omega Q^s \\Lambda(k-s)`,
        by replacing `s` by `s+(k-1)/2`, one can get it in the form we need."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 611)

                Initialize an `L`-function with real coefficients.

                EXAMPLES::

                    sage: from sage.libs.lcalc.lcalc_Lfunction import *
                    sage: chi = DirichletGroup(5)[2] #This is a quadratic character
                    sage: L=Lfunction_from_character(chi, type='double')
                    sage: type(L)
                    <class 'sage.libs.lcalc.lcalc_Lfunction.Lfunction_D'>
        """

class Lfunction_I(Lfunction):
    """Lfunction_I(name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue)

    File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 428)

    The ``Lfunction_I`` class is used to represent `L`-functions
    with integer Dirichlet Coefficients. We assume that `L`-functions
    satisfy the following functional equation.

    .. MATH::

        \\Lambda(s) = \\omega Q^s \\overline{\\Lambda(1-\\bar s)}

    where

    .. MATH::

        \\Lambda(s) = Q^s \\left( \\prod_{j=1}^a \\Gamma(\\kappa_j s + \\gamma_j) \\right) L(s)

    See (23) in :arxiv:`math/0412181`

    INPUT:

    - ``what_type_L`` -- integer; this should be set to 1 if the coefficients
      are periodic and 0 otherwise

    - ``dirichlet_coefficient`` -- list of Dirichlet coefficients of the
      `L`-function. Only first `M` coefficients are needed if they are periodic.

    - ``period`` -- if the coefficients are periodic, this should be the
      period of the coefficients

    - ``Q`` -- see above

    - ``OMEGA`` -- see above

    - ``kappa`` -- list of the values of `\\kappa_j` in the functional equation

    - ``gamma`` -- list of the values of `\\gamma_j` in the functional equation

    - ``pole`` -- list of the poles of `L`-function

    - ``residue`` -- list of the residues of the `L`-function

    .. NOTE::

         If an `L`-function satisfies `\\Lambda(s) = \\omega Q^s \\Lambda(k-s)`,
         by replacing `s` by `s+(k-1)/2`, one can get it in the form we need."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, name, what_type_L, dirichlet_coefficient, period, Q, OMEGA, gamma, lambd, pole, residue) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 475)

                Initialize an `L`-function with integer coefficients.

                EXAMPLES::

                    sage: from sage.libs.lcalc.lcalc_Lfunction import *
                    sage: chi = DirichletGroup(5)[2] #This is a quadratic character
                    sage: L=Lfunction_from_character(chi, type='int')
                    sage: type(L)
                    <class 'sage.libs.lcalc.lcalc_Lfunction.Lfunction_I'>
        """

class Lfunction_Zeta(Lfunction):
    """Lfunction_Zeta()

    File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 845)

    The ``Lfunction_Zeta`` class is used to generate the Riemann zeta function."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/lcalc/lcalc_Lfunction.pyx (starting at line 849)

                Initialize the Riemann zeta function.

                EXAMPLES::

                    sage: from sage.libs.lcalc.lcalc_Lfunction import *
                    sage: sage.libs.lcalc.lcalc_Lfunction.Lfunction_Zeta()
                    The Riemann zeta function
        """
