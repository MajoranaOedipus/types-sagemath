from .weightspace import WeightCharacter as WeightCharacter
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.matrix.special import diagonal_matrix as diagonal_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_class as Gamma1_class
from sage.modular.dirichlet import trivial_character as trivial_character
from sage.modular.etaproducts import EtaProduct as EtaProduct
from sage.modular.modform.element import ModularFormElement as ModularFormElement
from sage.modular.modform.hecke_operator_on_qexp import hecke_operator_on_qexp as hecke_operator_on_qexp
from sage.modules.free_module_element import vector as vector
from sage.modules.module import Module as Module
from sage.rings.big_oh import O as O
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import ModuleElement as ModuleElement, Vector as Vector
from sage.structure.richcmp import richcmp as richcmp
from typing import Iterator

def OverconvergentModularForms(prime, weight, radius, base_ring=..., prec: int = 20, char=None):
    """
    Create a space of overconvergent `p`-adic modular forms of level
    `\\Gamma_0(p)`, over the given base ring. The base ring need not be a
    `p`-adic ring (the spaces we compute with typically have bases over
    `\\QQ`).

    INPUT:

    - ``prime`` -- a prime number `p`, which must be one of the primes `\\{2, 3,
      5, 7, 13\\}`, or the congruence subgroup `\\Gamma_0(p)` where `p` is one of
      these primes

    - ``weight`` -- integer (which at present must be 0 or `\\ge 2`), the
      weight

    - ``radius`` -- a rational number in the interval `\\left( 0, \\frac{p}{p+1}
      \\right)`, the radius of overconvergence

    - ``base_ring`` -- (default: `\\QQ`), a ring over which to compute; this
      need not be a `p`-adic ring

    - ``prec`` -- integer (default: 20); the number of `q`-expansion terms to
      compute

    - ``char`` -- a Dirichlet character modulo `p` or ``None`` (the default);
      here ``None`` is interpreted as the trivial character modulo `p`

    The character `\\chi` and weight `k` must satisfy `(-1)^k = \\chi(-1)`, and
    the base ring must contain an element `v` such that
    `{\\rm ord}_p(v) = \\frac{12 r}{p-1}` where `r` is the radius of
    overconvergence (and `{\\rm ord}_p` is normalised so `{\\rm ord}_p(p) = 1`).

    EXAMPLES::

        sage: OverconvergentModularForms(3, 0, 1/2)
        Space of 3-adic 1/2-overconvergent modular forms
         of weight-character 0 over Rational Field
        sage: OverconvergentModularForms(3, 16, 1/2)
        Space of 3-adic 1/2-overconvergent modular forms
         of weight-character 16 over Rational Field
        sage: OverconvergentModularForms(3, 3, 1/2, char=DirichletGroup(3,QQ).0)
        Space of 3-adic 1/2-overconvergent modular forms
         of weight-character (3, 3, [-1]) over Rational Field
    """

class OverconvergentModularFormsSpace(Module):
    """
    A space of overconvergent modular forms of level `\\Gamma_0(p)`,
    where `p` is a prime such that `X_0(p)` has genus 0.

    Elements are represented as power series, with a formal power series `F`
    corresponding to the modular form `E_k^\\ast \\times F(g)` where `E_k^\\ast`
    is the `p`-deprived Eisenstein series of weight-character `k`, and `g` is a
    uniformiser of `X_0(p)` normalised so that the `r`-overconvergent region
    `X_0(p)_{\\ge r}` corresponds to `|g| \\le 1`.

    TESTS::

        sage: x = polygen(ZZ, 'x')
        sage: K.<w> = Qp(13).extension(x^2 - 13); M = OverconvergentModularForms(13, 20, radius=1/2, base_ring=K)
        sage: M is loads(dumps(M))
        True
    """
    def __init__(self, prime, weight, radius, base_ring, prec, char) -> None:
        """
        Create a space of overconvergent `p`-adic modular forms of level
        `\\Gamma_0(p)`, over the given base ring.

        The base ring need not be a
        `p`-adic ring (the spaces we compute with typically have bases over
        `\\QQ`).

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2); M
            Space of 3-adic 1/2-overconvergent modular forms of weight-character 0 over Rational Field
            sage: TestSuite(M).run()
        """
    def is_exact(self) -> bool:
        """
        Return ``True`` if elements of this space are represented exactly.

        This would mean that there is no precision loss when doing arithmetic.
        As this is never true for overconvergent modular forms spaces,
        this method returns ``False``.

        EXAMPLES::

            sage: OverconvergentModularForms(13, 12, 0).is_exact()
            False
        """
    def change_ring(self, ring):
        """
        Return the space corresponding to ``self`` but over the given base ring.

        EXAMPLES::

            sage: M = OverconvergentModularForms(2, 0, 1/2)
            sage: M.change_ring(Qp(2))
            Space of 2-adic 1/2-overconvergent modular forms of weight-character 0
             over 2-adic Field with ...
        """
    def base_extend(self, ring):
        """
        Return the base extension of ``self`` to the given base ring.

        There must be a canonical map to this ring from the current
        base ring, otherwise a :exc:`TypeError` will be raised.

        EXAMPLES::

            sage: M = OverconvergentModularForms(2, 0, 1/2, base_ring=Qp(2))
            sage: x = polygen(ZZ, 'x')
            sage: M.base_extend(Qp(2).extension(x^2 - 2, names='w'))
            Space of 2-adic 1/2-overconvergent modular forms of weight-character 0
             over 2-adic Eisenstein Extension ...
            sage: M.base_extend(QQ)
            Traceback (most recent call last):
            ...
            TypeError: Base extension of self (over '2-adic Field with capped
            relative precision 20') to ring 'Rational Field' not defined.
        """
    def character(self):
        """
        Return the character of ``self``.

        For overconvergent forms, the weight and the character are unified into
        the concept of a weight-character, so this returns exactly the same
        thing as :meth:`weight`.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 0, 1/2).character()
            0
            sage: type(OverconvergentModularForms(3, 0, 1/2).character())
            <class '...weightspace.AlgebraicWeight'>
            sage: OverconvergentModularForms(3, 3, 1/2, char=DirichletGroup(3,QQ).0).character()
            (3, 3, [-1])
        """
    def weight(self):
        """
        Return the weight of ``self``.

        For overconvergent forms, the weight and the character are unified into
        the concept of a weight-character, so this returns exactly the same
        thing as :meth:`character`.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 0, 1/2).weight()
            0
            sage: type(OverconvergentModularForms(3, 0, 1/2).weight())
            <class '...weightspace.AlgebraicWeight'>
            sage: OverconvergentModularForms(3, 3, 1/2, char=DirichletGroup(3,QQ).0).weight()
            (3, 3, [-1])
        """
    def normalising_factor(self):
        """
        Return the normalising factor of ``self``.

        The normalising factor `c` such that `g = c f` is a parameter for the
        `r`-overconvergent disc in `X_0(p)`, where `f` is the standard
        uniformiser.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<w> = Qp(7).extension(x^2 - 7)
            sage: OverconvergentModularForms(7, 0, 1/4, base_ring=L).normalising_factor()
            w + O(w^41)
        """
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 12, 1/2) == ModularForms(3, 12)
            False
            sage: OverconvergentModularForms(3, 0, 1/2) == OverconvergentModularForms(3, 0, 1/3)
            False
            sage: OverconvergentModularForms(3, 0, 1/2) == OverconvergentModularForms(3, 0, 1/2, base_ring=Qp(3))
            False
            sage: OverconvergentModularForms(3, 0, 1/2) == OverconvergentModularForms(3, 0, 1/2)
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 12, 1/2) != ModularForms(3, 12)
            True
            sage: OverconvergentModularForms(3, 0, 1/2) != OverconvergentModularForms(3, 0, 1/3)
            True
            sage: OverconvergentModularForms(3, 0, 1/2) != OverconvergentModularForms(3, 0, 1/2, base_ring=Qp(3))
            True
            sage: OverconvergentModularForms(3, 0, 1/2) != OverconvergentModularForms(3, 0, 1/2)
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: h1 = hash(OverconvergentModularForms(3, 12, 1/2))
            sage: h2 = hash(OverconvergentModularForms(3, 12, 1/2))
            sage: h3 = hash(OverconvergentModularForms(3, 0, 1/2))
            sage: h1 == h2 and h1 != h3
            True
        """
    def __reduce__(self):
        """
        Return the function and arguments used to construct ``self``. Used for pickling.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<w> = Qp(7).extension(x^2 - 7)
            sage: OverconvergentModularForms(7, 0, 1/4, base_ring=L).__reduce__()
            (<function OverconvergentModularForms at ...>,
             (7,
              0,
              1/4,
              7-adic Eisenstein Extension Field in w defined by x^2 - 7,
              20,
              Dirichlet character modulo 7 of conductor 1 mapping 3 |--> 1))
        """
    def gen(self, i):
        """
        Return the `i`-th module generator of ``self``.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 2, 1/2, prec=4)
            sage: M.gen(0)
            3-adic overconvergent modular form of weight-character 2
             with q-expansion 1 + 12*q + 36*q^2 + 12*q^3 + O(q^4)
            sage: M.gen(1)
            3-adic overconvergent modular form of weight-character 2
             with q-expansion 27*q + 648*q^2 + 7290*q^3 + O(q^4)
            sage: M.gen(30)
            3-adic overconvergent modular form of weight-character 2
             with q-expansion O(q^4)
        """
    def prime(self):
        """
        Return the residue characteristic of ``self``.

        This is the prime `p` such that this is a `p`-adic space.

        EXAMPLES::

            sage: OverconvergentModularForms(5, 12, 1/3).prime()
            5
        """
    def radius(self):
        """
        The radius of overconvergence of this space.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 0, 1/3).radius()
            1/3
        """
    def gens(self) -> Iterator:
        """
        Return a generator object that iterates over the (infinite) set of
        basis vectors of ``self``.

        EXAMPLES::

            sage: o = OverconvergentModularForms(3, 12, 1/2)
            sage: t = o.gens()
            sage: next(t)
            3-adic overconvergent modular form of weight-character 12 with q-expansion
            1 - 32760/61203943*q - 67125240/61203943*q^2 - ...
            sage: next(t)
            3-adic overconvergent modular form of weight-character 12 with q-expansion
            27*q + 19829193012/61203943*q^2 + 146902585770/61203943*q^3 + ...
        """
    def prec(self):
        """
        Return the series precision of ``self``.

        Note that this is different from the `p`-adic precision of the base ring.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 0, 1/2).prec()
            20
            sage: OverconvergentModularForms(3, 0, 1/2, prec=40).prec()
            40
        """
    @cached_method
    def zero(self):
        """
        Return the zero of this space.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<w> = Qp(13).extension(x^2 - 13)
            sage: M = OverconvergentModularForms(13, 20, radius=1/2, base_ring=K)
            sage: K.zero()
            0
        """
    def coordinate_vector(self, x):
        """
        Write ``x`` as a vector with respect to the basis given by ``self.basis()``.

        Here ``x`` must be an element of this space or something that can be
        converted into one. If ``x`` has precision less than the default precision
        of ``self``, then the returned vector will be shorter.

        EXAMPLES::

            sage: M = OverconvergentModularForms(Gamma0(3), 0, 1/3, prec=4)
            sage: M.coordinate_vector(M.gen(2))
            (0, 0, 1, 0)
            sage: q = QQ[['q']].gen(); M.coordinate_vector(q - q^2 + O(q^4))
            (0, 1/9, -13/81, 74/243)
            sage: M.coordinate_vector(q - q^2 + O(q^3))
            (0, 1/9, -13/81)
        """
    def ngens(self):
        """
        The number of generators of ``self`` (as a module over its base ring), i.e. infinity.

        EXAMPLES::

            sage: M = OverconvergentModularForms(2, 4, 1/6)
            sage: M.ngens()
            +Infinity
        """
    def hecke_operator(self, f, m):
        '''
        Given an element `f` and an integer `m`, calculates the Hecke operator
        `T_m` acting on `f`.

        The input may be either a "bare" power series, or an
        :class:`OverconvergentModularFormElement` object; the return value will be of
        the same type.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2)
            sage: f = M.1
            sage: M.hecke_operator(f, 3)
            3-adic overconvergent modular form of weight-character 0 with q-expansion
            2430*q + 265356*q^2 + 10670373*q^3 + 249948828*q^4 + 4113612864*q^5
             + 52494114852*q^6 + O(q^7)
            sage: M.hecke_operator(f.q_expansion(), 3)
            2430*q + 265356*q^2 + 10670373*q^3 + 249948828*q^4 + 4113612864*q^5
             + 52494114852*q^6 + O(q^7)
        '''
    def hecke_matrix(self, m, n, use_recurrence: bool = False, exact_arith: bool = False, side: str = 'left'):
        """
        Calculate the matrix of the `T_m` operator, truncated to `n \\times n`.

        INPUT:

        - ``m`` -- integer; determines the operator `T_m`

        - ``n`` -- integer; truncate the matrix in the basis of this space
          to an `n \\times n` matrix

        - ``use_recurrence`` -- boolean (default: ``False``); whether to use
          Kolberg style recurrences. If ``False``, use naive `q`-expansion
          arguments.

        - ``exact_arith`` -- boolean (default: ``True``); whether to do the
          computation to be done with rational arithmetic, even if the base ring
          is an inexact `p`-adic ring.

          This is useful as there can be precision loss issues (particularly
          with ``use_recurrence=False``).

        - ``side`` -- ``'left'`` (default) or ``'right'``; if ``'left'``, the
          operator acts on the left on column vectors

        EXAMPLES::

            sage: OverconvergentModularForms(2, 0, 1/2).hecke_matrix(2, 4)
            [    1     0     0     0]
            [    0    24    64     0]
            [    0    32  1152  4608]
            [    0     0  3072 61440]
            sage: o = OverconvergentModularForms(2, 12, 1/2, base_ring=pAdicField(2))
            sage: o.hecke_matrix(2, 3) * (1 + O(2^2))
            [        1 + O(2^2)                  0                  0]
            [                 0       2^3 + O(2^5)       2^6 + O(2^8)]
            [                 0       2^4 + O(2^6) 2^7 + 2^8 + O(2^9)]
            sage: o = OverconvergentModularForms(2, 12, 1/2, base_ring=pAdicField(2))
            sage: o.hecke_matrix(2, 3, exact_arith=True)
            [                             1                              0                              0]
            [                             0               33881928/1414477                             64]
            [                             0 -192898739923312/2000745183529             1626332544/1414477]

        Side switch::

            sage: OverconvergentModularForms(2, 0, 1/2).hecke_matrix(2, 4, side='right')
            [    1     0     0     0]
            [    0    24    32     0]
            [    0    64  1152  3072]
            [    0     0  4608 61440]
        """
    def slopes(self, n, use_recurrence: bool = False):
        """
        Compute the slopes of the `U_p` operator acting on ``self``, using an `n\\times n` matrix.

        EXAMPLES::

            sage: OverconvergentModularForms(5, 2, 1/3, base_ring=Qp(5), prec=100).slopes(5)
            [0, 2, 5, 6, 9]
            sage: OverconvergentModularForms(2, 1, 1/3, char=DirichletGroup(4,QQ).0).slopes(5)
            [0, 2, 4, 6, 8]
        """
    def eigenfunctions(self, n, F=None, exact_arith: bool = True):
        """
        Calculate approximations to eigenfunctions of ``self``.

        These are the eigenfunctions of ``self.hecke_matrix(p, n)``, which
        are approximations to the true eigenfunctions. Returns a list
        of :class:`OverconvergentModularFormElement` objects, in increasing
        order of slope.

        INPUT:

        - ``n`` -- integer; the size of the matrix to use

        - ``F`` -- either ``None`` or a field over which to calculate eigenvalues. If the
          field is ``None``, the current base ring is used. If the base ring is not
          a `p`-adic ring, an error will be raised.

        - ``exact_arith`` -- boolean (default: ``True``); if ``True``, use exact
          rational arithmetic to calculate the matrix of the `U` operator and its
          characteristic power series, even when the base ring is an inexact
          `p`-adic ring. This is typically slower, but more numerically stable.

        NOTE: Try using ``set_verbose(1, 'sage/modular/overconvergent')`` to
        get more feedback on what is going on in this algorithm. For even more
        feedback, use 2 instead of 1.

        EXAMPLES::

            sage: X = OverconvergentModularForms(2, 2, 1/6).eigenfunctions(8, Qp(2, 100))
            sage: X[1]
            2-adic overconvergent modular form of weight-character 2 with q-expansion
            (1 + O(2^74))*q
             + (2^4 + 2^5 + 2^9 + 2^10 + 2^12 + 2^13 + 2^15 + 2^17 + 2^19 + 2^20
                 + 2^21 + 2^23 + 2^28 + 2^30 + 2^31 + 2^32 + 2^34 + 2^36 + 2^37
                 + 2^39 + 2^40 + 2^43 + 2^44 + 2^45 + 2^47 + 2^48 + 2^52 + 2^53
                 + 2^54 + 2^55 + 2^56 + 2^58 + 2^59 + 2^60 + 2^61 + 2^67 + 2^68
                 + 2^70 + 2^71 + 2^72 + 2^74 + 2^76 + O(2^78))*q^2
             + (2^2 + 2^7 + 2^8 + 2^9 + 2^12 + 2^13 + 2^16 + 2^17 + 2^21 + 2^23
                 + 2^25 + 2^28 + 2^33 + 2^34 + 2^36 + 2^37 + 2^42 + 2^45 + 2^47
                 + 2^49 + 2^50 + 2^51 + 2^54 + 2^55 + 2^58 + 2^60 + 2^61 + 2^67
                 + 2^71 + 2^72 + O(2^76))*q^3
             + (2^8 + 2^11 + 2^14 + 2^19 + 2^21 + 2^22 + 2^24 + 2^25 + 2^26
                 + 2^27 + 2^28 + 2^29 + 2^32 + 2^33 + 2^35 + 2^36 + 2^44 + 2^45
                 + 2^46 + 2^47 + 2^49 + 2^50 + 2^53 + 2^54 + 2^55 + 2^56 + 2^57
                 + 2^60 + 2^63 + 2^66 + 2^67 + 2^69 + 2^74 + 2^76 + 2^79 + 2^80
                 + 2^81 + O(2^82))*q^4
             + (2 + 2^2 + 2^9 + 2^13 + 2^15 + 2^17 + 2^19 + 2^21 + 2^23 + 2^26
                 + 2^27 + 2^28 + 2^30 + 2^33 + 2^34 + 2^35 + 2^36 + 2^37 + 2^38
                 + 2^39 + 2^41 + 2^42 + 2^43 + 2^45 + 2^58 + 2^59 + 2^60 + 2^61
                 + 2^62 + 2^63 + 2^65 + 2^66 + 2^68 + 2^69 + 2^71 + 2^72 + O(2^75))*q^5
             + (2^6 + 2^7 + 2^15 + 2^16 + 2^21 + 2^24 + 2^25 + 2^28 + 2^29 + 2^33
                 + 2^34 + 2^37 + 2^44 + 2^45 + 2^48 + 2^50 + 2^51 + 2^54 + 2^55
                 + 2^57 + 2^58 + 2^59 + 2^60 + 2^64 + 2^69 + 2^71 + 2^73 + 2^75
                 + 2^78 + O(2^80))*q^6 + (2^3 + 2^8 + 2^9 + 2^10 + 2^11 + 2^12
                 + 2^14 + 2^15 + 2^17 + 2^19 + 2^20 + 2^21 + 2^23 + 2^25 + 2^26
                 + 2^34 + 2^37 + 2^38 + 2^39 + 2^40 + 2^41 + 2^45 + 2^47 + 2^49
                 + 2^51 + 2^53 + 2^54 + 2^55 + 2^57 + 2^58 + 2^59 + 2^60 + 2^61
                 + 2^66 + 2^69 + 2^70 + 2^71 + 2^74 + 2^76 + O(2^77))*q^7
             + O(q^8)
            sage: [x.slope() for x in X]
            [0, 4, 8, 14, 16, 18, 26, 30]
        """
    def recurrence_matrix(self, use_smithline: bool = True):
        """
        Return the recurrence matrix satisfied by the coefficients of `U`.

        This is a matrix `R =(r_{rs})_{r,s=1,\\dots,p}` such that `u_{ij} =
        \\sum_{r,s=1}^p r_{rs} u_{i-r, j-s}`.

        Uses an elegant construction which the author believes to be due
        to Smithline. See [Loe2007]_.

        EXAMPLES::

            sage: OverconvergentModularForms(2, 0, 0).recurrence_matrix()
            [  48    1]
            [4096    0]
            sage: OverconvergentModularForms(2, 0, 1/2).recurrence_matrix()
            [48 64]
            [64  0]
            sage: OverconvergentModularForms(3, 0, 0).recurrence_matrix()
            [   270     36      1]
            [ 26244    729      0]
            [531441      0      0]
            sage: OverconvergentModularForms(5, 0, 0).recurrence_matrix()
            [     1575      1300       315        30         1]
            [   162500     39375      3750       125         0]
            [  4921875    468750     15625         0         0]
            [ 58593750   1953125         0         0         0]
            [244140625         0         0         0         0]
            sage: OverconvergentModularForms(7, 0, 0).recurrence_matrix()
            [       4018        8624        5915        1904         322          28           1]
            [     422576      289835       93296       15778        1372          49           0]
            [   14201915     4571504      773122       67228        2401           0           0]
            [  224003696    37882978     3294172      117649           0           0           0]
            [ 1856265922   161414428     5764801           0           0           0           0]
            [ 7909306972   282475249           0           0           0           0           0]
            [13841287201           0           0           0           0           0           0]
            sage: OverconvergentModularForms(13, 0, 0).recurrence_matrix()
            [         15145         124852         354536 ...
        """
    def cps_u(self, n, use_recurrence: bool = False):
        """
        Compute the characteristic power series of `U_p` acting on ``self``, using
        an `n\\times n` matrix.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 16, 1/2, base_ring=Qp(3)).cps_u(4)
            1 + O(3^20)
             + (2 + 2*3 + 2*3^2 + 2*3^4 + 3^5 + 3^6 + 3^7
                 + 3^11 + 3^12 + 2*3^14 + 3^16 + 3^18 + O(3^19))*T
             + (2*3^3 + 3^5 + 3^6 + 3^7 + 2*3^8 + 2*3^9 + 2*3^10
                 + 3^11 + 3^12 + 2*3^13 + 2*3^16 + 2*3^18 + O(3^19))*T^2
             + (2*3^15 + 2*3^16 + 2*3^19 + 2*3^20 + 2*3^21 + O(3^22))*T^3
             + (3^17 + 2*3^18 + 3^19 + 3^20 + 3^22 + 2*3^23 + 2*3^25 + 3^26 + O(3^27))*T^4
            sage: OverconvergentModularForms(3, 16, 1/2, base_ring=Qp(3), prec=30).cps_u(10)
            1 + O(3^20)
             + (2 + 2*3 + 2*3^2 + 2*3^4 + 3^5 + 3^6 + 3^7 + 2*3^15 + O(3^16))*T
             + (2*3^3 + 3^5 + 3^6 + 3^7 + 2*3^8 + 2*3^9 + 2*3^10
                 + 2*3^11 + 2*3^12 + 2*3^13 + 3^14 + 3^15 + O(3^16))*T^2
             + (3^14 + 2*3^15 + 2*3^16 + 3^17 + 3^18 + O(3^19))*T^3
             + (3^17 + 2*3^18 + 3^19 + 3^20 + 3^21 + O(3^24))*T^4
             + (3^29 + 2*3^32 + O(3^33))*T^5
             + (2*3^44 + O(3^45))*T^6
             + (2*3^59 + O(3^60))*T^7
             + (2*3^78 + O(3^79))*T^8

        .. NOTE::

            Uses the Hessenberg form of the Hecke matrix to compute
            the characteristic polynomial.  Because of the use of
            relative precision here this tends to give better
            precision in the `p`-adic coefficients.
        """

class OverconvergentModularFormElement(ModuleElement):
    """
    A class representing an element of a space of overconvergent modular forms.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<w> = Qp(5).extension(x^7 - 5)
        sage: s = OverconvergentModularForms(5, 6, 1/21, base_ring=K).0
        sage: s == loads(dumps(s))
        True
    """
    def __init__(self, parent, gexp=None, qexp=None) -> None:
        """
        Create an element of this space.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 2, 1/6,prec=5).an_element() # indirect doctest
            3-adic overconvergent modular form of weight-character 2
             with q-expansion 3*q + 72*q^2 + 810*q^3 + 6096*q^4 + O(q^5)
        """
    def prec(self):
        """
        Return the series expansion precision of this overconvergent modular form.

        This is not the same as the `p`-adic precision of the coefficients.

        EXAMPLES::

            sage: OverconvergentModularForms(5, 6, 1/3, prec=15).gen(1).prec()
            15
        """
    def is_eigenform(self) -> bool:
        """
        Return ``True`` if this is an eigenform.

        At present this returns ``False`` unless this element was explicitly
        flagged as an eigenform, using the method :meth:`_notify_eigen`.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2)
            sage: f = M.eigenfunctions(3)[1]
            sage: f.is_eigenform()
            True
            sage: M.gen(4).is_eigenform()
            False
        """
    def slope(self):
        """
        Return the slope of this eigenform.

        This is the valuation of its `U_p`-eigenvalue.

        Raises an error unless this element was explicitly
        flagged as an eigenform, using the method :meth:`_notify_eigen`.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2)
            sage: f = M.eigenfunctions(3)[1]
            sage: f.slope()
            2
            sage: M.gen(4).slope()
            Traceback (most recent call last):
            ...
            TypeError: slope only defined for eigenfunctions
        """
    def eigenvalue(self):
        """
        Return the `U_p`-eigenvalue of this eigenform.

        This raises an error unless this element was explicitly flagged
        as an eigenform, using the method :meth:`_notify_eigen`.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2)
            sage: f = M.eigenfunctions(3)[1]
            sage: f.eigenvalue()
            3^2 + 3^4 + 2*3^6 + 3^7 + 3^8 + 2*3^9 + 2*3^10 + 3^12 + 3^16 + 2*3^17
             + 3^18 + 3^20 + 2*3^21 + 3^22 + 2*3^23 + 3^25 + 3^26 + 2*3^27 + 2*3^29
             + 3^30 + 3^31 + 3^32 + 3^33 + 3^34 + 3^36 + 3^40 + 2*3^41 + 3^43 + 3^44
             + 3^45 + 3^46 + 3^48 + 3^49 + 3^50 + 2*3^51 + 3^52 + 3^54 + 2*3^57
             + 2*3^59 + 3^60 + 3^61 + 2*3^63 + 2*3^66 + 2*3^67 + 3^69 + 2*3^72
             + 3^74 + 2*3^75 + 3^76 + 2*3^77 + 2*3^78 + 2*3^80 + 3^81 + 2*3^82
             + 3^84 + 2*3^85 + 2*3^86 + 3^87 + 3^88 + 2*3^89 + 2*3^91 + 3^93 + 3^94
             + 3^95 + 3^96 + 3^98 + 2*3^99 + O(3^100)
            sage: M.gen(4).eigenvalue()
            Traceback (most recent call last):
            ...
            TypeError: eigenvalue only defined for eigenfunctions
        """
    def q_expansion(self, prec=None):
        """
        Return the `q`-expansion of ``self``, to as high precision as it is known.

        EXAMPLES::

            sage: OverconvergentModularForms(3, 4, 1/2).gen(0).q_expansion()
            1 - 120/13*q - 1080/13*q^2 - 120/13*q^3 - 8760/13*q^4 - 15120/13*q^5
             - 1080/13*q^6 - 41280/13*q^7 - 5400*q^8 - 120/13*q^9 - 136080/13*q^10
             - 159840/13*q^11 - 8760/13*q^12 - 263760/13*q^13 - 371520/13*q^14
             - 15120/13*q^15 - 561720/13*q^16 - 45360*q^17 - 1080/13*q^18
             - 823200/13*q^19 + O(q^20)
        """
    def gexp(self):
        """
        Return the formal power series in `g` corresponding to ``self``.

        If this overconvergent modular form is `E_k^\\ast \\times F(g)`
        where `g` is the appropriately normalised parameter of `X_0(p)`,
        the result is `F`.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2)
            sage: f = M.eigenfunctions(3)[1]
            sage: f.gexp()
            (3^-3 + O(3^95))*g
            + (3^-1 + 1 + 2*3 + 3^2 + 2*3^3 + 3^5 + 3^7 + 3^10 + 3^11 + 3^14 + 3^15
                + 3^16 + 2*3^19 + 3^21 + 3^22 + 2*3^23 + 2*3^24 + 3^26 + 2*3^27
                + 3^29 + 3^31 + 3^34 + 2*3^35 + 2*3^36 + 3^38 + 2*3^39 + 3^41 + 2*3^42
                + 2*3^43 + 2*3^44 + 2*3^46 + 2*3^47 + 3^48 + 2*3^49 + 2*3^50 + 3^51
                + 2*3^54 + 2*3^55 + 2*3^56 + 3^57 + 2*3^58 + 2*3^59 + 2*3^60 + 3^61
                + 3^62 + 3^63 + 3^64 + 2*3^65 + 3^67 + 3^68 + 2*3^69 + 3^70 + 2*3^71
                + 2*3^74 + 3^76 + 2*3^77 + 3^78 + 2*3^79 + 2*3^80 + 3^84 + 2*3^85
                + 2*3^86 + 3^88 + 2*3^89 + 3^91 + 3^92 + 2*3^94 + 3^95 + O(3^97))*g^2
            + O(g^3)
        """
    def coordinates(self, prec=None):
        """
        Return the coordinates of this modular form in terms of the basis of this space.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2, prec=15)
            sage: f = (M.0 + M.3); f.coordinates()
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            sage: f.coordinates(6)
            [1, 0, 0, 1, 0, 0]
            sage: OverconvergentModularForms(3, 0, 1/6)(f).coordinates(6)
            [1, 0, 0, 729, 0, 0]
            sage: f.coordinates(100)
            Traceback (most recent call last):
            ...
            ValueError: Precision too large for space
        """
    def prime(self):
        """
        If this is a `p`-adic modular form, return `p`.

        EXAMPLES::

            sage: OverconvergentModularForms(2, 0, 1/2).an_element().prime()
            2
        """
    def is_integral(self) -> bool:
        """
        Test whether this element has `q`-expansion coefficients that are `p`-adically integral.

        This should always be the case with eigenfunctions, but sometimes
        if `n` is very large this breaks down for unknown reasons!

        EXAMPLES::

            sage: M = OverconvergentModularForms(2, 0, 1/3)
            sage: q = QQ[['q']].gen()
            sage: M(q - 17*q^2 + O(q^3)).is_integral()
            True
            sage: M(q - q^2/2 + 6*q^7  + O(q^9)).is_integral()
            False
        """
    def r_ord(self, r):
        """
        The `p`-adic valuation of the norm of ``self`` on the `r`-overconvergent region.

        EXAMPLES::

            sage: o = OverconvergentModularForms(3, 0, 1/2)
            sage: t = o([1, 1, 1/3])
            sage: t.r_ord(1/2)
            1
            sage: t.r_ord(2/3)
            3
        """
    def valuation(self):
        """
        Return the `p`-adic valuation of this form.

        This is the minimum of the `p`-adic valuations of its coordinates.

        EXAMPLES::

            sage: M = OverconvergentModularForms(3, 0, 1/2)
            sage: (M.7).valuation()
            0
            sage: (3^18 * (M.2)).valuation()
            18
        """
    def governing_term(self, r):
        """
        The degree of the series term with largest norm on the `r`-overconvergent region.

        EXAMPLES::

            sage: o = OverconvergentModularForms(3, 0, 1/2)
            sage: f = o.eigenfunctions(10)[1]
            sage: f.governing_term(1/2)
            1
        """
    def valuation_plot(self, rmax=None):
        """
        Draw a graph depicting the growth of the norm of this overconvergent
        modular form as it approaches the boundary of the overconvergent
        region.

        EXAMPLES::

            sage: o = OverconvergentModularForms(3, 0, 1/2)
            sage: f = o.eigenfunctions(4)[1]
            sage: f.valuation_plot()                                                    # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def weight(self):
        """
        Return the weight of this overconvergent modular form.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: R = Qp(13).extension(x^2 - 13, names='a')
            sage: M = OverconvergentModularForms(13, 10, 1/2, base_ring=R)
            sage: M.gen(0).weight()
            10
        """
    def additive_order(self):
        """
        Return the additive order of this element.

        This implements a required method for all
        elements deriving from :class:`sage.modules.ModuleElement`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: R = Qp(13).extension(x^2 - 13, names='a')
            sage: M = OverconvergentModularForms(13, 10, 1/2, base_ring=R)
            sage: M.gen(0).additive_order()
            +Infinity
            sage: M(0).additive_order()
            1
        """
    def base_extend(self, R):
        """
        Return a copy of ``self`` but with coefficients in the given ring.

        EXAMPLES::

            sage: M = OverconvergentModularForms(7, 10, 1/2, prec=5)
            sage: f = M.1
            sage: f.base_extend(Qp(7, 4))
            7-adic overconvergent modular form of weight-character 10 with q-expansion
             (7 + O(7^5))*q + (6*7 + 4*7^2 + 7^3 + 6*7^4 + O(7^5))*q^2
             + (5*7 + 5*7^2 + 7^4 + O(7^5))*q^3 + (7^2 + 4*7^3 + 3*7^4 + 2*7^5
             + O(7^6))*q^4 + O(q^5)
        """
    def __pari__(self):
        """
        Return the Pari object corresponding to ``self``.

        This is just the `q`-expansion of ``self`` as a formal power series.

        EXAMPLES::

            sage: f = OverconvergentModularForms(3, 0, 1/2).1
            sage: pari(f) # indirect doctest
            27*q + 324*q^2 + 2430*q^3 + 13716*q^4 + 64557*q^5 + 265356*q^6 + 983556*q^7 + 3353076*q^8 + 10670373*q^9 + 32031288*q^10 + 91455804*q^11 + 249948828*q^12 + 657261999*q^13 + 1669898592*q^14 + 4113612864*q^15 + 9853898292*q^16 + 23010586596*q^17 + 52494114852*q^18 + 117209543940*q^19 + O(q^20)
            sage: pari(f.base_extend(Qp(3))) # indirect doctest
            (3^3 + O(3^23))*q + (3^4 + 3^5 + O(3^24))*q^2 + (3^5 + 3^7 + O(3^25))*q^3 + (3^3 + 3^4 + 2*3^5 + 2*3^8 + O(3^23))*q^4 + (2*3^4 + 3^5 + 3^6 + 2*3^7 + 3^10 + O(3^24))*q^5 + (3^6 + 3^7 + 3^8 + 3^9 + 3^10 + 3^11 + O(3^26))*q^6 + (2*3^3 + 3^4 + 2*3^6 + 2*3^7 + 2*3^8 + 3^9 + 3^10 + 2*3^11 + 3^12 + O(3^23))*q^7 + (2*3^4 + 3^5 + 3^8 + 2*3^9 + 2*3^10 + 2*3^13 + O(3^24))*q^8 + (3^7 + 2*3^9 + 2*3^12 + 2*3^14 + O(3^27))*q^9 + (2*3^5 + 3^8 + 3^9 + 2*3^10 + 2*3^13 + 2*3^15 + O(3^25))*q^10 + (3^4 + 2*3^5 + 2*3^6 + 3^8 + 2*3^9 + 3^12 + 3^14 + 2*3^16 + O(3^24))*q^11 + (3^5 + 3^6 + 2*3^8 + 2*3^9 + 2*3^10 + 2*3^12 + 3^14 + 2*3^15 + 2*3^16 + 3^17 + O(3^25))*q^12 + (2*3^3 + 2*3^4 + 2*3^5 + 3^8 + 2*3^9 + 2*3^11 + 3^13 + 2*3^14 + 2*3^17 + 3^18 + O(3^23))*q^13 + (2*3^4 + 2*3^6 + 2*3^7 + 3^8 + 2*3^9 + 3^10 + 3^12 + 3^14 + 2*3^15 + 2*3^16 + 3^18 + 3^19 + O(3^24))*q^14 + (2*3^6 + 3^7 + 3^9 + 3^10 + 3^11 + 2*3^14 + 3^15 + 2*3^16 + 3^17 + 3^18 + 3^20 + O(3^26))*q^15 + (3^3 + 2*3^4 + 2*3^7 + 2*3^8 + 3^9 + 3^10 + 2*3^11 + 3^12 + 2*3^14 + 2*3^15 + 3^17 + 3^18 + 2*3^19 + 2*3^20 + O(3^23))*q^16 + (2*3^5 + 2*3^7 + 2*3^8 + 3^10 + 3^11 + 2*3^12 + 2*3^13 + 3^14 + 3^15 + 3^17 + 2*3^18 + 3^19 + 2*3^21 + O(3^25))*q^17 + (3^8 + 3^9 + 2*3^10 + 2*3^11 + 3^12 + 3^14 + 3^15 + 3^16 + 3^17 + 2*3^21 + 3^22 + O(3^28))*q^18 + (2*3^3 + 3^5 + 2*3^6 + 2*3^8 + 2*3^9 + 3^11 + 2*3^12 + 3^13 + 3^14 + 2*3^15 + 3^16 + 3^17 + 2*3^18 + 3^19 + 2*3^21 + O(3^23))*q^19 + O(q^20)
        """
