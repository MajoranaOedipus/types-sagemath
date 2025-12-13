import sage.rings.finite_rings.finite_field_ntl_gf2e
import sage.rings.finite_rings.residue_field
from sage.rings.finite_rings.finite_field_ntl_gf2e import FiniteField_ntl_gf2e as FiniteField_ntl_gf2e
from sage.rings.finite_rings.residue_field import ReductionMap as ReductionMap, ResidueFieldHomomorphism_global as ResidueFieldHomomorphism_global, ResidueField_generic as ResidueField_generic
from typing import Any

class ResidueFiniteField_ntl_gf2e(sage.rings.finite_rings.residue_field.ResidueField_generic, sage.rings.finite_rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/residue_field_ntl_gf2e.pyx (starting at line 29)

        The class representing residue fields with order a power of 2.

        When the order is less than `2^16`, givaro is used by default instead.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 7)
            sage: P = K.ideal(29).factor()[0][0]
            sage: k = K.residue_field(P)
            sage: k.degree()
            2
            sage: OK = K.maximal_order()
            sage: c = OK(a)
            sage: b = k(c)
            sage: b*c^2
            7
            sage: b*c
            13*abar + 5

            sage: R.<t> = GF(2)[]; P = R.ideal(t^19 + t^5 + t^2 + t + 1)
            sage: k.<a> = R.residue_field(P); type(k)
            <class 'sage.rings.finite_rings.residue_field_ntl_gf2e.ResidueFiniteField_ntl_gf2e_with_category'>
            sage: k(1/t)
            a^18 + a^4 + a + 1
            sage: k(1/t)*t
            1
    """
    def __init__(self, q, name, modulus, repr, p, to_vs, to_order, PB) -> Any:
        """ResidueFiniteField_ntl_gf2e.__init__(self, q, name, modulus, repr, p, to_vs, to_order, PB)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/residue_field_ntl_gf2e.pyx (starting at line 61)

        INPUT:

        - ``p`` -- the prime ideal defining this residue field

        - ``q`` -- the order of this residue field

        - ``name`` -- the name of the generator of this extension

        - ``modulus`` -- the polynomial modulus for this extension

        - ``to_vs`` -- the map from the number field (or function field) to
          the appropriate vector space (over `\\QQ` or `F_p(t)`)

        - ``to_order`` -- the map from a lattice in that vector space to the
          maximal order

        - ``PB`` -- a matrix used in defining the reduction and lifting maps

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)                                 # needs sage.rings.number_field
            sage: P = K.ideal(61).factor()[0][0]                                        # needs sage.rings.number_field
            sage: k = K.residue_field(P)                                                # needs sage.rings.number_field

            sage: R.<t> = GF(3)[]; P = R.ideal(t^4 - t^3 + t + 1); k.<a> = P.residue_field()
            sage: type(k)                                                               # needs sage.libs.linbox
            <class 'sage.rings.finite_rings.residue_field_givaro.ResidueFiniteField_givaro_with_category'>
            sage: a^5
            a^3 + 2*a^2 + a + 2"""
