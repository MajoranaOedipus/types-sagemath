from sage.arith.functions import lcm as lcm
from sage.arith.misc import CRT as CRT, factorial as factorial, gcd as gcd
from sage.combinat.combination import Combinations as Combinations
from sage.functions.log import exp as exp
from sage.matrix.constructor import block_matrix as block_matrix, identity_matrix as identity_matrix, matrix as matrix, vector as vector, zero_matrix as zero_matrix
from sage.misc.misc_c import prod as prod
from sage.modules.free_module_element import zero_vector as zero_vector
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.finite_rings.integer_mod import mod as mod
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field import is_real_place as is_real_place, refine_embedding as refine_embedding
from sage.rings.number_field.unit_group import UnitGroup as UnitGroup
from sage.rings.padics.factory import Qp as Qp
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RR as RR, RealField as RealField
from sage.symbolic.ring import SR as SR

def column_Log(SUK, iota, U, prec: int = 106):
    """
    Return the log vector of ``iota``; i.e., the logs of all the valuations.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``iota`` -- an element of ``K``
    - ``U`` -- list of places (finite or infinite) of ``K``
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the log vector as a list of real numbers

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import column_Log
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: S = tuple(K.primes_above(3))
        sage: SUK = UnitGroup(K, S=S)
        sage: phi_complex = K.places()[1]
        sage: v_fin = S[0]
        sage: U = [phi_complex, v_fin]
        sage: column_Log(SUK, xi^2, U)  # abs tol 1e-29
        [1.464816384890812968648768625966, -2.197224577336219382790490473845]

    REFERENCES:

    - [Sma1995]_ p. 823
    """
def c3_func(SUK, prec: int = 106):
    """
    Return the constant `c_3` from [AKMRVW]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the constant `c_3`, as a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import c3_func
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))

        sage: c3_func(SUK)  # abs tol 1e-29
        0.4257859134798034746197327286726

    .. NOTE::

        The numerator should be as close to 1 as possible, especially as the rank of the `S`-units grows large

    REFERENCES:

    - [AKMRVW]_ :arxiv:`1903.00977`
    """
def c4_func(SUK, v, A, prec: int = 106):
    """
    Return the constant `c_4` from Smart's TCDF paper, [Sma1995]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- a place of ``K``, finite (a fractional ideal) or infinite (element of ``SUK.number_field().places(prec)``)
    - ``A`` -- the set of the product of the coefficients of the ``S``-unit equation with each root of unity of ``K``
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the constant `c_4`, as a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import c4_func
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: phi_real = K.places()[0]
        sage: phi_complex = K.places()[1]
        sage: v_fin = tuple(K.primes_above(3))[0]
        sage: A = K.roots_of_unity()

        sage: c4_func(SUK, phi_real, A)
        1.000000000000000000000000000000

        sage: c4_func(SUK, phi_complex, A)
        1.000000000000000000000000000000

        sage: c4_func(SUK, v_fin, A)
        1.000000000000000000000000000000

    REFERENCES:

    - [Sma1995]_ p. 824
    """
def beta_k(betas_and_ns):
    """
    Return a pair `[\\beta_k,|beta_k|_v]`, where `\\beta_k` has the smallest
    nonzero valuation in absolute value of the list ``betas_and_ns``.

    INPUT:

    - ``betas_and_ns`` -- list of pairs ``[beta,val_v(beta)]`` outputted from
      the function where ``beta`` is an element of ``SUK.fundamental_units()``

    OUTPUT:

    The pair ``[beta_k,v(beta_k)]``, where ``beta_k`` is an element of ``K``
    and ``val_v(beta_k)`` is a integer.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import beta_k
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: v_fin = tuple(K.primes_above(3))[0]

        sage: betas = [[beta, beta.valuation(v_fin)] for beta in SUK.fundamental_units()]
        sage: beta_k(betas)
        [xi, 1]

    REFERENCES:

    - [Sma1995]_ pp. 824-825
    """
def mus(SUK, v):
    """
    Return a list `[\\mu]`, for `\\mu` defined in [AKMRVW]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- a finite place of ``K``

    OUTPUT: list ``[mus]`` where each ``mu`` is an element of ``K``

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import mus
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: v_fin = tuple(K.primes_above(3))[0]

        sage: mus(SUK, v_fin)
        [xi^2 - 2]

    REFERENCES:

    - [AKMRVW]_
    """
def possible_mu0s(SUK, v):
    """
    Return a list `[\\mu_0]` of all possible `\\mu_0` values defined in [AKMRVW]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- a finite place of ``K``

    OUTPUT: list ``[mu0s]`` where each ``mu0`` is an element of ``K``

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import possible_mu0s
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: S = tuple(K.primes_above(3))
        sage: SUK = UnitGroup(K, S=S)
        sage: v_fin = S[0]

        sage: possible_mu0s(SUK, v_fin)
        [-1, 1]

    .. NOTE::

        `n_0` is the valuation of the coefficient `\\alpha_d` of the `S`-unit equation such that `|\\alpha_d \\tau_d|_v = 1`
        We have set `n_0 = 0` here since the coefficients are roots of unity
        `\\alpha_0` is not defined in the paper, we set it to be 1

    REFERENCES:

    - [AKMRVW]_
    - [Sma1995]_ pp. 824-825, but we modify the definition of ``sigma`` (``sigma_tilde``) to make it easier to code
    """
def Yu_a1_kappa1_c1(p, dK, ep):
    """
    Compute the constants a(1), kappa1, and c(1) of [Yu2007]_.

    INPUT:

    - ``p`` -- a rational prime number
    - ``dK`` -- the absolute degree of some number field `K`
    - ``ep`` -- the absolute ramification index of some prime ``frak_p`` of `K` lying above `p`

    OUTPUT:

    The constants a(1), kappa1, and c(1).

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import Yu_a1_kappa1_c1
        sage: Yu_a1_kappa1_c1(5, 10, 3)
        (16, 20, 319)

    REFERENCES:

    - [Yu2007]_
    """
def Yu_condition_115(K, v):
    """
    Return ``True`` or ``False``, as the number field ``K`` and the finite place ``v`` satisfy condition (1.15) of [Yu2007]_.

    INPUT:

    - ``K`` -- a number field
    - ``v`` -- a finite place of ``K``

    OUTPUT:

    ``True`` if (1.15) is satisfied, otherwise ``False``.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import Yu_condition_115
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 5)
        sage: v2 = K.primes_above(2)[0]
        sage: v11 = K.primes_above(11)[0]
        sage: Yu_condition_115(K, v2)
        False
        sage: Yu_condition_115(K, v11)
        True

    REFERENCES:

    - [Yu2007]_ p. 188
    """
def Yu_modified_height(mu, n, v, prec: int = 106):
    """
    Return the value of h(n)(mu) as appearing in [Yu2007]_ equation (1.21).

    INPUT:

    - ``mu`` -- an element of a field K
    - ``n`` -- number of mu_j to be considered in Yu's Theorem
    - ``v`` -- a place of K
    - ``prec`` -- the precision of the real field

    OUTPUT:

    The value `h_p(mu)`.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 5)
        sage: v11 = K.primes_above(11)[0]
        sage: from sage.rings.number_field.S_unit_solver import Yu_modified_height
        sage: Yu_modified_height(a, 3, v11)
        0.8047189562170501873003796666131

    If mu is a root of unity, the output is not zero. ::
        sage: Yu_modified_height(-1, 3, v11)
        0.03425564675426243634374205111379

    REFERENCES:

    - [Yu2007]_ p. 192
    """
def Omega_prime(dK, v, mu_list, prec: int = 106):
    """
    Return the constant `\\Omega'` appearing in [AKMRVW]_.

    INPUT:

    - ``dK`` -- the degree of a number field `K`
    - ``v`` -- a finite place of `K`
    - ``mu_list`` -- list of nonzero elements of `K`. It is assumed that the
      sublist ``mu_list[1:]`` is multiplicatively independent
    - ``prec`` -- the precision of the real field

    OUTPUT: the constant `\\Omega'`

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import mus, Omega_prime
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(6)))
        sage: v = K.primes_above(3)[0]
        sage: mu_list = [-1] + mus(SUK, v)
        sage: dK = K.degree()
        sage: Omega_prime(dK, v, mu_list)
        0.000487349679922696

    REFERENCES:

    - [AKMRVW]_ :arxiv:`1903.00977`
    """
def Yu_C1_star(n, v, prec: int = 106):
    """
    Return the constant `C_1^*` appearing in [Yu2007]_ (1.23).

    INPUT:

    - ``n`` -- the number of generators of a multiplicative subgroup of a field `K`
    - ``v`` -- a finite place of `K` (a fractional ideal)
    - ``prec`` -- the precision of the real field

    OUTPUT: the constant `C_1^*` as a real number

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 5)
        sage: v11 = K.primes_above(11)[0]
        sage: from sage.rings.number_field.S_unit_solver import Yu_C1_star
        sage: Yu_C1_star(1,v11)
        2.154667761574516556114215527020e6

    REFERENCES:

    - [Yu2007]_ p.189,193
    """
def Yu_bound(SUK, v, prec: int = 106):
    """
    Return `c_8` such that `c_8 \\geq exp(2)/\\log(2)` and `ord_p (\\Theta - 1) < c_8 \\log B`,
    where `\\Theta = \\prod_{j=1}^n \\alpha_j^{b_j}` and `B \\geq \\max_j |b_j|` and `B \\geq 3`.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- a finite place of `K` (a fractional ideal)
    - ``prec`` -- the precision of the real field

    OUTPUT: the constant `c_8` as a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import Yu_bound
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 11)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(6)))
        sage: v = K.primes_above(3)[0]
        sage: Yu_bound(SUK, v)
        9.03984381033128e9

    REFERENCES:

    - [Sma1995]_ p. 825
    - [Yu2007]_ p. 189--193 esp. Theorem 1
    - [AKMRVW]_ :arxiv:`1903.00977`
    """
def K0_func(SUK, A, prec: int = 106):
    """
    Return the constant `K_0` from [AKMRVW]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``A`` -- the set of the products of the coefficients of the `S`-unit equation with each root of unity of `K`
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the constant `K_0`, a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import K0_func
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 11)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(6)))
        sage: v = K.primes_above(3)[0]
        sage: K0_func(SUK, K.roots_of_unity())
        8.84763586062272e12

    REFERENCES:

    - [Sma1995]_ p. 824
    - [AKMRVW]_ :arxiv:`1903.00977`
    """
def c11_func(SUK, v, A, prec: int = 106):
    """
    Return the constant `c_{11}` from Smart's TCDF paper, [Sma1995]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- a place of `K`, finite (a fractional ideal) or infinite (element of ``SUK.number_field().places(prec)``)
    - ``A`` -- the set of the product of the coefficients of the `S`-unit equation with each root of unity of `K`
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the constant `c_{11}`, a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import c11_func
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: phi_real = K.places()[0]
        sage: phi_complex = K.places()[1]
        sage: A = K.roots_of_unity()

        sage: c11_func(SUK, phi_real, A)  # abs tol 1e-29
        3.255848343572896153455615423662

        sage: c11_func(SUK, phi_complex, A)  # abs tol 1e-29
        6.511696687145792306911230847323

    REFERENCES:

    - [Sma1995]_ p. 825
    """
def c13_func(SUK, v, prec: int = 106):
    """
    Return the constant `c_{13}` from Smart's TCDF paper, [Sma1995]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- an infinite place of ``K`` (element of ``SUK.number_field().places(prec)``)
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the constant `c_{13}`, as a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import c13_func
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: phi_real = K.places()[0]
        sage: phi_complex = K.places()[1]

        sage: c13_func(SUK, phi_real)  # abs tol 1e-29
        0.4257859134798034746197327286726

        sage: c13_func(SUK, phi_complex)  # abs tol 1e-29
        0.2128929567399017373098663643363

    It is an error to input a finite place. ::

        sage: phi_finite = K.primes_above(3)[0]
        sage: c13_func(SUK, phi_finite)
        Traceback (most recent call last):
        ...
        TypeError: Place must be infinite


    REFERENCES:

    - [Sma1995]_ p. 825
    """
def K1_func(SUK, v, A, prec: int = 106):
    """
    Return the constant `K_1` from Smart's TCDF paper, [Sma1995]_.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``v`` -- an infinite place of `K` (element of ``SUK.number_field().places(prec)``)
    - ``A`` -- list of all products of each potential `a`, `b` in the `S`-unit
      equation `ax + by + 1 = 0` with each root of unity of `K`
    - ``prec`` -- the precision of the real field (default: 106)

    OUTPUT: the constant `K_1`, a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import K1_func
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: phi_real = K.places()[0]
        sage: phi_complex = K.places()[1]
        sage: A = K.roots_of_unity()

        sage: K1_func(SUK, phi_real, A)
        4.483038368145048508970350163578e16

        sage: K1_func(SUK, phi_complex, A)
        2.073346189067285101984136298965e17

    REFERENCES:

    - [Sma1995]_ p. 825
    """
def minimal_vector(A, y, prec: int = 106):
    """
    INPUT:

    - ``A`` -- a square `n` by `n` non-singular integer matrix whose rows generate a lattice `\\mathcal L`
    - ``y`` -- a row (1 by `n`) vector with integer coordinates
    - ``prec`` -- precision of real field (default: 106)

    OUTPUT: a lower bound for the square of

    .. MATH::

        \\ell (\\mathcal L,\\vec y) =
        \\begin{cases}
        \\displaystyle\\min_{\\vec x\\in\\mathcal L}\\Vert\\vec x-\\vec y\\Vert &, \\vec y\\not\\in\\mathcal L. \\\\\n        \\displaystyle\\min_{0\\neq\\vec x\\in\\mathcal L}\\Vert\\vec x\\Vert &,\\vec y\\in\\mathcal L.
        \\end{cases}`

    ALGORITHM:

    The algorithm is based on V.9 and V.10 of [Sma1998]_

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import minimal_vector
        sage: B = matrix(ZZ, 2, [1,1,1,0])
        sage: y = vector(ZZ, [2,1])
        sage: minimal_vector(B, y)
        1/2

    ::

        sage: B = random_matrix(ZZ, 3)
        sage: while not B.determinant():
        ....:     B = random_matrix(ZZ, 3)
        sage: B # random
        [-2 -1 -1]
        [ 1  1 -2]
        [ 6  1 -1]
        sage: y = vector([1, 2, 100])
        sage: minimal_vector(B, y)  # random
        15/28
    """
def reduction_step_complex_case(place, B0, list_of_gens, torsion_gen, c13):
    """
    INPUT:

    - ``place`` -- (ring morphism) an infinite place of a number field `K`
    - ``B0`` -- the initial bound
    - ``list_of_gens`` -- set of generators of the free part of the group
    - ``torsion_gen`` -- an element of the torsion part of the group
    - ``c13`` -- a positive real number

    OUTPUT: a tuple consisting of:

    1. a new upper bound, an integer
    2. a boolean value, ``True`` if we have to increase precision, otherwise ``False``

    .. NOTE::

        The constant ``c13``  in Section 5, [AKMRVW]_
        This function does handle both real and non-real infinite places.

    REFERENCES:

    See [Sma1998]_, [AKMRVW]_.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import reduction_step_complex_case
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField([x^3 - 2])
        sage: SK = sum([K.primes_above(p) for p in [2,3,5]],[])
        sage: G = [g for g in K.S_unit_group(S=SK).gens_values()
        ....:        if g.multiplicative_order() == Infinity]
        sage: p1 = K.places(prec=100)[1]
        sage: reduction_step_complex_case(p1, 10^5, G, -1, 2)
        (18, False)
    """
def cx_LLL_bound(SUK, A, prec: int = 106):
    """
    Return the maximum of all of the `K_1`'s as they are LLL-optimized for each infinite place `v`.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``A`` -- list of all products of each potential `a`, `b` in the `S`-unit
      equation `ax + by + 1 = 0` with each root of unity of `K`
    - ``prec`` -- precision of real field (default: 106)

    OUTPUT: a bound for the exponents at the infinite place, as a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import cx_LLL_bound
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: A = K.roots_of_unity()

        sage: cx_LLL_bound(SUK, A) # long time
        35
    """
def log_p(a, prime, prec):
    """
    INPUT:

    - ``a`` -- an element of a number field `K`
    - ``prime`` -- a prime ideal of the number field `K`
    - ``prec`` -- positive integer

    OUTPUT:

    An element of `K` which is congruent to the ``prime``-adic logarithm of `a`
    with respect to ``prime`` modulo ``p^prec``, where `p` is the rational
    prime below ``prime``.

    .. NOTE::

        Here we take into account the other primes in `K` above `p` in order to
        get coefficients with small values.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import log_p
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 14)
        sage: p1 = K.primes_above(3)[0]
        sage: p1
        Fractional ideal (3, a + 1)
        sage: log_p(a+2, p1, 20)
        8255385638/3*a + 15567609440/3

    ::

        sage: K.<a> = NumberField(x^4 + 14)
        sage: p1 = K.primes_above(5)[0]
        sage: p1
        Fractional ideal (5, a + 1)
        sage: log_p(1/(a^2-4), p1, 30)
        -42392683853751591352946/25*a^3 - 113099841599709611260219/25*a^2 -
        8496494127064033599196/5*a - 18774052619501226990432/25
    """
def log_p_series_part(a, prime, prec):
    """
    INPUT:

    - ``a`` -- an element of a number field `K`
    - ``prime`` -- a prime ideal of the number field `K`
    - ``prec`` -- positive integer

    OUTPUT:

    The ``prime``-adic logarithm of `a` and accuracy ``p^prec``, where `p` is
    the rational prime below ``prime``.

    ALGORITHM:

    The algorithm is based on the algorithm on page 30 of [Sma1998]_.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import log_p_series_part
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 5)
        sage: p1 = K.primes_above(3)[0]
        sage: p1
        Fractional ideal (3)
        sage: log_p_series_part(a^2 - a + 1, p1, 30)
        120042736778562*a + 263389019530092

    ::

        sage: K.<a> = NumberField(x^4 + 14)
        sage: p1 = K.primes_above(5)[0]
        sage: p1
        Fractional ideal (5, a + 1)
        sage: log_p_series_part(1/(a^2-4), p1, 30)
        5628940883264585369224688048459896543498793204839654215019548600621221950915106576555819252366183605504671859902129729380543157757424169844382836287443485157589362653561119898762509175000557196963413830027960725069496503331353532893643983455103456070939403472988282153160667807627271637196608813155377280943180966078/1846595723557147156151786152499366687569722744011302407020455809280594038056223852568951718462474153951672335866715654153523843955513167531739386582686114545823305161128297234887329119860255600972561534713008376312342295724191173957260256352612807316114669486939448006523889489471912384033203125*a^2 + 2351432413692022254066438266577100183514828004415905040437326602004946930635942233146528817325416948515797296867947688356616798913401046136899081536181084767344346480810627200495531180794326634382675252631839139904967037478184840941275812058242995052383261849064340050686841429735092777331963400618255005895650200107/1846595723557147156151786152499366687569722744011302407020455809280594038056223852568951718462474153951672335866715654153523843955513167531739386582686114545823305161128297234887329119860255600972561534713008376312342295724191173957260256352612807316114669486939448006523889489471912384033203125
    """
def defining_polynomial_for_Kp(prime, prec: int = 106):
    """
    INPUT:

    - ``prime`` -- a prime ideal of a number field `K`
    - ``prec`` -- a positive natural number (default: 106)

    OUTPUT: a polynomial with integer coefficients that is equivalent ``mod p^prec`` to a defining polynomial for the completion of `K` associated to the specified prime

    .. NOTE::

        `K` has to be an absolute extension

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import defining_polynomial_for_Kp
        sage: K.<a> = QuadraticField(2)
        sage: p2 = K.prime_above(7); p2
        Fractional ideal (2*a - 1)
        sage: defining_polynomial_for_Kp(p2, 10)
        x + 266983762

    ::

        sage: K.<a> = QuadraticField(-6)
        sage: p2 = K.prime_above(2); p2
        Fractional ideal (2, a)
        sage: defining_polynomial_for_Kp(p2, 100)
        x^2 + 6
        sage: p5 = K.prime_above(5); p5
        Fractional ideal (5, a + 2)
        sage: defining_polynomial_for_Kp(p5, 100)
        x + 3408332191958133385114942613351834100964285496304040728906961917542037
    """
def embedding_to_Kp(a, prime, prec):
    """
    INPUT:

    - ``a`` -- an element of a number field `K`
    - ``prime`` -- a prime ideal of `K`
    - ``prec`` -- a positive natural number

    OUTPUT:

    An element of `K` that is equivalent to `a` modulo ``p^(prec)`` and the generator of `K` appears with exponent less than `e \\cdot f`, where `p` is the rational prime below ``prime`` and `e`, `f` are the ramification index and residue degree, respectively.

    .. NOTE::

        `K` has to be an absolute number field

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import embedding_to_Kp
        sage: K.<a> = QuadraticField(17)
        sage: p = K.prime_above(13); p
        Fractional ideal (a - 2)
        sage: embedding_to_Kp(a-3, p, 15)
        -20542890112375827

    ::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^4 - 2)
        sage: p = K.prime_above(7); p
        Fractional ideal (-a^2 + a - 1)
        sage: embedding_to_Kp(a^3 - 3, p, 15)
        -1261985118949117459462968282807202378
    """
def p_adic_LLL_bound_one_prime(prime, B0, M, M_logp, m0, c3, prec: int = 106):
    """
    INPUT:

    - ``prime`` -- a prime ideal of a number field `K`
    - ``B0`` -- the initial bound
    - ``M`` -- list of elements of `K`, the `\\mu_i`'s from Lemma IX.3 of [Sma1998]_
    - ``M_logp`` -- the `p`-adic logarithm of elements in `M`
    - ``m0`` -- an element of `K`, this is `\\mu_0` from Lemma IX.3 of [Sma1998]_
    - ``c3`` -- a positive real constant
    - ``prec`` -- the precision of the calculations (default: 106), i.e.,
      values are known to ``O(p^prec)``

    OUTPUT: a pair consisting of:

    1. a new upper bound, an integer
    2. a boolean value, ``True`` if we have to increase precision, otherwise ``False``

    .. NOTE::

        The constant `c_5` is the constant `c_5` at the page 89 of [Sma1998]_ which is equal to the constant `c_{10}` at the page 139 of [Sma1995]_.
        In this function, the `c_i` constants are in line with [Sma1998]_, but generally differ from the constants in [Sma1995]_ and other parts of this code.

    EXAMPLES:

    This example indicates a case where we must increase precision::

        sage: from sage.rings.number_field.S_unit_solver import p_adic_LLL_bound_one_prime
        sage: prec = 50
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 3)
        sage: S = tuple(K.primes_above(3))
        sage: SUK = UnitGroup(K, S=S)
        sage: v = S[0]
        sage: A = SUK.roots_of_unity()
        sage: K0_old = 9.4755766731093e17
        sage: Mus = [a^2 - 2]
        sage: Log_p_Mus = [185056824593551109742400*a^2
        ....:               + 1389583284398773572269676*a + 717897987691852588770249]
        sage: mu0 = K(-1)
        sage: c3_value = 0.42578591347980
        sage: m0_Kv_new, increase_prec = p_adic_LLL_bound_one_prime(v, K0_old, Mus, Log_p_Mus,
        ....:                                                       mu0, c3_value, prec)
        sage: m0_Kv_new
        0
        sage: increase_prec
        True

    And now we increase the precision to make it all work::

        sage: prec = 106
        sage: K0_old = 9.475576673109275443280257946930e17
        sage: Log_p_Mus = [1029563604390986737334686387890424583658678662701816*a^2
        ....:               + 661450700156368458475507052066889190195530948403866*a]
        sage: c3_value = 0.4257859134798034746197327286726
        sage: m0_Kv_new, increase_prec = p_adic_LLL_bound_one_prime(v, K0_old, Mus, Log_p_Mus,
        ....:                                                       mu0, c3_value, prec)
        sage: m0_Kv_new
        476
        sage: increase_prec
        False
    """
def p_adic_LLL_bound(SUK, A, prec: int = 106):
    """
    Return the maximum of all of the `K_0`'s as they are LLL-optimized for each
    finite place `v`.

    INPUT:

    - ``SUK`` -- a group of `S`-units
    - ``A`` -- list of all products of each potential `a`, `b` in the `S`-unit
      equation `ax + by + 1 = 0` with each root of unity of `K`
    - ``prec`` -- precision for `p`-adic LLL calculations (default: 106)

    OUTPUT:

    A bound for the max of exponents in the case that extremal place is finite (see [Sma1995]_) as a real number

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import p_adic_LLL_bound
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: A = SUK.roots_of_unity()
        sage: prec = 100
        sage: p_adic_LLL_bound(SUK, A, prec)
        89
    """
def split_primes_large_lcm(SUK, bound):
    """
    Return a list `L` of rational primes `q` which split completely in `K` and
    which have desirable properties (see NOTE).

    INPUT:

    - ``SUK`` -- the `S`-unit group of an absolute number field `K`
    - ``bound`` -- positive integer

    OUTPUT: list `L` of rational primes `q`, with the following properties:

    - each prime `q` in `L` splits completely in `K`
    - if `Q` is a prime in `S` and `q` is the rational
      prime below `Q`, then `q` is **not** in `L`
    - the value `\\lcm(\\{ q-1 : q \\in L \\})` is greater than or equal to ``2*bound + 1``.

    .. NOTE::

        - A series of compatible exponent vectors for the primes in `L` will
          lift to **at most** one integer exponent vector whose entries
          `a_i` satisfy `|a_i|` is less than or equal to ``bound``.

        - The ordering of this set is not very intelligent for the purposes
          of the later sieving processes.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import split_primes_large_lcm
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3*x + 1)
        sage: S = K.primes_above(3)
        sage: SUK = UnitGroup(K, S=tuple(S))
        sage: split_primes_large_lcm(SUK, 200)
        [17, 19, 37, 53]

    With a tiny bound, Sage may ask you to increase the bound.

    ::

        sage: from sage.rings.number_field.S_unit_solver import split_primes_large_lcm
        sage: K.<xi> = NumberField(x^2 + 163)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(23)))
        sage: split_primes_large_lcm(SUK, 8)
        Traceback (most recent call last):
        ...
        ValueError: Not enough split primes found. Increase bound.
    """
def sieve_ordering(SUK, q):
    """
    Return ordered data for running sieve on the primes in ``SUK`` over the rational prime `q`.

    INPUT:

    - ``SUK`` -- the `S`-unit group of a number field `K`
    - ``q`` -- a rational prime number which splits completely in `K`

    OUTPUT: list of tuples;
    ``[ideals_over_q, residue_fields, rho_images, product_rho_orders]``, where:

    1. ``ideals_over_q`` is a list of the `d = [K:\\QQ]` ideals in `K` over `q`
    2. ``residue_fields[i]`` is the residue field of ``ideals_over_q[i]``
    3. ``rho_images[i]`` is a list of the reductions of the generators in of the `S`-unit group, modulo ``ideals_over_q[i]``
    4. ``product_rho_orders[i]`` is the product of the multiplicative orders of the elements in ``rho_images[i]``

    .. NOTE::

        - The list ``ideals_over_q`` is sorted so that the product of orders is smallest for ``ideals_over_q[0]``, as this will make the later sieving steps more efficient.
        - The primes of `S` must not lie over `q`.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import sieve_ordering
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^3 - 3*x + 1)
        sage: SUK = K.S_unit_group(S=3)
        sage: sieve_data = list(sieve_ordering(SUK, 19))
        sage: sieve_data[0]
        (Fractional ideal (-2*xi^2 + 3),
         Fractional ideal (-xi + 3),
         Fractional ideal (2*xi + 1))

        sage: sieve_data[1]
        (Residue field of Fractional ideal (-2*xi^2 + 3),
         Residue field of Fractional ideal (-xi + 3),
         Residue field of Fractional ideal (2*xi + 1))

        sage: sieve_data[2]
        ([18, 9, 16, 8], [18, 7, 10, 4], [18, 3, 12, 10])

        sage: sieve_data[3]
        (972, 972, 3888)
    """
def clean_rfv_dict(rfv_dictionary) -> None:
    """
    Given a residue field vector dictionary, remove some impossible keys and entries.

    INPUT:

    - ``rfv_dictionary`` -- dictionary whose keys are exponent vectors and
      whose values are residue field vectors

    OUTPUT: none, but it removes some keys from the input dictionary

    .. NOTE::

        - The keys of a residue field vector dictionary are exponent vectors modulo `q-1` for some prime `q`.
        - The values are residue field vectors. It is known that a residue field vector
          which comes from a solution to the `S`-unit equation cannot have 1 in any entry.

    EXAMPLES:

    In this example, we use a truncated list generated when solving the `S`-unit equation in the case that `K` is defined by the
    polynomial `x^2+x+1` and `S` consists of the primes above 3::

        sage: from sage.rings.number_field.S_unit_solver import clean_rfv_dict
        sage: rfv_dict = {(1, 3): [3, 2], (3, 0): [6, 6], (5, 4): [3, 6], (2, 1): [4, 6],
        ....:             (5, 1): [3, 1], (2, 5): [1, 5], (0, 3): [1, 6]}
        sage: len(rfv_dict)
        7
        sage: clean_rfv_dict(rfv_dict)
        sage: len(rfv_dict)
        4
        sage: rfv_dict
        {(1, 3): [3, 2], (2, 1): [4, 6], (3, 0): [6, 6], (5, 4): [3, 6]}
    """
def construct_rfv_to_ev(rfv_dictionary, q, d, verbose: bool = False):
    """
    Return a reverse lookup dictionary, to find the exponent vectors associated
    to a given residue field vector.

    INPUT:

    - ``rfv_dictionary`` -- dictionary whose keys are exponent vectors and
      whose values are the associated residue field vectors
    - ``q`` -- a prime (assumed to split completely in the relevant number field)
    - ``d`` -- the number of primes in `K` above the rational prime `q`
    - ``verbose`` -- boolean (default: ``False``); flag to indicate more
      detailed output is desired

    OUTPUT:

    A dictionary ``P`` whose keys are residue field vectors and whose values are lists of all exponent vectors
    which correspond to the given residue field vector.

    .. NOTE::

        - For example, if ``rfv_dictionary[e0] = r0``, then ``P[r0]`` is a list which contains ``e0``.
        - During construction, some residue field vectors can be eliminated as coming from
          solutions to the `S`-unit equation. Such vectors are dropped from the keys of the dictionary ``P``.

    EXAMPLES:

    In this example, we use a truncated list generated when solving the `S`-unit equation in the case that `K` is defined by the
    polynomial `x^2+x+1` and `S` consists of the primes above 3::

        sage: from sage.rings.number_field.S_unit_solver import construct_rfv_to_ev
        sage: rfv_dict = {(1, 3): [3, 2], (3, 0): [6, 6], (5, 4): [3, 6], (2, 1): [4, 6],
        ....:             (4, 0): [4, 2], (1, 2): [5, 6]}
        sage: construct_rfv_to_ev(rfv_dict,7,2,False)
        {(3, 2): [(1, 3)], (4, 2): [(4, 0)], (4, 6): [(2, 1)], (5, 6): [(1, 2)]}
    """
def construct_comp_exp_vec(rfv_to_ev_dict, q):
    """
    Construct a dictionary associating complement vectors to residue field vectors.

    INPUT:

    - ``rfv_to_ev_dict`` -- dictionary whose keys are residue field vectors and
      whose values are lists of exponent vectors with the associated residue
      field vector
    - ``q`` -- the characteristic of the residue field

    OUTPUT: a dictionary whose typical key is an exponent vector ``a``, and
    whose associated value is a list of complementary exponent vectors to ``a``

    EXAMPLES:

    In this example, we use the list generated when solving the `S`-unit equation in the case that `K` is defined by the
    polynomial `x^2+x+1` and `S` consists of the primes above 3

    ::

        sage: from sage.rings.number_field.S_unit_solver import construct_comp_exp_vec
        sage: rfv_to_ev_dict = {(6, 6): [(3, 0)], (5, 6): [(1, 2)], (5, 4): [(5, 3)],
        ....:                   (6, 2): [(5, 5)], (2, 5): [(0, 1)], (5, 5): [(3, 4)],
        ....:                   (4, 4): [(0, 2)], (6, 3): [(1, 4)], (3, 6): [(5, 4)],
        ....:                   (2, 2): [(0, 4)], (3, 5): [(1, 0)], (6, 4): [(1, 1)],
        ....:                   (3, 2): [(1, 3)], (2, 6): [(4, 5)], (4, 5): [(4, 3)],
        ....:                   (2, 3): [(2, 3)], (4, 2): [(4, 0)], (6, 5): [(5, 2)],
        ....:                   (3, 3): [(3, 2)], (5, 3): [(5, 0)], (4, 6): [(2, 1)],
        ....:                   (3, 4): [(3, 5)], (4, 3): [(0, 5)], (5, 2): [(3, 1)],
        ....:                   (2, 4): [(2, 0)]}
        sage: construct_comp_exp_vec(rfv_to_ev_dict, 7)
        {(0, 1): [(1, 4)],
         (0, 2): [(0, 2)],
         (0, 4): [(3, 0)],
         (0, 5): [(4, 3)],
         (1, 0): [(5, 0)],
         (1, 1): [(2, 0)],
         (1, 2): [(1, 3)],
         (1, 3): [(1, 2)],
         (1, 4): [(0, 1)],
         (2, 0): [(1, 1)],
         (2, 1): [(4, 0)],
         (2, 3): [(5, 2)],
         (3, 0): [(0, 4)],
         (3, 1): [(5, 4)],
         (3, 2): [(3, 4)],
         (3, 4): [(3, 2)],
         (3, 5): [(5, 3)],
         (4, 0): [(2, 1)],
         (4, 3): [(0, 5)],
         (4, 5): [(5, 5)],
         (5, 0): [(1, 0)],
         (5, 2): [(2, 3)],
         (5, 3): [(3, 5)],
         (5, 4): [(3, 1)],
         (5, 5): [(4, 5)]}
    """
def drop_vector(ev, p, q, complement_ev_dict):
    """
    Determine if the exponent vector, ``ev``, may be removed from the complement dictionary during construction.
    This will occur if ``ev`` is not compatible with an exponent vector mod `q-1`.

    INPUT:

    - ``ev`` -- an exponent vector modulo `p-1`
    - ``p`` -- the prime such that ``ev`` is an exponent vector modulo `p-1`
    - ``q`` -- a prime, distinct from `p`, that is a key in the ``complement_ev_dict``
    - ``complement_ev_dict`` -- dictionary of dictionaries, whose keys are primes
      ``complement_ev_dict[q]`` is a dictionary whose keys are exponent vectors modulo `q-1`
      and whose values are lists of complementary exponent vectors modulo `q-1`

    OUTPUT: ``True`` if ``ev`` may be dropped from the complement exponent
    vector dictionary, and ``False`` if not

    .. NOTE::

        - If ``ev`` is not compatible with any of the vectors modulo `q-1`, then it can no longer correspond to a solution
          of the `S`-unit equation. It returns ``True`` to indicate that it should be removed.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import drop_vector
        sage: drop_vector((1, 2, 5), 7, 11, {11: {(1, 1, 3): [(1, 1, 3), (2, 3, 4)]}})
        True

    ::

        sage: P = {3: {(1, 0, 0): [(1, 0, 0), (0, 1, 0)],
        ....:          (0, 1, 0): [(1, 0, 0), (0, 1, 0)]},
        ....:      7: {(0, 3, 4): [(0, 1, 2), (0, 3, 4), (0, 5, 0)],
        ....:          (1, 2, 4): [(1, 0, 4), (1, 4, 2), (1, 2, 0)],
        ....:          (0, 1, 2): [(0, 1, 2), (0, 3, 4), (0, 5, 0)],
        ....:          (0, 5, 4): [(1, 0, 0), (1, 4, 4), (1, 2, 2)],
        ....:          (1, 4, 2): [(1, 2, 4), (1, 4, 0), (1, 0, 2)],
        ....:          (1, 0, 4): [(1, 2, 4), (1, 4, 0), (1, 0, 2)],
        ....:          (0, 3, 2): [(1, 0, 0), (1, 4, 4), (1, 2, 2)],
        ....:          (1, 0, 0): [(0, 5, 4), (0, 3, 2), (0, 1, 0)],
        ....:          (1, 2, 0): [(1, 2, 4), (1, 4, 0), (1, 0, 2)],
        ....:          (0, 1, 0): [(1, 0, 0), (1, 4, 4), (1, 2, 2)],
        ....:          (0, 5, 0): [(0, 1, 2), (0, 3, 4), (0, 5, 0)],
        ....:          (1, 2, 2): [(0, 5, 4), (0, 3, 2), (0, 1, 0)],
        ....:          (1, 4, 0): [(1, 0, 4), (1, 4, 2), (1, 2, 0)],
        ....:          (1, 0, 2): [(1, 0, 4), (1, 4, 2), (1, 2, 0)],
        ....:          (1, 4, 4): [(0, 5, 4), (0, 3, 2), (0, 1, 0)]}}
        sage: drop_vector((0, 1, 0), 3, 7, P)
        False
    """
def construct_complement_dictionaries(split_primes_list, SUK, verbose: bool = False):
    """
    Construct the complement exponent vector dictionaries.

    INPUT:

    - ``split_primes_list`` -- list of rational primes which split completely
      in the number field `K`
    - ``SUK`` -- the `S`-unit group for a number field `K`
    - ``verbose`` -- boolean to provide additional feedback (default: ``False``)

    OUTPUT:

    A dictionary of dictionaries. The keys coincide with the primes in
    ``split_primes_list``. For each `q`, ``comp_exp_vec[q]`` is a dictionary
    whose keys are exponent vectors modulo `q-1`, and whose values are lists of
    exponent vectors modulo `q-1`.

    If `w` is an exponent vector in ``comp_exp_vec[q][v]``, then the residue field vectors modulo `q` for
    `v` and `w` sum to ``[1,1,...,1]``

    .. NOTE::

        - The data of ``comp_exp_vec`` will later be lifted to `\\ZZ` to look for true `S`-Unit equation solutions.
        - During construction, the various dictionaries are compared to each other several times to
          eliminate as many mod `q` solutions as possible.
        - The authors acknowledge a helpful discussion with Norman Danner which helped formulate this code.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import construct_complement_dictionaries
        sage: x = polygen(ZZ, 'x')
        sage: f = x^2 + 5
        sage: H = 10
        sage: K.<xi> = NumberField(f)
        sage: SUK = K.S_unit_group(S=K.primes_above(H))
        sage: split_primes_list = [3, 7]
        sage: actual = construct_complement_dictionaries(split_primes_list, SUK)
        sage: expected = {3: {(0, 1, 0): [(0, 1, 0), (1, 0, 0)],
        ....:                 (1, 0, 0): [(0, 1, 0), (1, 0, 0)]},
        ....:             7: {(0, 1, 0): [(1, 0, 0), (1, 2, 2), (1, 4, 4)],
        ....:                 (0, 1, 2): [(0, 1, 2), (0, 3, 4), (0, 5, 0)],
        ....:                 (0, 3, 2): [(1, 0, 0), (1, 2, 2), (1, 4, 4)],
        ....:                 (0, 3, 4): [(0, 1, 2), (0, 3, 4), (0, 5, 0)],
        ....:                 (0, 5, 0): [(0, 1, 2), (0, 3, 4), (0, 5, 0)],
        ....:                 (0, 5, 4): [(1, 0, 0), (1, 2, 2), (1, 4, 4)],
        ....:                 (1, 0, 0): [(0, 1, 0), (0, 3, 2), (0, 5, 4)],
        ....:                 (1, 0, 2): [(1, 0, 4), (1, 2, 0), (1, 4, 2)],
        ....:                 (1, 0, 4): [(1, 0, 2), (1, 2, 4), (1, 4, 0)],
        ....:                 (1, 2, 0): [(1, 0, 2), (1, 2, 4), (1, 4, 0)],
        ....:                 (1, 2, 2): [(0, 1, 0), (0, 3, 2), (0, 5, 4)],
        ....:                 (1, 2, 4): [(1, 0, 4), (1, 2, 0), (1, 4, 2)],
        ....:                 (1, 4, 0): [(1, 0, 4), (1, 2, 0), (1, 4, 2)],
        ....:                 (1, 4, 2): [(1, 0, 2), (1, 2, 4), (1, 4, 0)],
        ....:                 (1, 4, 4): [(0, 1, 0), (0, 3, 2), (0, 5, 4)]}}
        sage: all(set(actual[p][vec]) == set(expected[p][vec])
        ....:     for p in [3, 7] for vec in expected[p])
        True
    """
def compatible_vectors_check(a0, a1, g, l):
    """
    Given exponent vectors with respect to two moduli, determine if they are compatible.

    INPUT:

    - ``a0`` -- an exponent vector modulo ``m0``
    - ``a1`` -- an exponent vector modulo ``m1`` (must have the same length as ``a0``)
    - ``g`` -- the gcd of ``m0`` and ``m1``
    - ``l`` -- the length of ``a0`` and of ``a1``

    OUTPUT: ``True`` if there is an integer exponent vector a satisfying

    .. MATH::

        \\begin{aligned}
        a[0] &== a0[0] == a1[0]\\\\\n        a[1:] &== a0[1:] \\mod m_0\\\\\n        a[1:] &== a1[1:] \\mod m_1
        \\end{aligned}

    and ``False`` otherwise.

    .. NOTE::

        - Exponent vectors must agree exactly in the first coordinate.
        - If exponent vectors are different lengths, an error is raised.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import compatible_vectors_check
        sage: a0 = (3, 1, 8, 11)
        sage: a1 = (3, 5, 6, 13)
        sage: a2 = (5, 5, 6, 13)
        sage: compatible_vectors_check(a0, a1, gcd(12, 22), 4r)
        True
        sage: compatible_vectors_check(a0, a2, gcd(12, 22), 4r)
        False
    """
def compatible_vectors(a, m0, m1, g):
    """
    Given an exponent vector ``a`` modulo ``m0``, return an iterator over the exponent vectors for the modulus ``m1``, such that a lift to the lcm modulus exists.

    INPUT:

    - ``a`` -- an exponent vector for the modulus ``m0``
    - ``m0`` -- positive integer (specifying the modulus for ``a``)
    - ``m1`` -- positive integer (specifying the alternate modulus)
    - ``g`` -- the gcd of ``m0`` and ``m1``

    OUTPUT: list of exponent vectors modulo ``m1`` which are compatible with ``a``

    .. NOTE::

        Exponent vectors must agree exactly in the 0th position in order to be
        compatible.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import compatible_vectors
        sage: a = (3, 1, 8, 1)
        sage: list(compatible_vectors(a, 18, 12, gcd(18,12)))
        [(3, 1, 2, 1),
         (3, 1, 2, 7),
         (3, 1, 8, 1),
         (3, 1, 8, 7),
         (3, 7, 2, 1),
         (3, 7, 2, 7),
         (3, 7, 8, 1),
         (3, 7, 8, 7)]

    The order of the moduli matters. ::

        sage: len(list(compatible_vectors(a, 18, 12, gcd(18,12))))
        8
        sage: len(list(compatible_vectors(a, 12, 18, gcd(18,12))))
        27
    """
def compatible_systems(split_prime_list, complement_exp_vec_dict):
    """
    Given dictionaries of complement exponent vectors for various primes that
    split in `K`, compute all possible compatible systems.

    INPUT:

    - ``split_prime_list`` -- list of rational primes that split completely in `K`
    - ``complement_exp_vec_dict`` -- dictionary of dictionaries; the keys are
      primes from ``split_prime_list``

    OUTPUT: list of compatible systems of exponent vectors

    .. NOTE::

        - For any `q` in ``split_prime_list``, ``complement_exp_vec_dict[q]`` is a dictionary whose keys are exponent vectors modulo `q-1`
          and whose values are lists of exponent vectors modulo `q-1` which are complementary to the key.

        - An item in ``system_list`` has the form ``[ [v0, w0], [v1, w1], ..., [vk, wk] ]``, where::

          - ``qj = split_prime_list[j]``
          - ``vj`` and ``wj`` are complementary exponent vectors modulo ``qj - 1``
          - the pairs are all simultaneously compatible.

        - Let ``H = lcm( qj - 1 : qj in split_primes_list )``. Then for any compatible system, there is at most one pair of integer
          exponent vectors ``[v, w]`` such that::

          - every entry of ``v`` and ``w`` is bounded in absolute value by ``H``
          - for any ``qj``, ``v`` and ``vj`` agree modulo ``(qj - 1)``
          - for any ``qj``, ``w`` and ``wj`` agree modulo ``(qj - 1)``

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import compatible_systems
        sage: split_primes_list = [3, 7]
        sage: checking_dict = {3: {(0, 1, 0): [(1, 0, 0)]}, 7: {(0, 1, 0): [(1, 0, 0)]}}
        sage: compatible_systems(split_primes_list, checking_dict)
        [[[(0, 1, 0), (1, 0, 0)], [(0, 1, 0), (1, 0, 0)]]]
    """
def compatible_system_lift(compatible_system, split_primes_list):
    """
    Given a compatible system of exponent vectors and complementary exponent
    vectors, return a lift to the integers.

    INPUT:

    - ``compatible_system`` -- list of pairs ``[ [v0, w0], [v1, w1], .., [vk, wk] ]``
      where [vi, wi] is a pair of complementary exponent vectors modulo ``qi - 1``,
      and all pairs are compatible
    - ``split_primes_list`` -- list of primes ``[ q0, q1, .., qk ]``

    OUTPUT: a pair of vectors ``[v, w]`` satisfying:

    1. ``v[0] == vi[0]`` for all ``i``
    2. ``w[0] == wi[0]`` for all ``i``
    3. ``v[j] == vi[j]`` modulo ``qi - 1`` for all ``i`` and all ``j > 0``
    4. ``w[j] == wi[j]`` modulo ``qi - 1`` for all ``i`` and all `j > 0``
    5. every entry of ``v`` and ``w`` is bounded by ``L/2`` in absolute value, where ``L`` is the least common multiple of ``{qi - 1 : qi in split_primes_list }``

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import compatible_system_lift
        sage: split_primes_list = [3, 7]
        sage: comp_sys = [[(0, 1, 0), (0, 1, 0)], [(0, 3, 4), (0, 1, 2)]]
        sage: compatible_system_lift(comp_sys, split_primes_list)
        [(0, 3, -2), (0, 1, 2)]
    """
def solutions_from_systems(SUK, bound, cs_list, split_primes_list):
    """
    Lift compatible systems to the integers and return the `S`-unit equation
    solutions that the lifts yield.

    INPUT:

    - ``SUK`` -- the group of `S`-units where we search for solutions
    - ``bound`` -- a bound for the entries of all entries of all lifts
    - ``cs_list`` -- list of compatible systems of exponent vectors modulo
      `q-1` for various primes `q`
    - ``split_primes_list`` -- list of primes giving the moduli of the exponent
      vectors in ``cs_list``

    OUTPUT:

    A list of solutions to the S-unit equation. Each solution is a list:

    1. an exponent vector over the integers, ``ev``
    2. an exponent vector over the integers, ``cv``
    3. the S-unit corresponding to ``ev``, ``iota_exp``
    4. the S-unit corresponding to ``cv``, ``iota_comp``

    .. NOTE::

        - Every entry of ``ev`` is less than or equal to bound in absolute value
        - every entry of ``cv`` is less than or equal to bound in absolute value
        - ``iota_exp + iota_comp == 1``

    EXAMPLES:

    Given a single compatible system, a solution can be found. ::

        sage: from sage.rings.number_field.S_unit_solver import solutions_from_systems
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^2 - 15)
        sage: SUK = K.S_unit_group(S=K.primes_above(2))
        sage: split_primes_list = [7, 17]
        sage: a_compatible_system = [[[(0, 0, 5), (0, 0, 5)], [(0, 0, 15), (0, 0, 15)]]]
        sage: solutions_from_systems(SUK, 20, a_compatible_system, split_primes_list)
        [((0, 0, -1), (0, 0, -1), 1/2, 1/2)]
    """
def clean_sfs(sfs_list):
    """
    Given a list of `S`-unit equation solutions, remove trivial redundancies.

    INPUT:

    - ``sfs_list`` -- list of solutions to the `S`-unit equation

    OUTPUT: list of solutions to the `S`-unit equation

    .. NOTE::

        The function looks for cases where `x + y = 1` and `y + x = 1` appear
        as separate solutions, and removes one.

    EXAMPLES:

    The function is not dependent on the number field and removes redundancies in any list. ::

        sage: from sage.rings.number_field.S_unit_solver import clean_sfs
        sage: sols = [((1, 0, 0), (0, 0, 1), -1, 2), ((0, 0, 1), (1, 0, 0), 2, -1)]
        sage: clean_sfs( sols )
        [((1, 0, 0), (0, 0, 1), -1, 2)]
    """
def sieve_below_bound(K, S, bound: int = 10, bump: int = 10, split_primes_list=[], verbose: bool = False):
    """
    Return all solutions to the `S`-unit equation `x + y = 1` over `K` with
    exponents below the given bound.

    INPUT:

    - ``K`` -- a number field (an absolute extension of the rationals)
    - ``S`` -- list of finite primes of `K`
    - ``bound`` -- positive integer upper bound for exponents, solutions with
      exponents having absolute value below this bound will be found (default: 10)
    - ``bump`` -- positive integer by which the minimum LCM will be increased
      if not enough split primes are found in sieving step (default: 10)
    - ``split_primes_list`` -- list of rational primes that split completely in
      the extension `K/\\QQ`, used for sieving. For complete list of solutions
      should have lcm of `\\{(p_i-1)\\} for primes `p_i` greater than bound
      (default: ``[]``).
    - ``verbose`` -- an optional parameter allowing the user to print
      information during the sieving process (default: ``False``)

    OUTPUT:

    A list of tuples `[(A_1, B_1, x_1, y_1), (A_2, B_2, x_2, y_2), \\dots (A_n, B_n, x_n, y_n)]` such that:

    1. The first two entries are tuples `A_i = (a_0, a_1, \\dots, a_t)` and `B_i = (b_0, b_1, \\dots, b_t)` of exponents.
    2. The last two entries are `S`-units `x_i` and `y_i` in `K` with `x_i + y_i = 1`.
    3. If the default generators for the `S`-units of `K` are `(\\rho_0, \\rho_1, \\dots, \\rho_t)`,
       then these satisfy `x_i = \\prod(\\rho_i)^{(a_i)}` and `y_i = \\prod(\\rho_i)^{(b_i)}`.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import sieve_below_bound, eq_up_to_order
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^2 + x + 1)
        sage: SUK = UnitGroup(K, S=tuple(K.primes_above(3)))
        sage: S = SUK.primes()
        sage: sols = sieve_below_bound(K, S, 10)
        sage: expected = [((3, -1), (2, -1), 1/3*xi + 2/3, -1/3*xi + 1/3),
        ....:             ((4, 1), (4, 0), xi + 2, -xi - 1),
        ....:             ((2, 0), (3, 1), xi, -xi + 1),
        ....:             ((1, 0), (5, 0), xi + 1, -xi)]
        sage: eq_up_to_order(sols, expected)
        True
    """
def solve_S_unit_equation(K, S, prec: int = 106, include_exponents: bool = True, include_bound: bool = False, proof=None, verbose: bool = False):
    """
    Return all solutions to the `S`-unit equation `x + y = 1` over `K`.

    INPUT:

    - ``K`` -- a number field (an absolute extension of the rationals)
    - ``S`` -- list of finite primes of `K`
    - ``prec`` -- precision used for computations in real, complex, and `p`-adic
      fields (default: 106)
    - ``include_exponents`` -- whether to include the exponent vectors in the
      returned value (default: ``True``)
    - ``include_bound`` -- whether to return the final computed bound
      (default: ``False``)
    - ``verbose`` -- whether to print information during the sieving step
      (default: ``False``)

    OUTPUT:

    A list of tuples `[(A_1, B_1, x_1, y_1), (A_2, B_2, x_2, y_2), \\dots (A_n, B_n, x_n, y_n)]` such that:

    1. The first two entries are tuples `A_i = (a_0, a_1, \\dots, a_t)` and `B_i = (b_0, b_1, \\dots, b_t)` of exponents.  These will be omitted if ``include_exponents`` is ``False``.
    2. The last two entries are `S`-units `x_i` and `y_i` in `K` with `x_i + y_i = 1`.
    3. If the default generators for the `S`-units of `K` are `(\\rho_0, \\rho_1, \\dots, \\rho_t)``, then these satisfy `x_i = \\prod(\\rho_i)^{(a_i)}` and `y_i = \\prod(\\rho_i)^{(b_i)}`.

    If ``include_bound``, will return a pair ``(sols, bound)`` where ``sols`` is as above and ``bound`` is the bound used for the entries in the exponent vectors.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import solve_S_unit_equation, eq_up_to_order
        sage: x = polygen(ZZ, 'x')
        sage: K.<xi> = NumberField(x^2 + x + 1)
        sage: S = K.primes_above(3)
        sage: sols = solve_S_unit_equation(K, S, 200)
        sage: expected = [((4, 1), (4, 0), xi + 2, -xi - 1),
        ....:             ((3, -1), (2, -1), 1/3*xi + 2/3, -1/3*xi + 1/3),
        ....:             ((1, 0), (5, 0), xi + 1, -xi),
        ....:             ((2, 0), (3, 1), xi, -xi + 1)]
        sage: eq_up_to_order(sols, expected)
        True

    In order to see the bound as well, use the optional parameter ``include_bound``::

        sage: solutions, bound = solve_S_unit_equation(K, S, 100, include_bound=True)
        sage: bound
        6

    You can omit the exponent vectors::

        sage: sols = solve_S_unit_equation(K, S, 200, include_exponents=False)
        sage: expected = [(xi + 2, -xi - 1), (1/3*xi + 2/3, -1/3*xi + 1/3),
        ....:             (-xi, xi + 1), (-xi + 1, xi)]
        sage: set(frozenset(a) for a in sols) == set(frozenset(b) for b in expected)
        True

    It is an error to use values in S that are not primes in K::

        sage: solve_S_unit_equation(K, [3], 200)
        Traceback (most recent call last):
        ...
        ValueError: S must consist only of prime ideals,
        or a single element from which a prime ideal can be constructed.

    We check the case that the rank is 0::

        sage: K.<xi> = NumberField(x^2 + x + 1)
        sage: solve_S_unit_equation(K, [])
        [((1,), (5,), xi + 1, -xi)]
    """
def eq_up_to_order(A, B):
    """
    If ``A`` and ``B`` are lists of four-tuples ``[a0,a1,a2,a3]`` and ``[b0,b1,b2,b3]``,
    check that there is some reordering so that either ``ai=bi`` for all ``i`` or
    ``a0==b1``, ``a1==b0``, ``a2==b3``, ``a3==b2``.

    The entries must be hashable.

    EXAMPLES::

        sage: from sage.rings.number_field.S_unit_solver import eq_up_to_order
        sage: L = [(1,2,3,4), (5,6,7,8)]
        sage: L1 = [L[1], L[0]]
        sage: L2 = [(2,1,4,3), (6,5,8,7)]
        sage: eq_up_to_order(L, L1)
        True
        sage: eq_up_to_order(L, L2)
        True
        sage: eq_up_to_order(L, [(1,2,4,3), (5,6,8,7)])
        False
    """
