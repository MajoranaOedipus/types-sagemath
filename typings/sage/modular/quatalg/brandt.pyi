from _typeshed import Incomplete
from sage.arith.misc import gcd as gcd, kronecker as kronecker, next_prime as next_prime, prime_divisors as prime_divisors
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.verbose import verbose as verbose
from sage.modular.dirichlet import TrivialCharacter as TrivialCharacter
from sage.modular.hecke.ambient_module import AmbientHeckeModule as AmbientHeckeModule
from sage.modular.hecke.element import HeckeModuleElement as HeckeModuleElement
from sage.modular.hecke.submodule import HeckeSubmodule as HeckeSubmodule
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

cache: Incomplete

def BrandtModule(N, M: int = 1, weight: int = 2, base_ring=..., use_cache: bool = True):
    """
    Return the Brandt module of given weight associated to the prime
    power `p^r` and integer `M`, where `p` and `M` are coprime.

    INPUT:

    - ``N`` -- a product of primes with odd exponents
    - ``M`` -- integer coprime to `q` (default: 1)
    - ``weight`` -- integer that is at least 2 (default: 2)
    - ``base_ring`` -- the base ring (default: ``QQ``)
    - ``use_cache`` -- whether to use the cache (default: ``True``)

    OUTPUT: a Brandt module

    EXAMPLES::

        sage: BrandtModule(17)
        Brandt module of dimension 2 of level 17 of weight 2 over Rational Field
        sage: BrandtModule(17,15)
        Brandt module of dimension 32 of level 17*15 of weight 2 over Rational Field
        sage: BrandtModule(3,7)
        Brandt module of dimension 2 of level 3*7 of weight 2 over Rational Field
        sage: BrandtModule(3,weight=2)
        Brandt module of dimension 1 of level 3 of weight 2 over Rational Field
        sage: BrandtModule(11, base_ring=ZZ)
        Brandt module of dimension 2 of level 11 of weight 2 over Integer Ring
        sage: BrandtModule(11, base_ring=QQbar)
        Brandt module of dimension 2 of level 11 of weight 2 over Algebraic Field

    The ``use_cache`` option determines whether the Brandt module returned
    by this function is cached::

        sage: BrandtModule(37) is BrandtModule(37)
        True
        sage: BrandtModule(37,use_cache=False) is BrandtModule(37,use_cache=False)
        False

    TESTS:

    Note that `N` and `M` must be coprime::

        sage: BrandtModule(3,15)
        Traceback (most recent call last):
        ...
        ValueError: M must be coprime to N

    Only weight 2 is currently implemented::

        sage: BrandtModule(3,weight=4)
        Traceback (most recent call last):
        ...
        NotImplementedError: weight != 2 not yet implemented

    Brandt modules are cached::

        sage: B = BrandtModule(3,5,2,ZZ)
        sage: B is BrandtModule(3,5,2,ZZ)
        True
    """
def class_number(p, r, M):
    """
    Return the class number of an order of level `N = p^r M` in the
    quaternion algebra over `\\QQ` ramified precisely at `p` and infinity.

    This is an implementation of Theorem 1.12 of [Piz1980]_.

    INPUT:

    - ``p`` -- a prime
    - ``r`` -- an odd positive integer (default: 1)
    - ``M`` -- integer coprime to `q` (default: 1)

    OUTPUT: integer

    EXAMPLES::

        sage: sage.modular.quatalg.brandt.class_number(389,1,1)
        33
        sage: sage.modular.quatalg.brandt.class_number(389,1,2)  # TODO -- right?
        97
        sage: sage.modular.quatalg.brandt.class_number(389,3,1)  # TODO -- right?
        4892713
    """
def maximal_order(A):
    """
    Return a maximal order in the quaternion algebra ramified
    at `p` and infinity.

    This is an implementation of Proposition 5.2 of [Piz1980]_.

    INPUT:

    - ``A`` -- quaternion algebra ramified precisely at `p` and infinity

    OUTPUT: a maximal order in `A`

    EXAMPLES::

        sage: A = BrandtModule(17).quaternion_algebra()

        sage: sage.modular.quatalg.brandt.maximal_order(A)
        doctest:...:  DeprecationWarning: The function maximal_order() is deprecated, use the maximal_order() method of quaternion algebras
        See https://github.com/sagemath/sage/issues/37090 for details.
        Order of Quaternion Algebra (-3, -17) with base ring Rational Field with basis (1/2 + 1/2*i, 1/2*j - 1/2*k, -1/3*i + 1/3*k, -k)

        sage: A = QuaternionAlgebra(17,names='i,j,k')
        sage: A.maximal_order()
        Order of Quaternion Algebra (-3, -17) with base ring Rational Field with basis (1/2 + 1/2*i, 1/2*j - 1/2*k, -1/3*i + 1/3*k, -k)
    """
def basis_for_left_ideal(R, gens):
    """
    Return a basis for the left ideal of `R` with given generators.

    INPUT:

    - ``R`` -- quaternion order
    - ``gens`` -- list of elements of `R`

    OUTPUT: list of four elements of `R`

    EXAMPLES::

        sage: B = BrandtModule(17); A = B.quaternion_algebra(); i,j,k = A.gens()
        sage: sage.modular.quatalg.brandt.basis_for_left_ideal(B.maximal_order(), [i+j,i-j,2*k,A(3)])
        doctest:...:  DeprecationWarning: The function basis_for_left_ideal() is deprecated, use the _left_ideal_basis() method of quaternion algebras
        See https://github.com/sagemath/sage/issues/37090 for details.
        [1, 1/2 + 1/2*i, j, 1/3*i + 1/2*j + 1/6*k]
        sage: sage.modular.quatalg.brandt.basis_for_left_ideal(B.maximal_order(), [3*(i+j),3*(i-j),6*k,A(3)])
        [3, 3/2 + 3/2*i, 3*j, i + 3/2*j + 1/2*k]
    """
def right_order(R, basis):
    """
    Given a basis for a left ideal `I`, return the right order in the
    quaternion order `R` of elements `x` such that `I x` is contained in `I`.

    INPUT:

    - ``R`` -- order in quaternion algebra
    - ``basis`` -- basis for an ideal `I`

    OUTPUT: order in quaternion algebra

    EXAMPLES:

    We do a consistency check with the ideal equal to a maximal order::

        sage: B = BrandtModule(17); basis = B.maximal_order()._left_ideal_basis([1])
        sage: sage.modular.quatalg.brandt.right_order(B.maximal_order(), basis)
        doctest:...:  DeprecationWarning: The function right_order() is deprecated, use the _right_order_from_ideal_basis() method of quaternion algebras
        See https://github.com/sagemath/sage/issues/37090 for details.
        Order of Quaternion Algebra (-3, -17) with base ring Rational Field with basis (1/2 + 1/6*i + 1/3*k, 1/3*i + 2/3*k, 1/2*j + 1/2*k, k)
        sage: basis
        [1, 1/2 + 1/2*i, j, 1/3*i + 1/2*j + 1/6*k]

        sage: B = BrandtModule(17); A = B.quaternion_algebra(); i,j,k = A.gens()
        sage: basis = B.maximal_order()._left_ideal_basis([i*j - j])
        sage: sage.modular.quatalg.brandt.right_order(B.maximal_order(), basis)
        Order of Quaternion Algebra (-3, -17) with base ring Rational Field with basis (1/2 + 1/6*i + 1/3*k, 1/3*i + 2/3*k, 1/2*j + 1/2*k, k)
    """
def quaternion_order_with_given_level(A, level):
    """
    Return an order in the quaternion algebra A with given level.

    This is implemented only when the base field is the rational numbers.

    INPUT:

    - ``level`` -- the level of the order to be returned. Currently this
      is only implemented when the level is divisible by at
      most one power of a prime that ramifies in this quaternion algebra.

    EXAMPLES::

        sage: from sage.modular.quatalg.brandt import quaternion_order_with_given_level, maximal_order
        sage: A.<i,j,k> = QuaternionAlgebra(5)
        sage: level = 2 * 5 * 17
        sage: O = quaternion_order_with_given_level(A, level)
        doctest:...:  DeprecationWarning: The function quaternion_order_with_given_level() is deprecated, use the order_with_level() method of quaternion algebras
        See https://github.com/sagemath/sage/issues/37090 for details.
        sage: M = A.maximal_order()
        sage: L = O.free_module()
        sage: N = M.free_module()
        sage: L.index_in(N) == level/5  #check that the order has the right index in the maximal order
        True
    """

class BrandtSubmodule(HeckeSubmodule): ...

class BrandtModuleElement(HeckeModuleElement):
    def __init__(self, parent, x) -> None:
        """
        EXAMPLES::

            sage: B = BrandtModule(37)
            sage: x = B([1,2,3]); x
            (1, 2, 3)
            sage: parent(x)
            Brandt module of dimension 3 of level 37 of weight 2 over Rational Field
        """
    def monodromy_pairing(self, x):
        """
        Return the monodromy pairing of ``self`` and ``x``.

        EXAMPLES::

            sage: B = BrandtModule(5,13)
            sage: B.monodromy_weights()
            (1, 3, 1, 1, 1, 3)
            sage: (B.0 + B.1).monodromy_pairing(B.0 + B.1)
            4

        TESTS:

        One check for :issue:`12866`::

            sage: Br = BrandtModule(2,7)
            sage: g1, g2 = Br.basis()
            sage: g = g1 - g2
            sage: g.monodromy_pairing(g)
            6
        """
    def __mul__(self, right):
        """
        Return the monodromy pairing of ``self`` and ``right``.

        EXAMPLES::

            sage: B = BrandtModule(7,10)
            sage: B.monodromy_weights()
            (1, 1, 1, 2, 1, 1, 2, 1, 1, 1)
            sage: B.0 * B.0
            1
            sage: B.3 * B.3
            2
            sage: (B.0+B.3) * (B.0 + B.1 + 2*B.3)
            5
        """

class BrandtModule_class(AmbientHeckeModule):
    """
    A Brandt module.

    EXAMPLES::

        sage: BrandtModule(3, 10)
        Brandt module of dimension 4 of level 3*10 of weight 2 over Rational Field
    """
    def __init__(self, N, M, weight, base_ring) -> None:
        """
        INPUT:

        - ``N`` -- ramification number (coprime to M)
        - ``M`` -- auxiliary level
        - ``weight`` -- integer 2
        - ``base_ring`` -- the base ring

        EXAMPLES::

            sage: BrandtModule(3, 5, weight=2, base_ring=ZZ)
            Brandt module of dimension 2 of level 3*5 of weight 2 over Integer Ring
        """
    Element = BrandtModuleElement
    @cached_method
    def free_module(self):
        """
        Return the underlying free module of the Brandt module.

        EXAMPLES::

            sage: B = BrandtModule(10007,389)
            sage: B.free_module()
            Vector space of dimension 325196 over Rational Field
        """
    def N(self):
        """
        Return ramification level `N`.

        EXAMPLES::

            sage: BrandtModule(7,5,2,ZZ).N()
            7
        """
    def M(self):
        """
        Return the auxiliary level (prime to `p` part) of the quaternion
        order used to compute this Brandt module.

        EXAMPLES::

            sage: BrandtModule(7,5,2,ZZ).M()
            5
        """
    def character(self):
        """
        The character of this space.

        Always trivial.

        EXAMPLES::

            sage: BrandtModule(11,5).character()
            Dirichlet character modulo 55 of conductor 1 mapping 12 |--> 1, 46 |--> 1
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        EXAMPLES::

            sage: BrandtModule(37, 5, 2, ZZ) == BrandtModule(37, 5, 2, QQ)
            False
            sage: BrandtModule(37, 5, 2, ZZ) == BrandtModule(37, 5, 2, ZZ)
            True
            sage: BrandtModule(37, 5, 2, ZZ) == loads(dumps(BrandtModule(37, 5, 2, ZZ)))
            True
        """
    @cached_method
    def quaternion_algebra(self):
        """
        Return the quaternion algebra `A` over `\\QQ` ramified precisely at
        `p` and infinity used to compute this Brandt module.

        EXAMPLES::

            sage: BrandtModule(997).quaternion_algebra()
            Quaternion Algebra (-2, -997) with base ring Rational Field
            sage: BrandtModule(2).quaternion_algebra()
            Quaternion Algebra (-1, -1) with base ring Rational Field
            sage: BrandtModule(3).quaternion_algebra()
            Quaternion Algebra (-1, -3) with base ring Rational Field
            sage: BrandtModule(5).quaternion_algebra()
            Quaternion Algebra (-2, -5) with base ring Rational Field
            sage: BrandtModule(17).quaternion_algebra()
            Quaternion Algebra (-3, -17) with base ring Rational Field
        """
    def maximal_order(self):
        """
        Return a maximal order in the quaternion algebra associated to this Brandt module.

        EXAMPLES::

            sage: BrandtModule(17).maximal_order()
            Order of Quaternion Algebra (-3, -17) with base ring Rational Field with basis (1/2 + 1/2*i, 1/2*j - 1/2*k, -1/3*i + 1/3*k, -k)
            sage: BrandtModule(17).maximal_order() is BrandtModule(17).maximal_order()
            True
        """
    @cached_method
    def order_of_level_N(self):
        """
        Return an order of level `N = p^{2 r + 1} M` in the
        quaternion algebra.

        EXAMPLES::

            sage: BrandtModule(7).order_of_level_N()
            Order of Quaternion Algebra (-1, -7) with base ring Rational Field with basis (1/2 + 1/2*j, 1/2*i + 1/2*k, j, k)
            sage: BrandtModule(7,13).order_of_level_N()
            Order of Quaternion Algebra (-1, -7) with base ring Rational Field with basis (1/2 + 1/2*j + 12*k, 1/2*i + 9/2*k, j + 11*k, 13*k)
            sage: BrandtModule(7,3*17).order_of_level_N()
            Order of Quaternion Algebra (-1, -7) with base ring Rational Field with basis (1/2 + 1/2*j + 35*k, 1/2*i + 65/2*k, j + 19*k, 51*k)
        """
    def cyclic_submodules(self, I, p):
        """
        Return a list of rescaled versions of the fractional right
        ideals `J` such that `J` contains `I` and the quotient has
        group structure the product of two cyclic groups of order `p`.

        We emphasize again that `J` is rescaled to be integral.

        INPUT:

        - ``I`` -- ideal `I` in ``R = self.order_of_level_N()``
        - ``p`` -- prime `p` coprime to ``self.level()``

        OUTPUT:

        list of the `p+1` fractional right R-ideals that contain I
        such that J/I is GF(p) x GF(p).

        EXAMPLES::

            sage: B = BrandtModule(11)
            sage: I = B.order_of_level_N().unit_ideal()
            sage: B.cyclic_submodules(I, 2)
            [Fractional ideal (2, 2*i, 3/2 + i + 1/2*j, 1 + 1/2*i + 1/2*k),
             Fractional ideal (2, 1 + i, 1 + j, 1/2 + 1/2*i + 1/2*j + 1/2*k),
             Fractional ideal (2, 2*i, 1/2 + i + 1/2*j, 1 + 3/2*i + 1/2*k)]
            sage: B.cyclic_submodules(I, 3)
            [Fractional ideal (3, 3*i, 1/2 + 1/2*j, 5/2*i + 1/2*k),
             Fractional ideal (3, 3*i, 3/2 + 2*i + 1/2*j, 2 + 3/2*i + 1/2*k),
             Fractional ideal (3, 3*i, 3/2 + i + 1/2*j, 1 + 3/2*i + 1/2*k),
             Fractional ideal (3, 3*i, 5/2 + 1/2*j, 1/2*i + 1/2*k)]
            sage: B.cyclic_submodules(I, 11)
            Traceback (most recent call last):
            ...
            ValueError: p must be coprime to the level
        """
    def hecke_matrix(self, n, algorithm: str = 'default', sparse: bool = False, B=None):
        """
        Return the matrix of the `n`-th Hecke operator.

        INPUT:

        - ``n`` -- integer

        - ``algorithm`` -- string (default: ``'default'``)

           - ``'default'`` -- let Sage guess which algorithm is best

           - ``'direct'`` -- use cyclic subideals (generally much
             better when you want few Hecke operators and the
             dimension is very large); uses 'theta' if n divides
             the level.

           - ``'brandt'`` -- use Brandt matrices (generally much
             better when you want many Hecke operators and the
             dimension is very small; bad when the dimension
             is large)

        - ``sparse`` -- boolean (default: ``False``)

        - ``B`` -- integer or ``None`` (default: ``None``); in direct
          algorithm, use theta series to this precision as an initial
          check for equality of ideal classes.

        EXAMPLES::

            sage: B = BrandtModule(3,7); B.hecke_matrix(2)
            [0 3]
            [1 2]
            sage: B.hecke_matrix(5, algorithm='brandt')
            [0 6]
            [2 4]
            sage: t = B.hecke_matrix(11, algorithm='brandt', sparse=True); t
            [ 6  6]
            [ 2 10]
            sage: type(t)
            <class 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
            sage: B.hecke_matrix(19, algorithm='direct', B=2)
            [ 8 12]
            [ 4 16]
        """
    @cached_method
    def right_ideals(self, B=None):
        """
        Return sorted tuple of representatives for the equivalence
        classes of right ideals in ``self``.

        OUTPUT: sorted tuple of fractional ideals

        EXAMPLES::

            sage: B = BrandtModule(23)
            sage: B.right_ideals()
            (Fractional ideal (4, 4*i, 2 + 2*j, 2*i + 2*k),
             Fractional ideal (8, 8*i, 2 + 2*j, 6*i + 2*k),
             Fractional ideal (16, 16*i, 10 + 8*i + 2*j, 8 + 6*i + 2*k))

        TESTS::

            sage: B = BrandtModule(1009)
            sage: Is = B.right_ideals()
            sage: n = len(Is)
            sage: prod(not Is[i].is_right_equivalent(Is[j]) for i in range(n) for j in range(i))
            1
        """
    def brandt_series(self, prec, var: str = 'q'):
        """
        Return matrix of power series `\\sum T_n q^n` to the given
        precision.

        Note that the Hecke operators in this series are
        always over `\\QQ`, even if the base ring of this Brandt module
        is not `\\QQ`.

        INPUT:

        - ``prec`` -- positive integer
        - ``var`` -- string (default: `q`)

        OUTPUT: matrix of power series with coefficients in `\\QQ`

        EXAMPLES::

            sage: B = BrandtModule(11)
            sage: B.brandt_series(2)
            [1/4 + q + O(q^2)     1/4 + O(q^2)]
            [    1/6 + O(q^2) 1/6 + q + O(q^2)]
            sage: B.brandt_series(5)
            [1/4 + q + q^2 + 2*q^3 + 5*q^4 + O(q^5)   1/4 + 3*q^2 + 3*q^3 + 3*q^4 + O(q^5)]
            [  1/6 + 2*q^2 + 2*q^3 + 2*q^4 + O(q^5)         1/6 + q + q^3 + 4*q^4 + O(q^5)]


        Asking for a smaller precision works::

            sage: B.brandt_series(3)
            [1/4 + q + q^2 + O(q^3)   1/4 + 3*q^2 + O(q^3)]
            [  1/6 + 2*q^2 + O(q^3)       1/6 + q + O(q^3)]
            sage: B.brandt_series(3,var='t')
            [1/4 + t + t^2 + O(t^3)   1/4 + 3*t^2 + O(t^3)]
            [  1/6 + 2*t^2 + O(t^3)       1/6 + t + O(t^3)]
        """
    @cached_method
    def eisenstein_subspace(self):
        """
        Return the 1-dimensional subspace of ``self`` on which the Hecke
        operators `T_p` act as `p+1` for `p` coprime to the level.

        .. NOTE::

            This function assumes that the base field has
            characteristic 0.

        EXAMPLES::

            sage: B = BrandtModule(11); B.eisenstein_subspace()
            Subspace of dimension 1 of Brandt module of dimension 2 of level 11 of weight 2 over Rational Field
            sage: B.eisenstein_subspace() is B.eisenstein_subspace()
            True
            sage: BrandtModule(3,11).eisenstein_subspace().basis()
            ((1, 1),)
            sage: BrandtModule(7,10).eisenstein_subspace().basis()
            ((1, 1, 1, 1/2, 1, 1, 1/2, 1, 1, 1),)
            sage: BrandtModule(7,10,base_ring=ZZ).eisenstein_subspace().basis()
            ((2, 2, 2, 1, 2, 2, 1, 2, 2, 2),)
        """
    def is_cuspidal(self) -> bool:
        """
        Return whether ``self`` is cuspidal, i.e. has no Eisenstein part.

        EXAMPLES::

            sage: B = BrandtModule(3, 4)
            sage: B.is_cuspidal()
            False
            sage: B.eisenstein_subspace()
            Brandt module of dimension 1 of level 3*4 of weight 2 over Rational Field
        """
    @cached_method
    def monodromy_weights(self):
        """
        Return the weights for the monodromy pairing on this Brandt
        module.

        The weights are associated to each ideal class in our
        fixed choice of basis. The weight of an ideal class `[I]` is
        half the number of units of the right order `I`.

        .. NOTE:: The base ring must be `\\QQ` or `\\ZZ`.

        EXAMPLES::

            sage: BrandtModule(11).monodromy_weights()
            (2, 3)
            sage: BrandtModule(37).monodromy_weights()
            (1, 1, 1)
            sage: BrandtModule(43).monodromy_weights()
            (2, 1, 1, 1)
            sage: BrandtModule(7,10).monodromy_weights()
            (1, 1, 1, 2, 1, 1, 2, 1, 1, 1)
            sage: BrandtModule(5,13).monodromy_weights()
            (1, 3, 1, 1, 1, 3)
            sage: BrandtModule(2).monodromy_weights()
            (12,)
            sage: BrandtModule(2,7).monodromy_weights()
            (3, 3)
        """

def benchmark_magma(levels, silent: bool = False):
    """
    INPUT:

    - ``levels`` -- list of pairs `(p,M)` where `p` is a prime not
      dividing `M`
    - ``silent`` -- boolean (default: ``False``); if ``True`` suppress
      printing during computation

    OUTPUT:

    list of 4-tuples ('magma', p, M, tm), where tm is the
    CPU time in seconds to compute T2 using Magma

    EXAMPLES::

        sage: a = sage.modular.quatalg.brandt.benchmark_magma([(11,1), (37,1), (43,1), (97,1)])  # optional - magma
        ('magma', 11, 1, ...)
        ('magma', 37, 1, ...)
        ('magma', 43, 1, ...)
        ('magma', 97, 1, ...)
        sage: a = sage.modular.quatalg.brandt.benchmark_magma([(11,2), (37,2), (43,2), (97,2)])  # optional - magma
        ('magma', 11, 2, ...)
        ('magma', 37, 2, ...)
        ('magma', 43, 2, ...)
        ('magma', 97, 2, ...)
    """
def benchmark_sage(levels, silent: bool = False):
    """
    INPUT:

    - ``levels`` -- list of pairs `(p,M)` where `p` is a prime
      not dividing `M`
    - ``silent`` -- boolean (default: ``False``); if ``True`` suppress
      printing during computation

    OUTPUT:

    list of 4-tuples ('sage', p, M, tm), where tm is the
    CPU time in seconds to compute T2 using Sage

    EXAMPLES::

        sage: a = sage.modular.quatalg.brandt.benchmark_sage([(11,1), (37,1), (43,1), (97,1)])
        ('sage', 11, 1, ...)
        ('sage', 37, 1, ...)
        ('sage', 43, 1, ...)
        ('sage', 97, 1, ...)
        sage: a = sage.modular.quatalg.brandt.benchmark_sage([(11,2), (37,2), (43,2), (97,2)])
        ('sage', 11, 2, ...)
        ('sage', 37, 2, ...)
        ('sage', 43, 2, ...)
        ('sage', 97, 2, ...)
    """
