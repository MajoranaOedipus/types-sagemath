from .local_generic import LocalGeneric as LocalGeneric
from sage.categories.fields import Fields as Fields
from sage.categories.morphism import Morphism as Morphism
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc import some_tuples as some_tuples
from sage.rings.infinity import Infinity as Infinity, infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal

class pAdicGeneric(LocalGeneric):
    def __init__(self, base, p, prec, print_mode, names, element_class, category=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``base`` -- base ring
        - ``p`` -- prime
        - ``print_mode`` -- dictionary of print options
        - ``names`` -- how to print the uniformizer
        - ``element_class`` -- the class for elements of this ring

        EXAMPLES::

            sage: R = Zp(17)  # indirect doctest
        """
    def some_elements(self):
        """
        Return a list of elements in this ring.

        This is typically used for running generic tests (see :class:`TestSuite`).

        EXAMPLES::

            sage: Zp(2,4).some_elements()
            [0, 1 + O(2^4), 2 + O(2^5), 1 + 2^2 + 2^3 + O(2^4), 2 + 2^2 + 2^3 + 2^4 + O(2^5)]
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        We conventionally define this as 1: for base rings, we take a
        uniformizer as the generator; for extension rings, we take a
        root of the minimal polynomial defining the extension.

        EXAMPLES::

            sage: Zp(5).ngens()
            1
            sage: Zq(25,names='a').ngens()                                              # needs sage.libs.ntl
            1
        """
    def gens(self) -> tuple:
        """
        Return a tuple of generators.

        EXAMPLES::

            sage: R = Zp(5); R.gens()
            (5 + O(5^21),)
            sage: Zq(25,names='a').gens()                                               # needs sage.libs.ntl
            (a + O(5^20),)
            sage: S.<x> = ZZ[]; f = x^5 + 25*x -5; W.<w> = R.ext(f); W.gens()           # needs sage.libs.ntl
            (w + O(w^101),)
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison of ``self`` with ``other``.

        We consider two `p`-adic rings or fields to be equal if they are
        equal mathematically, and also have the same precision cap and
        printing parameters.

        EXAMPLES::

            sage: R = Qp(7)
            sage: S = Qp(7,print_mode='val-unit')
            sage: R == S
            False
            sage: S = Qp(7,type='capped-rel')
            sage: R == S
            True
            sage: R is S
            True
        """
    def print_mode(self) -> str:
        """
        Return the current print mode as a string.

        EXAMPLES::

            sage: R = Qp(7,5, 'capped-rel')
            sage: R.print_mode()
            'series'
        """
    def characteristic(self):
        """
        Return the characteristic of ``self``, which is always 0.

        EXAMPLES::

            sage: R = Zp(3, 10,'fixed-mod'); R.characteristic()
            0
        """
    def prime(self):
        """
        Return the prime, ie the characteristic of the residue field.

        OUTPUT: the characteristic of the residue field

        EXAMPLES::

            sage: R = Zp(3,5,'fixed-mod')
            sage: R.prime()
            3
        """
    def uniformizer_pow(self, n):
        """
        Return `p^n`, as an element of ``self``.

        If ``n`` is infinity, returns 0.

        EXAMPLES::

            sage: R = Zp(3, 5, 'fixed-mod')
            sage: R.uniformizer_pow(3)
            3^3
            sage: R.uniformizer_pow(infinity)
            0
        """
    def residue_characteristic(self):
        """
        Return the prime, i.e., the characteristic of the residue field.

        OUTPUT: the characteristic of the residue field

        EXAMPLES::

            sage: R = Zp(3,5,'fixed-mod')
            sage: R.residue_characteristic()
            3
        """
    def residue_class_field(self):
        """
        Return the residue class field.

        EXAMPLES::

            sage: R = Zp(3,5,'fixed-mod')
            sage: k = R.residue_class_field()
            sage: k
            Finite Field of size 3
        """
    def residue_field(self):
        """
        Return the residue class field.

        EXAMPLES::

            sage: R = Zp(3,5,'fixed-mod')
            sage: k = R.residue_field()
            sage: k
            Finite Field of size 3
        """
    def residue_ring(self, n):
        """
        Return the quotient of the ring of integers by the ``n``-th
        power of the maximal ideal.

        EXAMPLES::

            sage: R = Zp(11)
            sage: R.residue_ring(3)
            Ring of integers modulo 1331
        """
    def residue_system(self):
        """
        Return a list of elements representing all the residue classes.

        EXAMPLES::

            sage: R = Zp(3, 5,'fixed-mod')
            sage: R.residue_system()
            [0, 1, 2]
        """
    def fraction_field(self, print_mode=None):
        '''
        Return the fraction field of this ring or field.

        For `\\ZZ_p`, this is the `p`-adic field with the same options,
        and for extensions, it is just the extension of the fraction
        field of the base determined by the same polynomial.

        The fraction field of a capped absolute ring is capped relative,
        and that of a fixed modulus ring is floating point.

        INPUT:

        - ``print_mode`` -- (optional) a dictionary containing print options;
          defaults to the same options as this ring

        OUTPUT: the fraction field of this ring

        EXAMPLES::

            sage: R = Zp(5, print_mode=\'digits\', show_prec=False)
            sage: K = R.fraction_field(); K(1/3)
            31313131313131313132
            sage: L = R.fraction_field({\'max_ram_terms\':4}); L(1/3)
            doctest:warning
            ...
            DeprecationWarning: Use the change method if you want to change print options in fraction_field()
            See https://github.com/sagemath/sage/issues/23227 for details.
            3132
            sage: U.<a> = Zq(17^4, 6, print_mode=\'val-unit\', print_max_terse_terms=3)   # needs sage.libs.ntl
            sage: U.fraction_field()                                                    # needs sage.libs.ntl
            17-adic Unramified Extension Field in a defined by x^4 + 7*x^2 + 10*x + 3
            sage: U.fraction_field({"pos":False}) == U.fraction_field()                 # needs sage.libs.ntl
            False

        TESTS::

            sage: R = ZpLC(2); R
            doctest:...: FutureWarning: This class/method/function is marked as experimental. It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/23505 for details.
            2-adic Ring with lattice-cap precision
            sage: K = R.fraction_field(); K
            2-adic Field with lattice-cap precision

            sage: K = QpLC(2); K2 = K.fraction_field({\'mode\':\'terse\'})
            sage: K2 is K
            False
            sage: K = QpLC(2, label=\'test\'); K
            2-adic Field with lattice-cap precision (label: test)
            sage: K.fraction_field()
            2-adic Field with lattice-cap precision (label: test)
            sage: K.fraction_field({\'mode\':\'series\'}) is K
            True
        '''
    def integer_ring(self, print_mode=None):
        '''
        Return the ring of integers of this ring or field.

        For `\\QQ_p`, this is the `p`-adic ring with the same options,
        and for extensions, it is just the extension of the ring
        of integers of the base determined by the same polynomial.

        INPUT:

        - ``print_mode`` -- (optional) a dictionary containing print options;
          defaults to the same options as this ring

        OUTPUT: the ring of elements of this field with nonnegative valuation

        EXAMPLES::

            sage: K = Qp(5, print_mode=\'digits\', show_prec=False)
            sage: R = K.integer_ring(); R(1/3)
            31313131313131313132
            sage: S = K.integer_ring({\'max_ram_terms\':4}); S(1/3)
            doctest:warning
            ...
            DeprecationWarning: Use the change method if you want to change print options in integer_ring()
            See https://github.com/sagemath/sage/issues/23227 for details.
            3132
            sage: U.<a> = Qq(17^4, 6, print_mode=\'val-unit\', print_max_terse_terms=3)   # needs sage.libs.ntl
            sage: U.integer_ring()                                                      # needs sage.libs.ntl
            17-adic Unramified Extension Ring in a defined by x^4 + 7*x^2 + 10*x + 3
            sage: U.fraction_field({"print_mode":"terse"}) == U.fraction_field()        # needs sage.libs.ntl
            doctest:warning
            ...
            DeprecationWarning: Use the change method if you want to change print options in fraction_field()
            See https://github.com/sagemath/sage/issues/23227 for details.
            False

        TESTS::

            sage: K = QpLC(2); K
            2-adic Field with lattice-cap precision
            sage: R = K.integer_ring(); R
            2-adic Ring with lattice-cap precision

            sage: R = ZpLC(2); R2 = R.integer_ring({\'mode\':\'terse\'})
            sage: R2 is R
            False
            sage: R = ZpLC(2, label=\'test\'); R
            2-adic Ring with lattice-cap precision (label: test)
            sage: R.integer_ring()
            2-adic Ring with lattice-cap precision (label: test)
            sage: R.integer_ring({\'mode\':\'series\'}) is R
            True

        The `secure` attribute for relaxed type is preserved::

            sage: K = QpER(5, secure=True)                                              # needs sage.libs.flint
            sage: K.integer_ring().is_secure()
            True
        '''
    def teichmuller(self, x, prec=None):
        """
        Return the Teichmüller representative of ``x``.

        - ``x`` -- something that can be cast into ``self``

        OUTPUT: the Teichmüller lift of ``x``

        EXAMPLES::

            sage: R = Zp(5, 10, 'capped-rel', 'series')
            sage: R.teichmuller(2)
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)
            sage: R = Qp(5, 10,'capped-rel','series')
            sage: R.teichmuller(2)
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)
            sage: R = Zp(5, 10, 'capped-abs', 'series')
            sage: R.teichmuller(2)
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)
            sage: R = Zp(5, 10, 'fixed-mod', 'series')
            sage: R.teichmuller(2)
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 +125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W.teichmuller(3); y
            3 + 3*w^5 + w^7 + 2*w^9 + 2*w^10 + 4*w^11 + w^12 + 2*w^13 + 3*w^15
             + 2*w^16 + 3*w^17 + w^18 + 3*w^19 + 3*w^20 + 2*w^21 + 2*w^22
             + 3*w^23 + 4*w^24 + O(w^25)
            sage: y^5 == y
            True
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: b = A.teichmuller(1 + 2*a - a^2); b
            (4*a^2 + 2*a + 1) + 2*a*5 + (3*a^2 + 1)*5^2 + (a + 4)*5^3
             + (a^2 + a + 1)*5^4 + O(5^5)
            sage: b^125 == b
            True

        We check that :issue:`23736` is resolved::

            sage: # needs sage.libs.ntl
            sage: R.teichmuller(GF(5)(2))
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + O(5^5)

        AUTHORS:

        - Initial version: David Roe
        - Quadratic time version: Kiran Kedlaya <kedlaya@math.mit.edu> (2007-03-27)
        """
    def teichmuller_system(self):
        """
        Return a set of Teichmüller representatives for the invertible
        elements of `\\ZZ / p\\ZZ`.

        OUTPUT:

        A list of Teichmüller representatives for the invertible elements
        of `\\ZZ / p\\ZZ`.

        EXAMPLES::

            sage: R = Zp(3, 5,'fixed-mod', 'terse')
            sage: R.teichmuller_system()
            [1, 242]

        Check that :issue:`20457` is fixed::

            sage: F.<a> = Qq(5^2,6)                                                     # needs sage.libs.ntl
            sage: F.teichmuller_system()[3]                                             # needs sage.libs.ntl
            (2*a + 2) + (4*a + 1)*5 + 4*5^2 + (2*a + 1)*5^3 + (4*a + 1)*5^4 + (2*a + 3)*5^5 + O(5^6)

        .. NOTE::

            Should this return 0 as well?
        """
    def extension(self, modulus, prec=None, names=None, print_mode=None, implementation: str = 'FLINT', **kwds):
        """
        Create an extension of this `p`-adic ring.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: k = Qp(5)
            sage: R.<x> = k[]
            sage: l.<w> = k.extension(x^2 - 5); l
            5-adic Eisenstein Extension Field in w defined by x^2 - 5
            sage: F = list(Qp(19)['x'](cyclotomic_polynomial(5)).factor())[0][0]
            sage: L = Qp(19).extension(F, names='a'); L
            19-adic Unramified Extension Field in a defined by x^2 + 8751674996211859573806383*x + 1
        """
    def frobenius_endomorphism(self, n: int = 1):
        """
        Return the `n`-th power of the absolute arithmetic Frobeninus
        endomorphism on this field.

        INPUT:

        - ``n`` -- integer (default: 1)

        EXAMPLES::

            sage: K.<a> = Qq(3^5)                                                       # needs sage.libs.ntl
            sage: Frob = K.frobenius_endomorphism(); Frob                               # needs sage.libs.ntl
            Frobenius endomorphism on 3-adic Unramified Extension
            ... lifting a |--> a^3 on the residue field
            sage: Frob(a) == a.frobenius()                                              # needs sage.libs.ntl
            True

        We can specify a power::

            sage: K.frobenius_endomorphism(2)                                           # needs sage.libs.ntl
            Frobenius endomorphism on 3-adic Unramified Extension
            ... lifting a |--> a^(3^2) on the residue field

        The result is simplified if possible::

            sage: K.frobenius_endomorphism(6)                                           # needs sage.libs.ntl
            Frobenius endomorphism on 3-adic Unramified Extension
            ... lifting a |--> a^3 on the residue field
            sage: K.frobenius_endomorphism(5)                                           # needs sage.libs.ntl
            Identity endomorphism of 3-adic Unramified Extension ...

        Comparisons work::

            sage: K.frobenius_endomorphism(6) == Frob                                   # needs sage.libs.ntl
            True
        """
    def valuation(self):
        """
        Return the `p`-adic valuation on this ring.

        OUTPUT:

        A valuation that is normalized such that the rational prime `p` has
        valuation 1.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K = Qp(3)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^3 - 3)
            sage: v = L.valuation(); v
            3-adic valuation
            sage: v(3)
            1
            sage: L(3).valuation()
            3

        The normalization is chosen such that the valuation restricts to the
        valuation on the base ring::

            sage: v(3) == K.valuation()(3)                                              # needs sage.libs.ntl
            True
            sage: v.restriction(K) == K.valuation()                                     # needs sage.libs.ntl
            True

        .. SEEALSO::

            :meth:`NumberField_generic.valuation() <sage.rings.number_field.number_field.NumberField_generic.valuation>`,
            :meth:`Order.valuation() <sage.rings.number_field.order.Order.valuation>`
        """
    def primitive_root_of_unity(self, n=None, order: bool = False):
        """
        Return a generator of the group of ``n``-th roots of unity
        in this ring.

        INPUT:

        - ``n`` -- integer or ``None`` (default: ``None``)

        - ``order`` -- boolean (default: ``False``)

        OUTPUT:

        A generator of the group of ``n``-th roots of unity.
        If ``n`` is ``None``, a generator of the full group of roots
        of unity is returned.

        If ``order`` is ``True``, the order of the above group is
        returned as well.

        EXAMPLES::

            sage: R = Zp(5, 10)
            sage: zeta = R.primitive_root_of_unity(); zeta
            2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)
            sage: zeta == R.teichmuller(2)
            True

        Now we consider an example with non trivial ``p``-th roots of unity::

            sage: # needs sage.libs.ntl
            sage: W = Zp(3, 2)
            sage: S.<x> = W[]
            sage: R.<pi> = W.extension((x+1)^6 + (x+1)^3 + 1)
            sage: zeta, order = R.primitive_root_of_unity(order=True)
            sage: zeta
            2 + 2*pi + 2*pi^3 + 2*pi^7 + 2*pi^8 + 2*pi^9 + pi^11 + O(pi^12)
            sage: order
            18
            sage: zeta.multiplicative_order()
            18
            sage: zeta, order = R.primitive_root_of_unity(24, order=True)
            sage: zeta
            2 + pi^3 + 2*pi^7 + 2*pi^8 + 2*pi^10 + 2*pi^11 + O(pi^12)
            sage: order   # equal to gcd(18,24)
            6
            sage: zeta.multiplicative_order()
            6
        """
    def roots_of_unity(self, n=None):
        """
        Return all the ``n``-th roots of unity in this ring.

        INPUT:

        - ``n`` -- integer or ``None`` (default: ``None``); if
          ``None``, the full group of roots of unity is returned

        EXAMPLES::

            sage: R = Zp(5, 10)
            sage: roots = R.roots_of_unity(); roots
            [1 + O(5^10),
             2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10),
             4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10),
             3 + 3*5 + 2*5^2 + 3*5^3 + 5^4 + 2*5^6 + 5^7 + 4*5^8 + 5^9 + O(5^10)]

            sage: R.roots_of_unity(10)
            [1 + O(5^10),
             4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10)]

        In this case, the roots of unity are the Teichmüller representatives::

            sage: R.teichmuller_system()
            [1 + O(5^10),
             2 + 5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10),
             3 + 3*5 + 2*5^2 + 3*5^3 + 5^4 + 2*5^6 + 5^7 + 4*5^8 + 5^9 + O(5^10),
             4 + 4*5 + 4*5^2 + 4*5^3 + 4*5^4 + 4*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10)]

        In general, there might be more roots of unity (it happens when the ring has non
        trivial ``p``-th roots of unity)::

            sage: # needs sage.libs.ntl
            sage: W.<a> = Zq(3^2, 2)
            sage: S.<x> = W[]
            sage: R.<pi> = W.extension((x+1)^2 + (x+1) + 1)
            sage: roots = R.roots_of_unity(); roots
            [1 + O(pi^4),
             a + 2*a*pi + 2*a*pi^2 + a*pi^3 + O(pi^4),
             ...
             1 + pi + O(pi^4),
             a + a*pi^2 + 2*a*pi^3 + O(pi^4),
             ...
             1 + 2*pi + pi^2 + O(pi^4),
             a + a*pi + a*pi^2 + O(pi^4),
             ...]
            sage: len(roots)
            24

        We check that the logarithm of each root of unity vanishes::

            sage: # needs sage.libs.ntl
            sage: for root in roots:
            ....:     if root.log() != 0:
            ....:         raise ValueError
        """

class ResidueReductionMap(Morphism):
    """
    Reduction map from a `p`-adic ring or field to its residue field or ring.

    These maps must be created using the :meth:`_create_` method in order
    to support categories correctly.

    EXAMPLES::

        sage: from sage.rings.padics.padic_generic import ResidueReductionMap
        sage: R.<a> = Zq(125); k = R.residue_field()                                    # needs sage.libs.ntl
        sage: f = ResidueReductionMap._create_(R, k); f                                 # needs sage.libs.ntl
        Reduction morphism:
          From: 5-adic Unramified Extension Ring in a defined by x^3 + 3*x + 3
          To:   Finite Field in a0 of size 5^3
    """
    def is_surjective(self):
        """
        The reduction map is surjective.

        EXAMPLES::

            sage: GF(7).convert_map_from(Qp(7)).is_surjective()                         # needs sage.rings.finite_rings
            True
        """
    def is_injective(self):
        """
        The reduction map is far from injective.

        EXAMPLES::

            sage: GF(5).convert_map_from(ZpCA(5)).is_injective()                        # needs sage.rings.finite_rings
            False
        """
    def section(self):
        """
        Return the section from the residue ring or field
        back to the `p`-adic ring or field.

        EXAMPLES::

            sage: GF(3).convert_map_from(Zp(3)).section()                               # needs sage.rings.finite_rings
            Lifting morphism:
              From: Finite Field of size 3
              To:   3-adic Ring with capped relative precision 20
        """

class ResidueLiftingMap(Morphism):
    """
    Lifting map to a `p`-adic ring or field from its residue field or ring.

    These maps must be created using the :meth:`_create_` method in order
    to support categories correctly.

    EXAMPLES::

        sage: from sage.rings.padics.padic_generic import ResidueLiftingMap
        sage: R.<a> = Zq(125); k = R.residue_field()                                    # needs sage.libs.ntl
        sage: f = ResidueLiftingMap._create_(k, R); f                                   # needs sage.libs.ntl
        Lifting morphism:
          From: Finite Field in a0 of size 5^3
          To:   5-adic Unramified Extension Ring in a defined by x^3 + 3*x + 3
    """

def local_print_mode(obj, print_options, pos=None, ram_name=None):
    """
    Context manager for safely temporarily changing the print_mode
    of a `p`-adic ring/field.

    EXAMPLES::

        sage: R = Zp(5)
        sage: R(45)
        4*5 + 5^2 + O(5^21)
        sage: with local_print_mode(R, 'val-unit'):
        ....:     print(R(45))
        5 * 9 + O(5^21)

    .. NOTE::

        For more documentation see :class:`sage.structure.parent_gens.localvars`.
    """
