from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.homset import RingHomset_generic as RingHomset_generic
from sage.rings.integer import Integer as Integer
from sage.rings.number_field.morphism import CyclotomicFieldHomomorphism_im_gens as CyclotomicFieldHomomorphism_im_gens, NumberFieldHomomorphism_im_gens as NumberFieldHomomorphism_im_gens, RelativeNumberFieldHomomorphism_from_abs as RelativeNumberFieldHomomorphism_from_abs
from sage.structure.sequence import Sequence as Sequence

class NumberFieldHomset(RingHomset_generic):
    """
    Set of homomorphisms with domain a given number field.

    TESTS::

        sage: H = Hom(QuadraticField(-1, 'a'), QuadraticField(-1, 'b'))
        sage: TestSuite(H).run()
    """
    Element = NumberFieldHomomorphism_im_gens
    def __init__(self, R, S, category=None) -> None:
        """
        TESTS:

        Check that :issue:`23647` is fixed::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^2 - 2, x^2 - 3])
            sage: e, u, v, w = End(K)
            sage: e.abs_hom().parent().category()
            Category of homsets of number fields
            sage: (v*v).abs_hom().parent().category()
            Category of homsets of number fields
        """
    def order(self):
        """
        Return the order of this set of field homomorphism.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: End(k)
            Automorphism group of Number Field in a with defining polynomial x^2 + 1
            sage: End(k).order()
            2
            sage: k.<a> = NumberField(x^3 + 2)
            sage: End(k).order()
            1

            sage: K.<a> = NumberField([x^3 + 2, x^2 + x + 1])
            sage: End(K).order()
            6
        """
    cardinality = order
    @cached_method
    def list(self):
        """
        Return a list of all the elements of ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 3*x + 1)
            sage: End(K).list()
            [Ring endomorphism of Number Field in a with defining polynomial x^3 - 3*x + 1
               Defn: a |--> a,
             Ring endomorphism of Number Field in a with defining polynomial x^3 - 3*x + 1
               Defn: a |--> a^2 - 2,
             Ring endomorphism of Number Field in a with defining polynomial x^3 - 3*x + 1
               Defn: a |--> -a^2 - a + 2]
            sage: Hom(K, CyclotomicField(9))[0] # indirect doctest
            Ring morphism:
              From: Number Field in a with defining polynomial x^3 - 3*x + 1
              To:   Cyclotomic Field of order 9 and degree 6
              Defn: a |--> -zeta9^4 + zeta9^2 - zeta9

        An example where the codomain is a relative extension::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: L.<b> = K.extension(x^2 + 3)
            sage: Hom(K, L).list()
            [Ring morphism:
               From: Number Field in a with defining polynomial x^3 - 2
               To:   Number Field in b with defining polynomial x^2 + 3 over its base field
               Defn: a |--> a,
             Ring morphism:
               From: Number Field in a with defining polynomial x^3 - 2
               To:   Number Field in b with defining polynomial x^2 + 3 over its base field
               Defn: a |--> -1/2*a*b - 1/2*a,
             Ring morphism:
               From: Number Field in a with defining polynomial x^3 - 2
               To:   Number Field in b with defining polynomial x^2 + 3 over its base field
               Defn: a |--> 1/2*a*b - 1/2*a]
        """
    def __getitem__(self, n):
        """
        Return the `n`-th element of ``self.list()``.

        EXAMPLES::

            sage: End(CyclotomicField(37))[3] # indirect doctest
            Ring endomorphism of Cyclotomic Field of order 37 and degree 36
              Defn: zeta37 |--> zeta37^4
        """

class RelativeNumberFieldHomset(NumberFieldHomset):
    """
    Set of homomorphisms with domain a given relative number field.

    EXAMPLES:

    We construct a homomorphism from a relative field by giving
    the image of a generator::

        sage: x = polygen(ZZ, 'x')
        sage: L.<cuberoot2, zeta3> = CyclotomicField(3).extension(x^3 - 2)
        sage: phi = L.hom([cuberoot2 * zeta3]); phi
        Relative number field endomorphism of
         Number Field in cuberoot2 with defining polynomial x^3 - 2 over its base field
          Defn: cuberoot2 |--> zeta3*cuberoot2
                zeta3 |--> zeta3
        sage: phi(cuberoot2 + zeta3)
        zeta3*cuberoot2 + zeta3

    In fact, this ``phi`` is a generator for the Kummer Galois group of this
    cyclic extension::

        sage: phi(phi(cuberoot2 + zeta3))
        (-zeta3 - 1)*cuberoot2 + zeta3
        sage: phi(phi(phi(cuberoot2 + zeta3)))
        cuberoot2 + zeta3
    """
    Element = RelativeNumberFieldHomomorphism_from_abs
    @cached_method
    def default_base_hom(self):
        """
        Pick an embedding of the base field of ``self`` into the codomain of this
        homset. This is done in an essentially arbitrary way.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a, b> = NumberField([x^3 - x + 1, x^2 + 23])
            sage: M.<c> = NumberField(x^4 + 80*x^2 + 36)
            sage: Hom(L, M).default_base_hom()
            Ring morphism:
              From: Number Field in b with defining polynomial x^2 + 23
              To:   Number Field in c with defining polynomial x^4 + 80*x^2 + 36
              Defn: b |--> 1/12*c^3 + 43/6*c

        TESTS:

        Check that :issue:`30518` is fixed::

            sage: K.<i> = QuadraticField(-1, embedding=QQbar.gen())
            sage: L.<a> = K.extension(x^2 - 6*x - 4)
            sage: a0, a1 = a.galois_conjugates(QQbar)
            sage: f0 = hom(L, QQbar, a0)
            sage: assert f0(i) == QQbar.gen()
            sage: f1 = hom(L, QQbar, a1)
            sage: assert f1(i) == QQbar.gen()

            sage: K.<i> = QuadraticField(-1, embedding=-QQbar.gen())
            sage: L.<a> = K.extension(x^2 - 6*x - 4)
            sage: a0, a1 = a.galois_conjugates(QQbar)
            sage: f0 = hom(L, QQbar, a0)
            sage: assert f0(i) == -QQbar.gen()
            sage: f1 = hom(L, QQbar, a1)
            sage: assert f1(i) == -QQbar.gen()
        """
    @cached_method
    def list(self):
        """
        Return a list of all the elements of ``self`` (for which the domain
        is a relative number field).

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^2 + x + 1, x^3 + 2])
            sage: End(K).list()
            [Relative number field endomorphism of Number Field in a with defining polynomial x^2 + x + 1 over its base field
               Defn: a |--> a
                     b |--> b,
             ...
             Relative number field endomorphism of Number Field in a with defining polynomial x^2 + x + 1 over its base field
               Defn: a |--> a
                     b |--> -b*a - b]

        An example with an absolute codomain::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^2 - 3, x^2 + 2])
            sage: Hom(K, CyclotomicField(24, 'z')).list()
            [Relative number field morphism:
               From: Number Field in a with defining polynomial x^2 - 3 over its base field
               To:   Cyclotomic Field of order 24 and degree 8
               Defn: a |--> z^6 - 2*z^2
                     b |--> -z^5 - z^3 + z,
             ...
             Relative number field morphism:
               From: Number Field in a with defining polynomial x^2 - 3 over its base field
               To:   Cyclotomic Field of order 24 and degree 8
               Defn: a |--> -z^6 + 2*z^2
                     b |--> z^5 + z^3 - z]
        """

class CyclotomicFieldHomset(NumberFieldHomset):
    """
    Set of homomorphisms with domain a given cyclotomic field.

    EXAMPLES::

        sage: End(CyclotomicField(16))
        Automorphism group of Cyclotomic Field of order 16 and degree 8
    """
    Element = CyclotomicFieldHomomorphism_im_gens
    @cached_method
    def list(self):
        """
        Return a list of all the elements of ``self`` (for which the domain
        is a cyclotomic field).

        EXAMPLES::

            sage: K.<z> = CyclotomicField(12)
            sage: G = End(K); G
            Automorphism group of Cyclotomic Field of order 12 and degree 4
            sage: [g(z) for g in G]
            [z, z^3 - z, -z, -z^3 + z]
            sage: x = polygen(ZZ, 'x')
            sage: L.<a, b> = NumberField([x^2 + x + 1, x^4 + 1])
            sage: L
            Number Field in a with defining polynomial x^2 + x + 1 over its base field
            sage: Hom(CyclotomicField(12), L)[3]
            Ring morphism:
              From: Cyclotomic Field of order 12 and degree 4
              To:   Number Field in a with defining polynomial x^2 + x + 1 over its base field
              Defn: zeta12 |--> -b^2*a
            sage: list(Hom(CyclotomicField(5), K))
            []
            sage: Hom(CyclotomicField(11), L).list()
            []
        """
