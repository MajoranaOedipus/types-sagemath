from .constructor import ModularForms as ModularForms
from .element import GradedModularFormElement as GradedModularFormElement, ModularFormElement as ModularFormElement
from .space import ModularFormsSpace as ModularFormsSpace
from _typeshed import Incomplete
from sage.categories.graded_algebras import GradedAlgebras as GradedAlgebras
from sage.matrix.constructor import Matrix as Matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.misc.verbose import verbose as verbose
from sage.modular.arithgroup.congroup_generic import CongruenceSubgroupBase as CongruenceSubgroupBase
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.power_series_poly import PowerSeries_poly as PowerSeries_poly
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

class ModularFormsRing(Parent):
    """
    The ring of modular forms (of weights 0 or at least 2) for a congruence
    subgroup of `\\SL_2(\\ZZ)`, with coefficients in a specified base ring.

    EXAMPLES::

        sage: ModularFormsRing(Gamma1(13))
        Ring of Modular Forms for Congruence Subgroup Gamma1(13) over Rational Field
        sage: m = ModularFormsRing(4); m
        Ring of Modular Forms for Congruence Subgroup Gamma0(4) over Rational Field
        sage: m.modular_forms_of_weight(2)
        Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(4) of weight 2 over Rational Field
        sage: m.modular_forms_of_weight(10)
        Modular Forms space of dimension 6 for Congruence Subgroup Gamma0(4) of weight 10 over Rational Field
        sage: m == loads(dumps(m))
        True
        sage: m.generators()
        [(2, 1 + 24*q^2 + 24*q^4 + 96*q^6 + 24*q^8 + O(q^10)),
         (2, q + 4*q^3 + 6*q^5 + 8*q^7 + 13*q^9 + O(q^10))]
        sage: m.q_expansion_basis(2,10)
        [1 + 24*q^2 + 24*q^4 + 96*q^6 + 24*q^8 + O(q^10),
         q + 4*q^3 + 6*q^5 + 8*q^7 + 13*q^9 + O(q^10)]
        sage: m.q_expansion_basis(3,10)
        []
        sage: m.q_expansion_basis(10,10)
        [1 + 10560*q^6 + 3960*q^8 + O(q^10),
         q - 8056*q^7 - 30855*q^9 + O(q^10),
         q^2 - 796*q^6 - 8192*q^8 + O(q^10),
         q^3 + 66*q^7 + 832*q^9 + O(q^10),
         q^4 + 40*q^6 + 528*q^8 + O(q^10),
         q^5 + 20*q^7 + 190*q^9 + O(q^10)]

    Elements of modular forms ring can be initiated via multivariate polynomials (see :meth:`from_polynomial`)::

        sage: M = ModularFormsRing(1)
        sage: M.ngens()
        2
        sage: E4, E6 = polygens(QQ, 'E4, E6')
        sage: M(E4)
        1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
        sage: M(E6)
        1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)
        sage: M((E4^3 - E6^2)/1728)
        q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
    """
    Element = GradedModularFormElement
    def __init__(self, group, base_ring=...) -> None:
        """
        INPUT:

        - ``group`` -- a congruence subgroup of `\\SL_2(\\ZZ)`, or a
          positive integer `N` (interpreted as `\\Gamma_0(N)`)

        - ``base_ring`` -- ring (default: `\\QQ`); a base ring, which
          should be `\\QQ`, `\\ZZ`, or the integers mod `p` for some prime
          `p`

        TESTS:

        Check that :issue:`15037` is fixed::

            sage: ModularFormsRing(3.4)
            Traceback (most recent call last):
            ...
            ValueError: group (=3.40000000000000) should be a congruence subgroup
            sage: ModularFormsRing(Gamma0(2), base_ring=PolynomialRing(ZZ, 'x'))
            Traceback (most recent call last):
            ...
            ValueError: base ring (=Univariate Polynomial Ring in x over Integer Ring) should be QQ, ZZ or a finite prime field

        ::

            sage: TestSuite(ModularFormsRing(1)).run()
            sage: TestSuite(ModularFormsRing(Gamma0(6))).run()
            sage: TestSuite(ModularFormsRing(Gamma1(4))).run()

        .. TODO::

            - Add graded modular forms over non-trivial Dirichlet character;
            - makes gen_forms returns modular forms over base rings other than `QQ`;
            - implement binary operations between two forms with different groups.
        """
    def change_ring(self, base_ring):
        """
        Return a ring of modular forms over a new base ring of the same
        congruence subgroup.

        INPUT:

        - ``base_ring`` -- a base ring, which should be `\\QQ`, `\\ZZ`, or
          the integers mod `p` for some prime `p`

        EXAMPLES::

            sage: M = ModularFormsRing(11); M
            Ring of Modular Forms for Congruence Subgroup Gamma0(11) over Rational Field
            sage: M.change_ring(Zmod(7))
            Ring of Modular Forms for Congruence Subgroup Gamma0(11) over Ring of integers modulo 7
            sage: M.change_ring(ZZ)
            Ring of Modular Forms for Congruence Subgroup Gamma0(11) over Integer Ring
        """
    def some_elements(self):
        """
        Return some elements of this ring.

        EXAMPLES::

            sage: ModularFormsRing(1).some_elements()
            [1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6),
             1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)]
        """
    def group(self):
        """
        Return the congruence subgroup of this ring of modular forms.

        EXAMPLES::

            sage: R = ModularFormsRing(Gamma1(13))
            sage: R.group() is Gamma1(13)
            True
        """
    def gen(self, i):
        """
        Return the `i`-th generator of this ring.

        INPUT:

        - ``i`` -- integer

        OUTPUT: an instance of :class:`~sage.modular.modform.GradedModularFormElement`

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: E4 = M.0; E4 # indirect doctest
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: E6 = M.1; E6 # indirect doctest
            1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)
        """
    def ngens(self):
        """
        Return the number of generators of this ring.

        EXAMPLES::

            sage: ModularFormsRing(1).ngens()
            2
            sage: ModularFormsRing(Gamma0(2)).ngens()
            2
            sage: ModularFormsRing(Gamma1(13)).ngens() # long time
            33

        .. WARNING::

            Computing the number of generators of a graded ring of modular form for a certain
            congruence subgroup can be very long.
        """
    def polynomial_ring(self, names, gens=None):
        """
        Return a polynomial ring of which this ring of modular forms is
        a quotient.

        INPUT:

        - ``names`` -- a list or tuple of names (strings), or a comma
          separated string; consists in the names of the polynomial
          ring variables
        - ``gens`` -- list of modular forms generating this ring
          (default: ``None``); if ``gens`` is ``None`` then the list of
          generators returned by the method
          :meth:`~sage.modular.modform.find_generator.ModularFormsRing.gen_forms`
          is used instead. Note that we do not check if the list is
          indeed a generating set.

        OUTPUT: a multivariate polynomial ring in the variable
        ``names``. Each variable of the polynomial ring correspond to a
        generator given in the list ``gens`` (following the ordering of
        the list).

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: gens = M.gen_forms()
            sage: M.polynomial_ring('E4, E6', gens)
            Multivariate Polynomial Ring in E4, E6 over Rational Field
            sage: M = ModularFormsRing(Gamma0(8))
            sage: gens = M.gen_forms()
            sage: M.polynomial_ring('g', gens)
            Multivariate Polynomial Ring in g0, g1, g2 over Rational Field

        The degrees of the variables are the weights of the
        corresponding forms::

            sage: M = ModularFormsRing(1)
            sage: P.<E4, E6> = M.polynomial_ring()
            sage: E4.degree()
            4
            sage: E6.degree()
            6
            sage: (E4*E6).degree()
            10
        """
    def from_polynomial(self, polynomial, gens=None):
        """
        Return a graded modular form constructed by evaluating a given
        multivariate polynomial at a set of generators.

        INPUT:

        - ``polynomial`` -- a multivariate polynomial. The variables
          names of the polynomial should be different from ``'q'``. The
          number of variable of this polynomial should equal the number
          of given generators.
        - ``gens`` -- list of modular forms generating this ring
          (default: ``None``); if ``gens`` is ``None`` then the list of
          generators returned by the method
          :meth:`~sage.modular.modform.find_generator.ModularFormsRing.gen_forms`
          is used instead. Note that we do not check if the list is
          indeed a generating set.

        OUTPUT: a ``GradedModularFormElement`` given by the polynomial
        relation ``polynomial``

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: x,y = polygens(QQ, 'x,y')
            sage: M.from_polynomial(x^2+y^3)
            2 - 1032*q + 774072*q^2 - 77047584*q^3 - 11466304584*q^4 - 498052467504*q^5 + O(q^6)
            sage: M = ModularFormsRing(Gamma0(6))
            sage: M.ngens()
            3
            sage: x,y,z = polygens(QQ, 'x,y,z')
            sage: M.from_polynomial(x+y+z)
            1 + q + q^2 + 27*q^3 + q^4 + 6*q^5 + O(q^6)
            sage: M.0 + M.1 + M.2
            1 + q + q^2 + 27*q^3 + q^4 + 6*q^5 + O(q^6)
            sage: P = x.parent()
            sage: M.from_polynomial(P(1/2))
            1/2

        Note that the number of variables must be equal to the number of
        generators::

            sage: x, y = polygens(QQ, 'x, y')
            sage: M(x + y)
            Traceback (most recent call last):
            ...
            ValueError: the number of variables (2) must be equal to the number of generators of the modular forms ring (3)

        TESTS::

            sage: x,y = polygens(GF(7), 'x, y')
            sage: ModularFormsRing(1, GF(7))(x)
            Traceback (most recent call last):
            ...
            NotImplementedError: conversion from polynomial is not implemented if the base ring is not Q

        ..TODO::

            * add conversion for symbolic expressions?
        """
    def zero(self):
        """
        Return the zero element of this ring.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: zer = M.zero(); zer
            0
            sage: zer.is_zero()
            True
            sage: E4 = ModularForms(1,4).0; E4
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: E4 + zer
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: zer * E4
            0
            sage: E4 * zer
            0
        """
    def one(self):
        """
        Return the one element of this ring.

        EXAMPLES::

            sage: M = ModularFormsRing(1)
            sage: u = M.one(); u
            1
            sage: u.is_one()
            True
            sage: u + u
            2
            sage: E4 = ModularForms(1,4).0; E4
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
            sage: E4 * u
            1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` to ``other``.

        Rings are equal if and only if their groups and base rings are.

        EXAMPLES::

            sage: ModularFormsRing(3) == 3
            False
            sage: ModularFormsRing(Gamma0(3)) == ModularFormsRing(Gamma0(7))
            False
            sage: ModularFormsRing(Gamma0(3)) == ModularFormsRing(Gamma0(3))
            True
        """
    def modular_forms_of_weight(self, weight):
        """
        Return the space of modular forms of the given weight and the
        same congruence subgroup.

        EXAMPLES::

            sage: R = ModularFormsRing(13)
            sage: R.modular_forms_of_weight(10)
            Modular Forms space of dimension 11 for Congruence Subgroup Gamma0(13) of weight 10 over Rational Field
            sage: ModularFormsRing(Gamma1(13)).modular_forms_of_weight(3)
            Modular Forms space of dimension 20 for Congruence Subgroup Gamma1(13) of weight 3 over Rational Field
        """
    def generators(self, maxweight: int = 8, prec: int = 10, start_gens=[], start_weight: int = 2):
        """
        Return a list of generator of this ring as a list of pairs
        `(k, f)` where `k` is an integer and `f` is a univariate power
        series in `q` corresponding to the `q`-expansion of a modular
        form of weight `k`.

        More precisely, if `R` is the base ring of self, then this
        function calculates a set of modular forms which generate the
        `R`-algebra of all modular forms of weight up to ``maxweight``
        with coefficients in `R`.

        INPUT:

        - ``maxweight`` -- integer (default: 8); check up to this weight
          for generators

        - ``prec`` -- integer (default: 10); return `q`-expansions to
          this precision

        - ``start_gens`` -- list (default: ``[]``); list of pairs
          `(k, f)`, or triples `(k, f, F)`, where:

          - `k` is an integer,
          - `f` is the `q`-expansion of a modular form of weight `k`,
            as a power series over the base ring of self,
          - `F` (if provided) is a modular form object corresponding to F.

          If this list is nonempty, we find a minimal generating set containing
          these forms. If `F` is not supplied, then `f` needs to have
          sufficiently large precision (an error will be raised if this is not
          the case); otherwise, more terms will be calculated from the modular
          form object `F`.

        - ``start_weight`` -- integer (default: 2); calculate the graded
          subalgebra of forms of weight at least ``start_weight``

        OUTPUT:

        a list of pairs (k, f), where f is the `q`-expansion to precision
        ``prec`` of a modular form of weight k.

        .. SEEALSO::

            :meth:`gen_forms`, which does exactly the same thing, but returns
            Sage modular form objects rather than bare power series, and keeps
            track of a lifting to characteristic 0 when the base ring is a
            finite field.

        .. NOTE::

            If called with the default values of ``start_gens`` (an empty list)
            and ``start_weight`` (2), the values will be cached for re-use on
            subsequent calls to this function. (This cache is shared with
            :meth:`gen_forms`). If called with non-default values for these
            parameters, caching will be disabled.

        EXAMPLES::

            sage: ModularFormsRing(SL2Z).generators()
            [(4, 1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + 60480*q^6 + 82560*q^7 + 140400*q^8 + 181680*q^9 + O(q^10)),
             (6, 1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 - 4058208*q^6 - 8471232*q^7 - 17047800*q^8 - 29883672*q^9 + O(q^10))]
            sage: s = ModularFormsRing(SL2Z).generators(maxweight=5, prec=3); s
            [(4, 1 + 240*q + 2160*q^2 + O(q^3))]
            sage: s[0][1].parent()
            Power Series Ring in q over Rational Field

            sage: ModularFormsRing(1).generators(prec=4)
            [(4, 1 + 240*q + 2160*q^2 + 6720*q^3 + O(q^4)),
             (6, 1 - 504*q - 16632*q^2 - 122976*q^3 + O(q^4))]
            sage: ModularFormsRing(2).generators(prec=12)
            [(2, 1 + 24*q + 24*q^2 + 96*q^3 + 24*q^4 + 144*q^5 + 96*q^6 + 192*q^7 + 24*q^8 + 312*q^9 + 144*q^10 + 288*q^11 + O(q^12)),
             (4, 1 + 240*q^2 + 2160*q^4 + 6720*q^6 + 17520*q^8 + 30240*q^10 + O(q^12))]
            sage: ModularFormsRing(4).generators(maxweight=2, prec=20)
            [(2, 1 + 24*q^2 + 24*q^4 + 96*q^6 + 24*q^8 + 144*q^10 + 96*q^12 + 192*q^14 + 24*q^16 + 312*q^18 + O(q^20)),
             (2, q + 4*q^3 + 6*q^5 + 8*q^7 + 13*q^9 + 12*q^11 + 14*q^13 + 24*q^15 + 18*q^17 + 20*q^19 + O(q^20))]

        Here we see that for ``\\Gamma_0(11)`` taking a basis of forms in weights 2
        and 4 is enough to generate everything up to weight 12 (and probably
        everything else).::

            sage: v = ModularFormsRing(11).generators(maxweight=12)
            sage: len(v)
            3
            sage: [k for k, _ in v]
            [2, 2, 4]
            sage: from sage.modular.dims import dimension_modular_forms
            sage: dimension_modular_forms(11,2)
            2
            sage: dimension_modular_forms(11,4)
            4

        For congruence subgroups not containing -1, we miss out some forms since we
        can't calculate weight 1 forms at present, but we can still find generators
        for the ring of forms of weight `\\ge 2`::

            sage: ModularFormsRing(Gamma1(4)).generators(prec=10, maxweight=10)
            [(2, 1 + 24*q^2 + 24*q^4 + 96*q^6 + 24*q^8 + O(q^10)),
             (2, q + 4*q^3 + 6*q^5 + 8*q^7 + 13*q^9 + O(q^10)),
             (3, 1 + 12*q^2 + 64*q^3 + 60*q^4 + 160*q^6 + 384*q^7 + 252*q^8 + O(q^10)),
             (3, q + 4*q^2 + 8*q^3 + 16*q^4 + 26*q^5 + 32*q^6 + 48*q^7 + 64*q^8 + 73*q^9 + O(q^10))]

        Using different base rings will change the generators::

            sage: ModularFormsRing(Gamma0(13)).generators(maxweight=12, prec=4)
            [(2, 1 + 2*q + 6*q^2 + 8*q^3 + O(q^4)),
             (4, 1 + O(q^4)), (4, q + O(q^4)),
             (4, q^2 + O(q^4)), (4, q^3 + O(q^4)),
             (6, 1 + O(q^4)),
             (6, q + O(q^4))]
            sage: ModularFormsRing(Gamma0(13),base_ring=ZZ).generators(maxweight=12, prec=4)
            [(2, 1 + 2*q + 6*q^2 + 8*q^3 + O(q^4)),
             (4, q + 4*q^2 + 10*q^3 + O(q^4)),
             (4, 2*q^2 + 5*q^3 + O(q^4)),
             (4, q^2 + O(q^4)),
             (4, -2*q^3 + O(q^4)),
             (6, O(q^4)),
             (6, O(q^4)),
             (12, O(q^4))]
            sage: [k for k,f in ModularFormsRing(1, QQ).generators(maxweight=12)]
            [4, 6]
            sage: [k for k,f in ModularFormsRing(1, ZZ).generators(maxweight=12)]
            [4, 6, 12]
            sage: [k for k,f in ModularFormsRing(1, Zmod(5)).generators(maxweight=12)]
            [4, 6]
            sage: [k for k,f in ModularFormsRing(1, Zmod(2)).generators(maxweight=12)]
            [4, 6, 12]

        An example where ``start_gens`` are specified::

            sage: M = ModularForms(11, 2); f = (M.0 + M.1).qexp(8)
            sage: ModularFormsRing(11).generators(start_gens = [(2, f)])
            Traceback (most recent call last):
            ...
            ValueError: Requested precision cannot be higher than precision of approximate starting generators!
            sage: f = (M.0 + M.1).qexp(10); f
            1 + 17/5*q + 26/5*q^2 + 43/5*q^3 + 94/5*q^4 + 77/5*q^5 + 154/5*q^6 + 86/5*q^7 + 36*q^8 + 146/5*q^9 + O(q^10)
            sage: ModularFormsRing(11).generators(start_gens = [(2, f)])
            [(2, 1 + 17/5*q + 26/5*q^2 + 43/5*q^3 + 94/5*q^4 + 77/5*q^5 + 154/5*q^6 + 86/5*q^7 + 36*q^8 + 146/5*q^9 + O(q^10)),
             (2, 1 + 12*q^2 + 12*q^3 + 12*q^4 + 12*q^5 + 24*q^6 + 24*q^7 + 36*q^8 + 36*q^9 + O(q^10)),
             (4, 1 + O(q^10))]
        """
    def gen_forms(self, maxweight: int = 8, start_gens=[], start_weight: int = 2):
        """
        Return a list of modular forms generating this ring (as an algebra
        over the appropriate base ring).

        This method differs from :meth:`generators` only in that it returns
        graded modular form objects, rather than bare `q`-expansions.

        INPUT:

        - ``maxweight`` -- integer (default: 8); calculate forms
          generating all forms up to this weight

        - ``start_gens`` -- list (default: ``[]``); a list of
          modular forms. If this list is nonempty, we find a minimal
          generating set containing these forms.

        - ``start_weight`` -- integer (default: 2); calculate the graded
          subalgebra of forms of weight at least ``start_weight``

        .. NOTE::

            If called with the default values of ``start_gens`` (an empty list)
            and ``start_weight`` (2), the values will be cached for re-use on
            subsequent calls to this function. (This cache is shared with
            :meth:`generators`). If called with non-default values for these
            parameters, caching will be disabled.

        EXAMPLES::

            sage: A = ModularFormsRing(Gamma0(11), Zmod(5)).gen_forms(); A
            [1 + 12*q^2 + 12*q^3 + 12*q^4 + 12*q^5 + O(q^6),
             q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
             q - 9*q^4 - 10*q^5 + O(q^6)]
            sage: A[0].parent()
            Modular Forms space of dimension 2 for Congruence Subgroup Gamma0(11) of weight 2 over Rational Field
        """
    gens = gen_forms
    @cached_method
    def q_expansion_basis(self, weight, prec=None, use_random: bool = True):
        """
        Return a basis of `q`-expansions for the space of modular forms
        of the given weight for this group, calculated using the ring
        generators given by ``find_generators``.

        INPUT:

        - ``weight`` -- the weight
        - ``prec`` -- integer (default: ``None``); power series
          precision. If ``None``, the precision defaults to the Sturm
          bound for the requested level and weight.
        - ``use_random`` -- boolean (default: ``True``); whether or not to
          use a randomized algorithm when building up the space of forms
          at the given weight from known generators of small weight.

        EXAMPLES::

            sage: m = ModularFormsRing(Gamma0(4))
            sage: m.q_expansion_basis(2,10)
            [1 + 24*q^2 + 24*q^4 + 96*q^6 + 24*q^8 + O(q^10),
             q + 4*q^3 + 6*q^5 + 8*q^7 + 13*q^9 + O(q^10)]
            sage: m.q_expansion_basis(3,10)
            []

            sage: X = ModularFormsRing(SL2Z)
            sage: X.q_expansion_basis(12, 10)
            [1 + 196560*q^2 + 16773120*q^3 + 398034000*q^4 + 4629381120*q^5 + 34417656000*q^6 + 187489935360*q^7 + 814879774800*q^8 + 2975551488000*q^9 + O(q^10),
             q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 - 16744*q^7 + 84480*q^8 - 113643*q^9 + O(q^10)]

        We calculate a basis of a massive modular forms space, in two ways.
        Using this module is about twice as fast as Sage's generic code. ::

            sage: A = ModularFormsRing(11).q_expansion_basis(30, prec=40) # long time (5s)
            sage: B = ModularForms(Gamma0(11), 30).q_echelon_basis(prec=40) # long time (9s)
            sage: A == B # long time
            True

        Check that absurdly small values of ``prec`` don't mess things up::

            sage: ModularFormsRing(11).q_expansion_basis(10, prec=5)
            [1 + O(q^5), q + O(q^5), q^2 + O(q^5), q^3 + O(q^5),
             q^4 + O(q^5), O(q^5), O(q^5), O(q^5), O(q^5), O(q^5)]
        """
    def cuspidal_ideal_generators(self, maxweight: int = 8, prec=None):
        """
        Return a set of generators for the ideal of cuspidal forms in
        this ring, as a module over the whole ring.

        EXAMPLES::

            sage: ModularFormsRing(Gamma0(3)).cuspidal_ideal_generators(maxweight=12)
            [(6, q - 6*q^2 + 9*q^3 + 4*q^4 + O(q^5), q - 6*q^2 + 9*q^3 + 4*q^4 + 6*q^5 + O(q^6))]
            sage: [k for k,f,F in ModularFormsRing(13, base_ring=ZZ).cuspidal_ideal_generators(maxweight=14)]
            [4, 4, 4, 6, 6, 12]
        """
    def cuspidal_submodule_q_expansion_basis(self, weight, prec=None):
        """
        Return a basis of `q`-expansions for the space of cusp forms of
        weight ``weight`` for this group.

        INPUT:

        - ``weight`` -- the weight
        - ``prec`` -- integer (default: ``None``) precision of
          `q`-expansions to return

        ALGORITHM: Uses the method :meth:`cuspidal_ideal_generators` to
        calculate generators of the ideal of cusp forms inside this ring. Then
        multiply these up to weight ``weight`` using the generators of the
        whole modular form space returned by :meth:`q_expansion_basis`.

        EXAMPLES::

            sage: R = ModularFormsRing(Gamma0(3))
            sage: R.cuspidal_submodule_q_expansion_basis(20)
            [q - 8532*q^6 - 88442*q^7 + O(q^8), q^2 + 207*q^6 + 24516*q^7 + O(q^8),
             q^3 + 456*q^6 + O(q^8), q^4 - 135*q^6 - 926*q^7 + O(q^8), q^5 + 18*q^6 + 135*q^7 + O(q^8)]

        We compute a basis of a space of very large weight, quickly (using this
        module) and slowly (using modular symbols), and verify that the answers
        are the same. ::

            sage: A = R.cuspidal_submodule_q_expansion_basis(80, prec=30)  # long time (1s on sage.math, 2013)
            sage: B = R.modular_forms_of_weight(80).cuspidal_submodule().q_expansion_basis(prec=30)  # long time (19s on sage.math, 2013)
            sage: A == B # long time
            True
        """

find_generators: Incomplete
basis_for_modform_space: Incomplete
