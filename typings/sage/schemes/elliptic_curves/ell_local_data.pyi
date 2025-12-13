from .constructor import EllipticCurve as EllipticCurve
from .kodaira_symbol import KodairaSymbol as KodairaSymbol
from sage.misc.verbose import verbose as verbose
from sage.rings.ideal import Ideal_generic as Ideal_generic
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_base import NumberField as NumberField
from sage.rings.number_field.number_field_ideal import NumberFieldFractionalIdeal as NumberFieldFractionalIdeal
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class EllipticCurveLocalData(SageObject):
    '''
    The class for the local reduction data of an elliptic curve.

    Currently supported are elliptic curves defined over `\\QQ`, and
    elliptic curves defined over a number field, at an arbitrary prime
    or prime ideal.

    INPUT:

    - ``E`` -- an elliptic curve defined over a number field, or `\\QQ`

    - ``P`` -- a prime ideal of the field, or a prime integer if the field is `\\QQ`

    - ``proof`` -- boolean; if ``True``, only use provably correct
      methods (default: controlled by global proof module).  Note
      that the proof module is number_field, not elliptic_curves,
      since the functions that actually need the flag are in
      number fields.

    - ``algorithm`` -- string (default: ``\'pari\'``); ignored unless the
      base field is `\\QQ`.  If "pari", use the PARI C-library
      ``ellglobalred`` implementation of Tate\'s algorithm over
      `\\QQ`. If "generic", use the general number field
      implementation.

    .. NOTE::

        This function is not normally called directly by users, who
        may access the data via methods of the EllipticCurve
        classes.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
        sage: E = EllipticCurve(\'14a1\')
        sage: EllipticCurveLocalData(E,2)
        Local data at Principal ideal (2) of Integer Ring:
          Reduction type: bad non-split multiplicative
          Local minimal model: Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6
                               over Rational Field
          Minimal discriminant valuation: 6
          Conductor exponent: 1
          Kodaira Symbol: I6
          Tamagawa Number: 2
    '''
    def __init__(self, E, P, proof=None, algorithm: str = 'pari', globally: bool = False) -> None:
        '''
        Initialize the reduction data for the elliptic curve `E` at the prime `P`.

        INPUT:

        - ``E`` -- an elliptic curve defined over a number field, or `\\QQ`

        - ``P`` -- a prime ideal of the field, or a prime integer if the field is `\\QQ`

        - ``proof`` -- boolean; if ``True``, only use provably correct
          methods (default: controlled by global proof module).  Note
          that the proof module is number_field, not elliptic_curves,
          since the functions that actually need the flag are in
          number fields.

        - ``algorithm`` -- string (default: ``\'pari\'``); ignored unless the
          base field is `\\QQ`.  If "pari", use the PARI C-library
          ``ellglobalred`` implementation of Tate\'s algorithm over
          `\\QQ`. If "generic", use the general number field
          implementation.

        - ``globally`` -- boolean (default: ``False``); if ``True``, the algorithm
          uses the generators of principal ideals rather than an arbitrary
          uniformizer.

        .. NOTE::

            This function is not normally called directly by users, who
            may access the data via methods of the EllipticCurve
            classes.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve(\'14a1\')
            sage: EllipticCurveLocalData(E, 2)
            Local data at Principal ideal (2) of Integer Ring:
              Reduction type: bad non-split multiplicative
              Local minimal model: Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6
                                   over Rational Field
              Minimal discriminant valuation: 6
              Conductor exponent: 1
              Kodaira Symbol: I6
              Tamagawa Number: 2

        ::

            sage: EllipticCurveLocalData(E, 2, algorithm=\'generic\')
            Local data at Principal ideal (2) of Integer Ring:
              Reduction type: bad non-split multiplicative
              Local minimal model: Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6
                                   over Rational Field
              Minimal discriminant valuation: 6
              Conductor exponent: 1
              Kodaira Symbol: I6
              Tamagawa Number: 2

        ::

            sage: EllipticCurveLocalData(E, 2, algorithm=\'pari\')
            Local data at Principal ideal (2) of Integer Ring:
              Reduction type: bad non-split multiplicative
              Local minimal model: Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6
                                   over Rational Field
              Minimal discriminant valuation: 6
              Conductor exponent: 1
              Kodaira Symbol: I6
              Tamagawa Number: 2

        ::

            sage: EllipticCurveLocalData(E, 2, algorithm=\'unknown\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be one of \'pari\', \'generic\'

        ::

            sage: EllipticCurveLocalData(E, 3)
            Local data at Principal ideal (3) of Integer Ring:
              Reduction type: good
              Local minimal model: Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6
                                   over Rational Field
              Minimal discriminant valuation: 0
              Conductor exponent: 0
              Kodaira Symbol: I0
              Tamagawa Number: 1

        ::

            sage: EllipticCurveLocalData(E, 7)
            Local data at Principal ideal (7) of Integer Ring:
              Reduction type: bad split multiplicative
              Local minimal model: Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x - 6
                                   over Rational Field
              Minimal discriminant valuation: 3
              Conductor exponent: 1
              Kodaira Symbol: I3
              Tamagawa Number: 3
        '''
    def minimal_model(self, reduce: bool = True):
        '''
        Return the (local) minimal model from this local reduction data.

        INPUT:

        - ``reduce`` -- boolean (default: ``True``); if set to ``True`` and if
          the initial elliptic curve had globally integral
          coefficients, then the elliptic curve returned by Tate\'s
          algorithm will be "reduced" as specified in _reduce_model()
          for curves over number fields.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve([0,0,0,0,64]); E
            Elliptic Curve defined by y^2 = x^3 + 64 over Rational Field
            sage: data = EllipticCurveLocalData(E, 2)
            sage: data.minimal_model()
            Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field
            sage: data.minimal_model() == E.local_minimal_model(2)
            True

        To demonstrate the behaviour of the parameter ``reduce``::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, \'x\')
            sage: K.<a> = NumberField(x^3 + x + 1)
            sage: E = EllipticCurve(K, [0, 0, a, 0, 1])
            sage: E.local_data(K.ideal(a-1)).minimal_model()
            Elliptic Curve defined by y^2 + a*y = x^3 + 1
             over Number Field in a with defining polynomial x^3 + x + 1
            sage: E.local_data(K.ideal(a-1)).minimal_model(reduce=False)
            Elliptic Curve defined by y^2 + (a+2)*y = x^3 + 3*x^2 + 3*x + (-a+1)
             over Number Field in a with defining polynomial x^3 + x + 1

            sage: E = EllipticCurve([2, 1, 0, -2, -1])
            sage: E.local_data(ZZ.ideal(2), algorithm=\'generic\').minimal_model(reduce=False)
            Elliptic Curve defined by y^2 + 2*x*y + 2*y = x^3 + x^2 - 4*x - 2 over Rational Field
            sage: E.local_data(ZZ.ideal(2), algorithm=\'pari\').minimal_model(reduce=False)
            Traceback (most recent call last):
            ...
            ValueError: the argument reduce must not be False if algorithm=pari is used
            sage: E.local_data(ZZ.ideal(2), algorithm=\'generic\').minimal_model()
            Elliptic Curve defined by y^2 = x^3 - x^2 - 3*x + 2 over Rational Field
            sage: E.local_data(ZZ.ideal(2), algorithm=\'pari\').minimal_model()
            Elliptic Curve defined by y^2 = x^3 - x^2 - 3*x + 2 over Rational Field

        :issue:`14476`::

            sage: # needs sage.rings.number_field
            sage: t = QQ[\'t\'].0
            sage: K.<g> = NumberField(t^4 - t^3-3*t^2 - t +1)
            sage: E = EllipticCurve([-2*g^3 + 10/3*g^2 + 3*g - 2/3,
            ....:                    -11/9*g^3 + 34/9*g^2 - 7/3*g + 4/9,
            ....:                    -11/9*g^3 + 34/9*g^2 - 7/3*g + 4/9, 0, 0])
            sage: vv = K.fractional_ideal(g^2 - g - 2)
            sage: E.local_data(vv).minimal_model()
            Elliptic Curve defined by
             y^2 + (-2*g^3+10/3*g^2+3*g-2/3)*x*y + (-11/9*g^3+34/9*g^2-7/3*g+4/9)*y
              = x^3 + (-11/9*g^3+34/9*g^2-7/3*g+4/9)*x^2
             over Number Field in g with defining polynomial t^4 - t^3 - 3*t^2 - t + 1
        '''
    def prime(self):
        """
        Return the prime ideal associated with this local reduction data.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve([0,0,0,0,64]); E
            Elliptic Curve defined by y^2 = x^3 + 64 over Rational Field
            sage: data = EllipticCurveLocalData(E,2)
            sage: data.prime()
            Principal ideal (2) of Integer Ring
        """
    def conductor_valuation(self):
        """
        Return the valuation of the conductor from this local reduction data.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve([0,0,0,0,64]); E
            Elliptic Curve defined by y^2 = x^3 + 64 over Rational Field
            sage: data = EllipticCurveLocalData(E,2)
            sage: data.conductor_valuation()
            2
        """
    def discriminant_valuation(self):
        """
        Return the valuation of the minimal discriminant from this local reduction data.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve([0,0,0,0,64]); E
            Elliptic Curve defined by y^2 = x^3 + 64 over Rational Field
            sage: data = EllipticCurveLocalData(E,2)
            sage: data.discriminant_valuation()
            4
        """
    def kodaira_symbol(self):
        """
        Return the Kodaira symbol from this local reduction data.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve([0,0,0,0,64]); E
            Elliptic Curve defined by y^2 = x^3 + 64 over Rational Field
            sage: data = EllipticCurveLocalData(E,2)
            sage: data.kodaira_symbol()
            IV
        """
    def tamagawa_number(self):
        """
        Return the Tamagawa number from this local reduction data.

        This is the index `[E(K_v):E^0(K_v)]`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve([0,0,0,0,64]); E
            Elliptic Curve defined by y^2 = x^3 + 64 over Rational Field
            sage: data = EllipticCurveLocalData(E,2)
            sage: data.tamagawa_number()
            3
        """
    def tamagawa_exponent(self):
        """
        Return the Tamagawa index from this local reduction data.

        This is the exponent of `E(K_v)/E^0(K_v)`; in most cases it is
        the same as the Tamagawa index.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData
            sage: E = EllipticCurve('816a1')
            sage: data = EllipticCurveLocalData(E, 2)
            sage: data.kodaira_symbol()
            I2*
            sage: data.tamagawa_number()
            4
            sage: data.tamagawa_exponent()
            2

            sage: E = EllipticCurve('200c4')
            sage: data = EllipticCurveLocalData(E, 5)
            sage: data.kodaira_symbol()
            I4*
            sage: data.tamagawa_number()
            4
            sage: data.tamagawa_exponent()
            2
        """
    def bad_reduction_type(self):
        """
        Return the type of bad reduction of this reduction data.

        OUTPUT:

        integer or ``None``:

        - +1 for split multiplicative reduction
        - -1 for non-split multiplicative reduction
        - 0  for additive reduction
        - ``None`` for good reduction

        EXAMPLES::

            sage: E = EllipticCurve('14a1')
            sage: [(p,E.local_data(p).bad_reduction_type()) for p in prime_range(15)]
            [(2, -1), (3, None), (5, None), (7, 1), (11, None), (13, None)]

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p,E.local_data(p).bad_reduction_type()) for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), None), (Fractional ideal (2*a + 1), 0)]
        """
    def has_good_reduction(self) -> bool:
        """
        Return ``True`` if there is good reduction.

        EXAMPLES::

            sage: E = EllipticCurve('14a1')
            sage: [(p,E.local_data(p).has_good_reduction()) for p in prime_range(15)]
            [(2, False), (3, True), (5, True), (7, False), (11, True), (13, True)]

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p,E.local_data(p).has_good_reduction()) for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), True),
             (Fractional ideal (2*a + 1), False)]
        """
    def has_bad_reduction(self) -> bool:
        """
        Return ``True`` if there is bad reduction.

        EXAMPLES::

            sage: E = EllipticCurve('14a1')
            sage: [(p,E.local_data(p).has_bad_reduction()) for p in prime_range(15)]
            [(2, True), (3, False), (5, False), (7, True), (11, False), (13, False)]

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p,E.local_data(p).has_bad_reduction()) for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), False),
             (Fractional ideal (2*a + 1), True)]
        """
    def has_multiplicative_reduction(self) -> bool:
        """
        Return ``True`` if there is multiplicative reduction.

        .. NOTE::

            See also ``has_split_multiplicative_reduction()`` and
            ``has_nonsplit_multiplicative_reduction()``.

        EXAMPLES::

            sage: E = EllipticCurve('14a1')
            sage: [(p, E.local_data(p).has_multiplicative_reduction()) for p in prime_range(15)]
            [(2, True), (3, False), (5, False), (7, True), (11, False), (13, False)]

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p,E.local_data(p).has_multiplicative_reduction()) for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), False), (Fractional ideal (2*a + 1), False)]
        """
    def has_split_multiplicative_reduction(self) -> bool:
        """
        Return ``True`` if there is split multiplicative reduction.

        EXAMPLES::

            sage: E = EllipticCurve('14a1')
            sage: [(p, E.local_data(p).has_split_multiplicative_reduction())
            ....:  for p in prime_range(15)]
            [(2, False), (3, False), (5, False), (7, True), (11, False), (13, False)]

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p,E .local_data(p).has_split_multiplicative_reduction())
            ....:  for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), False),
             (Fractional ideal (2*a + 1), False)]
        """
    def has_nonsplit_multiplicative_reduction(self) -> bool:
        """
        Return ``True`` if there is non-split multiplicative reduction.

        EXAMPLES::

            sage: E = EllipticCurve('14a1')
            sage: [(p, E.local_data(p).has_nonsplit_multiplicative_reduction())
            ....:  for p in prime_range(15)]
            [(2, True), (3, False), (5, False), (7, False), (11, False), (13, False)]

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p, E.local_data(p).has_nonsplit_multiplicative_reduction())
            ....:  for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), False), (Fractional ideal (2*a + 1), False)]
        """
    def has_additive_reduction(self) -> bool:
        """
        Return ``True`` if there is additive reduction.

        EXAMPLES::

            sage: E = EllipticCurve('27a1')
            sage: [(p, E.local_data(p).has_additive_reduction()) for p in prime_range(15)]
            [(2, False), (3, True), (5, False), (7, False), (11, False), (13, False)]

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: P17a, P17b = [P for P,e in K.factor(17)]
            sage: E = EllipticCurve([0, 0, 0, 0, 2*a+1])
            sage: [(p, E.local_data(p).has_additive_reduction()) for p in [P17a,P17b]]
            [(Fractional ideal (4*a^2 - 2*a + 1), False),
             (Fractional ideal (2*a + 1), True)]
        """

def check_prime(K, P):
    """
    Function to check that `P` determines a prime of `K`, and return that ideal.

    INPUT:

    - ``K`` -- a number field (including `\\QQ`)

    - ``P`` -- an element of ``K`` or a (fractional) ideal of ``K``

    OUTPUT: if ``K`` is `\\QQ`: the prime integer equal to or which generates `P`

    - If ``K`` is not `\\QQ`: the prime ideal equal to or generated by `P`.

    .. NOTE::

        If `P` is not a prime and does not generate a prime, a :exc:`TypeError`
        is raised.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_local_data import check_prime
        sage: check_prime(QQ, 3)
        3
        sage: check_prime(QQ, QQ(3))
        3
        sage: check_prime(QQ, ZZ.ideal(31))
        31

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 5)
        sage: check_prime(K, a)
        Fractional ideal (a)
        sage: check_prime(K, a + 1)
        Fractional ideal (a + 1)
        sage: [check_prime(K, P) for P in K.primes_above(31)]
        [Fractional ideal (-5/2*a - 1/2), Fractional ideal (-5/2*a + 1/2)]
        sage: L.<b> = NumberField(x^2 + 3)
        sage: check_prime(K, L.ideal(5))
        Traceback (most recent call last):
        ...
        TypeError: The ideal Fractional ideal (5) is not a prime ideal of
        Number Field in a with defining polynomial x^2 - 5
        sage: check_prime(K, L.ideal(b))
        Traceback (most recent call last):
        ...
        TypeError: No compatible natural embeddings found for
        Number Field in a with defining polynomial x^2 - 5 and
        Number Field in b with defining polynomial x^2 + 3
    """
