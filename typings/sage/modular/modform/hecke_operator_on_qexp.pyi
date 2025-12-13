from .element import ModularFormElement as ModularFormElement
from sage.arith.misc import divisors as divisors, gcd as gcd
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modular.dirichlet import DirichletCharacter as DirichletCharacter, DirichletGroup as DirichletGroup
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring_element import PowerSeries as PowerSeries

def hecke_operator_on_qexp(f, n, k, eps=None, prec=None, check: bool = True, _return_list: bool = False):
    """
    Given the `q`-expansion `f` of a modular form with character
    `\\varepsilon`, this function computes the image of `f` under the
    Hecke operator `T_{n,k}` of weight `k`.

    EXAMPLES::

        sage: M = ModularForms(1,12)
        sage: hecke_operator_on_qexp(M.basis()[0], 3, 12)
        252*q - 6048*q^2 + 63504*q^3 - 370944*q^4 + O(q^5)
        sage: hecke_operator_on_qexp(M.basis()[0], 1, 12, prec=7)
        q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 + O(q^7)
        sage: hecke_operator_on_qexp(M.basis()[0], 1, 12)
        q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + 84480*q^8
          - 113643*q^9 - 115920*q^10 + 534612*q^11 - 370944*q^12 - 577738*q^13 + O(q^14)

        sage: M.prec(20)
        20
        sage: hecke_operator_on_qexp(M.basis()[0], 3, 12)
        252*q - 6048*q^2 + 63504*q^3 - 370944*q^4 + 1217160*q^5 - 1524096*q^6 + O(q^7)
        sage: hecke_operator_on_qexp(M.basis()[0], 1, 12)
        q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + 84480*q^8
          - 113643*q^9 - 115920*q^10 + 534612*q^11 - 370944*q^12 - 577738*q^13
          + 401856*q^14 + 1217160*q^15 + 987136*q^16 - 6905934*q^17 + 2727432*q^18
          + 10661420*q^19 - 7109760*q^20 + O(q^21)

        sage: (hecke_operator_on_qexp(M.basis()[0], 1, 12)*252).add_bigoh(7)
        252*q - 6048*q^2 + 63504*q^3 - 370944*q^4 + 1217160*q^5 - 1524096*q^6 + O(q^7)

        sage: hecke_operator_on_qexp(M.basis()[0], 6, 12)
        -6048*q + 145152*q^2 - 1524096*q^3 + O(q^4)

    An example on a formal power series::

        sage: R.<q> = QQ[[]]
        sage: f = q + q^2 + q^3 + q^7 + O(q^8)
        sage: hecke_operator_on_qexp(f, 3, 12)
        q + O(q^3)
        sage: hecke_operator_on_qexp(delta_qexp(24), 3, 12).prec()
        8
        sage: hecke_operator_on_qexp(delta_qexp(25), 3, 12).prec()
        9

    An example of computing `T_{p,k}` in characteristic `p`::

        sage: p = 199
        sage: fp = delta_qexp(prec=p^2+1, K=GF(p))
        sage: tfp = hecke_operator_on_qexp(fp, p, 12)
        sage: tfp == fp[p] * fp
        True
        sage: tf = hecke_operator_on_qexp(delta_qexp(prec=p^2+1), p, 12).change_ring(GF(p))
        sage: tfp == tf
        True
    """
def hecke_operator_on_basis(B, n, k, eps=None, already_echelonized: bool = False):
    """
    Given a basis `B` of `q`-expansions for a space of modular forms
    with character `\\varepsilon` to precision at least `\\#B\\cdot n+1`,
    this function computes the matrix of `T_n` relative to `B`.

    .. NOTE::

       If the elements of B are not known to sufficient precision,
       this function will report that the vectors are linearly
       dependent (since they are to the specified precision).

    INPUT:

    - ``B`` -- list of `q`-expansions

    - ``n`` -- integer >= 1

    - ``k`` -- integer

    - ``eps`` -- Dirichlet character

    - ``already_echelonized`` -- boolean (default: ``False``); if ``True``, use
      that the basis is already in Echelon form, which saves a lot of time

    EXAMPLES::

        sage: sage.modular.modform.constructor.ModularForms_clear_cache()
        sage: ModularForms(1,12).q_expansion_basis()
        [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6),
         1 + 65520/691*q + 134250480/691*q^2 + 11606736960/691*q^3 + 274945048560/691*q^4 + 3199218815520/691*q^5 + O(q^6)]
        sage: hecke_operator_on_basis(ModularForms(1,12).q_expansion_basis(), 3, 12)
        Traceback (most recent call last):
        ...
        ValueError: The given basis vectors must be linearly independent.

        sage: hecke_operator_on_basis(ModularForms(1,12).q_expansion_basis(30), 3, 12)
        [   252      0]
        [     0 177148]

    TESTS:

    This shows that the problem with finite fields reported at :issue:`8281` is solved::

        sage: bas_mod5 = [f.change_ring(GF(5)) for f in victor_miller_basis(12, 20)]
        sage: hecke_operator_on_basis(bas_mod5, 2, 12)
        [4 0]
        [0 1]

    This shows that empty input is handled sensibly (:issue:`12202`)::

        sage: # needs sage.rings.number_field
        sage: x = hecke_operator_on_basis([], 3, 12); x
        []
        sage: x.parent()
        Full MatrixSpace of 0 by 0 dense matrices over Cyclotomic Field of order 1 and degree 1
        sage: y = hecke_operator_on_basis([], 3, 12, eps=DirichletGroup(13).0^2); y
        []
        sage: y.parent()
        Full MatrixSpace of 0 by 0 dense matrices over Cyclotomic Field of order 12 and degree 4
    """
