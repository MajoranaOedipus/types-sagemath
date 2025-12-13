from _typeshed import Incomplete
from sage.homology.free_resolution import FiniteFreeResolution as FiniteFreeResolution, FiniteFreeResolution_free_module as FiniteFreeResolution_free_module, FiniteFreeResolution_singular as FiniteFreeResolution_singular
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.modules.free_module import Module_free_ambient as Module_free_ambient
from sage.modules.free_module_element import vector as vector
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.structure.element import Matrix as Matrix

class GradedFiniteFreeResolution(FiniteFreeResolution):
    """
    Graded finite free resolutions.

    INPUT:

    - ``module`` -- a homogeneous submodule of a free module `M` of rank `n`
      over `S` or a homogeneous ideal of a multivariate polynomial ring `S`

    - ``degrees`` -- (default: a list with all entries `1`) a list of integers
      or integer vectors giving degrees of variables of `S`

    - ``shifts`` -- list of integers or integer vectors giving shifts of
      degrees of `n` summands of the free module `M`; this is a list of zero
      degrees of length `n` by default

    - ``name`` -- string; name of the base ring
    """
    def __init__(self, module, degrees=None, shifts=None, name: str = 'S', **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: TestSuite(r).run(skip=['_test_pickling'])

        An overdetermined system over a PID::

            sage: from sage.homology.free_resolution import FreeResolution
            sage: M = matrix([[x^2, 2*x^2],
            ....:             [3*x^2, 5*x^2],
            ....:             [5*x^2, 4*x^2]])
            sage: res = FreeResolution(M, graded=True); res
            S(0)⊕S(0) <-- S(-2)⊕S(-2) <-- 0
            sage: res._res_shifts
            [[2, 2]]
        """
    def shifts(self, i):
        """
        Return the shifts of ``self``.

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: r.shifts(0)
            [0]
            sage: r.shifts(1)
            [2, 2, 2]
            sage: r.shifts(2)
            [3, 3]
            sage: r.shifts(3)
            []
        """
    def betti(self, i, a=None):
        """
        Return the `i`-th Betti number in degree `a`.

        INPUT:

        - ``i`` -- nonnegative integer

        - ``a`` -- a degree; if ``None``, return Betti numbers in all degrees

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: r.betti(0)
            {0: 1}
            sage: r.betti(1)
            {2: 3}
            sage: r.betti(2)
            {3: 2}
            sage: r.betti(1, 0)
            0
            sage: r.betti(1, 1)
            0
            sage: r.betti(1, 2)
            3
        """
    def K_polynomial(self, names=None):
        """
        Return the K-polynomial of this resolution.

        INPUT:

        - ``names`` -- (optional) a string of names of the variables
          of the K-polynomial

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: r.K_polynomial()
            2*t^3 - 3*t^2 + 1
        """

class GradedFiniteFreeResolution_free_module(GradedFiniteFreeResolution, FiniteFreeResolution_free_module):
    """
    Graded free resolution of free modules.

    EXAMPLES::

        sage: from sage.homology.free_resolution import FreeResolution
        sage: R.<x> = QQ[]
        sage: M = matrix([[x^3, 3*x^3, 5*x^3],
        ....:             [0, x, 2*x]])
        sage: res = FreeResolution(M, graded=True); res
        S(0)⊕S(0)⊕S(0) <-- S(-3)⊕S(-1) <-- 0
    """
    def __init__(self, module, degrees=None, *args, **kwds) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.homology.free_resolution import FreeResolution
            sage: R.<x> = QQ[]
            sage: M = matrix([[x^3, 3*x^3, 5*x^3],
            ....:             [0, x, 2*x]])
            sage: res = FreeResolution(M, graded=True)
            sage: TestSuite(res).run(skip='_test_pickling')
        """

class GradedFiniteFreeResolution_singular(GradedFiniteFreeResolution, FiniteFreeResolution_singular):
    """
    Graded free resolutions of submodules and ideals of multivariate
    polynomial rings implemented using Singular.

    INPUT:

    - ``module`` -- a homogeneous submodule of a free module `M` of rank `n`
      over `S` or a homogeneous ideal of a multivariate polynomial ring `S`

    - ``degrees`` -- (default: a list with all entries `1`) a list of integers
      or integer vectors giving degrees of variables of `S`

    - ``shifts`` -- list of integers or integer vectors giving shifts of
      degrees of `n` summands of the free module `M`; this is a list of zero
      degrees of length `n` by default

    - ``name`` -- string; name of the base ring

    - ``algorithm`` -- Singular algorithm to compute a resolution of ``ideal``

    OUTPUT: a graded minimal free resolution of ``ideal``

    If ``module`` is an ideal of `S`, it is considered as a submodule of a free
    module of rank `1` over `S`.

    The degrees given to the variables of `S` are integers or integer vectors of
    the same length. In the latter case, `S` is said to be multigraded, and the
    resolution is a multigraded free resolution. The standard grading where all
    variables have degree `1` is used if the degrees are not specified.

    A summand of the graded free module `M` is a shifted (or twisted) module of
    rank one over `S`, denoted `S(-d)` with shift `d`.

    The computation of the resolution is done by using ``libSingular``.
    Different Singular algorithms can be chosen for best performance. The
    available algorithms and the corresponding Singular commands are shown
    below:

    ============= ============================
    algorithm     Singular commands
    ============= ============================
    ``minimal``   ``mres(ideal)``
    ``shreyer``   ``minres(sres(std(ideal)))``
    ``standard``  ``minres(nres(std(ideal)))``
    ``heuristic`` ``minres(res(std(ideal)))``
    ============= ============================

    EXAMPLES::

        sage: S.<x,y,z,w> = PolynomialRing(QQ)
        sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
        sage: r = I.graded_free_resolution(); r
        S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
        sage: len(r)
        2

        sage: I = S.ideal([z^2 - y*w, y*z - x*w, y - x])
        sage: I.is_homogeneous()
        True
        sage: r = I.graded_free_resolution(); r
        S(0) <-- S(-1)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3)⊕S(-4) <-- S(-5) <-- 0
    """
    def __init__(self, module, degrees=None, shifts=None, name: str = 'S', algorithm: str = 'heuristic', **kwds) -> None:
        """
        Initialize.

        TESTS::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: TestSuite(r).run(skip=['_test_pickling'])
        """

GradedFreeResolution: Incomplete
