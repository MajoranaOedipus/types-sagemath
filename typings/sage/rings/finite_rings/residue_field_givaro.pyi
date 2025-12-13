import sage.rings.finite_rings.finite_field_givaro
import sage.rings.finite_rings.residue_field
from sage.rings.finite_rings.finite_field_givaro import FiniteField_givaro as FiniteField_givaro
from sage.rings.finite_rings.residue_field import ReductionMap as ReductionMap, ResidueFieldHomomorphism_global as ResidueFieldHomomorphism_global, ResidueField_generic as ResidueField_generic
from typing import Any

class ResidueFiniteField_givaro(sage.rings.finite_rings.residue_field.ResidueField_generic, sage.rings.finite_rings.finite_field_givaro.FiniteField_givaro):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/residue_field_givaro.pyx (starting at line 29)

        The class representing residue fields of number fields that have non-prime
        order strictly less than `2^16`.

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

            sage: R.<t> = GF(7)[]; P = R.ideal(t^2 + 4)
            sage: k.<a> = R.residue_field(P); type(k)
            <class 'sage.rings.finite_rings.residue_field_givaro.ResidueFiniteField_givaro_with_category'>
            sage: k(1/t)
            5*a
    """
    def __init__(self, p, q, name, modulus, to_vs, to_order, PB) -> Any:
        """ResidueFiniteField_givaro.__init__(self, p, q, name, modulus, to_vs, to_order, PB)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/residue_field_givaro.pyx (starting at line 57)

        INPUT:

        - ``p`` -- the prime ideal defining this residue field

        - ``q`` -- the order of this residue field (a power of intp)

        - ``name`` -- the name of the generator of this extension

        - ``modulus`` -- the polynomial modulus for this extension

        - ``to_vs`` -- the map from the number field (or function field) to
          the appropriate vector space (over `\\QQ` or `F_p(t)`)

        - ``to_order`` -- the map from a lattice in that vector space to the maximal order

        - ``PB`` -- a matrix used in defining the reduction and lifting maps

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)                                 # needs sage.rings.number_field
            sage: P = K.ideal(61).factor()[0][0]                                        # needs sage.rings.number_field
            sage: k = K.residue_field(P)                                                # needs sage.rings.number_field

            sage: R.<t> = GF(3)[]; P = R.ideal(t^4 - t^3 + t + 1); k.<a> = P.residue_field(); type(k)
            <class 'sage.rings.finite_rings.residue_field_givaro.ResidueFiniteField_givaro_with_category'>
            sage: a^5
            a^3 + 2*a^2 + a + 2"""
