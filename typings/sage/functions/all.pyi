from sage.functions.airy import (
    airy_ai as airy_ai,
    airy_ai_prime as airy_ai_prime,
    airy_bi as airy_bi,
    airy_bi_prime as airy_bi_prime,
)
from sage.functions.bessel import (
    Bessel as Bessel,
    bessel_I as bessel_I,
    bessel_J as bessel_J,
    bessel_K as bessel_K,
    bessel_Y as bessel_Y,
    hankel1 as hankel1,
    hankel2 as hankel2,
    spherical_bessel_J as spherical_bessel_J,
    spherical_bessel_Y as spherical_bessel_Y,
    spherical_hankel1 as spherical_hankel1,
    spherical_hankel2 as spherical_hankel2,
    struve_H as struve_H,
    struve_L as struve_L,
)
from sage.functions.exp_integral import (
    Chi as Chi,
    Ci as Ci,
    Ei as Ei,
    Li as Li,
    Shi as Shi,
    Si as Si,
    cos_integral as cos_integral,
    cosh_integral as cosh_integral,
    exp_integral_e as exp_integral_e,
    exp_integral_e1 as exp_integral_e1,
    exp_integral_ei as exp_integral_ei,
    exponential_integral_1 as exponential_integral_1,
    li as li,
    log_integral as log_integral,
    log_integral_offset as log_integral_offset,
    sin_integral as sin_integral,
    sinh_integral as sinh_integral,
)
from sage.functions.gamma import (
    beta as beta,
    gamma as gamma,
    gamma_inc as gamma_inc,
    gamma_inc_lower as gamma_inc_lower,
    log_gamma as log_gamma,
    psi as psi,
)
from sage.functions.generalized import (
    dirac_delta as dirac_delta,
    heaviside as heaviside,
    kronecker_delta as kronecker_delta,
    sgn as sgn,
    sign as sign,
    unit_step as unit_step,
)
from sage.functions.hyperbolic import (
    acosh as acosh,
    acoth as acoth,
    acsch as acsch,
    arccosh as arccosh,
    arccoth as arccoth,
    arccsch as arccsch,
    arcsech as arcsech,
    arcsinh as arcsinh,
    arctanh as arctanh,
    asech as asech,
    asinh as asinh,
    atanh as atanh,
    cosh as cosh,
    coth as coth,
    csch as csch,
    sech as sech,
    sinh as sinh,
    tanh as tanh,
)
from sage.functions.hypergeometric import (
    hypergeometric as hypergeometric,
    hypergeometric_M as hypergeometric_M,
    hypergeometric_U as hypergeometric_U,
)
from sage.functions.jacobi import (
    inverse_jacobi as inverse_jacobi,
    inverse_jacobi_cd as inverse_jacobi_cd,
    inverse_jacobi_cn as inverse_jacobi_cn,
    inverse_jacobi_cs as inverse_jacobi_cs,
    inverse_jacobi_dc as inverse_jacobi_dc,
    inverse_jacobi_dn as inverse_jacobi_dn,
    inverse_jacobi_ds as inverse_jacobi_ds,
    inverse_jacobi_nc as inverse_jacobi_nc,
    inverse_jacobi_nd as inverse_jacobi_nd,
    inverse_jacobi_ns as inverse_jacobi_ns,
    inverse_jacobi_sc as inverse_jacobi_sc,
    inverse_jacobi_sd as inverse_jacobi_sd,
    inverse_jacobi_sn as inverse_jacobi_sn,
    jacobi as jacobi,
    jacobi_am as jacobi_am,
    jacobi_cd as jacobi_cd,
    jacobi_cn as jacobi_cn,
    jacobi_cs as jacobi_cs,
    jacobi_dc as jacobi_dc,
    jacobi_dn as jacobi_dn,
    jacobi_ds as jacobi_ds,
    jacobi_nc as jacobi_nc,
    jacobi_nd as jacobi_nd,
    jacobi_ns as jacobi_ns,
    jacobi_sc as jacobi_sc,
    jacobi_sd as jacobi_sd,
    jacobi_sn as jacobi_sn,
)
from sage.functions.log import (
    dilog as dilog,
    exp as exp,
    exp_polar as exp_polar,
    harmonic_number as harmonic_number,
    lambert_w as lambert_w,
    ln as ln,
    log as log,
    polylog as polylog,
)
from sage.functions.min_max import (
    max_symbolic as max_symbolic,
    min_symbolic as min_symbolic,
)
from sage.functions.orthogonal_polys import (
    chebyshev_T as chebyshev_T,
    chebyshev_U as chebyshev_U,
    gegenbauer as gegenbauer,
    gen_laguerre as gen_laguerre,
    gen_legendre_P as gen_legendre_P,
    gen_legendre_Q as gen_legendre_Q,
    hahn as hahn,
    hermite as hermite,
    jacobi_P as jacobi_P,
    krawtchouk as krawtchouk,
    laguerre as laguerre,
    legendre_P as legendre_P,
    legendre_Q as legendre_Q,
    meixner as meixner,
    ultraspherical as ultraspherical,
)
from sage.functions.other import (
    abs_symbolic as abs_symbolic,
    arg as arg,
    binomial as binomial,
    cases as cases,
    ceil as ceil,
    complex_root_of as complex_root_of,
    conjugate as conjugate,
    factorial as factorial,
    floor as floor,
    frac as frac,
    imag as imag,
    imag_part as imag_part,
    imaginary as imaginary,
    real as real,
    real_nth_root as real_nth_root,
    real_part as real_part,
    sqrt as sqrt,
)
from sage.functions.prime_pi import (
    legendre_phi as legendre_phi,
    partial_sieve_function as partial_sieve_function,
    prime_pi as prime_pi,
)
from sage.functions.special import (
    elliptic_e as elliptic_e,
    elliptic_ec as elliptic_ec,
    elliptic_eu as elliptic_eu,
    elliptic_f as elliptic_f,
    elliptic_j as elliptic_j,
    elliptic_kc as elliptic_kc,
    elliptic_pi as elliptic_pi,
    spherical_harmonic as spherical_harmonic,
)
from sage.functions.spike_function import spike_function as spike_function
from sage.functions.transcendental import (
    dickman_rho as dickman_rho,
    hurwitz_zeta as hurwitz_zeta,
    stieltjes as stieltjes,
    zeta as zeta,
    zeta_symmetric as zeta_symmetric,
    zetaderiv as zetaderiv,
)
from sage.functions.trig import (
    acos as acos,
    acot as acot,
    acsc as acsc,
    arccos as arccos,
    arccot as arccot,
    arccsc as arccsc,
    arcsec as arcsec,
    arcsin as arcsin,
    arctan as arctan,
    arctan2 as arctan2,
    asec as asec,
    asin as asin,
    atan as atan,
    atan2 as atan2,
    cos as cos,
    cot as cot,
    csc as csc,
    sec as sec,
    sin as sin,
    tan as tan,
)
from sage.functions.wigner import (
    clebsch_gordan as clebsch_gordan,
    gaunt as gaunt,
    racah as racah,
    wigner_3j as wigner_3j,
    wigner_6j as wigner_6j,
    wigner_9j as wigner_9j,
)
from sage.functions.piecewise import piecewise as piecewise
from sage.functions.error import (
    erf as erf, erfc as erfc, erfi as erfi, erfinv as erfinv,
    fresnel_sin as fresnel_sin, fresnel_cos as fresnel_cos
)

reciprocal_trig_functions= {
    'sec': cos, 'csc': sin,
    'cot': tan, 'sech': cosh, 'csch': sinh, 'coth': tanh}
Γ = gamma
ψ = psi
ζ = zeta
