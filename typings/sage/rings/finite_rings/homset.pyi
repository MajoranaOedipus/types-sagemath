from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic as FiniteFieldHomomorphism_generic
from sage.rings.homset import RingHomset_generic as RingHomset_generic
from sage.rings.integer import Integer as Integer
from sage.rings.morphism import RingHomomorphism_im_gens as RingHomomorphism_im_gens
from sage.structure.sequence import Sequence as Sequence

class FiniteFieldHomset(RingHomset_generic):
    """
    Set of homomorphisms with domain a given finite field.
    """
    def __call__(self, im_gens, base_map=None, check: bool = True):
        """
        Construct the homomorphism defined by ``im_gens``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: E.<a> = GF(25, modulus = t^2 - 2)
            sage: F.<b> = GF(625)
            sage: End(E)
            Automorphism group of Finite Field in a of size 5^2
            sage: list(Hom(E, F))
            [Ring morphism:
              From: Finite Field in a of size 5^2
              To:   Finite Field in b of size 5^4
              Defn: a |--> 4*b^3 + 4*b^2 + 4*b,
             Ring morphism:
              From: Finite Field in a of size 5^2
              To:   Finite Field in b of size 5^4
              Defn: a |--> b^3 + b^2 + b]
            sage: [phi(2*a)^2 for phi in Hom(E, F)]
            [3, 3]
            sage: End(GF(7))[0]
            Ring endomorphism of Finite Field of size 7
              Defn: 1 |--> 1
            sage: H = Hom(GF(7), GF(49, 'c'))
            sage: H[0](2)
            2
            sage: Hom(GF(49, 'c'), GF(7)).list()
            []
            sage: Hom(GF(49, 'c'), GF(81, 'd')).list()
            []
            sage: H = Hom(GF(9, 'a'), GF(81, 'b'))
            sage: H == loads(dumps(H))
            True
        """
    def is_aut(self):
        """
        Check if ``self`` is an automorphism.

        EXAMPLES::

            sage: Hom(GF(4, 'a'), GF(16, 'b')).is_aut()
            False
            sage: Hom(GF(4, 'a'), GF(4, 'c')).is_aut()
            False
            sage: Hom(GF(4, 'a'), GF(4, 'a')).is_aut()
            True
        """
    def order(self):
        """
        Return the order of this set of field homomorphisms.

        EXAMPLES::

            sage: K.<a> = GF(125)
            sage: End(K)
            Automorphism group of Finite Field in a of size 5^3
            sage: End(K).order()
            3
            sage: L.<b> = GF(25)
            sage: Hom(L, K).order() == Hom(K, L).order() == 0
            True
        """
    def __len__(self) -> int:
        """
        Return the number of elements of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(25)
            sage: len(End(K))
            2
        """
    def list(self):
        """
        Return a list of all the elements in this set of field homomorphisms.

        EXAMPLES::

            sage: K.<a> = GF(25)
            sage: End(K)
            Automorphism group of Finite Field in a of size 5^2
            sage: list(End(K))
            [Ring endomorphism of Finite Field in a of size 5^2
              Defn: a |--> 4*a + 1,
             Ring endomorphism of Finite Field in a of size 5^2
              Defn: a |--> a]
            sage: L.<z> = GF(7^6)
            sage: [g for g in End(L) if (g^3)(z) == z]
            [Ring endomorphism of Finite Field in z of size 7^6
              Defn: z |--> z,
             Ring endomorphism of Finite Field in z of size 7^6
              Defn: z |--> 5*z^4 + 5*z^3 + 4*z^2 + 3*z + 1,
             Ring endomorphism of Finite Field in z of size 7^6
              Defn: z |--> 3*z^5 + 5*z^4 + 5*z^2 + 2*z + 3]

        Between isomorphic fields with different moduli::

            sage: k1 = GF(1009)
            sage: k2 = GF(1009, modulus='primitive')
            sage: Hom(k1, k2).list()
            [Ring morphism:
               From: Finite Field of size 1009
               To:   Finite Field of size 1009
               Defn: 1 |--> 1]
            sage: Hom(k2, k1).list()
            [Ring morphism:
               From: Finite Field of size 1009
               To:   Finite Field of size 1009
               Defn: 11 |--> 11]

            sage: k1.<a> = GF(1009^2, modulus='first_lexicographic')
            sage: k2.<b> = GF(1009^2, modulus='conway')
            sage: Hom(k1, k2).list()
            [Ring morphism:
               From: Finite Field in a of size 1009^2
               To:   Finite Field in b of size 1009^2
               Defn: a |--> 290*b + 864,
             Ring morphism:
               From: Finite Field in a of size 1009^2
               To:   Finite Field in b of size 1009^2
               Defn: a |--> 719*b + 145]

        TESTS:

        Check that :issue:`11390` is fixed::

            sage: K = GF(1<<16,'a'); L = GF(1<<32,'b')
            sage: K.Hom(L)[0]
            Ring morphism:
              From: Finite Field in a of size 2^16
              To:   Finite Field in b of size 2^32
              Defn: a |--> b^29 + b^27 + b^26 + b^23 + b^21 + b^19 + b^18 + b^16 + b^14 + b^13 + b^11 + b^10 + b^9 + b^8 + b^7 + b^6 + b^5 + b^2 + b
        """
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: H = Hom(GF(32, 'a'), GF(1024, 'b'))
            sage: H[1]
            Ring morphism:
              From: Finite Field in a of size 2^5
              To:   Finite Field in b of size 2^10
              Defn: a |--> b^7 + b^5
            sage: H[2:4]
            [Ring morphism:
               From: Finite Field in a of size 2^5
               To:   Finite Field in b of size 2^10
               Defn: a |--> b^8 + b^6 + b^2,
             Ring morphism:
               From: Finite Field in a of size 2^5
               To:   Finite Field in b of size 2^10
               Defn: a |--> b^9 + b^7 + b^6 + b^5 + b^4]
        """
    def index(self, item):
        """
        Return the index of ``self``.

        EXAMPLES::

            sage: K.<z> = GF(1024)
            sage: g = End(K)[3]
            sage: End(K).index(g) == 3
            True
        """
