from sage.matrix.constructor import Matrix as Matrix, zero_matrix as zero_matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose
from sage.modular.btquotients.btquotient import DoubleCosetReduction as DoubleCosetReduction
from sage.modular.hecke.all import AmbientHeckeModule as AmbientHeckeModule, HeckeModuleElement as HeckeModuleElement
from sage.modular.pollack_stevens.distributions import OverconvergentDistributions as OverconvergentDistributions, Symk as Symk
from sage.modular.pollack_stevens.sigma0 import Sigma0ActionAdjuster as Sigma0ActionAdjuster
from sage.modules.module import Module as Module
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RR as RR
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class _btquot_adjuster(Sigma0ActionAdjuster):
    """
    Callable object that turns matrices into 4-tuples.

    Since the modular symbol and harmonic cocycle code use different
    conventions for group actions, this function is used to make sure
    that actions are correct for harmonic cocycle computations.

    EXAMPLES::

        sage: from sage.modular.btquotients.pautomorphicform import _btquot_adjuster
        sage: adj = _btquot_adjuster()
        sage: adj(matrix(ZZ,2,2,[1..4]))
        (4, 2, 3, 1)
    """
    def __call__(self, g):
        """
        Turn matrices into 4-tuples.

        INPUT:

        - ``g`` -- a 2x2 matrix

        OUTPUT: a 4-tuple encoding the entries of ``g``

        EXAMPLES::

            sage: from sage.modular.btquotients.pautomorphicform import _btquot_adjuster
            sage: adj = _btquot_adjuster()
            sage: adj(matrix(ZZ,2,2,[0, 1, 2, 3]))
            (3, 1, 2, 0)
        """

def eval_dist_at_powseries(phi, f):
    """
    Evaluate a distribution on a powerseries.

    A distribution is an element in the dual of the Tate ring. The
    elements of coefficient modules of overconvergent modular symbols
    and overconvergent `p`-adic automorphic forms give examples of
    distributions in Sage.

    INPUT:

    - ``phi`` -- a distribution

    - ``f`` -- a power series over a ring coercible into a `p`-adic field

    OUTPUT:

    The value of ``phi`` evaluated at ``f``, which will be an element in the
    ring of definition of ``f``

    EXAMPLES::

        sage: from sage.modular.btquotients.pautomorphicform import eval_dist_at_powseries
        sage: R.<X> = PowerSeriesRing(ZZ,10)
        sage: f = (1 - 7*X)^(-1)

        sage: D = OverconvergentDistributions(0,7,10)                                   # needs sage.rings.padics
        sage: phi = D(list(range(1,11)))                                                # needs sage.rings.padics
        sage: eval_dist_at_powseries(phi,f)                                             # needs sage.rings.padics
        1 + 2*7 + 3*7^2 + 4*7^3 + 5*7^4 + 6*7^5 + 2*7^7 + 3*7^8 + 4*7^9 + O(7^10)
    """

class BruhatTitsHarmonicCocycleElement(HeckeModuleElement):
    """
    `\\Gamma`-invariant harmonic cocycles on the Bruhat-Tits
    tree. `\\Gamma`-invariance is necessary so that the cocycle can be
    stored in terms of a finite amount of data.

    More precisely, given a ``BruhatTitsQuotient`` `T`, harmonic cocycles are stored as
    a list of values in some coefficient module (e.g. for weight 2 forms
    can take `\\CC_p`) indexed by edges of a fundamental domain for `T` in the
    Bruhat-Tits tree. Evaluate the cocycle at other edges using Gamma
    invariance (although the values may not be equal over an orbit of
    edges as the coefficient module action may be nontrivial).

    EXAMPLES:

    Harmonic cocycles form a vector space, so they can be added and/or
    subtracted from each other::

        sage: X = BruhatTitsQuotient(5,23)
        sage: H = X.harmonic_cocycles(2,prec=10)
        sage: v1 = H.basis()[0]; v2 = H.basis()[1] # indirect doctest
        sage: v3 = v1+v2
        sage: v1 == v3-v2
        True

    and rescaled::

        sage: v4 = 2*v1
        sage: v1 == v4 - v1
        True

    AUTHORS:

    - Cameron Franc (2012-02-20)
    - Marc Masdeu
    """
    def __init__(self, _parent, vec) -> None:
        """
        Create a harmonic cocycle element.

        INPUT:

        - ``_parent`` : the parent space of harmonic cocycles.
        - ``vec`` : a list of elements in the coefficient module.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(31,7)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: v = H.basis()[0] # indirect doctest
            sage: TestSuite(v).run()
        """
    def monomial_coefficients(self, copy: bool = True):
        """
        Return a dictionary whose keys are indices of basis elements
        in the support of ``self`` and whose values are the
        corresponding coefficients.

        EXAMPLES::

            sage: M = BruhatTitsQuotient(3,5).harmonic_cocycles(2, prec=10)
            sage: M.monomial_coefficients()
            {}
        """
    def print_values(self) -> None:
        """
        Print the values of the cocycle on all of the edges.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,23)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: H.basis()[0].print_values()
            0   |1 + O(5^10)
            1   |0
            2   |0
            3   |4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10)
            4   |0
            5   |0
            6   |0
            7   |0
            8   |0
            9   |0
            10  |0
            11  |0
        """
    def valuation(self):
        """
        Return the valuation of the cocycle, defined as the
        minimum of the values it takes on a set of representatives.

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,17)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: b1 = H.basis()[0]
            sage: b2 = 3*b1
            sage: b1.valuation()
            0
            sage: b2.valuation()
            1
            sage: H(0).valuation()
            +Infinity
        """
    def evaluate(self, e1):
        """
        Evaluate a harmonic cocycle on an edge of the Bruhat-Tits tree.

        INPUT:

        - ``e1`` -- a matrix corresponding to an edge of the
          Bruhat-Tits tree

        OUTPUT:

        - An element of the coefficient module of the cocycle which
          describes the value of the cocycle on ``e1``

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,17)
            sage: e0 = X.get_edge_list()[0]
            sage: e1 = X.get_edge_list()[1]
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: b = H.basis()[0]
            sage: b.evaluate(e0.rep)
            1 + O(5^10)
            sage: b.evaluate(e1.rep)
            4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10)
        """
    def riemann_sum(self, f, center: int = 1, level: int = 0, E=None):
        """
        Evaluate the integral of the function ``f`` with respect
        to the measure determined by ``self`` over `\\mathbf{P}^1(\\QQ_p)`.

        INPUT:

        - ``f`` -- a function on `\\mathbf{P}^1(\\QQ_p)`

        - ``center`` -- integer (default: 1); Center of integration

        - ``level`` -- integer (default: 0); Determines the size of
          the covering when computing the Riemann sum. Runtime is
          exponential in the level.

        - ``E`` -- list of edges (default: ``None``); They should describe
          a covering of `\\mathbf{P}^1(\\QQ_p)`

        OUTPUT: a `p`-adic number

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: b = H.basis()[0]
            sage: R.<z> = PolynomialRing(QQ,1)
            sage: f = z^2

        Note that `f` has a pole at infinity, so that the result will
        be meaningless::

            sage: b.riemann_sum(f,level=0)
            1 + 5 + 2*5^3 + 4*5^4 + 2*5^5 + 3*5^6 + 3*5^7 + 2*5^8 + 4*5^9 + O(5^10)
        """
    def modular_form(self, z=None, level: int = 0):
        """
        Integrate Teitelbaum's `p`-adic Poisson kernel against
        the measure corresponding to ``self`` to evaluate the associated
        modular form at ``z``.

        If ``z`` = None, a function is returned that encodes the modular form.

        .. NOTE::

            This function uses the integration method of Riemann
            summation and is incredibly slow! It should only be used for
            testing and bug-finding. Overconvergent methods are quicker.

        INPUT:

        - ``z`` -- an element in the quadratic unramified extension of
          `\\QQ_p` that is not contained in `\\QQ_p` (default: ``None``)

        - ``level`` -- integer; how fine of a mesh should the Riemann
          sum use

        OUTPUT: an element of the quadratic unramified extension of `\\QQ_p`

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,23)
            sage: H = X.harmonic_cocycles(2,prec = 8)
            sage: b = H.basis()[0]
            sage: R.<a> = Qq(9,prec=10)
            sage: x1 = b.modular_form(a,level = 0); x1
            a + (2*a + 1)*3 + (a + 1)*3^2 + (a + 1)*3^3 + 3^4 + (a + 2)*3^5 + a*3^7 + O(3^8)
            sage: x2 = b.modular_form(a,level = 1); x2
            a + (a + 2)*3 + (2*a + 1)*3^3 + (2*a + 1)*3^4 + 3^5 + (a + 2)*3^6 + a*3^7 + O(3^8)
            sage: x3 = b.modular_form(a,level = 2); x3
            a + (a + 2)*3 + (2*a + 2)*3^2 + 2*a*3^4 + (a + 1)*3^5 + 3^6 + O(3^8)
            sage: x4 = b.modular_form(a,level = 3);x4
            a + (a + 2)*3 + (2*a + 2)*3^2 + (2*a + 2)*3^3 + 2*a*3^5 + a*3^6 + (a + 2)*3^7 + O(3^8)
            sage: (x4-x3).valuation()
            3

        TESTS:

        Check that :issue:`22634` is fixed::

            sage: X = BruhatTitsQuotient(7,2)
            sage: H = X.harmonic_cocycles(4,20)
            sage: f0, g0 = H.basis()
            sage: A = X.padic_automorphic_forms(4,20,overconvergent=True)
            sage: f = A.lift(f0).modular_form(method='moments')
            sage: T.<x> = Qq(7^2,20)
            sage: a,b,c,d = X.embed_quaternion(X.get_units_of_order()[1]).change_ring(Qp(7,20)).list()
            sage: (c*x + d)^4 * f(x) == f((a*x + b)/(c*x + d))
            True
            sage: g = A.lift(g0).modular_form(method='moments')
            sage: (c*x + d)^4 * f(x) == f((a*x + b)/(c*x + d))
            True
        """
    def derivative(self, z=None, level: int = 0, order: int = 1):
        """
        Integrate Teitelbaum's `p`-adic Poisson kernel against
        the measure corresponding to ``self`` to evaluate the rigid
        analytic Shimura-Maass derivatives of the associated modular
        form at `z`.

        If ``z = None``, a function is returned that encodes the
        derivative of the modular form.

        .. NOTE::

            This function uses the integration method of Riemann
            summation and is incredibly slow! It should only be used for
            testing and bug-finding. Overconvergent methods are quicker.

        INPUT:

        - ``z`` -- an element in the quadratic unramified extension of
          `\\QQ_p` that is not contained in `\\QQ_p` (default: ``None``); if
          ``z = None`` then a function encoding the derivative is returned.

        - ``level`` -- integer; how fine of a mesh should the Riemann
          sum use

        - ``order`` -- integer; how many derivatives to take

        OUTPUT:

        An element of the quadratic unramified extension of `\\QQ_p`, or
        a function encoding the derivative.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,23)
            sage: H = X.harmonic_cocycles(2,prec=5)
            sage: b = H.basis()[0]
            sage: R.<a> = Qq(9,prec=10)
            sage: b.modular_form(a,level=0) == b.derivative(a,level=0,order=0)
            True
            sage: b.derivative(a,level=1,order=1)
            (2*a + 2)*3 + (a + 2)*3^2 + 2*a*3^3 + 2*3^4 + O(3^5)
            sage: b.derivative(a,level=2,order=1)
            (2*a + 2)*3 + 2*a*3^2 + 3^3 + a*3^4 + O(3^5)
        """

class BruhatTitsHarmonicCocycles(AmbientHeckeModule, UniqueRepresentation):
    """
    Ensure unique representation.

    EXAMPLES::

        sage: X = BruhatTitsQuotient(3,5)
        sage: M1 = X.harmonic_cocycles( 2, prec = 10)
        sage: M2 = X.harmonic_cocycles( 2, 10)
        sage: M1 is M2
        True
    """
    Element = BruhatTitsHarmonicCocycleElement
    @staticmethod
    def __classcall__(cls, X, k, prec=None, basis_matrix=None, base_field=None):
        """
        Represent a space of Gamma invariant harmonic
        cocycles valued in a coefficient module.

        INPUT:

        - ``X`` -- a BruhatTitsQuotient object

        - ``k`` -- integer; the weight. It must be even.

        - ``prec`` -- integer (default: ``None``); if specified, the
          precision for the coefficient module

        - ``basis_matrix`` -- a matrix (default: ``None``)

        - ``base_field`` -- a ring (default: ``None``)

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,23)
            sage: H = X.harmonic_cocycles(2,prec = 5)
            sage: H.dimension()
            3
            sage: X.genus()
            3

        Higher even weights are implemented::

            sage: H = X.harmonic_cocycles(8, prec = 10)
            sage: H.dimension()
            26

        AUTHORS:

        - Cameron Franc (2012-02-20)
        - Marc Masdeu
        """
    def __init__(self, X, k, prec=None, basis_matrix=None, base_field=None) -> None:
        """
        Compute the space of harmonic cocycles.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,37)
            sage: H = X.harmonic_cocycles(4,prec=10)
            sage: TestSuite(H).run()
        """
    def monomial_coefficients(self):
        """
        Void method to comply with pickling.

        EXAMPLES::

            sage: M = BruhatTitsQuotient(3,5).harmonic_cocycles(2,prec=10)
            sage: M.monomial_coefficients()
            {}
        """
    def base_extend(self, base_ring):
        """
        Extend the base ring of the coefficient module.

        INPUT:

        - ``base_ring`` -- a ring that has a coerce map from the
          current base ring

        OUTPUT: a new space of HarmonicCocycles with the base extended

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,19)
            sage: H = X.harmonic_cocycles(2,10)
            sage: H.base_ring()
            3-adic Field with capped relative precision 10
            sage: H1 = H.base_extend(Qp(3,prec=15))
            sage: H1.base_ring()
            3-adic Field with capped relative precision 15
        """
    def change_ring(self, new_base_ring):
        """
        Change the base ring of the coefficient module.

        INPUT:

        - ``new_base_ring`` -- a ring that has a coerce map from the
          current base ring

        OUTPUT: new space of HarmonicCocycles with different base ring

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,17)
            sage: H = X.harmonic_cocycles(2,10)
            sage: H.base_ring()
            5-adic Field with capped relative precision 10
            sage: H1 = H.base_extend(Qp(5,prec=15)) # indirect doctest
            sage: H1.base_ring()
            5-adic Field with capped relative precision 15
        """
    def rank(self):
        """
        Return the rank (dimension) of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,11)
            sage: H = X.harmonic_cocycles(2,prec = 10)
            sage: X.genus() == H.rank()
            True
            sage: H1 = X.harmonic_cocycles(4,prec = 10)
            sage: H1.rank()
            16
        """
    def submodule(self, v, check: bool = False) -> None:
        """
        Return the submodule of ``self`` spanned by ``v``.

        INPUT:

        - ``v`` -- submodule of ``self.free_module()``

        - ``check`` -- boolean (default: ``False``)

        OUTPUT: subspace of harmonic cocycles

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,17)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: H.rank()
            3
            sage: v = H.gen(0)
            sage: N = H.free_module().span([v.element()])
            sage: H1 = H.submodule(N)
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def is_simple(self) -> bool:
        """
        Whether ``self`` is irreducible.

        OUTPUT: boolean; ``True`` if and only if ``self`` is irreducible

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3, 29)
            sage: H = X.harmonic_cocycles(4, prec=10)
            sage: H.rank()
            14
            sage: H.is_simple()
            False
            sage: X = BruhatTitsQuotient(7, 2)
            sage: H = X.harmonic_cocycles(2, prec=10)
            sage: H.rank()
            1
            sage: H.is_simple()
            True
        """
    def __eq__(self, other):
        """
        Test whether two BruhatTitsHarmonicCocycle spaces are equal.

        INPUT:

        - ``other`` -- a BruhatTitsHarmonicCocycles class

        OUTPUT: boolean

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H1 = X.harmonic_cocycles(2,prec=10)
            sage: H2 = X.harmonic_cocycles(2,prec=10)
            sage: H1 == H2
            True
        """
    def __ne__(self, other):
        """
        Test whether two BruhatTitsHarmonicCocycle spaces are not equal.

        INPUT:

        - ``other`` -- a BruhatTitsHarmonicCocycles class

        OUTPUT: boolean

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H1 = X.harmonic_cocycles(2,prec=10)
            sage: H2 = X.harmonic_cocycles(2,prec=10)
            sage: H1 != H2
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H1 = X.harmonic_cocycles(2,prec=10)
            sage: H2 = X.harmonic_cocycles(2,prec=10)
            sage: hash(H1) == hash(H2)
            True
        """
    def free_module(self):
        """
        Return the underlying free module.

        OUTPUT: a free module

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,7)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: H.free_module()
            Vector space of dimension 1 over 3-adic Field with
            capped relative precision 10
        """
    def character(self):
        """
        The trivial character.

        OUTPUT: the identity map

        EXAMPLES::

            sage: X = BruhatTitsQuotient(3,7)
            sage: H = X.harmonic_cocycles(2,prec = 10)
            sage: f = H.character()
            sage: f(1)
            1
            sage: f(2)
            2
        """
    def embed_quaternion(self, g, scale: int = 1, exact=None):
        """
        Embed the quaternion element ``g`` into the matrix algebra.

        INPUT:

        - ``g`` -- a quaternion, expressed as a 4x1 matrix

        OUTPUT: a 2x2 matrix with `p`-adic entries

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,2)
            sage: q = X.get_stabilizers()[0][1][0]
            sage: H = X.harmonic_cocycles(2,prec = 5)
            sage: Hmat = H.embed_quaternion(q)
            sage: Hmat.matrix().trace() == X._conv(q).reduced_trace() and Hmat.matrix().determinant() == 1
            True
        """
    def basis_matrix(self):
        """
        Return a basis of ``self`` in matrix form.

        If the coefficient module `M` is of finite rank then the space
        of Gamma invariant `M` valued harmonic cocycles can be
        represented as a subspace of the finite rank space of all
        functions from the finitely many edges in the corresponding
        BruhatTitsQuotient into `M`. This function computes this
        representation of the space of cocycles.

        OUTPUT:

        - A basis matrix describing the cocycles in the spaced of all
          `M` valued Gamma invariant functions on the tree.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,3)
            sage: M = X.harmonic_cocycles(4,prec = 20)
            sage: B = M.basis() # indirect doctest
            sage: len(B) == X.dimension_harmonic_cocycles(4)
            True

        AUTHORS:

        - Cameron Franc (2012-02-20)
        - Marc Masdeu (2012-02-20)
        """

class pAdicAutomorphicFormElement(ModuleElement):
    """
    Rudimentary implementation of a class for a `p`-adic
    automorphic form on a definite quaternion algebra over `\\QQ`. These
    are required in order to compute moments of measures associated to
    harmonic cocycles on the Bruhat-Tits tree using the overconvergent modules
    of Darmon-Pollack and Matt Greenberg. See Greenberg's thesis [Gr2006]_ for
    more details.

    INPUT:

    - ``vec`` -- a preformatted list of data

    EXAMPLES::

        sage: X = BruhatTitsQuotient(17,3)
        sage: H = X.harmonic_cocycles(2,prec=10)
        sage: h = H.an_element()
        sage: HH = X.padic_automorphic_forms(2,10)
        sage: a = HH(h)
        sage: a
        p-adic automorphic form of cohomological weight 0

    AUTHORS:

    - Cameron Franc (2012-02-20)
    - Marc Masdeu
    """
    def __init__(self, parent, vec) -> None:
        """
        Create a pAdicAutomorphicFormElement.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(17,3)
            sage: A = X.padic_automorphic_forms(2,prec=10)
            sage: TestSuite(A.an_element()).run()
        """
    def __bool__(self) -> bool:
        """
        Tell whether the form is zero or not.

        OUTPUT: boolean; whether ``self`` is zero

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,23)
            sage: H = X.harmonic_cocycles(4,prec = 20)
            sage: A = X.padic_automorphic_forms(4,prec = 20)
            sage: v1 = A(H.basis()[1])
            sage: bool(v1)
            True
            sage: v2 = v1-v1
            sage: bool(v2)
            False
        """
    def __getitem__(self, e1):
        """
        Evaluate a `p`-adic automorphic form on a matrix in `GL_2(\\QQ_p)`.

        INPUT:

        - ``e1`` -- a matrix in `GL_2(\\QQ_p)`

        OUTPUT: the value of ``self`` evaluated on ``e1``

        EXAMPLES::

            sage: X = BruhatTitsQuotient(17,3)
            sage: M = X.harmonic_cocycles(2,prec=5)
            sage: A = X.padic_automorphic_forms(2,prec=5)
            sage: a = A(M.gen(0))
            sage: a[Matrix(ZZ,2,2,[1,2,3,4])]
            8 + 8*17 + 8*17^2 + 8*17^3 + 8*17^4 + O(17^5)
        """
    def evaluate(self, e1):
        """
        Evaluate a `p`-adic automorphic form on a matrix in `GL_2(\\QQ_p)`.

        INPUT:

        - ``e1`` -- a matrix in `GL_2(\\QQ_p)`

        OUTPUT: the value of ``self`` evaluated on ``e1``

        EXAMPLES::

            sage: X = BruhatTitsQuotient(7,5)
            sage: M = X.harmonic_cocycles(2,prec=5)
            sage: A = X.padic_automorphic_forms(2,prec=5)
            sage: a = A(M.basis()[0])
            sage: a.evaluate(Matrix(ZZ,2,2,[1,2,3,1]))
            4 + 6*7 + 6*7^2 + 6*7^3 + 6*7^4 + O(7^5)
            sage: a.evaluate(Matrix(ZZ,2,2,[17,0,0,1]))
            1 + O(7^5)
        """
    def valuation(self):
        """
        The valuation of ``self``, defined as the minimum of the
        valuations of the values that it takes on a set of edge
        representatives.

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(17,3)
            sage: M = X.harmonic_cocycles(2,prec=10)
            sage: A = X.padic_automorphic_forms(2,prec=10)
            sage: a = A(M.gen(0))
            sage: a.valuation()
            0
            sage: (17*a).valuation()
            1
        """
    def integrate(self, f, center: int = 1, level: int = 0, method: str = 'moments'):
        """
        Calculate

        .. MATH::

            \\int_{\\mathbf{P}^1(\\QQ_p)} f(x)d\\mu(x)

        were `\\mu` is the measure associated to ``self``.

        INPUT:

        - ``f`` -- an analytic function

        - ``center`` -- 2x2 matrix over `\\QQ_p` (default: 1)

        - ``level`` -- integer (default: 0)

        - ``method`` -- string (default: ``'moments'``); which method of
          integration to use. Either ``'moments'`` or ``'riemann_sum'``.

        EXAMPLES:

        Integrating the Poisson kernel against a measure yields a
        value of the associated modular form. Such values can be
        computed efficiently using the overconvergent method, as long
        as one starts with an ordinary form::

            sage: X = BruhatTitsQuotient(7,2)
            sage: X.genus()
            1

        Since the genus is 1, the space of weight 2 forms is 1
        dimensional. Hence any nonzero form will be a `U_7`
        eigenvector. By Jacquet-Langlands and Cerednik-Drinfeld, in
        this case the Hecke eigenvalues correspond to that of any
        nonzero form on `\\Gamma_0(14)` of weight `2`. Such a form is
        ordinary at `7`, and so we can apply the overconvergent method
        directly to this form without `p`-stabilizing::

            sage: H = X.harmonic_cocycles(2,prec = 5)
            sage: h = H.gen(0)
            sage: A = X.padic_automorphic_forms(2,prec = 5,overconvergent=True)
            sage: a = A.lift(h)
            sage: a._value[0].moment(2)
            2 + 6*7 + 4*7^2 + 4*7^3 + 6*7^4 + O(7^5)

        Now that we've lifted our harmonic cocycle to an
        overconvergent automorphic form we simply need to define the
        Teitelbaum-Poisson Kernel, and then integrate::

            sage: Kp.<x> = Qq(49,prec = 5)
            sage: z = Kp['z'].gen()
            sage: f = 1/(z-x)
            sage: a.integrate(f)
            (5*x + 5) + (4*x + 4)*7 + (5*x + 5)*7^2 + (5*x + 6)*7^3 + O(7^5)

        AUTHORS:

        - Cameron Franc (2012-02-20)
        - Marc Masdeu (2012-02-20)
        """
    def modular_form(self, z=None, level: int = 0, method: str = 'moments'):
        """
        Return the modular form corresponding to ``self``.

        INPUT:

        - ``z`` -- (default: ``None``) if specified, returns the value of
          the form at the point ``z`` in the `p`-adic upper half
          plane

        - ``level`` -- integer (default: 0); if ``method`` is
          'riemann_sum', will use a covering of `P^1(\\QQ_p)` with
          balls of size `p^-\\mbox{level}`

        - ``method`` -- string (default: ``'moments'``); it must be
          either ``'moments'`` or ``'riemann_sum'``

        OUTPUT:

        A function from the `p`-adic upper half plane to `\\CC_p`. If
        an argument ``z`` was passed, returns instead the value at
        that point.

        EXAMPLES:

        Integrating the Poisson kernel against a measure yields a
        value of the associated modular form. Such values can be
        computed efficiently using the overconvergent method, as long
        as one starts with an ordinary form::

            sage: X = BruhatTitsQuotient(7, 2)
            sage: X.genus()
            1

        Since the genus is 1, the space of weight 2 forms is 1
        dimensional. Hence any nonzero form will be a `U_7`
        eigenvector. By Jacquet-Langlands and Cerednik-Drinfeld, in
        this case the Hecke eigenvalues correspond to that of any
        nonzero form on `\\Gamma_0(14)` of weight `2`. Such a form is
        ordinary at `7`, and so we can apply the overconvergent method
        directly to this form without `p`-stabilizing::

            sage: H = X.harmonic_cocycles(2,prec = 5)
            sage: A = X.padic_automorphic_forms(2,prec = 5,overconvergent=True)
            sage: f0 = A.lift(H.basis()[0])

        Now that we've lifted our harmonic cocycle to an
        overconvergent automorphic form, we extract the associated
        modular form as a function and test the modular property::

            sage: T.<x> = Qq(7^2,prec = 5)
            sage: f = f0.modular_form(method = 'moments')
            sage: a,b,c,d = X.embed_quaternion(X.get_units_of_order()[1]).change_ring(T.base_ring()).list()
            sage: ((c*x + d)^2*f(x)-f((a*x + b)/(c*x + d))).valuation()
            5
        """
    def derivative(self, z=None, level: int = 0, method: str = 'moments', order: int = 1):
        """
        Return the derivative of the modular form corresponding to
        ``self``.

        INPUT:

        - ``z`` -- (default: ``None``) if specified, evaluates the derivative
          at the point ``z`` in the `p`-adic upper half plane

        - ``level`` -- integer (default: 0); if ``method`` is
          'riemann_sum', will use a covering of `P^1(\\QQ_p)` with
          balls of size `p^-\\mbox{level}`.

        - ``method`` -- string (default: ``'moments'``); it must be
          either ``'moments'`` or ``'riemann_sum'``

        - ``order`` -- integer (default: 1); the order of the
          derivative to be computed

        OUTPUT:

        A function from the `p`-adic upper half plane to `\\CC_p`. If
        an argument ``z`` was passed, returns instead the value of
        the derivative at that point.

        EXAMPLES:

        Integrating the Poisson kernel against a measure yields a
        value of the associated modular form. Such values can be
        computed efficiently using the overconvergent method, as long
        as one starts with an ordinary form::

            sage: X = BruhatTitsQuotient(7, 2)
            sage: X.genus()
            1

        Since the genus is 1, the space of weight 2 forms is 1
        dimensional. Hence any nonzero form will be a `U_7`
        eigenvector. By Jacquet-Langlands and Cerednik-Drinfeld, in
        this case the Hecke eigenvalues correspond to that of any
        nonzero form on `\\Gamma_0(14)` of weight `2`. Such a form is
        ordinary at `7`, and so we can apply the overconvergent method
        directly to this form without `p`-stabilizing::

            sage: H = X.harmonic_cocycles(2,prec=5)
            sage: h = H.gen(0)
            sage: A = X.padic_automorphic_forms(2,prec=5,overconvergent=True)
            sage: f0 = A.lift(h)

        Now that we've lifted our harmonic cocycle to an
        overconvergent automorphic form, we extract the associated
        modular form as a function and test the modular property::

            sage: T.<x> = Qq(49,prec=10)
            sage: f = f0.modular_form()
            sage: g = X.get_embedding_matrix()*X.get_units_of_order()[1]
            sage: a,b,c,d = g.change_ring(T).list()
            sage: (c*x +d)^2*f(x)-f((a*x + b)/(c*x + d))
            O(7^5)

        We can also compute the Shimura-Maass derivative, which is a
        nearly rigid analytic modular forms of weight 4::

            sage: f = f0.derivative()
            sage: (c*x + d)^4*f(x)-f((a*x + b)/(c*x + d))
            O(7^5)
        """
    def coleman(self, t1, t2, E=None, method: str = 'moments', mult: bool = False):
        """
        If ``self`` is a `p`-adic automorphic form that
        corresponds to a rigid modular form, then this computes the
        Coleman integral of this form between two points on the
        boundary `P^1(\\QQ_p)` of the `p`-adic upper half plane.

        INPUT:

        - ``t1``, ``t2`` -- elements of `P^1(\\QQ_p)` (the endpoints
          of integration)

        - ``E`` -- (default: ``None``) if specified, will not compute the
          covering adapted to ``t1`` and ``t2`` and instead use the
          given one. In that case, ``E`` should be a list of matrices
          corresponding to edges describing the open balls to be
          considered.

        - ``method`` -- string (default: ``'moments'``); tells which
          algorithm to use (alternative is ``'riemann_sum'``, which is
          unsuitable for computations requiring high precision)

        - ``mult`` -- boolean (default: ``False``); whether to compute the
          multiplicative version

        OUTPUT: the result of the Coleman integral

        EXAMPLES::

            sage: p = 7
            sage: lev = 2
            sage: prec = 10
            sage: X = BruhatTitsQuotient(p, lev)
            sage: k = 2
            sage: M = X.harmonic_cocycles(k, prec)
            sage: B = M.basis()
            sage: f = 3*B[0]
            sage: MM = X.padic_automorphic_forms(k, prec, overconvergent=True)
            sage: D = -11
            sage: X.is_admissible(D)
            True
            sage: K.<a> = QuadraticField(D)
            sage: Kp.<g> = Qq(p**2, prec)
            sage: P = Kp.gen()
            sage: Q = 2 + Kp.gen() + p*(Kp.gen()+1)
            sage: F = MM.lift(f)  # long time
            sage: J0 = F.coleman(P, Q, mult=True)  # long time

        AUTHORS:

        - Cameron Franc (2012-02-20)
        - Marc Masdeu (2012-02-20)
        """

class pAdicAutomorphicForms(Module, UniqueRepresentation):
    Element = pAdicAutomorphicFormElement
    @staticmethod
    def __classcall__(cls, domain, U, prec=None, t=None, R=None, overconvergent: bool = False):
        """
        The module of (quaternionic) `p`-adic automorphic forms.

        INPUT:

        - ``domain`` -- a BruhatTitsQuotient

        - ``U`` -- a distributions module or an integer. If ``U`` is a
          distributions module then this creates the relevant space of
          automorphic forms. If ``U`` is an integer then the coefficients
          are the (`U-2`)nd power of the symmetric representation of
          `GL_2(\\QQ_p)`.

        - ``prec`` -- a precision (default: ``None``); if not ``None`` should
          be a positive integer

        - ``t`` -- (default: ``None``) the number of additional moments to
          store. If ``None``, determine it automatically from ``prec``, ``U``
          and the ``overconvergent`` flag.

        - ``R`` -- (default: ``None``) if specified, coefficient field of the automorphic forms.
          If not specified it defaults to the base ring of the distributions ``U``, or to `Q_p`
          with the working precision ``prec``.

        - ``overconvergent`` -- boolean (default: ``False``); if ``True``, will construct overconvergent
          `p`-adic automorphic forms. Otherwise it constructs the finite dimensional space of
          `p`-adic automorphic forms which is isomorphic to the space of harmonic cocycles.

        EXAMPLES:

        The space of weight 2 p-automorphic forms is isomorphic with
        the space of scalar valued invariant harmonic cocycles::

            sage: X = BruhatTitsQuotient(11,5)
            sage: H0 = X.padic_automorphic_forms(2,10)
            sage: H1 = X.padic_automorphic_forms(2,prec = 10)
            sage: H0 == H1
            True

        AUTHORS:

        - Cameron Franc (2012-02-20)
        - Marc Masdeu (2012-02-20)
        """
    def __init__(self, domain, U, prec=None, t=None, R=None, overconvergent: bool = False) -> None:
        """
        Create a space of `p`-automorphic forms.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(11,5)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: A = X.padic_automorphic_forms(2,prec=10)
            sage: TestSuite(A).run()
        """
    def prime(self):
        """
        Return the underlying prime.

        OUTPUT: ``p`` -- prime integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(11,5)
            sage: H = X.harmonic_cocycles(2,prec = 10)
            sage: A = X.padic_automorphic_forms(2,prec = 10)
            sage: A.prime()
            11
        """
    def zero(self):
        """
        Return the zero element of ``self``.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5, 7)
            sage: H1 = X.padic_automorphic_forms( 2, prec=10)
            sage: H1.zero() == 0
            True
        """
    def __eq__(self, other):
        """
        Test whether two pAdicAutomorphicForm spaces are equal.

        INPUT:

        - ``other`` -- another space of `p`-automorphic forms

        OUTPUT: boolean

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H1 = X.padic_automorphic_forms(2,prec = 10)
            sage: H2 = X.padic_automorphic_forms(2,prec = 10)
            sage: H1 == H2
            True
        """
    def __ne__(self, other):
        """
        Test whether two pAdicAutomorphicForm spaces are not equal.

        INPUT:

        - ``other`` -- another space of `p`-automorphic forms

        OUTPUT: boolean

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H1 = X.padic_automorphic_forms(2,prec = 10)
            sage: H2 = X.padic_automorphic_forms(2,prec = 10)
            sage: H1 == H2
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: X = BruhatTitsQuotient(5,7)
            sage: H1 = X.padic_automorphic_forms(2,prec = 10)
            sage: H2 = X.padic_automorphic_forms(2,prec = 10)
            sage: hash(H1) == hash(H2)
            True
        """
    def precision_cap(self):
        """
        Return the precision of ``self``.

        OUTPUT: integer

        EXAMPLES::

            sage: X = BruhatTitsQuotient(13,11)
            sage: A = X.padic_automorphic_forms(2,prec=10)
            sage: A.precision_cap()
            10
        """
    def lift(self, f):
        """
        Lift the harmonic cocycle ``f`` to a p-automorphic form.

        If one is using overconvergent coefficients, then this will
        compute all of the moments of the measure associated to ``f``.

        INPUT:

        - ``f`` -- a harmonic cocycle

        OUTPUT: a `p`-adic automorphic form

        EXAMPLES:

        If one does not work with an overconvergent form then lift
        does nothing::

            sage: X = BruhatTitsQuotient(13,5)
            sage: H = X.harmonic_cocycles(2,prec=10)
            sage: h = H.gen(0)
            sage: A = X.padic_automorphic_forms(2,prec=10)
            sage: A.lift(h) # long time
            p-adic automorphic form of cohomological weight 0

        With overconvergent forms, the input is lifted naively and its
        moments are computed::

            sage: X = BruhatTitsQuotient(13,11)
            sage: H = X.harmonic_cocycles(2,prec=5)
            sage: A2 = X.padic_automorphic_forms(2,prec=5,overconvergent=True)
            sage: a = H.gen(0)
            sage: A2.lift(a) # long time
            p-adic automorphic form of cohomological weight 0
        """
