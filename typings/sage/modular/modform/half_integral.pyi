from . import constructor as constructor
from .theta import theta2_qexp as theta2_qexp, theta_qexp as theta_qexp
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.modular.dirichlet import DirichletGroup as DirichletGroup

def half_integral_weight_modform_basis(chi, k, prec):
    '''
    A basis for the space of weight `k/2` forms with character
    `\\chi`. The modulus of `\\chi` must be divisible by
    `16` and `k` must be odd and `>1`.

    INPUT:

    - ``chi`` -- a Dirichlet character with modulus divisible by 16

    - ``k`` -- an odd integer > 1

    - ``prec`` -- positive integer

    OUTPUT: list of power series

    .. warning::

       1. This code is very slow because it requests computation of a
          basis of modular forms for integral weight spaces, and that
          computation is still very slow.

       2. If you give an input prec that is too small, then the output
          list of power series may be larger than the dimension of the
          space of half-integral forms.

    EXAMPLES:

    We compute some half-integral weight forms of level 16\\*7

    ::

        sage: half_integral_weight_modform_basis(DirichletGroup(16*7).0^2,3,30)
        [q - 2*q^2 - q^9 + 2*q^14 + 6*q^18 - 2*q^21 - 4*q^22 - q^25 + O(q^30),
         q^2 - q^14 - 3*q^18 + 2*q^22 + O(q^30),
         q^4 - q^8 - q^16 + q^28 + O(q^30),
         q^7 - 2*q^15 + O(q^30)]

    The following illustrates that choosing too low of a precision can
    give an incorrect answer.

    ::

        sage: half_integral_weight_modform_basis(DirichletGroup(16*7).0^2,3,20)
        [q - 2*q^2 - q^9 + 2*q^14 + 6*q^18 + O(q^20),
         q^2 - q^14 - 3*q^18 + O(q^20),
         q^4 - 2*q^8 + 2*q^12 - 4*q^16 + O(q^20),
         q^7 - 2*q^8 + 4*q^12 - 2*q^15 - 6*q^16 + O(q^20),
         q^8 - 2*q^12 + 3*q^16 + O(q^20)]

    We compute some spaces of low level and the first few possible
    weights.

    ::

        sage: half_integral_weight_modform_basis(DirichletGroup(16,QQ).1, 3, 10)
        []
        sage: half_integral_weight_modform_basis(DirichletGroup(16,QQ).1, 5, 10)
        [q - 2*q^3 - 2*q^5 + 4*q^7 - q^9 + O(q^10)]
        sage: half_integral_weight_modform_basis(DirichletGroup(16,QQ).1, 7, 10)
        [q - 2*q^2 + 4*q^3 + 4*q^4 - 10*q^5 - 16*q^7 + 19*q^9 + O(q^10),
         q^2 - 2*q^3 - 2*q^4 + 4*q^5 + 4*q^7 - 8*q^9 + O(q^10),
         q^3 - 2*q^5 - 2*q^7 + 4*q^9 + O(q^10)]
        sage: half_integral_weight_modform_basis(DirichletGroup(16,QQ).1, 9, 10)
        [q - 2*q^2 + 4*q^3 - 8*q^4 + 14*q^5 + 16*q^6 - 40*q^7 + 16*q^8 - 57*q^9 + O(q^10),
         q^2 - 2*q^3 + 4*q^4 - 8*q^5 - 8*q^6 + 20*q^7 - 8*q^8 + 32*q^9 + O(q^10),
         q^3 - 2*q^4 + 4*q^5 + 4*q^6 - 10*q^7 - 16*q^9 + O(q^10),
         q^4 - 2*q^5 - 2*q^6 + 4*q^7 + 4*q^9 + O(q^10),
         q^5 - 2*q^7 - 2*q^9 + O(q^10)]

    This example once raised an error (see :issue:`5792`).

    ::

        sage: half_integral_weight_modform_basis(trivial_character(16),9,10)
        [q - 2*q^2 + 4*q^3 - 8*q^4 + 4*q^6 - 16*q^7 + 48*q^8 - 15*q^9 + O(q^10),
         q^2 - 2*q^3 + 4*q^4 - 2*q^6 + 8*q^7 - 24*q^8 + O(q^10),
         q^3 - 2*q^4 - 4*q^7 + 12*q^8 + O(q^10),
         q^4 - 6*q^8 + O(q^10)]


    ALGORITHM: Basmaji (page 55 of his Essen thesis, "Ein Algorithmus
    zur Berechnung von Hecke-Operatoren und Anwendungen auf modulare
    Kurven", https://web.archive.org/web/20160905111513/http://wstein.org/scans/papers/basmaji/thesis_of_basmaji.dvi).

    Let `S = S_{k+1}(\\epsilon)` be the space of cusp forms of
    even integer weight `k+1` and character
    `\\varepsilon = \\chi \\psi^{(k+1)/2}`, where `\\psi`
    is the nontrivial mod-4 Dirichlet character. Let `U` be the
    subspace of `S \\times S` of elements `(a,b)` such
    that `\\Theta_2 a = \\Theta_3 b`. Then `U` is
    isomorphic to `S_{k/2}(\\chi)` via the map
    `(a,b) \\mapsto a/\\Theta_3`.
    '''
