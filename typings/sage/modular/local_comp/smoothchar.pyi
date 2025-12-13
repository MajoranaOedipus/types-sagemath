from sage.arith.functions import lcm as lcm
from sage.arith.misc import crt as crt
from sage.categories.groups import Groups as Groups
from sage.categories.rings import Rings as Rings
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.mrange import xmrange as xmrange
from sage.misc.verbose import verbose as verbose
from sage.modular.dirichlet import DirichletGroup as DirichletGroup
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import MultiplicativeGroupElement as MultiplicativeGroupElement, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence

class SmoothCharacterGeneric(MultiplicativeGroupElement):
    """
    A smooth (i.e. locally constant) character of `F^\\times`, for `F` some
    finite extension of `\\QQ_p`.
    """
    def __init__(self, parent, c, values_on_gens) -> None:
        """
        Standard init function.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(2, QQ)
            sage: G.character(0, [17]) # indirect doctest
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 0, mapping 2 |--> 17
            sage: G.character(1, [1, 17]) # indirect doctest
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 0, mapping 2 |--> 17
            sage: G.character(2, [1, -1, 1, 17]) # indirect doctest
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 2, mapping s |--> 1, 2*s + 1 |--> -1, -1 |--> 1, 2 |--> 17
            sage: G.character(2, [1, 1, 1, 17]) # indirect doctest
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 0, mapping 2 |--> 17
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: chi = SmoothCharacterGroupQp(5, QQ).character(5, [-1, 7])
            sage: D = {chi: 7}; D[chi] # indirect doctest
            7
        """
    def multiplicative_order(self):
        """
        Return the order of this character as an element of the character group.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: K.<z> = CyclotomicField(42)
            sage: G = SmoothCharacterGroupQp(7, K)
            sage: G.character(3, [z^10 - z^3, 11]).multiplicative_order()
            +Infinity
            sage: G.character(3, [z^10 - z^3, 1]).multiplicative_order()
            42
            sage: G.character(1, [z^7, z^14]).multiplicative_order()
            6
            sage: G.character(0, [1]).multiplicative_order()
            1
        """
    def level(self):
        """
        Return the level of this character, i.e. the smallest integer `c \\ge 0`
        such that it is trivial on `1 + \\mathfrak{p}^c`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, QQ).character(2, [-1, 1]).level()
            1
        """
    def __call__(self, x):
        """
        Evaluate the character at ``x``, which should be a nonzero element of
        the number field of the parent group.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: K.<z> = CyclotomicField(42)
            sage: chi = SmoothCharacterGroupQp(7, K).character(3, [z^10 - z^3, 11])
            sage: [chi(x) for x in [1, 2, 3, 9, 21, 1/12345678]]
            [1, -z, z^10 - z^3, -z^11 - z^10 + z^8 + z^7 - z^6 - z^5 + z^3 + z^2 - 1, 11*z^10 - 11*z^3, z^7 - 1]

        Non-examples::

            sage: chi(QuadraticField(-1,'i').gen())
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Number Field in i with defining polynomial x^2 + 1 with i = 1*I to Rational Field
            sage: chi(0)
            Traceback (most recent call last):
            ...
            ValueError: cannot evaluate at zero
            sage: chi(Mod(1, 12))
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Ring of integers modulo 12 to Rational Field

        Some examples with an unramified quadratic extension, where the choice
        of generators is arbitrary (but deterministic)::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: K.<z> = CyclotomicField(30)
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(5, K)
            sage: chi = G.character(2, [z**5, z**(-6), z**6, 3]); chi
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 2, mapping 11*s - 10 |--> z^5, 6 |--> -z^7 - z^6 + z^3 + z^2 - 1, 5*s + 1 |--> z^6, 5 |--> 3
            sage: chi(G.unit_gens(2)[0]**7 / G.unit_gens(2)[1]/5)
            1/3*z^6 - 1/3*z
            sage: chi(2)
            -z^3
        """
    def __invert__(self):
        """
        Multiplicative inverse of ``self``.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: K.<z> = CyclotomicField(12)
            sage: chi = SmoothCharacterGroupUnramifiedQuadratic(2, K).character(4, [z**4, z**3, z**9, -1, 7]); chi
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 4, mapping s |--> z^2 - 1, 2*s + 1 |--> z^3, 4*s + 1 |--> -z^3, -1 |--> -1, 2 |--> 7
            sage: chi**(-1) # indirect doctest
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 4, mapping s |--> -z^2, 2*s + 1 |--> -z^3, 4*s + 1 |--> z^3, -1 |--> -1, 2 |--> 1/7
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).character(0, [7]) / chi # indirect doctest
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 4, mapping s |--> -z^2, 2*s + 1 |--> -z^3, 4*s + 1 |--> z^3, -1 |--> -1, 2 |--> 1
        """
    def restrict_to_Qp(self):
        """
        Return the restriction of this character to `\\QQ_p^\\times`, embedded as
        a subfield of `F^\\times`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: SmoothCharacterGroupRamifiedQuadratic(3, 0, QQ).character(0, [2]).restrict_to_Qp()
            Character of Q_3*, of level 0, mapping 3 |--> 4
        """
    def galois_conjugate(self):
        """
        Return the composite of this character with the order `2` automorphism of
        `K / \\QQ_p` (assuming `K` is quadratic).

        Note that this is the Galois operation on the *domain*, not on the
        *codomain*.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: K.<w> = CyclotomicField(3)
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(2, K)
            sage: chi = G.character(2, [w, -1,-1, 3*w])
            sage: chi2 = chi.galois_conjugate(); chi2
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 2, mapping s |--> -w - 1, 2*s + 1 |--> 1, -1 |--> -1, 2 |--> 3*w

            sage: chi.restrict_to_Qp() == chi2.restrict_to_Qp()
            True
            sage: chi * chi2 == chi.parent().compose_with_norm(chi.restrict_to_Qp())
            True
        """

class SmoothCharacterGroupGeneric(Parent):
    """
    The group of smooth (i.e. locally constant) characters of a `p`-adic field,
    with values in some ring `R`. This is an abstract base class and should not
    be instantiated directly.
    """
    Element = SmoothCharacterGeneric
    def __init__(self, p, base_ring) -> None:
        '''
        TESTS::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: G = SmoothCharacterGroupGeneric(3, QQ)
            sage: SmoothCharacterGroupGeneric(3, "hello")
            Traceback (most recent call last):
            ...
            TypeError: base ring (=hello) must be a ring
        '''
    def __eq__(self, other):
        """
        TESTS::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(3, QQ)
            sage: G == SmoothCharacterGroupQp(3, QQ[I])
            False
            sage: G == 7
            False
            sage: G == SmoothCharacterGroupQp(7, QQ)
            False
            sage: G == SmoothCharacterGroupQp(3, QQ)
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(3, QQ)
            sage: G != SmoothCharacterGroupQp(3, QQ[I])
            True
            sage: G != 7
            True
            sage: G != SmoothCharacterGroupQp(7, QQ)
            True
            sage: G != SmoothCharacterGroupQp(3, QQ)
            False
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        TESTS::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(3, QQ)
            sage: hash(G) == hash(SmoothCharacterGroupQp(3, QQ[I]))
            False
            sage: hash(G) == hash(SmoothCharacterGroupQp(7, QQ))
            False
            sage: hash(G) == hash(SmoothCharacterGroupQp(3, QQ))
            True
        """
    def prime(self):
        """
        The residue characteristic of the underlying field.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).prime()
            3
        """
    @abstract_method
    def change_ring(self, ring) -> None:
        """
        Return the character group of the same field, but with values in a
        different coefficient ring. To be implemented by all derived classes
        (since the generic base class can't know the parameters).

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).change_ring(ZZ)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method change_ring at ...>
        """
    def base_extend(self, ring):
        """
        Return the character group of the same field, but with values in a new
        coefficient ring into which the old coefficient ring coerces. An error
        will be raised if there is no coercion map from the old coefficient
        ring to the new one.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(3, QQ)
            sage: G.base_extend(QQbar)
            Group of smooth characters of Q_3* with values in Algebraic Field
            sage: G.base_extend(Zmod(3))
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Rational Field to Ring of integers modulo 3
        """
    @abstract_method
    def ideal(self, level) -> None:
        """
        Return the ``level``-th power of the maximal ideal of the ring of
        integers of the `p`-adic field. Since we approximate by using number
        field arithmetic, what is actually returned is an ideal in a number
        field.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).ideal(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method ideal at ...>
        """
    @abstract_method
    def unit_gens(self, level) -> None:
        """
        A list of generators `x_1, \\dots, x_d` of the abelian group `F^\\times /
        (1 + \\mathfrak{p}^c)^\\times`, where `c` is the given level, satisfying
        no relations other than `x_i^{n_i} = 1` for each `i` (where the
        integers `n_i` are returned by :meth:`exponents`). We adopt the
        convention that the final generator `x_d` is a uniformiser (and `n_d =
        0`).

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).unit_gens(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method unit_gens at ...>
        """
    @abstract_method
    def exponents(self, level) -> None:
        """
        The orders `n_1, \\dots, n_d` of the generators `x_i` of `F^\\times / (1
        + \\mathfrak{p}^c)^\\times` returned by :meth:`unit_gens`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).exponents(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method exponents at ...>
        """
    @abstract_method
    def subgroup_gens(self, level) -> None:
        """
        A set of elements of `(\\mathcal{O}_F / \\mathfrak{p}^c)^\\times`
        generating the kernel of the reduction map to `(\\mathcal{O}_F /
        \\mathfrak{p}^{c-1})^\\times`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).subgroup_gens(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method subgroup_gens at ...>
        """
    @abstract_method
    def discrete_log(self, level) -> None:
        """
        Given an element `x \\in F^\\times` (lying in the number field `K` of
        which `F` is a completion, see module docstring), express the class of
        `x` in terms of the generators of `F^\\times / (1 +
        \\mathfrak{p}^c)^\\times` returned by :meth:`unit_gens`.

        This should be overridden by all derived classes. The method should
        first attempt to canonically coerce `x` into ``self.number_field()``,
        and check that the result is not zero.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupGeneric
            sage: SmoothCharacterGroupGeneric(3, QQ).discrete_log(3)
            Traceback (most recent call last):
            ...
            NotImplementedError: <abstract method discrete_log at ...>
        """
    def character(self, level, values_on_gens):
        """
        Return the unique character of the given level whose values on the
        generators returned by ``self.unit_gens(level)`` are
        ``values_on_gens``.

        INPUT:

        - ``level`` -- integer an integer `\\ge 0`
        - ``values_on_gens`` -- sequence a sequence of elements of length equal
          to the length of ``self.unit_gens(level)``. The values should be
          convertible (that is, possibly noncanonically) into the base ring of self; they
          should all be units, and all but the last must be roots of unity (of
          the orders given by ``self.exponents(level)``.

        .. NOTE::

            The character returned may have level less than ``level`` in general.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: K.<z> = CyclotomicField(42)
            sage: G = SmoothCharacterGroupQp(7, K)
            sage: G.character(2, [z^6, 8])
            Character of Q_7*, of level 2, mapping 3 |--> z^6, 7 |--> 8
            sage: G.character(2, [z^7, 8])
            Character of Q_7*, of level 1, mapping 3 |--> z^7, 7 |--> 8

        Non-examples::

            sage: G.character(1, [z, 1])
            Traceback (most recent call last):
            ...
            ValueError: value on generator 3 (=z) should be a root of unity of order 6
            sage: G.character(1, [1, 0])
            Traceback (most recent call last):
            ...
            ValueError: value on uniformiser 7 (=0) should be a unit

        An example with a funky coefficient ring::

            sage: G = SmoothCharacterGroupQp(7, Zmod(9))
            sage: G.character(1, [2, 2])
            Character of Q_7*, of level 1, mapping 3 |--> 2, 7 |--> 2
            sage: G.character(1, [2, 3])
            Traceback (most recent call last):
            ...
            ValueError: value on uniformiser 7 (=3) should be a unit

        TESTS::

            sage: G.character(1, [2])
            Traceback (most recent call last):
            ...
            AssertionError: 2 images must be given
        """
    def norm_character(self):
        """
        Return the normalised absolute value character in this group (mapping a
        uniformiser to `1/q` where `q` is the order of the residue field).

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp, SmoothCharacterGroupUnramifiedQuadratic
            sage: SmoothCharacterGroupQp(5, QQ).norm_character()
            Character of Q_5*, of level 0, mapping 5 |--> 1/5
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).norm_character()
            Character of unramified extension Q_2(s)* (s^2 + s + 1 = 0), of level 0, mapping 2 |--> 1/4
        """
    def compose_with_norm(self, chi):
        """
        Calculate the character of `K^\\times` given by `\\chi \\circ \\mathrm{Norm}_{K/\\QQ_p}`.
        Here `K` should be a quadratic extension and `\\chi` a character of `\\QQ_p^\\times`.

        EXAMPLES:

        When `K` is the unramified quadratic extension, the level of the new character is the same as the old::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp, SmoothCharacterGroupRamifiedQuadratic, SmoothCharacterGroupUnramifiedQuadratic
            sage: K.<w> = CyclotomicField(6)
            sage: G = SmoothCharacterGroupQp(3, K)
            sage: chi = G.character(2, [w, 5])
            sage: H = SmoothCharacterGroupUnramifiedQuadratic(3, K)
            sage: H.compose_with_norm(chi)
            Character of unramified extension Q_3(s)* (s^2 + 2*s + 2 = 0), of level 2, mapping -2*s |--> -1, 4 |--> -w, 3*s + 1 |--> w - 1, 3 |--> 25

        In ramified cases, the level of the new character may be larger:

        .. link

        ::

            sage: H = SmoothCharacterGroupRamifiedQuadratic(3, 0, K)
            sage: H.compose_with_norm(chi)
            Character of ramified extension Q_3(s)* (s^2 - 3 = 0), of level 3, mapping 2 |--> w - 1, s + 1 |--> -w, s |--> -5

        On the other hand, since norm is not surjective, the result can even be trivial:

        .. link

        ::

            sage: chi = G.character(1, [-1, -1]); chi
            Character of Q_3*, of level 1, mapping 2 |--> -1, 3 |--> -1
            sage: H.compose_with_norm(chi)
            Character of ramified extension Q_3(s)* (s^2 - 3 = 0), of level 0, mapping s |--> 1
        """

class SmoothCharacterGroupQp(SmoothCharacterGroupGeneric):
    """
    The group of smooth characters of `\\QQ_p^\\times`, with values in some fixed
    base ring.

    EXAMPLES::

        sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
        sage: G = SmoothCharacterGroupQp(7, QQ); G
        Group of smooth characters of Q_7* with values in Rational Field
        sage: TestSuite(G).run()
        sage: G == loads(dumps(G))
        True
    """
    def unit_gens(self, level):
        """
        Return a set of generators `x_1, \\dots, x_d` for `\\QQ_p^\\times / (1 +
        p^c \\ZZ_p)^\\times`. These must be independent in the sense that there
        are no relations between them other than relations of the form
        `x_i^{n_i} = 1`. They need not, however, be in Smith normal form.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, QQ).unit_gens(3)
            [3, 7]
            sage: SmoothCharacterGroupQp(2, QQ).unit_gens(4)
            [15, 5, 2]
        """
    def exponents(self, level):
        """
        Return the exponents of the generators returned by :meth:`unit_gens`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, QQ).exponents(3)
            [294, 0]
            sage: SmoothCharacterGroupQp(2, QQ).exponents(4)
            [2, 4, 0]
        """
    def change_ring(self, ring):
        """
        Return the group of characters of the same field but with values in a
        different ring. This need not have anything to do with the original
        base ring, and in particular there won't generally be a coercion map
        from ``self`` to the new group -- use
        :meth:`~SmoothCharacterGroupGeneric.base_extend` if you want this.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, Zmod(3)).change_ring(CC)
            Group of smooth characters of Q_7* with values in Complex Field with 53 bits of precision
        """
    def number_field(self):
        """
        Return the number field used for calculations (a dense subfield of the
        local field of which this is the character group). In this case, this
        is always the rational field.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, Zmod(3)).number_field()
            Rational Field
        """
    def ideal(self, level):
        """
        Return the ``level``-th power of the maximal ideal. Since we
        approximate by using rational arithmetic, what is actually returned is
        an ideal of `\\ZZ`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, Zmod(3)).ideal(2)
            Principal ideal (49) of Integer Ring
        """
    def discrete_log(self, level, x):
        """
        Express the class of `x` in `\\QQ_p^\\times / (1 + p^c)^\\times` in terms
        of the generators returned by :meth:`unit_gens`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(7, QQ)
            sage: G.discrete_log(0, 14)
            [1]
            sage: G.discrete_log(1, 14)
            [2, 1]
            sage: G.discrete_log(5, 14)
            [9308, 1]
        """
    def subgroup_gens(self, level):
        """
        Return a list of generators for the kernel of the map `(\\ZZ_p / p^c)^\\times
        \\to (\\ZZ_p / p^{c-1})^\\times`.

        INPUT:

        - ``c`` -- integer `\\ge 1`

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(7, QQ)
            sage: G.subgroup_gens(1)
            [3]
            sage: G.subgroup_gens(2)
            [8]

            sage: G = SmoothCharacterGroupQp(2, QQ)
            sage: G.subgroup_gens(1)
            []
            sage: G.subgroup_gens(2)
            [3]
            sage: G.subgroup_gens(3)
            [5]
        """
    def from_dirichlet(self, chi):
        """
        Given a Dirichlet character `\\chi`, return the factor at p of the
        adelic character `\\phi` which satisfies `\\phi(\\varpi_\\ell) =
        \\chi(\\ell)` for almost all `\\ell`, where `\\varpi_\\ell` is a uniformizer
        at `\\ell`.

        More concretely, if we write `\\chi = \\chi_p \\chi_M` as a product of
        characters of p-power, resp prime-to-p, conductor, then this function
        returns the character of `\\QQ_p^\\times` sending `p` to `\\chi_M(p)` and
        agreeing with `\\chi_p^{-1}` on integers that are 1 modulo M and coprime
        to `p`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: G = SmoothCharacterGroupQp(3, CyclotomicField(6))
            sage: G.from_dirichlet(DirichletGroup(9).0)
            Character of Q_3*, of level 2, mapping 2 |--> -zeta6 + 1, 3 |--> 1
        """
    def quadratic_chars(self):
        """
        Return a list of the (non-trivial) quadratic characters in this group.
        This will be a list of 3 characters, unless `p = 2` when there are 7.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp
            sage: SmoothCharacterGroupQp(7, QQ).quadratic_chars()
            [Character of Q_7*, of level 0, mapping 7 |--> -1,
             Character of Q_7*, of level 1, mapping 3 |--> -1, 7 |--> -1,
             Character of Q_7*, of level 1, mapping 3 |--> -1, 7 |--> 1]
            sage: SmoothCharacterGroupQp(2, QQ).quadratic_chars()
            [Character of Q_2*, of level 0, mapping 2 |--> -1,
             Character of Q_2*, of level 2, mapping 3 |--> -1, 2 |--> -1,
             Character of Q_2*, of level 2, mapping 3 |--> -1, 2 |--> 1,
             Character of Q_2*, of level 3, mapping 7 |--> -1, 5 |--> -1, 2 |--> -1,
             Character of Q_2*, of level 3, mapping 7 |--> -1, 5 |--> -1, 2 |--> 1,
             Character of Q_2*, of level 3, mapping 7 |--> 1, 5 |--> -1, 2 |--> -1,
             Character of Q_2*, of level 3, mapping 7 |--> 1, 5 |--> -1, 2 |--> 1]
        """

class SmoothCharacterGroupQuadratic(SmoothCharacterGroupGeneric):
    """
    The group of smooth characters of `E^\\times`, where `E` is a quadratic extension of `\\QQ_p`.
    """
    def discrete_log(self, level, x, gens=None):
        """
        Express the class of `x` in `F^\\times / (1 + \\mathfrak{p}^c)^\\times` in
        terms of the generators returned by ``self.unit_gens(level)``, or a
        custom set of generators if given.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(2, QQ)
            sage: G.discrete_log(0, 12)
            [2]
            sage: G.discrete_log(1, 12)
            [0, 2]
            sage: v = G.discrete_log(5, 12); v
            [0, 2, 0, 1, 2]
            sage: g = G.unit_gens(5); prod([g[i]**v[i] for i in [0..4]])/12 - 1 in G.ideal(5)
            True
            sage: G.discrete_log(3,G.number_field()([1,1]))
            [2, 0, 0, 1, 0]
            sage: H = SmoothCharacterGroupUnramifiedQuadratic(5, QQ)
            sage: x = H.number_field()([1,1]); x
            s + 1
            sage: v = H.discrete_log(5, x); v
            [22, 263, 379, 0]
            sage: h = H.unit_gens(5); prod([h[i]**v[i] for i in [0..3]])/x - 1 in H.ideal(5)
            True

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G = SmoothCharacterGroupRamifiedQuadratic(3, 1, QQ)
            sage: s = G.number_field().gen()
            sage: dl = G.discrete_log(4, 3 + 2*s)
            sage: gs = G.unit_gens(4); gs[0]^dl[0] * gs[1]^dl[1] * gs[2]^dl[2] * gs[3]^dl[3] - (3 + 2*s) in G.ideal(4)
            True

        An example with a custom generating set::

            sage: G.discrete_log(2, s+3, gens=[s, s+1, 2])
            [1, 2, 0]
        """
    @cached_method
    def quotient_gens(self, n):
        '''
        Return a list of elements of `E` which are a generating set for the
        quotient `E^\\times / \\QQ_p^\\times`, consisting of elements which are
        "minimal" in the sense of [LW12].

        In the examples we implement here, this quotient is almost always
        cyclic: the exceptions are the unramified quadratic extension of
        `\\QQ_2` for `n \\ge 3`, and the extension `\\QQ_3(\\sqrt{-3})` for `n \\ge
        4`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(7,QQ)
            sage: G.quotient_gens(1)
            [2*s - 2]
            sage: G.quotient_gens(2)
            [15*s + 21]
            sage: G.quotient_gens(3)
            [-75*s + 33]

        A ramified case::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G = SmoothCharacterGroupRamifiedQuadratic(7, 0, QQ)
            sage: G.quotient_gens(3)
            [22*s + 21]

        An example where the quotient group is not cyclic::

            sage: G = SmoothCharacterGroupUnramifiedQuadratic(2,QQ)
            sage: G.quotient_gens(1)
            [s + 1]
            sage: G.quotient_gens(2)
            [-s + 2]
            sage: G.quotient_gens(3)
            [-17*s - 14, 3*s - 2]
        '''
    def extend_character(self, level, chi, vals, check: bool = True):
        """
        Return the unique character of `F^\\times` which coincides with `\\chi`
        on `\\QQ_p^\\times` and maps the generators of the quotient returned by
        :meth:`quotient_gens` to ``vals``.

        INPUT:

        - ``chi`` -- a smooth character of `\\QQ_p`, where `p` is the residue
          characteristic of `F`, with values in the base ring of ``self`` (or some
          other ring coercible to it)
        - ``level`` -- the level of the new character (which should be at least
          the level of ``chi``)
        - ``vals`` -- a list of elements of the base ring of ``self`` (or some other
          ring coercible to it), specifying values on the quotients returned by
          :meth:`quotient_gens`

        A :exc:`ValueError` will be raised if `x^t \\ne \\chi(\\alpha^t)`, where `t`
        is the smallest integer such that `\\alpha^t` is congruent modulo
        `p^{\\rm level}` to an element of `\\QQ_p`.

        EXAMPLES:

        We extend an unramified character of `\\QQ_3^\\times` to the unramified
        quadratic extension in various ways.

        ::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupQp, SmoothCharacterGroupUnramifiedQuadratic
            sage: chi = SmoothCharacterGroupQp(5, QQ).character(0, [7]); chi
            Character of Q_5*, of level 0, mapping 5 |--> 7
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(5, QQ)
            sage: G.extend_character(1, chi, [-1])
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> -1, 5 |--> 7
            sage: G.extend_character(2, chi, [-1])
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> -1, 5 |--> 7
            sage: G.extend_character(3, chi, [1])
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 0, mapping 5 |--> 7
            sage: K.<z> = CyclotomicField(6); G.base_extend(K).extend_character(1, chi, [z])
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> -z + 1, 5 |--> 7

        We extend the nontrivial quadratic character::

            sage: chi = SmoothCharacterGroupQp(5, QQ).character(1, [-1, 7])
            sage: K.<z> = CyclotomicField(24); G.base_extend(K).extend_character(1, chi, [z^6])
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 1, mapping s |--> -z^6, 5 |--> 7

        Extensions of higher level::

            sage: K.<z> = CyclotomicField(20); rho = G.base_extend(K).extend_character(2, chi, [z]); rho
            Character of unramified extension Q_5(s)* (s^2 + 4*s + 2 = 0), of level 2, mapping 11*s - 10 |--> z^5, 6 |--> 1, 5*s + 1 |--> z^4, 5 |--> 7
            sage: rho(3)
            -1

        Examples where it doesn't work::

            sage: G.extend_character(1, chi, [1])
            Traceback (most recent call last):
            ...
            ValueError: Invalid values for extension

            sage: G = SmoothCharacterGroupQp(2, QQ); H = SmoothCharacterGroupUnramifiedQuadratic(2, QQ)
            sage: chi = G.character(3, [1, -1, 7])
            sage: H.extend_character(2, chi, [-1])
            Traceback (most recent call last):
            ...
            ValueError: Level of extended character cannot be smaller than level of character of Qp
        """

class SmoothCharacterGroupUnramifiedQuadratic(SmoothCharacterGroupQuadratic):
    """
    The group of smooth characters of `\\QQ_{p^2}^\\times`, where `\\QQ_{p^2}` is
    the unique unramified quadratic extension of `\\QQ_p`. We represent
    `\\QQ_{p^2}^\\times` internally as the completion at the prime above `p` of a
    quadratic number field, defined by (the obvious lift to `\\ZZ` of) the
    Conway polynomial modulo `p` of degree 2.

    EXAMPLES::

        sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
        sage: G = SmoothCharacterGroupUnramifiedQuadratic(3, QQ); G
        Group of smooth characters of unramified extension Q_3(s)* (s^2 + 2*s + 2 = 0) with values in Rational Field
        sage: G.unit_gens(3)
        [-11*s, 4, 3*s + 1, 3]
        sage: TestSuite(G).run()
        sage: TestSuite(SmoothCharacterGroupUnramifiedQuadratic(2, QQ)).run()
    """
    def __init__(self, prime, base_ring, names: str = 's') -> None:
        """
        Standard initialisation function.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(3, QQ, 'foo'); G
            Group of smooth characters of unramified extension Q_3(foo)* (foo^2 + 2*foo + 2 = 0) with values in Rational Field
            sage: G == loads(dumps(G))
            True
        """
    def change_ring(self, ring):
        """
        Return the character group of the same field, but with values in a
        different coefficient ring. This need not have anything to do with the
        original base ring, and in particular there won't generally be a
        coercion map from ``self`` to the new group -- use
        :meth:`~SmoothCharacterGroupGeneric.base_extend` if you want this.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, Zmod(3), names='foo').change_ring(CC)
            Group of smooth characters of unramified extension Q_7(foo)* (foo^2 + 6*foo + 3 = 0) with values in Complex Field with 53 bits of precision
        """
    def number_field(self):
        """
        Return a number field of which this is the completion at `p`, defined by a polynomial
        whose discriminant is not divisible by `p`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ, 'a').number_field()
            Number Field in a with defining polynomial x^2 + 6*x + 3
            sage: SmoothCharacterGroupUnramifiedQuadratic(5, QQ, 'b').number_field()
            Number Field in b with defining polynomial x^2 + 4*x + 2
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ, 'c').number_field()
            Number Field in c with defining polynomial x^2 + x + 1
        """
    @cached_method
    def ideal(self, c):
        """
        Return the ideal `p^c` of ``self.number_field()``. The result is
        cached, since we use the methods
        :meth:`~sage.rings.number_field.number_field_ideal.NumberFieldFractionalIdeal.idealstar` and
        :meth:`~sage.rings.number_field.number_field_ideal.NumberFieldFractionalIdeal.ideallog` which
        cache a Pari ``bid`` structure.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: G = SmoothCharacterGroupUnramifiedQuadratic(7, QQ, 'a'); I = G.ideal(3); I
            Fractional ideal (343)
            sage: I is G.ideal(3)
            True
        """
    @cached_method
    def unit_gens(self, c):
        """
        A list of generators `x_1, \\dots, x_d` of the abelian group `F^\\times /
        (1 + \\mathfrak{p}^c)^\\times`, where `c` is the given level, satisfying
        no relations other than `x_i^{n_i} = 1` for each `i` (where the
        integers `n_i` are returned by :meth:`exponents`). We adopt the
        convention that the final generator `x_d` is a uniformiser (and `n_d =
        0`).

        ALGORITHM: Use Teichmueller lifts.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).unit_gens(0)
            [7]
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).unit_gens(1)
            [s, 7]
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).unit_gens(2)
            [22*s, 8, 7*s + 1, 7]
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).unit_gens(3)
            [169*s + 49, 8, 7*s + 1, 7]

        In the 2-adic case there can be more than 4 generators::

            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).unit_gens(0)
            [2]
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).unit_gens(1)
            [s, 2]
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).unit_gens(2)
            [s, 2*s + 1, -1, 2]
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).unit_gens(3)
            [s, 2*s + 1, 4*s + 1, -1, 2]
        """
    def exponents(self, c):
        """
        The orders `n_1, \\dots, n_d` of the generators `x_i` of `F^\\times / (1
        + \\mathfrak{p}^c)^\\times` returned by :meth:`unit_gens`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).exponents(2)
            [48, 7, 7, 0]
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).exponents(3)
            [3, 4, 2, 2, 0]
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).exponents(2)
            [3, 2, 2, 0]
        """
    def subgroup_gens(self, level):
        """
        A set of elements of `(\\mathcal{O}_F / \\mathfrak{p}^c)^\\times`
        generating the kernel of the reduction map to `(\\mathcal{O}_F /
        \\mathfrak{p}^{c-1})^\\times`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupUnramifiedQuadratic
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).subgroup_gens(1)
            [s]
            sage: SmoothCharacterGroupUnramifiedQuadratic(7, QQ).subgroup_gens(2)
            [8, 7*s + 1]
            sage: SmoothCharacterGroupUnramifiedQuadratic(2, QQ).subgroup_gens(2)
            [3, 2*s + 1]
        """

class SmoothCharacterGroupRamifiedQuadratic(SmoothCharacterGroupQuadratic):
    """
    The group of smooth characters of `K^\\times`, where `K` is a ramified
    quadratic extension of `\\QQ_p`, and `p \\ne 2`.
    """
    def __init__(self, prime, flag, base_ring, names: str = 's') -> None:
        """
        Standard initialisation function.

        INPUT:

        - ``prime`` -- prime integer
        - ``flag`` -- either 0 or 1
        - ``base_ring`` -- a ring
        - ``names`` -- a variable name (default: ``'s'``)

        If ``flag`` is 0, return the group of characters of the multiplicative
        group of the field `\\QQ_p(\\sqrt{p})`. If ``flag`` is 1, use the
        extension `\\QQ_p(\\sqrt{dp})`, where `d` is `-1` (if `p = 3 \\pmod 4`) or
        the smallest positive quadratic nonresidue mod `p` otherwise.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G1 = SmoothCharacterGroupRamifiedQuadratic(3, 0, QQ); G1
            Group of smooth characters of ramified extension Q_3(s)* (s^2 - 3 = 0) with values in Rational Field
            sage: G2 = SmoothCharacterGroupRamifiedQuadratic(3, 1, QQ); G2
            Group of smooth characters of ramified extension Q_3(s)* (s^2 - 6 = 0) with values in Rational Field
            sage: G3 = SmoothCharacterGroupRamifiedQuadratic(5, 1, QQ); G3
            Group of smooth characters of ramified extension Q_5(s)* (s^2 - 10 = 0) with values in Rational Field

        TESTS:

        .. link

        ::

            sage: TestSuite(G1).run()
            sage: TestSuite(G2).run()
            sage: TestSuite(G3).run()
        """
    def change_ring(self, ring):
        """
        Return the character group of the same field, but with values in a
        different coefficient ring. This need not have anything to do with the
        original base ring, and in particular there won't generally be a
        coercion map from ``self`` to the new group -- use
        :meth:`~SmoothCharacterGroupGeneric.base_extend` if you want this.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: SmoothCharacterGroupRamifiedQuadratic(7, 1, Zmod(3), names='foo').change_ring(CC)
            Group of smooth characters of ramified extension Q_7(foo)* (foo^2 - 35 = 0) with values in Complex Field with 53 bits of precision
        """
    def number_field(self):
        """
        Return a number field of which this is the completion at `p`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: SmoothCharacterGroupRamifiedQuadratic(7, 0, QQ, 'a').number_field()
            Number Field in a with defining polynomial x^2 - 7
            sage: SmoothCharacterGroupRamifiedQuadratic(5, 1, QQ, 'b').number_field()
            Number Field in b with defining polynomial x^2 - 10
            sage: SmoothCharacterGroupRamifiedQuadratic(7, 1, Zmod(6), 'c').number_field()
            Number Field in c with defining polynomial x^2 - 35
        """
    @cached_method
    def ideal(self, c):
        """
        Return the ideal `p^c` of ``self.number_field()``. The result is
        cached, since we use the methods
        :meth:`~sage.rings.number_field.number_field_ideal.NumberFieldFractionalIdeal.idealstar` and
        :meth:`~sage.rings.number_field.number_field_ideal.NumberFieldFractionalIdeal.ideallog` which
        cache a Pari ``bid`` structure.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G = SmoothCharacterGroupRamifiedQuadratic(5, 1, QQ, 'a'); I = G.ideal(3); I
            Fractional ideal (25, 5*a)
            sage: I is G.ideal(3)
            True
        """
    def unit_gens(self, c):
        """
        A list of generators `x_1, \\dots, x_d` of the abelian group `F^\\times /
        (1 + \\mathfrak{p}^c)^\\times`, where `c` is the given level, satisfying
        no relations other than `x_i^{n_i} = 1` for each `i` (where the
        integers `n_i` are returned by :meth:`exponents`). We adopt the
        convention that the final generator `x_d` is a uniformiser.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G = SmoothCharacterGroupRamifiedQuadratic(5, 0, QQ)
            sage: G.unit_gens(0)
            [s]
            sage: G.unit_gens(1)
            [2, s]
            sage: G.unit_gens(8)
            [2, s + 1, s]
        """
    def exponents(self, c):
        """
        Return the orders of the independent generators of the unit group
        returned by :meth:`~unit_gens`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G = SmoothCharacterGroupRamifiedQuadratic(5, 0, QQ)
            sage: G.exponents(0)
            (0,)
            sage: G.exponents(1)
            (4, 0)
            sage: G.exponents(8)
            (500, 625, 0)
        """
    def subgroup_gens(self, level):
        """
        A set of elements of `(\\mathcal{O}_F / \\mathfrak{p}^c)^\\times`
        generating the kernel of the reduction map to `(\\mathcal{O}_F /
        \\mathfrak{p}^{c-1})^\\times`.

        EXAMPLES::

            sage: from sage.modular.local_comp.smoothchar import SmoothCharacterGroupRamifiedQuadratic
            sage: G = SmoothCharacterGroupRamifiedQuadratic(3, 1, QQ)
            sage: G.subgroup_gens(2)
            [s + 1]
        """
