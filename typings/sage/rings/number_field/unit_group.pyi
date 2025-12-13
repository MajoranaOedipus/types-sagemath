from sage.groups.abelian_gps.values import AbelianGroupWithValues_class as AbelianGroupWithValues_class
from sage.libs.pari import pari as pari
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.proof.proof import get_flag as get_flag

class UnitGroup(AbelianGroupWithValues_class):
    """
    The unit group or an `S`-unit group of a number field.

    TESTS::

        sage: x = polygen(QQ)
        sage: K.<a> = NumberField(x^4 + 23)
        sage: UK = K.unit_group()
        sage: u = UK.an_element();  u
        u0*u1
        sage: u.value()
        -1/4*a^3 + 7/4*a^2 - 17/4*a + 19/4

        sage: x = polygen(QQ)
        sage: K.<a> = NumberField(x^4 + 23)
        sage: K.unit_group().gens_values() # random
        [-1, 1/4*a^3 - 7/4*a^2 + 17/4*a - 19/4]

        sage: x = polygen(QQ)
        sage: U = NumberField(x^2 + x + 23899, 'a').unit_group(); U
        Unit group with structure C2 of Number Field in a with defining polynomial x^2 + x + 23899
        sage: U.ngens()
        1

        sage: K.<z> = CyclotomicField(13)
        sage: UK = K.unit_group()
        sage: UK.ngens()
        6
        sage: UK.gen(5)
        u5
        sage: UK.gen(5).value()
        -z^7 - z

    An S-unit group::

        sage: SUK = UnitGroup(K,S=21); SUK
        S-unit group with structure C26 x Z x Z x Z x Z x Z x Z x Z x Z x Z x Z of
         Cyclotomic Field of order 13 and degree 12 with
         S = (Fractional ideal (3, z^3 - z - 1),
              Fractional ideal (3, z^3 + z^2 + z - 1),
              Fractional ideal (3, z^3 + z^2 - 1),
              Fractional ideal (3, z^3 - z^2 - z - 1),
              Fractional ideal (7))
        sage: SUK.rank()
        10
        sage: SUK.zeta_order()
        26
        sage: SUK.log(21*z)
        (25, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1)
    """
    def __init__(self, number_field, proof: bool = True, S=None) -> None:
        """
        Create a unit group of a number field.

        INPUT:

        - ``number_field`` -- a number field
        - ``proof`` -- boolean (default: ``True``); proof flag
        - ``S`` -- tuple of prime ideals, or an ideal, or a single
          ideal or element from which an ideal can be constructed, in
          which case the support is used.  If ``None``, the global unit
          group is constructed; otherwise, the `S`-unit group is
          constructed.

        The ``proof`` flag is passed to PARI via the :pari:`pari_bnf` function
        which computes the unit group.  See the documentation for the
        ``number_field`` module.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2-38)
            sage: UK = K.unit_group(); UK
            Unit group with structure C2 x Z of Number Field in a with defining polynomial x^2 - 38
            sage: UK.gens()
            (u0, u1)
            sage: UK.gens_values()
            [-1, -6*a + 37]

            sage: K.<a> = QuadraticField(-3)
            sage: UK = K.unit_group(); UK
            Unit group with structure C6 of Number Field in a with defining polynomial x^2 + 3 with a = 1.732050807568878?*I
            sage: UK.gens()
            (u,)
            sage: UK.gens_values()
            [-1/2*a + 1/2]

            sage: K.<z> = CyclotomicField(13)
            sage: UK = K.unit_group(); UK
            Unit group with structure C26 x Z x Z x Z x Z x Z of Cyclotomic Field of order 13 and degree 12
            sage: UK.gens()
            (u0, u1, u2, u3, u4, u5)
            sage: UK.gens_values() # random
            [-z^11, z^5 + z^3, z^6 + z^5, z^9 + z^7 + z^5, z^9 + z^5 + z^4 + 1, z^5 + z]
            sage: SUK = UnitGroup(K,S=2); SUK
            S-unit group with structure C26 x Z x Z x Z x Z x Z x Z of
             Cyclotomic Field of order 13 and degree 12 with S = (Fractional ideal (2),)

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`);
        the representation depends on the PARI version::

            sage: K.<a> = NumberField(7/9*x^3 + 7/3*x^2 - 56*x + 123)
            sage: K.unit_group()
            Unit group with structure C2 x Z x Z of
             Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
            sage: UnitGroup(K, S=tuple(K.primes_above(7)))
            S-unit group with structure C2 x Z x Z x Z of
             Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
             with S = (Fractional ideal (...),)
            sage: K.primes_above(7)[0] in (7/225*a^2 - 7/75*a - 42/25, 28/225*a^2 + 77/75*a - 133/25)
            True

        Conversion from unit group to a number field and back
        gives the right results (:issue:`25874`)::

            sage: # needs sage.libs.linbox
            sage: K = QuadraticField(-3).composite_fields(QuadraticField(2))[0]
            sage: U = K.unit_group()
            sage: tuple(U(K(u)) for u in U.gens()) == U.gens()
            True
            sage: US = K.S_unit_group(3)
            sage: tuple(US(K(u)) for u in US.gens()) == US.gens()
            True

        Bug :issue:`36386` (pari stack overflow while expanding units)::

            sage: d = 12936642
            sage: K = QuadraticField(d)
            sage: K.unit_group(proof=False)
            Unit group with structure C2 x Z of Number Field in a with defining polynomial x^2 - 12936642 with a = 3596.754370262167?
        """
    def rank(self):
        """
        Return the rank of the unit group.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(13)
            sage: UnitGroup(K).rank()
            5
            sage: SUK = UnitGroup(K, S=2); SUK.rank()
            6
        """
    def fundamental_units(self):
        """
        Return generators for the free part of the unit group, as a list.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^4 + 23)
            sage: U = UnitGroup(K)
            sage: U.fundamental_units()  # random
            [1/4*a^3 - 7/4*a^2 + 17/4*a - 19/4]
        """
    def roots_of_unity(self):
        """
        Return all the roots of unity in this unit group, primitive or not.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<b> = NumberField(x^2 + 1)
            sage: U = UnitGroup(K)
            sage: zs = U.roots_of_unity(); zs
            [b, -1, -b, 1]
            sage: [ z**U.zeta_order() for z in zs ]
            [1, 1, 1, 1]
        """
    def torsion_generator(self):
        """
        Return a generator for the torsion part of the unit group.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^4 - x^2 + 4)
            sage: U = UnitGroup(K)
            sage: U.torsion_generator()
            u0
            sage: U.torsion_generator().value() # random
            -1/4*a^3 - 1/4*a + 1/2
        """
    def zeta_order(self):
        """
        Return the order of the torsion part of the unit group.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^4 - x^2 + 4)
            sage: U = UnitGroup(K)
            sage: U.zeta_order()
            6
        """
    def zeta(self, n: int = 2, all: bool = False):
        """
        Return one, or a list of all, primitive `n`-th root of unity in this unit group.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<z> = NumberField(x^2 + 3)
            sage: U = UnitGroup(K)
            sage: U.zeta(1)
            1
            sage: U.zeta(2)
            -1
            sage: U.zeta(2, all=True)
            [-1]
            sage: U.zeta(3)
            -1/2*z - 1/2
            sage: U.zeta(3, all=True)
            [-1/2*z - 1/2, 1/2*z - 1/2]
            sage: U.zeta(4)
            Traceback (most recent call last):
            ...
            ValueError: n (=4) does not divide order of generator

            sage: r.<x> = QQ[]
            sage: K.<b> = NumberField(x^2 + 1)
            sage: U = UnitGroup(K)
            sage: U.zeta(4)
            b
            sage: U.zeta(4,all=True)
            [b, -b]
            sage: U.zeta(3)
            Traceback (most recent call last):
            ...
            ValueError: n (=3) does not divide order of generator
            sage: U.zeta(3, all=True)
            []
        """
    def number_field(self):
        """
        Return the number field associated with this unit group.

        EXAMPLES::

            sage: U = UnitGroup(QuadraticField(-23, 'w')); U
            Unit group with structure C2 of
             Number Field in w with defining polynomial x^2 + 23 with w = 4.795831523312720?*I
            sage: U.number_field()
            Number Field in w with defining polynomial x^2 + 23 with w = 4.795831523312720?*I
        """
    def primes(self):
        """
        Return the (possibly empty) list of primes associated with this S-unit group.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-23)
            sage: S = tuple(K.ideal(3).prime_factors()); S
            (Fractional ideal (3, 1/2*a - 1/2), Fractional ideal (3, 1/2*a + 1/2))
            sage: U = UnitGroup(K,S=tuple(S)); U
            S-unit group with structure C2 x Z x Z of
             Number Field in a with defining polynomial x^2 + 23 with a = 4.795831523312720?*I
             with S = (Fractional ideal (3, 1/2*a - 1/2), Fractional ideal (3, 1/2*a + 1/2))
            sage: U.primes() == S
            True
        """
    def log(self, u):
        """
        Return the exponents of the unit `u` with respect to group generators.

        INPUT:

        - ``u`` -- any object from which an element of the unit group's number
          field `K` may be constructed; an error is raised if an element of `K`
          cannot be constructed from `u`, or if the element constructed is not a
          unit

        OUTPUT: list of integers giving the exponents of `u` with
        respect to the unit group's basis

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<z> = CyclotomicField(13)
            sage: UK = UnitGroup(K)
            sage: [UK.log(u) for u in UK.gens()]
            [(1, 0, 0, 0, 0, 0),
             (0, 1, 0, 0, 0, 0),
             (0, 0, 1, 0, 0, 0),
             (0, 0, 0, 1, 0, 0),
             (0, 0, 0, 0, 1, 0),
             (0, 0, 0, 0, 0, 1)]
            sage: vec = [65,6,7,8,9,10]
            sage: unit = UK.exp(vec); unit  # random
            -253576*z^11 + 7003*z^10 - 395532*z^9 - 35275*z^8 - 500326*z^7 - 35275*z^6
             - 395532*z^5 + 7003*z^4 - 253576*z^3 - 59925*z - 59925
            sage: UK.log(unit)
            (13, 6, 7, 8, 9, 10)

        An S-unit example::

           sage: SUK = UnitGroup(K, S=2)
           sage: v = (3,1,4,1,5,9,2)
           sage: u = SUK.exp(v); u
           8732*z^11 - 15496*z^10 - 51840*z^9 - 68804*z^8 - 51840*z^7 - 15496*z^6
            + 8732*z^5 - 34216*z^3 - 64312*z^2 - 64312*z - 34216
           sage: SUK.log(u)
           (3, 1, 4, 1, 5, 9, 2)
           sage: SUK.log(u) == v
           True
        """
    def exp(self, exponents):
        """
        Return unit with given exponents with respect to group generators.

        INPUT:

        - ``u`` -- any object from which an element of the unit
          group's number field `K` may be constructed; an error is
          raised if an element of `K` cannot be constructed from `u`, or
          if the element constructed is not a unit.

        OUTPUT: list of integers giving the exponents of `u` with
        respect to the unit group's basis.

        EXAMPLES::

            sage: x = polygen(QQ)
            sage: K.<z> = CyclotomicField(13)
            sage: UK = UnitGroup(K)
            sage: [UK.log(u) for u in UK.gens()]
            [(1, 0, 0, 0, 0, 0),
             (0, 1, 0, 0, 0, 0),
             (0, 0, 1, 0, 0, 0),
             (0, 0, 0, 1, 0, 0),
             (0, 0, 0, 0, 1, 0),
             (0, 0, 0, 0, 0, 1)]
            sage: vec = [65,6,7,8,9,10]
            sage: unit = UK.exp(vec)
            sage: UK.log(unit)
            (13, 6, 7, 8, 9, 10)
            sage: u = UK.gens()[-1]
            sage: UK.exp(UK.log(u)) == u.value()
            True

        An S-unit example::

           sage: SUK = UnitGroup(K,S=2)
           sage: v = (3,1,4,1,5,9,2)
           sage: u = SUK.exp(v); u
           8732*z^11 - 15496*z^10 - 51840*z^9 - 68804*z^8 - 51840*z^7 - 15496*z^6
            + 8732*z^5 - 34216*z^3 - 64312*z^2 - 64312*z - 34216
           sage: SUK.log(u)
           (3, 1, 4, 1, 5, 9, 2)
           sage: SUK.log(u) == v
           True
        """
