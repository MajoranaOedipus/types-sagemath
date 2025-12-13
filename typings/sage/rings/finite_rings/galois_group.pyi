from sage.groups.abelian_gps.abelian_group_element import AbelianGroupElement as AbelianGroupElement
from sage.groups.galois_group import GaloisGroup_cyc as GaloisGroup_cyc
from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic as FiniteFieldHomomorphism_generic, FrobeniusEndomorphism_finite_field as FrobeniusEndomorphism_finite_field
from sage.rings.integer_ring import ZZ as ZZ

class GaloisGroup_GFElement(AbelianGroupElement):
    def as_hom(self):
        """
        Return the automorphism of the finite field corresponding to this element.

        EXAMPLES::

            sage: GF(3^6).galois_group()([4]).as_hom()
            Frobenius endomorphism z6 |--> z6^(3^4) on Finite Field in z6 of size 3^6
        """
    def __call__(self, x):
        """
        Return the action of this automorphism on an element `x` of the finite field.

        EXAMPLES::

            sage: k.<a> = GF(3^6)
            sage: g = k.galois_group()([4])
            sage: g(a) == a^(3^4)
            True
        """
    def fixed_field(self):
        """
        The fixed field of this automorphism.

        EXAMPLES::

            sage: k.<a> = GF(3^12)
            sage: g = k.galois_group()([8])
            sage: k0, embed = g.fixed_field()
            sage: k0.cardinality()
            81
            sage: embed.domain() is k0
            True
            sage: embed.codomain() is k
            True
        """

class GaloisGroup_GF(GaloisGroup_cyc):
    """
    The Galois group of a finite field.
    """
    Element = GaloisGroup_GFElement
    def __init__(self, field) -> None:
        """
        Create a Galois group.

        TESTS::

            sage: TestSuite(GF(9).galois_group()).run()
        """
