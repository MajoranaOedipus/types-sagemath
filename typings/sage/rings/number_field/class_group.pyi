from sage.groups.abelian_gps.abelian_group_element import AbelianGroupElement as AbelianGroupElement
from sage.groups.abelian_gps.values import AbelianGroupWithValuesElement as AbelianGroupWithValuesElement, AbelianGroupWithValues_class as AbelianGroupWithValues_class
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import MonoidElement as MonoidElement

class FractionalIdealClass(AbelianGroupWithValuesElement):
    """
    A fractional ideal class in a number field.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: G = NumberField(x^2 + 23,'a').class_group(); G
        Class group of order 3 with structure C3 of
         Number Field in a with defining polynomial x^2 + 23
        sage: I = G.0; I
        Fractional ideal class (2, 1/2*a - 1/2)
        sage: I.ideal()
        Fractional ideal (2, 1/2*a - 1/2)

        sage: K.<w> = QuadraticField(-23)
        sage: OK = K.ring_of_integers()
        sage: C = OK.class_group()
        sage: P2a, P2b = [P for P, e in (2*K).factor()]
        sage: c = C(P2a); c
        Fractional ideal class (2, 1/2*w - 1/2)
        sage: c.gens()
        (2, 1/2*w - 1/2)
    """
    def __init__(self, parent, element, ideal=None) -> None:
        """
        Return the ideal class of this fractional ideal.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23,'a'); G = K.class_group()
            sage: G(K.ideal(13, a + 4))
            Fractional ideal class (13, 1/2*a + 17/2)
        """
    def __pow__(self, n):
        """
        Raise this element to the power n.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 3*x + 8)
            sage: C = K.class_group()
            sage: c = C(2, a)
            sage: c^2
            Fractional ideal class (4, a)
            sage: c^3
            Trivial principal fractional ideal class
            sage: c^1000
            Fractional ideal class (2, a)
            sage: (c^2)^2
            Fractional ideal class (2, a)
        """
    def inverse(self):
        """
        Return the multiplicative inverse of this ideal class.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 3*x + 8); G = K.class_group()
            sage: G(2, a).inverse()
            Fractional ideal class (2, a^2 + 2*a - 1)
            sage: ~G(2, a)
            Fractional ideal class (2, a^2 + 2*a - 1)
        """
    __invert__ = inverse
    def is_principal(self):
        """
        Return ``True`` iff this ideal class is the trivial (principal) class.

        EXAMPLES::

            sage: K.<w> = QuadraticField(-23)
            sage: OK = K.ring_of_integers()
            sage: C = OK.class_group()
            sage: P2a, P2b = [P for P, e in (2*K).factor()]
            sage: c = C(P2a)
            sage: c.is_principal()
            False
            sage: (c^2).is_principal()
            False
            sage: (c^3).is_principal()
            True
        """
    def reduce(self):
        """
        Return representative for this ideal class that has been
        reduced using PARI's :pari:`idealred`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 20072); G = k.class_group(); G
            Class group of order 76 with structure C38 x C2 of
             Number Field in a with defining polynomial x^2 + 20072
            sage: I = (G.0)^11; I
            Fractional ideal class (33, 1/2*a + 8)
            sage: J = G(I.ideal()^5); J
            Fractional ideal class (39135393, 1/2*a + 13654253)
            sage: J.reduce()
            Fractional ideal class (73, 1/2*a + 47)
            sage: J == I^5
            True
        """
    def ideal(self):
        """
        Return a representative ideal in this ideal class.

        EXAMPLES::

            sage: K.<w> = QuadraticField(-23)
            sage: OK = K.ring_of_integers()
            sage: C = OK.class_group()
            sage: P2a, P2b = [P for P, e in (2*K).factor()]
            sage: c = C(P2a); c
            Fractional ideal class (2, 1/2*w - 1/2)
            sage: c.ideal()
            Fractional ideal (2, 1/2*w - 1/2)
        """
    def representative_prime(self, norm_bound: int = 1000):
        """
        Return a prime ideal in this ideal class.

        INPUT:

        - ``norm_bound`` -- (positive integer) upper bound on the norm of
          primes tested

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 31)
            sage: K.class_number()
            3
            sage: Cl = K.class_group()
            sage: [c.representative_prime() for c in Cl]
            [Fractional ideal (3),
             Fractional ideal (2, 1/2*a + 1/2),
             Fractional ideal (2, 1/2*a - 1/2)]

            sage: K.<a> = NumberField(x^2 + 223)
            sage: K.class_number()
            7
            sage: Cl = K.class_group()
            sage: [c.representative_prime() for c in Cl]
            [Fractional ideal (3),
             Fractional ideal (2, 1/2*a + 1/2),
             Fractional ideal (17, 1/2*a + 7/2),
             Fractional ideal (7, 1/2*a - 1/2),
             Fractional ideal (7, 1/2*a + 1/2),
             Fractional ideal (17, 1/2*a + 27/2),
             Fractional ideal (2, 1/2*a - 1/2)]
        """
    def gens(self) -> tuple:
        """
        Return generators for a representative ideal in this
        (`S`-)ideal class.

        EXAMPLES::

            sage: K.<w> = QuadraticField(-23)
            sage: OK = K.ring_of_integers()
            sage: C = OK.class_group()
            sage: P2a, P2b = [P for P, e in (2*K).factor()]
            sage: c = C(P2a); c
            Fractional ideal class (2, 1/2*w - 1/2)
            sage: c.gens()
            (2, 1/2*w - 1/2)
        """

class SFractionalIdealClass(FractionalIdealClass):
    """
    An `S`-fractional ideal class in a number field for a tuple `S` of primes.

    EXAMPLES::

        sage: K.<a> = QuadraticField(-14)
        sage: I = K.ideal(2, a)
        sage: S = (I,)
        sage: CS = K.S_class_group(S)
        sage: J = K.ideal(7, a)
        sage: G = K.ideal(3, a + 1)
        sage: CS(I)
        Trivial S-ideal class
        sage: CS(J)
        Trivial S-ideal class
        sage: CS(G)
        Fractional S-ideal class (3, a + 1)

    ::

        sage: K.<a> = QuadraticField(-14)
        sage: I = K.ideal(2, a)
        sage: S = (I,)
        sage: CS = K.S_class_group(S)
        sage: J = K.ideal(7, a)
        sage: G = K.ideal(3, a + 1)
        sage: CS(I).ideal()
        Fractional ideal (2, a)
        sage: CS(J).ideal()
        Fractional ideal (7, a)
        sage: CS(G).ideal()
        Fractional ideal (3, a + 1)

    ::

        sage: K.<a> = QuadraticField(-14)
        sage: I = K.ideal(2, a)
        sage: S = (I,)
        sage: CS = K.S_class_group(S)
        sage: G = K.ideal(3, a + 1)
        sage: CS(G).inverse()
        Fractional S-ideal class (3, a + 2)

    TESTS::

        sage: K.<a> = QuadraticField(-14)
        sage: I = K.ideal(2,a)
        sage: S = (I,)
        sage: CS = K.S_class_group(S)
        sage: J = K.ideal(7,a)
        sage: G = K.ideal(3,a+1)
        sage: CS(I).order()
        1
        sage: CS(J).order()
        1
        sage: CS(G).order()
        2
    """

class ClassGroup(AbelianGroupWithValues_class):
    """
    The class group of a number field.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 23)
        sage: G = K.class_group(); G
        Class group of order 3 with structure C3 of
         Number Field in a with defining polynomial x^2 + 23
        sage: G.category()
        Category of finite enumerated commutative groups

    Note the distinction between abstract generators, their ideal, and
    exponents::

        sage: C = NumberField(x^2 + 120071, 'a').class_group(); C
        Class group of order 500 with structure C250 x C2
        of Number Field in a with defining polynomial x^2 + 120071
        sage: c = C.gen(0)
        sage: c  # random
        Fractional ideal class (5, 1/2*a + 3/2)
        sage: c.ideal()  # random
        Fractional ideal (5, 1/2*a + 3/2)
        sage: c.ideal() is c.value()   # alias
        True
        sage: c.exponents()
        (1, 0)
    """
    Element = FractionalIdealClass
    def __init__(self, gens_orders, names, number_field, gens, proof: bool = True) -> None:
        """
        Create a class group.

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: G = K.class_group()
            sage: TestSuite(G).run()
        """
    def gens_ideals(self):
        """
        Return generating ideals for the (`S`-)class group.

        This is an alias for :meth:`gens_values`.

        OUTPUT: a tuple of ideals, one for each abstract Abelian group generator

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 + 23)
            sage: K.class_group().gens_ideals()   # random gens (platform dependent)
            (Fractional ideal (2, 1/4*a^3 - 1/4*a^2 + 1/4*a - 1/4),)

            sage: C = NumberField(x^2 + x + 23899, 'a').class_group(); C
            Class group of order 68 with structure C34 x C2 of Number Field
            in a with defining polynomial x^2 + x + 23899
            sage: C.gens()
            (Fractional ideal class (83, a + 21), Fractional ideal class (15, a + 8))
            sage: C.gens_ideals()
            (Fractional ideal (83, a + 21), Fractional ideal (15, a + 8))
        """
    def __iter__(self):
        """
        Return an iterator of all ideal classes in this class group.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 + 23)
            sage: G = K.class_group()
            sage: G
            Class group of order 3 with structure C3 of Number Field
            in a with defining polynomial x^4 + 23
            sage: list(G)
            [Trivial principal fractional ideal class,
             Fractional ideal class (2, 1/4*a^3 - 1/4*a^2 + 1/4*a - 1/4),
             Fractional ideal class (2, 1/2*a^2 + 1/2)]
            sage: G.list()
            (Trivial principal fractional ideal class,
             Fractional ideal class (2, 1/4*a^3 - 1/4*a^2 + 1/4*a - 1/4),
             Fractional ideal class (2, 1/2*a^2 + 1/2))

        TESTS::

            sage: K.<a> = NumberField(x^2 + 1)
            sage: G = K.class_group()
            sage: G
            Class group of order 1 of Number Field in a with defining polynomial x^2 + 1
            sage: list(G)
            [Trivial principal fractional ideal class]
            sage: G.list()
            (Trivial principal fractional ideal class,)
        """
    def number_field(self):
        """
        Return the number field that this (`S`-)class group is attached to.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: C = NumberField(x^2 + 23, 'w').class_group(); C
            Class group of order 3 with structure C3 of
             Number Field in w with defining polynomial x^2 + 23
            sage: C.number_field()
            Number Field in w with defining polynomial x^2 + 23

            sage: K.<a> = QuadraticField(-14)
            sage: CS = K.S_class_group(K.primes_above(2))
            sage: CS.number_field()
            Number Field in a with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
        """

class SClassGroup(ClassGroup):
    """
    The `S`-class group of a number field.

    EXAMPLES::

        sage: K.<a> = QuadraticField(-14)
        sage: S = K.primes_above(2)
        sage: K.S_class_group(S).gens()   # random gens (platform dependent)
        (Fractional S-ideal class (3, a + 2),)

        sage: K.<a> = QuadraticField(-974)
        sage: CS = K.S_class_group(K.primes_above(2)); CS
        S-class group of order 18 with structure C6 x C3 of
         Number Field in a with defining polynomial x^2 + 974 with a = 31.20897306865447?*I
        sage: CS.gen(0) # random
        Fractional S-ideal class (3, a + 2)
        sage: CS.gen(1) # random
        Fractional S-ideal class (31, a + 24)
    """
    Element = SFractionalIdealClass
    def __init__(self, gens_orders, names, number_field, gens, S, proof: bool = True) -> None:
        """
        Create an `S`-class group.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-14)
            sage: I = K.ideal(2,a)
            sage: S = (I,)
            sage: K.S_class_group(S)
            S-class group of order 2 with structure C2 of Number Field in a with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
            sage: K.<a> = QuadraticField(-105)
            sage: K.S_class_group([K.ideal(13, a + 8)])
            S-class group of order 4 with structure C2 x C2 of Number Field in a with defining polynomial x^2 + 105 with a = 10.24695076595960?*I
        """
    def S(self):
        """
        Return the set (or rather tuple) of primes used to define this class group.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-14)
            sage: I = K.ideal(2, a)
            sage: S = (I,)
            sage: CS = K.S_class_group(S);CS
            S-class group of order 2 with structure C2 of
             Number Field in a with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
            sage: T = tuple()
            sage: CT = K.S_class_group(T);CT
            S-class group of order 4 with structure C4 of
             Number Field in a with defining polynomial x^2 + 14 with a = 3.741657386773942?*I
            sage: CS.S()
            (Fractional ideal (2, a),)
            sage: CT.S()
            ()
        """
