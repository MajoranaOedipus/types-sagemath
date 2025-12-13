from . import cycliccover_generic as cycliccover_generic
from .charpoly_frobenius import charpoly_frobenius as charpoly_frobenius
from sage.arith.misc import euler_phi as euler_phi
from sage.matrix.constructor import matrix as matrix, zero_matrix as zero_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing

class CyclicCover_finite_field(cycliccover_generic.CyclicCover_generic):
    def __init__(self, AA, r, f, names=None, verbose: int = 0) -> None:
        '''
        EXAMPLES::

            sage: p = 13
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: C = CyclicCover(4, x^4 + 1)
            sage: C.frobenius_polynomial()
            x^6 - 6*x^5 + 3*x^4 + 60*x^3 + 39*x^2 - 1014*x + 2197
            sage: R.<t> = PowerSeriesRing(Integers())
            sage: C.projective_closure().zeta_series(2,t)
            1 + 8*t + 102*t^2 + O(t^3)
            sage: C.frobenius_polynomial().reverse()(t)/((1-t)*(1-p*t)) + O(t^5)
            1 + 8*t + 102*t^2 + 1384*t^3 + 18089*t^4 + O(t^5)
        '''
    @cached_method
    def frobenius_matrix(self, N=None):
        '''
        Compute `p`-adic Frobenius matrix to precision `p^N`.

        If `N` not supplied, a default value is selected, which is the minimum
        needed to recover the charpoly unambiguously.

        EXAMPLES::

            sage: p = 107
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: CyclicCover(2, x^5 + x).frobenius_matrix()
            [              O(107^2)      89*107 + O(107^2)               O(107^2)               O(107^2)]
            [     89*107 + O(107^2)               O(107^2)               O(107^2)               O(107^2)]
            [              O(107^2)               O(107^2)               O(107^2) 105 + 5*107 + O(107^2)]
            [              O(107^2)               O(107^2) 89 + 53*107 + O(107^2)               O(107^2)]
            sage: CyclicCover(2, 3*x^5 + x).frobenius_matrix()
            [              O(107^2)      14*107 + O(107^2)               O(107^2)               O(107^2)]
            [     69*107 + O(107^2)               O(107^2)               O(107^2)               O(107^2)]
            [              O(107^2)               O(107^2)               O(107^2) 61 + 58*107 + O(107^2)]
            [              O(107^2)               O(107^2) 69 + 53*107 + O(107^2)               O(107^2)]
            sage: CyclicCover(3, x^3 + x).frobenius_matrix()
            [          0           0      O(107)      O(107)]
            [          0           0 52 + O(107)      O(107)]
            [     O(107) 35 + O(107)           0           0]
            [44 + O(107)      O(107)           0           0]
            sage: CyclicCover(3, 3*x^3 + x).frobenius_matrix()
            [          0           0      O(107)      O(107)]
            [          0           0 79 + O(107)      O(107)]
            [     O(107) 42 + O(107)           0           0]
            [30 + O(107)      O(107)           0           0]
        '''
    @cached_method
    def frobenius_polynomial(self):
        '''
        Return the characteristic polynomial of Frobenius.

        EXAMPLES:

        Hyperelliptic curves::

            sage: p = 11
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: f = x^7 + 4*x^2 + 10*x + 4
            sage: CyclicCover(2, f).frobenius_polynomial() == \\\n            ....: HyperellipticCurve(f).frobenius_polynomial()
            True
            sage: f = 2*x^5 + 4*x^3 + x^2 + 2*x + 1
            sage: CyclicCover(2, f).frobenius_polynomial() == \\\n            ....: HyperellipticCurve(f).frobenius_polynomial()
            True
            sage: f = 2*x^6 + 4*x^4 + x^3 + 2*x^2 + x
            sage: CyclicCover(2, f).frobenius_polynomial() == \\\n            ....: HyperellipticCurve(f).frobenius_polynomial()
            True
            sage: p = 1117
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: f = x^9 + 4*x^2 + 10*x + 4
            sage: P1 = CyclicCover(2, f).frobenius_polynomial()
            sage: P2 = HyperellipticCurve(f).frobenius_polynomial()
            sage: P1 == P2  # long time
            True
            sage: f = 2*x^5 + 4*x^3 + x^2 + 2*x + 1
            sage: CyclicCover(2, f).frobenius_polynomial() == \\\n            ....: HyperellipticCurve(f).frobenius_polynomial()
            True

        Superelliptic curves::

            sage: p = 11
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: CyclicCover(3, x^4 + 4*x^3 + 9*x^2 + 3*x + 1).frobenius_polynomial()
            x^6 + 21*x^4 + 231*x^2 + 1331
            sage: CyclicCover(4, x^3 + x + 1).frobenius_polynomial()
            x^6 + 2*x^5 + 11*x^4 + 121*x^2 + 242*x + 1331
            sage: p = 4999
            sage: x = PolynomialRing(GF(p),"x").gen()
            sage: CyclicCover(4, x^3  - 1).frobenius_polynomial() == \\\n            ....: CyclicCover(3, x^4  + 1).frobenius_polynomial()
            True
            sage: CyclicCover(3, x^4 + 4*x^3 + 9*x^2 + 3*x + 1).frobenius_polynomial()
            x^6 + 180*x^5 + 20988*x^4 + 1854349*x^3 + 104919012*x^2 + 4498200180*x + 124925014999
            sage: CyclicCover(4, x^5 + x + 1).frobenius_polynomial()
            x^12 - 64*x^11 + 5018*x^10 - 488640*x^9 + 28119583*x^8 - 641791616*x^7
             + 124245485932*x^6 - 3208316288384*x^5 + 702708407289583*x^4 - 61043359329111360*x^3
             + 3133741752599645018*x^2 - 199800079984001599936*x + 15606259372500374970001

            sage: h = PolynomialRing(GF(1129), \'x\')([-1] + [0]*(5-1) + [1])
            sage: CyclicCover(11, h).frobenius_polynomial()  # long time
            x^40 + 7337188909826596*x^30 + 20187877911930897108199045855206*x^20
             + 24687045654725446027864774006541463602997309796*x^10
             + 11320844849639649951608809973589776933203136765026963553258401

            sage: h = PolynomialRing(GF(1009^2), \'x\')([-1] + [0]*(5-1) + [1])
            sage: CyclicCover(3, h).frobenius_polynomial()  # long time
            x^8 + 532*x^7 - 2877542*x^6 - 242628176*x^5 + 4390163797795*x^4 - 247015136050256*x^3
             - 2982540407204025062*x^2 + 561382189105547134612*x + 1074309286591662654798721

        A non-monic example checking that :issue:`29015` is fixed::

            sage: a = 3
            sage: K.<s> = GF(83^3);
            sage: R.<x> = PolynomialRing(K)
            sage: h = s*x^4 + x*3 + 8
            sage: C = CyclicCover(a, h)
            sage: C.frobenius_polynomial()
            x^6 + 1563486*x^4 + 893980969482*x^2 + 186940255267540403

        Non-superelliptic curves::

            sage: p = 13
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: C = CyclicCover(4, x^4 + 1)
            sage: C.frobenius_polynomial()
            x^6 - 6*x^5 + 3*x^4 + 60*x^3 + 39*x^2 - 1014*x + 2197
            sage: R.<t> = PowerSeriesRing(Integers())
            sage: C.projective_closure().zeta_series(2, t)
            1 + 8*t + 102*t^2 + O(t^3)
            sage: C.frobenius_polynomial().reverse()(t)/((1-t)*(1-p*t)) + O(t^5)
            1 + 8*t + 102*t^2 + 1384*t^3 + 18089*t^4 + O(t^5)

            sage: x = PolynomialRing(GF(11), "x").gen()
            sage: CyclicCover(4, x^6 - 11*x^3 + 70*x^2 - x + 961).frobenius_polynomial()  # long time
            x^14 + 14*x^12 + 287*x^10 + 3025*x^8 + 33275*x^6 + 381997*x^4 + 2254714*x^2 + 19487171
            sage: x = PolynomialRing(GF(4999), "x").gen()
            sage: CyclicCover(4, x^6 - 11*x^3 + 70*x^2 - x + 961).frobenius_polynomial()  # long time
            x^14 - 4*x^13 - 2822*x^12 - 30032*x^11 + 37164411*x^10 - 152369520*x^9
             + 54217349361*x^8 - 1021791160888*x^7 + 271032529455639*x^6 - 3807714457169520*x^5
             + 4642764601604000589*x^4 - 18754988504199390032*x^3 - 8809934776794570547178*x^2
             - 62425037490001499880004*x + 78015690603129374475034999

            sage: p = 11
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: CyclicCover(3, 5*x^3 - 5*x + 13).frobenius_polynomial()
            x^2 + 11
            sage: CyclicCover(3, x^6 + x^4 - x^3 + 2*x^2 - x - 1).frobenius_polynomial()
            x^8 + 32*x^6 + 462*x^4 + 3872*x^2 + 14641
            sage: p = 4999
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: CyclicCover(3, 5*x^3 - 5*x + 13).frobenius_polynomial()
            x^2 - 47*x + 4999
            sage: CyclicCover(3, x^6 + x^4 - x^3 + 2*x^2 - x - 1).frobenius_polynomial()
            x^8 + 122*x^7 + 4594*x^6 - 639110*x^5 - 82959649*x^4 - 3194910890*x^3
             + 114804064594*x^2 + 15240851829878*x + 624500149980001

            sage: p = 11
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: CyclicCover(5, x^5 + x).frobenius_polynomial()  # long time
            x^12 + 4*x^11 + 22*x^10 + 108*x^9 + 503*x^8 + 1848*x^7 + 5588*x^6 + 20328*x^5
             + 60863*x^4 + 143748*x^3 + 322102*x^2 + 644204*x + 1771561
            sage: CyclicCover(5, 2*x^5 + x).frobenius_polynomial()  # long time
            x^12 - 9*x^11 + 42*x^10 - 108*x^9 - 47*x^8 + 1782*x^7 - 8327*x^6 + 19602*x^5
             - 5687*x^4 - 143748*x^3 + 614922*x^2 - 1449459*x + 1771561
            sage: p = 49999
            sage: x = PolynomialRing(GF(p), "x").gen()
            sage: CyclicCover(5, x^5 + x).frobenius_polynomial()  # long time
            x^12 + 299994*x^10 + 37498500015*x^8 + 2499850002999980*x^6
             + 93742500224997000015*x^4 + 1874812507499850001499994*x^2
             + 15623125093747500037499700001
            sage: CyclicCover(5, 2*x^5 + x).frobenius_polynomial() # long time
            x^12 + 299994*x^10 + 37498500015*x^8 + 2499850002999980*x^6
             + 93742500224997000015*x^4 + 1874812507499850001499994*x^2
             + 15623125093747500037499700001


        TESTS::

            sage: for _ in range(5): # long time
            ....:     fail = False
            ....:     p = random_prime(500, lbound=5)
            ....:     for i in range(1, 4):
            ....:         F = GF((p, i))
            ....:         Fx = PolynomialRing(F, \'x\')
            ....:         b = F.random_element()
            ....:         while b == 0:
            ....:            b = F.random_element()
            ....:         E = EllipticCurve(F, [0, b])
            ....:         C1 = CyclicCover(3, Fx([-b, 0, 1]))
            ....:         C2 = CyclicCover(2, Fx([b, 0, 0, 1]))
            ....:         frob = [elt.frobenius_polynomial() for elt in [E, C1, C2]]
            ....:         if len(set(frob)) != 1:
            ....:             E
            ....:             C1
            ....:             C2
            ....:             frob
            ....:             fail = True
            ....:             break
            ....:     if fail:
            ....:       break
            ....: else:
            ....:     True
            True
        '''
