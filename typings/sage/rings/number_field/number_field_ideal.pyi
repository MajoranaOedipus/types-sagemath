from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.misc.mrange import xmrange_iter as xmrange_iter
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.ideal import Ideal_fractional as Ideal_fractional, Ideal_generic as Ideal_generic
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.factorization import Factorization as Factorization
from sage.structure.proof.proof import get_flag as get_flag
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

SMALL_DISC: int
QQ: Incomplete
ZZ: Incomplete

class NumberFieldIdeal(Ideal_generic):
    '''
    An ideal of a number field.

    EXAMPLES::

        sage: x = polygen(ZZ)
        sage: K.<i> = NumberField(x^2 + 1)
        sage: K.ideal(7)
        Fractional ideal (7)

    Initialization from PARI::

        sage: K.ideal(pari(7))
        Fractional ideal (7)
        sage: K.ideal(pari(4), pari(4 + 2*i))
        Fractional ideal (2)
        sage: K.ideal(pari("i + 2"))
        Fractional ideal (i + 2)
        sage: K.ideal(pari("[3,0;0,3]"))
        Fractional ideal (3)
        sage: F = pari(K).idealprimedec(5)
        sage: K.ideal(F[0])
        Fractional ideal (-2*i - 1)

    TESTS:

    Check that ``_pari_prime`` is set when initializing from a PARI
    prime ideal::

        sage: K.ideal(pari(K).idealprimedec(5)[0])._pari_prime
        [5, [-2, 1]~, 1, 1, [2, -1; 1, 2]]

    Number fields defined by non-monic and non-integral
    polynomials are supported (:issue:`252`)::

        sage: K.<a> = NumberField(2*x^2 - 1/3)
        sage: I = K.ideal(a); I
        Fractional ideal (a)
        sage: I.norm()
        1/6
    '''
    quadratic_form: Incomplete
    def __init__(self, field, gens, coerce: bool = True) -> None:
        """
        INPUT:

        - ``field`` -- a number field

        - ``gens`` -- list of :class:`NumberFieldElement` objects belonging to
          the field

        TESTS:

        We test that pickling works::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 - 5)
            sage: I = K.ideal(2/(5+a))
            sage: I == loads(dumps(I))
            True
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: NumberField(x^2 + 1, 'a').ideal(7).__hash__()  # random
            7806919040325273549
        """
    def coordinates(self, x):
        """
        Return  the coordinate vector of `x` with respect to this ideal.

        INPUT:

        - ``x`` -- an element of the number field (or ring of integers) of this
          ideal

        OUTPUT:

        List giving the coordinates of `x` with respect to the integral basis
        of the ideal.  In general this will be a vector of
        rationals; it will consist of integers if and only if `x`
        is in the ideal.

        AUTHOR: John Cremona  2008-10-31

        ALGORITHM:

        Uses linear algebra.
        Provides simpler implementations for :meth:`_contains_`,
        :meth:`is_integral` and :meth:`smallest_integer`.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: I = K.ideal(7 + 3*i)
            sage: Ibasis = I.integral_basis(); Ibasis
            [58, i + 41]
            sage: a = 23 - 14*i
            sage: acoords = I.coordinates(a); acoords
            (597/58, -14)
            sage: sum([Ibasis[j]*acoords[j] for j in range(2)]) == a
            True
            sage: b = 123 + 456*i
            sage: bcoords = I.coordinates(b); bcoords
            (-18573/58, 456)
            sage: sum([Ibasis[j]*bcoords[j] for j in range(2)]) == b
            True
            sage: J = K.ideal(0)
            sage: J.coordinates(0)
            ()
            sage: J.coordinates(1)
            Traceback (most recent call last):
            ...
            TypeError: vector is not in free module
        """
    def __pari__(self):
        """
        Return  PARI Hermite Normal Form representations of this
        ideal.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<w> = NumberField(x^2 + 23)
            sage: I = K.class_group().0.ideal(); I
            Fractional ideal (2, 1/2*w - 1/2)
            sage: I.__pari__()
            [2, 0; 0, 1]
        """
    def pari_hnf(self):
        """
        Return PARI's representation of this ideal in Hermite normal form.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^3 - 2)
            sage: I = K.ideal(2/(5+a))
            sage: I.pari_hnf()
            [2, 0, 50/127; 0, 2, 244/127; 0, 0, 2/127]
        """
    @cached_method
    def basis(self):
        """
        Return a basis for this ideal viewed as a `\\ZZ`-module.

        OUTPUT:

        An immutable sequence of elements of this ideal (note: their
        parent is the number field) forming a basis for this ideal.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(7)
            sage: I = K.factor(11)[0][0]
            sage: I.basis()           # warning -- choice of basis can be somewhat random
            [11, 11*z, 11*z^2, z^3 + 5*z^2 + 4*z + 10,
             z^4 + z^2 + z + 5, z^5 + z^4 + z^3 + 2*z^2 + 6*z + 5]

        An example of a non-integral ideal.::

            sage: J = 1/I
            sage: J          # warning -- choice of generators can be somewhat random
            Fractional ideal (2/11*z^5 + 2/11*z^4 + 3/11*z^3 + 2/11)
            sage: J.basis()           # warning -- choice of basis can be somewhat random
            [1, z, z^2, 1/11*z^3 + 7/11*z^2 + 6/11*z + 10/11,
             1/11*z^4 + 1/11*z^2 + 1/11*z + 7/11,
             1/11*z^5 + 1/11*z^4 + 1/11*z^3 + 2/11*z^2 + 8/11*z + 7/11]

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(2*x^2 - 1/3)
            sage: K.ideal(a).basis()
            [1, a]
        """
    @cached_method
    def free_module(self):
        """
        Return the free `\\ZZ`-module contained in the vector space
        associated to the ambient number field, that corresponds
        to this ideal.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(7)
            sage: I = K.factor(11)[0][0]; I
            Fractional ideal (-3*z^4 - 2*z^3 - 2*z^2 - 2)
            sage: A = I.free_module()
            sage: A              # warning -- choice of basis can be somewhat random
            Free module of degree 6 and rank 6 over Integer Ring
            User basis matrix:
            [11  0  0  0  0  0]
            [ 0 11  0  0  0  0]
            [ 0  0 11  0  0  0]
            [10  4  5  1  0  0]
            [ 5  1  1  0  1  0]
            [ 5  6  2  1  1  1]

        However, the actual `\\ZZ`-module is not at all random::

            sage: A.basis_matrix().change_ring(ZZ).echelon_form()
            [ 1  0  0  5  1  1]
            [ 0  1  0  1  1  7]
            [ 0  0  1  7  6 10]
            [ 0  0  0 11  0  0]
            [ 0  0  0  0 11  0]
            [ 0  0  0  0  0 11]

        The ideal doesn't have to be integral::

            sage: J = I^(-1)
            sage: B = J.free_module()
            sage: B.echelonized_basis_matrix()
            [ 1/11     0     0  7/11  1/11  1/11]
            [    0  1/11     0  1/11  1/11  5/11]
            [    0     0  1/11  5/11  4/11 10/11]
            [    0     0     0     1     0     0]
            [    0     0     0     0     1     0]
            [    0     0     0     0     0     1]

        This also works for relative extensions::

            sage: x = polygen(ZZ)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 2])
            sage: I = K.fractional_ideal(4)
            sage: I.free_module()
            Free module of degree 4 and rank 4 over Integer Ring
            User basis matrix:
            [ 4  0  0  0]
            [ 3  7  1  1]
            [ 0 10  0  2]
            [ 3 -7  1 -1]
            sage: J = I^(-1); J.free_module()
            Free module of degree 4 and rank 4 over Integer Ring
            User basis matrix:
            [  1/4     0     0     0]
            [ 3/16  7/16  1/16  1/16]
            [    0   5/8     0   1/8]
            [ 3/16 -7/16  1/16 -1/16]

        An example of intersecting ideals by intersecting free modules.::

            sage: K.<a> = NumberField(x^3 + x^2 - 2*x + 8)
            sage: I = K.factor(2)
            sage: p1 = I[0][0]; p2 = I[1][0]
            sage: N = p1.free_module().intersection(p2.free_module()); N
            Free module of degree 3 and rank 3 over Integer Ring
            Echelon basis matrix:
            [  1 1/2 1/2]
            [  0   1   1]
            [  0   0   2]
            sage: N.index_in(p1.free_module()).abs()
            2

        TESTS:

        Sage can find the free module associated to quite large ideals
        quickly (see :issue:`4627`)::

            sage: y = polygen(ZZ)
            sage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)
            sage: M.ideal(prod(prime_range(6000, 6200))).free_module()
            Free module of degree 20 and rank 20 over Integer Ring
            User basis matrix:
            20 x 20 dense matrix over Rational Field
        """
    def reduce_equiv(self):
        """
        Return a small ideal that is equivalent to ``self`` in the group
        of fractional ideals modulo principal ideals.  Very often (but
        not always) if ``self`` is principal then this function returns
        the unit ideal.

        ALGORITHM: Calls :pari:`idealred` function.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<w> = NumberField(x^2 + 23)
            sage: I = ideal(w*23^5); I
            Fractional ideal (6436343*w)
            sage: I.reduce_equiv()
            Fractional ideal (1)
            sage: I = K.class_group().0.ideal()^10; I
            Fractional ideal (1024, 1/2*w + 979/2)
            sage: I.reduce_equiv()
            Fractional ideal (2, 1/2*w - 1/2)
        """
    def gens_reduced(self, proof=None):
        """
        Express this ideal in terms of at most two generators, and one
        if possible.

        This function indirectly uses :pari:`bnfisprincipal`, so set
        ``proof=True`` if you want to prove correctness (which *is* the
        default).

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^2 + 5)
            sage: K.ideal(0).gens_reduced()
            (0,)
            sage: J = K.ideal([a + 2, 9])
            sage: J.gens()
            (a + 2, 9)
            sage: J.gens_reduced()  # random sign
            (a + 2,)
            sage: K.ideal([a + 2, 3]).gens_reduced()
            (3, a + 2)

        TESTS::

            sage: len(J.gens_reduced()) == 1
            True

            sage: all(j.parent() is K for j in J.gens())
            True
            sage: all(j.parent() is K for j in J.gens_reduced())
            True

            sage: K.<a> = NumberField(x^4 + 10*x^2 + 20)
            sage: J = K.prime_above(5)
            sage: J.is_principal()
            False
            sage: J.gens_reduced()
            (5, -a)
            sage: all(j.parent() is K for j in J.gens())
            True
            sage: all(j.parent() is K for j in J.gens_reduced())
            True

        Make sure this works with large ideals (:issue:`11836`)::

            sage: R.<x> = QQ['x']
            sage: L.<b> = NumberField(x^10 - 10*x^8 - 20*x^7 + 165*x^6 - 12*x^5 - 760*x^3 + 2220*x^2 + 5280*x + 7744)
            sage: z_x = -96698852571685/2145672615243325696*b^9 + 2472249905907/195061146840302336*b^8 + 916693155514421/2145672615243325696*b^7 + 1348520950997779/2145672615243325696*b^6 - 82344497086595/12191321677518896*b^5 + 2627122040194919/536418153810831424*b^4 - 452199105143745/48765286710075584*b^3 + 4317002771457621/536418153810831424*b^2 + 2050725777454935/67052269226353928*b + 3711967683469209/3047830419379724
            sage: P = EllipticCurve(L, '57a1').lift_x(z_x) * 3                          # needs sage.schemes
            sage: ideal = L.fractional_ideal(P[0], P[1])                                # needs sage.schemes
            sage: ideal.is_principal(proof=False)                                       # needs sage.schemes
            True
            sage: len(ideal.gens_reduced(proof=False))                                  # needs sage.schemes
            1
        """
    def gens_two(self) -> tuple:
        """
        Express this ideal using exactly two generators, the first of
        which is a generator for the intersection of the ideal with `\\QQ`.

        ALGORITHM: uses PARI's :pari:`idealtwoelt` function, which runs in
        randomized polynomial time and is very fast in practice.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^2 + 5)
            sage: J = K.ideal([a + 2, 9])
            sage: J.gens()
            (a + 2, 9)
            sage: J.gens_two()
            (9, a + 2)
            sage: K.ideal([a + 5, a + 8]).gens_two()
            (3, a + 2)
            sage: K.ideal(0).gens_two()
            (0, 0)

        The second generator is zero if and only if the ideal is
        generated by a rational, in contrast to the PARI function
        :pari:`idealtwoelt`::

            sage: I = K.ideal(12)
            sage: pari(K).idealtwoelt(I)  # Note that second element is not zero
            [12, [0, 12]~]
            sage: I.gens_two()
            (12, 0)
        """
    def integral_basis(self):
        """
        Return a list of generators for this ideal as a `\\ZZ`-module.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: J = K.ideal(i + 1)
            sage: J.integral_basis()
            [2, i + 1]
        """
    def integral_split(self):
        """
        Return a tuple `(I, d)`, where `I` is an integral ideal, and `d` is the
        smallest positive integer such that this ideal is equal to `I/d`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^2 - 5)
            sage: I = K.ideal(2/(5+a))
            sage: I.is_integral()
            False
            sage: J, d = I.integral_split()
            sage: J
            Fractional ideal (-1/2*a + 5/2)
            sage: J.is_integral()
            True
            sage: d
            5
            sage: I == J/d
            True
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` and ``other``.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-11)
            sage: p = K.ideal((a + 1)/2); q = K.ideal((a + 3)/2)
            sage: p.intersection(q) == q.intersection(p) == K.ideal(a - 2)
            True

        An example with non-principal ideals::

            sage: x = polygen(ZZ)
            sage: L.<a> = NumberField(x^3 - 7)
            sage: p = L.ideal(a^2 + a + 1, 2)
            sage: q = L.ideal(a + 1)
            sage: p.intersection(q) == L.ideal(8, 2*a + 2)
            True

        A relative example::

            sage: L.<a,b> = NumberField([x^2 + 11, x^2 - 5])
            sage: A = L.ideal([15, (-3/2*b + 7/2)*a - 8])
            sage: B = L.ideal([6, (-1/2*b + 1)*a - b - 5/2])
            sage: A.intersection(B) == L.ideal(-1/2*a - 3/2*b - 1)
            True

        TESTS:

        Test that this works with non-integral ideals (:issue:`10767`)::

            sage: K = QuadraticField(-2)
            sage: I = K.ideal(1/2)
            sage: I.intersection(I)
            Fractional ideal (1/2)
        """
    def is_integral(self):
        """
        Return ``True`` if this ideal is integral.

        EXAMPLES::

           sage: R.<x> = PolynomialRing(QQ)
           sage: K.<a> = NumberField(x^5 - x + 1)
           sage: K.ideal(a).is_integral()
           True
           sage: (K.ideal(1) / (3*a+1)).is_integral()
           False
        """
    def is_maximal(self):
        """
        Return ``True`` if this ideal is maximal.  This is equivalent to
        ``self`` being prime and nonzero.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 3); K
            Number Field in a with defining polynomial x^3 + 3
            sage: K.ideal(5).is_maximal()
            False
            sage: K.ideal(7).is_maximal()
            True
        """
    def is_prime(self):
        """
        Return ``True`` if this ideal is prime.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 - 17); K
            Number Field in a with defining polynomial x^2 - 17
            sage: K.ideal(5).is_prime()   # inert prime
            True
            sage: K.ideal(13).is_prime()  # split
            False
            sage: K.ideal(17).is_prime()  # ramified
            False

        TESTS:

        Check that we do not factor the norm of the ideal, this used
        to take half an hour, see :issue:`33360`::

            sage: K.<a,b,c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])
            sage: t = (((-2611940*c + 1925290/7653)*b - 1537130/7653*c
            ....:       + 10130950)*a + (1343014/7653*c - 8349770)*b
            ....:       + 6477058*c - 2801449990/4002519)
            sage: t.is_prime()
            False
        """
    def pari_prime(self):
        '''
        Return a PARI prime ideal corresponding to the ideal ``self``.

        INPUT:

        - ``self`` -- a prime ideal

        OUTPUT: a PARI "prime ideal", i.e. a five-component vector `[p,a,e,f,b]`
        representing the prime ideal `p O_K + a O_K`, `e`, `f` as usual, `a` as
        vector of components on the integral basis, `b` Lenstra\'s constant.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: K.ideal(3).pari_prime()
            [3, [3, 0]~, 1, 2, 1]
            sage: K.ideal(2+i).pari_prime()
            [5, [2, 1]~, 1, 1, [-2, -1; 1, -2]]
            sage: K.ideal(2).pari_prime()
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (2) is not a prime ideal
        '''
    def is_principal(self, proof=None):
        """
        Return ``True`` if this ideal is principal.

        Since it uses the PARI method :pari:`bnfisprincipal`, specify
        ``proof=True`` (this is the default setting) to prove the correctness
        of the output.

        EXAMPLES::

            sage: K = QuadraticField(-119,'a')
            sage: P = K.factor(2)[1][0]
            sage: P.is_principal()
            False
            sage: I = P^5
            sage: I.is_principal()
            True
            sage: I  # random
            Fractional ideal (-1/2*a + 3/2)
            sage: P = K.ideal([2]).factor()[1][0]
            sage: I = P^5
            sage: I.is_principal()
            True
        """
    def ideal_class_log(self, proof=None):
        """
        Return the output of PARI's :pari:`bnfisprincipal` for this ideal,
        i.e. a vector expressing the class of this ideal in terms of a
        set of generators for the class group.

        Since it uses the PARI method :pari:`bnfisprincipal`, specify
        ``proof=True`` (this is the default setting) to prove the correctness
        of the output.

        EXAMPLES:

        When the class number is 1, the result is always the empty list::

            sage: K.<a> = QuadraticField(-163)
            sage: J = K.primes_above(random_prime(10^6))[0]
            sage: J.ideal_class_log()
            []

        An example with class group of order 2.  The first ideal is
        not principal, the second one is::

            sage: K.<a> = QuadraticField(-5)
            sage: J = K.ideal(23).factor()[0][0]
            sage: J.ideal_class_log()
            [1]
            sage: (J^10).ideal_class_log()
            [0]

        An example with a more complicated class group::

            sage: x = polygen(ZZ)
            sage: K.<a, b> = NumberField([x^3 - x + 1, x^2 + 26])
            sage: K.class_group()
            Class group of order 18 with structure C6 x C3 of
             Number Field in a with defining polynomial x^3 - x + 1 over its base field
            sage: K.primes_above(7)[0].ideal_class_log() # random
            [1, 2]
        """
    def S_ideal_class_log(self, S):
        """
        S-class group version of :meth:`ideal_class_log`.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-14)
            sage: S = K.primes_above(2)
            sage: I = K.ideal(3, a + 1)
            sage: I.S_ideal_class_log(S)
            [1]
            sage: I.S_ideal_class_log([])
            [3]

        TESTS::

            sage: K.<a> = QuadraticField(-974)
            sage: S = K.primes_above(2)
            sage: G = K.S_class_group(S)
            sage: I0 = G.0.ideal(); I1 = G.1.ideal()
            sage: for p in prime_range(100):
            ....:     for P in K.primes_above(p):
            ....:         v = P.S_ideal_class_log(S)
            ....:         assert(G(P) == G(I0^v[0] * I1^v[1]))
        """
    def is_zero(self):
        """
        Return ``True`` iff ``self`` is the zero ideal.

        Note that `(0)` is a :class:`NumberFieldIdeal`, not a
        :class:`NumberFieldFractionalIdeal`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 + 2); K
            Number Field in a with defining polynomial x^2 + 2
            sage: K.ideal(3).is_zero()
            False
            sage: I = K.ideal(0); I.is_zero()
            True
            sage: I
            Ideal (0) of Number Field in a with defining polynomial x^2 + 2
        """
    def norm(self):
        """
        Return the norm of this fractional ideal as a rational number.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^4 + 23); K
            Number Field in a with defining polynomial x^4 + 23
            sage: I = K.ideal(19); I
            Fractional ideal (19)
            sage: factor(I.norm())
            19^4
            sage: F = I.factor()
            sage: F[0][0].norm().factor()
            19^2
        """
    def absolute_norm(self):
        """
        A synonym for :meth:`norm`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.ideal(1 + 2*i).absolute_norm()
            5
        """
    def relative_norm(self):
        """
        A synonym for :meth:`norm`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.ideal(1 + 2*i).relative_norm()
            5
        """
    def absolute_ramification_index(self):
        """
        A synonym for :meth:`ramification_index`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.ideal(1 + i).absolute_ramification_index()
            2
        """
    def relative_ramification_index(self):
        """
        A synonym for :meth:`ramification_index`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: K.ideal(1 + i).relative_ramification_index()
            2
        """
    def number_field(self):
        """
        Return the number field that this is a fractional ideal in.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 + 2); K
            Number Field in a with defining polynomial x^2 + 2
            sage: K.ideal(3).number_field()
            Number Field in a with defining polynomial x^2 + 2
            sage: K.ideal(0).number_field()  # not tested (not implemented)
            Number Field in a with defining polynomial x^2 + 2
        """
    def smallest_integer(self):
        """
        Return the smallest nonnegative integer in `I \\cap \\ZZ`,
        where `I` is this ideal.  If `I = 0`, returns 0.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^2 + 6)
            sage: I = K.ideal([4, a])/7; I
            Fractional ideal (2/7, 1/7*a)
            sage: I.smallest_integer()
            2

        TESTS::

            sage: K.<i> = QuadraticField(-1)
            sage: P1, P2 = [P for P,e in K.factor(13)]
            sage: all((P1^i*P2^j).smallest_integer() == 13^max(i,j,0) for i in range(-3,3) for j in range(-3,3))
            True
            sage: I = K.ideal(0)
            sage: I.smallest_integer()
            0

        See :issue:`4392`::

            sage: K.<a>=QuadraticField(-5)
            sage: I=K.ideal(7)
            sage: I.smallest_integer()
            7

            sage: K.<z> = CyclotomicField(13)
            sage: a = K([-8, -4, -4, -6, 3, -4, 8, 0, 7, 4, 1, 2])
            sage: I = K.ideal(a)
            sage: I.smallest_integer()
            146196692151
            sage: I.norm()
            1315770229359
            sage: I.norm() / I.smallest_integer()
            9
        """
    def valuation(self, p):
        """
        Return the valuation of ``self`` at ``p``.

        INPUT:

        - ``p`` -- a prime ideal `\\mathfrak{p}` of this number field

        OUTPUT:

        (integer) The valuation of this fractional ideal at the prime
        `\\mathfrak{p}`.  If `\\mathfrak{p}` is not prime, raise a
        :exc:`ValueError`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^5 + 2); K
            Number Field in a with defining polynomial x^5 + 2
            sage: i = K.ideal(38); i
            Fractional ideal (38)
            sage: i.valuation(K.factor(19)[0][0])
            1
            sage: i.valuation(K.factor(2)[0][0])
            5
            sage: i.valuation(K.factor(3)[0][0])
            0
            sage: i.valuation(0)
            Traceback (most recent call last):
            ...
            ValueError: p (= Ideal (0) of Number Field in a
            with defining polynomial x^5 + 2) must be nonzero
            sage: K.ideal(0).valuation(K.factor(2)[0][0])
            +Infinity
        """
    def decomposition_group(self):
        """
        Return the decomposition group of ``self``, as a subset of the
        automorphism group of the number field of ``self``. Raises an
        error if the field isn't Galois. See the :meth:`GaloisGroup_v2.decomposition_group`
        method for further examples and doctests.

        EXAMPLES::

            sage: QuadraticField(-23, 'w').primes_above(7)[0].decomposition_group()     # needs sage.groups
            Subgroup generated by [(1,2)] of (Galois group 2T1 (S2) with order 2 of x^2 + 23)
        """
    def ramification_group(self, v):
        """
        Return the `v`-th ramification group of ``self``, i.e. the set of
        elements `s` of the Galois group of the number field of ``self``
        (which we assume is Galois) such that `s` acts trivially
        modulo the `(v+1)`'st power of ``self``. See the
        :meth:`GaloisGroup.ramification_group` method for
        further examples and doctests.

        EXAMPLES::

            sage: QuadraticField(-23, 'w').primes_above(23)[0].ramification_group(0)    # needs sage.groups
            Subgroup generated by [(1,2)] of (Galois group 2T1 (S2) with order 2 of x^2 + 23)
            sage: QuadraticField(-23, 'w').primes_above(23)[0].ramification_group(1)    # needs sage.groups
            Subgroup generated by [()] of (Galois group 2T1 (S2) with order 2 of x^2 + 23)
        """
    def inertia_group(self):
        """
        Return the inertia group of ``self``, i.e. the set of elements `s` of the
        Galois group of the number field of ``self`` (which we assume is Galois)
        such that `s` acts trivially modulo ``self``. This is the same as the 0th
        ramification group of ``self``. See the
        :meth:`GaloisGroup_v2.inertia_group` method further examples and doctests.

        EXAMPLES::

            sage: QuadraticField(-23, 'w').primes_above(23)[0].inertia_group()          # needs sage.groups
            Subgroup generated by [(1,2)] of (Galois group 2T1 (S2) with order 2 of x^2 + 23)
        """
    def random_element(self, *args, **kwds):
        """
        Return a random element of this ideal.

        INPUT:

        - ``*args``, ``*kwds`` -- parameters passed to the random integer
          function.  See the documentation of ``ZZ.random_element()`` for
          details.

        OUTPUT:

        A random element of this fractional ideal, computed as a random
        `\\ZZ`-linear combination of the basis.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 2)
            sage: I = K.ideal(1 - a)
            sage: I.random_element() # random output
            -a^2 - a - 19
            sage: I.random_element(distribution='uniform') # random output
            a^2 - 2*a - 8
            sage: I.random_element(-30, 30) # random output
            -7*a^2 - 17*a - 75
            sage: I.random_element(-100, 200).is_integral()
            True
            sage: I.random_element(-30, 30).parent() is K
            True

        A relative example::

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: I = K.ideal(1 - a)
            sage: I.random_element()  # random output
            17/500002*a^3 + 737253/250001*a^2 - 1494505893/500002*a + 752473260/250001
            sage: I.random_element().is_integral()
            True
            sage: I.random_element(-100, 200).parent() is K
            True
        """
    def artin_symbol(self):
        """
        Return the Artin symbol `(K / \\QQ, P)`, where `K` is the
        number field of `P` = ``self``.  This is the unique element `s` of
        the decomposition group of `P` such that `s(x) = x^p \\pmod{P}`
        where `p` is the residue characteristic of `P`.  (Here `P`
        (``self``) should be prime and unramified.)

        See the :meth:`GaloisGroup_v2.artin_symbol` method
        for further documentation and examples.

        EXAMPLES::

            sage: QuadraticField(-23, 'w').primes_above(7)[0].artin_symbol()            # needs sage.groups
            (1,2)
        """
    def residue_symbol(self, e, m, check: bool = True):
        """
        The `m`-th power residue symbol for an element `e` and the proper ideal.

        .. MATH:: \\left(\\frac{\\alpha}{\\mathbf{P}}\\right) \\equiv \\alpha^{\\frac{N(\\mathbf{P})-1}{m}} \\operatorname{mod} \\mathbf{P}

        .. NOTE:: accepts `m=1`, in which case returns 1

        .. NOTE:: can also be called for an element from sage.rings.number_field_element.residue_symbol

        .. NOTE:: `e` is coerced into the number field of ``self``

        .. NOTE::

            if `m=2`, `e` is an integer, and ``self.number_field()`` has absolute degree 1 (i.e. it is a copy of the rationals),
            then this calls :func:`kronecker_symbol`, which is implemented using GMP.

        INPUT:

        - ``e`` -- element of the number field

        - ``m`` -- positive integer

        OUTPUT: an `m`-th root of unity in the number field

        EXAMPLES:

        Quadratic Residue (7 is not a square modulo 11)::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x - 1)
            sage: K.ideal(11).residue_symbol(7,2)
            -1

        Cubic Residue::

            sage: K.<w> = NumberField(x^2 - x + 1)
            sage: K.ideal(17).residue_symbol(w^2 + 3, 3)
            -w

        The field must contain the `m`-th roots of unity::

            sage: K.<w> = NumberField(x^2 - x + 1)
            sage: K.ideal(17).residue_symbol(w^2 + 3, 5)
            Traceback (most recent call last):
            ...
            ValueError: The residue symbol to that power is not defined for the number field
        """

def basis_to_module(B, K):
    """
    Given a basis `B` of elements for a `\\ZZ`-submodule of a number
    field `K`, return the corresponding `\\ZZ`-submodule.

    EXAMPLES::

        sage: x = polygen(ZZ)
        sage: K.<w> = NumberField(x^4 + 1)
        sage: from sage.rings.number_field.number_field_ideal import basis_to_module
        sage: basis_to_module([K.0, K.0^2 + 3], K)
        Free module of degree 4 and rank 2 over Integer Ring
        User basis matrix:
        [0 1 0 0]
        [3 0 1 0]
    """
def is_NumberFieldIdeal(x):
    """
    Return ``True`` if `x` is an ideal of a number field.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field_ideal import is_NumberFieldIdeal
        sage: is_NumberFieldIdeal(2/3)
        doctest:warning...
        DeprecationWarning: The function is_NumberFieldIdeal is deprecated;
        use 'isinstance(..., NumberFieldIdeal)' instead.
        See https://github.com/sagemath/sage/issues/38124 for details.
        False
        sage: is_NumberFieldIdeal(ideal(5))
        False

        sage: x = polygen(ZZ)
        sage: k.<a> = NumberField(x^2 + 2)
        sage: I = k.ideal([a + 1]); I
        Fractional ideal (a + 1)
        sage: is_NumberFieldIdeal(I)
        True
        sage: Z = k.ideal(0); Z
        Ideal (0) of Number Field in a with defining polynomial x^2 + 2
        sage: is_NumberFieldIdeal(Z)
        True
    """

class NumberFieldFractionalIdeal(MultiplicativeGroupElement, NumberFieldIdeal, Ideal_fractional):
    """
    A fractional ideal in a number field.

    EXAMPLES::

        sage: x = polygen(ZZ)
        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(x^3 - 2)
        sage: I = K.ideal(2/(5+a))
        sage: J = I^2
        sage: Jinv = I^(-2)
        sage: J*Jinv
        Fractional ideal (1)

    TESTS:

    Number-field fractional ideals are fractional ideals (:issue:`32380`)::

        sage: from sage.rings.ideal import Ideal_fractional
        sage: isinstance(I, Ideal_fractional)
        True
    """
    def __init__(self, field, gens, coerce: bool = True) -> None:
        """
        INPUT:

        - ``field`` -- a number field
        - ``x`` -- list of NumberFieldElements of the field, not all zero

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: NumberField(x^2 + 1, 'a').ideal(7)
            Fractional ideal (7)
        """
    def divides(self, other):
        """
        Return ``True`` if this ideal divides ``other`` and ``False`` otherwise.

        EXAMPLES::

            sage: K.<a> = CyclotomicField(11); K
            Cyclotomic Field of order 11 and degree 10
            sage: I = K.factor(31)[0][0]; I
            Fractional ideal (31, a^5 + 10*a^4 - a^3 + a^2 + 9*a - 1)
            sage: I.divides(I)
            True
            sage: I.divides(31)
            True
            sage: I.divides(29)
            False
        """
    def factor(self):
        """
        Factorization of this ideal in terms of prime ideals.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^4 + 23); K
            Number Field in a with defining polynomial x^4 + 23
            sage: I = K.ideal(19); I
            Fractional ideal (19)
            sage: F = I.factor(); F
            (Fractional ideal (19, 1/2*a^2 + a - 17/2))
             * (Fractional ideal (19, 1/2*a^2 - a - 17/2))
            sage: type(F)
            <class 'sage.structure.factorization.Factorization'>
            sage: list(F)
            [(Fractional ideal (19, 1/2*a^2 + a - 17/2), 1),
             (Fractional ideal (19, 1/2*a^2 - a - 17/2), 1)]
            sage: F.prod()
            Fractional ideal (19)

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`);
        the representation depends on the PARI version::

            sage: F.<a> = NumberField(2*x^3 + x + 1)
            sage: fact = F.factor(2)
            sage: (fact[0][1], fact[1][1])
            (2, 1)
            sage: fact[0][0] == F.ideal(2*a^2 + 1)
            True
            sage: fact[1][0] == F.ideal(-2*a^2)
            True
            sage: [p[0].norm() for p in fact]
            [2, 2]
        """
    def prime_factors(self):
        """
        Return a list of the prime ideal factors of ``self``.

        OUTPUT:

        list of prime ideals (a new list is returned
        each time this function is called)

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<w> = NumberField(x^2 + 23)
            sage: I = ideal(w+1)
            sage: I.prime_factors()
            [Fractional ideal (2, 1/2*w - 1/2),
             Fractional ideal (2, 1/2*w + 1/2),
             Fractional ideal (3, 1/2*w + 1/2)]
        """
    support = prime_factors
    def __invert__(self):
        """
        Return the multiplicative inverse of ``self``.  Call with ``~self``.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^3 - 2)
            sage: I = K.ideal(2/(5+a))
            sage: ~I
            Fractional ideal (1/2*a + 5/2)
            sage: 1/I
            Fractional ideal (1/2*a + 5/2)
            sage: (1/I) * I
            Fractional ideal (1)
        """
    def is_maximal(self):
        """
        Return ``True`` if this ideal is maximal.  This is equivalent to
        ``self`` being prime, since it is nonzero.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 3); K
            Number Field in a with defining polynomial x^3 + 3
            sage: K.ideal(5).is_maximal()
            False
            sage: K.ideal(7).is_maximal()
            True
        """
    def is_trivial(self, proof=None):
        """
        Return ``True`` if this is a trivial ideal.

        EXAMPLES::

            sage: F.<a> = QuadraticField(-5)
            sage: I = F.ideal(3)
            sage: I.is_trivial()
            False
            sage: J = F.ideal(5)
            sage: J.is_trivial()
            False
            sage: (I + J).is_trivial()
            True
        """
    def ramification_index(self):
        """
        Return the ramification index of this fractional ideal,
        assuming it is prime.  Otherwise, raise a :exc:`ValueError`.

        The ramification index is the power of this prime appearing in
        the factorization of the prime in `\\ZZ` that this prime lies
        over.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 + 2); K
            Number Field in a with defining polynomial x^2 + 2
            sage: f = K.factor(2); f
            (Fractional ideal (a))^2
            sage: f[0][0].ramification_index()
            2
            sage: K.ideal(13).ramification_index()
            1
            sage: K.ideal(17).ramification_index()
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (17) is not a prime ideal
        """
    def reduce(self, f):
        """
        Return the canonical reduction of the element `f` modulo the ideal
        `I` (= ``self``). This is an element of `R` (the ring of integers of the
        number field) that is equivalent modulo `I` to `f`.

        An error is raised if this fractional ideal is not integral or
        the element `f` is not integral.

        INPUT:

        - ``f`` -- an integral element of the number field

        OUTPUT:

        An integral element `g`, such that `f - g` belongs to the ideal ``self``
        and such that `g` is a canonical reduced representative of the coset
        `f + I` (where `I` = ``self``) as described in the method :meth:`residues`,
        namely an integral element with coordinates `(r_0, \\dots,r_{n-1})`, where:

        - `r_i` is reduced modulo `d_i`
        - `d_i = b_i[i]`, with `\\{b_0, b_1, \\dots, b_n\\}` HNF basis
          of the ideal ``self``.

        .. NOTE::

           The reduced element `g` is not necessarily small. To get a
           small `g` use the method :meth:`small_residue`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^3 + 11)
            sage: I = k.ideal(5, a^2 - a + 1)
            sage: c = 4*a + 9
            sage: I.reduce(c)
            a^2 - 2*a
            sage: c - I.reduce(c) in I
            True

        The reduced element is in the list of canonical representatives
        returned by the ``residues`` method:

        ::

            sage: I.reduce(c) in list(I.residues())
            True

        The reduced element does not necessarily have smaller norm (use
        :meth:`small_residue` for that)

        ::

            sage: c.norm()
            25
            sage: (I.reduce(c)).norm()
            209
            sage: (I.small_residue(c)).norm()
            10

        Sometimes the canonical reduced representative of `1` won't be `1`
        (it depends on the choice of basis for the ring of integers):

        ::

            sage: k.<a> = NumberField(x^2 + 23)
            sage: I = k.ideal(3)
            sage: I.reduce(3*a + 1)
            -3/2*a - 1/2
            sage: k.ring_of_integers().basis()
            [1/2*a + 1/2, a]

        AUTHOR: Maite Aranes.
        """
    def residues(self):
        """
        Return a iterator through a complete list of residues modulo this integral ideal.

        An error is raised if this fractional ideal is not integral.

        OUTPUT:

        An iterator through a complete list of residues modulo the integral
        ideal ``self``. This list is the set of canonical reduced representatives
        given by all integral elements with coordinates `(r_0, \\dots,r_{n-1})`,
        where:

        - `r_i` is reduced modulo `d_i`

        - `d_i = b_i[i]`, with `\\{b_0, b_1, \\dots, b_n\\}` HNF basis
          of the ideal.

        AUTHOR: John Cremona (modified by Maite Aranes)

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: res = K.ideal(2).residues(); res
            xmrange_iter([[0, 1], [0, 1]], <function ...<lambda> at 0x...>)
            sage: list(res)
            [0, i, 1, i + 1]
            sage: list(K.ideal(2 + i).residues())
            [-2*i, -i, 0, i, 2*i]
            sage: list(K.ideal(i).residues())
            [0]
            sage: I = K.ideal(3 + 6*i)
            sage: reps = I.residues()
            sage: len(list(reps)) == I.norm()
            True
            sage: all(r == s or not (r-s) in I      # long time (6s on sage.math, 2011)
            ....:     for r in reps for s in reps)
            True

            sage: K.<a> = NumberField(x^3 - 10)
            sage: I = K.ideal(a - 1)
            sage: len(list(I.residues())) == I.norm()
            True

            sage: K.<z> = CyclotomicField(11)
            sage: len(list(K.primes_above(3)[0].residues())) == 3**5  # long time (5s on sage.math, 2011)
            True
        """
    def invertible_residues(self, reduce: bool = True):
        """
        Return an iterator through a list of invertible residues
        modulo this integral ideal.

        An error is raised if this fractional ideal is not integral.

        INPUT:

        - ``reduce`` -- boolean; if ``True`` (default), use ``small_residue`` to get
          small representatives of the residues

        OUTPUT:

        An iterator through a list of invertible residues modulo this ideal
        `I`, i.e. a list of elements in the ring of integers `R` representing
        the elements of `(R/I)^*`.

        ALGORITHM: Use :pari:`idealstar` to find the group structure and
        generators of the multiplicative group modulo the ideal.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: ires = K.ideal(2).invertible_residues(); ires
            xmrange_iter([[0, 1]], <function ...<lambda> at 0x...>)
            sage: list(ires)
            [1, -i]
            sage: list(K.ideal(2 + i).invertible_residues())
            [1, 2, 4, 3]
            sage: list(K.ideal(i).residues())
            [0]
            sage: list(K.ideal(i).invertible_residues())
            [1]
            sage: I = K.ideal(3 + 6*i)
            sage: units = I.invertible_residues()
            sage: len(list(units)) == I.euler_phi()
            True

            sage: K.<a> = NumberField(x^3 - 10)
            sage: I = K.ideal(a - 1)
            sage: len(list(I.invertible_residues())) == I.euler_phi()
            True

            sage: K.<z> = CyclotomicField(10)
            sage: len(list(K.primes_above(3)[0].invertible_residues()))
            80

        TESTS:

        Check that the integrality is not lost,  cf. :issue:`30801`::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: all(x.is_integral() for x in K.ideal(8).invertible_residues())
            True

        AUTHOR: John Cremona
        """
    def invertible_residues_mod(self, subgp_gens=[], reduce: bool = True):
        """
        Return a iterator through a list of representatives for the invertible
        residues modulo this integral ideal, modulo the subgroup generated by
        the elements in the list ``subgp_gens``.

        INPUT:

        - ``subgp_gens`` -- either ``None`` or a list of elements of the number
          field of ``self``. These need not be integral, but should be coprime to
          the ideal ``self``. If the list is empty or ``None``, the function returns
          an iterator through a list of representatives for the invertible
          residues modulo the integral ideal ``self``.

        - ``reduce`` -- boolean; if ``True`` (default), use ``small_residues`` to
          get small representatives of the residues

        .. NOTE::

            See also :meth:`invertible_residues` for a simpler version without the subgroup.

        OUTPUT:

        An iterator through a list of representatives for the invertible
        residues modulo ``self`` and modulo the group generated by
        ``subgp_gens``, i.e. a list of elements in the ring of integers `R`
        representing the elements of `(R/I)^*/U`, where `I` is this ideal and
        `U` is the subgroup of `(R/I)^*` generated by ``subgp_gens``.

        EXAMPLES:

        ::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^2 + 23)
            sage: I = k.ideal(a)
            sage: list(I.invertible_residues_mod([-1]))
            [1, 5, 2, 10, 4, 20, 8, 17, 16, 11, 9]
            sage: list(I.invertible_residues_mod([1/2]))
            [1, 5]
            sage: list(I.invertible_residues_mod([23]))
            Traceback (most recent call last):
            ...
            TypeError: the element must be invertible mod the ideal

        ::

            sage: K.<a> = NumberField(x^3 - 10)
            sage: I = K.ideal(a - 1)
            sage: len(list(I.invertible_residues_mod([]))) == I.euler_phi()
            True

            sage: I = K.ideal(1)
            sage: list(I.invertible_residues_mod([]))
            [1]

        ::

            sage: K.<z> = CyclotomicField(10)
            sage: len(list(K.primes_above(3)[0].invertible_residues_mod([])))
            80

        AUTHOR: Maite Aranes.
        """
    def denominator(self):
        """
        Return the denominator ideal of this fractional ideal. Each
        fractional ideal has a unique expression as `N/D` where `N`,
        `D` are coprime integral ideals; the denominator is `D`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: I = K.ideal((3+4*i)/5); I
            Fractional ideal (4/5*i + 3/5)
            sage: I.denominator()
            Fractional ideal (-2*i - 1)
            sage: I.numerator()
            Fractional ideal (2*i - 1)
            sage: I.numerator().is_integral() and I.denominator().is_integral()
            True
            sage: I.numerator() + I.denominator() == K.unit_ideal()
            True
            sage: I.numerator()/I.denominator() == I
            True
        """
    def numerator(self):
        """
        Return the numerator ideal of this fractional ideal.

        Each fractional ideal has a unique expression as `N/D` where `N`,
        `D` are coprime integral ideals.  The numerator is `N`.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: I = K.ideal((3+4*i)/5); I
            Fractional ideal (4/5*i + 3/5)
            sage: I.denominator()
            Fractional ideal (-2*i - 1)
            sage: I.numerator()
            Fractional ideal (2*i - 1)
            sage: I.numerator().is_integral() and I.denominator().is_integral()
            True
            sage: I.numerator() + I.denominator() == K.unit_ideal()
            True
            sage: I.numerator()/I.denominator() == I
            True
        """
    def is_coprime(self, other):
        """
        Return ``True`` if this ideal is coprime to ``other``, else ``False``.

        INPUT:

        - ``other`` -- another ideal of the same field, or generators
          of an ideal

        OUTPUT: ``True`` if ``self`` and ``other`` are coprime, else ``False``

        .. NOTE::

           This function works for fractional ideals as well as
           integral ideals.

        AUTHOR: John Cremona

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: I = K.ideal(2 + i)
            sage: J = K.ideal(2 - i)
            sage: I.is_coprime(J)
            True
            sage: (I^-1).is_coprime(J^3)
            True
            sage: I.is_coprime(5)
            False
            sage: I.is_coprime(6 + i)
            True

        See :issue:`4536`::

            sage: E.<a> = NumberField(x^5 + 7*x^4 + 18*x^2 + x - 3)
            sage: i,j,k = [u[0] for u in factor(3*E)]
            sage: (i/j).is_coprime(j/k)
            False
            sage: (j/k).is_coprime(j/k)
            False

            sage: F.<a, b> = NumberField([x^2 - 2, x^2 - 3])
            sage: F.ideal(3 - a*b).is_coprime(F.ideal(3))
            False
        """
    def idealcoprime(self, J):
        """
        Return `l` such that ``l*self`` is coprime to `J`.

        INPUT:

        - ``J`` -- another integral ideal of the same field as ``self``, which
          must also be integral

        OUTPUT: an element `l` such that ``l*self`` is coprime to the ideal `J`

        .. TODO::

            Extend the implementation to non-integral ideals.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^2 + 23)
            sage: A = k.ideal(a + 1)
            sage: B = k.ideal(3)
            sage: A.is_coprime(B)
            False
            sage: lam = A.idealcoprime(B)
            sage: lam  # representation depends, not tested
            -1/6*a + 1/6
            sage: (lam*A).is_coprime(B)
            True

        ALGORITHM: Uses Pari function :pari:`idealcoprime`.

        TESTS:

        Check the above doctests, where the representation
        depends on the PARI version::

            sage: k.<a> = NumberField(x^2 + 23)
            sage: A = k.ideal(a + 1)
            sage: B = k.ideal(3)
            sage: lam = A.idealcoprime(B)
            sage: lam in (-1/6*a + 1/6, 1/6*a - 1/6)
            True
        """
    def small_residue(self, f):
        """
        Given an element `f` of the ambient number field, return an
        element `g` such that `f - g` belongs to the ideal ``self`` (which
        must be integral), and `g` is small.

        .. NOTE::

            The reduced representative returned is not uniquely determined.

        ALGORITHM: Uses PARI function :pari:`nfeltreduce`.

        EXAMPLES:

        ::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^2 + 5)
            sage: I = k.ideal(a)
            sage: I.small_residue(14)
            4

        ::

            sage: K.<a> = NumberField(x^5 + 7*x^4 + 18*x^2 + x - 3)
            sage: I = K.ideal(5)
            sage: I.small_residue(a^2 -13)
            a^2 + 5*a - 3
        """
    def idealstar(self, flag: int = 1):
        """
        Return  the finite abelian group `(O_K/I)^*`, where `I` is the ideal ``self``
        of the number field `K`, and `O_K` is the ring of integers of `K`.

        INPUT:

        - ``flag`` -- integer (default: 1); when ``flag==2``, it also
          computes the generators of the group `(O_K/I)^*`, which
          takes more time. By default ``flag`` is 1 (no generators are
          computed). In both cases the special PARI structure ``bid``
          is computed as well.  If ``flag`` is 0 (deprecated) it computes
          only the group structure of `(O_K/I)^*` (with generators)
          and not the special ``bid`` structure.

        OUTPUT:

        The finite abelian group `(O_K/I)^*`.

        .. NOTE::

            Uses the PARI function :pari:`idealstar`. The PARI function outputs
            a special ``bid`` structure which is stored in the internal
            field ``_bid`` of the ideal (when ``flag`` = 1,2). The special structure
            ``bid`` is used in the PARI function :pari:`ideallog`
            to compute discrete logarithms.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^3 - 11)
            sage: A = k.ideal(5)
            sage: G = A.idealstar(); G
            Multiplicative Abelian group isomorphic to C24 x C4
            sage: G.gens()
            (f0, f1)

            sage: G = A.idealstar(2)
            sage: G.gens()
            (f0, f1)
            sage: G.gens_values()   # random output
            (2*a^2 - 1, 2*a^2 + 2*a - 2)
            sage: all(G.gen(i).value() in k for i in range(G.ngens()))
            True

        TESTS::

            sage: k.<a> = NumberField(x^2 + 1)
            sage: k.ideal(a+1).idealstar(2)
            Trivial Abelian group

        ALGORITHM: Uses Pari function :pari:`idealstar`
        """
    def ideallog(self, x, gens=None, check: bool = True):
        """
        Return  the discrete logarithm of `x` with respect to the generators
        given in the ``bid`` structure of the ideal ``self``, or with respect to
        the generators ``gens`` if these are given.

        INPUT:

        - ``x`` -- a nonzero element of the number field of ``self``,
          which must have valuation equal to 0 at all prime ideals in
          the support of the ideal ``self``
        - ``gens`` -- list of elements of the number field which generate `(R
          / I)^*`, where `R` is the ring of integers of the field and `I` is
          this ideal, or ``None``. If ``None``, use the generators calculated
          by :meth:`~idealstar`.
        - ``check`` -- if ``True``, do a consistency check on the results.
          Ignored if ``gens`` is ``None``.

        OUTPUT:

        a list of nonnegative integers `(x_i)` such that `x =
        \\prod_i g_i^{x_i}` in `(R/I)^*`, where `x_i` are the generators, and
        the list `(x_i)` is lexicographically minimal with respect to this
        requirement. If the `x_i` generate independent cyclic factors of
        order `d_i`, as is the case for the default generators calculated by
        :meth:`~idealstar`, this just means that `0 \\le x_i < d_i`.

        A :exc:`ValueError` will be raised if the elements specified in ``gens``
        do not in fact generate the unit group (even if the element `x` is in
        the subgroup they generate).

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^3 - 11)
            sage: A = k.ideal(5)
            sage: G = A.idealstar(2)
            sage: l = A.ideallog(a^2 + 3)
            sage: r = G(l).value()
            sage: (a^2 + 3) - r in A
            True
            sage: A.small_residue(r) # random
            a^2 - 2

        Examples with custom generators::

            sage: K.<a> = NumberField(x^2 - 7)
            sage: I = K.ideal(17)
            sage: I.ideallog(a + 7, [1 + a, 2])
            [10, 3]
            sage: I.ideallog(a + 7, [2, 1 + a])
            [0, 118]

            sage: L.<b> = NumberField(x^4 - x^3 - 7*x^2 + 3*x + 2)
            sage: J = L.ideal(-b^3 - b^2 - 2)
            sage: u = -14*b^3 + 21*b^2 + b - 1
            sage: v = 4*b^2 + 2*b - 1
            sage: J.ideallog(5 + 2*b, [u, v], check=True)
            [4, 13]

        A non-example::

            sage: I.ideallog(a + 7, [2])
            Traceback (most recent call last):
            ...
            ValueError: Given elements do not generate unit group --
            they generate a subgroup of index 36

        ALGORITHM: Uses PARI function :pari:`ideallog`, and (if ``gens`` is not
        ``None``) a Hermite normal form calculation to express the result in terms
        of the generators ``gens``.
        """
    def element_1_mod(self, other):
        """
        Return an element `r` in this ideal such that `1-r` is in ``other``.

        An error is raised if either ideal is not integral of if they
        are not coprime.

        INPUT:

        - ``other`` -- another ideal of the same field, or generators
          of an ideal

        OUTPUT: an element `r` of the ideal ``self`` such that `1-r` is in the
        ideal ``other``

        AUTHOR: Maite Aranes (modified to use PARI's :pari:`idealaddtoone` by Francis Clarke)

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 - 2)
            sage: A = K.ideal(a + 1); A; A.norm()
            Fractional ideal (a + 1)
            3
            sage: B = K.ideal(a^2 - 4*a + 2); B; B.norm()
            Fractional ideal (a^2 - 4*a + 2)
            68
            sage: r = A.element_1_mod(B); r
            -33
            sage: r in A
            True
            sage: 1 - r in B
            True

        TESTS::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: A = K.ideal(a+1)
            sage: B = K.ideal(a^2-4*a+1); B; B.norm()
            Fractional ideal (a^2 - 4*a + 1)
            99
            sage: A.element_1_mod(B)
            Traceback (most recent call last):
            ...
            TypeError: Fractional ideal (a + 1), Fractional ideal (a^2 - 4*a + 1) are not coprime ideals

            sage: B = K.ideal(1/a); B
            Fractional ideal (1/2*a^2)
            sage: A.element_1_mod(B)
            Traceback (most recent call last):
            ...
            TypeError: Fractional ideal (1/2*a^2) is not an integral ideal
        """
    def euler_phi(self):
        """
        Return the Euler `\\varphi`-function of this integral ideal.

        This is the order of the multiplicative group of the quotient
        modulo the ideal.

        An error is raised if the ideal is not integral.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<i> = NumberField(x^2 + 1)
            sage: I = K.ideal(2 + i)
            sage: [r for r in I.residues() if I.is_coprime(r)]
            [-2*i, -i, i, 2*i]
            sage: I.euler_phi()
            4
            sage: J = I^3
            sage: J.euler_phi()
            100
            sage: len([r for r in J.residues() if J.is_coprime(r)])
            100
            sage: J = K.ideal(3 - 2*i)
            sage: I.is_coprime(J)
            True
            sage: I.euler_phi()*J.euler_phi() == (I*J).euler_phi()
            True
            sage: L.<b> = K.extension(x^2 - 7)
            sage: L.ideal(3).euler_phi()
            64
        """
    def prime_to_S_part(self, S):
        """
        Return the part of this fractional ideal which is coprime to
        the prime ideals in the list `S`.

        .. NOTE::

           This function assumes that `S` is a list of prime ideals,
           but does not check this.  This function will fail if `S` is
           not a list of prime ideals.

        INPUT:

        - ``S`` -- list of prime ideals

        OUTPUT:

        A fractional ideal coprime to the primes in `S`, whose prime
        factorization is that of ``self`` with the primes in `S`
        removed.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 - 23)
            sage: I = K.ideal(24)
            sage: S = [K.ideal(-a + 5), K.ideal(5)]
            sage: I.prime_to_S_part(S)
            Fractional ideal (3)
            sage: J = K.ideal(15)
            sage: J.prime_to_S_part(S)
            Fractional ideal (3)

            sage: K.<a> = NumberField(x^5 - 23)
            sage: I = K.ideal(24)
            sage: S = [K.ideal(15161*a^4 + 28383*a^3 + 53135*a^2 + 99478*a + 186250),
            ....:      K.ideal(2*a^4 + 3*a^3 + 4*a^2 + 15*a + 11),
            ....:      K.ideal(101)]
            sage: I.prime_to_S_part(S)
            Fractional ideal (24)
        """
    def is_S_unit(self, S):
        """
        Return ``True`` if this fractional ideal is a unit with respect to the list of primes `S`.

        INPUT:

        - ``S`` -- list of prime ideals (not checked if they are
          indeed prime)

        .. NOTE::

           This function assumes that `S` is a list of prime ideals,
           but does not check this.  This function will fail if `S` is
           not a list of prime ideals.

        OUTPUT:

        ``True``, if the ideal is an `S`-unit: that is, if the valuations of
        the ideal at all primes not in `S` are zero. ``False``, otherwise.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 + 23)
            sage: I = K.ideal(2)
            sage: P = I.factor()[0][0]
            sage: I.is_S_unit([P])
            False
        """
    def is_S_integral(self, S):
        """
        Return ``True`` if this fractional ideal is integral with respect to the list of primes `S`.

        INPUT:

        - ``S`` -- list of prime ideals (not checked if they are indeed prime)

        .. NOTE::

           This function assumes that `S` is a list of prime ideals,
           but does not check this.  This function will fail if `S` is
           not a list of prime ideals.

        OUTPUT:

        ``True``, if the ideal is `S`-integral: that is, if the valuations
        of the ideal at all primes not in `S` are nonnegative. ``False``,
        otherwise.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^2 + 23)
            sage: I = K.ideal(1/2)
            sage: P = K.ideal(2, 1/2*a - 1/2)
            sage: I.is_S_integral([P])
            False

            sage: J = K.ideal(1/5)
            sage: J.is_S_integral([K.ideal(5)])
            True
        """
    def prime_to_idealM_part(self, M):
        """
        Version for integral ideals of the ``prime_to_m_part`` function over `\\ZZ`.
        Return the largest divisor of ``self`` that is coprime to the ideal `M`.

        INPUT:

        - ``M`` -- an integral ideal of the same field, or generators of an ideal

        OUTPUT: an ideal which is the largest divisor of ``self`` that is coprime to `M`

        AUTHOR: Maite Aranes

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: k.<a> = NumberField(x^2 + 23)
            sage: I = k.ideal(a + 1)
            sage: M = k.ideal(2, 1/2*a - 1/2)
            sage: J = I.prime_to_idealM_part(M); J
            Fractional ideal (12, 1/2*a + 13/2)
            sage: J.is_coprime(M)
            True

            sage: J = I.prime_to_idealM_part(2); J
            Fractional ideal (3, 1/2*a + 1/2)
            sage: J.is_coprime(M)
            True
        """
    def residue_field(self, names=None):
        """
        Return the residue class field of this fractional ideal, which
        must be prime.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 - 7)
            sage: P = K.ideal(29).factor()[0][0]
            sage: P.residue_field()
            Residue field in abar of Fractional ideal (2*a^2 + 3*a - 10)
            sage: P.residue_field('z')
            Residue field in z of Fractional ideal (2*a^2 + 3*a - 10)

        Another example::

            sage: K.<a> = NumberField(x^3 - 7)
            sage: P = K.ideal(389).factor()[0][0]; P
            Fractional ideal (389, a^2 - 44*a - 9)
            sage: P.residue_class_degree()
            2
            sage: P.residue_field()
            Residue field in abar of Fractional ideal (389, a^2 - 44*a - 9)
            sage: P.residue_field('z')
            Residue field in z of Fractional ideal (389, a^2 - 44*a - 9)
            sage: FF.<w> = P.residue_field()
            sage: FF
            Residue field in w of Fractional ideal (389, a^2 - 44*a - 9)
            sage: FF((a+1)^390)
            36
            sage: FF(a)
            w

        An example of reduction maps to the residue field: these are defined on
        the whole valuation ring, i.e. the subring of the number field
        consisting of elements with nonnegative valuation. This shows that the
        issue raised in :issue:`1951` has been fixed::

            sage: K.<i> = NumberField(x^2 + 1)
            sage: P1, P2 = [g[0] for g in K.factor(5)]; P1, P2
            (Fractional ideal (2*i - 1), Fractional ideal (-2*i - 1))
            sage: a = 1/(1+2*i)
            sage: F1, F2 = [g.residue_field() for g in [P1, P2]]; F1, F2
            (Residue field of Fractional ideal (2*i - 1),
             Residue field of Fractional ideal (-2*i - 1))
            sage: a.valuation(P1)
            0
            sage: F1(i/7)
            4
            sage: F1(a)
            3
            sage: a.valuation(P2)
            -1
            sage: F2(a)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot reduce field element -2/5*i + 1/5
            modulo Fractional ideal (-2*i - 1): it has negative valuation

        An example with a relative number field::

            sage: L.<a,b> = NumberField([x^2 + 1, x^2 - 5])
            sage: p = L.ideal((-1/2*b - 1/2)*a + 1/2*b - 1/2)
            sage: R = p.residue_field(); R
            Residue field in abar of Fractional ideal ((-1/2*b - 1/2)*a + 1/2*b - 1/2)
            sage: R.cardinality()
            9
            sage: R(17)
            2
            sage: R((a + b)/17)
            abar
            sage: R(1/b)
            2*abar

        We verify that :issue:`8721` is fixed::

            sage: L.<a, b> = NumberField([x^2 - 3, x^2 - 5])
            sage: L.ideal(a).residue_field()
            Residue field in abar of Fractional ideal (a)
        """
    def residue_class_degree(self):
        """
        Return the residue class degree of this fractional ideal,
        assuming it is prime. Otherwise, raise a :exc:`ValueError`.

        The residue class degree of a prime ideal `I` is the degree of
        the extension `O_K/I` of its prime subfield.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^5 + 2); K
            Number Field in a with defining polynomial x^5 + 2
            sage: f = K.factor(19); f
            (Fractional ideal (a^2 + a - 3))
             * (Fractional ideal (2*a^4 + a^2 - 2*a + 1))
             * (Fractional ideal (a^2 + a - 1))
            sage: [i.residue_class_degree() for i, _ in f]
            [2, 2, 1]
        """
    def ray_class_number(self):
        """
        Return the order of the ray class group modulo this ideal. This is a
        wrapper around PARI's :pari:`bnrclassno` function.

        EXAMPLES::

            sage: K.<z> = QuadraticField(-23)
            sage: p = K.primes_above(3)[0]
            sage: p.ray_class_number()
            3

            sage: x = polygen(K)
            sage: L.<w> = K.extension(x^3 - z)
            sage: I = L.ideal(5)
            sage: I.ray_class_number()
            5184
        """

def is_NumberFieldFractionalIdeal(x):
    """
    Return ``True`` if `x` is a fractional ideal of a number field.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field_ideal import is_NumberFieldFractionalIdeal
        sage: is_NumberFieldFractionalIdeal(2/3)
        doctest:warning...
        DeprecationWarning: The function is_NumberFieldFractionalIdeal is deprecated;
        use 'isinstance(..., NumberFieldFractionalIdeal)' instead.
        See https://github.com/sagemath/sage/issues/38124 for details.
        False
        sage: is_NumberFieldFractionalIdeal(ideal(5))
        False
        sage: x = polygen(ZZ)
        sage: k.<a> = NumberField(x^2 + 2)
        sage: I = k.ideal([a + 1]); I
        Fractional ideal (a + 1)
        sage: is_NumberFieldFractionalIdeal(I)
        True
        sage: Z = k.ideal(0); Z
        Ideal (0) of Number Field in a with defining polynomial x^2 + 2
        sage: is_NumberFieldFractionalIdeal(Z)
        False
    """

class QuotientMap:
    """
    Class to hold data needed by quotient maps from number field
    orders to residue fields.  These are only partial maps: the exact
    domain is the appropriate valuation ring.  For examples, see
    :meth:`~sage.rings.number_field.number_field_ideal.NumberFieldFractionalIdeal.residue_field`.
    """
    def __init__(self, K, M_OK_change, Q, I) -> None:
        """
        Initialize this QuotientMap.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 4)
            sage: f = K.ideal(1 + a^2/2).residue_field().reduction_map(); f # indirect doctest
            Partially defined reduction map:
              From: Number Field in a with defining polynomial x^3 + 4
              To:   Residue field of Fractional ideal (1/2*a^2 + 1)
            sage: f.__class__
            <class 'sage.rings.finite_rings.residue_field.ReductionMap'>
        """
    def __call__(self, x):
        """
        Apply this QuotientMap to an element of the number field.

        INPUT:

        - ``x`` -- an element of the field

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 4)
            sage: f = K.ideal(1 + a^2/2).residue_field().reduction_map()
            sage: f(a)
            2
        """

class LiftMap:
    """
    Class to hold data needed by lifting maps from residue fields to
    number field orders.
    """
    def __init__(self, OK, M_OK_map, Q, I) -> None:
        """
        Initialize this LiftMap.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 4)
            sage: I = K.ideal(1 + a^2/2)
            sage: f = I.residue_field().lift_map()
            sage: f.__class__
            <class 'sage.rings.finite_rings.residue_field.LiftingMap'>
        """
    def __call__(self, x):
        """
        Apply this LiftMap to an element of the residue field.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: K.<a> = NumberField(x^3 + 4)
            sage: R = K.ideal(1 + a^2/2).residue_field()
            sage: f = R.lift_map()
            sage: f(R(a/17))
            1

        A relative example, which used to fail but is fixed by :issue:`8721`::

            sage: L.<a, b> = NumberField([x^2 + 1, x^2 - 5])
            sage: p = L.ideal(2*a + 3)
            sage: V, to_V, from_V = p._p_quotient(13)
            sage: from_V(V.0)
            (-1/2*b + 7/2)*a - 1/2*b + 3/2
        """

def quotient_char_p(I, p):
    """
    Given an integral ideal `I` that contains a prime number `p`, compute
    a vector space `V = (O_K \\mod p) / (I \\mod p)`, along with a
    homomorphism `O_K \\to V` and a section `V \\to O_K`.

    EXAMPLES::

        sage: from sage.rings.number_field.number_field_ideal import quotient_char_p

        sage: x = polygen(ZZ)
        sage: K.<i> = NumberField(x^2 + 1); O = K.maximal_order(); I = K.fractional_ideal(15)
        sage: quotient_char_p(I, 5)[0]
        Vector space quotient V/W of dimension 2 over Finite Field of size 5 where
        V: Vector space of dimension 2 over Finite Field of size 5
        W: Vector space of degree 2 and dimension 0 over Finite Field of size 5
        Basis matrix:
        []
        sage: quotient_char_p(I, 3)[0]
        Vector space quotient V/W of dimension 2 over Finite Field of size 3 where
        V: Vector space of dimension 2 over Finite Field of size 3
        W: Vector space of degree 2 and dimension 0 over Finite Field of size 3
        Basis matrix:
        []

        sage: I = K.factor(13)[0][0]; I
        Fractional ideal (3*i + 2)
        sage: I.residue_class_degree()
        1
        sage: quotient_char_p(I, 13)[0]
        Vector space quotient V/W of dimension 1 over Finite Field of size 13 where
        V: Vector space of dimension 2 over Finite Field of size 13
        W: Vector space of degree 2 and dimension 1 over Finite Field of size 13
        Basis matrix:
        [1 8]
    """
