from sage.arith.functions import lcm as lcm
from sage.arith.misc import binomial as binomial, factorial as factorial, prime_divisors as prime_divisors
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.verbose import verbose as verbose
from sage.modular.modsym.p1list import P1List as P1List
from sage.quadratic_forms.binary_qf import BinaryQF as BinaryQF, BinaryQF_reduced_representatives as BinaryQF_reduced_representatives
from sage.rings.factorint import factor_trial_division as factor_trial_division
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_element_base import NumberFieldElement_base as NumberFieldElement_base
from sage.rings.rational_field import QQ as QQ
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal
from sage.structure.sage_object import SageObject as SageObject

def heegner_points(N, D=None, c=None):
    """
    Return all Heegner points of given level `N`.  Can also restrict
    to Heegner points with specified discriminant `D` and optionally
    conductor `c`.

    INPUT:

    - ``N`` -- level (positive integer)

    - ``D`` -- discriminant (negative integer)

    - ``c`` -- conductor (positive integer)

    EXAMPLES::

        sage: heegner_points(389, -7)
        Set of all Heegner points on X_0(389) associated to QQ[sqrt(-7)]
        sage: heegner_points(389, -7, 1)
        All Heegner points of conductor 1 on X_0(389) associated to QQ[sqrt(-7)]
        sage: heegner_points(389, -7, 5)
        All Heegner points of conductor 5 on X_0(389) associated to QQ[sqrt(-7)]
    """
def heegner_point(N, D=None, c: int = 1):
    """
    Return a specific Heegner point of level `N` with given
    discriminant and conductor.  If `D` is not specified, then the
    first valid Heegner discriminant is used.  If `c` is not given,
    then `c=1` is used.

    INPUT:

    - ``N`` -- level (positive integer)

    - ``D`` -- discriminant (optional: default first valid `D`)

    - ``c`` -- conductor (positive integer, default: 1)

    EXAMPLES::

        sage: heegner_point(389)
        Heegner point 1/778*sqrt(-7) - 185/778 of discriminant -7 on X_0(389)
        sage: heegner_point(389,-7)
        Heegner point 1/778*sqrt(-7) - 185/778 of discriminant -7 on X_0(389)
        sage: heegner_point(389,-7,5)
        Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7 and conductor 5 on X_0(389)
        sage: heegner_point(389,-20)
        Heegner point 1/778*sqrt(-20) - 165/389 of discriminant -20 on X_0(389)
    """

class RingClassField(SageObject):
    """
    A Ring class field of a quadratic imaginary field of given conductor.

    .. NOTE::

        This is a *ring* class field, not a ray class field. In
        general, the ring class field of given conductor is a subfield
        of the ray class field of the same conductor.

    EXAMPLES::

        sage: heegner_point(37,-7).ring_class_field()
        Hilbert class field of QQ[sqrt(-7)]
        sage: heegner_point(37,-7,5).ring_class_field()
        Ring class field extension of QQ[sqrt(-7)] of conductor 5
        sage: heegner_point(37,-7,55).ring_class_field()
        Ring class field extension of QQ[sqrt(-7)] of conductor 55

    TESTS::

        sage: K_c = heegner_point(37,-7).ring_class_field()
        sage: type(K_c)
        <class 'sage.schemes.elliptic_curves.heegner.RingClassField'>
        sage: loads(dumps(K_c)) == K_c
        True
    """
    def __init__(self, D, c, check: bool = True) -> None:
        """
        INPUT:

        - ``D`` -- discriminant of quadratic imaginary field

        - ``c`` -- conductor (positive integer coprime to `D`)

        - ``check`` -- boolean (default: ``True``); whether to check
          validity of input

        EXAMPLES::

            sage: sage.schemes.elliptic_curves.heegner.RingClassField(-7, 5, False)
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """
    def __eq__(self, other):
        """
        Used for equality testing.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: K5 = E.heegner_point(-7,5).ring_class_field()
            sage: K11 = E.heegner_point(-7,11).ring_class_field()
            sage: K5 == K11
            False
            sage: K5 == K5
            True
            sage: K11 == 11
            False
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: K5 = E.heegner_point(-7,5).ring_class_field()
            sage: K11 = E.heegner_point(-7,11).ring_class_field()
            sage: K5 != K11
            True
            sage: K5 != K5
            False
            sage: K11 != 11
            True
        """
    def __hash__(self):
        """
        Used for computing hash of ``self``.

        .. NOTE::

            The hash is equal to the hash of the pair
            ``(discriminant, conductor)``.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K5 = E.heegner_point(-7,5).ring_class_field()
            sage: hash(K5) == hash((-7,5))
            True
        """
    def conductor(self):
        """
        Return the conductor of this ring class field.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K5 = E.heegner_point(-7,5).ring_class_field()
            sage: K5.conductor()
            5
        """
    def discriminant_of_K(self):
        """
        Return the discriminant of the quadratic imaginary field `K` contained in ``self``.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K5 = E.heegner_point(-7,5).ring_class_field()
            sage: K5.discriminant_of_K()
            -7
        """
    @cached_method
    def ramified_primes(self):
        """
        Return the primes of `\\ZZ` that ramify in this ring class field.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K55 = E.heegner_point(-7,55).ring_class_field()
            sage: K55.ramified_primes()
            [5, 7, 11]
            sage: E.heegner_point(-7).ring_class_field().ramified_primes()
            [7]
        """
    @cached_method
    def degree_over_K(self):
        """
        Return the relative degree of this ring class field over the
        quadratic imaginary field `K`.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7,5)
            sage: K5 = P.ring_class_field(); K5
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: K5.degree_over_K()
            6
            sage: type(K5.degree_over_K())
            <... 'sage.rings.integer.Integer'>

            sage: E = EllipticCurve('389a'); E.heegner_point(-20).ring_class_field().degree_over_K()
            2
            sage: E.heegner_point(-20,3).ring_class_field().degree_over_K()
            4
            sage: kronecker(-20,11)
            -1
            sage: E.heegner_point(-20,11).ring_class_field().degree_over_K()
            24
        """
    @cached_method
    def degree_over_H(self):
        '''
        Return the degree of this field over the Hilbert class field `H` of `K`.

        EXAMPLES::

            sage: E = EllipticCurve(\'389a\')
            sage: E.heegner_point(-59).ring_class_field().degree_over_H()
            1
            sage: E.heegner_point(-59).ring_class_field().degree_over_K()
            3
            sage: QuadraticField(-59,\'a\').class_number()
            3

        Some examples in which prime dividing c is inert::

            sage: heegner_point(37,-7,3).ring_class_field().degree_over_H()
            4
            sage: heegner_point(37,-7,3^2).ring_class_field().degree_over_H()
            12
            sage: heegner_point(37,-7,3^3).ring_class_field().degree_over_H()
            36

        The prime dividing c is split.  For example, in the first case
        `O_K/cO_K` is isomorphic to a direct sum of two copies of
        ``GF(2)``, so the units are trivial::

            sage: heegner_point(37,-7,2).ring_class_field().degree_over_H()
            1
            sage: heegner_point(37,-7,4).ring_class_field().degree_over_H()
            2
            sage: heegner_point(37,-7,8).ring_class_field().degree_over_H()
            4

        Now c is ramified::

            sage: heegner_point(37,-7,7).ring_class_field().degree_over_H()
            7
            sage: heegner_point(37,-7,7^2).ring_class_field().degree_over_H()
            49

        Check that :issue:`15218` is solved::

            sage: E = EllipticCurve("19a");
            sage: s = E.heegner_point(-3,2).ring_class_field().galois_group().complex_conjugation()
            sage: H = s.domain(); H.absolute_degree()
            2
        '''
    @cached_method
    def absolute_degree(self):
        """
        Return the absolute degree of this field over `\\QQ`.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K = E.heegner_point(-7,5).ring_class_field()
            sage: K.absolute_degree()
            12
            sage: K.degree_over_K()
            6
        """
    degree_over_Q = absolute_degree
    @cached_method
    def quadratic_field(self):
        """
        Return the quadratic imaginary field `K = \\QQ(\\sqrt{D})`.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K = E.heegner_point(-7,5).ring_class_field()
            sage: K.quadratic_field()
            Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
             with sqrt_minus_7 = 2.645751311064591?*I
        """
    @cached_method
    def galois_group(self, base=...):
        """
        Return the Galois group of ``self`` over base.

        INPUT:

        - ``base`` -- (default: `\\QQ`) a subfield of ``self`` or `\\QQ`

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: A = E.heegner_point(-7,5).ring_class_field()
            sage: A.galois_group()
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: B = E.heegner_point(-7).ring_class_field()
            sage: C = E.heegner_point(-7,15).ring_class_field()
            sage: A.galois_group()
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: A.galois_group(B)
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
             over Hilbert class field of QQ[sqrt(-7)]
            sage: A.galois_group().cardinality()
            12
            sage: A.galois_group(B).cardinality()
            6
            sage: C.galois_group(A)
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 15
             over Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: C.galois_group(A).cardinality()
            4
        """
    def is_subfield(self, M):
        """
        Return ``True`` if this ring class field is a subfield of the ring class field `M`.
        If `M` is not a ring class field, then a :exc:`TypeError` is raised.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: A = E.heegner_point(-7,5).ring_class_field()
            sage: B = E.heegner_point(-7).ring_class_field()
            sage: C = E.heegner_point(-20).ring_class_field()
            sage: D = E.heegner_point(-7,15).ring_class_field()
            sage: B.is_subfield(A)
            True
            sage: B.is_subfield(B)
            True
            sage: B.is_subfield(D)
            True
            sage: B.is_subfield(C)
            False
            sage: A.is_subfield(B)
            False
            sage: A.is_subfield(D)
            True
        """

class GaloisGroup(SageObject):
    """
    A Galois group of a ring class field.

    EXAMPLES::

        sage: E = EllipticCurve('389a')
        sage: G = E.heegner_point(-7,5).ring_class_field().galois_group(); G
        Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
        sage: G.field()
        Ring class field extension of QQ[sqrt(-7)] of conductor 5
        sage: G.cardinality()
        12
        sage: G.complex_conjugation()
        Complex conjugation automorphism of Ring class field extension of QQ[sqrt(-7)]
         of conductor 5

    TESTS::

        sage: G = heegner_point(37,-7).ring_class_field().galois_group()
        sage: loads(dumps(G)) == G
        True
        sage: type(G)
        <class 'sage.schemes.elliptic_curves.heegner.GaloisGroup'>
    """
    def __init__(self, field, base=...) -> None:
        """
        INPUT:

        - ``field`` -- a ring class field

        - ``base`` -- subfield of field (default: `\\QQ`)

        EXAMPLES::

            sage: K5 = heegner_points(389,-7,5).ring_class_field()
            sage: K1 = heegner_points(389,-7,1).ring_class_field()
            sage: sage.schemes.elliptic_curves.heegner.GaloisGroup(K5,K1)
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
             over Hilbert class field of QQ[sqrt(-7)]
            sage: K5.galois_group(K1)
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
             over Hilbert class field of QQ[sqrt(-7)]
        """
    def __eq__(self, G):
        """
        EXAMPLES::

            sage: G = EllipticCurve('389a').heegner_point(-7,5).ring_class_field().galois_group()
            sage: G == G
            True
            sage: G == 0
            False
            sage: H = EllipticCurve('389a').heegner_point(-7,11).ring_class_field().galois_group()
            sage: G == H
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: G = EllipticCurve('389a').heegner_point(-7,5).ring_class_field().galois_group()
            sage: G != G
            False
            sage: G != 0
            True
            sage: H = EllipticCurve('389a').heegner_point(-7,11).ring_class_field().galois_group()
            sage: G != H
            True
        """
    def __hash__(self):
        """
        Return hash of this Galois group, which is the same as the
        hash of the pair, the field and its base.

        EXAMPLES::

            sage: G = EllipticCurve('389a').heegner_point(-7,5).ring_class_field().galois_group()
            sage: hash(G) == hash((G.field(), G.base_field()))
            True
        """
    def __call__(self, x):
        """
        Coerce `x` into ``self``, where `x` is a Galois group element, or
        in case ``self`` has base field the Hilbert class field, `x` can
        also be an element of the ring of integers.

        INPUT:

        - ``x`` -- automorphism or quadratic field element

        OUTPUT: an automorphism (or :exc:`TypeError`)

        EXAMPLES::

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K5.galois_group(K1)
            sage: G(1)
            Class field automorphism defined by x^2 + 325*y^2
            sage: G(G[0])
            Class field automorphism defined by x^2 + 325*y^2
            sage: alpha = 2 + K1.quadratic_field().gen(); alpha
            sqrt_minus_52 + 2
            sage: G(alpha)
            Class field automorphism defined by 14*x^2 - 10*x*y + 25*y^2

        A :exc:`TypeError` is raised when the coercion is not possible::

            sage: G(0)
            Traceback (most recent call last):
            ...
            TypeError: x does not define element of (O_K/c*O_K)^*
        """
    def field(self):
        """
        Return the ring class field that this Galois group acts on.

        EXAMPLES::

            sage: G = heegner_point(389,-7,5).ring_class_field().galois_group()
            sage: G.field()
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """
    def base_field(self):
        """
        Return the base field, which the field fixed by all the
        automorphisms in this Galois group.

        EXAMPLES::

            sage: x = heegner_point(37,-7,5)
            sage: Kc = x.ring_class_field(); Kc
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: K = x.quadratic_field()
            sage: G = Kc.galois_group(); G
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: G.base_field()
            Rational Field
            sage: G.cardinality()
            12
            sage: Kc.absolute_degree()
            12
            sage: G = Kc.galois_group(K); G
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
             over Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
              with sqrt_minus_7 = 2.645751311064591?*I
            sage: G.cardinality()
            6
            sage: G.base_field()
            Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
             with sqrt_minus_7 = 2.645751311064591?*I
            sage: G = Kc.galois_group(Kc); G
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
             over Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: G.cardinality()
            1
            sage: G.base_field()
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """
    @cached_method
    def kolyvagin_generators(self):
        """
        Assuming this Galois group `G` is of the form
        `G=\\textrm{Gal}(K_c/K_1)`, with `c=p_1\\dots p_n` satisfying the
        Kolyvagin hypothesis, this function returns noncanonical
        choices of lifts of generators for each of the cyclic factors
        of `G` corresponding to the primes dividing `c`.  Thus the
        `i`-th returned valued is an element of `G` that maps to the
        identity element of `\\textrm{Gal}(K_p/K_1)` for all `p \\neq p_i` and
        to a choice of generator of `\\textrm{Gal}(K_{p_i}/K_1)`.

        OUTPUT: list of elements of ``self``

        EXAMPLES::

            sage: K3 = heegner_points(389,-52,3).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K3.galois_group(K1)
            sage: G.kolyvagin_generators()
            (Class field automorphism defined by 9*x^2 - 6*x*y + 14*y^2,)

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K5.galois_group(K1)
            sage: G.kolyvagin_generators()
            (Class field automorphism defined by 17*x^2 - 14*x*y + 22*y^2,)
        """
    @cached_method
    def lift_of_hilbert_class_field_galois_group(self):
        """
        Assuming this Galois group `G` is of the form `G=\\textrm{Gal}(K_c/K)`,
        this function returns noncanonical choices of lifts of the
        elements of the quotient group `\\textrm{Gal}(K_1/K)`.

        OUTPUT: tuple of elements of ``self``

        EXAMPLES::

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: G = K5.galois_group(K5.quadratic_field())
            sage: G.lift_of_hilbert_class_field_galois_group()
            (Class field automorphism defined by x^2 + 325*y^2,
             Class field automorphism defined by 2*x^2 + 2*x*y + 163*y^2)
            sage: G.cardinality()
            12
            sage: K5.quadratic_field().class_number()
            2
        """
    def is_kolyvagin(self):
        """
        Return ``True`` if conductor `c` is prime to the discriminant of the
        quadratic field, `c` is squarefree and each prime dividing `c`
        is inert.

        EXAMPLES::

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: K5.galois_group(K1).is_kolyvagin()
            True
            sage: K7 = heegner_points(389,-52,7).ring_class_field()
            sage: K7.galois_group(K1).is_kolyvagin()
            False
            sage: K25 = heegner_points(389,-52,25).ring_class_field()
            sage: K25.galois_group(K1).is_kolyvagin()
            False
        """
    def __getitem__(self, i):
        """
        EXAMPLES::

            sage: E = EllipticCurve('389a'); F = E.heegner_point(-7,5).ring_class_field()
            sage: G = F.galois_group(F.quadratic_field())
            sage: G[0]
            Class field automorphism defined by x^2 + x*y + 44*y^2
        """
    def __len__(self) -> int:
        """
        EXAMPLES::

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K5.galois_group(K1)
            sage: G.cardinality()
            6
            sage: len(G)
            6
        """
    @cached_method
    def cardinality(self):
        """
        Return the cardinality of this Galois group.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: G = E.heegner_point(-7,5).ring_class_field().galois_group(); G
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: G.cardinality()
            12
            sage: G = E.heegner_point(-7).ring_class_field().galois_group()
            sage: G.cardinality()
            2
            sage: G = E.heegner_point(-7,55).ring_class_field().galois_group()
            sage: G.cardinality()
            120
        """
    @cached_method
    def complex_conjugation(self):
        """
        Return the automorphism of ``self`` determined by complex
        conjugation.  The base field must be the rational numbers.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: G = E.heegner_point(-7,5).ring_class_field().galois_group()
            sage: G.complex_conjugation()
            Complex conjugation automorphism of Ring class field extension
             of QQ[sqrt(-7)] of conductor 5
        """

class GaloisAutomorphism(SageObject):
    """
    An abstract automorphism of a ring class field.

    .. TODO::

        make :class:`GaloisAutomorphism` derive from GroupElement, so
        that one gets powers for free, etc.
    """
    def __init__(self, parent) -> None:
        """
        INPUT:

        - ``parent`` -- a group of automorphisms of a ring class field

        EXAMPLES::

            sage: G = heegner_points(389,-7,5).ring_class_field().galois_group(); G
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
            sage: sage.schemes.elliptic_curves.heegner.GaloisAutomorphism(G)
            <sage.schemes.elliptic_curves.heegner.GaloisAutomorphism object at ...>
        """
    def parent(self):
        """
        Return the parent of this automorphism, which is a Galois
        group of a ring class field.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: G = E.heegner_point(-7,5).ring_class_field().galois_group()
            sage: s = G.complex_conjugation()
            sage: s.parent()
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """
    def domain(self):
        """
        Return the domain of this automorphism.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: G = E.heegner_point(-7,5).ring_class_field().galois_group()
            sage: s = G.complex_conjugation()
            sage: s.domain()
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """

class GaloisAutomorphismComplexConjugation(GaloisAutomorphism):
    """
    The complex conjugation automorphism of a ring class field.

    EXAMPLES::

        sage: G = heegner_point(37,-7,5).ring_class_field().galois_group()
        sage: conj = G.complex_conjugation()
        sage: conj
        Complex conjugation automorphism of Ring class field extension
         of QQ[sqrt(-7)] of conductor 5
        sage: conj.domain()
        Ring class field extension of QQ[sqrt(-7)] of conductor 5

    TESTS::

        sage: type(conj)
        <class 'sage.schemes.elliptic_curves.heegner.GaloisAutomorphismComplexConjugation'>
        sage: loads(dumps(conj)) == conj
        True
    """
    def __init__(self, parent) -> None:
        """
        INPUT:

            - ``parent`` -- a group of automorphisms of a ring class field

        EXAMPLES::

            sage: G = heegner_point(37,-7,5).ring_class_field().galois_group()
            sage: sage.schemes.elliptic_curves.heegner.GaloisAutomorphismComplexConjugation(G)
            Complex conjugation automorphism of Ring class field extension
             of QQ[sqrt(-7)] of conductor 5
        """
    def __hash__(self):
        """
        The hash value is the same as the hash value of the
        pair ``(self.parent(), 1)``.

        EXAMPLES::

            sage: G = EllipticCurve('389a').heegner_point(-7,5).ring_class_field().galois_group()
            sage: conj = G.complex_conjugation()
            sage: hash(conj) == hash((conj.parent(), 1))
            True
        """
    def __eq__(self, right):
        """
        EXAMPLES::

            sage: G = EllipticCurve('389a').heegner_point(-7,5).ring_class_field().galois_group()
            sage: conj = G.complex_conjugation()
            sage: conj2 = sage.schemes.elliptic_curves.heegner.GaloisAutomorphismComplexConjugation(G)
            sage: conj is conj2
            False
            sage: conj == conj2
            True
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: G = EllipticCurve('389a').heegner_point(-7,5).ring_class_field().galois_group()
            sage: conj = G.complex_conjugation()
            sage: conj2 = sage.schemes.elliptic_curves.heegner.GaloisAutomorphismComplexConjugation(G)
            sage: conj != conj2
            False
        """
    def __invert__(self):
        """
        Return the inverse of ``self``, which is just ``self`` again.

        EXAMPLES::

            sage: conj = heegner_point(37,-7,5).ring_class_field().galois_group().complex_conjugation()
            sage: ~conj
            Complex conjugation automorphism of Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """
    def order(self):
        """
        EXAMPLES::

            sage: G = heegner_point(37,-7,5).ring_class_field().galois_group()
            sage: conj = G.complex_conjugation()
            sage: conj.order()
            2
        """

class GaloisAutomorphismQuadraticForm(GaloisAutomorphism):
    """
    An automorphism of a ring class field defined by a quadratic form.

    EXAMPLES::

        sage: H = heegner_points(389,-20,3)
        sage: sigma = H.ring_class_field().galois_group(H.quadratic_field())[0]; sigma
        Class field automorphism defined by x^2 + 45*y^2
        sage: type(sigma)
        <class 'sage.schemes.elliptic_curves.heegner.GaloisAutomorphismQuadraticForm'>
        sage: loads(dumps(sigma)) == sigma
        True
    """
    def __init__(self, parent, quadratic_form, alpha=None) -> None:
        """
        INPUT:

        - ``parent`` -- a group of automorphisms of a ring class field

        - ``quadratic_form`` -- a binary quadratic form that
          defines an element of the Galois group of `K_c` over `K`

        - ``alpha`` -- (default: ``None``) optional data that specified
          element corresponding element of `(\\mathcal{O}_K /
          c\\mathcal{O}_K)^* / (\\ZZ/c\\ZZ)^*`, via class field theory.

        EXAMPLES::

            sage: H = heegner_points(389,-20,3)
            sage: G = H.ring_class_field().galois_group(H.quadratic_field())
            sage: f = BinaryQF_reduced_representatives(-20*9)[0]
            sage: sage.schemes.elliptic_curves.heegner.GaloisAutomorphismQuadraticForm(G, f)
            Class field automorphism defined by x^2 + 45*y^2
        """
    @cached_method
    def order(self):
        """
        Return the multiplicative order of this Galois group automorphism.

        EXAMPLES::

            sage: K3 = heegner_points(389,-52,3).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K3.galois_group(K1)
            sage: sorted([g.order() for g in G])
            [1, 2, 4, 4]
            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K5.galois_group(K1)
            sage: sorted([g.order() for g in G])
            [1, 2, 3, 3, 6, 6]
        """
    def alpha(self):
        """
        Optional data that specified element corresponding element of
        `(\\mathcal{O}_K / c\\mathcal{O}_K)^* / (\\ZZ/c\\ZZ)^*`, via class
        field theory.

        This is a generator of the ideal corresponding to this
        automorphism.

        EXAMPLES::

            sage: K3 = heegner_points(389,-52,3).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K3.galois_group(K1)
            sage: orb = sorted([g.alpha() for g in G]); orb # random (the sign depends on the database being installed or not)
            [1, 1/2*sqrt_minus_52 + 1, -1/2*sqrt_minus_52, 1/2*sqrt_minus_52 - 1]
            sage: sorted([x^2 for x in orb]) # this is just for testing
            [-13, -sqrt_minus_52 - 12, sqrt_minus_52 - 12, 1]

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K5.galois_group(K1)
            sage: orb = sorted([g.alpha() for g in G]); orb # random (the sign depends on the database being installed or not)
            [1, -1/2*sqrt_minus_52, 1/2*sqrt_minus_52 + 1, 1/2*sqrt_minus_52 - 1,
             1/2*sqrt_minus_52 - 2, -1/2*sqrt_minus_52 - 2]
            sage: sorted([x^2 for x in orb]) # just for testing
            [-13, -sqrt_minus_52 - 12, sqrt_minus_52 - 12,
             -2*sqrt_minus_52 - 9, 2*sqrt_minus_52 - 9, 1]
        """
    @cached_method
    def p1_element(self):
        """
        Return element of the projective line corresponding to this
        automorphism.

        This only makes sense if this automorphism is in the Galois
        group `\\textrm{Gal}(K_c/K_1)`.

        EXAMPLES::

            sage: K3 = heegner_points(389,-52,3).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K3.galois_group(K1)
            sage: sorted([g.p1_element() for g in G])
            [(0, 1), (1, 0), (1, 1), (1, 2)]

            sage: K5 = heegner_points(389,-52,5).ring_class_field()
            sage: K1 = heegner_points(389,-52,1).ring_class_field()
            sage: G = K5.galois_group(K1)
            sage: sorted([g.p1_element() for g in G])
            [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]
        """
    def __hash__(self):
        """
        The hash value is the hash of the pair formed by the parent
        and the quadratic form read as tuple.

        EXAMPLES::

            sage: H = heegner_points(389,-20,3)
            sage: s = H.ring_class_field().galois_group(H.quadratic_field())[0]
            sage: hash(s) == hash((s.parent(), tuple(s.quadratic_form())))
            True
        """
    def __richcmp__(self, right, op):
        """
        Comparison.

        EXAMPLES::

            sage: H = heegner_points(389,-7,5)
            sage: s = H.ring_class_field().galois_group(H.quadratic_field())[1]
            sage: s == s
            True
            sage: s == s*s
            False
            sage: s == s*s*s*s*s
            False
            sage: s == s*s*s*s*s*s*s
            True

            sage: H = heegner_points(389,-20,3)
            sage: s = H.ring_class_field().galois_group(H.quadratic_field())[0]
            sage: s == s
            True
            sage: s == 0
            False
        """
    def __mul__(self, right):
        """
        Return the composition of two automorphisms.

        EXAMPLES::

            sage: H = heegner_points(389,-20,3); s = H.ring_class_field().galois_group(H.quadratic_field())[0]
            sage: s * s
            Class field automorphism defined by x^2 + 45*y^2
            sage: G = s.parent(); list(G)
            [Class field automorphism defined by x^2 + 45*y^2, Class field automorphism defined by 2*x^2 + 2*x*y + 23*y^2,
             Class field automorphism defined by 5*x^2 + 9*y^2, Class field automorphism defined by 7*x^2 + 4*x*y + 7*y^2]
            sage: G[0]*G[0]
            Class field automorphism defined by x^2 + 45*y^2
            sage: G[1]*G[2] == G[3]
            True
        """
    def quadratic_form(self):
        """
        Return reduced quadratic form corresponding to this Galois
        automorphism.

        EXAMPLES::

            sage: H = heegner_points(389,-20,3); s = H.ring_class_field().galois_group(H.quadratic_field())[0]
            sage: s.quadratic_form()
            x^2 + 45*y^2
        """
    @cached_method
    def ideal(self):
        """
        Return ideal of ring of integers of quadratic imaginary field
        corresponding to this quadratic form.  This is the ideal

         `I = \\left(A, \\frac{-B+ c\\sqrt{D}}{2}\\right) \\mathcal{O}_K`.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); F = E.heegner_point(-20,3).ring_class_field()
            sage: G = F.galois_group(F.quadratic_field())
            sage: G[1].ideal()
            Fractional ideal (2, 1/2*sqrt_minus_20 + 1)
            sage: [s.ideal().gens() for s in G]
            [(1, 3/2*sqrt_minus_20), (2, 3/2*sqrt_minus_20 - 1),
             (5, 3/2*sqrt_minus_20), (7, 3/2*sqrt_minus_20 - 2)]
        """

class HeegnerPoint(SageObject):
    """
    A Heegner point of level `N`, discriminant `D` and conductor `c`
    is any point on a modular curve or elliptic curve that is
    concocted in some way from a quadratic imaginary `\\tau` in the upper
    half plane with `\\Delta(\\tau) = D c = \\Delta(N \\tau)`.

    EXAMPLES::

        sage: x = sage.schemes.elliptic_curves.heegner.HeegnerPoint(389,-7,13); x
        Heegner point of level 389, discriminant -7, and conductor 13
        sage: type(x)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoint'>
        sage: loads(dumps(x)) == x
        True
    """
    def __init__(self, N, D, c) -> None:
        """
        INPUT:

        - ``N`` -- (positive integer) the level

        - ``D`` -- (negative integer) fundamental discriminant

        - ``c`` -- (positive integer) conductor

        Since this is an abstract base class, no type or compatibility
        checks are done, as those are all assumed to be done in the
        derived class.

        EXAMPLES::

            sage: H = sage.schemes.elliptic_curves.heegner.HeegnerPoint(389,-7,5)
            sage: type(H)
            <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoint'>
        """
    def __richcmp__(self, x, op):
        """
        Compare two Heegner points.

        EXAMPLES::

            sage: H = sage.schemes.elliptic_curves.heegner.HeegnerPoint(389,-7,5)
            sage: H == H
            True

            sage: H = sage.schemes.elliptic_curves.heegner.HeegnerPoint(389,-7,5); type(H)
            <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoint'>
            sage: J = sage.schemes.elliptic_curves.heegner.HeegnerPoint(389,-7,11)
            sage: H == H
            True
            sage: H == J
            False
            sage: J == H
            False
            sage: H == 0
            False
        """
    def __hash__(self):
        """
        The hash value is obtained from level, discriminant, and conductor.

        EXAMPLES::

            sage: H = sage.schemes.elliptic_curves.heegner.HeegnerPoint(389,-7,5); type(H)
            <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoint'>
            sage: hash(H)  == hash((H.level(), H.discriminant(), H.conductor()))
            True
        """
    def level(self):
        """
        Return the level of this Heegner point, which is the level of the
        modular curve `X_0(N)` on which this is a Heegner point.

        EXAMPLES::

            sage: heegner_point(389,-7,5).level()
            389
        """
    def conductor(self):
        """
        Return the conductor of this Heegner point.

        EXAMPLES::

            sage: heegner_point(389,-7,5).conductor()
            5
            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67,7); P
            Kolyvagin point of discriminant -67 and conductor 7
             on elliptic curve of conductor 37
            sage: P.conductor()
            7
            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5); P.conductor()
            5
        """
    def discriminant(self):
        """
        Return the discriminant of the quadratic imaginary field
        associated to this Heegner point.

        EXAMPLES::

            sage: heegner_point(389,-7,5).discriminant()
            -7
            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67,7); P
            Kolyvagin point of discriminant -67 and conductor 7
             on elliptic curve of conductor 37
            sage: P.discriminant()
            -67
            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5); P.discriminant()
            -7
        """
    @cached_method
    def quadratic_field(self):
        """
        Return the quadratic number field of discriminant `D`.

        EXAMPLES::

            sage: x = heegner_point(37,-7,5)
            sage: x.quadratic_field()
            Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
             with sqrt_minus_7 = 2.645751311064591?*I

            sage: E = EllipticCurve('37a'); P = E.heegner_point(-40)
            sage: P.quadratic_field()
            Number Field in sqrt_minus_40 with defining polynomial x^2 + 40
             with sqrt_minus_40 = 6.324555320336759?*I
            sage: P.quadratic_field() is P.quadratic_field()
            True
            sage: type(P.quadratic_field())
            <class 'sage.rings.number_field.number_field.NumberField_quadratic_with_category'>
        """
    @cached_method
    def quadratic_order(self):
        """
        Return the order in the quadratic imaginary field of conductor
        `c`, where `c` is the conductor of this Heegner point.

        EXAMPLES::

            sage: heegner_point(389,-7,5).quadratic_order()
            Order of conductor 10 generated by 5*sqrt_minus_7
             in Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
             with sqrt_minus_7 = 2.645751311064591?*I
            sage: heegner_point(389,-7,5).quadratic_order().basis()
            [1, 5*sqrt_minus_7]

            sage: E = EllipticCurve('37a'); P = E.heegner_point(-40,11)
            sage: P.quadratic_order()
            Order of conductor 22 generated by 11*sqrt_minus_40
             in Number Field in sqrt_minus_40 with defining polynomial x^2 + 40
             with sqrt_minus_40 = 6.324555320336759?*I
            sage: P.quadratic_order().basis()
            [1, 11*sqrt_minus_40]
        """
    @cached_method
    def ring_class_field(self):
        """
        Return the ring class field associated to this Heegner point.
        This is an extension `K_c` over `K`, where `K` is the
        quadratic imaginary field and `c` is the conductor associated
        to this Heegner point.  This Heegner point is defined over
        `K_c` and the Galois group `Gal(K_c/K)` acts transitively on
        the Galois conjugates of this Heegner point.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K.<a> = QuadraticField(-5)
            sage: len(K.factor(5))
            1
            sage: len(K.factor(23))
            2
            sage: E.heegner_point(-7, 5).ring_class_field().degree_over_K()
            6
            sage: E.heegner_point(-7, 23).ring_class_field().degree_over_K()
            22
            sage: E.heegner_point(-7, 5*23).ring_class_field().degree_over_K()
            132
            sage: E.heegner_point(-7, 5^2).ring_class_field().degree_over_K()
            30
            sage: E.heegner_point(-7, 7).ring_class_field().degree_over_K()
            7
        """

class HeegnerPoints(SageObject):
    """
    The set of Heegner points with given parameters.

    EXAMPLES::

        sage: H = heegner_points(389); H
        Set of all Heegner points on X_0(389)
        sage: type(H)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoints_level'>
        sage: isinstance(H, sage.schemes.elliptic_curves.heegner.HeegnerPoints)
        True
    """
    def __init__(self, N) -> None:
        """
        INPUT:

        - ``N`` -- level, a positive integer

        EXAMPLES::

            sage: heegner_points(37)
            Set of all Heegner points on X_0(37)
            sage: heegner_points(0)
            Traceback (most recent call last):
            ...
            ValueError: N must a positive integer
        """
    def level(self):
        """
        Return the level `N` of the modular curve `X_0(N)`.

        EXAMPLES::

            sage: heegner_points(389).level()
            389
        """

class HeegnerPoints_level(HeegnerPoints):
    """
    Return the infinite set of all Heegner points on `X_0(N)` for all
    quadratic imaginary fields.

    EXAMPLES::

        sage: H = heegner_points(11); H
        Set of all Heegner points on X_0(11)
        sage: type(H)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoints_level'>
        sage: loads(dumps(H)) == H
        True
    """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(11)
            sage: H == heegner_points(13)
            False
            sage: H == heegner_points(11)
            True
            sage: H == 0
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(11)
            sage: H != heegner_points(13)
            True
            sage: H != heegner_points(11)
            False
            sage: H != 0
            True
        """
    def reduce_mod(self, ell):
        """
        Return object that allows for computation with Heegner points
        of level `N` modulo the prime `\\ell`, represented using
        quaternion algebras.

        INPUT:

        - `\\ell` -- prime

        EXAMPLES::

            sage: heegner_points(389).reduce_mod(7).quaternion_algebra()
            Quaternion Algebra (-1, -7) with base ring Rational Field
        """
    def discriminants(self, n: int = 10, weak: bool = False):
        """
        Return the first `n` quadratic imaginary discriminants that
        satisfy the Heegner hypothesis for `N`.

        INPUT:

        - ``n`` -- nonnegative integer

        - ``weak`` -- boolean (default: ``False``); if ``True`` only require
          weak Heegner hypothesis, which is the same as usual but
          without the condition that `\\gcd(D,N)=1`.

        EXAMPLES::

            sage: X = heegner_points(37)
            sage: X.discriminants(5)
            [-7, -11, -40, -47, -67]

        The default is 10::

            sage: X.discriminants()
            [-7, -11, -40, -47, -67, -71, -83, -84, -95, -104]
            sage: X.discriminants(15)
            [-7, -11, -40, -47, -67, -71, -83, -84, -95, -104, -107, -115, -120, -123, -127]

        The discriminant -111 satisfies only the weak Heegner hypothesis, since it
        is divisible by 37::

            sage: X.discriminants(15, weak=True)
            [-7, -11, -40, -47, -67, -71, -83, -84, -95, -104, -107, -111, -115, -120, -123]
        """

class HeegnerPoints_level_disc(HeegnerPoints):
    """
    Set of Heegner points of given level and all conductors associated
    to a quadratic imaginary field.

    EXAMPLES::

        sage: H = heegner_points(389,-7); H
        Set of all Heegner points on X_0(389) associated to QQ[sqrt(-7)]
        sage: type(H)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoints_level_disc'>
        sage: H._repr_()
        'Set of all Heegner points on X_0(389) associated to QQ[sqrt(-7)]'
        sage: H.discriminant()
        -7
        sage: H.quadratic_field()
        Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
         with sqrt_minus_7 = 2.645751311064591?*I
        sage: H.kolyvagin_conductors()
        [1, 3, 5, 13, 15, 17, 19, 31, 39, 41]

        sage: loads(dumps(H)) == H
        True
    """
    def __init__(self, N, D) -> None:
        """
        INPUT:

        - ``N`` -- positive integer

        - ``D`` -- negative fundamental discriminant

        EXAMPLES::

            sage: sage.schemes.elliptic_curves.heegner.HeegnerPoints_level_disc(37,-7)
            Set of all Heegner points on X_0(37) associated to QQ[sqrt(-7)]
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(389,-7)
            sage: H == heegner_points(389,-7)
            True
            sage: H == 0
            False
            sage: H == heegner_points(389,-11)
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(389,-7)
            sage: H != heegner_points(389,-7)
            False
            sage: H != 0
            True
            sage: H != heegner_points(389,-11)
            True
        """
    def discriminant(self):
        """
        Return the discriminant of the quadratic imaginary extension `K`.

        EXAMPLES::

            sage: heegner_points(389,-7).discriminant()
            -7
        """
    @cached_method
    def quadratic_field(self):
        """
        Return the quadratic imaginary field `K = \\QQ(\\sqrt{D})`.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); K = E.heegner_point(-7,5).ring_class_field()
            sage: K.quadratic_field()
            Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
             with sqrt_minus_7 = 2.645751311064591?*I
        """
    def kolyvagin_conductors(self, r=None, n: int = 10, E=None, m=None):
        """
        Return the first `n` conductors that are squarefree products
        of distinct primes inert in the quadratic imaginary field
        `K = \\QQ(\\sqrt{D})`.  If `r` is specified, return only
        conductors that are a product of `r` distinct primes all inert
        in `K`.  If `r = 0`, always return the list ``[1]``,
        no matter what.

        If the optional elliptic curve `E` and integer `m` are given,
        then only include conductors `c` such that for each prime
        divisor `p` of `c` we have `m \\mid \\gcd(a_p(E), p+1)`.

        INPUT:

        - ``r`` -- (default: ``None``) nonnegative integer or ``None``

        - ``n`` -- positive integer

        - ``E`` -- an elliptic curve

        - ``m`` -- positive integer

        EXAMPLES::

            sage: H = heegner_points(389, -7)
            sage: H.kolyvagin_conductors(0)
            [1]
            sage: H.kolyvagin_conductors(1)
            [3, 5, 13, 17, 19, 31, 41, 47, 59, 61]
            sage: H.kolyvagin_conductors(1,15)
            [3, 5, 13, 17, 19, 31, 41, 47, 59, 61, 73, 83, 89, 97, 101]
            sage: H.kolyvagin_conductors(1,5)
            [3, 5, 13, 17, 19]
            sage: H.kolyvagin_conductors(1, 5, EllipticCurve('389a'), 3)
            [5, 17, 41, 59, 83]
            sage: H.kolyvagin_conductors(2, 5, EllipticCurve('389a'), 3)
            [85, 205, 295, 415, 697]
        """

def is_kolyvagin_conductor(N, E, D, r, n, c):
    """
    Return ``True`` if `c` is a Kolyvagin conductor for level `N`,
    discriminant `D`, mod `n`, etc., i.e., `c` is divisible by exactly
    `r` prime factors, is coprime to `ND`, each prime dividing `c` is
    inert, and if `E` is not ``None`` then `n | \\gcd(p+1, a_p(E))`
    for each prime `p` dividing `c`.

    INPUT:

    - ``N`` -- level (positive integer)

    - ``E`` -- elliptic curve or ``None``

    - ``D`` -- negative fundamental discriminant

    - ``r`` -- number of prime factors (nonnegative integer) or ``None``

    - ``n`` -- torsion order (i.e., do we get class in `(E(K_c)/n E(K_c))^{Gal(K_c/K)}`?)

    - ``c`` -- conductor (positive integer)

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.heegner import is_kolyvagin_conductor
        sage: is_kolyvagin_conductor(389, None, -7, 1, None, 5)
        True
        sage: is_kolyvagin_conductor(389, None, -7, 1, None, 7)
        False
        sage: is_kolyvagin_conductor(389, None, -7, 1, None, 11)
        False
        sage: is_kolyvagin_conductor(389, EllipticCurve('389a'), -7, 1, 3, 5)
        True
        sage: is_kolyvagin_conductor(389, EllipticCurve('389a'), -7, 1, 11, 5)
        False
    """

class HeegnerPoints_level_disc_cond(HeegnerPoints_level, HeegnerPoints_level_disc):
    """
    The set of Heegner points of given level, discriminant, and conductor.

    EXAMPLES::

        sage: H = heegner_points(389,-7,5); H
        All Heegner points of conductor 5 on X_0(389) associated to QQ[sqrt(-7)]
        sage: type(H)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoints_level_disc_cond'>
        sage: H.discriminant()
        -7
        sage: H.level()
        389

        sage: len(H.points())
        12
        sage: H.points()[0]
        Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7 and conductor 5 on X_0(389)
        sage: H.betas()
        (147, 631)

        sage: H.quadratic_field()
        Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
         with sqrt_minus_7 = 2.645751311064591?*I
        sage: H.ring_class_field()
        Ring class field extension of QQ[sqrt(-7)] of conductor 5

        sage: H.kolyvagin_conductors()
        [1, 3, 5, 13, 15, 17, 19, 31, 39, 41]
        sage: H.satisfies_kolyvagin_hypothesis()
        True

        sage: H = heegner_points(389,-7,5)
        sage: loads(dumps(H)) == H
        True
    """
    def __init__(self, N, D, c=...) -> None:
        """
        Create set of Heegner points.

        INPUT:

        - ``N`` -- positive integer (the level)

        - ``D`` -- negative fundamental discriminant

        - ``c`` -- conductor (default: 1)

        EXAMPLES::

            sage: H = heegner_points(389,-7,5); H
            All Heegner points of conductor 5 on X_0(389) associated to QQ[sqrt(-7)]
            sage: type(H)
            <class 'sage.schemes.elliptic_curves.heegner.HeegnerPoints_level_disc_cond'>
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(389,-7, 3)
            sage: H == heegner_points(389,-7, 3)
            True
            sage: H == heegner_points(389,-7, 1)
            False
            sage: H == 0
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(389,-7, 3)
            sage: H != heegner_points(389,-7, 3)
            False
            sage: H != heegner_points(389,-7, 1)
            True
            sage: H != 0
            True
        """
    def conductor(self):
        """
        Return the level of the conductor.

        EXAMPLES::

            sage: heegner_points(389,-7,5).conductor()
            5
        """
    @cached_method
    def satisfies_kolyvagin_hypothesis(self):
        """
        Return ``True`` if ``self`` satisfies the Kolyvagin hypothesis, i.e.,
        that each prime dividing the conductor `c` of ``self`` is inert in
        `K` and coprime to `ND`.

        EXAMPLES:

        The prime 5 is inert, but the prime 11 is not::

            sage: heegner_points(389,-7,5).satisfies_kolyvagin_hypothesis()
            True
            sage: heegner_points(389,-7,11).satisfies_kolyvagin_hypothesis()
            False
        """
    @cached_method
    def ring_class_field(self):
        """
        Return the ring class field associated to this set of Heegner
        points.  This is an extension `K_c` over `K`, where `K` is the
        quadratic imaginary field and `c` the conductor associated to
        this Heegner point.  This Heegner point is defined over `K_c`
        and the Galois group `Gal(K_c/K)` acts transitively on the
        Galois conjugates of this Heegner point.

        EXAMPLES::

            sage: heegner_points(389,-7,5).ring_class_field()
            Ring class field extension of QQ[sqrt(-7)] of conductor 5
        """
    def __getitem__(self, i):
        """
        Return the `i`-th Heegner point.

        EXAMPLES::

            sage: H = heegner_points(389,-7,5)
            sage: len(H)
            12
            sage: H[0]
            Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7 and conductor 5
             on X_0(389)
            sage: H[-1]
            Heegner point 5/5446*sqrt(-7) - 757/778 of discriminant -7 and conductor 5
             on X_0(389)
        """
    def __len__(self) -> int:
        """
        Return the number of Heegner points.

        EXAMPLES::

            sage: len(heegner_points(389,-7,5))
            12

        When the conductor is 1 the length is a power of 2 (number of
        square roots of `D` mod `4N` reduced mod `2N`) times the class
        number::

            sage: len(heegner_points(389,-20,1))
            4
            sage: QQ[sqrt(-20)].class_number()
            2
        """
    @cached_method
    def betas(self):
        """
        Return the square roots of `D c^2` modulo `4 N` all reduced
        mod `2 N`, without multiplicity.

        EXAMPLES::

            sage: X = heegner_points(45,-11,1); X
            All Heegner points of conductor 1 on X_0(45) associated to QQ[sqrt(-11)]
            sage: [x.quadratic_form() for x in X]
            [45*x^2 + 13*x*y + y^2,
             45*x^2 + 23*x*y + 3*y^2,
             45*x^2 + 67*x*y + 25*y^2,
             45*x^2 + 77*x*y + 33*y^2]
            sage: X.betas()
            (13, 23, 67, 77)
            sage: X.points(13)
            (Heegner point 1/90*sqrt(-11) - 13/90 of discriminant -11 on X_0(45),)
            sage: [x.quadratic_form() for x in X.points(13)]
            [45*x^2 + 13*x*y + y^2]
        """
    @cached_method
    def points(self, beta=None):
        """
        Return the Heegner points in ``self``.  If `\\beta` is given,
        return only those Heegner points with given `\\beta`, i.e.,
        whose quadratic form has `B` congruent to `\\beta` modulo `2 N`.

        Use ``self.beta()`` to get a list of betas.

        EXAMPLES::

            sage: H = heegner_points(389, -7, 5); H
            All Heegner points of conductor 5 on X_0(389) associated to QQ[sqrt(-7)]
            sage: H.points()
            (Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7 and conductor 5
              on X_0(389),
             ...,
             Heegner point 5/5446*sqrt(-7) - 757/778 of discriminant -7 and conductor 5
              on X_0(389))
            sage: H.betas()
            (147, 631)
            sage: [x.tau() for x in H.points(147)]
            [5/778*sqrt_minus_7 - 147/778, 5/1556*sqrt_minus_7 - 147/1556,
             5/1556*sqrt_minus_7 - 925/1556, 5/3112*sqrt_minus_7 - 1703/3112,
             5/3112*sqrt_minus_7 - 2481/3112, 5/5446*sqrt_minus_7 - 21/778]

            sage: [x.tau() for x in H.points(631)]
            [5/778*sqrt_minus_7 - 631/778, 5/1556*sqrt_minus_7 - 631/1556,
             5/1556*sqrt_minus_7 - 1409/1556, 5/3112*sqrt_minus_7 - 631/3112,
             5/3112*sqrt_minus_7 - 1409/3112, 5/5446*sqrt_minus_7 - 757/778]

        The result is cached and is a tuple (since it is immutable)::

            sage: H.points() is H.points()
            True
            sage: type(H.points())
            <... 'tuple'>
        """
    def plot(self, *args, **kwds):
        """
        Return plot of all the representatives in the upper half
        plane of the Heegner points in this set of Heegner points.

        The inputs to this function get passed onto the point command.

        EXAMPLES::

            sage: heegner_points(389,-7,5).plot(pointsize=50, rgbcolor='red')           # needs sage.plot
            Graphics object consisting of 12 graphics primitives
            sage: heegner_points(53,-7,15).plot(pointsize=50, rgbcolor='purple')        # needs sage.plot
            Graphics object consisting of 48 graphics primitives
        """

class HeegnerPointOnX0N(HeegnerPoint):
    """
    A Heegner point as a point on the modular curve `X_0(N)`, which we
    view as the upper half plane modulo the action of `\\Gamma_0(N)`.

    EXAMPLES::

        sage: x = heegner_point(37, -7, 5); x
        Heegner point 5/74*sqrt(-7) - 11/74 of discriminant -7 and conductor 5 on X_0(37)
        sage: type(x)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPointOnX0N'>
        sage: x.level()
        37
        sage: x.conductor()
        5
        sage: x.discriminant()
        -7
        sage: x.quadratic_field()
        Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
         with sqrt_minus_7 = 2.645751311064591?*I
        sage: x.quadratic_form()
        37*x^2 + 11*x*y + 2*y^2
        sage: x.quadratic_order()
        Order of conductor 10 generated by 5*sqrt_minus_7
         in Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
         with sqrt_minus_7 = 2.645751311064591?*I
        sage: x.tau()
        5/74*sqrt_minus_7 - 11/74
        sage: loads(dumps(x)) == x
        True
    """
    def __init__(self, N, D, c=..., f=None, check: bool = True) -> None:
        """
        INPUT:

        - ``N`` -- positive integer

        - ``D`` -- fundamental discriminant, a negative integer

        - ``c`` -- conductor, a positive integer coprime to `N`

        - ``f`` -- binary quadratic form, 3-tuple `(A,B,C)` of coefficients
          of `AX^2 + BXY + CY^2`, or element of quadratic imaginary
          field `\\QQ(\\sqrt{D})` in the upper half plane

        - ``check`` -- boolean (default: ``True``); should not be used
          except internally

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.heegner import HeegnerPointOnX0N
            sage: x = heegner_point(389, -7, 5); x
            Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7 and conductor 5
             on X_0(389)
            sage: type(x)
            <class 'sage.schemes.elliptic_curves.heegner.HeegnerPointOnX0N'>
            sage: HeegnerPointOnX0N(389, -7, 5, None, check=False)
            Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7 and conductor 5
             on X_0(389)
        """
    def __hash__(self):
        """
        The hash is obtained from the hash provided by :class:`HeegnerPoint`,
        together with the reduced quadratic form.

        EXAMPLES::

            sage: x = heegner_point(37, -7, 5)
            sage: from sage.schemes.elliptic_curves.heegner import HeegnerPoint
            sage: hash(x) == hash( (HeegnerPoint.__hash__(x), x.reduced_quadratic_form()) )
            True
        """
    def __richcmp__(self, x, op):
        """
        Compare two Heegner points with character.

        EXAMPLES::

            sage: x1 = EllipticCurve('389a').heegner_point(-7).heegner_point_on_X0N()
            sage: x5 = EllipticCurve('389a').heegner_point(-7, 5).heegner_point_on_X0N()
            sage: x1 == x1
            True
            sage: x1 < x5
            True
            sage: x5 > x1
            True
        """
    def atkin_lehner_act(self, Q=None):
        """
        Given an integer Q dividing the level N such that `\\gcd(Q, N/Q) = 1`, return the
        image of this Heegner point under the Atkin-Lehner operator `W_Q`.

        INPUT:

        - ``Q`` -- positive divisor of `N`; if not given, default to `N`

        EXAMPLES::

            sage: x = heegner_point(389, -7, 5)
            sage: x.atkin_lehner_act()
            Heegner point 5/199168*sqrt(-7) - 631/199168 of discriminant -7
             and conductor 5 on X_0(389)

            sage: x = heegner_point(45, D=-11, c=1); x
            Heegner point 1/90*sqrt(-11) - 13/90 of discriminant -11 on X_0(45)
            sage: x.atkin_lehner_act(5)
            Heegner point 1/90*sqrt(-11) + 23/90 of discriminant -11 on X_0(45)
            sage: y = x.atkin_lehner_act(9); y
            Heegner point 1/90*sqrt(-11) - 23/90 of discriminant -11 on X_0(45)
            sage: z = y.atkin_lehner_act(9); z
            Heegner point 1/90*sqrt(-11) - 13/90 of discriminant -11 on X_0(45)
            sage: z == x
            True
        """
    @cached_method
    def quadratic_form(self):
        """
        Return the integral primitive positive-definite binary
        quadratic form associated to this Heegner point.

        EXAMPLES::

            sage: heegner_point(389, -7, 5).quadratic_form()
            389*x^2 + 147*x*y + 14*y^2
        """
    def reduced_quadratic_form(self):
        """
        Return reduced binary quadratic corresponding to this Heegner point.

        EXAMPLES::

            sage: x = heegner_point(389, -7, 5)
            sage: x.quadratic_form()
            389*x^2 + 147*x*y + 14*y^2
            sage: x.reduced_quadratic_form()
            4*x^2 - x*y + 11*y^2
        """
    @cached_method
    def tau(self):
        """
        Return an element ``tau`` in the upper half plane that corresponds
        to this particular Heegner point.

        Actually, ``tau`` is in the quadratic imaginary field K associated
        to this Heegner point.

        EXAMPLES::

            sage: x = heegner_point(37, -7, 5); tau = x.tau(); tau
            5/74*sqrt_minus_7 - 11/74
            sage: 37 * tau.minpoly()
            37*x^2 + 11*x + 2
            sage: x.quadratic_form()
            37*x^2 + 11*x*y + 2*y^2
        """
    def map_to_curve(self, E):
        """
        Return the image of this Heegner point on the elliptic curve
        `E`, which must also have conductor `N`, where `N` is the
        level of ``self``.

        EXAMPLES::

            sage: x = heegner_point(389, -7, 5); x
            Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7
             and conductor 5 on X_0(389)
            sage: y = x.map_to_curve(EllipticCurve('389a')); y
            Heegner point of discriminant -7 and conductor 5
             on elliptic curve of conductor 389
            sage: y.curve().cremona_label()
            '389a1'
            sage: y.heegner_point_on_X0N()
            Heegner point 5/778*sqrt(-7) - 147/778 of discriminant -7
             and conductor 5 on X_0(389)

        You can also directly apply the modular parametrization of the elliptic curve::

            sage: x = heegner_point(37,-7); x
            Heegner point 1/74*sqrt(-7) - 17/74 of discriminant -7 on X_0(37)
            sage: E = EllipticCurve('37a'); phi = E.modular_parametrization()
            sage: phi(x)
            Heegner point of discriminant -7 on elliptic curve of conductor 37
        """
    @cached_method
    def galois_orbit_over_K(self):
        """
        Return the `Gal(K_c/K)`-orbit of this Heegner point.

        EXAMPLES::

            sage: x = heegner_point(389, -7, 3); x
            Heegner point 3/778*sqrt(-7) - 223/778 of discriminant -7
             and conductor 3 on X_0(389)
            sage: x.galois_orbit_over_K()
            [Heegner point 3/778*sqrt(-7) - 223/778 of discriminant -7 and conductor 3 on X_0(389),
             Heegner point 3/1556*sqrt(-7) - 223/1556 of discriminant -7 and conductor 3 on X_0(389),
             Heegner point 3/1556*sqrt(-7) - 1001/1556 of discriminant -7 and conductor 3 on X_0(389),
             Heegner point 3/3112*sqrt(-7) - 223/3112 of discriminant -7 and conductor 3 on X_0(389)]
        """
    def plot(self, **kwds):
        """
        Draw a point at `(x,y)` where this Heegner point is
        represented by the point `\\tau = x + i y` in the upper half
        plane.

        The ``kwds`` get passed onto the point plotting command.

        EXAMPLES::

            sage: heegner_point(389,-7,1).plot(pointsize=50)
            Graphics object consisting of 1 graphics primitive
        """

class HeegnerPointOnEllipticCurve(HeegnerPoint):
    """
    A Heegner point on a curve associated to an order in a quadratic
    imaginary field.

    EXAMPLES::

        sage: E = EllipticCurve('37a'); P = E.heegner_point(-7,5); P
        Heegner point of discriminant -7 and conductor 5 on elliptic curve of conductor 37
        sage: type(P)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPointOnEllipticCurve'>
    """
    def __init__(self, E, x, check: bool = True) -> None:
        """
        INPUT:

        - ``E`` -- an elliptic curve over the rational numbers

        - ``x`` -- Heegner point on `X_0(N)`

        - ``check`` -- boolean (default: ``True``); if ``True``, ensure that `D`,
          `c` are of type Integer and define a Heegner point on `E`

        EXAMPLES::

            sage: x = heegner_point(389,-7,5)
            sage: E = EllipticCurve('389a')
            sage: sage.schemes.elliptic_curves.heegner.HeegnerPointOnEllipticCurve(E, x)
            Heegner point of discriminant -7 and conductor 5 on elliptic curve
             of conductor 389
        """
    @cached_method
    def satisfies_kolyvagin_hypothesis(self, n=None):
        """
        Return ``True`` if this Heegner point and `n` satisfy the
        Kolyvagin hypothesis, i.e., that each prime dividing the
        conductor `c` of ``self`` is inert in K and coprime to `ND`.
        Moreover, if `n` is not ``None``, also check that for each prime
        `p` dividing `c` we have that `n | \\gcd(a_p(E), p+1)`.

        INPUT:

        - ``n`` -- positive integer

        EXAMPLES::

            sage: EllipticCurve('389a').heegner_point(-7).satisfies_kolyvagin_hypothesis()
            True
            sage: EllipticCurve('389a').heegner_point(-7, 5).satisfies_kolyvagin_hypothesis()
            True
            sage: EllipticCurve('389a').heegner_point(-7, 11).satisfies_kolyvagin_hypothesis()
            False
        """
    def __hash__(self):
        """
        The hash value is obtained from the elliptic curve and the Heegner
        point on `X_0(N)`.

        EXAMPLES::

            sage: x = EllipticCurve('389a').heegner_point(-7, 5)
            sage: hash(x) == hash( (x.curve(), x.heegner_point_on_X0N()) )
            True
        """
    def __eq__(self, right):
        """
        EXAMPLES::

            sage: y1 = EllipticCurve('389a').heegner_point(-7)
            sage: y5 = EllipticCurve('389a').heegner_point(-7, 5)
            sage: y1 == y1
            True
            sage: y5 == y5
            True
            sage: y1 == y5
            False
            sage: y1 == 10
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: y1 = EllipticCurve('389a').heegner_point(-7)
            sage: y5 = EllipticCurve('389a').heegner_point(-7, 5)
            sage: y1 != y1
            False
            sage: y5 != y5
            False
            sage: y1 != y5
            True
            sage: y1 != 10
            True
        """
    def heegner_point_on_X0N(self):
        """
        Return Heegner point on `X_0(N)` that maps to this Heegner point on `E`.

        EXAMPLES::

            sage: E = EllipticCurve('37a'); P = E.heegner_point(-7,5); P
            Heegner point of discriminant -7 and conductor 5 on elliptic curve
             of conductor 37
            sage: P.heegner_point_on_X0N()
            Heegner point 5/74*sqrt(-7) - 11/74 of discriminant -7 and conductor 5
             on X_0(37)
        """
    def map_to_complex_numbers(self, prec: int = 53):
        """
        Return the point in the subfield `M` of the complex numbers
        (well defined only modulo the period lattice) corresponding to
        this Heegner point.

        EXAMPLES:

        We compute a nonzero Heegner point over a ring class field on
        a curve of rank 2::

            sage: E = EllipticCurve('389a'); y = E.heegner_point(-7,5)
            sage: y.map_to_complex_numbers()
            1.49979679635196 + 0.369156204821526*I
            sage: y.map_to_complex_numbers(100)
            1.4997967963519640592142411892 + 0.36915620482152626830089145962*I
            sage: y.map_to_complex_numbers(10)
            1.5 + 0.37*I

        Here we see that the Heegner point is 0 since it lies in the
        lattice::

            sage: E = EllipticCurve('389a'); y = E.heegner_point(-7)
            sage: y.map_to_complex_numbers(10)
            0.0034 - 3.9*I
            sage: y.map_to_complex_numbers()
            4.71844785465692e-15 - 3.94347540310330*I
            sage: E.period_lattice().basis()
            (2.49021256085505, 1.97173770155165*I)
            sage: 2*E.period_lattice().basis()[1]
            3.94347540310330*I

        You can also directly coerce to the complex field::

            sage: E = EllipticCurve('389a'); y = E.heegner_point(-7)
            sage: z = ComplexField(100)(y); z # real part approx. 0
            -... - 3.9434754031032964088448153963*I
            sage: E.period_lattice().elliptic_exponential(z)
            (0.00000000000000000000000000000 : 1.0000000000000000000000000000 : 0.00000000000000000000000000000)
        """
    @cached_method
    def kolyvagin_point(self):
        """
        Return the Kolyvagin point corresponding to this Heegner
        point.

        This is the point obtained by applying the Kolyvagin
        operator `J_c I_c` in the group ring of the Galois group to
        this Heegner point.   It is a point that defines an element
        of `H^1(K, E[n])`, under certain hypotheses on `n`.

        EXAMPLES::

            sage: E = EllipticCurve('37a1'); y = E.heegner_point(-7); y
            Heegner point of discriminant -7 on elliptic curve of conductor 37
            sage: P = y.kolyvagin_point(); P
            Kolyvagin point of discriminant -7 on elliptic curve of conductor 37
            sage: P.numerical_approx()  # abs tol 1e-15
            (-3.36910401903861e-16 - 2.22076195576076e-16*I
             : 3.33066907387547e-16 + 2.22076195576075e-16*I : 1.00000000000000)
        """
    def curve(self):
        """
        Return the elliptic curve on which this is a Heegner point.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5)
            sage: P.curve()
            Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field
            sage: P.curve() is E
            True
        """
    @cached_method
    def quadratic_form(self):
        """
        Return the integral primitive positive definite binary
        quadratic form associated to this Heegner point.

        EXAMPLES::

            sage: EllipticCurve('389a').heegner_point(-7, 5).quadratic_form()
            389*x^2 + 147*x*y + 14*y^2

            sage: P = EllipticCurve('389a').heegner_point(-7, 5, (778,925,275)); P
            Heegner point of discriminant -7 and conductor 5 on elliptic curve
             of conductor 389
            sage: P.quadratic_form()
            778*x^2 + 925*x*y + 275*y^2
        """
    @cached_method
    def numerical_approx(self, prec: int = 53, algorithm=None):
        """
        Return a numerical approximation to this Heegner point
        computed using a working precision of prec bits.

        .. WARNING::

            The answer is *not* provably correct to prec bits!  A
            priori, due to rounding and other errors, it is possible that
            not a single digit is correct.

        INPUT:

        - prec     -- (default: ``None``) the working precision

        EXAMPLES::

            sage: E = EllipticCurve('37a'); P = E.heegner_point(-7); P
            Heegner point of discriminant -7 on elliptic curve of conductor 37
            sage: P.numerical_approx()  # abs tol 1e-15
            (-3.36910401903861e-16 - 2.22076195576076e-16*I
             : 3.33066907387547e-16 + 2.22076195576075e-16*I : 1.00000000000000)
            sage: P.numerical_approx(10)  # expect random digits
            (0.0030 - 0.0028*I : -0.0030 + 0.0028*I : 1.0)
            sage: P.numerical_approx(100)[0]  # expect random digits
            8.4...e-31 + 6.0...e-31*I
            sage: E = EllipticCurve('37a'); P = E.heegner_point(-40); P
            Heegner point of discriminant -40 on elliptic curve of conductor 37
            sage: P.numerical_approx()  # abs tol 1e-14
            (-3.15940603400359e-16 + 1.41421356237309*I
             : 1.00000000000000 - 1.41421356237309*I : 1.00000000000000)

        A rank 2 curve, where all Heegner points of conductor 1 are 0::

            sage: E = EllipticCurve('389a'); E.rank()
            2
            sage: P = E.heegner_point(-7); P
            Heegner point of discriminant -7 on elliptic curve of conductor 389
            sage: P.numerical_approx()
            (0.000000000000000 : 1.00000000000000 : 0.000000000000000)

        However, Heegner points of bigger conductor are often nonzero::

            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5); P
            Heegner point of discriminant -7 and conductor 5 on elliptic curve
             of conductor 389
            sage: numerical_approx(P)
            (0.675507556926807 + 0.344749649302635*I
             : -0.377142931401887 + 0.843366227137146*I : 1.00000000000000)
            sage: P.numerical_approx()
            (0.6755075569268... + 0.3447496493026...*I
             : -0.3771429314018... + 0.8433662271371...*I : 1.00000000000000)
            sage: E.heegner_point(-7, 11).numerical_approx()
            (0.1795583794118... + 0.02035501750912...*I
             : -0.5573941377055... + 0.2738940831635...*I : 1.00000000000000)
            sage: E.heegner_point(-7, 13).numerical_approx()
            (1.034302915374... - 3.302744319777...*I
             : 1.323937875767... + 6.908264226850...*I : 1.00000000000000)

        We find (probably) the defining polynomial of the
        `x`-coordinate of `P`, which defines a class field.  The shape of
        the discriminant below is strong confirmation -- but not proof
        -- that this polynomial is correct::

            sage: f = P.numerical_approx(70)[0].algebraic_dependency(6); f
            1225*x^6 + 1750*x^5 - 21675*x^4 - 380*x^3 + 110180*x^2 - 129720*x + 48771
            sage: f.discriminant().factor()
            2^6 * 3^2 * 5^11 * 7^4 * 13^2 * 19^6 * 199^2 * 719^2 * 26161^2
        """
    def tau(self):
        """
        Return `\\tau` in the upper half plane that maps via the
        modular parametrization to this Heegner point.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5)
            sage: P.tau()
            5/778*sqrt_minus_7 - 147/778
        """
    @cached_method
    def x_poly_exact(self, prec: int = 53, algorithm: str = 'lll'):
        """
        Return irreducible polynomial over the rational numbers
        satisfied by the `x` coordinate of this Heegner point.  A
        :exc:`ValueError` is raised if the precision is clearly insignificant
        to define a point on the curve.

        .. WARNING::

            It is in theory possible for this function to not raise a
            :exc:`ValueError`, find a polynomial, but via some very unlikely
            coincidence that point is not actually this Heegner point.

        INPUT:

        - ``prec`` -- integer (default: 53)

        - ``algorithm`` -- 'conjugates' or 'lll' (default); if
          'conjugates', compute numerically all the
          conjugates ``y[i]`` of the Heegner point and construct
          the characteristic polynomial as the product
          `f(X)=(X-y[i])`.  If 'lll', compute only one of the
          conjugates ``y[0]``, then uses the LLL algorithm to
          guess `f(X)`.

        EXAMPLES:

        We compute some `x`-coordinate polynomials of some conductor 1
        Heegner points::

            sage: E = EllipticCurve('37a')
            sage: v = E.heegner_discriminants_list(10)
            sage: [E.heegner_point(D).x_poly_exact() for D in v]
            [x, x, x^2 + 2, x^5 - x^4 + x^3 + x^2 - 2*x + 1, x - 6,
             x^7 - 2*x^6 + 9*x^5 - 10*x^4 - x^3 + 8*x^2 - 5*x + 1,
             x^3 + 5*x^2 + 10*x + 4, x^4 - 10*x^3 + 10*x^2 + 12*x - 12,
             x^8 - 5*x^7 + 7*x^6 + 13*x^5 - 10*x^4 - 4*x^3 + x^2 - 5*x + 7,
             x^6 - 2*x^5 + 11*x^4 - 24*x^3 + 30*x^2 - 16*x + 4]

        We compute `x`-coordinate polynomials for some Heegner points
        of conductor bigger than 1 on a rank 2 curve::

            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5); P
            Heegner point of discriminant -7 and conductor 5
             on elliptic curve of conductor 389
            sage: P.x_poly_exact()
            Traceback (most recent call last):
            ...
            ValueError: insufficient precision to determine Heegner point
            (fails discriminant test)
            sage: P.x_poly_exact(120)
            x^6 + 10/7*x^5 - 867/49*x^4 - 76/245*x^3 + 3148/35*x^2 - 25944/245*x + 48771/1225
            sage: E.heegner_point(-7, 11).x_poly_exact(500)
            x^10 + 282527/52441*x^9 + 27049007420/2750058481*x^8 - 22058564794/2750058481*x^7
             - 140054237301/2750058481*x^6 + 696429998952/30250643291*x^5
             + 2791387923058/30250643291*x^4 - 3148473886134/30250643291*x^3
             + 1359454055022/30250643291*x^2 - 250620385365/30250643291*x
             + 181599685425/332757076201

        Here we compute a Heegner point of conductor 5 on a rank 3 curve::

            sage: E = EllipticCurve('5077a'); P = E.heegner_point(-7,5); P
            Heegner point of discriminant -7 and conductor 5
             on elliptic curve of conductor 5077
            sage: P.x_poly_exact(500)
            x^6 + 1108754853727159228/72351048803252547*x^5 + 88875505551184048168/1953478317687818769*x^4 - 2216200271166098662132/3255797196146364615*x^3 + 14941627504168839449851/9767391588439093845*x^2 - 3456417460183342963918/3255797196146364615*x + 1306572835857500500459/5426328660243941025

        See :issue:`34121`::

            sage: E = EllipticCurve('11a1')
            sage: P = E.heegner_point(-7)
            sage: PE = P.point_exact()
            sage: PE
            (a : -4*a + 3 : 1)
            sage: all(c.parent().disc() == -7 for c in PE)
            True
        """
    def point_exact(self, prec: int = 53, algorithm: str = 'lll', var: str = 'a', optimize: bool = False):
        """
        Return exact point on the elliptic curve over a number field
        defined by computing this Heegner point to the given number of
        bits of precision. A :exc:`ValueError` is raised if the precision
        is clearly insignificant to define a point on the curve.

        .. WARNING::

            It is in theory possible for this function to not raise a
            :exc:`ValueError`, find a point on the curve, but via some very
            unlikely coincidence that point is not actually this Heegner point.

        .. WARNING::

            Currently we make an arbitrary choice of `y`-coordinate for
            the lift of the `x`-coordinate.

        INPUT:

        - ``prec`` -- integer (default: 53)

        - ``algorithm`` -- see the description of the algorithm
          parameter for the ``x_poly_exact`` method

        - ``var`` -- string (default: ``'a'``)

        - ``optimize`` -- boolean (default: ``False``); if ``True``, try to
          optimize defining polynomial for the number field that
          the point is defined over.  Off by default, since this
          can be very expensive.

        EXAMPLES::

            sage: E = EllipticCurve('389a'); P = E.heegner_point(-7, 5); P
            Heegner point of discriminant -7 and conductor 5
             on elliptic curve of conductor 389
            sage: z = P.point_exact(200, optimize=True)
            sage: z[1].charpoly()
            x^12 + 6*x^11 + 90089/1715*x^10 + 71224/343*x^9 + 52563964/588245*x^8 - 483814934/588245*x^7 - 156744579/16807*x^6 - 2041518032/84035*x^5 + 1259355443184/14706125*x^4 + 3094420220918/14706125*x^3 + 123060442043827/367653125*x^2 + 82963044474852/367653125*x + 211679465261391/1838265625
            sage: f = P.numerical_approx(500)[1].algebraic_dependency(12); f / f.leading_coefficient()
            x^12 + 6*x^11 + 90089/1715*x^10 + 71224/343*x^9 + 52563964/588245*x^8 - 483814934/588245*x^7 - 156744579/16807*x^6 - 2041518032/84035*x^5 + 1259355443184/14706125*x^4 + 3094420220918/14706125*x^3 + 123060442043827/367653125*x^2 + 82963044474852/367653125*x + 211679465261391/1838265625

            sage: E = EllipticCurve('5077a')
            sage: P = E.heegner_point(-7)
            sage: P.point_exact(prec=100)
            (0 : 1 : 0)
        """
    @cached_method
    def conjugates_over_K(self):
        """
        Return the `Gal(K_c/K)` conjugates of this Heegner point.

        EXAMPLES::

            sage: E = EllipticCurve('77a')
            sage: y = E.heegner_point(-52,5); y
            Heegner point of discriminant -52 and conductor 5
             on elliptic curve of conductor 77
            sage: print([z.quadratic_form() for z in y.conjugates_over_K()])
            [77*x^2 + 52*x*y + 13*y^2, 154*x^2 + 206*x*y + 71*y^2, 539*x^2 + 822*x*y + 314*y^2,
             847*x^2 + 1284*x*y + 487*y^2, 1001*x^2 + 52*x*y + y^2, 1078*x^2 + 822*x*y + 157*y^2,
             1309*x^2 + 360*x*y + 25*y^2, 1309*x^2 + 2054*x*y + 806*y^2,
             1463*x^2 + 976*x*y + 163*y^2, 2233*x^2 + 2824*x*y + 893*y^2,
             2387*x^2 + 2054*x*y + 442*y^2, 3619*x^2 + 3286*x*y + 746*y^2]
            sage: y.quadratic_form()
            77*x^2 + 52*x*y + 13*y^2
        """
    def kolyvagin_cohomology_class(self, n=None):
        """
        Return the Kolyvagin class associated to this Heegner point.

        INPUT:

        - ``n`` -- positive integer that divides the gcd of `a_p`
          and `p+1` for all `p` dividing the conductor.  If `n` is
          ``None``, choose the largest valid `n`.

        EXAMPLES::

            sage: y = EllipticCurve('389a').heegner_point(-7,5)
            sage: y.kolyvagin_cohomology_class(3)
            Kolyvagin cohomology class c(5) in H^1(K,E[3])
        """

class KolyvaginPoint(HeegnerPoint):
    """
    A Kolyvagin point.

    EXAMPLES:

    We create a few Kolyvagin points::

        sage: EllipticCurve('11a1').kolyvagin_point(-7)
        Kolyvagin point of discriminant -7 on elliptic curve of conductor 11
        sage: EllipticCurve('37a1').kolyvagin_point(-7)
        Kolyvagin point of discriminant -7 on elliptic curve of conductor 37
        sage: EllipticCurve('37a1').kolyvagin_point(-67)
        Kolyvagin point of discriminant -67 on elliptic curve of conductor 37
        sage: EllipticCurve('389a1').kolyvagin_point(-7, 5)
        Kolyvagin point of discriminant -7 and conductor 5
         on elliptic curve of conductor 389

    One can also associated a Kolyvagin point to a Heegner point::

        sage: y = EllipticCurve('37a1').heegner_point(-7); y
        Heegner point of discriminant -7 on elliptic curve of conductor 37
        sage: y.kolyvagin_point()
        Kolyvagin point of discriminant -7 on elliptic curve of conductor 37

    TESTS::

        sage: y = EllipticCurve('37a1').heegner_point(-7)
        sage: type(y)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerPointOnEllipticCurve'>
        sage: loads(dumps(y)) == y
        True
    """
    def __init__(self, heegner_point) -> None:
        """
        Create a Kolyvagin point.

        INPUT:

            - ``heegner_point`` -- a Heegner point on some elliptic curve

        EXAMPLES:

        We directly construct a Kolyvagin point from the KolyvaginPoint class::

            sage: y = EllipticCurve('37a1').heegner_point(-7)
            sage: sage.schemes.elliptic_curves.heegner.KolyvaginPoint(y)
            Kolyvagin point of discriminant -7 on elliptic curve of conductor 37
        """
    def satisfies_kolyvagin_hypothesis(self, n=None):
        """
        Return ``True`` if this Kolyvagin point satisfies the Heegner
        hypothesis for `n`, so that it defines a Galois equivariant
        element of `E(K_c)/n E(K_c)`.

        EXAMPLES::

            sage: y = EllipticCurve('389a').heegner_point(-7,5); P = y.kolyvagin_point()
            sage: P.kolyvagin_cohomology_class(3)
            Kolyvagin cohomology class c(5) in H^1(K,E[3])
            sage: P.satisfies_kolyvagin_hypothesis(3)
            True
            sage: P.satisfies_kolyvagin_hypothesis(5)
            False
            sage: P.satisfies_kolyvagin_hypothesis(7)
            False
            sage: P.satisfies_kolyvagin_hypothesis(11)
            False
        """
    def curve(self):
        """
        Return the elliptic curve over `\\QQ` on which this Kolyvagin
        point sits.

        EXAMPLES::

            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67, 3)
            sage: P.curve()
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        """
    def heegner_point(self):
        """
        This Kolyvagin point `P_c` is associated to some Heegner point
        `y_c` via Kolyvagin's construction.  This function returns that
        point `y_c`.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: P = E.kolyvagin_point(-67); P
            Kolyvagin point of discriminant -67 on elliptic curve of conductor 37
            sage: y = P.heegner_point(); y
            Heegner point of discriminant -67 on elliptic curve of conductor 37
            sage: y.kolyvagin_point() is P
            True
        """
    def index(self, *args, **kwds):
        """
        Return index of this Kolyvagin point in the full group of
        `K_c` rational points on `E`.

        When the conductor is 1, this is computed numerically using
        the Gross-Zagier formula and explicit point search, and it may
        be off by `2`. See the documentation for ``E.heegner_index``,
        where `E` is the curve attached to ``self``.

        EXAMPLES::

            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67); P.index()
            6
        """
    def numerical_approx(self, prec: int = 53):
        """
        Return a numerical approximation to this Kolyvagin point using
        prec bits of working precision.

        INPUT:

        - ``prec`` -- precision in bits (default: 53)

        EXAMPLES::

            sage: P = EllipticCurve('37a1').kolyvagin_point(-7); P
            Kolyvagin point of discriminant -7 on elliptic curve of conductor 37
            sage: P.numerical_approx() # approx. (0 : 0 : 1)
            (...e-16 - ...e-16*I : ...e-16 + ...e-16*I : 1.00000000000000)
            sage: P.numerical_approx(100)[0].abs() < 2.0^-99
            True

            sage: P = EllipticCurve('389a1').kolyvagin_point(-7, 5); P
            Kolyvagin point of discriminant -7 and conductor 5
             on elliptic curve of conductor 389

        Numerical approximation is only implemented for points of conductor 1::

            sage: P.numerical_approx()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def point_exact(self, prec: int = 53):
        """
        INPUT:

        - ``prec`` -- precision in bits (default: 53)

        EXAMPLES:

        A rank 1 curve::

            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67)
            sage: P.point_exact()
            (6 : -15 : 1)
            sage: P.point_exact(40)
            (6 : -15 : 1)
            sage: P.point_exact(20)
            Traceback (most recent call last):
            ...
            RuntimeError: insufficient precision to find exact point

        A rank 0 curve::

            sage: E = EllipticCurve('11a1'); P = E.kolyvagin_point(-7)
            sage: P.point_exact()
            (-1/2*sqrt_minus_7 + 1/2 : -2*sqrt_minus_7 - 2 : 1)

        A rank 2 curve::

            sage: E = EllipticCurve('389a1'); P = E.kolyvagin_point(-7)
            sage: P.point_exact()
            (0 : 1 : 0)
        """
    def plot(self, prec: int = 53, *args, **kwds):
        """
        Plot a Kolyvagin point `P_1` if it is defined over the
        rational numbers.

        EXAMPLES::

            sage: E = EllipticCurve('37a'); P = E.heegner_point(-11).kolyvagin_point()
            sage: P.plot(prec=30, pointsize=50, rgbcolor='red') + E.plot()              # needs sage.plot
            Graphics object consisting of 3 graphics primitives
        """
    @cached_method
    def trace_to_real_numerical(self, prec: int = 53):
        """
        Return the trace of this Kolyvagin point down to the real
        numbers, computed numerically using prec bits of working
        precision.

        EXAMPLES::

            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67)
            sage: PP = P.numerical_approx()
            sage: [c.real() for c in PP]
            [6.00000000000000, -15.0000000000000, 1.00000000000000]
            sage: all(c.imag().abs() < 1e-14 for c in PP)
            True
            sage: P.trace_to_real_numerical()
            (1.61355529131986 : -2.18446840788880 : 1.00000000000000)
            sage: P.trace_to_real_numerical(prec=80)  # abs tol 1e-21
            (1.6135552913198573127230 : -2.1844684078888023289187 : 1.0000000000000000000000)
        """
    def mod(self, p, prec: int = 53):
        """
        Return the trace of the reduction `Q` modulo a prime over `p` of this
        Kolyvagin point as an element of `E(\\GF{p})`, where
        `p` is any prime that is inert in `K` that is coprime to `NDc`.

        The point `Q` is only well defined up to an element of
        `(p+1) E(\\GF{p})`, i.e., it gives a well defined element
        of the abelian group `E(\\GF{p}) / (p+1) E(\\GF{p})`.

        See [St2011b]_, Proposition 5.4 for a proof of the above
        well-definedness assertion.

        EXAMPLES:

        A Kolyvagin point on a rank 1 curve::

            sage: E = EllipticCurve('37a1'); P = E.kolyvagin_point(-67)
            sage: P.mod(2)
            (1 : 1 : 1)
            sage: P.mod(3)
            (1 : 0 : 1)
            sage: P.mod(5)
            (2 : 2 : 1)
            sage: P.mod(7)
            (6 : 0 : 1)
            sage: P.trace_to_real_numerical()
            (1.61355529131986 : -2.18446840788880 : 1.00000000000000)
            sage: P._trace_exact_conductor_1()  # the actual point we're reducing
            (1357/841 : -53277/24389 : 1)
            sage: (P._trace_exact_conductor_1().height() / E.regulator()).sqrt()
            12.0000000000000

        Here the Kolyvagin point is a torsion point (since `E` has
        rank 1), and we reduce it modulo several primes.::

            sage: E = EllipticCurve('11a1'); P = E.kolyvagin_point(-7)
            sage: P.mod(3,70)  # long time (4s on sage.math, 2013)
            (1 : 2 : 1)
            sage: P.mod(5,70)
            (1 : 4 : 1)
            sage: P.mod(7,70)
            Traceback (most recent call last):
            ...
            ValueError: p must be coprime to conductors and discriminant
            sage: P.mod(11,70)
            Traceback (most recent call last):
            ...
            ValueError: p must be coprime to conductors and discriminant
            sage: P.mod(13,70)
            (3 : 4 : 1)
        """
    def kolyvagin_cohomology_class(self, n=None):
        """
        INPUT:

        - ``n`` -- positive integer that divides the gcd of `a_p`
          and `p+1` for all `p` dividing the conductor.  If `n` is
          ``None``, choose the largest valid `n`.

        EXAMPLES::

            sage: y = EllipticCurve('389a').heegner_point(-7, 5)
            sage: P = y.kolyvagin_point()
            sage: P.kolyvagin_cohomology_class(3)
            Kolyvagin cohomology class c(5) in H^1(K,E[3])

            sage: y = EllipticCurve('37a').heegner_point(-7, 5).kolyvagin_point()
            sage: y.kolyvagin_cohomology_class()
            Kolyvagin cohomology class c(5) in H^1(K,E[2])
        """

class KolyvaginCohomologyClass(SageObject):
    """
    A Kolyvagin cohomology class in `H^1(K,E[n])` or `H^1(K,E)[n]`
    attached to a Heegner point.

    EXAMPLES::

        sage: y = EllipticCurve('37a').heegner_point(-7)
        sage: c = y.kolyvagin_cohomology_class(3); c
        Kolyvagin cohomology class c(1) in H^1(K,E[3])
        sage: type(c)
        <class 'sage.schemes.elliptic_curves.heegner.KolyvaginCohomologyClassEn'>
        sage: loads(dumps(c)) == c
        True
        sage: y.kolyvagin_cohomology_class(5)
        Kolyvagin cohomology class c(1) in H^1(K,E[5])
    """
    def __init__(self, kolyvagin_point, n) -> None:
        """

        EXAMPLES::

            sage: y = EllipticCurve('389a').heegner_point(-7, 5)
            sage: y.kolyvagin_cohomology_class(3)
            Kolyvagin cohomology class c(5) in H^1(K,E[3])
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: y = EllipticCurve('37a').heegner_point(-7)
            sage: c = y.kolyvagin_cohomology_class(3)
            sage: c == y.kolyvagin_cohomology_class(3)
            True
            sage: c == y.kolyvagin_cohomology_class(5)
            False

        This does not mean that c is nonzero (!) -- it just means c is not the number 0::

            sage: c == 0
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: y = EllipticCurve('37a').heegner_point(-7)
            sage: c = y.kolyvagin_cohomology_class(3)
            sage: c != y.kolyvagin_cohomology_class(3)
            False
            sage: c != y.kolyvagin_cohomology_class(5)
            True
        """
    def n(self):
        """
        Return the integer `n` so that this is a cohomology class in
        `H^1(K,E[n])` or `H^1(K,E)[n]`.

        EXAMPLES::

            sage: y = EllipticCurve('37a').heegner_point(-7)
            sage: t = y.kolyvagin_cohomology_class(3); t
            Kolyvagin cohomology class c(1) in H^1(K,E[3])
            sage: t.n()
            3
        """
    def conductor(self):
        """
        Return the integer `c` such that this cohomology class is associated
        to the Heegner point `y_c`.

        EXAMPLES::

            sage: y = EllipticCurve('37a').heegner_point(-7, 5)
            sage: t = y.kolyvagin_cohomology_class()
            sage: t.conductor()
            5
        """
    def kolyvagin_point(self):
        """
        Return the Kolyvagin point `P_c` to which this cohomology
        class is associated.

        EXAMPLES::

            sage: y = EllipticCurve('37a').heegner_point(-7, 5)
            sage: t = y.kolyvagin_cohomology_class()
            sage: t.kolyvagin_point()
            Kolyvagin point of discriminant -7 and conductor 5
             on elliptic curve of conductor 37
        """
    def heegner_point(self):
        """
        Return the Heegner point `y_c` to which this cohomology class
        is associated.

        EXAMPLES::

            sage: y = EllipticCurve('37a').heegner_point(-7, 5)
            sage: t = y.kolyvagin_cohomology_class()
            sage: t.heegner_point()
            Heegner point of discriminant -7 and conductor 5
             on elliptic curve of conductor 37
        """

class KolyvaginCohomologyClassEn(KolyvaginCohomologyClass): ...

class HeegnerQuatAlg(SageObject):
    """
    Heegner points viewed as supersingular points on the modular curve
    `X_0(N)/\\mathbf{F}_{\\ell}`.

    EXAMPLES::

        sage: H = heegner_points(11).reduce_mod(13); H
        Heegner points on X_0(11) over F_13
        sage: type(H)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerQuatAlg'>
        sage: loads(dumps(H)) == H
        True
    """
    def __init__(self, level, ell) -> None:
        """
        INPUT:

        - ``level`` -- the level (a positive integer)

        - `\\ell` -- the characteristic, a prime coprime to the level

        EXAMPLES::

            sage: sage.schemes.elliptic_curves.heegner.HeegnerQuatAlg(11, 13)
            Heegner points on X_0(11) over F_13
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3)
            sage: H == heegner_points(11).reduce_mod(3)
            True
            sage: H == heegner_points(11).reduce_mod(5)
            False
            sage: H == 0
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3)
            sage: H != heegner_points(11).reduce_mod(3)
            False
            sage: H != heegner_points(11).reduce_mod(5)
            True
            sage: H != 0
            True
        """
    def level(self):
        """
        Return the level.

        EXAMPLES::

            sage: heegner_points(11).reduce_mod(3).level()
            11
        """
    def ell(self):
        """
        Return the prime `\\ell` modulo which we are working.

        EXAMPLES::

            sage: heegner_points(11).reduce_mod(3).ell()
            3
        """
    def satisfies_heegner_hypothesis(self, D, c=...):
        """
        The fundamental discriminant `D` must be coprime to `N\\ell`,
        and must define a quadratic imaginary field `K` in which `\\ell`
        is inert.  Also, all primes dividing `N` must split in `K`,
        and `c` must be squarefree and coprime to `ND\\ell`.

        INPUT:

        - ``D`` -- negative integer

        - ``c`` -- positive integer (default: 1)

        OUTPUT: boolean

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(7)
            sage: H.satisfies_heegner_hypothesis(-5)
            False
            sage: H.satisfies_heegner_hypothesis(-7)
            False
            sage: H.satisfies_heegner_hypothesis(-8)
            True
            sage: [D for D in [-1,-2..-100] if H.satisfies_heegner_hypothesis(D)]
            [-8, -39, -43, -51, -79, -95]
        """
    def heegner_discriminants(self, n: int = 5):
        """
        Return the first `n` negative fundamental discriminants
        coprime to `N\\ell` such that `\\ell` is inert in the
        corresponding quadratic imaginary field and that field
        satisfies the Heegner hypothesis, and `N` is the level.

        INPUT:

        - ``n`` -- positive integer (default: 5)

        OUTPUT: list

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3)
            sage: H.heegner_discriminants()
            [-7, -19, -40, -43, -52]
            sage: H.heegner_discriminants(10)
            [-7, -19, -40, -43, -52, -79, -127, -139, -151, -184]
        """
    def heegner_conductors(self, D, n: int = 5):
        """
        Return the first `n` negative fundamental discriminants
        coprime to `N\\ell` such that `\\ell` is inert in the
        corresponding quadratic imaginary field and that field
        satisfies the Heegner hypothesis.

        INPUT:

        - ``D`` -- negative integer; a fundamental Heegner discriminant

        - ``n`` -- positive integer (default: 5)

        OUTPUT: list

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3)
            sage: H.heegner_conductors(-7)
            [1, 2, 4, 5, 8]
            sage: H.heegner_conductors(-7, 10)
            [1, 2, 4, 5, 8, 10, 13, 16, 17, 19]
        """
    def optimal_embeddings(self, D, c, R):
        """
        INPUT:

        - ``D`` -- negative fundamental discriminant

        - ``c`` -- integer coprime

        - ``R`` -- Eichler order

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3)
            sage: R = H.left_orders()[0]
            sage: H.optimal_embeddings(-7, 1, R)
            [Embedding sending sqrt(-7) to i - j - k,
             Embedding sending sqrt(-7) to -i + j + k]
            sage: H.optimal_embeddings(-7, 2, R)
            [Embedding sending 2*sqrt(-7) to 5*i - k,
             Embedding sending 2*sqrt(-7) to -5*i + k,
             Embedding sending 2*sqrt(-7) to 2*i - 2*j - 2*k,
             Embedding sending 2*sqrt(-7) to -2*i + 2*j + 2*k]
        """
    @cached_method
    def brandt_module(self):
        """
        Return the Brandt module of right ideal classes that we
        used to represent the set of supersingular points on
        the modular curve.

        EXAMPLES::

            sage: heegner_points(11).reduce_mod(3).brandt_module()
            Brandt module of dimension 2 of level 3*11 of weight 2 over Rational Field
        """
    @cached_method
    def quaternion_algebra(self):
        """
        Return the rational quaternion algebra used to implement ``self``.

        EXAMPLES::

            sage: heegner_points(389).reduce_mod(7).quaternion_algebra()
            Quaternion Algebra (-1, -7) with base ring Rational Field
        """
    def right_ideals(self):
        """
        Return representative right ideals in the Brandt module.

        EXAMPLES::

            sage: heegner_points(11).reduce_mod(3).right_ideals()
            (Fractional ideal (4, 44*i, 2 + 8*i + 2*j, 34*i + 2*k),
             Fractional ideal (8, 88*i, 2 + 52*i + 2*j, 4 + 78*i + 2*k))
        """
    @cached_method
    def left_orders(self):
        """
        Return the left orders associated to the representative right
        ideals in the Brandt module.

        EXAMPLES::

            sage: heegner_points(11).reduce_mod(3).left_orders()
            [Order of Quaternion Algebra (-1, -3) with base ring Rational Field
              with basis (1/2 + 1/2*j + 7*k, 1/2*i + 13/2*k, j + 3*k, 11*k),
             Order of Quaternion Algebra (-1, -3) with base ring Rational Field
              with basis (1/2 + 1/2*j + 7*k, 1/4*i + 1/2*j + 63/4*k, j + 14*k, 22*k)]
        """
    @cached_method
    def heegner_divisor(self, D, c=...):
        """
        Return Heegner divisor as an element of the Brandt module
        corresponding to the discriminant `D` and conductor `c`, which
        both must be coprime to `N\\ell`.

        More precisely, we compute the sum of the reductions of the
        `\\textrm{Gal}(K_1/K)`-conjugates of each choice of `y_1`,
        where the choice comes from choosing the ideal `\\mathcal{N}`.
        Then we apply the Hecke operator `T_c` to this sum.

        INPUT:

        - ``D`` -- discriminant (negative integer)

        - ``c`` -- conductor (positive integer)

        OUTPUT: a Brandt module element

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(7)
            sage: H.heegner_discriminants()
            [-8, -39, -43, -51, -79]
            sage: H.heegner_divisor(-8)
            (1, 0, 0, 1, 0, 0)
            sage: H.heegner_divisor(-39)
            (1, 2, 2, 1, 2, 0)
            sage: H.heegner_divisor(-43)
            (1, 0, 0, 1, 0, 0)
            sage: H.heegner_divisor(-51)
            (1, 0, 0, 1, 0, 2)
            sage: H.heegner_divisor(-79)
            (3, 2, 2, 3, 0, 0)

            sage: sum(H.heegner_divisor(-39).element())
            8
            sage: QuadraticField(-39,'a').class_number()
            4
        """
    @cached_method
    def modp_splitting_data(self, p):
        """
        Return mod `p` splitting data for the quaternion algebra at the
        unramified prime `p`.  This is a pair of `2\\times 2` matrices
        `A`, `B` over the finite field `\\GF{p}` such that if the
        quaternion algebra has generators `i, j, k`, then the
        homomorphism sending `i` to `A` and `j` to `B` maps any
        maximal order homomorphically onto the ring of `2\\times 2` matrices.

        Because of how the homomorphism is defined, we must assume that the
        prime `p` is odd.

        INPUT:

        - ``p`` -- unramified odd prime

        OUTPUT: a 2-tuple of matrices over finite field

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(7)
            sage: H.quaternion_algebra()
            Quaternion Algebra (-1, -7) with base ring Rational Field
            sage: I, J = H.modp_splitting_data(13)
            sage: I
            [ 0 12]
            [ 1  0]
            sage: J
            [7 3]
            [3 6]
            sage: I^2
            [12  0]
            [ 0 12]
            sage: J^2
            [6 0]
            [0 6]
            sage: I*J == -J*I
            True

        The following is a good test because of the asserts in the code::

            sage: v = [H.modp_splitting_data(p) for p in primes(13,200)]

        Some edge cases::

            sage: H.modp_splitting_data(11)
            (
            [ 0 10]  [6 1]
            [ 1  0], [1 5]
            )

        Proper error handling::

            sage: H.modp_splitting_data(7)
            Traceback (most recent call last):
            ...
            ValueError: p (=7) must be an unramified prime

            sage: H.modp_splitting_data(2)
            Traceback (most recent call last):
            ...
            ValueError: p must be odd
        """
    def modp_splitting_map(self, p):
        """
        Return (algebra) map from the (`p`-integral) quaternion algebra to
        the set of `2\\times 2` matrices over `\\GF{p}`.

        INPUT:

        - ``p`` -- prime number

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(7)
            sage: f = H.modp_splitting_map(13)
            sage: B = H.quaternion_algebra(); B
            Quaternion Algebra (-1, -7) with base ring Rational Field
            sage: i, j, k = H.quaternion_algebra().gens()
            sage: a = 2 + i - j + 3*k; b = 7 + 2*i - 4*j + k
            sage: f(a*b)
            [12  3]
            [10  5]
            sage: f(a)*f(b)
            [12  3]
            [10  5]
        """
    def cyclic_subideal_p1(self, I, c):
        """
        Compute dictionary mapping 2-tuples that defined normalized
        elements of `P^1(\\ZZ/c\\ZZ)`

        INPUT:

        - ``I`` -- right ideal of Eichler order or in quaternion algebra

        - ``c`` -- square free integer (currently must be odd prime
          and coprime to level, discriminant, characteristic, etc.

        OUTPUT:

        - dictionary mapping 2-tuples (u,v) to ideals

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(7)
            sage: I = H.brandt_module().right_ideals()[0]
            sage: sorted(H.cyclic_subideal_p1(I, 3).items())
            [((0, 1), Fractional ideal (12, 132*i, 10 + 76*i + 2*j, 4 + 86*i + 2*k)),
             ((1, 0), Fractional ideal (12, 132*i, 2 + 32*i + 2*j, 8 + 130*i + 2*k)),
             ((1, 1), Fractional ideal (12, 132*i, 10 + 32*i + 2*j, 8 + 86*i + 2*k)),
             ((1, 2), Fractional ideal (12, 132*i, 2 + 76*i + 2*j, 4 + 130*i + 2*k))]
            sage: len(H.cyclic_subideal_p1(I, 17))
            18
        """
    @cached_method
    def galois_group_over_hilbert_class_field(self, D, c):
        """
        Return the Galois group of the extension of ring class fields
        `K_c` over the Hilbert class field `K_{1}` of the quadratic
        imaginary field of discriminant `D`.

        INPUT:

        - ``D`` -- fundamental discriminant

        - ``c`` -- conductor (square-free integer)

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; c = 41; p = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: H.galois_group_over_hilbert_class_field(D, c)
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 41
             over Hilbert class field of QQ[sqrt(-7)]
        """
    @cached_method
    def galois_group_over_quadratic_field(self, D, c):
        """
        Return the Galois group of the extension of ring class fields
        `K_c` over the quadratic imaginary field `K` of discriminant `D`.

        INPUT:

        - ``D`` -- fundamental discriminant

        - ``c`` -- conductor (square-free integer)

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; c = 41; p = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: H.galois_group_over_quadratic_field(D, c)
            Galois group of Ring class field extension of QQ[sqrt(-7)] of conductor 41
             over Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
              with sqrt_minus_7 = 2.645751311064591?*I
        """
    @cached_method
    def quadratic_field(self, D):
        """
        Return our fixed choice of quadratic imaginary field of
        discriminant `D`.

        INPUT:

        - ``D`` -- fundamental discriminant

        OUTPUT: a quadratic number field

        EXAMPLES::

            sage: H = heegner_points(389).reduce_mod(5)
            sage: H.quadratic_field(-7)
            Number Field in sqrt_minus_7 with defining polynomial x^2 + 7
             with sqrt_minus_7 = 2.645751311064591?*I
        """
    @cached_method
    def kolyvagin_cyclic_subideals(self, I, p, alpha_quaternion):
        """
        Return list of pairs `(J, n)` where `J` runs through the
        cyclic subideals of `I` of index `(\\ZZ/p\\ZZ)^2`, and `J \\sim
        \\alpha^n(J_0)` for some fixed choice of cyclic subideal `J_0`.

        INPUT:

        - ``I`` -- right ideal of the quaternion algebra

        - ``p`` -- prime number

        - ``alpha_quaternion`` -- image in the quaternion algebra
          of generator `\\alpha` for `(\\mathcal{O}_K / c\\mathcal{O}_K)^* / (\\ZZ/c\\ZZ)^*`

        OUTPUT: list of 2-tuples

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; c = 5
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: I = H.brandt_module().right_ideals()[49]
            sage: f = H.optimal_embeddings(D, 1, I.left_order())[1]
            sage: g = H.kolyvagin_generators(f.domain().number_field(), c)
            sage: alpha_quaternion = f(g[0]); alpha_quaternion
            1 - 77/192*i - 5/128*j - 137/384*k
            sage: H.kolyvagin_cyclic_subideals(I, 5, alpha_quaternion)
            [(Fractional ideal (2560, 1280 + 47360*i, 1146 + 37678*i + 4*j, 212 + 54664/3*i + 2*j + 2/3*k), 0),
             (Fractional ideal (2560, 1280 + 47360*i, 2426 + 9262*i + 4*j, 2004 + 83080/3*i + 2*j + 2/3*k), 1),
             (Fractional ideal (2560, 1280 + 47360*i, 1914 + 9262*i + 4*j, 1748 + 111496/3*i + 2*j + 2/3*k), 2),
             (Fractional ideal (2560, 1280 + 47360*i, 2170 + 18734*i + 4*j, 212 + 111496/3*i + 2*j + 2/3*k), 3),
             (Fractional ideal (2560, 1280 + 47360*i, 890 + 28206*i + 4*j, 1748 + 54664/3*i + 2*j + 2/3*k), 4),
             (Fractional ideal (2560, 1280 + 47360*i, 634 + 37678*i + 4*j, 2516 + 83080/3*i + 2*j + 2/3*k), 5)]
        """
    @cached_method
    def kolyvagin_generator(self, K, p):
        """
        Return element in `K` that maps to the multiplicative generator
        for the quotient group

           `(\\mathcal{O}_K / p \\mathcal{O}_K)^* / (\\ZZ/p\\ZZ)^*`

        of the form `\\sqrt{D}+n` with `n\\geq 1` minimal.

        INPUT:

        - ``K`` -- quadratic imaginary field

        - ``p`` -- inert prime

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; p = 5
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: I = H.brandt_module().right_ideals()[49]
            sage: f = H.optimal_embeddings(D, 1, I.left_order())[0]
            sage: H.kolyvagin_generator(f.domain().number_field(), 5)
            a + 1

        This function requires that `p` be prime, but ``kolyvagin_generators`` works in general::

            sage: H.kolyvagin_generator(f.domain().number_field(), 5*17)
            Traceback (most recent call last):
            ...
            NotImplementedError: p must be prime
            sage: H.kolyvagin_generators(f.domain().number_field(), 5*17)
            [-34*a + 1, 35*a + 106]
        """
    @cached_method
    def kolyvagin_generators(self, K, c):
        """
        Return elements in `\\mathcal{O}_K` that map to multiplicative generators
        for the factors of the quotient group

           `(\\mathcal{O}_K / c \\mathcal{O}_K)^* / (\\ZZ/c\\ZZ)^*`

        corresponding to the prime divisors of c.  Each generator is
        of the form `\\sqrt{D}+n` with `n\\geq 1` minimal.

        INPUT:

        - ``K`` -- quadratic imaginary field

        - ``c`` -- square free product of inert prime

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; p = 5
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: I = H.brandt_module().right_ideals()[49]
            sage: f = H.optimal_embeddings(D, 1, I.left_order())[0]
            sage: H.kolyvagin_generators(f.domain().number_field(), 5*17)
            [-34*a + 1, 35*a + 106]
        """
    @cached_method
    def kolyvagin_sigma_operator(self, D, c, r, bound=None):
        """
        Return the action of the Kolyvagin sigma operator on the `r`-th
        basis vector.

        INPUT:

        - ``D`` -- fundamental discriminant

        - ``c`` -- conductor (square-free integer, need not be prime)

        - ``r`` -- nonnegative integer

        - ``bound`` -- (default: ``None``), if given, controls
          precision of computation of theta series, which could
          impact performance, but does not impact correctness

        EXAMPLES:

        We first try to verify Kolyvagin's conjecture for a rank 2
        curve by working modulo 5, but we are unlucky with `c=17`::

            sage: N = 389; D = -7; ell = 5; c = 17; q = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: E = EllipticCurve('389a')
            sage: V = H.modp_dual_elliptic_curve_factor(E, q, 5)  # long time (4s on sage.math, 2012)
            sage: k118 = H.kolyvagin_sigma_operator(D, c, 118)
            sage: k104 = H.kolyvagin_sigma_operator(D, c, 104)
            sage: [b.dot_product(k104.element().change_ring(GF(3)))  # long time
            ....:  for b in V.basis()]
            [0, 0]
            sage: [b.dot_product(k118.element().change_ring(GF(3)))  # long time
            ....:  for b in V.basis()]
            [0, 0]

        Next we try again with `c=41` and this does work, in that we
        get something nonzero, when dotting with V::

            sage: c = 41
            sage: k118 = H.kolyvagin_sigma_operator(D, c, 118)
            sage: k104 = H.kolyvagin_sigma_operator(D, c, 104)
            sage: [b.dot_product(k118.element().change_ring(GF(3)))  # long time
            ....:  for b in V.basis()]
            [2, 0]
            sage: [b.dot_product(k104.element().change_ring(GF(3)))  # long time
            ....:  for b in V.basis()]
            [1, 0]

        By the way, the above is the first ever provable verification
        of Kolyvagin's conjecture for any curve of rank at least 2.

        Another example, but where the curve has rank 1::

            sage: N = 37; D = -7; ell = 17; c = 41; q = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: H.heegner_divisor(D,1).element().nonzero_positions()
            [49, 51]
            sage: k49 = H.kolyvagin_sigma_operator(D, c, 49); k49
            (79, 32, 31, 11, 53, 37, 1, 23, 15, 7, 0, 0, 0, 64, 32, 34, 53, 0, 27, 27, 0, 0, 0, 26, 0, 0, 18, 0, 22, 0, 53, 19, 27, 10, 0, 0, 0, 30, 35, 38, 0, 0, 0, 53, 0, 0, 4, 0, 0, 0, 0, 0)
            sage: k51 = H.kolyvagin_sigma_operator(D, c, 51); k51
            (20, 12, 57, 0, 0, 0, 0, 52, 23, 15, 0, 7, 0, 0, 19, 4, 0, 73, 11, 0, 104, 31, 0, 38, 31, 0, 0, 31, 5, 47, 0, 27, 35, 0, 57, 32, 24, 10, 0, 8, 0, 31, 41, 0, 0, 0, 16, 0, 0, 0, 0, 0)
            sage: V = H.modp_dual_elliptic_curve_factor(EllipticCurve('37a'), q, 5); V
            Vector space of degree 52 and dimension 2 over Ring of integers modulo 3
            Basis matrix:
            2 x 52 dense matrix over Ring of integers modulo 3
            sage: [b.dot_product(k49.element().change_ring(GF(q))) for b in V.basis()]
            [1, 1]
            sage: [b.dot_product(k51.element().change_ring(GF(q))) for b in V.basis()]
            [1, 1]

        An example with `c` a product of two primes::

            sage: N = 389; D = -7; ell = 5; q = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: V = H.modp_dual_elliptic_curve_factor(EllipticCurve('389a'), q, 5)
            sage: k = H.kolyvagin_sigma_operator(D, 17*41, 104)     # long time
            sage: k                                                 # long time
            (990, 656, 219, ..., 246, 534, 1254)
            sage: [b.dot_product(k.element().change_ring(GF(3))) for b in V.basis()]   # long time (but only because depends on something slow)
            [0, 0]
        """
    @cached_method
    def modp_dual_elliptic_curve_factor(self, E, p, bound: int = 10):
        """
        Return the factor of the Brandt module space modulo `p`
        corresponding to the elliptic curve `E`, cut out using
        Hecke operators up to ``bound``.

        INPUT:

        - ``E`` -- elliptic curve of conductor equal to the level of ``self``

        - ``p`` -- prime number

        - ``bound`` -- positive integer (default: 10)

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; c = 41; q = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: V = H.modp_dual_elliptic_curve_factor(EllipticCurve('37a'), q, 5); V
            Vector space of degree 52 and dimension 2 over Ring of integers modulo 3
             Basis matrix: 2 x 52 dense matrix over Ring of integers modulo 3
        """
    @cached_method
    def rational_kolyvagin_divisor(self, D, c):
        """
        Return the Kolyvagin divisor as an element of the Brandt module
        corresponding to the discriminant `D` and conductor `c`, which
        both must be coprime to `N\\ell`.

        INPUT:

        - ``D`` -- discriminant (negative integer)

        - ``c`` -- conductor (positive integer)

        OUTPUT: Brandt module element (or tuple of them)

        EXAMPLES::

            sage: N = 389; D = -7; ell = 5; c = 17; q = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: k = H.rational_kolyvagin_divisor(D, c); k  # long time (5s on sage.math, 2013)
            (2, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 4, 0, 0, 9, 11, 0, 6, 0, 0, 7, 0, 0, 0, 0, 14, 12, 13, 15, 17, 0, 0, 0, 0, 8, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sage: V = H.modp_dual_elliptic_curve_factor(EllipticCurve('389a'), q, 2)
            sage: [b.dot_product(k.element().change_ring(GF(q))) for b in V.basis()]  # long time
            [0, 0]
            sage: k = H.rational_kolyvagin_divisor(D, 59)
            sage: [b.dot_product(k.element().change_ring(GF(q))) for b in V.basis()]
            [2, 0]
        """
    @cached_method
    def kolyvagin_point_on_curve(self, D, c, E, p, bound: int = 10):
        """
        Compute image of the Kolyvagin divisor `P_c` in
        `E(\\GF{\\ell^2}) / p E(\\GF{\\ell^2})`.

        Note that this image is by definition only well defined up to
        scalars.  However, doing multiple computations will always
        yield the same result, and working modulo different `\\ell` is
        compatible (since we always choose the same generator for
        `\\textrm{Gal}(K_c/K_1)`).

        INPUT:

        - ``D`` -- fundamental negative discriminant

        - ``c`` -- conductor

        - ``E`` -- elliptic curve of conductor the level of self

        - ``p`` -- odd prime number such that we consider image in
          `E(\\GF{\\ell^2}) / p E(\\GF{\\ell^2})`

        - ``bound`` -- integer (default: 10)

        EXAMPLES::

            sage: N = 37; D = -7; ell = 17; c = 41; p = 3
            sage: H = heegner_points(N).reduce_mod(ell)
            sage: H.kolyvagin_point_on_curve(D, c, EllipticCurve('37a'), p)
            [1, 1]
        """

def kolyvagin_reduction_data(E, q, first_only: bool = True):
    """
    Given an elliptic curve of positive rank and a prime `q`, this
    function returns data about how to use Kolyvagin's `q`-torsion
    Heegner point Euler system to do computations with this curve.
    See the precise description of the output below.

    INPUT:

    - ``E`` -- elliptic curve over `\\QQ` of rank 1 or 2

    - ``q`` -- an odd prime that does not divide the order of the
      rational torsion subgroup of `E`

    - ``first_only`` -- boolean (default: ``True``); whether two only return
      the first prime that one can work modulo to get data about the Euler system

    OUTPUT in the rank 1 case or when the default flag ``first_only=True``:

    - `\\ell` -- first good odd prime satisfying the Kolyvagin condition that
      `q` divides \\gcd(a_{\\ell},\\ell+1)` and the reduction map is surjective to
      `E(\\GF{\\ell}) / q E(\\GF{\\ell})`

    - ``D`` -- discriminant of the first quadratic imaginary field
       `K` that satisfies the Heegner hypothesis for `E` such that
       both `\\ell` is inert in `K`, and the twist `E^D` has analytic
       rank `\\leq 1`

    - ``h_D`` -- the class number of `K`

    - the dimension of the Brandt module `B(\\ell,N)`, where `N` is
      the conductor of `E`

    OUTPUT in the rank 2 case:

    - `\\ell_1` -- first prime (as above in the rank 1 case) where
      reduction map is surjective

    - `\\ell_2` -- second prime (as above) where reduction map is
      surjective

    - ``D`` -- discriminant of the first quadratic imaginary field
       `K` that satisfies the Heegner hypothesis for `E` such that
       both `\\ell_1` and `\\ell_2` are simultaneously inert in `K`,
       and the twist `E^D` has analytic rank `\\leq 1`

    - ``h_D`` -- the class number of `K`

    - the dimension of the Brandt module `B(\\ell_1,N)`, where `N` is
      the conductor of `E`

    - the dimension of the Brandt module `B(\\ell_2,N)`

    EXAMPLES:

    Import this function::

        sage: from sage.schemes.elliptic_curves.heegner import kolyvagin_reduction_data

    A rank 1 example::

        sage: kolyvagin_reduction_data(EllipticCurve('37a1'), 3)
        (17, -7, 1, 52)

    A rank 3 example::

        sage: kolyvagin_reduction_data(EllipticCurve('5077a1'), 3)
        (11, -47, 5, 4234)
        sage: H = heegner_points(5077, -47)
        sage: [c for c in H.kolyvagin_conductors(2, 10, EllipticCurve('5077a1'), 3)
        ....:    if c % 11]
        [667, 943, 1189, 2461]
        sage: factor(667)
        23 * 29

    A rank 4 example (the first Kolyvagin class that we could try to
    compute would be `P_{23\\cdot 29\\cdot 41}`, and would require
    working in a space of dimension 293060 (so prohibitive at
    present)::

        sage: E = elliptic_curves.rank(4)[0]
        sage: kolyvagin_reduction_data(E,3)              # long time
        (11, -71, 7, 293060)
        sage: H = heegner_points(293060, -71)
        sage: H.kolyvagin_conductors(1,4,E,3)
        [11, 17, 23, 41]

    The first rank 2 example::

        sage: kolyvagin_reduction_data(EllipticCurve('389a'), 3)
        (5, -7, 1, 130)
        sage: kolyvagin_reduction_data(EllipticCurve('389a'), 3, first_only=False)
        (5, 17, -7, 1, 130, 520)

    A large `q = 7`::

        sage: kolyvagin_reduction_data(EllipticCurve('1143c1'), 7, first_only=False)
        (13, 83, -59, 3, 1536, 10496)

    Additive reduction::

        sage: kolyvagin_reduction_data(EllipticCurve('2350g1'), 5, first_only=False)
        (19, 239, -311, 19, 6480, 85680)
    """

class HeegnerQuatAlgEmbedding(SageObject):
    """
    The homomorphism `\\mathcal{O} \\to R`, where `\\mathcal{O}` is the
    order of conductor `c` in the quadratic field of discriminant `D`,
    and `R` is an Eichler order in a quaternion algebra.

    EXAMPLES::

        sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
        sage: f = H.optimal_embeddings(-7, 2, R)[1]; f
        Embedding sending 2*sqrt(-7) to -5*i + k
        sage: type(f)
        <class 'sage.schemes.elliptic_curves.heegner.HeegnerQuatAlgEmbedding'>
        sage: loads(dumps(f)) == f
        True
    """
    def __init__(self, D, c, R, beta) -> None:
        """
        INPUT:

        - ``D`` -- negative fundamental discriminant

        - ``c`` -- positive integer coprime to `D`

        - ``R`` -- Eichler order in a rational quaternion algebra

        - ``beta`` -- element of `R` such that the homomorphism
          sends `c\\sqrt{D}` to `\\beta`

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: i,j,k = H.quaternion_algebra().gens()
            sage: import sage.schemes.elliptic_curves.heegner as heegner
            sage: heegner.HeegnerQuatAlgEmbedding(-7, 2, R, -5*i+k)
            Embedding sending 2*sqrt(-7) to -5*i + k
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: f = H.optimal_embeddings(-7, 2, R)[0]
            sage: f == H.optimal_embeddings(-7, 2, R)[0]
            True
            sage: f == H.optimal_embeddings(-7, 2, R)[1]
            False
            sage: f == 0
            False
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: f = H.optimal_embeddings(-7, 2, R)[0]
            sage: f != H.optimal_embeddings(-7, 2, R)[0]
            False
            sage: f != H.optimal_embeddings(-7, 2, R)[1]
            True
            sage: f != 0
            True
        """
    def __call__(self, x):
        """
        Return image of `x` under this embedding.

        INPUT:

        - ``x`` -- element of the quadratic order

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: f = H.optimal_embeddings(-7, 1, R)[1]; f
            Embedding sending sqrt(-7) to -i + j + k
            sage: a = f.domain_gen(); a^2
            -7
            sage: f(2 + 3*a)
            2 - 3*i + 3*j + 3*k
            sage: 2 + 3*f(a)
            2 - 3*i + 3*j + 3*k
            sage: f(a)^2
            -7
        """
    @cached_method
    def matrix(self):
        """
        Return matrix over `\\QQ` of this morphism, with respect to the
        basis 1, `c\\sqrt{D}` of the domain and the basis `1,i,j,k` of
        the ambient rational quaternion algebra (which contains the
        domain).

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: f = H.optimal_embeddings(-7, 1, R)[1]; f
            Embedding sending sqrt(-7) to -i + j + k
            sage: f.matrix()
            [ 1  0  0  0]
            [ 0 -1  1  1]
            sage: f.conjugate().matrix()
            [ 1  0  0  0]
            [ 0  1 -1 -1]
        """
    @cached_method
    def domain(self):
        """
        Return the domain of this embedding.

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: H.optimal_embeddings(-7, 2, R)[0].domain()
            Order of conductor 4 generated by 2*a
             in Number Field in a with defining polynomial x^2 + 7
             with a = 2.645751311064591?*I
        """
    def domain_gen(self):
        """
        Return the specific generator `c \\sqrt{D}` for the domain
        order.

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: f = H.optimal_embeddings(-7, 2, R)[0]
            sage: f.domain_gen()
            2*a
            sage: f.domain_gen()^2
            -28
        """
    def domain_conductor(self):
        """
        Return the conductor of the domain.

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: H.optimal_embeddings(-7, 2, R)[0].domain_conductor()
            2
        """
    def beta(self):
        """
        Return the element `\\beta` in the quaternion algebra order
        that `c\\sqrt{D}` maps to.

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: H.optimal_embeddings(-7, 2, R)[1].beta()
            -5*i + k
        """
    def codomain(self):
        """
        Return the codomain of this embedding.

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: H.optimal_embeddings(-7, 2, R)[0].codomain()
            Order of Quaternion Algebra (-1, -3) with base ring Rational Field
             with basis (1/2 + 1/2*j + 7*k, 1/2*i + 13/2*k, j + 3*k, 11*k)
        """
    def conjugate(self):
        """
        Return the conjugate of this embedding, which is also an
        embedding.

        EXAMPLES::

            sage: H = heegner_points(11).reduce_mod(3); R = H.left_orders()[0]
            sage: f = H.optimal_embeddings(-7, 2, R)[1]
            sage: f.conjugate()
            Embedding sending 2*sqrt(-7) to 5*i - k
            sage: f
            Embedding sending 2*sqrt(-7) to -5*i + k
        """

def quadratic_order(D, c, names: str = 'a'):
    """
    Return order of conductor `c` in quadratic field with fundamental
    discriminant `D`.

    INPUT:

    - ``D`` -- fundamental discriminant

    - ``c`` -- conductor

    - ``names`` -- string (default: ``'a'``)

    OUTPUT:

    - order `R` of conductor `c` in an imaginary quadratic field

    - the element `c\\sqrt{D}` as an element of `R`

    The generator for the field is named 'a' by default.

    EXAMPLES::

        sage: sage.schemes.elliptic_curves.heegner.quadratic_order(-7,3)
        (Order of conductor 6 generated by 3*a in Number Field in a
         with defining polynomial x^2 + 7 with a = 2.645751311064591?*I,
         3*a)
        sage: sage.schemes.elliptic_curves.heegner.quadratic_order(-7,3,'alpha')
        (Order of conductor 6 generated by 3*alpha in Number Field in alpha
         with defining polynomial x^2 + 7 with alpha = 2.645751311064591?*I,
         3*alpha)
    """
def class_number(D):
    """
    Return the class number of the quadratic field with fundamental
    discriminant `D`.

    INPUT:

    - ``D`` -- integer

    EXAMPLES::

        sage: sage.schemes.elliptic_curves.heegner.class_number(-20)
        2
        sage: sage.schemes.elliptic_curves.heegner.class_number(-23)
        3
        sage: sage.schemes.elliptic_curves.heegner.class_number(-163)
        1

    A :exc:`ValueError` is raised when `D` is not a fundamental
    discriminant::

        sage: sage.schemes.elliptic_curves.heegner.class_number(-5)
        Traceback (most recent call last):
        ...
        ValueError: D (=-5) must be a fundamental discriminant
    """
def is_inert(D, p):
    """
    Return ``True`` if p is an inert prime in the field `\\QQ(\\sqrt{D})`.

    INPUT:

    - ``D`` -- fundamental discriminant

    - ``p`` -- prime integer

    EXAMPLES::

        sage: sage.schemes.elliptic_curves.heegner.is_inert(-7,3)
        True
        sage: sage.schemes.elliptic_curves.heegner.is_inert(-7,7)
        False
        sage: sage.schemes.elliptic_curves.heegner.is_inert(-7,11)
        False
    """
def is_split(D, p):
    """
    Return ``True`` if p is a split prime in the field `\\QQ(\\sqrt{D})`.

    INPUT:

    - ``D`` -- fundamental discriminant

    - ``p`` -- prime integer

    EXAMPLES::

        sage: sage.schemes.elliptic_curves.heegner.is_split(-7,3)
        False
        sage: sage.schemes.elliptic_curves.heegner.is_split(-7,7)
        False
        sage: sage.schemes.elliptic_curves.heegner.is_split(-7,11)
        True
    """
def is_ramified(D, p):
    """
    Return ``True`` if p is a ramified prime in the field `\\QQ(\\sqrt{D})`.

    INPUT:

    - ``D`` -- fundamental discriminant

    - ``p`` -- prime integer

    EXAMPLES::

        sage: sage.schemes.elliptic_curves.heegner.is_ramified(-7,2)
        False
        sage: sage.schemes.elliptic_curves.heegner.is_ramified(-7,7)
        True
        sage: sage.schemes.elliptic_curves.heegner.is_ramified(-1,2)
        True
    """
def nearby_rational_poly(f, **kwds):
    """
    Return a polynomial whose coefficients are rational numbers close
    to the coefficients of `f`.

    INPUT:

    - ``f`` -- polynomial with real floating point entries

    - ``**kwds`` -- passed on to ``nearby_rational`` method

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.heegner import nearby_rational_poly
        sage: R.<x> = RR[]
        sage: nearby_rational_poly(2.1*x^2 + 3.5*x - 1.2, max_error=10e-16)
        21/10*X^2 + 7/2*X - 6/5
        sage: nearby_rational_poly(2.1*x^2 + 3.5*x - 1.2, max_error=10e-17)
        4728779608739021/2251799813685248*X^2 + 7/2*X - 5404319552844595/4503599627370496
        sage: RR(4728779608739021/2251799813685248  - 21/10)
        8.88178419700125e-17
    """
def simplest_rational_poly(f, prec):
    """
    Return a polynomial whose coefficients are as simple as possible
    rationals that are also close to the coefficients of f.

    INPUT:

    - ``f`` -- polynomial with real floating point entries

    - ``prec`` -- positive integer

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.heegner import simplest_rational_poly
        sage: R.<x> = RR[]
        sage: simplest_rational_poly(2.1*x^2 + 3.5*x - 1.2, 53)
        21/10*X^2 + 7/2*X - 6/5
    """
def satisfies_weak_heegner_hypothesis(N, D):
    """
    Check that `D` satisfies the weak Heegner hypothesis relative to `N`.
    This is all that is needed to define Heegner points.

    The condition is that `D<0` is a fundamental discriminant and that
    each unramified prime dividing `N` splits in `K=\\QQ(\\sqrt{D})` and
    each ramified prime exactly divides `N`.  We also do not require
    that `D<-4`.

    INPUT:

    - ``N`` -- positive integer

    - ``D`` -- negative integer

    EXAMPLES::

        sage: s = sage.schemes.elliptic_curves.heegner.satisfies_weak_heegner_hypothesis
        sage: s(37,-7)
        True
        sage: s(37,-37)
        False
        sage: s(37,-37*4)
        True
        sage: s(100,-4)
        False
        sage: [D for D in [-1,-2,..,-40] if s(37,D)]
        [-3, -4, -7, -11, -40]
        sage: [D for D in [-1,-2,..,-100] if s(37,D)]
        [-3, -4, -7, -11, -40, -47, -67, -71, -83, -84, -95]
        sage: EllipticCurve('37a').heegner_discriminants_list(10)
        [-7, -11, -40, -47, -67, -71, -83, -84, -95, -104]
    """
def make_monic(f):
    """
    Return a monic integral polynomial `g` and an integer `d` such
    that if `\\alpha` is a root of `g`, then `\\alpha/d` is a root of `f`.
    In other words, `c f(x) = g(d x)` for some scalar `c`.

    INPUT:

    - ``f`` -- polynomial over the rational numbers

    OUTPUT: a monic integral polynomial and an integer

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.heegner import make_monic
        sage: R.<x> = QQ[]
        sage: make_monic(3*x^3 + 14*x^2 - 7*x + 5)
        (x^3 + 14*x^2 - 21*x + 45, 3)

    In this example we verify that ``make_monic`` does what we claim it does::

        sage: K.<a> = NumberField(x^3 + 17*x - 3)
        sage: f = (a/7+2/3).minpoly(); f
        x^3 - 2*x^2 + 247/147*x - 4967/9261
        sage: g, d = make_monic(f); (g, d)
        (x^3 - 42*x^2 + 741*x - 4967, 21)
        sage: K.<b> = NumberField(g)
        sage: (b/d).minpoly()
        x^3 - 2*x^2 + 247/147*x - 4967/9261

    TESTS::

        sage: f = x^5 + x^3/4 + 5
        sage: make_monic(f)
        (x^5 + x^3 + 160, 2)

    Scalar factors do not matter, the result is always monic::

        sage: make_monic(f * 1000000)
        (x^5 + x^3 + 160, 2)
        sage: make_monic(f / 1000000)
        (x^5 + x^3 + 160, 2)
    """
def ell_heegner_point(self, D, c=..., f=None, check: bool = True):
    """
    Return the Heegner point on this curve associated to the
    quadratic imaginary field `K=\\QQ(\\sqrt{D})`.

    If the optional parameter `c` is given, returns the higher Heegner
    point associated to the order of conductor `c`.

    INPUT:

    - ``D`` -- a Heegner discriminant

    - ``c`` -- (default: 1) conductor, must be coprime to `DN`

    - ``f`` -- binary quadratic form or 3-tuple `(A,B,C)` of coefficients
      of `AX^2 + BXY + CY^2`

    - ``check`` -- boolean (default: ``True``)

    OUTPUT: the Heegner point `y_c`

    EXAMPLES::

        sage: E = EllipticCurve('37a')
        sage: E.heegner_discriminants_list(10)
        [-7, -11, -40, -47, -67, -71, -83, -84, -95, -104]
        sage: P = E.heegner_point(-7); P                          # indirect doctest
        Heegner point of discriminant -7 on elliptic curve of conductor 37
        sage: z = P.point_exact(); z == E(0, 0, 1)  or -z == E(0, 0, 1)
        True
        sage: P.curve()
        Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
        sage: P = E.heegner_point(-40).point_exact(); P
        (a : -a + 1 : 1)
        sage: P = E.heegner_point(-47).point_exact(); P
        (a : a^4 + a - 1 : 1)
        sage: P[0].parent()
        Number Field in a with defining polynomial x^5 - x^4 + x^3 + x^2 - 2*x + 1

    Working out the details manually::

        sage: P = E.heegner_point(-47).numerical_approx(prec=200)
        sage: f = algebraic_dependency(P[0], 5); f
        x^5 - x^4 + x^3 + x^2 - 2*x + 1
        sage: f.discriminant().factor()
        47^2

    The Heegner hypothesis is checked::

        sage: E = EllipticCurve('389a'); P = E.heegner_point(-5,7);
        Traceback (most recent call last):
        ...
        ValueError: N (=389) and D (=-5) must satisfy the Heegner hypothesis

    We can specify the quadratic form::

        sage: P = EllipticCurve('389a').heegner_point(-7, 5, (778,925,275)); P
        Heegner point of discriminant -7 and conductor 5
         on elliptic curve of conductor 389
        sage: P.quadratic_form()
        778*x^2 + 925*x*y + 275*y^2
    """
def kolyvagin_point(self, D, c=..., check: bool = True):
    """
    Return the Kolyvagin point on this curve associated to the
    quadratic imaginary field `K=\\QQ(\\sqrt{D})` and conductor `c`.

    INPUT:

    - ``D`` -- a Heegner discriminant

    - ``c`` -- (default: 1) conductor, must be coprime to `DN`

    - ``check`` -- boolean (default: ``True``)

    OUTPUT: the Kolyvagin point `P` of conductor `c`

    EXAMPLES::

        sage: E = EllipticCurve('37a1')
        sage: P = E.kolyvagin_point(-67); P
        Kolyvagin point of discriminant -67 on elliptic curve of conductor 37
        sage: P.numerical_approx()  # abs tol 1e-14
        (6.00000000000000 : -15.0000000000000 : 1.00000000000000)
        sage: P.index()
        6
        sage: g = E((0,-1,1)) # a generator
        sage: E.regulator() == E.regulator_of_points([g])
        True
        sage: 6*g
        (6 : -15 : 1)
    """
def ell_heegner_discriminants(self, bound):
    """
    Return the list of ``self``'s Heegner discriminants between -1 and
    -bound.

    INPUT:

    - ``bound`` -- integer; upper bound for -discriminant

    OUTPUT: the list of Heegner discriminants between -1 and -bound for
    the given elliptic curve

    EXAMPLES::

        sage: E=EllipticCurve('11a')
        sage: E.heegner_discriminants(30)                     # indirect doctest
        [-7, -8, -19, -24]
    """
def ell_heegner_discriminants_list(self, n):
    """
    Return the list of ``self``'s first `n` Heegner discriminants smaller
    than -5.

    INPUT:

    - ``n`` -- integer; the number of discriminants to compute

    OUTPUT: the list of the first `n` Heegner discriminants smaller than
    `-5` for the given elliptic curve

    EXAMPLES::

        sage: E=EllipticCurve('11a')
        sage: E.heegner_discriminants_list(4)                     # indirect doctest
        [-7, -8, -19, -24]
    """
def heegner_point_height(self, D, prec: int = 2, check_rank: bool = True):
    """
    Use the Gross-Zagier formula to compute the Neron-Tate canonical
    height over `K` of the Heegner point corresponding to `D`, as an
    interval (it is computed to some precision using `L`-functions).

    If the curve has rank at least 2, then the returned height is the
    exact Sage integer 0.

    INPUT:

    - ``D`` -- integer; fundamental discriminant (=/= -3, -4)

    - ``prec`` -- integer (default: 2); use `prec \\cdot \\sqrt(N) + 20`
      terms of `L`-series in computations, where `N` is the
      conductor

    - ``check_rank`` -- whether to check if the rank is at least 2 by
      computing the Mordell-Weil rank directly

    OUTPUT: interval that contains the height of the Heegner point

    EXAMPLES::

        sage: E = EllipticCurve('11a')
        sage: E.heegner_point_height(-7)
        0.22227?

    Some higher rank examples::

        sage: E = EllipticCurve('389a')
        sage: E.heegner_point_height(-7)
        0
        sage: E = EllipticCurve('5077a')
        sage: E.heegner_point_height(-7)
        0
        sage: E.heegner_point_height(-7, check_rank=False)
        0.0000?
    """
def heegner_index(self, D, min_p: int = 2, prec: int = 5, descent_second_limit: int = 12, verbose_mwrank: bool = False, check_rank: bool = True):
    """
    Return an interval that contains the index of the Heegner
    point `y_K` in the group of `K`-rational points modulo torsion
    on this elliptic curve, computed using the Gross-Zagier
    formula and/or a point search, or possibly half the index
    if the rank is greater than one.

    If the curve has rank > 1, then the returned index is infinity.

    .. NOTE::

        If ``min_p`` is bigger than 2 then the index can be off by
        any prime less than ``min_p``. This function returns the
        index divided by `2` exactly when the rank of `E(K)` is
        greater than 1 and `E(\\QQ)_{/tor} \\oplus E^D(\\QQ)_{/tor}`
        has index `2` in `E(K)_{/tor}`, where the second factor
        undergoes a twist.

    INPUT:

    - ``D`` -- integer; Heegner discriminant

    - ``min_p`` -- integer (default: 2); only rule out primes
      = min_p dividing the index

    - ``verbose_mwrank`` -- boolean (default: ``False``); print lots of
      mwrank search status information when computing regulator

    - ``prec`` -- integer (default: 5);, use prec\\*sqrt(N) +
      20 terms of `L`-series in computations, where N is the conductor

    - ``descent_second_limit`` -- (default: 12)- used in 2-descent
      when computing regulator of the twist

    - ``check_rank`` -- whether to check if the rank is at least 2 by
      computing the Mordell-Weil rank directly

    OUTPUT: an interval that contains the index, or half the index

    EXAMPLES::

        sage: E = EllipticCurve('11a')
        sage: E.heegner_discriminants(50)
        [-7, -8, -19, -24, -35, -39, -40, -43]
        sage: E.heegner_index(-7)
        1.00000?

    ::

        sage: E = EllipticCurve('37b')
        sage: E.heegner_discriminants(100)
        [-3, -4, -7, -11, -40, -47, -67, -71, -83, -84, -95]
        sage: E.heegner_index(-95)          # long time (1 second)
        2.00000?

    This tests doing direct computation of the Mordell-Weil group.

    ::

        sage: EllipticCurve('675b').heegner_index(-11)
        3.0000?

    Currently discriminants -3 and -4 are not supported::

        sage: E.heegner_index(-3)
        Traceback (most recent call last):
        ...
        ArithmeticError: Discriminant (=-3) must not be -3 or -4.

    The curve 681b returns the true index, which is `3`::

        sage: E = EllipticCurve('681b')
        sage: I = E.heegner_index(-8); I
        3.0000?

    In fact, whenever the returned index has a denominator of
    `2`, the true index is got by multiplying the returned
    index by `2`. Unfortunately, this is not an if and only if
    condition, i.e., sometimes the index must be multiplied by
    `2` even though the denominator is not `2`.

    This example demonstrates the ``descent_second_limit`` option,
    which can be used to fine tune the 2-descent used to compute
    the regulator of the twist::

        sage: E = EllipticCurve([1,-1,0,-1228,-16267])
        sage: E.heegner_index(-8)
        Traceback (most recent call last):
        ...
        RuntimeError: ...

    However when we search higher, we find the points we need::

        sage: E.heegner_index(-8, descent_second_limit=16, check_rank=False)  # long time
        2.00000?

    Two higher rank examples (of ranks 2 and 3)::

        sage: E = EllipticCurve('389a')
        sage: E.heegner_index(-7)
        +Infinity
        sage: E = EllipticCurve('5077a')
        sage: E.heegner_index(-7)
        +Infinity
        sage: E.heegner_index(-7, check_rank=False)
        0.001?
        sage: E.heegner_index(-7, check_rank=False).lower() == 0
        True
    """
def heegner_index_bound(self, D: int = 0, prec: int = 5, max_height=None):
    """
    Assume ``self`` has rank 0.

    Return a list `v` of primes such that if an odd prime `p` divides
    the index of the Heegner point in the group of rational points
    modulo torsion, then `p` is in `v`.

    If 0 is in the interval of the height of the Heegner point
    computed to the given prec, then this function returns `v =
    0`. This does not mean that the Heegner point is torsion, just
    that it is very likely torsion.

    If we obtain no information from a search up to ``max_height``,
    e.g., if the Siksek et al. bound is bigger than ``max_height``,
    then we return `v = -1`.

    INPUT:

    - ``D`` -- integer (default: 0); Heegner discriminant; if
      0, use the first discriminant -4 that satisfies the Heegner
      hypothesis

    - ``verbose`` -- boolean (default: ``True``)

    - ``prec`` -- integer (default: 5); use `prec \\cdot \\sqrt(N) + 20`
      terms of `L`-series in computations, where `N` is the conductor

    - ``max_height (float)`` -- should be = 21; bound on
      logarithmic naive height used in point searches. Make smaller to
      make this function faster, at the expense of possibly obtaining a
      worse answer. A good range is between 13 and 21.

    OUTPUT:

    - ``v`` -- list or int (bad primes or 0 or -1)

    - ``D`` -- the discriminant that was used (this is
      useful if `D` was automatically selected)

    - ``exact`` -- either False, or the exact Heegner index
      (up to factors of 2)

    EXAMPLES::

        sage: E = EllipticCurve('11a1')
        sage: E.heegner_index_bound()
        ([2], -7, 2)
    """
def heegner_sha_an(self, D, prec: int = 53):
    """
    Return the conjectural (analytic) order of Sha for E over the field `K=\\QQ(\\sqrt{D})`.

    INPUT:

    - ``D`` -- negative integer; the Heegner discriminant

    - ``prec`` -- integer (default: 53); bits of precision to
      compute analytic order of Sha

    OUTPUT:

    (floating point number) an approximation to the conjectural order of Sha.

    .. NOTE::

        Often you'll want to do ``proof.elliptic_curve(False)`` when
        using this function, since often the twisted elliptic
        curves that come up have enormous conductor, and Sha is
        nontrivial, which makes provably finding the Mordell-Weil
        group using 2-descent difficult.

    EXAMPLES:

    An example where E has conductor 11::

        sage: E = EllipticCurve('11a')
        sage: E.heegner_sha_an(-7)                                  # long time
        1.00000000000000

    The cache works::

        sage: E.heegner_sha_an(-7) is E.heegner_sha_an(-7)          # long time
        True

    Lower precision::

        sage: E.heegner_sha_an(-7,10)                               # long time
        1.0

    Checking that the cache works for any precision::

        sage: E.heegner_sha_an(-7,10) is E.heegner_sha_an(-7,10)    # long time
        True

    Next we consider a rank 1 curve with nontrivial Sha over the
    quadratic imaginary field `K`; however, there is no Sha for `E`
    over `\\QQ` or for the quadratic twist of `E`::

        sage: E = EllipticCurve('37a')
        sage: E.heegner_sha_an(-40)                                 # long time
        4.00000000000000
        sage: E.quadratic_twist(-40).sha().an()                     # long time
        1
        sage: E.sha().an()                                          # long time
        1

    A rank 2 curve::

        sage: E = EllipticCurve('389a')                             # long time
        sage: E.heegner_sha_an(-7)                                  # long time
        1.00000000000000

    If we remove the hypothesis that `E(K)` has rank 1 in Conjecture
    2.3 in [GZ1986]_ page 311, then that conjecture is
    false, as the following example shows::

        sage: # long time
        sage: E = EllipticCurve('65a')
        sage: E.heegner_sha_an(-56)
        1.00000000000000
        sage: E.torsion_order()
        2
        sage: E.tamagawa_product()
        1
        sage: E.quadratic_twist(-56).rank()
        2
    """
def satisfies_heegner_hypothesis(self, D):
    """
    Return ``True`` precisely when `D` is a fundamental discriminant that
    satisfies the Heegner hypothesis for this elliptic curve.

    EXAMPLES::

        sage: E = EllipticCurve('11a1')
        sage: E.satisfies_heegner_hypothesis(-7)
        True
        sage: E.satisfies_heegner_hypothesis(-11)
        False
    """
