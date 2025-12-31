r"""
Dirichlet characters

A :class:`DirichletCharacter` is the extension of a homomorphism

.. MATH::

    (\ZZ/N\ZZ)^* \to R^*,

for some ring `R`, to the map `\ZZ/N\ZZ \to R` obtained by sending
those `x\in\ZZ/N\ZZ` with `\gcd(N,x)>1` to `0`.

EXAMPLES::

    sage: G = DirichletGroup(35)
    sage: x = G.gens()
    sage: e = x[0]*x[1]^2; e
    Dirichlet character modulo 35 of conductor 35
     mapping 22 |--> zeta12^3, 31 |--> zeta12^2 - 1
    sage: e.order()
    12

This illustrates a canonical coercion::

    sage: e = DirichletGroup(5, QQ).0
    sage: f = DirichletGroup(5, CyclotomicField(4)).0
    sage: e*f
    Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -zeta4

AUTHORS:

-  William Stein (2005-09-02): Fixed bug in comparison of Dirichlet
   characters. It was checking that their values were the same, but
   not checking that they had the same level!

-  William Stein (2006-01-07): added more examples

-  William Stein (2006-05-21): added examples of everything; fix a
   *lot* of tiny bugs and design problem that became clear when
   creating examples.

-  Craig Citro (2008-02-16): speed up __call__ method for
   Dirichlet characters, miscellaneous fixes

-  Julian Rueth (2014-03-06): use UniqueFactory to cache DirichletGroups
"""
from sage.arith.functions import lcm as lcm
from sage.arith.misc import bernoulli as bernoulli, euler_phi as euler_phi, factor as factor, factorial as factorial, fundamental_discriminant as fundamental_discriminant, gcd as gcd, kronecker as kronecker, valuation as valuation
from sage.categories.map import Map as Map
from sage.categories.objects import Objects as Objects
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.functional import round as round
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ, RationalField as RationalField
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.gens_py import multiplicative_iterator as multiplicative_iterator
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

def trivial_character(N, base_ring=...):
    """
    Return the trivial character of the given modulus, with values in the given
    base ring.

    EXAMPLES::

        sage: t = trivial_character(7)
        sage: [t(x) for x in [0..20]]
        [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        sage: t(1).parent()
        Rational Field
        sage: trivial_character(7, Integers(3))(1).parent()
        Ring of integers modulo 3
    """
TrivialCharacter = trivial_character

def kronecker_character(d):
    """
    Return the quadratic Dirichlet character (d/.) of minimal
    conductor.

    EXAMPLES::

        sage: kronecker_character(97*389*997^2)
        Dirichlet character modulo 37733 of conductor 37733
         mapping 1557 |--> -1, 37346 |--> -1

    ::

        sage: a = kronecker_character(1)
        sage: b = DirichletGroup(2401,QQ)(a)    # NOTE -- over QQ!
        sage: b.modulus()
        2401

    AUTHORS:

    - Jon Hanke (2006-08-06)
    """
def kronecker_character_upside_down(d):
    """
    Return the quadratic Dirichlet character (./d) of conductor d, for
    d > 0.

    EXAMPLES::

        sage: kronecker_character_upside_down(97*389*997^2)
        Dirichlet character modulo 37506941597 of conductor 37733
         mapping 13533432536 |--> -1, 22369178537 |--> -1, 14266017175 |--> 1

    AUTHORS:

    - Jon Hanke (2006-08-06)
    """
def is_DirichletCharacter(x) -> bool:
    """
    Return ``True`` if ``x`` is of type ``DirichletCharacter``.

    EXAMPLES::

        sage: from sage.modular.dirichlet import is_DirichletCharacter
        sage: is_DirichletCharacter(trivial_character(3))
        doctest:warning...
        DeprecationWarning: The function is_DirichletCharacter is deprecated;
        use 'isinstance(..., DirichletCharacter)' instead.
        See https://github.com/sagemath/sage/issues/38184 for details.
        True
        sage: is_DirichletCharacter([1])
        False
    """

class DirichletCharacter(MultiplicativeGroupElement):
    """
    A Dirichlet character.
    """
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        Create a Dirichlet character with specified values on
        generators of `(\\ZZ/n\\ZZ)^*`.

        INPUT:

        - ``parent`` -- :class:`DirichletGroup`, a group of Dirichlet
          characters

        - ``x`` -- one of the following:

           - tuple or list of ring elements: the values of the
             Dirichlet character on the standard generators of
             `(\\ZZ/N\\ZZ)^*` as returned by
             :meth:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic.unit_gens`.

           - vector over `\\ZZ/e\\ZZ`, where `e` is the order of the
             standard root of unity for ``parent``.

           In both cases, the orders of the elements must divide the
           orders of the respective generators of `(\\ZZ/N\\ZZ)^*`.

        OUTPUT:

        The Dirichlet character defined by `x` (type
        :class:`DirichletCharacter`).

        EXAMPLES::

            sage: G.<e> = DirichletGroup(13)
            sage: G
            Group of Dirichlet characters modulo 13 with values
             in Cyclotomic Field of order 12 and degree 4
            sage: e
            Dirichlet character modulo 13 of conductor 13 mapping 2 |--> zeta12
            sage: loads(e.dumps()) == e
            True

        ::

            sage: G, x = DirichletGroup(35).objgens()
            sage: e = x[0]*x[1]; e
            Dirichlet character modulo 35 of conductor 35
             mapping 22 |--> zeta12^3, 31 |--> zeta12^2
            sage: e.order()
            12
            sage: loads(e.dumps()) == e
            True

        TESTS::

            sage: G = DirichletGroup(10)
            sage: TestSuite(G[1]).run()

        It is checked that the orders of the elements in `x` are
        admissible (see :issue:`17283`)::

            sage: k.<i> = CyclotomicField(4)
            sage: G = DirichletGroup(192)
            sage: G([i, -1, -1])
            Traceback (most recent call last):
            ...
            ValueError: values (= (zeta16^4, -1, -1)) must have
            multiplicative orders dividing (2, 16, 2), respectively

            sage: from sage.modular.dirichlet import DirichletCharacter
            sage: M = FreeModule(Zmod(16), 3)
            sage: DirichletCharacter(G, M([4, 8, 8]))
            Traceback (most recent call last):
            ...
            ValueError: values (= (4, 8, 8) modulo 16) must have
            additive orders dividing (2, 16, 2), respectively
        """
    def __call__(self, m):
        """
        Return the value of this character at the integer `m`.

        .. warning::

            A table of values of the character is made the first time
            you call this (unless `m` equals -1)

        EXAMPLES::

            sage: G = DirichletGroup(60)
            sage: e = prod(G.gens(), G(1))
            sage: e
            Dirichlet character modulo 60 of conductor 60 mapping 31 |--> -1, 41 |--> -1, 37 |--> zeta4
            sage: e(-1)
            -1
            sage: e(2)
            0
            sage: e(7)
            -zeta4
            sage: Integers(60).unit_gens()
            (31, 41, 37)
            sage: e(31)
            -1
            sage: e(41)
            -1
            sage: e(37)
            zeta4
            sage: e(31*37)
            -zeta4
            sage: parent(e(31*37))
            Cyclotomic Field of order 4 and degree 2
        """
    def change_ring(self, R):
        """
        Return the base extension of ``self`` to ``R``.

        INPUT:

        - ``R`` -- either a ring admitting a conversion map from the
          base ring of ``self``, or a ring homomorphism with the base
          ring of ``self`` as its domain

        EXAMPLES::

            sage: e = DirichletGroup(7, QQ).0
            sage: f = e.change_ring(QuadraticField(3, 'a'))
            sage: f.parent()
            Group of Dirichlet characters modulo 7 with values in Number Field in a
             with defining polynomial x^2 - 3 with a = 1.732050807568878?

        ::

            sage: e = DirichletGroup(13).0
            sage: e.change_ring(QQ)
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce zeta12 to a rational

        We test the case where `R` is a map (:issue:`18072`)::

            sage: K.<i> = QuadraticField(-1)
            sage: chi = DirichletGroup(5, K)[1]
            sage: chi(2)
            i
            sage: f = K.complex_embeddings()[0]
            sage: psi = chi.change_ring(f)
            sage: psi(2)
            -1.83697019872103e-16 - 1.00000000000000*I
        """
    def __hash__(self) -> int:
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: e = DirichletGroup(16)([-1, 1])
            sage: hash(e) == hash((-1,1))
            True
        """
    def __invert__(self):
        """
        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: e = DirichletGroup(13).0
            sage: f = ~e
            sage: f*e
            Dirichlet character modulo 13 of conductor 1 mapping 2 |--> 1
        """
    def __copy__(self):
        """
        Return a (shallow) copy of this Dirichlet character.

        EXAMPLES::

            sage: G.<a> = DirichletGroup(11)
            sage: b = copy(a)
            sage: a is b
            False
            sage: a.element() is b.element()
            False
            sage: a.values_on_gens() is b.values_on_gens()
            True
        """
    def __pow__(self, n):
        """
        Return ``self`` raised to the power of ``n``.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: a^2
            Dirichlet character modulo 20 of conductor 1 mapping 11 |--> 1, 17 |--> 1
            sage: b^2
            Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> -1
        """
    def base_ring(self):
        """
        Return the base ring of this Dirichlet character.

        EXAMPLES::

            sage: G = DirichletGroup(11)
            sage: G.gen(0).base_ring()
            Cyclotomic Field of order 10 and degree 4
            sage: G = DirichletGroup(11, RationalField())
            sage: G.gen(0).base_ring()
            Rational Field
        """
    def bar(self):
        """
        Return the complex conjugate of this Dirichlet character.

        EXAMPLES::

            sage: e = DirichletGroup(5).0
            sage: e
            Dirichlet character modulo 5 of conductor 5 mapping 2 |--> zeta4
            sage: e.bar()
            Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -zeta4
        """
    def bernoulli(self, k, algorithm: str = 'recurrence', cache: bool = True, **opts):
        """
        Return the generalized Bernoulli number `B_{k,eps}`.

        INPUT:

        - ``k`` -- nonnegative integer

        - ``algorithm`` -- either ``'recurrence'`` (default) or
          ``'definition'``

        - ``cache`` -- if ``True``, cache answers

        - ``**opts`` -- optional arguments; not used directly, but
          passed to the :func:`bernoulli` function if this is called

        OUTPUT:

        Let `\\varepsilon` be a (not necessarily primitive) character
        of modulus `N`.  This function returns the generalized
        Bernoulli number `B_{k,\\varepsilon}`, as defined by the
        following identity of power series (see for example
        [DI1995]_, Section 2.2):

        .. MATH::

            \\sum_{a=1}^N \\frac{\\varepsilon(a) t e^{at}}{e^{Nt}-1}
            = \\sum_{k=0}^{\\infty} \\frac{B_{k,\\varepsilon}}{k!} t^k.

        ALGORITHM:

        The ``'recurrence'`` algorithm computes generalized Bernoulli
        numbers via classical Bernoulli numbers using the formula in
        [Coh2007]_, Proposition 9.4.5; this is usually optimal.  The
        ``definition`` algorithm uses the definition directly.

        .. WARNING::

            In the case of the trivial Dirichlet character modulo 1,
            this function returns `B_{1,\\varepsilon} = 1/2`, in
            accordance with the above definition, but in contrast to
            the value `B_1 = -1/2` for the classical Bernoulli number.
            Some authors use an alternative definition giving
            `B_{1,\\varepsilon} = -1/2`; see the discussion in
            [Coh2007]_, Section 9.4.1.

        EXAMPLES::

            sage: G = DirichletGroup(13)
            sage: e = G.0
            sage: e.bernoulli(5)
            7430/13*zeta12^3 - 34750/13*zeta12^2 - 11380/13*zeta12 + 9110/13
            sage: eps = DirichletGroup(9).0
            sage: eps.bernoulli(3)
            10*zeta6 + 4
            sage: eps.bernoulli(3, algorithm='definition')
            10*zeta6 + 4

        TESTS:

        Check that :issue:`17586` is fixed::

            sage: DirichletGroup(1)[0].bernoulli(1)
            1/2
        """
    def lfunction(self, prec: int = 53, algorithm: str = 'pari'):
        '''
        Return the `L`-function of ``self``.

        The result is a wrapper around a PARI `L`-function or around
        the ``lcalc`` program.

        INPUT:

        - ``prec`` -- precision (default: 53)

        - ``algorithm`` -- \'pari\' (default) or \'lcalc\'

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: L = a.lfunction(); L
            PARI L-function associated to Dirichlet character modulo 20
            of conductor 4 mapping 11 |--> -1, 17 |--> 1
            sage: L(4)
            0.988944551741105

        With the algorithm "lcalc"::

            sage: a = a.primitive_character()
            sage: L = a.lfunction(algorithm=\'lcalc\'); L
            L-function with complex Dirichlet coefficients
            sage: L.value(4)  # abs tol 1e-8
            0.988944551741105 + 0.0*I
        '''
    @cached_method
    def conductor(self):
        """
        Compute and return the conductor of this character.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: a.conductor()
            4
            sage: b.conductor()
            5
            sage: (a*b).conductor()
            20

        TESTS::

            sage: G.<a, b> = DirichletGroup(20)
            sage: type(G(1).conductor())
            <class 'sage.rings.integer.Integer'>
        """
    @cached_method
    def fixed_field_polynomial(self, algorithm: str = 'pari'):
        """
        Given a Dirichlet character, this will return a
        polynomial generating the abelian extension fixed by the kernel
        of the corresponding Galois character.

        ALGORITHM: (Sage)

        A formula by Gauss for the products of periods;
        see Disquisitiones §343. See the source code for more.

        OUTPUT: a polynomial with integer coefficients

        EXAMPLES::

            sage: G = DirichletGroup(37)
            sage: chi = G.0
            sage: psi = chi^18
            sage: psi.fixed_field_polynomial()
            x^2 + x - 9

            sage: G = DirichletGroup(7)
            sage: chi = G.0^2
            sage: chi
            Dirichlet character modulo 7 of conductor 7 mapping 3 |--> zeta6 - 1
            sage: chi.fixed_field_polynomial()
            x^3 + x^2 - 2*x - 1

            sage: G = DirichletGroup(31)
            sage: chi = G.0
            sage: chi^6
            Dirichlet character modulo 31 of conductor 31 mapping 3 |--> zeta30^6
            sage: psi = chi^6
            sage: psi.fixed_field_polynomial()
            x^5 + x^4 - 12*x^3 - 21*x^2 + x + 5

            sage: G = DirichletGroup(7)
            sage: chi = G.0
            sage: chi.fixed_field_polynomial()
            x^6 + x^5 + x^4 + x^3 + x^2 + x + 1

            sage: G = DirichletGroup(1001)
            sage: chi = G.0
            sage: psi = chi^3
            sage: psi.order()
            2
            sage: psi.fixed_field_polynomial(algorithm='pari')
            x^2 + x + 2

        With the Sage implementation::

            sage: G = DirichletGroup(37)
            sage: chi = G.0
            sage: psi = chi^18
            sage: psi.fixed_field_polynomial(algorithm='sage')
            x^2 + x - 9

            sage: G = DirichletGroup(7)
            sage: chi = G.0^2
            sage: chi
            Dirichlet character modulo 7 of conductor 7 mapping 3 |--> zeta6 - 1
            sage: chi.fixed_field_polynomial(algorithm='sage')
            x^3 + x^2 - 2*x - 1

            sage: G = DirichletGroup(31)
            sage: chi = G.0
            sage: chi^6
            Dirichlet character modulo 31 of conductor 31 mapping 3 |--> zeta30^6
            sage: psi = chi^6
            sage: psi.fixed_field_polynomial(algorithm='sage')
            x^5 + x^4 - 12*x^3 - 21*x^2 + x + 5

            sage: G = DirichletGroup(7)
            sage: chi = G.0
            sage: chi.fixed_field_polynomial(algorithm='sage')
            x^6 + x^5 + x^4 + x^3 + x^2 + x + 1

            sage: G = DirichletGroup(1001)
            sage: chi = G.0
            sage: psi = chi^3
            sage: psi.order()
            2
            sage: psi.fixed_field_polynomial(algorithm='sage')
            x^2 + x + 2

        The algorithm must be one of `sage` or `pari`::

            sage: G = DirichletGroup(1001)
            sage: chi = G.0
            sage: psi = chi^3
            sage: psi.order()
            2
            sage: psi.fixed_field_polynomial(algorithm='banana')
            Traceback (most recent call last):
            ...
            NotImplementedError: algorithm must be one of 'pari' or 'sage'
        """
    def fixed_field(self):
        """
        Given a Dirichlet character, this will return the abelian extension
        fixed by the kernel of the corresponding Galois character.

        OUTPUT: a number field

        EXAMPLES::

            sage: G = DirichletGroup(37)
            sage: chi = G.0
            sage: psi = chi^18
            sage: psi.fixed_field()
            Number Field in a with defining polynomial x^2 + x - 9


            sage: G = DirichletGroup(7)
            sage: chi = G.0^2
            sage: chi
            Dirichlet character modulo 7 of conductor 7 mapping 3 |--> zeta6 - 1
            sage: chi.fixed_field()
            Number Field in a with defining polynomial x^3 + x^2 - 2*x - 1

            sage: G = DirichletGroup(31)
            sage: chi = G.0
            sage: chi^6
            Dirichlet character modulo 31 of conductor 31 mapping 3 |--> zeta30^6
            sage: psi = chi^6
            sage: psi.fixed_field()
            Number Field in a with defining polynomial x^5 + x^4 - 12*x^3 - 21*x^2 + x + 5
        """
    @cached_method
    def decomposition(self) -> list:
        """
        Return the decomposition of ``self`` as a product of Dirichlet
        characters of prime power modulus, where the prime powers exactly
        divide the modulus of this character.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: c = a*b
            sage: d = c.decomposition(); d
            [Dirichlet character modulo 4 of conductor 4 mapping 3 |--> -1,
             Dirichlet character modulo 5 of conductor 5 mapping 2 |--> zeta4]
            sage: d[0].parent()
            Group of Dirichlet characters modulo 4 with values
             in Cyclotomic Field of order 4 and degree 2
            sage: d[1].parent()
            Group of Dirichlet characters modulo 5 with values
             in Cyclotomic Field of order 4 and degree 2

        We cannot multiply directly, since coercion of one element into the
        other parent fails in both cases::

            sage: d[0]*d[1] == c
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: 'Group of Dirichlet
            characters modulo 4 with values in Cyclotomic Field of order 4 and
            degree 2' and 'Group of Dirichlet characters modulo 5 with values
            in Cyclotomic Field of order 4 and degree 2'

        We can multiply if we are explicit about where we want the
        multiplication to take place.

        ::

            sage: G(d[0])*G(d[1]) == c
            True

        Conductors that are divisible by various powers of 2 present
        some problems as the multiplicative group modulo `2^k` is
        trivial for `k = 1` and non-cyclic for `k \\ge 3`::

            sage: (DirichletGroup(18).0).decomposition()
            [Dirichlet character modulo 2 of conductor 1,
             Dirichlet character modulo 9 of conductor 9 mapping 2 |--> zeta6]
            sage: (DirichletGroup(36).0).decomposition()
            [Dirichlet character modulo 4 of conductor 4 mapping 3 |--> -1,
             Dirichlet character modulo 9 of conductor 1 mapping 2 |--> 1]
            sage: (DirichletGroup(72).0).decomposition()
            [Dirichlet character modulo 8 of conductor 4 mapping 7 |--> -1, 5 |--> 1,
             Dirichlet character modulo 9 of conductor 1 mapping 2 |--> 1]
        """
    def extend(self, M):
        """
        Return the extension of this character to a Dirichlet character
        modulo the multiple ``M`` of the modulus.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: H.<c> = DirichletGroup(4)
            sage: c.extend(20)
            Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1
            sage: a
            Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1
            sage: c.extend(20) == a
            True
        """
    def conrey_number(self):
        """
        Return the Conrey number for this character.

        This is a positive integer coprime to `q` that identifies a
        Dirichlet character of modulus `q`.

        See https://www.lmfdb.org/knowledge/show/character.dirichlet.conrey

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: chi4 = DirichletGroup(4).gen()
            sage: chi4.conrey_number()
            3
            sage: chi = DirichletGroup(24)([1,-1,-1]); chi
            Dirichlet character modulo 24 of conductor 24
            mapping 7 |--> 1, 13 |--> -1, 17 |--> -1
            sage: chi.conrey_number()
            5

            sage: chi = DirichletGroup(60)([1,-1,I])
            sage: chi.conrey_number()
            17

            sage: chi = DirichletGroup(420)([1,-1,-I,1])
            sage: chi.conrey_number()
            113

        TESTS::

            sage: eps1 = DirichletGroup(5)([-1])
            sage: eps2 = DirichletGroup(5,QQ)([-1])
            sage: eps1.conrey_number() == eps2.conrey_number()
            True
            sage: chi = DirichletGroup(1)[0]
            sage: chi.conrey_number()
            1
        """
    def lmfdb_page(self) -> None:
        """
        Open the LMFDB web page of the character in a browser.

        See https://www.lmfdb.org

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: E = DirichletGroup(4).gen()
            sage: E.lmfdb_page()  # optional -- webbrowser
        """
    def galois_orbit(self, sort: bool = True) -> list:
        """
        Return the orbit of this character under the action of the absolute
        Galois group of the prime subfield of the base ring.

        EXAMPLES::

            sage: G = DirichletGroup(30); e = G.1
            sage: e.galois_orbit()
            [Dirichlet character modulo 30 of conductor 5 mapping 11 |--> 1, 7 |--> -zeta4,
             Dirichlet character modulo 30 of conductor 5 mapping 11 |--> 1, 7 |--> zeta4]

        Another example::

            sage: G = DirichletGroup(13)
            sage: G.galois_orbits()
            [[Dirichlet character modulo 13 of conductor 1 mapping 2 |--> 1],
             ...,
             [Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -1]]
            sage: e = G.0
            sage: e
            Dirichlet character modulo 13 of conductor 13 mapping 2 |--> zeta12
            sage: e.galois_orbit()
            [Dirichlet character modulo 13 of conductor 13 mapping 2 |--> zeta12,
             Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -zeta12^3 + zeta12,
             Dirichlet character modulo 13 of conductor 13 mapping 2 |--> zeta12^3 - zeta12,
             Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -zeta12]
            sage: e = G.0^2; e
            Dirichlet character modulo 13 of conductor 13 mapping 2 |--> zeta12^2
            sage: e.galois_orbit()
            [Dirichlet character modulo 13 of conductor 13 mapping 2 |--> zeta12^2,
             Dirichlet character modulo 13 of conductor 13 mapping 2 |--> -zeta12^2 + 1]

        A non-example::

            sage: chi = DirichletGroup(7, Integers(9), zeta = Integers(9)(2)).0
            sage: chi.galois_orbit()
            Traceback (most recent call last):
            ...
            TypeError: Galois orbits only defined if base ring is an integral domain
        """
    def gauss_sum(self, a: int = 1):
        """
        Return a Gauss sum associated to this Dirichlet character.

        The Gauss sum associated to `\\chi` is

        .. MATH::

            g_a(\\chi) = \\sum_{r \\in \\ZZ/m\\ZZ} \\chi(r)\\,\\zeta^{ar},

        where `m` is the modulus of `\\chi` and `\\zeta` is a primitive
        `m`-th root of unity.

        FACTS: If the modulus is a prime `p` and the character is
        nontrivial, then the Gauss sum has absolute value `\\sqrt{p}`.

        CACHING: Computed Gauss sums are *not* cached with this character.

        EXAMPLES::

            sage: G = DirichletGroup(3)
            sage: e = G([-1])
            sage: e.gauss_sum(1)
            2*zeta6 - 1
            sage: e.gauss_sum(2)
            -2*zeta6 + 1
            sage: norm(e.gauss_sum())
            3

        ::

            sage: G = DirichletGroup(13)
            sage: e = G.0
            sage: e.gauss_sum()
            -zeta156^46 + zeta156^45 + zeta156^42 + zeta156^41 + 2*zeta156^40
             + zeta156^37 - zeta156^36 - zeta156^34 - zeta156^33 - zeta156^31
             + 2*zeta156^30 + zeta156^28 - zeta156^24 - zeta156^22 + zeta156^21
             + zeta156^20 - zeta156^19 + zeta156^18 - zeta156^16 - zeta156^15
             - 2*zeta156^14 - zeta156^10 + zeta156^8 + zeta156^7 + zeta156^6
             + zeta156^5 - zeta156^4 - zeta156^2 - 1
            sage: factor(norm(e.gauss_sum()))
            13^24

        TESTS:

        The field of algebraic numbers is supported (:issue:`19056`)::

            sage: G = DirichletGroup(7, QQbar)
            sage: G[1].gauss_sum()
            -2.440133358345538? + 1.022618791871794?*I

        Check that :issue:`19060` is fixed::

            sage: K.<z> = CyclotomicField(8)
            sage: G = DirichletGroup(13, K)
            sage: chi = G([z^2])
            sage: chi.gauss_sum()
            zeta52^22 + zeta52^21 + zeta52^19 - zeta52^16 + zeta52^15 + zeta52^14
             + zeta52^12 - zeta52^11 - zeta52^10 - zeta52^7 - zeta52^5 + zeta52^4

        Check that :issue:`25127` is fixed::

            sage: G = DirichletGroup(1)
            sage: chi = G.one()
            sage: chi.gauss_sum()
            1

        .. SEEALSO::

            - :func:`sage.arith.misc.gauss_sum` for general finite fields
            - :func:`sage.rings.padics.misc.gauss_sum` for a `p`-adic version
        """
    def gauss_sum_numerical(self, prec: int = 53, a: int = 1):
        """
        Return a Gauss sum associated to this Dirichlet character as an
        approximate complex number with ``prec`` bits of precision.

        INPUT:

        - ``prec`` -- integer (default: 53); *bits* of precision

        - ``a`` -- integer; as for :meth:`gauss_sum`

        The Gauss sum associated to `\\chi` is

        .. MATH::

            g_a(\\chi) = \\sum_{r \\in \\ZZ/m\\ZZ} \\chi(r)\\,\\zeta^{ar},

        where `m` is the modulus of `\\chi` and `\\zeta` is a primitive
        `m`-th root of unity.

        EXAMPLES::

            sage: G = DirichletGroup(3)
            sage: e = G.0
            sage: abs(e.gauss_sum_numerical())
            1.7320508075...
            sage: sqrt(3.0)
            1.73205080756888
            sage: e.gauss_sum_numerical(a=2)
            -...e-15 - 1.7320508075...*I
            sage: e.gauss_sum_numerical(a=2, prec=100)
            4.7331654313260708324703713917e-30 - 1.7320508075688772935274463415*I
            sage: G = DirichletGroup(13)
            sage: H = DirichletGroup(13, CC)
            sage: e = G.0
            sage: f = H.0
            sage: e.gauss_sum_numerical()
            -3.07497205... + 1.8826966926...*I
            sage: f.gauss_sum_numerical()
            -3.07497205... + 1.8826966926...*I
            sage: abs(e.gauss_sum_numerical())
            3.60555127546...
            sage: abs(f.gauss_sum_numerical())
            3.60555127546...
            sage: sqrt(13.0)
            3.60555127546399

        TESTS:

        The field of algebraic numbers is supported (:issue:`19056`)::

            sage: G = DirichletGroup(7, QQbar)
            sage: G[1].gauss_sum_numerical()
            -2.44013335834554 + 1.02261879187179*I
        """
    def jacobi_sum(self, char, check: bool = True):
        """
        Return the Jacobi sum associated to these Dirichlet characters
        (i.e., J(self,char)).

        This is defined as

        .. MATH::

            J(\\chi, \\psi) = \\sum_{a \\in \\ZZ / N\\ZZ} \\chi(a) \\psi(1-a)

        where `\\chi` and `\\psi` are both characters modulo `N`.

        EXAMPLES::

            sage: D = DirichletGroup(13)
            sage: e = D.0
            sage: f = D[-2]
            sage: e.jacobi_sum(f)
            3*zeta12^2 + 2*zeta12 - 3
            sage: f.jacobi_sum(e)
            3*zeta12^2 + 2*zeta12 - 3
            sage: p = 7
            sage: DP = DirichletGroup(p)
            sage: f = DP.0
            sage: e.jacobi_sum(f)
            Traceback (most recent call last):
            ...
            NotImplementedError: Characters must be from the same Dirichlet Group.

            sage: all_jacobi_sums = [(DP[i].values_on_gens(),
            ....:                     DP[j].values_on_gens(),
            ....:                     DP[i].jacobi_sum(DP[j]))
            ....:                    for i in range(p - 1) for j in range(i, p - 1)]
            sage: for s in all_jacobi_sums:
            ....:     print(s)
            ((1,), (1,), 5)
            ((1,), (zeta6,), -1)
            ((1,), (zeta6 - 1,), -1)
            ((1,), (-1,), -1)
            ((1,), (-zeta6,), -1)
            ((1,), (-zeta6 + 1,), -1)
            ((zeta6,), (zeta6,), -zeta6 + 3)
            ((zeta6,), (zeta6 - 1,), 2*zeta6 + 1)
            ((zeta6,), (-1,), -2*zeta6 - 1)
            ((zeta6,), (-zeta6,), zeta6 - 3)
            ((zeta6,), (-zeta6 + 1,), 1)
            ((zeta6 - 1,), (zeta6 - 1,), -3*zeta6 + 2)
            ((zeta6 - 1,), (-1,), 2*zeta6 + 1)
            ((zeta6 - 1,), (-zeta6,), -1)
            ((zeta6 - 1,), (-zeta6 + 1,), -zeta6 - 2)
            ((-1,), (-1,), 1)
            ((-1,), (-zeta6,), -2*zeta6 + 3)
            ((-1,), (-zeta6 + 1,), 2*zeta6 - 3)
            ((-zeta6,), (-zeta6,), 3*zeta6 - 1)
            ((-zeta6,), (-zeta6 + 1,), -2*zeta6 + 3)
            ((-zeta6 + 1,), (-zeta6 + 1,), zeta6 + 2)

        Let's check that trivial sums are being calculated correctly::

            sage: N = 13
            sage: D = DirichletGroup(N)
            sage: g = D(1)
            sage: g.jacobi_sum(g)
            11
            sage: sum([g(x)*g(1-x) for x in IntegerModRing(N)])
            11

        And sums where exactly one character is nontrivial (see :issue:`6393`)::

            sage: G = DirichletGroup(5); X = G.list(); Y = X[0]; Z = X[1]
            sage: Y.jacobi_sum(Z)
            -1
            sage: Z.jacobi_sum(Y)
            -1

        Now let's take a look at a non-prime modulus::

            sage: N = 9
            sage: D = DirichletGroup(N)
            sage: g = D(1)
            sage: g.jacobi_sum(g)
            3

        We consider a sum with values in a finite field::

            sage: g = DirichletGroup(17, GF(9,'a')).0
            sage: g.jacobi_sum(g**2)
            2*a

        TESTS:

        This shows that :issue:`6393` has been fixed::

            sage: G = DirichletGroup(5); X = G.list(); Y = X[0]; Z = X[1]
            sage: # Y is trivial and Z is quartic
            sage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])
            -1
            sage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).
            sage: Y.jacobi_sum(Z); Z.jacobi_sum(Y)
            -1
            -1
        """
    def kloosterman_sum(self, a: int = 1, b: int = 0):
        '''
        Return the "twisted" Kloosterman sum associated to this Dirichlet character.

        This includes Gauss sums, classical Kloosterman sums, Salié sums, etc.

        The Kloosterman sum associated to `\\chi` and the integers a,b is

        .. MATH::

            K(a,b,\\chi) = \\sum_{r \\in (\\ZZ/m\\ZZ)^\\times} \\chi(r)\\,\\zeta^{ar+br^{-1}},

        where `m` is the modulus of `\\chi` and `\\zeta` is a primitive
        `m` th root of unity. This reduces to the Gauss sum if `b=0`.

        This method performs an exact calculation and returns an element of a
        suitable cyclotomic field; see also :meth:`.kloosterman_sum_numerical`,
        which gives an inexact answer (but is generally much quicker).

        CACHING: Computed Kloosterman sums are *not* cached with this
        character.

        EXAMPLES::

            sage: G = DirichletGroup(3)
            sage: e = G([-1])
            sage: e.kloosterman_sum(3,5)
            -2*zeta6 + 1
            sage: G = DirichletGroup(20)
            sage: e = G([1 for u in G.unit_gens()])
            sage: e.kloosterman_sum(7,17)
            -2*zeta20^6 + 2*zeta20^4 + 4

        TESTS::

            sage: G = DirichletGroup(20, UniversalCyclotomicField())
            sage: e = G([1 for u in G.unit_gens()])
            sage: e.kloosterman_sum(7,17)
            -2*E(5) - 4*E(5)^2 - 4*E(5)^3 - 2*E(5)^4

            sage: G = DirichletGroup(12, QQbar)
            sage: e = G.gens()[0]
            sage: e.kloosterman_sum(5, 4)
            0.?e-17 - 4.000000000000000?*I
            sage: e.kloosterman_sum(5,11)
            0
        '''
    def kloosterman_sum_numerical(self, prec: int = 53, a: int = 1, b: int = 0):
        """
        Return the Kloosterman sum associated to this Dirichlet character as
        an approximate complex number with ``prec`` bits of precision.

        See also :meth:`.kloosterman_sum`, which calculates the sum
        exactly (which is generally slower).

        INPUT:

        - ``prec`` -- integer (default: 53); *bits* of precision
        - ``a`` -- integer; as for :meth:`.kloosterman_sum`
        - ``b`` -- integer; as for :meth:`.kloosterman_sum`

        EXAMPLES::

            sage: G = DirichletGroup(3)
            sage: e = G.0

        The real component of the numerical value of e is near zero::

            sage: v = e.kloosterman_sum_numerical()
            sage: v.real() < 1.0e15
            True
            sage: v.imag()
            1.73205080756888
            sage: G = DirichletGroup(20)
            sage: e = G.1
            sage: e.kloosterman_sum_numerical(53,3,11)
            3.80422606518061 - 3.80422606518061*I
        """
    @cached_method
    def is_even(self) -> bool:
        """
        Return ``True`` if and only if `\\varepsilon(-1) = 1`.

        EXAMPLES::

            sage: G = DirichletGroup(13)
            sage: e = G.0
            sage: e.is_even()
            False
            sage: e(-1)
            -1
            sage: [e.is_even() for e in G]
            [True, False, True, False, True, False, True, False, True, False, True, False]

            sage: G = DirichletGroup(13, CC)
            sage: e = G.0
            sage: e.is_even()
            False
            sage: e(-1)
            -1.000000...
            sage: [e.is_even() for e in G]
            [True, False, True, False, True, False, True, False, True, False, True, False]

            sage: G = DirichletGroup(100000, CC)
            sage: G.1.is_even()
            True

        Note that ``is_even`` need not be the negation of
        is_odd, e.g., in characteristic 2::

            sage: G.<e> = DirichletGroup(13, GF(4,'a'))
            sage: e.is_even()
            True
            sage: e.is_odd()
            True
        """
    @cached_method
    def is_odd(self) -> bool:
        """
        Return ``True`` if and only if `\\varepsilon(-1) = -1`.

        EXAMPLES::

            sage: G = DirichletGroup(13)
            sage: e = G.0
            sage: e.is_odd()
            True
            sage: [e.is_odd() for e in G]
            [False, True, False, True, False, True, False, True, False, True, False, True]

            sage: G = DirichletGroup(13)
            sage: e = G.0
            sage: e.is_odd()
            True
            sage: [e.is_odd() for e in G]
            [False, True, False, True, False, True, False, True, False, True, False, True]

            sage: G = DirichletGroup(100000, CC)
            sage: G.0.is_odd()
            True

        Note that ``is_even`` need not be the negation of
        is_odd, e.g., in characteristic 2::

            sage: G.<e> = DirichletGroup(13, GF(4,'a'))
            sage: e.is_even()
            True
            sage: e.is_odd()
            True
        """
    @cached_method
    def is_primitive(self) -> bool:
        """
        Return ``True`` if and only if this character is
        primitive, i.e., its conductor equals its modulus.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: a.is_primitive()
            False
            sage: b.is_primitive()
            False
            sage: (a*b).is_primitive()
            True
            sage: G.<a,b> = DirichletGroup(20, CC)
            sage: a.is_primitive()
            False
            sage: b.is_primitive()
            False
            sage: (a*b).is_primitive()
            True
        """
    @cached_method
    def is_trivial(self) -> bool:
        """
        Return ``True`` if this is the trivial character,
        i.e., has order 1.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: a.is_trivial()
            False
            sage: (a^2).is_trivial()
            True
        """
    def kernel(self) -> list:
        """
        Return the kernel of this character.

        OUTPUT: currently the kernel is returned as a list; this may
        change

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: a.kernel()
            [1, 9, 13, 17]
            sage: b.kernel()
            [1, 11]
        """
    def maximize_base_ring(self):
        """
        Let

        .. MATH::

           \\varepsilon : (\\ZZ/N\\ZZ)^* \\to \\QQ(\\zeta_n)

        be a Dirichlet character. This function returns an equal Dirichlet
        character

        .. MATH::

           \\chi : (\\ZZ/N\\ZZ)^* \\to \\QQ(\\zeta_m)

        where `m` is the least common multiple of `n` and
        the exponent of `(\\ZZ/N\\ZZ)^*`.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20,QQ)
            sage: b.maximize_base_ring()
            Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> -1
            sage: b.maximize_base_ring().base_ring()
            Cyclotomic Field of order 4 and degree 2
            sage: DirichletGroup(20).base_ring()
            Cyclotomic Field of order 4 and degree 2
        """
    def minimize_base_ring(self):
        """
        Return a Dirichlet character that equals this one, but over as
        small a subfield (or subring) of the base ring as possible.

        .. NOTE::

            This function is currently only implemented when the base
            ring is a number field. It is the identity function in
            characteristic p.

        EXAMPLES::

            sage: G = DirichletGroup(13)
            sage: e = DirichletGroup(13).0
            sage: e.base_ring()
            Cyclotomic Field of order 12 and degree 4
            sage: e.minimize_base_ring().base_ring()
            Cyclotomic Field of order 12 and degree 4
            sage: (e^2).minimize_base_ring().base_ring()
            Cyclotomic Field of order 6 and degree 2
            sage: (e^3).minimize_base_ring().base_ring()
            Cyclotomic Field of order 4 and degree 2
            sage: (e^12).minimize_base_ring().base_ring()
            Rational Field

        TESTS:

        Check that :issue:`18479` is fixed::

            sage: f = Newforms(Gamma1(25), names='a')[1]
            sage: eps = f.character()
            sage: eps.minimize_base_ring() == eps
            True

        A related bug (see :issue:`18086`)::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: chi = DirichletGroup(7, K).0
            sage: chi.minimize_base_ring()
            Dirichlet character modulo 7 of conductor 7 mapping 3 |--> -1/2*b*a + 1/2
        """
    def modulus(self):
        """
        Return the modulus of this character.

        EXAMPLES::

            sage: e = DirichletGroup(100, QQ).0
            sage: e.modulus()
            100
            sage: e.conductor()
            4
        """
    def level(self):
        """
        Synonym for modulus.

        EXAMPLES::

            sage: e = DirichletGroup(100, QQ).0
            sage: e.level()
            100
        """
    @cached_method
    def multiplicative_order(self):
        """
        Return the order of this character.

        EXAMPLES::

            sage: e = DirichletGroup(100).1
            sage: e.order()    # same as multiplicative_order, since group is multiplicative
            20
            sage: e.multiplicative_order()
            20
            sage: e = DirichletGroup(100).0
            sage: e.multiplicative_order()
            2
        """
    def primitive_character(self):
        """
        Return the primitive character associated to ``self``.

        EXAMPLES::

            sage: e = DirichletGroup(100).0; e
            Dirichlet character modulo 100 of conductor 4 mapping 51 |--> -1, 77 |--> 1
            sage: e.conductor()
            4
            sage: f = e.primitive_character(); f
            Dirichlet character modulo 4 of conductor 4 mapping 3 |--> -1
            sage: f.modulus()
            4
        """
    def restrict(self, M):
        """
        Return the restriction of this character to a Dirichlet character
        modulo the divisor ``M`` of the modulus, which must also be a multiple
        of the conductor of this character.

        EXAMPLES::

            sage: e = DirichletGroup(100).0
            sage: e.modulus()
            100
            sage: e.conductor()
            4
            sage: e.restrict(20)
            Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1
            sage: e.restrict(4)
            Dirichlet character modulo 4 of conductor 4 mapping 3 |--> -1
            sage: e.restrict(50)
            Traceback (most recent call last):
            ...
            ValueError: conductor(=4) must divide M(=50)
        """
    @cached_method
    def values(self) -> list:
        """
        Return a list of the values of this character on each integer
        between 0 and the modulus.

        EXAMPLES::

            sage: e = DirichletGroup(20)(1)
            sage: e.values()
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
            sage: e = DirichletGroup(20).gen(0)
            sage: e.values()
            [0, 1, 0, -1, 0, 0, 0, -1, 0, 1, 0, -1, 0, 1, 0, 0, 0, 1, 0, -1]
            sage: e = DirichletGroup(20).gen(1)
            sage: e.values()
            [0, 1, 0, -zeta4, 0, 0, 0, zeta4, 0, -1, 0, 1, 0, -zeta4, 0, 0, 0, zeta4, 0, -1]
            sage: e = DirichletGroup(21).gen(0) ; e.values()
            [0, 1, -1, 0, 1, -1, 0, 0, -1, 0, 1, -1, 0, 1, 0, 0, 1, -1, 0, 1, -1]
            sage: e = DirichletGroup(21, base_ring=GF(37)).gen(0) ; e.values()
            [0, 1, 36, 0, 1, 36, 0, 0, 36, 0, 1, 36, 0, 1, 0, 0, 1, 36, 0, 1, 36]
            sage: e = DirichletGroup(21, base_ring=GF(3)).gen(0) ; e.values()
            [0, 1, 2, 0, 1, 2, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 1, 2, 0, 1, 2]

        ::

            sage: chi = DirichletGroup(100151, CyclotomicField(10)).0
            sage: ls = chi.values() ; ls[0:10]
            [0,
            1,
            -zeta10^3,
            -zeta10,
            -zeta10,
            1,
            zeta10^3 - zeta10^2 + zeta10 - 1,
            zeta10,
            zeta10^3 - zeta10^2 + zeta10 - 1,
            zeta10^2]

        TESTS:

        Test that :issue:`11783` and :issue:`14368` are fixed::

            sage: chi = DirichletGroup(1).list()[0]
            sage: chi.values()
            [1]
            sage: chi(1)
            1
        """
    def values_on_gens(self) -> tuple:
        """
        Return a tuple of the values of ``self`` on the standard
        generators of `(\\ZZ/N\\ZZ)^*`, where `N` is the modulus.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: e = DirichletGroup(16)([-1, 1])
            sage: e.values_on_gens ()
            (-1, 1)

        .. NOTE::

            The constructor of :class:`DirichletCharacter` sets the
            cache of :meth:`element` or of :meth:`values_on_gens`. The cache of
            one of these methods needs to be set for the other method to work properly,
            these caches have to be stored when pickling an instance of
            :class:`DirichletCharacter`.
        """
    def element(self):
        """
        Return the underlying `\\ZZ/n\\ZZ`-module
        vector of exponents.

        EXAMPLES::

            sage: G.<a,b> = DirichletGroup(20)
            sage: a.element()
            (2, 0)
            sage: b.element()
            (0, 1)

        .. NOTE::

            The constructor of :class:`DirichletCharacter` sets the
            cache of :meth:`element` or of :meth:`values_on_gens`. The cache of
            one of these methods needs to be set for the other method to work properly,
            these caches have to be stored when pickling an instance of
            :class:`DirichletCharacter`.
        """

class DirichletGroupFactory(UniqueFactory):
    """
    Construct a group of Dirichlet characters modulo `N`.

    INPUT:

    - ``N`` -- positive integer

    - ``base_ring`` -- commutative ring; the value ring for the
      characters in this group (default: the cyclotomic field
      `\\QQ(\\zeta_n)`, where `n` is the exponent of `(\\ZZ/N\\ZZ)^*`)

    - ``zeta`` -- (optional) root of unity in ``base_ring``

    - ``zeta_order`` -- (optional) positive integer; this must be the
      order of ``zeta`` if both are specified

    - ``names`` -- ignored (needed so ``G.<...> = DirichletGroup(...)``
      notation works)

    - ``integral`` -- boolean (default: ``False``); whether to replace
      the default cyclotomic field by its rings of integers as the
      base ring.  This is ignored if ``base_ring`` is not ``None``.

    OUTPUT:

    The group of Dirichlet characters modulo `N` with values in a
    subgroup `V` of the multiplicative group `R^*` of ``base_ring``.
    This is the group of homomorphisms `(\\ZZ/N\\ZZ)^* \\to V` with
    pointwise multiplication.  The group `V` is determined as follows:

    - If both ``zeta`` and ``zeta_order`` are omitted, then `V` is
      taken to be `R^*`, or equivalently its `n`-torsion subgroup,
      where `n` is the exponent of `(\\ZZ/N\\ZZ)^*`.  Many operations,
      such as finding a set of generators for the group, are only
      implemented if `V` is cyclic and a generator for `V` can be
      found.

    - If ``zeta`` is specified, then `V` is taken to be the cyclic
      subgroup of `R^*` generated by ``zeta``.  If ``zeta_order`` is
      also given, it must be the multiplicative order of ``zeta``;
      this is useful if the base ring is not exact or if the order of
      ``zeta`` is very large.

    - If ``zeta`` is not specified but ``zeta_order`` is, then `V` is
      taken to be the group of roots of unity of order dividing
      ``zeta_order`` in `R`.  In this case, `R` must be a domain (so
      `V` is cyclic), and `V` must have order ``zeta_order``.
      Furthermore, a generator ``zeta`` of `V` is computed, and an
      error is raised if such ``zeta`` cannot be found.

    EXAMPLES:

    The default base ring is a cyclotomic field of order the exponent
    of `(\\ZZ/N\\ZZ)^*`::

        sage: DirichletGroup(20)
        Group of Dirichlet characters modulo 20 with values
         in Cyclotomic Field of order 4 and degree 2

    We create the group of Dirichlet character mod 20 with values in
    the rational numbers::

        sage: G = DirichletGroup(20, QQ); G
        Group of Dirichlet characters modulo 20 with values in Rational Field
        sage: G.order()
        4
        sage: G.base_ring()
        Rational Field

    The elements of G print as lists giving the values of the character
    on the generators of `(Z/NZ)^*`::

        sage: list(G)
        [Dirichlet character modulo 20 of conductor 1 mapping 11 |--> 1, 17 |--> 1,
         Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1,
         Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> -1,
         Dirichlet character modulo 20 of conductor 20 mapping 11 |--> -1, 17 |--> -1]

    Next we construct the group of Dirichlet character mod 20, but with
    values in `\\QQ(\\zeta_n)`::

        sage: G = DirichletGroup(20)
        sage: G.1
        Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> zeta4

    We next compute several invariants of ``G``::

        sage: G.gens()
        (Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1,
         Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> zeta4)
        sage: G.unit_gens()
        (11, 17)
        sage: G.zeta()
        zeta4
        sage: G.zeta_order()
        4

    In this example we create a Dirichlet group with values in a
    number field::

        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(x^4 + 1)
        sage: DirichletGroup(5, K)
        Group of Dirichlet characters modulo 5 with values
         in Number Field in a with defining polynomial x^4 + 1

    An example where we give ``zeta``, but not its order::

        sage: G = DirichletGroup(5, K, a); G
        Group of Dirichlet characters modulo 5 with values in the group of order 8
         generated by a in Number Field in a with defining polynomial x^4 + 1
        sage: G.list()
        [Dirichlet character modulo 5 of conductor 1 mapping 2 |--> 1,
         Dirichlet character modulo 5 of conductor 5 mapping 2 |--> a^2,
         Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -1,
         Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -a^2]

    We can also restrict the order of the characters, either with or
    without specifying a root of unity::

        sage: DirichletGroup(5, K, zeta=-1, zeta_order=2)
        Group of Dirichlet characters modulo 5 with values in the group of order 2
         generated by -1 in Number Field in a with defining polynomial x^4 + 1
        sage: DirichletGroup(5, K, zeta_order=2)
        Group of Dirichlet characters modulo 5 with values in the group of order 2
         generated by -1 in Number Field in a with defining polynomial x^4 + 1

    ::

        sage: G.<e> = DirichletGroup(13)
        sage: loads(G.dumps()) == G
        True

    ::

        sage: G = DirichletGroup(19, GF(5))
        sage: loads(G.dumps()) == G
        True

    We compute a Dirichlet group over a large prime field::

        sage: p = next_prime(10^40)
        sage: g = DirichletGroup(19, GF(p)); g
        Group of Dirichlet characters modulo 19 with values
         in Finite Field of size 10000000000000000000000000000000000000121

    Note that the root of unity has small order, i.e., it is not the
    largest order root of unity in the field::

        sage: g.zeta_order()
        2

    ::

        sage: K = CyclotomicField(4)
        sage: r4 = K.ring_of_integers()
        sage: G = DirichletGroup(60, r4)
        sage: G.gens()
        (Dirichlet character modulo 60 of conductor 4
           mapping 31 |--> -1, 41 |--> 1, 37 |--> 1,
         Dirichlet character modulo 60 of conductor 3
           mapping 31 |--> 1, 41 |--> -1, 37 |--> 1,
         Dirichlet character modulo 60 of conductor 5
           mapping 31 |--> 1, 41 |--> 1, 37 |--> zeta4)
        sage: val = G.gens()[2].values_on_gens()[2] ; val
        zeta4
        sage: parent(val)
        Gaussian Integers generated by zeta4 in Cyclotomic Field of order 4 and degree 2
        sage: r4_29_0 = r4.residue_field(K(29).factor()[0][0]); r4_29_0(val)
        12
        sage: r4_29_0(val) * GF(29)(3)
        7
        sage: r4_29_0(G.gens()[2].values_on_gens()[2]) * 3
        7
        sage: parent(r4_29_0(G.gens()[2].values_on_gens()[2]) * 3)
        Residue field of Fractional ideal (-2*zeta4 - 5)

    ::

        sage: DirichletGroup(60, integral=True)
        Group of Dirichlet characters modulo 60 with values in
         Gaussian Integers generated by zeta4 in Cyclotomic Field of order 4 and degree 2
        sage: parent(DirichletGroup(60, integral=True).gens()[2].values_on_gens()[2])
        Gaussian Integers generated by zeta4 in Cyclotomic Field of order 4 and degree 2

    If the order of ``zeta`` cannot be determined automatically, we
    can specify it using ``zeta_order``::

        sage: DirichletGroup(7, CC, zeta=exp(2*pi*I/6))                                 # needs sage.symbolic
        Traceback (most recent call last):
        ...
        NotImplementedError: order of element not known

        sage: DirichletGroup(7, CC, zeta=exp(2*pi*I/6), zeta_order=6)                   # needs sage.symbolic
        Group of Dirichlet characters modulo 7 with values in the group of order 6
         generated by 0.500000000000000 + 0.866025403784439*I
         in Complex Field with 53 bits of precision

    If the base ring is not a domain (in which case the group of roots
    of unity is not necessarily cyclic), some operations still work,
    such as creation of elements::

        sage: G = DirichletGroup(5, Zmod(15)); G
        Group of Dirichlet characters modulo 5 with values in Ring of integers modulo 15
        sage: chi = G([13]); chi
        Dirichlet character modulo 5 of conductor 5 mapping 2 |--> 13
        sage: chi^2
        Dirichlet character modulo 5 of conductor 5 mapping 2 |--> 4
        sage: chi.multiplicative_order()
        4

    Other operations only work if ``zeta`` is specified::

        sage: G.gens()
        Traceback (most recent call last):
        ...
        NotImplementedError: factorization of polynomials over rings
        with composite characteristic is not implemented
        sage: G = DirichletGroup(5, Zmod(15), zeta=2); G
        Group of Dirichlet characters modulo 5 with values in the group of order 4
         generated by 2 in Ring of integers modulo 15
        sage: G.gens()
        (Dirichlet character modulo 5 of conductor 5 mapping 2 |--> 2,)

    TESTS:

    Dirichlet groups are cached, creating two groups with the same parameters
    yields the same object::

        sage: DirichletGroup(60) is DirichletGroup(60)
        True

    Test for pickling::

        sage: G = DirichletGroup(9)
        sage: loads(dumps(G)) is G
        True
    """
    def create_key(self, N, base_ring=None, zeta=None, zeta_order=None, names=None, integral: bool = False):
        """
        Create a key that uniquely determines a Dirichlet group.

        TESTS::

            sage: DirichletGroup.create_key(60)
            (Cyclotomic Field of order 4 and degree 2, 60, None, None)

        An example to illustrate that ``base_ring`` is a part of the key::

            sage: k = DirichletGroup.create_key(2, base_ring=QQ); k
            (Rational Field, 2, None, None)
            sage: l = DirichletGroup.create_key(2, base_ring=CC); l
            (Complex Field with 53 bits of precision, 2, None, None)
            sage: k == l
            False
            sage: G = DirichletGroup.create_object(None, k); G
            Group of Dirichlet characters modulo 2 with values in Rational Field
            sage: H = DirichletGroup.create_object(None, l); H
            Group of Dirichlet characters modulo 2 with values in Complex Field with 53 bits of precision
            sage: G == H
            False

        If ``base_ring`` was not be a part of the key, the keys would compare
        equal and the caching would be broken::

            sage: k = k[1:]; k
            (2, None, None)
            sage: l = l[1:]; l
            (2, None, None)
            sage: k == l
            True
            sage: DirichletGroup(2, base_ring=QQ) is DirichletGroup(2, base_ring=CC)
            False

        If the base ring is not an integral domain, an error will be
        raised if only ``zeta_order`` is specified::

            sage: DirichletGroup(17, Integers(15))
            Group of Dirichlet characters modulo 17 with values in Ring of integers modulo 15
            sage: DirichletGroup(17, Integers(15), zeta_order=4)
            Traceback (most recent call last):
            ...
            ValueError: base ring (= Ring of integers modulo 15) must be an integral domain if only zeta_order is specified
            sage: G = DirichletGroup(17, Integers(15), zeta=7); G
            Group of Dirichlet characters modulo 17 with values in the group of order 4 generated by 7 in Ring of integers modulo 15
            sage: G.order()
            4

            sage: DirichletGroup(-33)
            Traceback (most recent call last):
            ...
            ValueError: modulus should be positive
        """
    def create_object(self, version, key, **extra_args):
        """
        Create the object from the key (extra arguments are ignored).

        This is only called if the object was not found in the cache.

        TESTS::

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(4)
            sage: DirichletGroup.create_object(None, (K, 60, K.gen(), 4))
            Group of Dirichlet characters modulo 60 with values in the group of order 4
             generated by zeta4 in Cyclotomic Field of order 4 and degree 2
        """

DirichletGroup: DirichletGroupFactory

def is_DirichletGroup(x) -> bool:
    """
    Return ``True`` if ``x`` is a Dirichlet group.

    EXAMPLES::

        sage: from sage.modular.dirichlet import is_DirichletGroup
        sage: is_DirichletGroup(DirichletGroup(11))
        doctest:warning...
        DeprecationWarning: The function is_DirichletGroup is deprecated; use 'isinstance(..., DirichletGroup_class)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        True
        sage: is_DirichletGroup(11)
        False
        sage: is_DirichletGroup(DirichletGroup(11).0)
        False
    """

class DirichletGroup_class(WithEqualityById, Parent):
    """
    Group of Dirichlet characters modulo `N` with values in a ring `R`.
    """
    Element = DirichletCharacter
    def __init__(self, base_ring, modulus, zeta, zeta_order) -> None:
        """
        Create a Dirichlet group.

        Not to be called directly (use the factory function ``DirichletGroup``).

        The ``DirichletGroup`` factory ensures that either both
        ``zeta`` and ``zeta_order`` are specified, or that both are
        ``None``.  In the former case, it also ensures that ``zeta``
        is an element of ``base_ring`` and that ``zeta_order`` is an
        element of ``ZZ``.

        TESTS::

            sage: G = DirichletGroup(7, base_ring=Integers(9), zeta=2)  # indirect doctest
            sage: TestSuite(G).run()
            sage: G.base()  # check that Parent.__init__ has been called
            Ring of integers modulo 9

            sage: DirichletGroup(13) == DirichletGroup(13)
            True
            sage: DirichletGroup(13) == DirichletGroup(13, QQ)
            False
        """
    def change_ring(self, R, zeta=None, zeta_order=None):
        """
        Return the base extension of ``self`` to ``R``.

        INPUT:

        - ``R`` -- either a ring admitting a conversion map from the
          base ring of ``self``, or a ring homomorphism with the base
          ring of ``self`` as its domain

        - ``zeta`` -- (optional) root of unity in ``R``

        - ``zeta_order`` -- (optional) order of ``zeta``

        EXAMPLES::

            sage: G = DirichletGroup(7,QQ); G
            Group of Dirichlet characters modulo 7 with values in Rational Field
            sage: G.change_ring(CyclotomicField(6))                                     # needs sage.rings.number_field
            Group of Dirichlet characters modulo 7 with values in
             Cyclotomic Field of order 6 and degree 2

        TESTS:

        We test the case where `R` is a map (:issue:`18072`)::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: f = K.complex_embeddings()[0]
            sage: D = DirichletGroup(5, K)
            sage: D.change_ring(f)
            Group of Dirichlet characters modulo 5 with values in
             Complex Field with 53 bits of precision
        """
    def base_extend(self, R):
        """
        Return the base extension of ``self`` to ``R``.

        INPUT:

        - ``R`` -- either a ring admitting a *coercion* map from the
          base ring of ``self``, or a ring homomorphism with the base
          ring of ``self`` as its domain

        EXAMPLES::

            sage: G = DirichletGroup(7,QQ); G
            Group of Dirichlet characters modulo 7 with values in Rational Field
            sage: H = G.base_extend(CyclotomicField(6)); H
            Group of Dirichlet characters modulo 7 with values in Cyclotomic Field of order 6 and degree 2

        Note that the root of unity can change::

            sage: H.zeta()
            zeta6

        This method (in contrast to :meth:`change_ring`) requires a
        coercion map to exist::

            sage: G.base_extend(ZZ)
            Traceback (most recent call last):
            ...
            TypeError: no coercion map from Rational Field to Integer Ring is defined

        Base-extended Dirichlet groups do not silently get roots of
        unity with smaller order than expected (:issue:`6018`)::

            sage: G = DirichletGroup(10, QQ).base_extend(CyclotomicField(4))
            sage: H = DirichletGroup(10, CyclotomicField(4))
            sage: G is H
            True

            sage: G3 = DirichletGroup(31, CyclotomicField(3))
            sage: G5 = DirichletGroup(31, CyclotomicField(5))
            sage: K30 = CyclotomicField(30)
            sage: G3.gen(0).base_extend(K30) * G5.gen(0).base_extend(K30)
            Dirichlet character modulo 31 of conductor 31 mapping 3 |--> -zeta30^7 + zeta30^5 + zeta30^4 + zeta30^3 - zeta30 - 1

        When a root of unity is specified, base extension still works
        if the new base ring is not an integral domain::

            sage: f = DirichletGroup(17, ZZ, zeta=-1).0
            sage: g = f.base_extend(Integers(15))
            sage: g(3)
            14
            sage: g.parent().zeta()
            14
        """
    def __len__(self) -> int:
        """
        Return the number of elements of this Dirichlet group.

        This is the same as self.order().

        EXAMPLES::

            sage: len(DirichletGroup(20))
            8
            sage: len(DirichletGroup(20, QQ))
            4
            sage: len(DirichletGroup(20, GF(5)))
            8
            sage: len(DirichletGroup(20, GF(2)))
            1
            sage: len(DirichletGroup(20, GF(3)))
            4
        """
    @cached_method
    def decomposition(self) -> list:
        '''
        Return the Dirichlet groups of prime power modulus corresponding
        to primes dividing modulus.

        (Note that if the modulus is 2 mod 4, there will be a "factor" of
        `(\\ZZ/2\\ZZ)^*`, which is the trivial group.)

        EXAMPLES::

            sage: DirichletGroup(20).decomposition()
            [Group of Dirichlet characters modulo 4 with values in Cyclotomic Field of order 4 and degree 2,
             Group of Dirichlet characters modulo 5 with values in Cyclotomic Field of order 4 and degree 2]
            sage: DirichletGroup(20,GF(5)).decomposition()
            [Group of Dirichlet characters modulo 4 with values in Finite Field of size 5,
             Group of Dirichlet characters modulo 5 with values in Finite Field of size 5]
        '''
    def exponent(self):
        """
        Return the exponent of this group.

        EXAMPLES::

            sage: DirichletGroup(20).exponent()
            4
            sage: DirichletGroup(20,GF(3)).exponent()
            2
            sage: DirichletGroup(20,GF(2)).exponent()
            1
            sage: DirichletGroup(37).exponent()
            36
        """
    def galois_orbits(self, v=None, reps_only: bool = False, sort: bool = True, check: bool = True):
        """
        Return a list of the Galois orbits of Dirichlet characters in ``self``,
        or in ``v`` if ``v`` is not ``None``.

        INPUT:

        - ``v`` -- (optional) list of elements of ``self``

        - ``reps_only`` -- (optional: default ``False``) if ``True``
          only returns representatives for the orbits

        - ``sort`` -- (optional: default ``True``) whether to sort
          the list of orbits and the orbits themselves (slightly faster if
          ``False``).

        - ``check`` -- boolean (default: ``True``); whether or not
          to explicitly coerce each element of ``v`` into ``self``

        The Galois group is the absolute Galois group of the prime subfield
        of Frac(R). If R is not a domain, an error will be raised.

        EXAMPLES::

            sage: DirichletGroup(20).galois_orbits()
            [[Dirichlet character modulo 20 of conductor 20 mapping ...]]
            sage: DirichletGroup(17, Integers(6), zeta=Integers(6)(5)).galois_orbits()
            Traceback (most recent call last):
            ...
            TypeError: Galois orbits only defined if base ring is an integral domain
            sage: DirichletGroup(17, Integers(9), zeta=Integers(9)(2)).galois_orbits()
            Traceback (most recent call last):
            ...
            TypeError: Galois orbits only defined if base ring is an integral domain
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of ``self``.

        EXAMPLES::

            sage: G = DirichletGroup(20)
            sage: G.gen(0)
            Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1
            sage: G.gen(1)
            Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> zeta4
            sage: G.gen(2)
            Traceback (most recent call last):
            ...
            IndexError: n(=2) must be between 0 and 1

        ::

            sage: G.gen(-1)
            Traceback (most recent call last):
            ...
            IndexError: n(=-1) must be between 0 and 1
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return generators of ``self``.

        EXAMPLES::

            sage: G = DirichletGroup(20)
            sage: G.gens()
            (Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1, Dirichlet character modulo 20 of conductor 5 mapping 11 |--> 1, 17 |--> zeta4)
        """
    def integers_mod(self):
        """
        Return the group of integers `\\ZZ/N\\ZZ`
        where `N` is the modulus of ``self``.

        EXAMPLES::

            sage: G = DirichletGroup(20)
            sage: G.integers_mod()
            Ring of integers modulo 20
        """
    __iter__ = multiplicative_iterator
    def list(self) -> list:
        """
        Return a list of the Dirichlet characters in this group.

        EXAMPLES::

            sage: DirichletGroup(5).list()
            [Dirichlet character modulo 5 of conductor 1 mapping 2 |--> 1,
             Dirichlet character modulo 5 of conductor 5 mapping 2 |--> zeta4,
             Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -1,
             Dirichlet character modulo 5 of conductor 5 mapping 2 |--> -zeta4]
        """
    def modulus(self):
        """
        Return the modulus of ``self``.

        EXAMPLES::

            sage: G = DirichletGroup(20)
            sage: G.modulus()
            20
        """
    def ngens(self) -> int:
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: G = DirichletGroup(20)
            sage: G.ngens()
            2
        """
    @cached_method
    def order(self):
        """
        Return the number of elements of ``self``.

        This is the same as len(self).

        EXAMPLES::

            sage: DirichletGroup(20).order()
            8
            sage: DirichletGroup(37).order()
            36
        """
    def random_element(self):
        """
        Return a random element of ``self``.

        The element is computed by multiplying a random power of each
        generator together, where the power is between 0 and the order of
        the generator minus 1, inclusive.

        EXAMPLES::

            sage: D = DirichletGroup(37)
            sage: g = D.random_element()
            sage: g.parent() is D
            True
            sage: g**36
            Dirichlet character modulo 37 of conductor 1 mapping 2 |--> 1
            sage: S = set(D.random_element().conductor() for _ in range(100))
            sage: while S != {1, 37}:
            ....:     S.add(D.random_element().conductor())

            sage: D = DirichletGroup(20)
            sage: g = D.random_element()
            sage: g.parent() is D
            True
            sage: g**4
            Dirichlet character modulo 20 of conductor 1 mapping 11 |--> 1, 17 |--> 1
            sage: S = set(D.random_element().conductor() for _ in range(100))
            sage: while S != {1, 4, 5, 20}:
            ....:     S.add(D.random_element().conductor())

            sage: D = DirichletGroup(60)
            sage: g = D.random_element()
            sage: g.parent() is D
            True
            sage: g**4
            Dirichlet character modulo 60 of conductor 1 mapping 31 |--> 1, 41 |--> 1, 37 |--> 1
            sage: S = set(D.random_element().conductor() for _ in range(100))
            sage: while S != {1, 3, 4, 5, 12, 15, 20, 60}:
            ....:     S.add(D.random_element().conductor())
        """
    def unit_gens(self) -> tuple:
        """
        Return the minimal generators for the units of
        `(\\ZZ/N\\ZZ)^*`, where `N` is the
        modulus of ``self``.

        EXAMPLES::

            sage: DirichletGroup(37).unit_gens()
            (2,)
            sage: DirichletGroup(20).unit_gens()
            (11, 17)
            sage: DirichletGroup(60).unit_gens()
            (31, 41, 37)
            sage: DirichletGroup(20,QQ).unit_gens()
            (11, 17)
        """
    @cached_method
    def zeta(self):
        """
        Return the chosen root of unity in the base ring.

        EXAMPLES::

            sage: DirichletGroup(37).zeta()
            zeta36
            sage: DirichletGroup(20).zeta()
            zeta4
            sage: DirichletGroup(60).zeta()
            zeta4
            sage: DirichletGroup(60,QQ).zeta()
            -1
            sage: DirichletGroup(60, GF(25,'a')).zeta()
            2
        """
    @cached_method
    def zeta_order(self):
        """
        Return the order of the chosen root of unity in the base ring.

        EXAMPLES::

            sage: DirichletGroup(20).zeta_order()
            4
            sage: DirichletGroup(60).zeta_order()
            4
            sage: DirichletGroup(60, GF(25,'a')).zeta_order()
            4
            sage: DirichletGroup(19).zeta_order()
            18
        """
