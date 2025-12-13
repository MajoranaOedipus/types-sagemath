import sage.modular.hecke.all as hecke
from . import defaults as defaults, hecke_operator_on_qexp as hecke_operator_on_qexp
from .element import ModularFormElement as ModularFormElement, Newform as Newform
from sage.arith.misc import gcd as gcd
from sage.categories.rings import Rings as Rings
from sage.matrix.constructor import zero_matrix as zero_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import PlusInfinity as PlusInfinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.power_series_ring_element import PowerSeries as PowerSeries
from sage.rings.rational_field import QQ as QQ
from sage.structure.all import Sequence as Sequence
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal

WARN: bool

def is_ModularFormsSpace(x):
    """
    Return ``True`` if x is a ``ModularFormsSpace``.

    EXAMPLES::

        sage: from sage.modular.modform.space import is_ModularFormsSpace
        sage: is_ModularFormsSpace(ModularForms(11,2))
        doctest:warning...
        DeprecationWarning: The function is_ModularFormsSpace is deprecated; use 'isinstance(..., ModularFormsSpace)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        True
        sage: is_ModularFormsSpace(CuspForms(11,2))
        True
        sage: is_ModularFormsSpace(3)
        False
    """

class ModularFormsSpace(hecke.HeckeModule_generic):
    """
    A generic space of modular forms.
    """
    Element = ModularFormElement
    def __init__(self, group, weight, character, base_ring, category=None) -> None:
        """
        Generic spaces of modular forms. For spaces of modular forms for
        `\\Gamma_0(N)` or `\\Gamma_1(N)`, the default base
        ring is `\\QQ`.

        EXAMPLES::

            sage: ModularForms(11,2)
            Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Rational Field

        ::

            sage: ModularForms(11,2,base_ring=GF(13))
            Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Finite Field of size 13

        ::

            sage: ModularForms(DirichletGroup(13).0,3)
            Modular Forms space of dimension 3, character [zeta12] and weight 3 over Cyclotomic Field of order 12 and degree 4

        ::

            sage: M = ModularForms(11,2)
            sage: M == loads(dumps(M))
            True
        """
    def prec(self, new_prec=None):
        """
        Return or set the default precision used for displaying
        `q`-expansions of elements of this space.

        INPUT:

        - ``new_prec`` -- positive integer (default: ``None``)

        OUTPUT: if new_prec is None, returns the current precision

        EXAMPLES::

            sage: M = ModularForms(1,12)
            sage: S = M.cuspidal_subspace()
            sage: S.prec()
            6
            sage: S.basis()
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)]
            sage: S.prec(8)
            8
            sage: S.basis()
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + O(q^8)]
        """
    def set_precision(self, new_prec) -> None:
        """
        Set the default precision used for displaying
        `q`-expansions.

        INPUT:

        - ``new_prec`` -- positive integer

        EXAMPLES::

            sage: M = ModularForms(Gamma0(37),2)
            sage: M.set_precision(10)
            sage: S = M.cuspidal_subspace()
            sage: S.basis()
            [q + q^3 - 2*q^4 - q^7 - 2*q^9 + O(q^10),
             q^2 + 2*q^3 - 2*q^4 + q^5 - 3*q^6 - 4*q^9 + O(q^10)]

        ::

            sage: S.set_precision(0)
            sage: S.basis()
            [O(q^0), O(q^0)]

        The precision of subspaces is the same as the precision of the
        ambient space.

        ::

            sage: S.set_precision(2)
            sage: M.basis()
            [q + O(q^2), O(q^2), 1 + 2/3*q + O(q^2)]

        The precision must be nonnegative::

            sage: S.set_precision(-1)
            Traceback (most recent call last):
            ...
            ValueError: n (=-1) must be >= 0

        We do another example with nontrivial character.

        ::

            sage: M = ModularForms(DirichletGroup(13).0^2)
            sage: M.set_precision(10)
            sage: M.cuspidal_subspace().0
            q + (-zeta6 - 1)*q^2 + (2*zeta6 - 2)*q^3 + zeta6*q^4 + (-2*zeta6 + 1)*q^5 + (-2*zeta6 + 4)*q^6 + (2*zeta6 - 1)*q^8 - zeta6*q^9 + O(q^10)
        """
    def weight(self):
        """
        Return the weight of this space of modular forms.

        EXAMPLES::

            sage: M = ModularForms(Gamma1(13),11)
            sage: M.weight()
            11

        ::

            sage: M = ModularForms(Gamma0(997),100)
            sage: M.weight()
            100

        ::

            sage: M = ModularForms(Gamma0(97),4)
            sage: M.weight()
            4
            sage: M.eisenstein_submodule().weight()
            4
        """
    def group(self):
        """
        Return the congruence subgroup associated to this space of modular
        forms.

        EXAMPLES::

            sage: ModularForms(Gamma0(12),4).group()
            Congruence Subgroup Gamma0(12)

        ::

            sage: CuspForms(Gamma1(113),2).group()
            Congruence Subgroup Gamma1(113)

        Note that `\\Gamma_1(1)` and `\\Gamma_0(1)` are replaced by
        `\\SL_2(\\ZZ)`.

        ::

            sage: CuspForms(Gamma1(1),12).group()
            Modular Group SL(2,Z)
            sage: CuspForms(SL2Z,12).group()
            Modular Group SL(2,Z)
        """
    def character(self):
        """
        Return the Dirichlet character corresponding to this space of
        modular forms. Returns None if there is no specific character
        corresponding to this space, e.g., if this is a space of modular
        forms on `\\Gamma_1(N)` with `N>1`.

        EXAMPLES: The trivial character::

            sage: ModularForms(Gamma0(11),2).character()
            Dirichlet character modulo 11 of conductor 1 mapping 2 |--> 1

        Spaces of forms with nontrivial character::

            sage: ModularForms(DirichletGroup(20).0,3).character()
            Dirichlet character modulo 20 of conductor 4 mapping 11 |--> -1, 17 |--> 1

            sage: M = ModularForms(DirichletGroup(11).0, 3)
            sage: M.character()
            Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta10
            sage: s = M.cuspidal_submodule()
            sage: s.character()
            Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta10
            sage: CuspForms(DirichletGroup(11).0,3).character()
            Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta10

        A space of forms with no particular character (hence None is
        returned)::

            sage: print(ModularForms(Gamma1(11),2).character())
            None

        If the level is one then the character is trivial.

        ::

            sage: ModularForms(Gamma1(1),12).character()
            Dirichlet character modulo 1 of conductor 1
        """
    def has_character(self) -> bool:
        """
        Return ``True`` if this space of modular forms has a specific
        character.

        This is ``True`` exactly when the ``character()`` function does not
        return ``None``.

        EXAMPLES: A space for `\\Gamma_0(N)` has trivial character,
        hence has a character.

        ::

            sage: CuspForms(Gamma0(11),2).has_character()
            True

        A space for `\\Gamma_1(N)` (for `N\\geq 2`) never
        has a specific character.

        ::

            sage: CuspForms(Gamma1(11),2).has_character()
            False
            sage: CuspForms(DirichletGroup(11).0,3).has_character()
            True
        """
    def is_ambient(self) -> bool:
        """
        Return ``True`` if this an ambient space of modular forms.

        EXAMPLES::

            sage: M = ModularForms(Gamma1(4),4)
            sage: M.is_ambient()
            True

        ::

            sage: E = M.eisenstein_subspace()
            sage: E.is_ambient()
            False
        """
    @cached_method
    def echelon_form(self):
        """
        Return a space of modular forms isomorphic to ``self`` but with basis
        of `q`-expansions in reduced echelon form.

        This is useful, e.g., the default basis for spaces of modular forms
        is rarely in echelon form, but echelon form is useful for quickly
        recognizing whether a `q`-expansion is in the space.

        EXAMPLES: We first illustrate two ambient spaces and their echelon
        forms.

        ::

            sage: M = ModularForms(11)
            sage: M.basis()
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
             1 + 12/5*q + 36/5*q^2 + 48/5*q^3 + 84/5*q^4 + 72/5*q^5 + O(q^6)]
            sage: M.echelon_form().basis()
            [1 + 12*q^2 + 12*q^3 + 12*q^4 + 12*q^5 + O(q^6),
             q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)]

        ::

            sage: M = ModularForms(Gamma1(6),4)
            sage: M.basis()
            [q - 2*q^2 - 3*q^3 + 4*q^4 + 6*q^5 + O(q^6),
             1 + O(q^6),
             q - 8*q^4 + 126*q^5 + O(q^6),
             q^2 + 9*q^4 + O(q^6),
             q^3 + O(q^6)]
            sage: M.echelon_form().basis()
            [1 + O(q^6),
             q + 94*q^5 + O(q^6),
             q^2 + 36*q^5 + O(q^6),
             q^3 + O(q^6),
             q^4 - 4*q^5 + O(q^6)]

        We create a space with a funny basis then compute the corresponding
        echelon form.

        ::

            sage: M = ModularForms(11,4)
            sage: M.basis()
            [q + 3*q^3 - 6*q^4 - 7*q^5 + O(q^6),
             q^2 - 4*q^3 + 2*q^4 + 8*q^5 + O(q^6),
             1 + O(q^6),
             q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6)]
            sage: F = M.span_of_basis([M.0 + 1/3*M.1, M.2 + M.3]); F.basis()
            [q + 1/3*q^2 + 5/3*q^3 - 16/3*q^4 - 13/3*q^5 + O(q^6),
             1 + q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6)]
            sage: E = F.echelon_form(); E.basis()
            [1 + 26/3*q^2 + 79/3*q^3 + 235/3*q^4 + 391/3*q^5 + O(q^6),
             q + 1/3*q^2 + 5/3*q^3 - 16/3*q^4 - 13/3*q^5 + O(q^6)]
        """
    @cached_method
    def echelon_basis(self):
        """
        Return a basis for ``self`` in reduced echelon form. This means that if
        we view the `q`-expansions of the basis as defining rows of
        a matrix (with infinitely many columns), then this matrix is in
        reduced echelon form.

        EXAMPLES::

            sage: M = ModularForms(Gamma0(11),4)
            sage: M.echelon_basis()
            [1 + O(q^6),
             q - 9*q^4 - 10*q^5 + O(q^6),
             q^2 + 6*q^4 + 12*q^5 + O(q^6),
             q^3 + q^4 + q^5 + O(q^6)]
            sage: M.cuspidal_subspace().echelon_basis()
            [q + 3*q^3 - 6*q^4 - 7*q^5 + O(q^6), q^2 - 4*q^3 + 2*q^4 + 8*q^5 + O(q^6)]

        ::

            sage: M = ModularForms(SL2Z, 12)
            sage: M.echelon_basis()
            [1 + 196560*q^2 + 16773120*q^3 + 398034000*q^4 + 4629381120*q^5 + O(q^6),
             q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)]

        ::

            sage: M = CuspForms(Gamma0(17),4, prec=10)
            sage: M.echelon_basis()
            [q + 2*q^5 - 8*q^7 - 8*q^8 + 7*q^9 + O(q^10),
             q^2 - 3/2*q^5 - 7/2*q^6 + 9/2*q^7 + q^8 - 4*q^9 + O(q^10),
             q^3 - 2*q^6 + q^7 - 4*q^8 - 2*q^9 + O(q^10),
             q^4 - 1/2*q^5 - 5/2*q^6 + 3/2*q^7 + 2*q^9 + O(q^10)]
        """
    @cached_method
    def integral_basis(self):
        """
        Return an integral basis for this space of modular forms.

        EXAMPLES:

        In this example the integral and echelon bases are
        different. ::

            sage: m = ModularForms(97,2,prec=10)
            sage: s = m.cuspidal_subspace()
            sage: s.integral_basis()
            [q + 2*q^7 + 4*q^8 - 2*q^9 + O(q^10),
             q^2 + q^4 + q^7 + 3*q^8 - 3*q^9 + O(q^10),
             q^3 + q^4 - 3*q^8 + q^9 + O(q^10),
             2*q^4 - 2*q^8 + O(q^10),
             q^5 - 2*q^8 + 2*q^9 + O(q^10),
             q^6 + 2*q^7 + 5*q^8 - 5*q^9 + O(q^10),
             3*q^7 + 6*q^8 - 4*q^9 + O(q^10)]
            sage: s.echelon_basis()
            [q + 2/3*q^9 + O(q^10),
             q^2 + 2*q^8 - 5/3*q^9 + O(q^10),
             q^3 - 2*q^8 + q^9 + O(q^10),
             q^4 - q^8 + O(q^10),
             q^5 - 2*q^8 + 2*q^9 + O(q^10),
             q^6 + q^8 - 7/3*q^9 + O(q^10),
             q^7 + 2*q^8 - 4/3*q^9 + O(q^10)]

        Here's another example where there is a big gap in the valuations::

            sage: m = CuspForms(64,2)
            sage: m.integral_basis()
            [q + O(q^6), q^2 + O(q^6), q^5 + O(q^6)]

        TESTS::

            sage: m = CuspForms(11*2^4,2, prec=13); m
            Cuspidal subspace of dimension 19 of Modular Forms space of dimension 30 for Congruence Subgroup Gamma0(176) of weight 2 over Rational Field
            sage: m.integral_basis()          # takes a long time (3 or 4 seconds)
            [q + O(q^13),
             q^2 + O(q^13),
             q^3 + O(q^13),
             q^4 + O(q^13),
             q^5 + O(q^13),
             q^6 + O(q^13),
             q^7 + O(q^13),
             q^8 + O(q^13),
             q^9 + O(q^13),
             q^10 + O(q^13),
             q^11 + O(q^13),
             q^12 + O(q^13),
             O(q^13),
             O(q^13),
             O(q^13),
             O(q^13),
             O(q^13),
             O(q^13),
             O(q^13)]
        """
    def q_expansion_basis(self, prec=None):
        """
        Return a sequence of `q`-expansions for the basis of this space
        computed to the given input precision.

        INPUT:

        - ``prec`` -- integer (>=0) or None

        If prec is None, the prec is computed to be *at least* large
        enough so that each `q`-expansion determines the form as an element
        of this space.

        .. NOTE::

           In fact, the `q`-expansion basis is always computed to
           *at least* ``self.prec()``.

        EXAMPLES::

            sage: S = ModularForms(11,2).cuspidal_submodule()
            sage: S.q_expansion_basis()
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)]
            sage: S.q_expansion_basis(5)
            [q - 2*q^2 - q^3 + 2*q^4 + O(q^5)]
            sage: S = ModularForms(1,24).cuspidal_submodule()
            sage: S.q_expansion_basis(8)
            [q + 195660*q^3 + 12080128*q^4 + 44656110*q^5 - 982499328*q^6 - 147247240*q^7 + O(q^8),
             q^2 - 48*q^3 + 1080*q^4 - 15040*q^5 + 143820*q^6 - 985824*q^7 + O(q^8)]

        An example which used to be buggy::

            sage: M = CuspForms(128, 2, prec=3)
            sage: M.q_expansion_basis()
            [q - q^17 + O(q^22),
             q^2 - 3*q^18 + O(q^22),
             q^3 - q^11 + q^19 + O(q^22),
             q^4 - 2*q^20 + O(q^22),
             q^5 - 3*q^21 + O(q^22),
             q^7 - q^15 + O(q^22),
             q^9 - q^17 + O(q^22),
             q^10 + O(q^22),
             q^13 - q^21 + O(q^22)]
        """
    def q_echelon_basis(self, prec=None):
        """
        Return the echelon form of the basis of `q`-expansions of
        ``self`` up to precision ``prec``.

        The `q`-expansions are power series (not actual modular
        forms). The number of `q`-expansions returned equals the
        dimension.

        EXAMPLES::

            sage: M = ModularForms(11,2)
            sage: M.q_expansion_basis()
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
             1 + 12/5*q + 36/5*q^2 + 48/5*q^3 + 84/5*q^4 + 72/5*q^5 + O(q^6)]

        ::

            sage: M.q_echelon_basis()
            [1 + 12*q^2 + 12*q^3 + 12*q^4 + 12*q^5 + O(q^6),
             q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)]
        """
    def q_integral_basis(self, prec=None):
        """
        Return a `\\ZZ`-reduced echelon basis of
        `q`-expansions for ``self``.

        The `q`-expansions are power series with coefficients in
        `\\ZZ`; they are *not* actual modular forms.

        The base ring of ``self`` must be `\\QQ`. The number of
        `q`-expansions returned equals the dimension.

        EXAMPLES::

            sage: S = CuspForms(11,2)
            sage: S.q_integral_basis(5)
            [q - 2*q^2 - q^3 + 2*q^4 + O(q^5)]
        """
    def __add__(self, right):
        """
        If ``self`` and ``right`` live inside the same ambient module, return the
        sum of the two spaces (as modules).

        EXAMPLES::

            sage: N = CuspForms(44,2) ; ls = [N.submodule([N(u) for u in x.q_expansion_basis(20)]) for x in N.modular_symbols().decomposition()]; ls
            [Modular Forms subspace of dimension 1 of Modular Forms space of dimension 9 for Congruence Subgroup Gamma0(44) of weight 2 over Rational Field,
            Modular Forms subspace of dimension 3 of Modular Forms space of dimension 9 for Congruence Subgroup Gamma0(44) of weight 2 over Rational Field]

        ::

            sage: N1 = ls[0] ; N2 = ls[1]
            sage: N1 + N2 # indirect doctest
            Modular Forms subspace of dimension 4 of Modular Forms space of dimension 9 for Congruence Subgroup Gamma0(44) of weight 2 over Rational Field
        """
    def __richcmp__(self, x, op):
        """
        Compare ``self`` and ``x``.

        For spaces of modular forms, we order first by signature, then by
        dimension, and then by the ordering on the underlying free
        modules.

        EXAMPLES::

            sage: N = ModularForms(6,4) ; S = N.cuspidal_subspace()
            sage: S < N
            True
            sage: N > S
            True
            sage: N == N
            True
            sage: M = ModularForms(11,2)
            sage: N < M
            True
            sage: M > N
            True
        """
    def span_of_basis(self, B):
        """
        Take a set B of forms, and return the subspace of ``self`` with B as a
        basis.

        EXAMPLES::

            sage: N = ModularForms(6,4) ; N
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field

        ::

            sage: N.span_of_basis([N.basis()[0]])
            Modular Forms subspace of dimension 1 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field

        ::

            sage: N.span_of_basis([N.basis()[0], N.basis()[1]])
            Modular Forms subspace of dimension 2 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field

        ::

            sage: N.span_of_basis( N.basis() )
            Modular Forms subspace of dimension 5 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field
        """
    span = span_of_basis
    @cached_method
    def basis(self):
        """
        Return a basis for ``self``.

        EXAMPLES::

            sage: MM = ModularForms(11,2)
            sage: MM.basis()
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
             1 + 12/5*q + 36/5*q^2 + 48/5*q^3 + 84/5*q^4 + 72/5*q^5 + O(q^6)]
        """
    def gen(self, n):
        """
        Return the `n`-th generator of ``self``.

        EXAMPLES::

            sage: N = ModularForms(6,4)
            sage: N.basis()
            [q - 2*q^2 - 3*q^3 + 4*q^4 + 6*q^5 + O(q^6),
             1 + O(q^6),
             q - 8*q^4 + 126*q^5 + O(q^6),
             q^2 + 9*q^4 + O(q^6),
             q^3 + O(q^6)]

        ::

            sage: N.gen(0)
            q - 2*q^2 - 3*q^3 + 4*q^4 + 6*q^5 + O(q^6)

        ::

            sage: N.gen(4)
            q^3 + O(q^6)

        ::

            sage: N.gen(5)
            Traceback (most recent call last):
            ...
            ValueError: Generator 5 not defined
        """
    def gens(self) -> tuple:
        """
        Return a complete set of generators for ``self``.

        EXAMPLES::

            sage: N = ModularForms(6,4)
            sage: N.gens()
            (q - 2*q^2 - 3*q^3 + 4*q^4 + 6*q^5 + O(q^6),
             1 + O(q^6),
             q - 8*q^4 + 126*q^5 + O(q^6),
             q^2 + 9*q^4 + O(q^6),
             q^3 + O(q^6))
        """
    def sturm_bound(self, M=None):
        """
        For a space M of modular forms, this function returns an integer B
        such that two modular forms in either ``self`` or M are equal if and
        only if their `q`-expansions are equal to precision B (note that this
        is 1+ the usual Sturm bound, since `O(q^\\mathrm{prec})` has
        precision ``prec``). If M is none, then M is set equal to ``self``.

        EXAMPLES::

            sage: S37=CuspForms(37,2)
            sage: S37.sturm_bound()
            8
            sage: M = ModularForms(11,2)
            sage: M.sturm_bound()
            3
            sage: ModularForms(Gamma1(15),2).sturm_bound()
            33

            sage: CuspForms(Gamma1(144), 3).sturm_bound()
            3457
            sage: CuspForms(DirichletGroup(144).1^2, 3).sturm_bound()
            73
            sage: CuspForms(Gamma0(144), 3).sturm_bound()
            73

        REFERENCES:

        - [Stu1987]_

        NOTE:

        Kevin Buzzard pointed out to me (William Stein) in Fall 2002 that
        the above bound is fine for Gamma1 with character, as one sees by
        taking a power of `f`. More precisely, if
        `f\\cong 0\\pmod{p}` for first `s` coefficients, then
        `f^r = 0 \\pmod{p}` for first `s r` coefficients.
        Since the weight of `f^r` is
        `r \\text{weight}(f)`, it follows that if
        `s \\geq` the Sturm bound for `\\Gamma_0` at
        weight(f), then `f^r` has valuation large enough to be
        forced to be `0` at `r\\cdot` weight(f) by Sturm
        bound (which is valid if we choose `r` right). Thus
        `f \\cong 0 \\pmod{p}`. Conclusion: For `\\Gamma_1`
        with fixed character, the Sturm bound is *exactly* the same as for
        `\\Gamma_0`. A key point is that we are finding
        `\\ZZ[\\varepsilon]` generators for the Hecke algebra
        here, not `\\ZZ`-generators. So if one wants
        generators for the Hecke algebra over `\\ZZ`, this
        bound is wrong.

        This bound works over any base, even a finite field. There might be
        much better bounds over `\\QQ`, or for comparing two
        eigenforms.
        """
    def cuspidal_submodule(self):
        """
        Return the cuspidal submodule of ``self``.

        EXAMPLES::

            sage: N = ModularForms(6,4) ; N
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field
            sage: N.eisenstein_subspace().dimension()
            4

        ::

            sage: N.cuspidal_submodule()
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field

        ::

            sage: N.cuspidal_submodule().dimension()
            1

        We check that a bug noticed on :issue:`10450` is fixed::

            sage: M = ModularForms(6, 10)
            sage: W = M.span_of_basis(M.basis()[0:2])
            sage: W.cuspidal_submodule()
            Modular Forms subspace of dimension 2 of Modular Forms space of dimension 11 for Congruence Subgroup Gamma0(6) of weight 10 over Rational Field
        """
    def cuspidal_subspace(self):
        """
        Synonym for cuspidal_submodule.

        EXAMPLES::

            sage: N = ModularForms(6,4) ; N
            Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field
            sage: N.eisenstein_subspace().dimension()
            4

        ::

            sage: N.cuspidal_subspace()
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(6) of weight 4 over Rational Field

        ::

            sage: N.cuspidal_submodule().dimension()
            1
        """
    def is_cuspidal(self) -> bool:
        """
        Return ``True`` if this space is cuspidal.

        EXAMPLES::

            sage: M = ModularForms(Gamma0(11), 2).new_submodule()
            sage: M.is_cuspidal()
            False
            sage: M.cuspidal_submodule().is_cuspidal()
            True
        """
    @cached_method
    def is_eisenstein(self) -> bool:
        """
        Return ``True`` if this space is Eisenstein.

        EXAMPLES::

            sage: M = ModularForms(Gamma0(11), 2).new_submodule()
            sage: M.is_eisenstein()
            False
            sage: M.eisenstein_submodule().is_eisenstein()
            True
        """
    def new_submodule(self, p=None) -> None:
        """
        Return the new submodule of ``self``.

        If `p` is specified, return the `p`-new submodule of ``self``.

        .. NOTE::

            This function should be overridden by all derived classes.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: M = sage.modular.modform.space.ModularFormsSpace(Gamma0(11), 2, DirichletGroup(1)[0], base_ring=QQ); M.new_submodule()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of new submodule not yet implemented
        """
    def new_subspace(self, p=None):
        """
        Synonym for new_submodule.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: M = sage.modular.modform.space.ModularFormsSpace(Gamma0(11), 2, DirichletGroup(1)[0], base_ring=QQ); M.new_subspace()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of new submodule not yet implemented
        """
    def eisenstein_series(self) -> None:
        """
        Compute the Eisenstein series associated to this space.

        .. NOTE::

           This function should be overridden by all derived classes.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: M = sage.modular.modform.space.ModularFormsSpace(Gamma0(11), 2, DirichletGroup(1)[0], base_ring=QQ); M.eisenstein_series()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of Eisenstein series in this space not yet implemented
        """
    def decomposition(self) -> None:
        """
        This function returns a list of submodules `V(f_i,t)`
        corresponding to newforms `f_i` of some level dividing the
        level of self, such that the direct sum of the submodules equals
        self, if possible. The space `V(f_i,t)` is the image under
        `g(q)` maps to `g(q^t)` of the intersection with
        `R[[q]]` of the space spanned by the conjugates of
        `f_i`, where `R` is the base ring of ``self``.

        TODO: Implement this function.

        EXAMPLES::

            sage: M = ModularForms(11,2); M.decomposition()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def newforms(self, names=None):
        """
        Return all newforms in the cuspidal subspace of ``self``.

        EXAMPLES::

            sage: CuspForms(18,4).newforms()
            [q + 2*q^2 + 4*q^4 - 6*q^5 + O(q^6)]
            sage: CuspForms(32,4).newforms()
            [q - 8*q^3 - 10*q^5 + O(q^6), q + 22*q^5 + O(q^6), q + 8*q^3 - 10*q^5 + O(q^6)]
            sage: CuspForms(23).newforms('b')
            [q + b0*q^2 + (-2*b0 - 1)*q^3 + (-b0 - 1)*q^4 + 2*b0*q^5 + O(q^6)]
            sage: CuspForms(23).newforms()
            Traceback (most recent call last):
            ...
            ValueError: Please specify a name to be used when generating names for generators of Hecke eigenvalue fields corresponding to the newforms.
        """
    @cached_method
    def eisenstein_submodule(self):
        """
        Return the Eisenstein submodule for this space of modular forms.

        EXAMPLES::

            sage: M = ModularForms(11,2)
            sage: M.eisenstein_submodule()
            Eisenstein subspace of dimension 1 of Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Rational Field

        We check that a bug noticed on :issue:`10450` is fixed::

            sage: M = ModularForms(6, 10)
            sage: W = M.span_of_basis(M.basis()[0:2])
            sage: W.eisenstein_submodule()
            Modular Forms subspace of dimension 0 of Modular Forms space of dimension 11 for Congruence Subgroup Gamma0(6) of weight 10 over Rational Field
        """
    def eisenstein_subspace(self):
        """
        Synonym for :meth:`eisenstein_submodule`.

        EXAMPLES::

            sage: M = ModularForms(11,2)
            sage: M.eisenstein_subspace()
            Eisenstein subspace of dimension 1 of Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Rational Field
        """
    def embedded_submodule(self):
        """
        Return the underlying module of ``self``.

        EXAMPLES::

            sage: N = ModularForms(6,4)
            sage: N.dimension()
            5

        ::

            sage: N.embedded_submodule()
            Vector space of dimension 5 over Rational Field
        """
    def level(self):
        """
        Return the level of ``self``.

        EXAMPLES::

            sage: M = ModularForms(47,3)
            sage: M.level()
            47
        """
    def modular_symbols(self, sign: int = 0) -> None:
        """
        Return the space of modular symbols corresponding to ``self`` with the
        given sign.

        .. NOTE::

            This function should be overridden by all derived classes.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: M = sage.modular.modform.space.ModularFormsSpace(Gamma0(11), 2, DirichletGroup(1)[0], base_ring=QQ); M.modular_symbols()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of associated modular symbols space not yet implemented
        """
    def find_in_space(self, f, forms=None, prec=None, indep: bool = True):
        """
        INPUT:

        - ``f`` -- a modular form or power series

        - ``forms`` -- (default: ``None``) a specific list of
          modular forms or `q`-expansions

        - ``prec`` -- if forms are given, compute with them to
          the given precision

        - ``indep`` -- boolean (default: ``True``); whether the given list
          of forms are assumed to form a basis

        OUTPUT: list of numbers that give f as a linear combination of
        the basis for this space or of the given forms if
        independent=True.

        .. NOTE::

           If the list of forms is given, they do *not* have to be in
           ``self``.

        EXAMPLES::

            sage: M = ModularForms(11,2)
            sage: N = ModularForms(10,2)
            sage: M.find_in_space( M.basis()[0] )
            [1, 0]

        ::

            sage: M.find_in_space( N.basis()[0], forms=N.basis() )
            [1, 0, 0]

        ::

            sage: M.find_in_space( N.basis()[0] )
            Traceback (most recent call last):
            ...
            ArithmeticError: vector is not in free module
        """

def contains_each(V, B):
    """
    Determine whether or not V contains every element of B. Used here
    for linear algebra, but works very generally.

    EXAMPLES::

        sage: contains_each = sage.modular.modform.space.contains_each
        sage: contains_each( range(20), prime_range(20) )
        True
        sage: contains_each( range(20), range(30) )
        False
    """
