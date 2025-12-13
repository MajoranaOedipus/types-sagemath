from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.morphism import RingHomomorphism as RingHomomorphism, RingHomomorphism_im_gens as RingHomomorphism_im_gens
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

class NumberFieldHomomorphism_im_gens(RingHomomorphism_im_gens):
    def __invert__(self):
        """
        Return the inverse of an isomorphism of absolute number fields.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: tau1, tau2 = K.automorphisms(); tau1, tau2
            (Ring endomorphism of Number Field in a with defining polynomial x^2 + 5
              Defn: a |--> a,
             Ring endomorphism of Number Field in a with defining polynomial x^2 + 5
              Defn: a |--> -a)
            sage: ~tau1
            Ring endomorphism of Number Field in a with defining polynomial x^2 + 5
             Defn: a |--> a
            sage: ~tau2
            Ring endomorphism of Number Field in a with defining polynomial x^2 + 5
             Defn: a |--> -a

            sage: L.<z> = CyclotomicField(5)
            sage: tau1, tau2, tau3, tau4 = L.automorphisms()
            sage: (tau1, ~tau1)
            (Ring endomorphism of Cyclotomic Field of order 5 and degree 4
              Defn: z |--> z,
             Ring endomorphism of Cyclotomic Field of order 5 and degree 4
              Defn: z |--> z)
            sage: (tau2, ~tau2)
            (Ring endomorphism of Cyclotomic Field of order 5 and degree 4
              Defn: z |--> z^2,
             Ring endomorphism of Cyclotomic Field of order 5 and degree 4
              Defn: z |--> z^3)
            sage: (tau3, ~tau3)
            (Ring endomorphism of Cyclotomic Field of order 5 and degree 4
              Defn: z |--> z^3,
             Ring endomorphism of Cyclotomic Field of order 5 and degree 4
              Defn: z |--> z^2)

             sage: M.<w> = NumberField(x^4 - 5*x + 5)
             sage: phi = M.hom([z - z^2]); phi
             Ring morphism:
               From: Number Field in w with defining polynomial x^4 - 5*x + 5
               To:   Cyclotomic Field of order 5 and degree 4
               Defn: w |--> -z^2 + z
             sage: phi^-1
             Ring morphism:
               From: Cyclotomic Field of order 5 and degree 4
               To:   Number Field in w with defining polynomial x^4 - 5*x + 5
               Defn: z |--> 3/11*w^3 + 4/11*w^2 + 9/11*w - 14/11
        """
    def preimage(self, y):
        """
        Compute a preimage of `y` in the domain, provided one exists.
        Raises a :exc:`ValueError` if `y` has no preimage.

        INPUT:

        - ``y`` -- an element of the codomain of ``self``

        OUTPUT:

        Returns the preimage of `y` in the domain, if one exists.
        Raises a :exc:`ValueError` if `y` has no preimage.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 7)
            sage: L.<b> = NumberField(x^4 - 7)
            sage: f = K.embeddings(L)[0]
            sage: f.preimage(3*b^2 - 12/7)
            3*a - 12/7
            sage: f.preimage(b)
            Traceback (most recent call last):
            ...
            ValueError: Element 'b' is not in the image of this homomorphism.

        ::

            sage: # needs sage.libs.linbox
            sage: F.<b> = QuadraticField(23)
            sage: G.<a> = F.extension(x^3 + 5)
            sage: f = F.embeddings(G)[0]
            sage: f.preimage(a^3 + 2*b + 3)
            2*b - 2
        """

class RelativeNumberFieldHomomorphism_from_abs(RingHomomorphism):
    """
    A homomorphism from a relative number field to some other ring, stored as a
    homomorphism from the corresponding absolute field.
    """
    def __init__(self, parent, abs_hom) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^3 + 2, x^2 + x + 1])
            sage: f = K.hom(-a*b - a, K); f
            Relative number field endomorphism of
             Number Field in a with defining polynomial x^3 + 2 over its base field
              Defn: a |--> (-b - 1)*a
                    b |--> b
            sage: type(f)
            <class 'sage.rings.number_field.homset.RelativeNumberFieldHomset_with_category.element_class'>
        """
    def abs_hom(self):
        """
        Return the corresponding homomorphism from the absolute number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^3 + 2, x^2 + x + 1])
            sage: K.hom(a, K).abs_hom()
            Ring morphism:
              From: Number Field in a with defining polynomial
                    x^6 - 3*x^5 + 6*x^4 - 3*x^3 - 9*x + 9
              To:   Number Field in a with defining polynomial x^3 + 2 over its base field
              Defn: a |--> a - b
        """
    @cached_method
    def im_gens(self):
        """
        Return the images of the generators under this map.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^3 + 2, x^2 + x + 1])
            sage: K.hom(a, K).im_gens()
            [a, b]
        """

class CyclotomicFieldHomomorphism_im_gens(NumberFieldHomomorphism_im_gens): ...
