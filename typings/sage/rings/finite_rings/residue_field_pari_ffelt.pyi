import sage.rings.finite_rings.finite_field_pari_ffelt
import sage.rings.finite_rings.residue_field
from sage.rings.finite_rings.finite_field_pari_ffelt import FiniteField_pari_ffelt as FiniteField_pari_ffelt
from sage.rings.finite_rings.residue_field import ReductionMap as ReductionMap, ResidueFieldHomomorphism_global as ResidueFieldHomomorphism_global, ResidueField_generic as ResidueField_generic
from typing import Any

class ResidueFiniteField_pari_ffelt(sage.rings.finite_rings.residue_field.ResidueField_generic, sage.rings.finite_rings.finite_field_pari_ffelt.FiniteField_pari_ffelt):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/residue_field_pari_ffelt.pyx (starting at line 29)

        The class representing residue fields of number fields that have non-prime
        order at least `2^16`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 7)
            sage: P = K.ideal(923478923).factor()[0][0]
            sage: k = K.residue_field(P)
            sage: k.degree()
            2
            sage: OK = K.maximal_order()
            sage: c = OK(a)
            sage: b = k(c)
            sage: b + c
            2*abar
            sage: b*c
            664346875*abar + 535606347
            sage: k.base_ring()
            Finite Field of size 923478923

            sage: R.<t> = GF(5)[]
            sage: P = R.ideal(4*t^12 + 3*t^11 + 4*t^10 + t^9 + t^8
            ....:             + 3*t^7 + 2*t^6 + 3*t^4 + t^3 + 3*t^2 + 2)
            sage: k.<a> = P.residue_field()
            sage: type(k)
            <class 'sage.rings.finite_rings.residue_field_pari_ffelt.ResidueFiniteField_pari_ffelt_with_category'>
            sage: k(1/t)
            3*a^11 + a^10 + 3*a^9 + 2*a^8 + 2*a^7 + a^6 + 4*a^5 + a^3 + 2*a^2 + a
    """
    def __init__(self, p, characteristic, name, modulus, to_vs, to_order, PB) -> Any:
        """ResidueFiniteField_pari_ffelt.__init__(self, p, characteristic, name, modulus, to_vs, to_order, PB)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/residue_field_pari_ffelt.pyx (starting at line 63)

        Initialize ``self``.

        EXAMPLES:

        We create a residue field with implementation ``pari_ffelt``::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 7)
            sage: P = K.ideal(923478923).factor()[0][0]
            sage: type(P.residue_field())
            <class 'sage.rings.finite_rings.residue_field_pari_ffelt.ResidueFiniteField_pari_ffelt_with_category'>"""
