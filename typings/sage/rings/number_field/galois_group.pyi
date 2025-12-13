from sage.groups.galois_group_perm import GaloisGroup_perm as GaloisGroup_perm, GaloisSubgroup_perm as GaloisSubgroup_perm
from sage.groups.perm_gps.permgroup import standardize_generator as standardize_generator
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.libs.pari import pari as pari
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.superseded import deprecation as deprecation
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.morphism import NumberFieldHomomorphism_im_gens as NumberFieldHomomorphism_im_gens
from sage.rings.number_field.number_field import refine_embedding as refine_embedding
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class GaloisGroup_v1(SageObject):
    '''
    A wrapper around a class representing an abstract transitive group.

    This is just a fairly minimal object at present.  To get the underlying
    group, do ``G.group()``, and to get the corresponding number field do
    ``G.number_field()``. For a more sophisticated interface use the
    ``type=None`` option.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
        sage: K = QQ[2^(1/3)]
        sage: pK = K.absolute_polynomial()
        sage: G = GaloisGroup_v1(pK.galois_group(pari_group=True), K); G
        ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
        See https://github.com/sagemath/sage/issues/28782 for details.
        Galois group PARI group [6, -1, 2, "S3"] of degree 3 of the
         Number Field in a with defining polynomial x^3 - 2 with a = 1.259921049894873?
        sage: G.order()
        6
        sage: G.group()
        PARI group [6, -1, 2, "S3"] of degree 3
        sage: G.number_field()
        Number Field in a with defining polynomial x^3 - 2 with a = 1.259921049894873?
    '''
    def __init__(self, group, number_field) -> None:
        '''
        Create a Galois group.

        EXAMPLES::

            sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
            sage: x = polygen(ZZ, \'x\')
            sage: K = NumberField([x^2 + 1, x^2 + 2],\'a\')
            sage: GaloisGroup_v1(K.absolute_polynomial().galois_group(pari_group=True), K)
            ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
            See https://github.com/sagemath/sage/issues/28782 for details.
            Galois group PARI group [4, 1, 2, "E(4) = 2[x]2"] of degree 4 of the
             Number Field in a0 with defining polynomial x^2 + 1 over its base field

        TESTS::

            sage: x = polygen(ZZ, \'x\')
            sage: G = NumberField(x^3 + 2, \'alpha\').galois_group(names=\'beta\'); G
            Galois group 3T2 (S3) with order 6 of x^3 + 2
            sage: G == loads(dumps(G))
            True
        '''
    def __eq__(self, other):
        """
        Compare two number field Galois groups.

        First the number fields are compared, then the Galois groups
        if the number fields are equal.  (Of course, if the number
        fields are the same, the Galois groups are automatically
        equal.)

        EXAMPLES::

            sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 + 2, 'alpha')
            sage: G = GaloisGroup_v1(K.absolute_polynomial().galois_group(pari_group=True), K)
            ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
            See https://github.com/sagemath/sage/issues/28782 for details.

            sage: # needs sage.symbolic
            sage: L = QQ[sqrt(2)]
            sage: H = GaloisGroup_v1(L.absolute_polynomial().galois_group(pari_group=True), L)
            sage: H == G
            False
            sage: H == H
            True
            sage: G == G
            True
        """
    def __ne__(self, other):
        """
        Test for unequality.

        EXAMPLES::

            sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 + 2, 'alpha')
            sage: G = GaloisGroup_v1(K.absolute_polynomial().galois_group(pari_group=True), K)
            ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
            See https://github.com/sagemath/sage/issues/28782 for details.

            sage: # needs sage.symbolic
            sage: L = QQ[sqrt(2)]
            sage: H = GaloisGroup_v1(L.absolute_polynomial().galois_group(pari_group=True), L)
            sage: H != G
            True
            sage: H != H
            False
            sage: G != G
            False
        """
    def group(self):
        '''
        Return the underlying abstract group.

        EXAMPLES::

            sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
            sage: x = polygen(ZZ, \'x\')
            sage: K = NumberField(x^3 + 2*x + 2, \'theta\')
            sage: G = GaloisGroup_v1(K.absolute_polynomial().galois_group(pari_group=True), K)
            ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
            See https://github.com/sagemath/sage/issues/28782 for details.
            sage: H = G.group(); H
            PARI group [6, -1, 2, "S3"] of degree 3
            sage: P = H.permutation_group(); P
            Transitive group number 2 of degree 3
            sage: sorted(P)
            [(), (2,3), (1,2), (1,2,3), (1,3,2), (1,3)]
        '''
    def order(self):
        '''
        Return the order of this Galois group.

        EXAMPLES::

            sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
            sage: x = polygen(ZZ, \'x\')
            sage: K = NumberField(x^5 + 2, \'theta_1\')
            sage: G = GaloisGroup_v1(K.absolute_polynomial().galois_group(pari_group=True), K); G
            ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
            See https://github.com/sagemath/sage/issues/28782 for details.
            Galois group PARI group [20, -1, 3, "F(5) = 5:4"] of degree 5 of the
             Number Field in theta_1 with defining polynomial x^5 + 2
            sage: G.order()
            20
        '''
    def number_field(self):
        '''
        Return the number field of which this is the Galois group.

        EXAMPLES::

            sage: from sage.rings.number_field.galois_group import GaloisGroup_v1
            sage: x = polygen(ZZ, \'x\')
            sage: K = NumberField(x^6 + 2, \'t\')
            sage: G = GaloisGroup_v1(K.absolute_polynomial().galois_group(pari_group=True), K); G
            ...DeprecationWarning: GaloisGroup_v1 is deprecated; please use GaloisGroup_v2
            See https://github.com/sagemath/sage/issues/28782 for details.
            Galois group PARI group [12, -1, 3, "D(6) = S(3)[x]2"] of degree 6 of the
             Number Field in t with defining polynomial x^6 + 2
            sage: G.number_field()
            Number Field in t with defining polynomial x^6 + 2
        '''

class GaloisGroup_v2(GaloisGroup_perm):
    """
    The Galois group of an (absolute) number field.

    .. NOTE::

        We define the Galois group of a non-normal field `K` to be the
        Galois group of its Galois closure `L`, and elements are stored as
        permutations of the roots of the defining polynomial of `L`, *not* as
        permutations of the roots (in `L`) of the defining polynomial of `K`. The
        latter would probably be preferable, but is harder to implement. Thus
        the permutation group that is returned is always simply-transitive.

        The 'arithmetical' features (decomposition and ramification groups,
        Artin symbols etc) are only available for Galois fields.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: G = NumberField(x^3 - x - 1, 'a').galois_closure('b').galois_group()
        sage: G.subgroup([G([(1,2,3),(4,5,6)])])
        Subgroup generated by [(1,2,3)(4,5,6)] of
         (Galois group 6T2 ([3]2) with order 6 of x^6 - 6*x^4 + 9*x^2 + 23)

    Subgroups can be specified using generators (:issue:`26816`)::

        sage: K.<a> = NumberField(x^6 - 6*x^4 + 9*x^2 + 23)
        sage: G = K.galois_group()
        sage: list(G)
        [(),
         (1,2,3)(4,5,6),
         (1,3,2)(4,6,5),
         (1,4)(2,6)(3,5),
         (1,5)(2,4)(3,6),
         (1,6)(2,5)(3,4)]
        sage: g = G[1]
        sage: h = G[3]
        sage: list(G.subgroup([]))
        [()]
        sage: list(G.subgroup([g]))
        [(), (1,2,3)(4,5,6), (1,3,2)(4,6,5)]
        sage: list(G.subgroup([h]))
        [(), (1,4)(2,6)(3,5)]
        sage: sorted(G.subgroup([g,h])) == sorted(G)
        True
    """
    def __init__(self, number_field, algorithm: str = 'pari', names=None, gc_numbering=None, _type=None) -> None:
        """
        Create a Galois group.

        EXAMPLES::

            sage: QuadraticField(-23,'a').galois_group()
            Galois group 2T1 (S2) with order 2 of x^2 + 23

        You can specify the variable name for the Galois closure::

            sage: x = polygen(ZZ, 'x')
            sage: G = NumberField(x^3 - 2, 'b').galois_group(names='c'); G
            Galois group 3T2 (S3) with order 6 of x^3 - 2
            sage: G._galois_closure
            Number Field in c with defining polynomial x^6 + 108

        Or have one chosen automatically (``c`` is appended to the variable name)::

            sage: G = NumberField(x^3 - 2, 'b').galois_group()
            sage: G._galois_closure
            Number Field in bc with defining polynomial x^6 + 108

        TESTS::

            sage: F.<z> = CyclotomicField(7)
            sage: G = F.galois_group()

        We test that a method inherited from PermutationGroup_generic returns
        the right type of element (see :issue:`133`)::

            sage: phi = G.random_element()
            sage: type(phi) is G.element_class
            True
            sage: phi(z) # random
            z^3
        """
    def group(self):
        '''
        While :class:`GaloisGroup_v1` is being deprecated, this provides public access to the PARI/GAP group
        in order to keep all aspects of that API.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: x = polygen(ZZ, \'x\')
            sage: K.<a> = NumberField(x^3 + 2*x + 2)
            sage: G = K.galois_group(type=\'pari\')
            ...DeprecationWarning: the different Galois types have been merged into one class
            See https://github.com/sagemath/sage/issues/28782 for details.
            sage: G.group()
            ...DeprecationWarning: the group method is deprecated;
            you can use _pol_galgp if you really need it
            See https://github.com/sagemath/sage/issues/28782 for details.
            PARI group [6, -1, 2, "S3"] of degree 3
        '''
    def order(self, algorithm=None, recompute: bool = False):
        """
        Return the order of this Galois group.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2*x + 2)
            sage: G = K.galois_group()
            sage: G.order()
            6
        """
    def easy_order(self, algorithm=None):
        """
        Return the order of this Galois group if it's quick to compute.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2*x + 2)
            sage: G = K.galois_group()
            sage: G.easy_order()
            6
            sage: x = polygen(ZZ, 'x')
            sage: L.<b> = NumberField(x^72 + 2*x + 2)
            sage: H = L.galois_group()
            sage: H.easy_order()
        """
    def transitive_number(self, algorithm=None, recompute: bool = False):
        """
        Regardless of the value of ``gc_numbering``, give the transitive number
        for the action on the roots of the defining polynomial of the original number field,
        not the Galois closure.

        INPUT:

        - ``algorithm`` -- string, specify the algorithm to be used
        - ``recompute`` -- boolean, whether to recompute the result even if known by another algorithm

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2*x + 2)
            sage: G = K.galois_group()
            sage: G.transitive_number()
            2
            sage: x = polygen(ZZ, 'x')
            sage: L.<b> = NumberField(x^13 + 2*x + 2)
            sage: H = L.galois_group(algorithm='gap')
            sage: H.transitive_number() # optional - gap_packages
            9
        """
    def pari_label(self):
        """
        Return the label assigned by PARI for this Galois group, an attempt at giving a human readable description of the group.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^8 - x^5 + x^4 - x^3 + 1)
            sage: G = K.galois_group()
            sage: G.transitive_label()
            '8T44'
            sage: G.pari_label()
            '[2^4]S(4)'
        """
    @cached_method
    def signature(self):
        """
        Return `1` if contained in the alternating group, `-1` otherwise.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: K.galois_group().signature()
            -1
            sage: K.<a> = NumberField(x^3 - 3*x - 1)
            sage: K.galois_group().signature()
            1
        """
    def is_galois(self):
        """
        Whether the underlying number field is Galois.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: NumberField(x^3 - x + 1,'a').galois_group(names='b').is_galois()
            False
            sage: NumberField(x^2 - x + 1,'a').galois_group().is_galois()
            True
        """
    def number_field(self):
        """
        The ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 - x + 1, 'a')
            sage: K.galois_group(names='b').number_field() is K
            True
        """
    def list(self):
        """
        List of the elements of ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: NumberField(x^3 - 3*x + 1,'a').galois_group().list()
            [(), (1,2,3), (1,3,2)]
        """
    def unrank(self, i):
        """
        Return the `i`-th element of ``self``.

        INPUT:

        - ``i`` -- integer between `0` and `n-1` where
          `n` is the cardinality of this set

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: G = NumberField(x^3 - 3*x + 1,'a').galois_group()
            sage: [G.unrank(i) for i in range(G.cardinality())]
            [(), (1,2,3), (1,3,2)]

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: G = NumberField(x^3 - 3*x + 1,'a').galois_group()
            sage: L = [G.unrank(i) for i in range(G.cardinality())]
            sage: L == G.list()
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: G = NumberField(x^3 - 3*x + 1,'a').galois_group()
            sage: list(G) == G.list()
            True
        """
    def decomposition_group(self, P):
        """
        Decomposition group of a prime ideal `P`, i.e., the subgroup of elements
        that map `P` to itself. This is the same as the Galois group of the
        extension of local fields obtained by completing at `P`.

        This function will raise an error if `P` is not prime or the given number
        field is not Galois.

        `P` can also be an infinite prime, i.e., an embedding into `\\RR` or `\\CC`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 - 2*x^2 + 2, 'b').galois_closure()
            sage: P = K.ideal([17, a^2])
            sage: G = K.galois_group()
            sage: G.decomposition_group(P)
            Subgroup generated by [(1,8)(2,7)(3,6)(4,5)] of
             (Galois group 8T4 ([4]2) with order 8 of x^8 - 20*x^6 + 104*x^4 - 40*x^2 + 1156)
            sage: G.decomposition_group(P^2)
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (...) is not a prime ideal
            sage: G.decomposition_group(17)
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (17) is not a prime ideal

        An example with an infinite place::

            sage: x = polygen(ZZ, 'x')
            sage: L.<b> = NumberField(x^3 - 2,'a').galois_closure(); G = L.galois_group()
            sage: x = L.places()[0]
            sage: G.decomposition_group(x).order()
            2
        """
    def complex_conjugation(self, P=None):
        '''
        Return the unique element of ``self`` corresponding to complex conjugation,
        for a specified embedding `P` into the complex numbers. If `P` is not
        specified, use the "standard" embedding, whenever that is well-defined.

        EXAMPLES::

            sage: L.<z> = CyclotomicField(7)
            sage: G = L.galois_group()
            sage: conj = G.complex_conjugation(); conj
            (1,4)(2,5)(3,6)
            sage: conj(z)
            -z^5 - z^4 - z^3 - z^2 - z - 1

        An example where the field is not CM, so complex conjugation really
        depends on the choice of embedding::

            sage: x = polygen(ZZ, \'x\')
            sage: L = NumberField(x^6 + 40*x^3 + 1372, \'a\')
            sage: G = L.galois_group()
            sage: [G.complex_conjugation(x) for x in L.places()]
            [(1,3)(2,6)(4,5), (1,5)(2,4)(3,6), (1,2)(3,4)(5,6)]
        '''
    def ramification_group(self, P, v):
        """
        Return the `v`-th ramification group of ``self`` for the prime `P`, i.e., the set
        of elements `s` of ``self`` such that `s` acts trivially modulo `P^{(v+1)}`. This
        is only defined for Galois fields.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^3 - 3, 'a').galois_closure()
            sage: G=K.galois_group()
            sage: P = K.primes_above(3)[0]
            sage: G.ramification_group(P, 3)
            Subgroup generated by [(1,2,4)(3,5,6)] of
             (Galois group 6T2 ([3]2) with order 6 of x^6 + 243)
            sage: G.ramification_group(P, 5)
            Subgroup generated by [()] of (Galois group 6T2 ([3]2) with order 6 of x^6 + 243)
        """
    def inertia_group(self, P):
        """
        Return the inertia group of the prime `P`, i.e., the group of elements acting
        trivially modulo `P`. This is just the 0th ramification group of `P`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^2 - 3, 'a')
            sage: G = K.galois_group()
            sage: G.inertia_group(K.primes_above(2)[0])
            Subgroup generated by [(1,2)] of (Galois group 2T1 (S2) with order 2 of x^2 - 3)
            sage: G.inertia_group(K.primes_above(5)[0])
            Subgroup generated by [()] of (Galois group 2T1 (S2) with order 2 of x^2 - 3)
        """
    def ramification_breaks(self, P):
        """
        Return the set of ramification breaks of the prime ideal `P`, i.e., the
        set of indices `i` such that the ramification group `G_{i+1} \\ne G_{i}`.
        This is only defined for Galois fields.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^8 - 20*x^6 + 104*x^4 - 40*x^2 + 1156)
            sage: G = K.galois_group()
            sage: P = K.primes_above(2)[0]
            sage: G.ramification_breaks(P)
            {1, 3, 5}
            sage: min(G.ramification_group(P, i).order()
            ....:         / G.ramification_group(P, i + 1).order()
            ....:     for i in G.ramification_breaks(P))
            2
        """
    def artin_symbol(self, P):
        """
        Return the Artin symbol `\\left(\\frac{K /
        \\QQ}{\\mathfrak{P}}\\right)`, where `K` is the number field of ``self``,
        and `\\mathfrak{P}` is an unramified prime ideal. This is the unique
        element `s` of the decomposition group of `\\mathfrak{P}` such that `s(x) = x^p \\bmod
        \\mathfrak{P}`, where `p` is the residue characteristic of `\\mathfrak{P}`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^4 - 2*x^2 + 2, 'a').galois_closure()
            sage: G = K.galois_group()
            sage: sorted([G.artin_symbol(P) for P in K.primes_above(7)])  # random (see remark in primes_above)
            [(1,4)(2,3)(5,8)(6,7),
             (1,4)(2,3)(5,8)(6,7),
             (1,5)(2,6)(3,7)(4,8),
             (1,5)(2,6)(3,7)(4,8)]
            sage: G.artin_symbol(17)
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (17) is not prime
            sage: QuadraticField(-7,'c').galois_group().artin_symbol(13)
            (1,2)
            sage: G.artin_symbol(K.primes_above(2)[0])
            Traceback (most recent call last):
            ...
            ValueError: Fractional ideal (...) is ramified
        """

class GaloisGroup_subgroup(GaloisSubgroup_perm):
    """
    A subgroup of a Galois group, as returned by functions such as
    ``decomposition_group``.

    INPUT:

    - ``ambient`` -- the ambient Galois group

    - ``gens`` -- list of generators for the group

    - ``gap_group`` -- a gap or libgap permutation group, or a string
        defining one (default: ``None``)

    - ``domain`` -- set on which this permutation group acts; extracted from
      ``ambient`` if not specified

    - ``category`` -- the category for this object

    - ``canonicalize`` -- if ``True``, sorts and removes duplicates

    - ``check`` -- whether to check that generators actually lie in the
      ambient group

    EXAMPLES::

        sage: from sage.rings.number_field.galois_group import GaloisGroup_subgroup
            sage: x = polygen(ZZ, 'x')
        sage: G = NumberField(x^3 - x - 1, 'a').galois_closure('b').galois_group()
        sage: GaloisGroup_subgroup( G, [G([(1,2,3),(4,5,6)])])
        Subgroup generated by [(1,2,3)(4,5,6)] of
         (Galois group 6T2 ([3]2) with order 6 of x^6 - 6*x^4 + 9*x^2 + 23)

        sage: K.<a> = NumberField(x^6 - 3*x^2 - 1)
        sage: L.<b> = K.galois_closure()
        sage: G = L.galois_group()
        sage: P = L.primes_above(3)[0]
        sage: H = G.decomposition_group(P)
        sage: H.order()
        3

        sage: G = NumberField(x^3 - x - 1, 'a').galois_closure('b').galois_group()
        sage: H = G.subgroup([G([(1,2,3),(4,5,6)])])
        sage: H
        Subgroup generated by [(1,2,3)(4,5,6)] of
         (Galois group 6T2 ([3]2) with order 6 of x^6 - 6*x^4 + 9*x^2 + 23)

    TESTS:

    Check that :issue:`17664` is fixed::

        sage: L.<c> = QuadraticField(-1)
        sage: P = L.primes_above(5)[0]
        sage: G = L.galois_group()
        sage: H = G.decomposition_group(P)
        sage: H.domain()
        {1, 2}
        sage: G.artin_symbol(P)
        ()
    """
    def fixed_field(self, name=None, polred=None, threshold=None):
        """
        Return the fixed field of this subgroup (as a subfield of the Galois
        closure of the number field associated to the ambient Galois group).

        INPUT:

        - ``name`` -- a variable name for the new field

        - ``polred`` -- whether to optimize the generator of the newly created field
            for a simpler polynomial, using PARI's :pari:`polredbest`.
            Defaults to ``True`` when the degree of the fixed field is at most 8.

        - ``threshold`` -- positive number; polred only performed if the cost is at most this threshold

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a> = NumberField(x^4 + 1)
            sage: G = L.galois_group()
            sage: H = G.decomposition_group(L.primes_above(3)[0])
            sage: H.fixed_field()
            (Number Field in a0 with defining polynomial x^2 + 2 with a0 = a^3 + a,
             Ring morphism:
               From: Number Field in a0 with defining polynomial x^2 + 2 with a0 = a^3 + a
               To:   Number Field in a with defining polynomial x^4 + 1
               Defn: a0 |--> a^3 + a)

        You can use the ``polred`` option to get a simpler defining polynomial::

            sage: K.<a> = NumberField(x^5 - 5*x^2 - 3)
            sage: G = K.galois_group(); G
            Galois group 5T2 (5:2) with order 10 of x^5 - 5*x^2 - 3
            sage: sigma, tau = G.gens()
            sage: H = G.subgroup([tau])
            sage: H.fixed_field(polred=False)
            (Number Field in a0 with defining polynomial x^2 + 84375
              with a0 = 5*ac^5 + 25*ac^3,
             Ring morphism:
               From: Number Field in a0 with defining polynomial x^2 + 84375
                     with a0 = 5*ac^5 + 25*ac^3
               To:   Number Field in ac with defining polynomial x^10 + 10*x^8 + 25*x^6 + 3375
               Defn: a0 |--> 5*ac^5 + 25*ac^3)
            sage: H.fixed_field(polred=True)
            (Number Field in a0 with defining polynomial x^2 - x + 4
              with a0 = -1/30*ac^5 - 1/6*ac^3 + 1/2,
             Ring morphism:
               From: Number Field in a0 with defining polynomial x^2 - x + 4
                     with a0 = -1/30*ac^5 - 1/6*ac^3 + 1/2
               To:   Number Field in ac with defining polynomial x^10 + 10*x^8 + 25*x^6 + 3375
               Defn: a0 |--> -1/30*ac^5 - 1/6*ac^3 + 1/2)
            sage: G.splitting_field()
            Number Field in ac with defining polynomial x^10 + 10*x^8 + 25*x^6 + 3375

        An embedding is returned also if the subgroup is trivial
        (:issue:`26817`)::

            sage: H = G.subgroup([])
            sage: H.fixed_field()
            (Number Field in ac with defining polynomial x^10 + 10*x^8 + 25*x^6 + 3375,
             Identity endomorphism of
              Number Field in ac with defining polynomial x^10 + 10*x^8 + 25*x^6 + 3375)
        """

class GaloisGroupElement(PermutationGroupElement):
    """
    An element of a Galois group. This is stored as a permutation, but may also
    be made to act on elements of the field (generally returning elements of
    its Galois closure).

    EXAMPLES::

        sage: K.<w> = QuadraticField(-7); G = K.galois_group()
        sage: G[1]
        (1,2)
        sage: G[1](w + 2)
        -w + 2

        sage: x = polygen(ZZ, 'x')
        sage: L.<v> = NumberField(x^3 - 2); G = L.galois_group(names='y')
        sage: G[4]
        (1,5)(2,4)(3,6)
        sage: G[4](v)
        1/18*y^4
        sage: G[4](G[4](v))
        -1/36*y^4 - 1/2*y
        sage: G[4](G[4](G[4](v)))
        1/18*y^4
    """
    @cached_method
    def as_hom(self):
        """
        Return the homomorphism `L \\to L` corresponding to ``self``, where `L` is the
        Galois closure of the ambient number field.

        EXAMPLES::

            sage: G = QuadraticField(-7,'w').galois_group()
            sage: G[1].as_hom()
            Ring endomorphism of Number Field in w with defining polynomial x^2 + 7
             with w = 2.645751311064591?*I
              Defn: w |--> -w

        TESTS:

        Number fields defined by non-monic and non-integral
        polynomials are supported (:issue:`252`)::

            sage: R.<x> = QQ[]
            sage: x = polygen(ZZ, 'x')
            sage: f = 7/9*x^3 + 7/3*x^2 - 56*x + 123
            sage: K.<a> = NumberField(f)
            sage: G = K.galois_group()
            sage: G[1].as_hom()
            Ring endomorphism of Number Field in a with defining polynomial 7/9*x^3 + 7/3*x^2 - 56*x + 123
              Defn: a |--> -7/15*a^2 - 18/5*a + 96/5
            sage: prod(x - sigma(a) for sigma in G) == f.monic()
            True
        """
    def __call__(self, x):
        """
        Return the action of ``self`` on an element x in the number field of
        ``self`` (or its Galois closure).

        EXAMPLES::

            sage: K.<w> = QuadraticField(-7)
            sage: f = K.galois_group()[1]
            sage: f(w)
            -w
        """
    def ramification_degree(self, P):
        """
        Return the greatest value of `v` such that `s` acts trivially modulo `P^v`.
        Should only be used if `P` is prime and `s` is in the decomposition group of `P`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^3 - 3, 'a').galois_closure()
            sage: G = K.galois_group()
            sage: P = K.primes_above(3)[0]
            sage: s = hom(K, K, 1/18*b^4 - 1/2*b)
            sage: G(s).ramification_degree(P)
            4
        """
GaloisGroup = GaloisGroup_v1
