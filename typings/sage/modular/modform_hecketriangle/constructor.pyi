from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

def rational_type(f, n=..., base_ring=...):
    '''
    Return the basic analytic properties that can be determined
    directly from the specified rational function ``f``
    which is interpreted as a representation of an
    element of a FormsRing for the Hecke Triangle group
    with parameter ``n`` and the specified ``base_ring``.

    In particular the following degree of the generators is assumed:

    `deg(1) := (0, 1)`
    `deg(x) := (4/(n-2), 1)`
    `deg(y) := (2n/(n-2), -1)`
    `deg(z) := (2, -1)`

    The meaning of homogeneous elements changes accordingly.

    INPUT:

    - ``f`` -- a rational function in ``x,y,z,d`` over ``base_ring``

    - ``n`` -- integer greater or equal to `3` corresponding
      to the ``HeckeTriangleGroup`` with that parameter (default: `3`)

    - ``base_ring`` -- the base ring of the corresponding forms ring, resp.
      polynomial ring (default: ``ZZ``)

    OUTPUT:

    A tuple ``(elem, homo, k, ep, analytic_type)`` describing the basic
    analytic properties of `f` (with the interpretation indicated above).

    - ``elem`` -- ``True`` if `f` has a homogeneous denominator

    - ``homo`` -- ``True`` if `f` also has a homogeneous numerator

    - ``k`` -- ``None`` if `f` is not homogeneous, otherwise
      the weight of `f` (which is the first component of its degree)

    - ``ep`` -- ``None`` if `f` is not homogeneous, otherwise
      the multiplier of `f` (which is the second component of its degree)

    - ``analytic_type`` -- the :class:`AnalyticType` of `f`

    For the zero function the degree `(0, 1)` is chosen.

    This function is (heavily) used to determine the type of elements
    and to check if the element really is contained in its parent.

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.constructor import rational_type

        sage: rational_type(0, n=4)
        (True, True, 0, 1, zero)
        sage: rational_type(1, n=12)
        (True, True, 0, 1, modular)

        sage: # needs sage.symbolic
        sage: (x,y,z,d) = var("x,y,z,d")
        sage: rational_type(x^3 - y^2)
        (True, True, 12, 1, cuspidal)
        sage: rational_type(x * z, n=7)
        (True, True, 14/5, -1, quasi modular)
        sage: rational_type(1/(x^3 - y^2) + z/d)
        (True, False, None, None, quasi weakly holomorphic modular)
        sage: rational_type(x^3/(x^3 - y^2))
        (True, True, 0, 1, weakly holomorphic modular)
        sage: rational_type(1/(x + z))
        (False, False, None, None, None)
        sage: rational_type(1/x + 1/z)
        (True, False, None, None, quasi meromorphic modular)
        sage: rational_type(d/x, n=10)
        (True, True, -1/2, 1, meromorphic modular)
        sage: rational_type(1.1 * z * (x^8-y^2), n=8, base_ring=CC)
        (True, True, 22/3, -1, quasi cuspidal)
        sage: rational_type(x-y^2, n=infinity)
        (True, True, 4, 1, modular)
        sage: rational_type(x*(x-y^2), n=infinity)
        (True, True, 8, 1, cuspidal)
        sage: rational_type(1/x, n=infinity)
        (True, True, -4, 1, weakly holomorphic modular)
    '''
def FormsSpace(analytic_type, group: int = 3, base_ring=..., k=..., ep=None):
    '''
    Return the FormsSpace with the given ``analytic_type``, ``group``
    ``base_ring`` and degree (``k``, ``ep``).

    INPUT:

    - ``analytic_type`` -- an element of ``AnalyticType()`` describing
      the analytic type of the space

    - ``group`` -- the index of the (Hecke triangle) group of the space (default: `3`)

    - ``base_ring`` -- the base ring of the space (default: ``ZZ``)

    - ``k`` -- the weight of the space, a rational number (default: ``0``)

    - ``ep`` -- the multiplier of the space, `1`, `-1` or ``None``
      (in which case ``ep`` should be determined from ``k``). Default: ``None``.

    For the variables ``group``, ``base_ring``, ``k``, ``ep``
    the same arguments as for the class ``FormsSpace_abstract`` can be used.
    The variables will then be put in canonical form.
    In particular the multiplier ``ep`` is calculated
    as usual from ``k`` if ``ep == None``.

    OUTPUT: the FormsSpace with the given properties

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.constructor import FormsSpace
        sage: FormsSpace([])
        ZeroForms(n=3, k=0, ep=1) over Integer Ring
        sage: FormsSpace(["quasi"]) # not implemented

        sage: FormsSpace("cusp", group=5, base_ring=CC, k=12, ep=1)
        CuspForms(n=5, k=12, ep=1) over Complex Field with 53 bits of precision

        sage: FormsSpace("holo")
        ModularForms(n=3, k=0, ep=1) over Integer Ring

        sage: FormsSpace("weak", group=6, base_ring=ZZ, k=0, ep=-1)
        WeakModularForms(n=6, k=0, ep=-1) over Integer Ring

        sage: FormsSpace("mero", group=7, base_ring=ZZ, k=2, ep=-1)
        MeromorphicModularForms(n=7, k=2, ep=-1) over Integer Ring

        sage: FormsSpace(["quasi", "cusp"], group=5, base_ring=CC, k=12, ep=1)
        QuasiCuspForms(n=5, k=12, ep=1) over Complex Field with 53 bits of precision

        sage: FormsSpace(["quasi", "holo"])
        QuasiModularForms(n=3, k=0, ep=1) over Integer Ring

        sage: FormsSpace(["quasi", "weak"], group=6, base_ring=ZZ, k=0, ep=-1)
        QuasiWeakModularForms(n=6, k=0, ep=-1) over Integer Ring

        sage: FormsSpace(["quasi", "mero"], group=7, base_ring=ZZ, k=2, ep=-1)
        QuasiMeromorphicModularForms(n=7, k=2, ep=-1) over Integer Ring

        sage: FormsSpace(["quasi", "cusp"], group=infinity, base_ring=ZZ, k=2, ep=-1)
        QuasiCuspForms(n=+Infinity, k=2, ep=-1) over Integer Ring
    '''
def FormsRing(analytic_type, group: int = 3, base_ring=..., red_hom: bool = False):
    '''
    Return the FormsRing with the given ``analytic_type``, ``group``
    ``base_ring`` and variable ``red_hom``.

    INPUT:

    - ``analytic_type`` -- an element of ``AnalyticType()`` describing
      the analytic type of the space

    - ``group`` -- the index of the (Hecke triangle) group of the space
      (default: 3`)

    - ``base_ring`` -- the base ring of the space (default: ``ZZ``)

    - ``red_hom`` -- the (boolean) variable ``red_hom`` of the space
      (default: ``False``)

    For the variables ``group``, ``base_ring``, ``red_hom``
    the same arguments as for the class :class:`FormsRing_abstract` can be used.
    The variables will then be put in canonical form.

    OUTPUT: the FormsRing with the given properties

    EXAMPLES::

        sage: from sage.modular.modform_hecketriangle.constructor import FormsRing
        sage: FormsRing("cusp", group=5, base_ring=CC)
        CuspFormsRing(n=5) over Complex Field with 53 bits of precision

        sage: FormsRing("holo")
        ModularFormsRing(n=3) over Integer Ring

        sage: FormsRing("weak", group=6, base_ring=ZZ, red_hom=True)
        WeakModularFormsRing(n=6) over Integer Ring

        sage: FormsRing("mero", group=7, base_ring=ZZ)
        MeromorphicModularFormsRing(n=7) over Integer Ring

        sage: FormsRing(["quasi", "cusp"], group=5, base_ring=CC)
        QuasiCuspFormsRing(n=5) over Complex Field with 53 bits of precision

        sage: FormsRing(["quasi", "holo"])
        QuasiModularFormsRing(n=3) over Integer Ring

        sage: FormsRing(["quasi", "weak"], group=6, base_ring=ZZ, red_hom=True)
        QuasiWeakModularFormsRing(n=6) over Integer Ring

        sage: FormsRing(["quasi", "mero"], group=7, base_ring=ZZ, red_hom=True)
        QuasiMeromorphicModularFormsRing(n=7) over Integer Ring

        sage: FormsRing(["quasi", "cusp"], group=infinity)
        QuasiCuspFormsRing(n=+Infinity) over Integer Ring
    '''
