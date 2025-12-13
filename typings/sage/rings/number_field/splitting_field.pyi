from _typeshed import Incomplete
from sage.arith.misc import factorial as factorial
from sage.libs.pari import pari as pari
from sage.rings.integer import Integer as Integer
from sage.rings.number_field.number_field import NumberField as NumberField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField

class SplittingFieldAbort(Exception):
    """
    Special exception class to indicate an early abort of :func:`splitting_field`.

    EXAMPLES::

        sage: from sage.rings.number_field.splitting_field import SplittingFieldAbort
        sage: raise SplittingFieldAbort(20, 60)
        Traceback (most recent call last):
        ...
        SplittingFieldAbort: degree of splitting field is a multiple of 20
        sage: raise SplittingFieldAbort(12, 12)
        Traceback (most recent call last):
        ...
        SplittingFieldAbort: degree of splitting field equals 12
    """
    degree_divisor: Incomplete
    degree_multiple: Incomplete
    def __init__(self, div, mult) -> None: ...

class SplittingData:
    """
    A class to store data for internal use in :func:`splitting_field`.
    It contains two attributes :attr:`pol` (polynomial), :attr:`dm`
    (degree multiple), where ``pol`` is a PARI polynomial and
    ``dm`` a Sage :class:`Integer`.

    ``dm`` is a multiple of the degree of the splitting field of
    ``pol`` over some field `E`. In :func:`splitting_field`, `E` is the
    field containing the current field `K` and all roots of other
    polynomials inside the list `L` with ``dm`` less than this ``dm``.
    """
    pol: Incomplete
    dm: Incomplete
    def __init__(self, _pol, _dm) -> None: ...
    def key(self):
        '''
        Return a sorting key. Compare first by degree bound, then by
        polynomial degree, then by discriminant.

        EXAMPLES::

            sage: from sage.rings.number_field.splitting_field import SplittingData
            sage: L = []
            sage: L.append(SplittingData(pari("x^2 + 1"), 1))
            sage: L.append(SplittingData(pari("x^3 + 1"), 1))
            sage: L.append(SplittingData(pari("x^2 + 7"), 2))
            sage: L.append(SplittingData(pari("x^3 + 1"), 2))
            sage: L.append(SplittingData(pari("x^3 + x^2 + x + 1"), 2))
            sage: L.sort(key=lambda x: x.key()); L
            [SplittingData(x^2 + 1, 1), SplittingData(x^3 + 1, 1), SplittingData(x^2 + 7, 2), SplittingData(x^3 + x^2 + x + 1, 2), SplittingData(x^3 + 1, 2)]
            sage: [x.key() for x in L]
            [(1, 2, 16), (1, 3, 729), (2, 2, 784), (2, 3, 256), (2, 3, 729)]
        '''
    def poldegree(self):
        '''
        Return the degree of ``self.pol``.

        EXAMPLES::

            sage: from sage.rings.number_field.splitting_field import SplittingData
            sage: SplittingData(pari("x^123 + x + 1"), 2).poldegree()
            123
        '''

def splitting_field(poly, name, map: bool = False, degree_multiple=None, abort_degree=None, simplify: bool = True, simplify_all: bool = False):
    """
    Compute the splitting field of a given polynomial, defined over a
    number field.

    INPUT:

    - ``poly`` -- a monic polynomial over a number field

    - ``name`` -- a variable name for the number field

    - ``map`` -- boolean (default: ``False``); also return an embedding of
      ``poly`` into the resulting field. Note that computing this
      embedding might be expensive.

    - ``degree_multiple`` -- a multiple of the absolute degree of
      the splitting field.  If ``degree_multiple`` equals the actual
      degree, this can enormously speed up the computation.

    - ``abort_degree`` -- abort by raising a :class:`SplittingFieldAbort`
      if it can be determined that the absolute degree of the splitting
      field is strictly larger than ``abort_degree``.

    - ``simplify`` -- boolean (default: ``True``); during the algorithm, try
      to find a simpler defining polynomial for the intermediate
      number fields using PARI's ``polredbest()``.  This usually speeds
      up the computation but can also considerably slow it down.
      Try and see what works best in the given situation.

    - ``simplify_all`` -- boolean (default: ``False``); if ``True``, simplify
      intermediate fields and also the resulting number field

    OUTPUT:

    If ``map`` is ``False``, the splitting field as an absolute number
    field.  If ``map`` is ``True``, a tuple ``(K, phi)`` where ``phi``
    is an embedding of the base field in ``K``.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = (x^3 + 2).splitting_field(); K
        Number Field in a with defining polynomial
         x^6 + 3*x^5 + 6*x^4 + 11*x^3 + 12*x^2 - 3*x + 1
        sage: K.<a> = (x^3 - 3*x + 1).splitting_field(); K
        Number Field in a with defining polynomial x^3 - 3*x + 1

    The ``simplify`` and ``simplify_all`` flags usually yield
    fields defined by polynomials with smaller coefficients.
    By default, ``simplify`` is ``True`` and ``simplify_all`` is ``False``.

    ::

        sage: (x^4 - x + 1).splitting_field('a', simplify=False)
        Number Field in a with defining polynomial
         x^24 - 2780*x^22 + 2*x^21 + 3527512*x^20 - 2876*x^19 - 2701391985*x^18 + 945948*x^17
          + 1390511639677*x^16 + 736757420*x^15 - 506816498313560*x^14 - 822702898220*x^13
          + 134120588299548463*x^12 + 362240696528256*x^11 - 25964582366880639486*x^10
          - 91743672243419990*x^9 + 3649429473447308439427*x^8 + 14310332927134072336*x^7
          - 363192569823568746892571*x^6 - 1353403793640477725898*x^5
          + 24293393281774560140427565*x^4 + 70673814899934142357628*x^3
          - 980621447508959243128437933*x^2 - 1539841440617805445432660*x
          + 18065914012013502602456565991
        sage: (x^4 - x + 1).splitting_field('a', simplify=True)
        Number Field in a with defining polynomial
         x^24 + 8*x^23 - 32*x^22 - 310*x^21 + 540*x^20 + 4688*x^19 - 6813*x^18 - 32380*x^17
          + 49525*x^16 + 102460*x^15 - 129944*x^14 - 287884*x^13 + 372727*x^12 + 150624*x^11
          - 110530*x^10 - 566926*x^9 + 1062759*x^8 - 779940*x^7 + 863493*x^6 - 1623578*x^5
          + 1759513*x^4 - 955624*x^3 + 459975*x^2 - 141948*x + 53919
        sage: (x^4 - x + 1).splitting_field('a', simplify_all=True)
        Number Field in a with defining polynomial x^24 - 3*x^23 + 2*x^22 - x^20 + 4*x^19
         + 32*x^18 - 35*x^17 - 92*x^16 + 49*x^15 + 163*x^14 - 15*x^13 - 194*x^12 - 15*x^11
         + 163*x^10 + 49*x^9 - 92*x^8 - 35*x^7 + 32*x^6 + 4*x^5 - x^4 + 2*x^2 - 3*x + 1

    Reducible polynomials also work::

        sage: pol = (x^4 - 1)*(x^2 + 1/2)*(x^2 + 1/3)
        sage: pol.splitting_field('a', simplify_all=True)
        Number Field in a with defining polynomial x^8 - x^4 + 1

    Relative situation::

        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(x^3 + 2)
        sage: S.<t> = PolynomialRing(K)
        sage: L.<b> = (t^2 - a).splitting_field()
        sage: L
        Number Field in b with defining polynomial t^6 + 2

    With ``map=True``, we also get the embedding of the base field
    into the splitting field::

        sage: L.<b>, phi = (t^2 - a).splitting_field(map=True)
        sage: phi
        Ring morphism:
          From: Number Field in a with defining polynomial x^3 + 2
          To:   Number Field in b with defining polynomial t^6 + 2
          Defn: a |--> b^2
        sage: (x^4 - x + 1).splitting_field('a', simplify_all=True, map=True)[1]
        Ring morphism:
          From: Rational Field
          To:   Number Field in a with defining polynomial
                x^24 - 3*x^23 + 2*x^22 - x^20 + 4*x^19 + 32*x^18 - 35*x^17 - 92*x^16
                + 49*x^15 + 163*x^14 - 15*x^13 - 194*x^12 - 15*x^11 + 163*x^10 + 49*x^9
                - 92*x^8 - 35*x^7 + 32*x^6 + 4*x^5 - x^4 + 2*x^2 - 3*x + 1
          Defn: 1 |--> 1

    We can enable verbose messages::

        sage: from sage.misc.verbose import set_verbose
        sage: set_verbose(2)
        sage: K.<a> = (x^3 - x + 1).splitting_field()
        verbose 1 (...: splitting_field.py, splitting_field) Starting field: y
        verbose 1 (...: splitting_field.py, splitting_field) SplittingData to factor: [(3, 0)]
        verbose 2 (...: splitting_field.py, splitting_field) Done factoring (time = ...)
        verbose 1 (...: splitting_field.py, splitting_field) SplittingData to handle: [(2, 2), (3, 3)]
        verbose 1 (...: splitting_field.py, splitting_field) Bounds for absolute degree: [6, 6]
        verbose 2 (...: splitting_field.py, splitting_field) Handling polynomial x^2 + 23
        verbose 1 (...: splitting_field.py, splitting_field) New field before simplifying: x^2 + 23 (time = ...)
        verbose 1 (...: splitting_field.py, splitting_field) New field: y^2 - y + 6 (time = ...)
        verbose 2 (...: splitting_field.py, splitting_field) Converted polynomials to new field (time = ...)
        verbose 1 (...: splitting_field.py, splitting_field) SplittingData to factor: []
        verbose 2 (...: splitting_field.py, splitting_field) Done factoring (time = ...)
        verbose 1 (...: splitting_field.py, splitting_field) SplittingData to handle: [(3, 3)]
        verbose 1 (...: splitting_field.py, splitting_field) Bounds for absolute degree: [6, 6]
        verbose 2 (...: splitting_field.py, splitting_field) Handling polynomial x^3 - x + 1
        verbose 1 (...: splitting_field.py, splitting_field) New field: y^6 + 3*y^5 + 19*y^4 + 35*y^3 + 127*y^2 + 73*y + 271 (time = ...)
        sage: set_verbose(0)

    Try all Galois groups in degree 4. We use a quadratic base field
    such that ``polgalois()`` cannot be used::

        sage: R.<x> = PolynomialRing(QuadraticField(-11))
        sage: C2C2pol = x^4 - 10*x^2 + 1
        sage: C2C2pol.splitting_field('x')
        Number Field in x with defining polynomial x^8 + 24*x^6 + 608*x^4 + 9792*x^2 + 53824
        sage: C4pol = x^4 + x^3 + x^2 + x + 1
        sage: C4pol.splitting_field('x')
        Number Field in x with defining polynomial
         x^8 - x^7 - 2*x^6 + 5*x^5 + x^4 + 15*x^3 - 18*x^2 - 27*x + 81
        sage: D8pol = x^4 - 2
        sage: D8pol.splitting_field('x')
        Number Field in x with defining polynomial
         x^16 + 8*x^15 + 68*x^14 + 336*x^13 + 1514*x^12 + 5080*x^11 + 14912*x^10
          + 35048*x^9 + 64959*x^8 + 93416*x^7 + 88216*x^6 + 41608*x^5 - 25586*x^4
          - 60048*x^3 - 16628*x^2 + 12008*x + 34961
        sage: A4pol = x^4 - 4*x^3 + 14*x^2 - 28*x + 21
        sage: A4pol.splitting_field('x')
        Number Field in x with defining polynomial
         x^24 - 20*x^23 + 290*x^22 - 3048*x^21 + 26147*x^20 - 186132*x^19 + 1130626*x^18
          - 5913784*x^17 + 26899345*x^16 - 106792132*x^15 + 371066538*x^14 - 1127792656*x^13
          + 2991524876*x^12 - 6888328132*x^11 + 13655960064*x^10 - 23000783036*x^9
          + 32244796382*x^8 - 36347834476*x^7 + 30850889884*x^6 - 16707053128*x^5
          + 1896946429*x^4 + 4832907884*x^3 - 3038258802*x^2 - 200383596*x + 593179173
        sage: S4pol = x^4 + x + 1
        sage: S4pol.splitting_field('x')
        Number Field in x with defining polynomial x^48 ...

    Some bigger examples::

        sage: R.<x> = PolynomialRing(QQ)
        sage: pol15 = chebyshev_T(31, x) - 1    # 2^30*(x-1)*minpoly(cos(2*pi/31))^2
        sage: pol15.splitting_field('a')
        Number Field in a with defining polynomial
         x^15 - x^14 - 14*x^13 + 13*x^12 + 78*x^11 - 66*x^10 - 220*x^9 + 165*x^8
          + 330*x^7 - 210*x^6 - 252*x^5 + 126*x^4 + 84*x^3 - 28*x^2 - 8*x + 1
        sage: pol48 = x^6 - 4*x^4 + 12*x^2 - 12
        sage: pol48.splitting_field('a')
        Number Field in a with defining polynomial x^48 ...

    If you somehow know the degree of the field in advance, you
    should add a ``degree_multiple`` argument.  This can speed up the
    computation, in particular for polynomials of degree >= 12 or
    for relative extensions::

        sage: pol15.splitting_field('a', degree_multiple=15)
        Number Field in a with defining polynomial
         x^15 + x^14 - 14*x^13 - 13*x^12 + 78*x^11 + 66*x^10 - 220*x^9 - 165*x^8
          + 330*x^7 + 210*x^6 - 252*x^5 - 126*x^4 + 84*x^3 + 28*x^2 - 8*x - 1

    A value for ``degree_multiple`` which isn't actually a
    multiple of the absolute degree of the splitting field can
    either result in a wrong answer or the following exception::

        sage: pol48.splitting_field('a', degree_multiple=20)
        Traceback (most recent call last):
        ...
        ValueError: inconsistent degree_multiple in splitting_field()

    Compute the Galois closure as the splitting field of the defining polynomial::

        sage: R.<x> = PolynomialRing(QQ)
        sage: pol48 = x^6 - 4*x^4 + 12*x^2 - 12
        sage: K.<a> = NumberField(pol48)
        sage: L.<b> = pol48.change_ring(K).splitting_field()
        sage: L
        Number Field in b with defining polynomial x^48 ...

    Try all Galois groups over `\\QQ` in degree 5 except for `S_5`
    (the latter is infeasible with the current implementation)::

        sage: C5pol = x^5 + x^4 - 4*x^3 - 3*x^2 + 3*x + 1
        sage: C5pol.splitting_field('x')
        Number Field in x with defining polynomial x^5 + x^4 - 4*x^3 - 3*x^2 + 3*x + 1
        sage: D10pol = x^5 - x^4 - 5*x^3 + 4*x^2 + 3*x - 1
        sage: D10pol.splitting_field('x')
        Number Field in x with defining polynomial
         x^10 - 28*x^8 + 216*x^6 - 681*x^4 + 902*x^2 - 401
        sage: AGL_1_5pol = x^5 - 2
        sage: AGL_1_5pol.splitting_field('x')
        Number Field in x with defining polynomial
         x^20 + 10*x^19 + 55*x^18 + 210*x^17 + 595*x^16 + 1300*x^15 + 2250*x^14
          + 3130*x^13 + 3585*x^12 + 3500*x^11 + 2965*x^10 + 2250*x^9 + 1625*x^8
          + 1150*x^7 + 750*x^6 + 400*x^5 + 275*x^4 + 100*x^3 + 75*x^2 + 25
        sage: A5pol = x^5 - x^4 + 2*x^2 - 2*x + 2
        sage: A5pol.splitting_field('x')
        Number Field in x with defining polynomial x^60 ...

    We can use the ``abort_degree`` option if we don't want to compute
    fields of too large degree (this can be used to check whether the
    splitting field has small degree)::

        sage: (x^5 + x + 3).splitting_field('b', abort_degree=119)
        Traceback (most recent call last):
        ...
        SplittingFieldAbort: degree of splitting field equals 120
        sage: (x^10 + x + 3).splitting_field('b', abort_degree=60)  # long time (10s on sage.math, 2014)
        Traceback (most recent call last):
        ...
        SplittingFieldAbort: degree of splitting field is a multiple of 180

    Use the ``degree_divisor`` attribute to recover the divisor of the
    degree of the splitting field or ``degree_multiple`` to recover a
    multiple::

        sage: from sage.rings.number_field.splitting_field import SplittingFieldAbort
        sage: try:  # long time (4s on sage.math, 2014)
        ....:     (x^8 + x + 1).splitting_field('b', abort_degree=60, simplify=False)
        ....: except SplittingFieldAbort as e:
        ....:     print(e.degree_divisor)
        ....:     print(e.degree_multiple)
        120
        1440

    TESTS::

        sage: from sage.rings.number_field.splitting_field import splitting_field
        sage: splitting_field(polygen(QQ), name='x', map=True, simplify_all=True)
        (Number Field in x with defining polynomial x, Ring morphism:
          From: Rational Field
          To:   Number Field in x with defining polynomial x
          Defn: 1 |--> 1)
    """
