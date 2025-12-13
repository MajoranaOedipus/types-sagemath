from _typeshed import Incomplete
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.prandom import randint as randint
from sage.misc.verbose import verbose as verbose
from sage.modular.modsym.all import ModularSymbols as ModularSymbols
from sage.rings.complex_double import CDF as CDF
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.sequence import Sequence as Sequence

scipy: Incomplete

class NumericalEigenforms(SageObject):
    '''
    numerical_eigenforms(group, weight=2, eps=1e-20, delta=1e-2, tp=[2,3,5]).

    INPUT:

    - ``group`` -- a congruence subgroup of a Dirichlet character of
      order 1 or 2

    - ``weight`` -- integer >= 2

    - ``eps`` -- a small float; abs( ) < eps is what "equal to zero" is
      interpreted as for floating point numbers

    - ``delta`` -- a small-ish float; eigenvalues are considered distinct
      if their difference has absolute value at least delta

    - ``tp`` -- use the Hecke operators T_p for p in tp when searching
      for a random Hecke operator with distinct Hecke eigenvalues

    OUTPUT: a numerical eigenforms object, with the following useful methods:

    - :meth:`ap` -- return all eigenvalues of `T_p`

    - :meth:`eigenvalues` -- list of eigenvalues corresponding
      to the given list of primes, e.g.,::

          [[eigenvalues of T_2],
           [eigenvalues of T_3],
           [eigenvalues of T_5], ...]

    - :meth:`systems_of_eigenvalues` -- list of the systems of
      eigenvalues of eigenforms such that the chosen random linear
      combination of Hecke operators has multiplicity 1 eigenvalues.

    EXAMPLES::

        sage: n = numerical_eigenforms(23)
        sage: n == loads(dumps(n))
        True
        sage: n.ap(2)  # abs tol 1e-12
        [3.0, -1.6180339887498947, 0.6180339887498968]
        sage: n.systems_of_eigenvalues(7)  # abs tol 2e-12
        [[-1.6180339887498947, 2.23606797749979, -3.2360679774997894],
         [0.618033988749895, -2.236067977499788, 1.23606797749979],
         [3.0, 4.0, 6.0]]
        sage: n.systems_of_abs(7)  # abs tol 2e-12
        [[0.618033988749895, 2.236067977499788, 1.23606797749979],
         [1.6180339887498947, 2.23606797749979, 3.2360679774997894],
         [3.0, 4.0, 6.0]]
        sage: n.eigenvalues([2,3,5])  # rel tol 2e-12
        [[3.0, -1.6180339887498947, 0.6180339887498968],
         [4.0, 2.2360679774997894, -2.236067977499788],
         [6.0, -3.2360679774997894, 1.2360679774997936]]
    '''
    def __init__(self, group, weight: int = 2, eps: float = 1e-20, delta: float = 0.01, tp=[2, 3, 5]) -> None:
        """
        Create a new space of numerical eigenforms.

        EXAMPLES::

            sage: numerical_eigenforms(61) # indirect doctest
            Numerical Hecke eigenvalues for Congruence Subgroup Gamma0(61) of weight 2
        """
    def __richcmp__(self, other, op):
        """
        Compare two spaces of numerical eigenforms.

        They are considered equal if and only if they come from the
        same space of modular symbols.

        EXAMPLES::

            sage: n = numerical_eigenforms(23)
            sage: n == loads(dumps(n))
            True
        """
    def level(self):
        """
        Return the level of this set of modular eigenforms.

        EXAMPLES::

            sage: n = numerical_eigenforms(61) ; n.level()
            61
        """
    def weight(self):
        """
        Return the weight of this set of modular eigenforms.

        EXAMPLES::

            sage: n = numerical_eigenforms(61) ; n.weight()
            2
        """
    @cached_method
    def modular_symbols(self):
        """
        Return the space of modular symbols used for computing this
        set of modular eigenforms.

        EXAMPLES::

            sage: n = numerical_eigenforms(61) ; n.modular_symbols()
            Modular Symbols space of dimension 5 for Gamma_0(61) of weight 2 with sign 1 over Rational Field
        """
    @cached_method
    def ap(self, p):
        """
        Return a list of the eigenvalues of the Hecke operator `T_p`
        on all the computed eigenforms.  The eigenvalues match up
        between one prime and the next.

        INPUT:

        - ``p`` -- integer; a prime number

        OUTPUT: list of double precision complex numbers

        EXAMPLES::

            sage: n = numerical_eigenforms(11,4)
            sage: n.ap(2) # random order
            [9.0, 9.0, 2.73205080757, -0.732050807569]
            sage: n.ap(3) # random order
            [28.0, 28.0, -7.92820323028, 5.92820323028]
            sage: m = n.modular_symbols()
            sage: x = polygen(QQ, 'x')
            sage: m.T(2).charpoly('x').factor()
            (x - 9)^2 * (x^2 - 2*x - 2)
            sage: m.T(3).charpoly('x').factor()
            (x - 28)^2 * (x^2 + 2*x - 47)
        """
    def eigenvalues(self, primes):
        """
        Return the eigenvalues of the Hecke operators corresponding
        to the primes in the input list of primes.   The eigenvalues
        match up between one prime and the next.

        INPUT:

        - ``primes`` -- list of primes

        OUTPUT: list of lists of eigenvalues

        EXAMPLES::

            sage: n = numerical_eigenforms(1,12)
            sage: n.eigenvalues([3,5,13])  # rel tol 2.4e-10
            [[177148.0, 252.00000000001896], [48828126.0, 4830.000000001376], [1792160394038.0, -577737.9999898539]]
        """
    def systems_of_eigenvalues(self, bound):
        """
        Return all systems of eigenvalues for ``self`` for primes
        up to bound.

        EXAMPLES::

            sage: numerical_eigenforms(61).systems_of_eigenvalues(10)  # rel tol 1e-9
            [[-1.481194304092014,
              0.8060634335253706,
              3.156325174658664,
              0.6751308705666462],
             [-1.0, -2.0, -3.0, 1.0],
             [0.311107817465981,
              2.903211925911551,
              -2.5254275608435184,
              -3.214319743377534],
             [2.1700864866260323,
              -1.7092753594369237,
              -1.6308976138151459,
              -0.460811127189112],
             [3.0, 4.0, 6.0, 8.0]]
        """
    def systems_of_abs(self, bound):
        """
        Return the absolute values of all systems of eigenvalues for
        ``self`` for primes up to bound.

        EXAMPLES::

            sage: numerical_eigenforms(61).systems_of_abs(10)  # rel tol 1e-9
            [[0.311107817465981, 2.903211925911551, 2.5254275608435184, 3.214319743377534],
             [1.0, 2.0, 3.0, 1.0],
             [1.481194304092014,
              0.8060634335253706,
              3.156325174658664,
              0.6751308705666462],
             [2.1700864866260323,
              1.7092753594369237,
              1.6308976138151459,
              0.460811127189112],
             [3.0, 4.0, 6.0, 8.0]]
        """

def support(v, eps):
    """
    Given a vector `v` and a threshold eps, return all
    indices where `|v|` is larger than eps.

    EXAMPLES::

        sage: sage.modular.modform.numerical.support( numerical_eigenforms(61)._easy_vector(), 1.0 )
        []

        sage: sage.modular.modform.numerical.support( numerical_eigenforms(61)._easy_vector(), 0.5 )
        [0, 4]
    """
