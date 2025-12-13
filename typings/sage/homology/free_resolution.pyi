from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.modules.free_module import FreeModule as FreeModule, FreeModule_generic as FreeModule_generic, Module_free_ambient as Module_free_ambient
from sage.modules.free_module_element import vector as vector
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.structure.element import Matrix as Matrix
from sage.structure.sage_object import SageObject as SageObject

class FreeResolution(SageObject, metaclass=ClasscallMetaclass):
    """
    A free resolution.

    Let `R` be a commutative ring. A *free resolution* of an `R`-module `M`
    is a (possibly infinite) chain complex of free `R`-modules

    .. MATH::

        \\cdots \\rightarrow R^{n_k} \\xrightarrow{d_k}
        \\cdots \\xrightarrow{d_2} R^{n_1} \\xrightarrow{d_1} R^{n_0}

    that is exact (all homology groups are zero) such that the image
    of `d_1` is `M`.
    """
    @staticmethod
    def __classcall_private__(cls, module, *args, graded: bool = False, degrees=None, shifts=None, **kwds):
        """
        Dispatch to the correct constructor.

        TESTS::

            sage: from sage.homology.free_resolution import FreeResolution
            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: m = matrix(S, 1, [z^2 - y*w, y*z - x*w, y^2 - x*z]).transpose()
            sage: r = FreeResolution(m, name='S')
            sage: type(r)
            <class 'sage.homology.free_resolution.FiniteFreeResolution_singular'>

            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = FreeResolution(I)
            sage: type(r)
            <class 'sage.homology.free_resolution.FiniteFreeResolution_singular'>

            sage: R.<x> = QQ[]
            sage: M = R^3
            sage: v = M([x^2, 2*x^2, 3*x^2])
            sage: w = M([0, x, 2*x])
            sage: S = M.submodule([v, w])
            sage: r = FreeResolution(S)
            sage: type(r)
            <class 'sage.homology.free_resolution.FiniteFreeResolution_free_module'>

            sage: I = R.ideal([x^4 + 3*x^2 + 2])
            sage: r = FreeResolution(I)
            sage: type(r)
            <class 'sage.homology.free_resolution.FiniteFreeResolution_free_module'>

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([x^2, y^3])
            sage: Q = R.quo(I)
            sage: Q.is_integral_domain()
            False
            sage: xb, yb = Q.gens()                                                     # needs sage.rings.function_field
            sage: FreeResolution(Q.ideal([xb]))  # has torsion                          # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: the ring must be a polynomial ring using Singular
        """
    def __init__(self, module, name: str = 'S', **kwds) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``base_ring`` -- a ring
        - ``name`` -- (default: ``'S'``) the name of the ring for printing

        TESTS::

            sage: from sage.homology.free_resolution import FreeResolution
            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: m1 = matrix(S, 1, [z^2 - y*w, y*z - x*w, y^2 - x*z])
            sage: r = FreeResolution(m1, name='S')
            sage: TestSuite(r).run(skip=['_test_pickling'])
        """
    @abstract_method
    def differential(self, i) -> None:
        """
        Return the `i`-th differential map.

        INPUT:

        - ``i`` -- positive integer

        TESTS::

            sage: from sage.homology.free_resolution import FreeResolution
            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: m1 = matrix(S, 1, [z^2 - y*w, y*z - x*w, y^2 - x*z])
            sage: r = FreeResolution(m1, name='S')
            sage: FreeResolution.differiental(r, 1)
            Traceback (most recent call last):
            ...
            AttributeError: type object 'FreeResolution' has no attribute 'differiental'...
        """
    def target(self):
        """
        Return the codomain of the `0`-th differential map.

        The codomain of the `0`-th differential map is the cokernel of
        the first differential map.

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: r
            S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
            sage: r.target()
            Quotient module by
             Submodule of Ambient free module of rank 1 over the integral domain
              Multivariate Polynomial Ring in x, y, z, w over Rational Field
              Generated by the rows of the matrix:
              [-z^2 + y*w]
              [ y*z - x*w]
              [-y^2 + x*z]
        """

class FiniteFreeResolution(FreeResolution):
    """
    Finite free resolutions.

    The matrix at index `i` in the list defines the differential map from
    `(i + 1)`-th free module to the `i`-th free module over the base ring by
    multiplication on the left. The number of matrices in the list is the
    length of the resolution. The number of rows and columns of the matrices
    define the ranks of the free modules in the resolution.

    Note that the first matrix in the list defines the differential map at
    homological index `1`.

    A subclass must provide a ``_maps`` attribute that contains a list of the
    maps defining the resolution.

    A subclass can define ``_initial_differential`` attribute that
    contains the `0`-th differential map whose codomain is the target
    of the free resolution.

    EXAMPLES::

        sage: from sage.homology.free_resolution import FreeResolution
        sage: S.<x,y,z,w> = PolynomialRing(QQ)
        sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
        sage: r = FreeResolution(I)
        sage: r.differential(0)
        Coercion map:
          From: Ambient free module of rank 1 over the integral domain
                Multivariate Polynomial Ring in x, y, z, w over Rational Field
          To:   Quotient module by
                Submodule of Ambient free module of rank 1 over the integral domain
                Multivariate Polynomial Ring in x, y, z, w over Rational Field
                Generated by the rows of the matrix:
                [-z^2 + y*w]
                [ y*z - x*w]
                [-y^2 + x*z]
    """
    def __len__(self) -> int:
        """
        Return the length of this resolution.

        The length of a free resolution is the index of the last nonzero free module.

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution(); r
            S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
            sage: len(r)
            2
        """
    def __getitem__(self, i):
        """
        Return the `i`-th free module of this resolution.

        INPUT:

        - ``i`` -- positive integer

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution(); r
            S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
            sage: r.target()
            Quotient module by Submodule of Ambient free module of rank 1 over the integral domain
            Multivariate Polynomial Ring in x, y, z, w over Rational Field
            Generated by the rows of the matrix:
            [-z^2 + y*w]
            [ y*z - x*w]
            [-y^2 + x*z]
        """
    def differential(self, i):
        """
        Return the `i`-th differential map.

        INPUT:

        - ``i`` -- positive integer

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: r
            S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
            sage: r.differential(3)
            Free module morphism defined as left-multiplication by the matrix
             []
             Domain:   Ambient free module of rank 0 over the integral domain
                       Multivariate Polynomial Ring in x, y, z, w over Rational Field
             Codomain: Ambient free module of rank 2 over the integral domain
                       Multivariate Polynomial Ring in x, y, z, w over Rational Field
            sage: r.differential(2)
            Free module morphism defined as left-multiplication by the matrix
              [-y  x]
              [ z -y]
              [-w  z]
              Domain:   Ambient free module of rank 2 over the integral domain
                        Multivariate Polynomial Ring in x, y, z, w over Rational Field
              Codomain: Ambient free module of rank 3 over the integral domain
                        Multivariate Polynomial Ring in x, y, z, w over Rational Field
            sage: r.differential(1)
            Free module morphism defined as left-multiplication by the matrix
              [z^2 - y*w y*z - x*w y^2 - x*z]
              Domain:   Ambient free module of rank 3 over the integral domain
                        Multivariate Polynomial Ring in x, y, z, w over Rational Field
              Codomain: Ambient free module of rank 1 over the integral domain
                        Multivariate Polynomial Ring in x, y, z, w over Rational Field
            sage: r.differential(0)
            Coercion map:
              From: Ambient free module of rank 1 over the integral domain
                    Multivariate Polynomial Ring in x, y, z, w over Rational Field
              To:   Quotient module by
                    Submodule of Ambient free module of rank 1 over the integral domain
                    Multivariate Polynomial Ring in x, y, z, w over Rational Field
                    Generated by the rows of the matrix:
                    [-z^2 + y*w]
                    [ y*z - x*w]
                    [-y^2 + x*z]

        TESTS::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: S = P2.coordinate_ring()
            sage: I = S.ideal(0)
            sage: C = I.graded_free_resolution(); C
            S(0) <-- 0
            sage: C[1]
            Ambient free module of rank 0 over the integral domain
             Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: C[0]
            Ambient free module of rank 1 over the integral domain
             Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: C.differential(1)
            Free module morphism defined as left-multiplication by the matrix
            []
            Domain: Ambient free module of rank 0 over the integral domain
             Multivariate Polynomial Ring in x, y, z over Rational Field
            Codomain: Ambient free module of rank 1 over the integral domain
             Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: C.differential(1).matrix()
            []
            sage: C.differential(1).matrix().dimensions()
            (1, 0)
        """
    def matrix(self, i):
        """
        Return the matrix representing the `i`-th differential map.

        INPUT:

        - ``i`` -- positive integer

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution(); r
            S(0) <-- S(-2)⊕S(-2)⊕S(-2) <-- S(-3)⊕S(-3) <-- 0
            sage: r.matrix(3)
            []
            sage: r.matrix(2)
            [-y  x]
            [ z -y]
            [-w  z]
            sage: r.matrix(1)
            [z^2 - y*w y*z - x*w y^2 - x*z]
        """
    def chain_complex(self):
        """
        Return this resolution as a chain complex.

        A chain complex in Sage has its own useful methods.

        EXAMPLES::

            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = I.graded_free_resolution()
            sage: unicode_art(r.chain_complex())
                                                           ⎛-y  x⎞
                                                           ⎜ z -y⎟
                       (z^2 - y*w y*z - x*w y^2 - x*z)     ⎝-w  z⎠
             0 <── C_0 <────────────────────────────── C_1 <────── C_2 <── 0
        """

class FiniteFreeResolution_free_module(FiniteFreeResolution):
    """
    Free resolutions of a free module.

    INPUT:

    - ``module`` -- a free module or ideal over a PID
    - ``name`` -- the name of the base ring

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: M = R^3
        sage: v = M([x^2, 2*x^2, 3*x^2])
        sage: w = M([0, x, 2*x])
        sage: S = M.submodule([v, w]); S
        Free module of degree 3 and rank 2 over
         Univariate Polynomial Ring in x over Rational Field
         Echelon basis matrix:
         [  x^2 2*x^2 3*x^2]
         [    0     x   2*x]
        sage: res = S.free_resolution(); res
        S^3 <-- S^2 <-- 0
        sage: ascii_art(res.chain_complex())
                    [  x^2     0]
                    [2*x^2     x]
                    [3*x^2   2*x]
         0 <-- C_0 <-------------- C_1 <-- 0

        sage: R.<x> = PolynomialRing(QQ)
        sage: I = R.ideal([x^4 + 3*x^2 + 2])
        sage: res = I.free_resolution(); res
        S^1 <-- S^1 <-- 0
    """

class FiniteFreeResolution_singular(FiniteFreeResolution):
    """
    Minimal free resolutions of ideals or submodules of free modules
    of multivariate polynomial rings implemented in Singular.

    INPUT:

    - ``module`` -- a submodule of a free module `M` of rank `n` over `S` or
      an ideal of a multi-variate polynomial ring

    - ``name`` -- string (optional); name of the base ring

    - ``algorithm`` -- (default: ``'heuristic'``) Singular algorithm
      to compute a resolution of ``ideal``

    OUTPUT: a minimal free resolution of the ideal

    If ``module`` is an ideal of `S`, it is considered as a submodule of a
    free module of rank `1` over `S`.

    The available algorithms and the corresponding Singular commands
    are shown below:

    ============= ============================
    algorithm     Singular commands
    ============= ============================
    ``minimal``   ``mres(ideal)``
    ``shreyer``   ``minres(sres(std(ideal)))``
    ``standard``  ``minres(nres(std(ideal)))``
    ``heuristic`` ``minres(res(std(ideal)))``
    ============= ============================

    EXAMPLES::

        sage: from sage.homology.free_resolution import FreeResolution
        sage: S.<x,y,z,w> = PolynomialRing(QQ)
        sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
        sage: r = FreeResolution(I); r
        S^1 <-- S^3 <-- S^2 <-- 0
        sage: len(r)
        2

    ::

        sage: FreeResolution(I, algorithm='minimal')
        S^1 <-- S^3 <-- S^2 <-- 0
        sage: FreeResolution(I, algorithm='shreyer')
        S^1 <-- S^3 <-- S^2 <-- 0
        sage: FreeResolution(I, algorithm='standard')
        S^1 <-- S^3 <-- S^2 <-- 0
        sage: FreeResolution(I, algorithm='heuristic')
        S^1 <-- S^3 <-- S^2 <-- 0

    We can also construct a resolution by passing in a matrix defining
    the initial differential::

        sage: m = matrix(S, 1, [z^2 - y*w, y*z - x*w, y^2 - x*z]).transpose()
        sage: r = FreeResolution(m, name='S'); r
        S^1 <-- S^3 <-- S^2 <-- 0
        sage: r.matrix(1)
        [z^2 - y*w y*z - x*w y^2 - x*z]

    An additional construction is using a submodule of a free module::

        sage: M = m.image()
        sage: r = FreeResolution(M, name='S'); r
        S^1 <-- S^3 <-- S^2 <-- 0

    A nonhomogeneous ideal::

        sage: I = S.ideal([z^2 - y*w, y*z - x*w, y^2 - x])
        sage: R = FreeResolution(I); R
        S^1 <-- S^3 <-- S^3 <-- S^1 <-- 0
        sage: R.matrix(2)
        [ y*z - x*w    y^2 - x          0]
        [-z^2 + y*w          0    y^2 - x]
        [         0 -z^2 + y*w -y*z + x*w]
        sage: R.matrix(3)
        [   y^2 - x]
        [-y*z + x*w]
        [ z^2 - y*w]
    """
    def __init__(self, module, name: str = 'S', algorithm: str = 'heuristic', **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.homology.free_resolution import FreeResolution
            sage: S.<x,y,z,w> = PolynomialRing(QQ)
            sage: I = S.ideal([y*w - z^2, -x*w + y*z, x*z - y^2])
            sage: r = FreeResolution(I)
            sage: TestSuite(r).run(skip=['_test_pickling'])

            sage: m = matrix(S, 1, [z^2 - y*w, y*z - x*w, y^2 - x*z]).transpose()
            sage: r = FreeResolution(m, name='S')
            sage: TestSuite(r).run(skip=['_test_pickling'])

            sage: M = m.image()
            sage: r = FreeResolution(M, name='S')
            sage: TestSuite(r).run(skip=['_test_pickling'])
        """
