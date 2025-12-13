from sage.features.msolve import msolve as msolve
from sage.misc.converting_dict import KeyConvertingDict as KeyConvertingDict
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_arb import RealBallField as RealBallField
from sage.rings.real_double import RealDoubleField_class as RealDoubleField_class
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField, RealIntervalField_class as RealIntervalField_class
from sage.rings.real_mpfr import RealField_class as RealField_class
from sage.structure.sequence import Sequence as Sequence

def groebner_basis_degrevlex(ideal, proof: bool = True):
    """
    Compute a degrevlex Gröbner basis using msolve

    EXAMPLES::

        sage: from sage.rings.polynomial.msolve import groebner_basis_degrevlex

        sage: R.<a,b,c> = PolynomialRing(GF(101), 3, order='lex')
        sage: I = sage.rings.ideal.Katsura(R,3)
        sage: gb = groebner_basis_degrevlex(I); gb # optional - msolve
        [a + 2*b + 2*c - 1, b*c - 19*c^2 + 10*b + 40*c,
        b^2 - 41*c^2 + 20*b - 20*c, c^3 + 28*c^2 - 37*b + 13*c]
        sage: gb.universe() is R # optional - msolve
        False
        sage: gb.universe().term_order() # optional - msolve
        Degree reverse lexicographic term order
        sage: ideal(gb).transformed_basis(other_ring=R) # optional - msolve
        [c^4 + 38*c^3 - 6*c^2 - 6*c, 30*c^3 + 32*c^2 + b - 14*c,
        a + 2*b + 2*c - 1]

    Gröbner bases over the rationals require `proof=False`::

        sage: R.<x, y> = PolynomialRing(QQ, 2)
        sage: I = Ideal([ x*y - 1, (x-2)^2 + (y-1)^2 - 1])
        sage: I.groebner_basis(algorithm='msolve') # optional - msolve
        Traceback (most recent call last):
        ...
        ValueError: msolve relies on heuristics; please use proof=False
        sage: I.groebner_basis(algorithm='msolve', proof=False) # optional - msolve
        [x*y - 1, x^2 + y^2 - 4*x - 2*y + 4, y^3 - 2*y^2 + x + 4*y - 4]

    TESTS::

        sage: R.<foo, bar> = PolynomialRing(GF(536870909), 2)
        sage: I = Ideal([ foo^2 - 1, bar^2 - 1 ])
        sage: I.groebner_basis(algorithm='msolve') # optional - msolve
        [bar^2 - 1, foo^2 - 1]
    """
def variety(ideal, ring, *, proof: bool = True):
    """
    Compute the variety of a zero-dimensional ideal using msolve.

    Part of the initial implementation was loosely based on the example
    interfaces available as part of msolve, with the authors' permission.

    EXAMPLES::

        sage: from sage.rings.polynomial.msolve import variety
        sage: p = 536870909
        sage: R.<x, y> = PolynomialRing(GF(p), 2, order='lex')
        sage: I = Ideal([ x*y - 1, (x-2)^2 + (y-1)^2 - 1])
        sage: sorted(variety(I, GF(p^2), proof=False), key=str) # optional - msolve
        [{x: 1, y: 1},
         {x: 254228855*z2 + 114981228, y: 232449571*z2 + 402714189},
         {x: 267525699, y: 473946006},
         {x: 282642054*z2 + 154363985, y: 304421338*z2 + 197081624}]

    TESTS::

        sage: p = 536870909
        sage: R.<x, y> = PolynomialRing(GF(p), 2, order='lex')
        sage: I = Ideal([ x*y - 1, (x-2)^2 + (y-1)^2 - 1])

        sage: sorted(I.variety(algorithm='msolve', proof=False), key=str) # optional - msolve
        [{x: 1, y: 1}, {x: 267525699, y: 473946006}]

        sage: K.<a> = GF(p^2)
        sage: sorted(I.variety(K, algorithm='msolve', proof=False), key=str) # optional - msolve
        [{x: 1, y: 1},
         {x: 118750849*a + 194048031, y: 510295713*a + 18174854},
         {x: 267525699, y: 473946006},
         {x: 418120060*a + 75297182, y: 26575196*a + 44750050}]

        sage: R.<x, y> = PolynomialRing(GF(2147483659), 2, order='lex')
        sage: ideal([x, y]).variety(algorithm='msolve', proof=False)
        Traceback (most recent call last):
        ...
        NotImplementedError: unsupported base field: Finite Field of size 2147483659

        sage: R.<x, y> = PolynomialRing(QQ, 2, order='lex')
        sage: I = Ideal([ x*y - 1, (x-2)^2 + (y-1)^2 - 1])

        sage: I.variety(algorithm='msolve', proof=False) # optional - msolve
        [{x: 1, y: 1}]
        sage: I.variety(RealField(100), algorithm='msolve', proof=False) # optional - msolve
        [{x: 2.7692923542386314152404094643, y: 0.36110308052864737763464656216},
         {x: 1.0000000000000000000000000000, y: 1.0000000000000000000000000000}]
        sage: I.variety(RealIntervalField(100), algorithm='msolve', proof=False) # optional - msolve
        [{x: 2.76929235423863141524040946434?, y: 0.361103080528647377634646562159?},
         {x: 1, y: 1}]
        sage: I.variety(RBF, algorithm='msolve', proof=False) # optional - msolve
        [{x: [2.76929235423863 +/- 2.08e-15], y: [0.361103080528647 +/- 4.53e-16]},
         {x: 1.000000000000000, y: 1.000000000000000}]
        sage: I.variety(RDF, algorithm='msolve', proof=False) # optional - msolve
        [{x: 2.7692923542386314, y: 0.36110308052864737}, {x: 1.0, y: 1.0}]
        sage: I.variety(AA, algorithm='msolve', proof=False) # optional - msolve
        [{x: 2.769292354238632?, y: 0.3611030805286474?},
         {x: 1.000000000000000?, y: 1.000000000000000?}]
        sage: I.variety(QQbar, algorithm='msolve', proof=False) # optional - msolve
        [{x: 2.769292354238632?, y: 0.3611030805286474?},
         {x: 1, y: 1},
         {x: 0.11535382288068429? + 0.5897428050222055?*I, y: 0.3194484597356763? - 1.633170240915238?*I},
         {x: 0.11535382288068429? - 0.5897428050222055?*I, y: 0.3194484597356763? + 1.633170240915238?*I}]
        sage: I.variety(ComplexField(100))
        [{y: 1.0000000000000000000000000000, x: 1.0000000000000000000000000000},
         {y: 0.36110308052864737763464656216, x: 2.7692923542386314152404094643},
         {y: 0.31944845973567631118267671892 - 1.6331702409152376561188467320*I, x: 0.11535382288068429237979526783 + 0.58974280502220550164728074602*I},
         {y: 0.31944845973567631118267671892 + 1.6331702409152376561188467320*I, x: 0.11535382288068429237979526783 - 0.58974280502220550164728074602*I}]

        sage: Ideal(x^2 + y^2 - 1, x - y).variety(RBF, algorithm='msolve', proof=False) # optional - msolve
        [{x: [-0.707106781186547 +/- 6.29e-16], y: [-0.707106781186547 +/- 6.29e-16]},
         {x: [0.707106781186547 +/- 6.29e-16], y: [0.707106781186547 +/- 6.29e-16]}]
        sage: sorted(Ideal(x^2 - 1, y^2 - 1).variety(QQ, algorithm='msolve', proof=False), key=str) # optional - msolve
        [{x: -1, y: -1}, {x: -1, y: 1}, {x: 1, y: -1}, {x: 1, y: 1}]
        sage: Ideal(x^2-1, y^2-2).variety(CC, algorithm='msolve', proof=False) # optional - msolve
        [{x: 1.00000000000000, y: 1.41421356237310},
         {x: -1.00000000000000, y: 1.41421356237309},
         {x: 1.00000000000000, y: -1.41421356237309},
         {x: -1.00000000000000, y: -1.41421356237310}]

        sage: Ideal([x, y, x + y]).variety(algorithm='msolve', proof=False) # optional - msolve
        [{x: 0, y: 0}]

        sage: Ideal([x, y, x + y - 1]).variety(algorithm='msolve', proof=False) # optional - msolve
        []
        sage: Ideal([x, y, x + y - 1]).variety(RR, algorithm='msolve', proof=False) # optional - msolve
        []

        sage: Ideal([x*y - 1]).variety(QQbar, algorithm='msolve', proof=False) # optional - msolve
        Traceback (most recent call last):
        ...
        ValueError: positive-dimensional ideal

        sage: R.<x, y> = PolynomialRing(RR, 2, order='lex')
        sage: Ideal(x, y).variety(algorithm='msolve', proof=False)
        Traceback (most recent call last):
        ...
        NotImplementedError: unsupported base field: Real Field with 53 bits of precision

        sage: R.<x, y> = PolynomialRing(QQ, 2, order='lex')
        sage: Ideal(x, y).variety(ZZ, algorithm='msolve', proof=False)
        Traceback (most recent call last):
        ...
        ValueError: no coercion from base field Rational Field to output ring Integer Ring
    """
