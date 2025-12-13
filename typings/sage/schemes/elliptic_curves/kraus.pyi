from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve

def c4c6_nonsingular(c4, c6):
    """
    Check if `c_4`, `c_6` are integral with valid associated discriminant.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    OUTPUT:

    Boolean, ``True`` if `c_4`, `c_6` are both integral and `c_4^3-c_6^2` is a
    nonzero multiple of 1728.

    EXAMPLES:

    Over `\\QQ`::

        sage: from sage.schemes.elliptic_curves.kraus import c4c6_nonsingular
        sage: c4c6_nonsingular(0,0)
        False
        sage: c4c6_nonsingular(0,1/2)
        False
        sage: c4c6_nonsingular(2,3)
        False
        sage: c4c6_nonsingular(4,8)
        False
        sage: all(c4c6_nonsingular(*E.c_invariants()) for E in cremona_curves([    11..100]))
        True

    Over number fields::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4c6_nonsingular(-217728*a - 679104, 141460992*a + 409826304)
        True
        sage: K.<a> = NumberField(x^3 - 10)
        sage: c4c6_nonsingular(-217728*a - 679104, 141460992*a + 409826304)
        True
    """
def c4c6_model(c4, c6, assume_nonsingular: bool = False):
    """
    Return the elliptic curve [0,0,0,-c4/48,-c6/864] with given c-invariants.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``assume_nonsingular`` -- boolean (default: ``False``); if ``True``,
      check for integrality and nosingularity

    OUTPUT:

    The elliptic curve with a-invariants `[0,0,0,-c_4/48,-c_6/864]`, whose
    c-invariants are the given `c_4`, `c_6`.  If the supplied invariants are
    singular, returns ``None`` when ``assume_nonsingular`` is ``False`` and
    raises an :exc:`ArithmeticError` otherwise.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.kraus import c4c6_model
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^3 - 10)                                             # needs sage.rings.number_field
        sage: c4c6_model(-217728*a - 679104, 141460992*a + 409826304)                   # needs sage.rings.number_field
        Elliptic Curve defined by y^2 = x^3 + (4536*a+14148)*x + (-163728*a-474336)
         over Number Field in a with defining polynomial x^3 - 10

        sage: c4, c6 = EllipticCurve('389a1').c_invariants()
        sage: c4c6_model(c4,c6)
        Elliptic Curve defined by y^2 = x^3 - 7/3*x + 107/108 over Rational Field
    """
def make_integral(a, P, e):
    """
    Return `b` in `O_K` with `P^e|(a-b)`, given `a` in `O_{K,P}`.

    INPUT:

    - ``a`` -- a number field element integral at `P`

    - ``P`` -- a prime ideal of the number field

    - ``e`` -- positive integer

    OUTPUT:

    A globally integral number field element `b` which is congruent to
    `a` modulo `P^e`.

    ALGORITHM:

    Totally naive, we simply test residues modulo `P^e` until one
    works.  We will only use this when `P` is a prime dividing 2 and `e`
    is the ramification degree, so the number of residues to check is
    at worst `2^d` where `d` is the degree of the field.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.kraus import make_integral

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: P = K.primes_above(2)[0]
        sage: e = P.ramification_index(); e
        2
        sage: x = 1/5
        sage: b = make_integral(x, P, e); b
        1
        sage: (b-x).valuation(P) >= e
        True
        sage: make_integral(1/a, P, e)
        Traceback (most recent call last):
        ...
        ArithmeticError: Cannot lift 1/10*a to O_K mod (Fractional ideal (2, a))^2
    """
def sqrt_mod_4(x, P):
    """
    Return a local square root mod 4, if it exists.

    INPUT:

    - ``x`` -- an integral number field element

    - ``P`` -- a prime ideal of the number field dividing 2

    OUTPUT:

    A pair ``(True, r)`` where that `r^2-x` has valuation at least `2e`,
    or ``(False, 0)`` if there is no such `r`.  Note that
    `r^2\\mod{P^{2e}}` only depends on `r\\mod{P^e}`.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import sqrt_mod_4
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: P = K.primes_above(2)[0]
        sage: sqrt_mod_4(1 + 2*a, P)
        (False, 0)
        sage: sqrt_mod_4(-1 + 2*a, P)
        (True, a + 1)
        sage: (1+a)^2 - (-1 + 2*a)
        12
        sage: e = P.ramification_index()
        sage: ((1+a)^2 - (-1+2*a)).mod(P**e)
        0
    """
def check_b2_local(c4, c6, P, b2, debug: bool = False):
    """
    Test if `b_2` gives a valid model at a prime dividing 3.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``P`` -- a prime ideal of the number field which divides 3

    - ``b2`` -- an element of the number field

    OUTPUT:

    The elliptic curve which is the `(b_2/12,0,0)`-transform of
    `[0,0,0,-c_4/48,-c_6/864]` if this is integral at `P`, else ``False``.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4 = -60544*a + 385796
        sage: c6 = -55799680*a + 262126328
        sage: P3a, P3b = K.primes_above(3)
        sage: from sage.schemes.elliptic_curves.kraus import check_b2_local

    `b_2=0` works at the first prime but not the second::

        sage: b2 = 0
        sage: check_b2_local(c4,c6,P3a,b2)                                               # needs sage.rings.number_field
        Elliptic Curve defined by
         y^2 = x^3 + (3784/3*a-96449/12)*x + (1743740/27*a-32765791/108)
         over Number Field in a with defining polynomial x^2 - 10
        sage: check_b2_local(c4,c6,P3b,b2)                                               # needs sage.rings.number_field
        False

    `b_2=-a` works at the second prime but not the first::

        sage: b2 = -a                                                                   # needs sage.rings.number_field
        sage: check_b2_local(c4,c6,P3a,b2,debug=True)                                    # needs sage.rings.number_field
        check_b2_local: not integral at Fractional ideal (3, a + 1)
        False
        sage: check_b2_local(c4,c6,P3b,b2)                                               # needs sage.rings.number_field
        Elliptic Curve defined by
         y^2 = x^3 + (-1/4*a)*x^2 + (3784/3*a-192893/24)*x + (56378369/864*a-32879311/108)
         over Number Field in a with defining polynomial x^2 - 10

    Using CRT we can do both with the same `b_2`::

        sage: b2 = K.solve_CRT([0,-a],[P3a,P3b]); b2                                    # needs sage.rings.number_field
        a + 1
        sage: check_b2_local(c4,c6,P3a,b2)                                               # needs sage.rings.number_field
        Elliptic Curve defined by
         y^2 = x^3 + (1/4*a+1/4)*x^2 + (10091/8*a-128595/16)*x + (4097171/64*a-19392359/64)
         over Number Field in a with defining polynomial x^2 - 10
        sage: check_b2_local(c4,c6,P3b,b2)                                               # needs sage.rings.number_field
        Elliptic Curve defined
         by y^2 = x^3 + (1/4*a+1/4)*x^2 + (10091/8*a-128595/16)*x + (4097171/64*a-19392359/64)
         over Number Field in a with defining polynomial x^2 - 10
    """
def check_b2_global(c4, c6, b2, debug: bool = False):
    """
    Test if `b_2` gives a valid model at all primes dividing 3.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``b2`` -- an element of the number field

    OUTPUT:

    The elliptic curve which is the `(b_2/12,0,0)`-transform of
    `[0,0,0,-c_4/48,-c_6/864]` if this is integral at all primes `P`
    dividing 3, else ``False``.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4 = -60544*a + 385796
        sage: c6 = -55799680*a + 262126328
        sage: b2 = a+1
        sage: from sage.schemes.elliptic_curves.kraus import check_b2_global
        sage: check_b2_global(c4,c6,b2)
        Elliptic Curve defined by
         y^2 = x^3 + (1/4*a+1/4)*x^2 + (10091/8*a-128595/16)*x + (4097171/64*a-19392359/64)
         over Number Field in a with defining polynomial x^2 - 10
        sage: check_b2_global(c4,c6,0,debug=True)
        check_b2_global: not integral at all primes dividing 3
        False
        sage: check_b2_global(c4,c6,-a,debug=True)
        check_b2_global: not integral at all primes dividing 3
        False
    """
def check_Kraus_local_3(c4, c6, P, assume_nonsingular: bool = False, debug: bool = False):
    """
    Test if `c_4`, `c_6` satisfy Kraus's conditions at a prime `P` dividing 3.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``P`` -- a prime ideal of the number field which divides 3

    - ``assume_nonsingular`` -- boolean (default: ``False``); if ``True``,
      check for integrality and nosingularity

    OUTPUT:

    Either ``(False, 0)`` if Kraus's conditions fail, or ``(True, b2)`` if
    they pass, in which case the elliptic curve which is the
    `(b_2/12,0,0)`-transform of `[0,0,0,-c_4/48,-c_6/864]` is integral at `P`.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_Kraus_local_3
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4 = -60544*a + 385796
        sage: c6 = -55799680*a + 262126328
        sage: P3a, P3b = K.primes_above(3)
        sage: check_Kraus_local_3(c4,c6,P3a)
        (True, 0)
        sage: check_Kraus_local_3(c4,c6,P3b)
        (True, -a)

    An example in a field where 3 is ramified::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^2 - 15)
        sage: c4 = -60504*a + 386001
        sage: c6 = -55346820*a + 261045153
        sage: P3 = K.primes_above(3)[0]
        sage: check_Kraus_local_3(c4,c6,P3)
        (True, a)
    """
def check_a1a3_local(c4, c6, P, a1, a3, debug: bool = False):
    """
    Test if `a_1`, `a_3` are valid at a prime `P` dividing `2`.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``P`` -- a prime ideal of the number field which divides 2

    - ``a1``, ``a3`` -- elements of the number field

    OUTPUT:

    The elliptic curve which is the `(a_1^2/12,a_1/2,a_3/2)`-transform of
    `[0,0,0,-c_4/48,-c_6/864]` if this is integral at `P`, else ``False``.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_a1a3_local
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4 = -60544*a + 385796
        sage: c6 = -55799680*a + 262126328
        sage: P = K.primes_above(2)[0]
        sage: check_a1a3_local(c4,c6,P,a,0)
        Elliptic Curve defined by
         y^2 + a*x*y = x^3 + (3784/3*a-24106/3)*x + (1772120/27*a-2790758/9)
         over Number Field in a with defining polynomial x^2 - 10
        sage: check_a1a3_local(c4,c6,P,a,a,debug=True)
        check_a1a3_local: not integral at Fractional ideal (2, a)
        False
    """
def check_a1a3_global(c4, c6, a1, a3, debug: bool = False):
    """
    Test if `a_1`, `a_3` are valid at all primes `P` dividing 2.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``a1``, ``a3`` -- elements of the number field

    OUTPUT:

    The elliptic curve which is the `(a_1^2/12,a_1/2,a_3/2)`-transform of
    `[0,0,0,-c_4/48,-c_6/864]` if this is integral at all primes `P`
    dividing 2, else ``False``.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_a1a3_global
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4 = -60544*a + 385796
        sage: c6 = -55799680*a + 262126328
        sage: check_a1a3_global(c4,c6,a,a,debug=False)
        False
        sage: check_a1a3_global(c4,c6,a,0)
        Elliptic Curve defined by
         y^2 + a*x*y = x^3 + (3784/3*a-24106/3)*x + (1772120/27*a-2790758/9)
         over Number Field in a with defining polynomial x^2 - 10
    """
def check_rst_global(c4, c6, r, s, t, debug: bool = False):
    """
    Test if the `(r,s,t)`-transform of the standard `c_4,c_6`-model is integral.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``r``, ``s``, ``t`` -- elements of the number field

    OUTPUT:

    The elliptic curve which is the `(r,s,t)`-transform of
    `[0,0,0,-c_4/48,-c_6/864]` if this is integral at all primes `P`, else
    ``False``.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_rst_global
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2-10)
        sage: c4 = -60544*a + 385796
        sage: c6 = -55799680*a + 262126328
        sage: check_rst_global(c4,c6,1/3*a - 133/6, 3/2*a, -89/2*a + 5)
        Elliptic Curve defined by
         y^2 + 3*a*x*y + (-89*a+10)*y = x^3 + (a-89)*x^2 + (1202*a-5225)*x + (34881*a-151813)
         over Number Field in a with defining polynomial x^2 - 10
        sage: check_rst_global(c4,c6,a, 3, -89*a, debug=False)
        False
    """
def check_Kraus_local_2(c4, c6, P, a1=None, assume_nonsingular: bool = False):
    """
    Test if `c_4`, `c_6` satisfy Kraus's conditions at a prime `P` dividing 2.

    INPUT:

    - ``c4``, ``c6`` -- integral elements of a number field

    - ``P`` -- a prime ideal of the number field which divides 2

    - ``a1`` -- an integral elements of a number field, or ``None`` (default)

    - ``assume_nonsingular`` -- boolean (default: ``False``); if ``True``,
      check for integrality and nonsingularity

    OUTPUT:

    Either ``(False, 0, 0)`` if Kraus's conditions fail, or ``(True, a1,
    a3)`` if they pass, in which case the elliptic curve which is the
    `(a_1^2/12,a_1/2,a_3/2)`-transform of `[0,0,0,-c_4/48,-c_6/864]` is
    integral at `P`.  If `a_1` is provided and valid then the output will
    be ``(True, a1, a3)`` for suitable `a_3`.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_Kraus_local_2
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: c4 = -60544*a + 385796  # EllipticCurve([a,a,0,1263*a-8032,62956*a-305877])
        sage: c6 = -55799680*a + 262126328
        sage: P = K.primes_above(2)[0]
        sage: check_Kraus_local_2(c4,c6,P)
        (True, a, 0)
    """
def check_Kraus_local(c4, c6, P, assume_nonsingular: bool = False):
    """
    Check Kraus's conditions locally at a prime `P`.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``P`` -- a prime ideal of the number field

    - ``assume_nonsingular`` -- boolean (default: ``False``); if ``True``,
      check for integrality and nonsingularity

    OUTPUT:

    Tuple: either ``(True, E)`` if there is a Weierstrass model `E` integral
    at `P` and with invariants `c_4`, `c_6`, or ``(False, None)`` if there is
    none.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_Kraus_local
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 15)
        sage: P2 = K.primes_above(2)[0]
        sage: P3 = K.primes_above(3)[0]
        sage: P5 = K.primes_above(5)[0]
        sage: E = EllipticCurve([a,a,0,1263*a-8032,62956*a-305877])
        sage: c4, c6 = E.c_invariants()
        sage: flag, E = check_Kraus_local(c4,c6,P2); flag
        True
        sage: E.is_local_integral_model(P2) and (c4,c6)==E.c_invariants()
        True
        sage: flag, E = check_Kraus_local(c4,c6,P3); flag
        True
        sage: E.is_local_integral_model(P3) and (c4,c6)==E.c_invariants()
        True
        sage: flag, E = check_Kraus_local(c4,c6,P5); flag
        True
        sage: E.is_local_integral_model(P5) and (c4,c6)==E.c_invariants()
        True

        sage: # needs sage.rings.number_field
        sage: c4 = 123+456*a
        sage: c6 = 789+101112*a
        sage: check_Kraus_local(c4,c6,P2)
        (False, None)
        sage: check_Kraus_local(c4,c6,P3)
        (False, None)
        sage: check_Kraus_local(c4,c6,P5)
        (False, None)
    """
def check_Kraus_global(c4, c6, assume_nonsingular: bool = False, debug: bool = False):
    """
    Test if `c_4`, `c_6` satisfy Kraus's conditions at all primes.

    INPUT:

    - ``c4``, ``c6`` -- elements of a number field

    - ``assume_nonsingular`` -- boolean (default: ``False``); if ``True``,
      check for integrality and nonsingularity

    OUTPUT:

    Either ``False`` if Kraus's conditions fail, or, if they pass, an
    elliptic curve `E` which is integral and has c-invariants `c_4`, `c_6`.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.kraus import check_Kraus_global
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: E = EllipticCurve([a,a,0,1263*a-8032,62956*a-305877])
        sage: c4, c6 = E.c_invariants()
        sage: check_Kraus_global(c4,c6,debug=True)
        Local Kraus conditions for (c4,c6)=(-60544*a + 385796,-55799680*a + 262126328) pass at all primes dividing 3
        Using b2=a + 1 gives a model integral at 3:
        (0, 1/4*a + 1/4, 0, 10091/8*a - 128595/16, 4097171/64*a - 19392359/64)
        Local Kraus conditions for (c4,c6)=(-60544*a + 385796,-55799680*a + 262126328) pass at all primes dividing 2
        Using (a1,a3)=(3*a,0) gives a model integral at 2:
        (3*a, 0, 0, 3784/3*a - 23606/3, 1999160/27*a - 9807634/27)
        (a1, b2, a3) = (3*a, a + 1, 0)
        Using (r, s, t)=(1/3*a - 133/6, 3/2*a, -89/2*a + 5) should give a global integral model...
        ...and it does!
        Elliptic Curve defined by
         y^2 + 3*a*x*y + (-89*a+10)*y = x^3 + (a-89)*x^2 + (1202*a-5225)*x + (34881*a-151813)
         over Number Field in a with defining polynomial x^2 - 10

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^2 - 15)
        sage: E = EllipticCurve([0, 0, 0, 4536*a + 14148, -163728*a - 474336])
        sage: c4, c6 = E.c_invariants()
        sage: check_Kraus_global(c4,c6)
        Elliptic Curve defined by y^2 = x^3 + (4536*a+14148)*x + (-163728*a-474336)
         over Number Field in a with defining polynomial x^2 - 15

    TESTS (see :issue:`17295`)::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(x^3 - 7*x - 5)
        sage: E = EllipticCurve([a, 0, 1, 2*a^2 + 5*a + 3, -a^2 - 3*a - 2])
        sage: assert E.conductor().norm() == 8
        sage: G = K.galois_group(names='b')
        sage: def conj_curve(E, sigma): return EllipticCurve([sigma(a) for a in E.ainvs()])
        sage: EL = conj_curve(E,G[0])
        sage: L = EL.base_field()
        sage: assert L.class_number() == 2
        sage: EL.isogeny_class()  # long time (~10s)
        Isogeny class of Elliptic Curve defined by
         y^2 + (-1/90*b^4+7/18*b^2-1/2*b-98/45)*x*y + y = x^3 + (1/45*b^5-1/18*b^4-7/9*b^3+41/18*b^2+167/90*b-29/9)*x + (-1/90*b^5+1/30*b^4+7/18*b^3-4/3*b^2-61/90*b+11/5)
         over Number Field in b with defining polynomial x^6 - 42*x^4 + 441*x^2 - 697
    """
def semi_global_minimal_model(E, debug: bool = False):
    """
    Return a global minimal model for this elliptic curve if it
    exists, or a model minimal at all but one prime otherwise.

    INPUT:

    - ``E`` -- an elliptic curve over a number field

    - ``debug`` -- boolean (default: ``False``); if ``True``, prints some
      messages about the progress of the computation

    OUTPUT:

    A tuple ``(Emin, I)`` where ``Emin`` is an elliptic curve which is either a
    global minimal model of `E` if one exists (i.e., an integral model
    which is minimal at every prime), or a semi-global minimal model
    (i.e., an integral model which is minimal at every prime except
    one).  `I` is the unit ideal of ``Emin`` is a global minimal model, else
    is the unique prime at which ``Emin`` is not minimal.  Thus in all
    cases,
    ``Emin.minimal_discriminant_ideal() * I**12 == (E.discriminant())``.

    .. NOTE::

        This function is normally not called directly by users, who
        will use the elliptic curve method :meth:`global_minimal_model`
        instead; that method also applied various reductions after
        minimising the model.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 10)
        sage: K.class_number()
        2
        sage: E = EllipticCurve([0,0,0,-186408*a - 589491, 78055704*a + 246833838])
        sage: from sage.schemes.elliptic_curves.kraus import semi_global_minimal_model
        sage: Emin, P = semi_global_minimal_model(E)
        sage: Emin
        Elliptic Curve defined by
         y^2 + 3*x*y + (2*a-11)*y = x^3 + (a-10)*x^2 + (-152*a-415)*x + (1911*a+5920)
         over Number Field in a with defining polynomial x^2 - 10
        sage: E.minimal_discriminant_ideal()*P**12 == K.ideal(Emin.discriminant())
        True

    TESTS:

    Consider (see :issue:`20737`) a curve with no global minimal model
    whose non-minimality class has order 3 in the class group, which
    has order 3315. The smallest prime in that ideal class has norm
    23567::

        sage: # long time, needs sage.rings.number_field
        sage: K.<a> = NumberField(x^2 - x + 31821453)
        sage: ainvs = (0, 0, 0, -382586771000351226384*a - 2498023791133552294513515,
        ....:          358777608829102441023422458989744*a + 1110881475104109582383304709231832166)
        sage: E = EllipticCurve(ainvs)
        sage: from sage.schemes.elliptic_curves.kraus import semi_global_minimal_model
        sage: Emin, p = semi_global_minimal_model(E)  # 25s
        sage: p
        Fractional ideal (23567, a + 2270)
        sage: p.norm()
        23567
        sage: Emin.discriminant().norm().factor()
        23567^12
    """
