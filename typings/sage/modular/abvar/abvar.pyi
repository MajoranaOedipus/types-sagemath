from .cuspidal_subgroup import CuspidalSubgroup as CuspidalSubgroup, RationalCuspSubgroup as RationalCuspSubgroup, RationalCuspidalSubgroup as RationalCuspidalSubgroup
from .finite_subgroup import FiniteSubgroup as FiniteSubgroup, FiniteSubgroup_lattice as FiniteSubgroup_lattice, TorsionPoint as TorsionPoint
from .morphism import DegeneracyMap as DegeneracyMap, HeckeOperator as HeckeOperator, Morphism as Morphism
from .torsion_subgroup import QQbarTorsionSubgroup as QQbarTorsionSubgroup, RationalTorsionSubgroup as RationalTorsionSubgroup
from sage.arith.misc import divisors as divisors, is_prime as is_prime, next_prime as next_prime
from sage.categories.fields import Fields as Fields
from sage.categories.modular_abelian_varieties import ModularAbelianVarieties as ModularAbelianVarieties
from sage.matrix.constructor import matrix as matrix
from sage.matrix.special import block_diagonal_matrix as block_diagonal_matrix, identity_matrix as identity_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modular.abvar import homspace as homspace, lseries as lseries
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_class as Gamma1_class
from sage.modular.arithgroup.congroup_gammaH import GammaH_class as GammaH_class
from sage.modular.arithgroup.congroup_generic import CongruenceSubgroupBase as CongruenceSubgroupBase
from sage.modular.modform.constructor import Newform as Newform
from sage.modular.modsym.modsym import ModularSymbols as ModularSymbols
from sage.modular.modsym.space import ModularSymbolsSpace as ModularSymbolsSpace
from sage.modular.quatalg.brandt import BrandtModule as BrandtModule
from sage.modules.free_module import FreeModule_generic as FreeModule_generic
from sage.modules.free_module_element import vector as vector
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.sets.primes import Primes as Primes
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence, Sequence_generic as Sequence_generic

def is_ModularAbelianVariety(x) -> bool:
    """
    Return ``True`` if x is a modular abelian variety.

    INPUT:

    - ``x`` -- object

    EXAMPLES::

        sage: from sage.modular.abvar.abvar import is_ModularAbelianVariety
        sage: is_ModularAbelianVariety(5)
        doctest:warning...
        DeprecationWarning: The function is_ModularAbelianVariety is deprecated; use 'isinstance(..., ModularAbelianVariety_abstract)' instead.
        See https://github.com/sagemath/sage/issues/38035 for details.
        False
        sage: is_ModularAbelianVariety(J0(37))
        True

    Returning ``True`` is a statement about the data type not whether or
    not some abelian variety is modular::

        sage: is_ModularAbelianVariety(EllipticCurve('37a'))
        False
    """

class ModularAbelianVariety_abstract(Parent):
    def __init__(self, groups, base_field, is_simple=None, newform_level=None, isogeny_number=None, number=None, check: bool = True) -> None:
        """
        Abstract base class for modular abelian varieties.

        INPUT:

        - ``groups`` -- tuple of congruence subgroups

        - ``base_field`` -- a field

        - ``is_simple`` -- boolean; whether or not ``self`` is simple

        - ``newform_level`` -- if ``self`` is isogenous to a
          newform abelian variety, returns the level of that abelian variety

        - ``isogeny_number`` -- which isogeny class the corresponding newform
          is in; this corresponds to the Cremona letter code

        - ``number`` -- the t number of the degeneracy map that
          this abelian variety is the image under

        - ``check`` -- whether to do some type checking on the
          defining data

        EXAMPLES: One should not create an instance of this class, but we
        do so anyways here as an example::

            sage: A = sage.modular.abvar.abvar.ModularAbelianVariety_abstract((Gamma0(37),), QQ)
            sage: type(A)
            <class 'sage.modular.abvar.abvar.ModularAbelianVariety_abstract_with_category'>


        All hell breaks loose if you try to do anything with `A`::

            sage: A
            <repr(<sage.modular.abvar.abvar.ModularAbelianVariety_abstract_with_category at 0x...>) failed: NotImplementedError: BUG -- lattice method must be defined in derived class>


        All instances of this class are in the category of modular
        abelian varieties::

            sage: A.category()
            Category of modular abelian varieties over Rational Field
            sage: J0(23).category()
            Category of modular abelian varieties over Rational Field
        """
    def groups(self):
        """
        Return an ordered tuple of the congruence subgroups that the
        ambient product Jacobian is attached to.

        Every modular abelian variety is a finite quotient of an abelian
        subvariety of a product of modular Jacobians `J_\\Gamma`.
        This function returns a tuple containing the groups
        `\\Gamma`.

        EXAMPLES::

            sage: A = (J0(37) * J1(13))[0]; A
            Simple abelian subvariety 13aG1(1,13) of dimension 2 of J0(37) x J1(13)
            sage: A.groups()
            (Congruence Subgroup Gamma0(37), Congruence Subgroup Gamma1(13))
        """
    def is_J0(self) -> bool:
        """
        Return whether or not ``self`` is of the form J0(N).

        OUTPUT: boolean

        EXAMPLES::

            sage: J0(23).is_J0()
            True
            sage: J1(11).is_J0()
            False
            sage: (J0(23) * J1(11)).is_J0()
            False
            sage: J0(37)[0].is_J0()
            False
            sage: (J0(23) * J0(21)).is_J0()
            False
        """
    def is_J1(self) -> bool:
        """
        Return whether or not ``self`` is of the form J1(N).

        OUTPUT: boolean

        EXAMPLES::

            sage: J1(23).is_J1()
            True
            sage: J0(23).is_J1()
            False
            sage: (J1(11) * J1(13)).is_J1()
            False
            sage: (J1(11) * J0(13)).is_J1()
            False
            sage: J1(23)[0].is_J1()
            False
        """
    def lattice(self) -> None:
        """
        Return lattice in ambient cuspidal modular symbols product that
        defines this modular abelian variety.

        This must be defined in each derived class.

        OUTPUT: a free module over `\\ZZ`

        EXAMPLES::

            sage: A = sage.modular.abvar.abvar.ModularAbelianVariety_abstract((Gamma0(37),), QQ)
            sage: A
            <repr(<sage.modular.abvar.abvar.ModularAbelianVariety_abstract_with_category at 0x...>) failed: NotImplementedError: BUG -- lattice method must be defined in derived class>
        """
    def free_module(self):
        """
        Synonym for ``self.lattice()``.

        OUTPUT: a free module over `\\ZZ`

        EXAMPLES::

            sage: J0(37).free_module()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: J0(37)[0].free_module()
            Free module of degree 4 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1 -1  1  0]
            [ 0  0  2 -1]
        """
    def vector_space(self):
        """
        Return vector space corresponding to the modular abelian variety.

        This is the lattice tensored with `\\QQ`.

        EXAMPLES::

            sage: J0(37).vector_space()
            Vector space of dimension 4 over Rational Field
            sage: J0(37)[0].vector_space()
            Vector space of degree 4 and dimension 2 over Rational Field
            Basis matrix:
            [   1   -1    0  1/2]
            [   0    0    1 -1/2]
        """
    def base_field(self):
        """
        Synonym for ``self.base_ring()``.

        EXAMPLES::

            sage: J0(11).base_field()
            Rational Field
        """
    def base_extend(self, K):
        """
        EXAMPLES::

            sage: A = J0(37); A
            Abelian variety J0(37) of dimension 2
            sage: A.base_extend(QQbar)                                                  # needs sage.rings.number_field
            Abelian variety J0(37) over Algebraic Field of dimension 2
            sage: A.base_extend(GF(7))
            Abelian variety J0(37) over Finite Field of size 7 of dimension 2
        """
    def __contains__(self, x) -> bool:
        """
        Determine whether or not ``self`` contains x.

        EXAMPLES::

            sage: J = J0(67); G = (J[0] + J[1]).intersection(J[1] + J[2])
            sage: G[0]
            Finite subgroup with invariants [5, 10] over QQbar of Abelian subvariety of dimension 3 of J0(67)
            sage: a = G[0].0; a
            [(1/10, 1/10, 3/10, 1/2, 1, -2, -3, 33/10, 0, -1/2)]
            sage: a in J[0]
            False
            sage: a in (J[0]+J[1])
            True
            sage: a in (J[1]+J[2])
            True
            sage: C = G[1]   # abelian variety in kernel
            sage: G[0].0
            [(1/10, 1/10, 3/10, 1/2, 1, -2, -3, 33/10, 0, -1/2)]
            sage: 5*G[0].0
            [(1/2, 1/2, 3/2, 5/2, 5, -10, -15, 33/2, 0, -5/2)]
            sage: 5*G[0].0 in C
            True
        """
    def __richcmp__(self, other, op):
        """
        Compare two modular abelian varieties.

        If ``other`` is not a modular abelian variety, compares the types of
        ``self`` and ``other``. If ``other`` is a modular abelian variety,
        compares the groups, then if those are the same, compares the newform
        level and isogeny class number and degeneracy map numbers. If those are
        not defined or matched up, compare the underlying lattices.

        EXAMPLES::

            sage: J0(37)[0] < J0(37)[1]
            True
            sage: J0(37)[0] == J0(37)[1]
            False
            sage: J0(33)[0] < J0(33)[1]
            True
            sage: J0(33)[0] >= J0(33)[1]
            False
        """
    def __radd__(self, other):
        """
        Return ``other`` + ``self`` when ``other`` is 0. Otherwise raise a
        :exc:`TypeError`.

        EXAMPLES::

            sage: int(0) + J0(37)
            Abelian variety J0(37) of dimension 2
        """
    def label(self) -> str:
        """
        Return the label associated to this modular abelian variety.

        The format of the label is [level][isogeny class][group](t, ambient
        level)

        If this abelian variety `B` has the above label, this
        implies only that `B` is isogenous to the newform abelian
        variety `A_f` associated to the newform with label
        [level][isogeny class][group]. The [group] is empty for
        `\\Gamma_0(N)`, is G1 for `\\Gamma_1(N)` and is
        GH[...] for `\\Gamma_H(N)`.

        .. warning::

           The sum of `\\delta_s(A_f)` for all `s\\mid t`
           contains `A`, but no sum for a proper divisor of
           `t` contains `A`. It need *not* be the case
           that `B` is equal to `\\delta_t(A_f)`!!!

        OUTPUT: string

        EXAMPLES::

            sage: J0(11).label()
            '11a(1,11)'
            sage: J0(11)[0].label()
            '11a(1,11)'
            sage: J0(33)[2].label()
            '33a(1,33)'
            sage: J0(22).label()
            Traceback (most recent call last):
            ...
            ValueError: self must be simple

        We illustrate that ``self`` need not equal `\\delta_t(A_f)`::

            sage: J = J0(11); phi = J.degeneracy_map(33, 1) + J.degeneracy_map(33,3)
            sage: B = phi.image(); B
            Abelian subvariety of dimension 1 of J0(33)
            sage: B.decomposition()
            [Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33)]
            sage: C = J.degeneracy_map(33,3).image(); C
            Abelian subvariety of dimension 1 of J0(33)
            sage: C == B
            False
        """
    def newform(self, names=None):
        """
        Return the newform `f` such that this abelian variety is isogenous to
        the newform abelian variety `A_f`.

        If this abelian variety is not
        simple, this raises a :exc:`ValueError`.

        INPUT:

        - ``names`` -- (default: ``None``) if the newform has coefficients
          in a number field, then a generator name must be specified

        OUTPUT: a newform `f` so that ``self`` is isogenous to `A_f`

        EXAMPLES::

            sage: J0(11).newform()
            q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)

            sage: f = J0(23).newform(names='a')
            sage: AbelianVariety(f) == J0(23)
            True

            sage: J = J0(33)
            sage: [s.newform('a') for s in J.decomposition()]
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
             q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
             q + q^2 - q^3 - q^4 - 2*q^5 + O(q^6)]

        The following fails since `J_0(33)` is not simple::

            sage: J0(33).newform()
            Traceback (most recent call last):
            ...
            ValueError: self must be simple
        """
    def newform_decomposition(self, names=None):
        """
        Return the newforms of the simple subvarieties in the decomposition of
        ``self`` as a product of simple subvarieties, up to isogeny.

        OUTPUT: an array of newforms

        EXAMPLES::

            sage: J = J1(11) * J0(23)
            sage: J.newform_decomposition('a')
            [q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6),
            q + a0*q^2 + (-2*a0 - 1)*q^3 + (-a0 - 1)*q^4 + 2*a0*q^5 + O(q^6)]
        """
    def newform_label(self):
        """
        Return the label [level][isogeny class][group] of the newform
        `f` such that this abelian variety is isogenous to the newform
        abelian variety `A_f`.

        If this abelian variety is not simple, this raises
        a :exc:`ValueError`.

        OUTPUT: string

        EXAMPLES::

            sage: J0(11).newform_label()
            '11a'
            sage: J0(33)[2].newform_label()
            '33a'

        The following fails since `J_0(33)` is not simple::

            sage: J0(33).newform_label()
            Traceback (most recent call last):
            ...
            ValueError: self must be simple
        """
    def elliptic_curve(self):
        """
        Return an elliptic curve isogenous to ``self``.

        If ``self`` is not dimension 1
        with rational base ring, this raises a :exc:`ValueError`.

        The elliptic curve is found by looking it up in the
        CremonaDatabase.  The CremonaDatabase contains all curves up
        to some large conductor.  If a curve is not found in the
        CremonaDatabase, a :exc:`RuntimeError` will be raised. In
        practice, only the most committed users will see this
        :exc:`RuntimeError`.

        OUTPUT: an elliptic curve isogenous to ``self``

        EXAMPLES::

            sage: J = J0(11)
            sage: J.elliptic_curve()
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field

            sage: J = J0(49)
            sage: J.elliptic_curve()
            Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 2*x - 1 over Rational Field

            sage: A = J0(37)[1]
            sage: E = A.elliptic_curve()
            sage: A.lseries()(1)
            0.725681061936153
            sage: E.lseries()(1)
            0.725681061936153

        Elliptic curves are of dimension 1. ::

            sage: J = J0(23)
            sage: J.elliptic_curve()
            Traceback (most recent call last):
            ...
            ValueError: self must be of dimension 1

        This is only implemented for curves over QQ. ::

            sage: J = J0(11).change_ring(CC)
            sage: J.elliptic_curve()
            Traceback (most recent call last):
            ...
            ValueError: base ring must be QQ
        """
    def in_same_ambient_variety(self, other):
        """
        Return ``True`` if ``self`` and ``other`` are abelian subvarieties of
        the same ambient product Jacobian.

        EXAMPLES::

            sage: A,B,C = J0(33)
            sage: A.in_same_ambient_variety(B)
            True
            sage: A.in_same_ambient_variety(J0(11))
            False
        """
    def modular_kernel(self):
        """
        Return the modular kernel of this abelian variety, which is the
        kernel of the canonical polarization of ``self``.

        EXAMPLES::

            sage: A = AbelianVariety('33a'); A
            Newform abelian subvariety 33a of dimension 1 of J0(33)
            sage: A.modular_kernel()
            Finite subgroup with invariants [3, 3] over QQ of Newform abelian subvariety 33a of dimension 1 of J0(33)
        """
    def modular_degree(self):
        """
        Return the modular degree of this abelian variety, which is the
        square root of the degree of the modular kernel.

        EXAMPLES::

            sage: A = AbelianVariety('37a')
            sage: A.modular_degree()
            2
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` and ``other`` inside a common
        ambient Jacobian product.

        When ``other`` is a modular abelian variety, the output will be a tuple
        ``(G, A)``, where ``G`` is a finite subgroup that surjects onto the
        component group and ``A`` is the identity component. So in particular,
        the intersection is the variety ``G+A``. Note that ``G`` is not chosen
        in any canonical way. When ``other`` is a finite group, the
        intersection will be returned as a finite group.

        INPUT:

        - ``other`` -- a modular abelian variety or a finite
          group

        OUTPUT: if other is a modular abelian variety:


        - ``G`` -- finite subgroup of self

        - ``A`` -- abelian variety (identity component of
          intersection)

        If other is a finite group:

        - ``G`` -- a finite group

        EXAMPLES: We intersect some abelian varieties with finite
        intersection.

        ::

            sage: J = J0(37)
            sage: J[0].intersection(J[1])
            (Finite subgroup with invariants [2, 2] over QQ of Simple abelian
             subvariety 37a(1,37) of dimension 1 of J0(37), Simple abelian
             subvariety of dimension 0 of J0(37))

        ::

            sage: D = list(J0(65)); D
            [Simple abelian subvariety 65a(1,65) of dimension 1 of J0(65),
             Simple abelian subvariety 65b(1,65) of dimension 2 of J0(65),
             Simple abelian subvariety 65c(1,65) of dimension 2 of J0(65)]
            sage: D[0].intersection(D[1])
            (Finite subgroup with invariants [2] over QQ of Simple abelian
             subvariety 65a(1,65) of dimension 1 of J0(65), Simple abelian
             subvariety of dimension 0 of J0(65))
            sage: (D[0]+D[1]).intersection(D[1]+D[2])
            (Finite subgroup with invariants [2] over QQbar of Abelian
             subvariety of dimension 3 of J0(65), Abelian subvariety of
             dimension 2 of J0(65))

        ::

            sage: J = J0(33)
            sage: J[0].intersection(J[1])
            (Finite subgroup with invariants [5] over QQ of Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33), Simple abelian subvariety of dimension 0 of J0(33))

        Next we intersect two abelian varieties with non-finite
        intersection::

            sage: J = J0(67); D = J.decomposition(); D
            [Simple abelian subvariety 67a(1,67) of dimension 1 of J0(67),
             Simple abelian subvariety 67b(1,67) of dimension 2 of J0(67),
             Simple abelian subvariety 67c(1,67) of dimension 2 of J0(67)]
            sage: (D[0] + D[1]).intersection(D[1] + D[2])
            (Finite subgroup with invariants [5, 10] over QQbar of Abelian subvariety of dimension 3 of J0(67), Abelian subvariety of dimension 2 of J0(67))

        When the intersection is infinite, the output is ``(G, A)``, where
        ``G`` surjects onto the component group. This choice of ``G`` is not
        canonical (see :issue:`26189`). In this following example, ``B`` is a
        subvariety of ``J``::

            sage: d1 = J0(11).degeneracy_map(22, 1)
            sage: d2 = J0(11).degeneracy_map(22, 2)
            sage: B = (d1-d2).image()
            sage: J = J0(22)
            sage: J.intersection(B)
            (Finite subgroup with invariants [] over QQbar of Abelian variety J0(22) of dimension 2,
             Abelian subvariety of dimension 1 of J0(22))
            sage: G, B = B.intersection(J); G, B
            (Finite subgroup with invariants [2] over QQbar of Abelian subvariety of dimension 1 of J0(22),
             Abelian subvariety of dimension 1 of J0(22))
            sage: G.is_subgroup(B)
            True
        """
    def __add__(self, other):
        """
        Return the sum of the *images* of ``self`` and ``other`` inside the
        ambient Jacobian product.

        Here ``self`` and ``other`` must be abelian
        subvarieties of the ambient Jacobian product.

        .. WARNING::

            The sum of course only makes sense in some ambient variety,
            and by definition this function takes the sum of the images
            of both ``self`` and ``other`` in the ambient product Jacobian.

        EXAMPLES:

        We compute the sum of two abelian varieties of `J_0(33)`::

            sage: J = J0(33)
            sage: J[0] + J[1]
            Abelian subvariety of dimension 2 of J0(33)

        We sum all three and get the full `J_0(33)`::

            sage: (J[0] + J[1]) + (J[1] + J[2])
            Abelian variety J0(33) of dimension 3

        Adding to zero works::

            sage: J[0] + 0
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)

        Hence the sum command works::

            sage: sum([J[0], J[2]])
            Abelian subvariety of dimension 2 of J0(33)

        We try to add something in `J_0(33)` to something in
        `J_0(11)`; this shouldn't and doesn't work.

        ::

            sage: J[0] + J0(11)
            Traceback (most recent call last):
            ...
            TypeError: sum not defined since ambient spaces different

        We compute the diagonal image of `J_0(11)` in
        `J_0(33)`, then add the result to the new elliptic curve
        of level `33`.

        ::

            sage: A = J0(11)
            sage: B = (A.degeneracy_map(33,1) + A.degeneracy_map(33,3)).image()
            sage: B + J0(33)[2]
            Abelian subvariety of dimension 2 of J0(33)

        TESTS:

        This exposed a bug in HNF (see :issue:`4527`)::

            sage: A = J0(206).new_subvariety().decomposition()[3] ; A # long time
            Simple abelian subvariety 206d(1,206) of dimension 4 of J0(206)
            sage: B = J0(206).old_subvariety(2) ; B # long time
            Abelian subvariety of dimension 16 of J0(206)
            sage: A+B # long time
            Abelian subvariety of dimension 20 of J0(206)
        """
    def direct_product(self, other):
        """
        Compute the direct product of ``self`` and ``other``.

        INPUT:

        - ``self``, ``other`` -- modular abelian varieties

        OUTPUT: abelian variety

        EXAMPLES::

            sage: J0(11).direct_product(J1(13))
            Abelian variety J0(11) x J1(13) of dimension 3
            sage: A = J0(33)[0].direct_product(J0(33)[1]); A
            Abelian subvariety of dimension 2 of J0(33) x J0(33)
            sage: A.lattice()
            Free module of degree 12 and rank 4 over Integer Ring
            Echelon basis matrix:
            [ 1  1 -2  0  2 -1  0  0  0  0  0  0]
            [ 0  3 -2 -1  2  0  0  0  0  0  0  0]
            [ 0  0  0  0  0  0  1  0  0  0 -1  2]
            [ 0  0  0  0  0  0  0  1 -1  1  0 -2]
        """
    def __pow__(self, n):
        """
        Return `n`-th power of ``self``.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: an abelian variety

        EXAMPLES::

            sage: J = J0(37)
            sage: J^0
            Simple abelian subvariety of dimension 0 of J0(37)
            sage: J^1
            Abelian variety J0(37) of dimension 2
            sage: J^1 is J
            True
        """
    def __mul__(self, other):
        """
        Compute the direct product of ``self`` and ``other``.

        EXAMPLES: Some modular Jacobians::

            sage: J0(11) * J0(33)
            Abelian variety J0(11) x J0(33) of dimension 4
            sage: J0(11) * J0(33) * J0(11)
            Abelian variety J0(11) x J0(33) x J0(11) of dimension 5

        We multiply some factors of `J_0(65)`::

            sage: d = J0(65).decomposition()
            sage: d[0] * d[1] * J0(11)
            Abelian subvariety of dimension 4 of J0(65) x J0(65) x J0(11)
        """
    def quotient(self, other, **kwds):
        """
        Compute the quotient of ``self`` and ``other``, where other is either an
        abelian subvariety of ``self`` or a finite subgroup of ``self``.

        INPUT:

        - ``other`` -- a finite subgroup or subvariety
        - further named arguments, that are currently ignored

        OUTPUT: a pair (A, phi) with phi the quotient map from ``self`` to A

        EXAMPLES: We quotient `J_0(33)` out by an abelian
        subvariety::

            sage: Q, f = J0(33).quotient(J0(33)[0])
            sage: Q
            Abelian variety factor of dimension 2 of J0(33)
            sage: f
            Abelian variety morphism:
              From: Abelian variety J0(33) of dimension 3
              To:   Abelian variety factor of dimension 2 of J0(33)

        We quotient `J_0(33)` by the cuspidal subgroup::

            sage: C = J0(33).cuspidal_subgroup()
            sage: Q, f = J0(33).quotient(C)
            sage: Q
            Abelian variety factor of dimension 3 of J0(33)
            sage: f.kernel()[0]
            Finite subgroup with invariants [10, 10] over QQ of Abelian variety J0(33) of dimension 3
            sage: C
            Finite subgroup with invariants [10, 10] over QQ of Abelian variety J0(33) of dimension 3
            sage: J0(11).direct_product(J1(13))
            Abelian variety J0(11) x J1(13) of dimension 3
        """
    def __truediv__(self, other):
        """
        Compute the quotient of ``self`` and ``other``, where other is either
        an abelian subvariety of ``self`` or a finite subgroup of ``self``.

        INPUT:

        - ``other`` -- a finite subgroup or subvariety

        EXAMPLES: Quotient out by a finite group::

            sage: J = J0(67); G = (J[0] + J[1]).intersection(J[1] + J[2])
            sage: Q, _ = J/G[0]; Q
            Abelian variety factor of dimension 5 of J0(67) over Algebraic Field
            sage: Q.base_field()
            Algebraic Field
            sage: Q.lattice()
            Free module of degree 10 and rank 10 over Integer Ring
            Echelon basis matrix:
            [1/10 1/10 3/10  1/2    0    0    0 3/10    0  1/2]
            [   0  1/5  4/5  4/5    0    0    0    0    0  3/5]
            ...

        Quotient out by an abelian subvariety::

            sage: A, B, C = J0(33)
            sage: Q, phi = J0(33)/A
            sage: Q
            Abelian variety factor of dimension 2 of J0(33)
            sage: phi.domain()
            Abelian variety J0(33) of dimension 3
            sage: phi.codomain()
            Abelian variety factor of dimension 2 of J0(33)
            sage: phi.kernel()
            (Finite subgroup with invariants [2] over QQbar of Abelian variety J0(33) of dimension 3,
             Abelian subvariety of dimension 1 of J0(33))
            sage: phi.kernel()[1] == A
            True

        The abelian variety we quotient out by must be an abelian
        subvariety.

        ::

            sage: Q = (A + B)/C; Q
            Traceback (most recent call last):
            ...
            TypeError: other must be a subgroup or abelian subvariety
        """
    def degeneracy_map(self, M_ls, t_ls):
        """
        Return the degeneracy map with domain ``self`` and given
        level/parameter. If ``self.ambient_variety()`` is a product of
        Jacobians (as opposed to a single Jacobian), then one can provide a
        list of new levels and parameters, corresponding to the ambient
        Jacobians in order. (See the examples below.)

        INPUT:

        - ``M``, ``t`` -- integers level and `t`, or

        - ``Mlist, tlist`` -- if ``self`` is in a nontrivial
          product ambient Jacobian, input consists of a list of levels and
          corresponding list of `t`'s.

        OUTPUT: a degeneracy map

        EXAMPLES: We make several degeneracy maps related to
        `J_0(11)` and `J_0(33)` and compute their
        matrices.

        ::

            sage: d1 = J0(11).degeneracy_map(33, 1); d1
            Degeneracy map from Abelian variety J0(11) of dimension 1 to Abelian variety J0(33) of dimension 3 defined by [1]
            sage: d1.matrix()
            [ 0 -3  2  1 -2  0]
            [ 1 -2  0  1  0 -1]
            sage: d2 = J0(11).degeneracy_map(33, 3); d2
            Degeneracy map from Abelian variety J0(11) of dimension 1 to Abelian variety J0(33) of dimension 3 defined by [3]
            sage: d2.matrix()
            [-1  0  0  0  1 -2]
            [-1 -1  1 -1  1  0]
            sage: d3 = J0(33).degeneracy_map(11, 1); d3
            Degeneracy map from Abelian variety J0(33) of dimension 3 to Abelian variety J0(11) of dimension 1 defined by [1]

        He we verify that first mapping from level `11` to level
        `33`, then back is multiplication by `4`::

            sage: d1.matrix() * d3.matrix()
            [4 0]
            [0 4]

        We compute a more complicated degeneracy map involving nontrivial
        product ambient Jacobians; note that this is just the block direct
        sum of the two matrices at the beginning of this example::

            sage: d = (J0(11)*J0(11)).degeneracy_map([33,33], [1,3]); d
            Degeneracy map from Abelian variety J0(11) x J0(11) of dimension 2 to Abelian variety J0(33) x J0(33) of dimension 6 defined by [1, 3]
            sage: d.matrix()
            [ 0 -3  2  1 -2  0  0  0  0  0  0  0]
            [ 1 -2  0  1  0 -1  0  0  0  0  0  0]
            [ 0  0  0  0  0  0 -1  0  0  0  1 -2]
            [ 0  0  0  0  0  0 -1 -1  1 -1  1  0]
        """
    def projection(self, A, check: bool = True):
        """
        Given an abelian subvariety A of self, return a projection morphism
        from ``self`` to A. Note that this morphism need not be unique.

        INPUT:

        - ``A`` -- an abelian variety

        OUTPUT: a morphism

        EXAMPLES::

            sage: a,b,c = J0(33)
            sage: pi = J0(33).projection(a); pi.matrix()
            [ 3 -2]
            [-5  5]
            [-4  1]
            [ 3 -2]
            [ 5  0]
            [ 1  1]
            sage: pi = (a+b).projection(a); pi.matrix()
            [ 0  0]
            [-3  2]
            [-4  1]
            [-1 -1]
            sage: pi = a.projection(a); pi.matrix()
            [1 0]
            [0 1]

        We project onto a factor in a product of two Jacobians::

            sage: A = J0(11)*J0(11); A
            Abelian variety J0(11) x J0(11) of dimension 2
            sage: A[0]
            Simple abelian subvariety 11a(1,11) of dimension 1 of J0(11) x J0(11)
            sage: A.projection(A[0])
            Abelian variety morphism:
              From: Abelian variety J0(11) x J0(11) of dimension 2
              To:   Simple abelian subvariety 11a(1,11) of dimension 1 of J0(11) x J0(11)
            sage: A.projection(A[0]).matrix()
            [0 0]
            [0 0]
            [1 0]
            [0 1]
            sage: A.projection(A[1]).matrix()
            [1 0]
            [0 1]
            [0 0]
            [0 0]
        """
    def project_to_factor(self, n):
        """
        If ``self`` is an ambient product of Jacobians, return a projection
        from ``self`` to the `n`-th such Jacobian.

        EXAMPLES::

            sage: J = J0(33)
            sage: J.project_to_factor(0)
            Abelian variety endomorphism of Abelian variety J0(33) of dimension 3

        ::

            sage: J = J0(33) * J0(37) * J0(11)
            sage: J.project_to_factor(2)
            Abelian variety morphism:
              From: Abelian variety J0(33) x J0(37) x J0(11) of dimension 6
              To:   Abelian variety J0(11) of dimension 1
            sage: J.project_to_factor(2).matrix()
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [0 0]
            [1 0]
            [0 1]
        """
    def is_subvariety_of_ambient_jacobian(self) -> bool:
        """
        Return ``True`` if ``self`` is (presented as) a subvariety of the ambient
        product Jacobian.

        Every abelian variety in Sage is a quotient of a subvariety of an
        ambient Jacobian product by a finite subgroup.

        EXAMPLES::

            sage: J0(33).is_subvariety_of_ambient_jacobian()
            True
            sage: A = J0(33)[0]; A
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: A.is_subvariety_of_ambient_jacobian()
            True
            sage: B, phi = A / A.torsion_subgroup(2)
            sage: B
            Abelian variety factor of dimension 1 of J0(33)
            sage: phi.matrix()
            [2 0]
            [0 2]
            sage: B.is_subvariety_of_ambient_jacobian()
            False
        """
    def ambient_variety(self):
        """
        Return the ambient modular abelian variety that contains this
        abelian variety. The ambient variety is always a product of
        Jacobians of modular curves.

        OUTPUT: abelian variety

        EXAMPLES::

            sage: A = J0(33)[0]; A
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: A.ambient_variety()
            Abelian variety J0(33) of dimension 3
        """
    def ambient_morphism(self):
        """
        Return the morphism from ``self`` to the ambient variety. This is
        injective if ``self`` is natural a subvariety of the ambient product
        Jacobian.

        OUTPUT: morphism

        The output is cached.

        EXAMPLES: We compute the ambient structure morphism for an abelian
        subvariety of `J_0(33)`::

            sage: A,B,C = J0(33)
            sage: phi = A.ambient_morphism()
            sage: phi.domain()
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: phi.codomain()
            Abelian variety J0(33) of dimension 3
            sage: phi.matrix()
            [ 1  1 -2  0  2 -1]
            [ 0  3 -2 -1  2  0]

        ``phi`` is of course injective::

            sage: phi.kernel()
            (Finite subgroup with invariants [] over QQ of Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33),
             Abelian subvariety of dimension 0 of J0(33))

        This is the same as the basis matrix for the lattice corresponding
        to self::

            sage: A.lattice()
            Free module of degree 6 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 1  1 -2  0  2 -1]
            [ 0  3 -2 -1  2  0]

        We compute a non-injective map to an ambient space::

            sage: Q,pi = J0(33)/A
            sage: phi = Q.ambient_morphism()
            sage: phi.matrix()
            [  1   4   1   9  -1  -1]
            [  0  15   0   0  30 -75]
            [  0   0   5  10  -5  15]
            [  0   0   0  15 -15  30]
            sage: phi.kernel()[0]
            Finite subgroup with invariants [5, 15, 15] over QQ of Abelian
             variety factor of dimension 2 of J0(33)
        """
    @cached_method
    def is_ambient(self) -> bool:
        """
        Return ``True`` if ``self`` equals the ambient product Jacobian.

        OUTPUT: boolean

        EXAMPLES::

            sage: A,B,C = J0(33)
            sage: A.is_ambient()
            False
            sage: J0(33).is_ambient()
            True
            sage: (A+B).is_ambient()
            False
            sage: (A+B+C).is_ambient()
            True
        """
    def dimension(self):
        """
        Return the dimension of this abelian variety.

        EXAMPLES::

            sage: A = J0(23)
            sage: A.dimension()
            2
        """
    def conductor(self):
        """
        Return the conductor of this abelian variety.

        EXAMPLES::

            sage: A = J0(23)
            sage: A.conductor().factor()
            23^2

            sage: A = J1(25)
            sage: A.conductor().factor()
            5^24

            sage: A = J0(11^2); A.decomposition()
            [Simple abelian subvariety 11a(1,121) of dimension 1 of J0(121),
             Simple abelian subvariety 11a(11,121) of dimension 1 of J0(121),
             Simple abelian subvariety 121a(1,121) of dimension 1 of J0(121),
             Simple abelian subvariety 121b(1,121) of dimension 1 of J0(121),
             Simple abelian subvariety 121c(1,121) of dimension 1 of J0(121),
             Simple abelian subvariety 121d(1,121) of dimension 1 of J0(121)]
            sage: A.conductor().factor()
            11^10

            sage: A = J0(33)[0]; A
            Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: A.conductor()
            11
            sage: A.elliptic_curve().conductor()
            11
        """
    def rank(self):
        """
        Return the rank of the underlying lattice of ``self``.

        EXAMPLES::

            sage: J = J0(33)
            sage: J.rank()
            6
            sage: J[1]
            Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33)
            sage: (J[1] * J[1]).rank()
            4
        """
    def degree(self):
        """
        Return the degree of this abelian variety, which is the dimension
        of the ambient Jacobian product.

        EXAMPLES::

            sage: A = J0(23)
            sage: A.dimension()
            2
        """
    def endomorphism_ring(self, category=None):
        """
        Return the endomorphism ring of ``self``.

        OUTPUT: b = self.sturm_bound()

        EXAMPLES: We compute a few endomorphism rings::

            sage: J0(11).endomorphism_ring()
            Endomorphism ring of Abelian variety J0(11) of dimension 1
            sage: J0(37).endomorphism_ring()
            Endomorphism ring of Abelian variety J0(37) of dimension 2
            sage: J0(33)[2].endomorphism_ring()
            Endomorphism ring of Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)

        No real computation is done::

            sage: J1(123456).endomorphism_ring()
            Endomorphism ring of Abelian variety J1(123456) of dimension 423185857
        """
    def sturm_bound(self):
        """
        Return a bound `B` such that all Hecke operators
        `T_n` for `n\\leq B` generate the Hecke algebra.

        OUTPUT: integer

        EXAMPLES::

            sage: J0(11).sturm_bound()
            2
            sage: J0(33).sturm_bound()
            8
            sage: J1(17).sturm_bound()
            48
            sage: J1(123456).sturm_bound()
            1693483008
            sage: JH(37,[2,3]).sturm_bound()
            7
            sage: J1(37).sturm_bound()
            228
        """
    @cached_method
    def is_hecke_stable(self) -> bool:
        """
        Return ``True`` if ``self`` is stable under the Hecke operators of its
        ambient Jacobian.

        OUTPUT: boolean

        EXAMPLES::

            sage: J0(11).is_hecke_stable()
            True
            sage: J0(33)[2].is_hecke_stable()
            True
            sage: J0(33)[0].is_hecke_stable()
            False
            sage: (J0(33)[0] + J0(33)[1]).is_hecke_stable()
            True
        """
    def is_subvariety(self, other) -> bool:
        """
        Return ``True`` if ``self`` is a subvariety of other as they sit in a
        common ambient modular Jacobian. In particular, this function will
        only return ``True`` if ``self`` and ``other`` have exactly the same ambient
        Jacobians.

        EXAMPLES::

            sage: J = J0(37); J
            Abelian variety J0(37) of dimension 2
            sage: A = J[0]; A
            Simple abelian subvariety 37a(1,37) of dimension 1 of J0(37)
            sage: A.is_subvariety(A)
            True
            sage: A.is_subvariety(J)
            True
        """
    def change_ring(self, R):
        """
        Change the base ring of this modular abelian variety.

        EXAMPLES::

            sage: A = J0(23)
            sage: A.change_ring(QQ)
            Abelian variety J0(23) of dimension 2
        """
    def level(self):
        """
        Return the level of this modular abelian variety, which is an
        integer `N` (usually minimal) such that this modular abelian variety
        is a quotient of `J_1(N)`. In the case that the ambient
        variety of ``self`` is a product of Jacobians, return the LCM of their
        levels.

        EXAMPLES::

            sage: J1(5077).level()
            5077
            sage: JH(389,[4]).level()
            389
            sage: (J0(11)*J0(17)).level()
            187
        """
    def newform_level(self, none_if_not_known: bool = False):
        """
        Write ``self`` as a product (up to isogeny) of newform abelian
        varieties `A_f`. Then this function return the least
        common multiple of the levels of the newforms `f`, along
        with the corresponding group or list of groups (the groups do not
        appear with multiplicity).

        INPUT:

        - ``none_if_not_known`` -- boolean (default: ``False``); if ``True``,
          return ``None`` instead of attempting to compute the newform level,
          if it isn't already known. This None result is not cached.

        OUTPUT: integer group or list of distinct groups

        EXAMPLES::

            sage: J0(33)[0].newform_level()
            (11, Congruence Subgroup Gamma0(33))
            sage: J0(33)[0].newform_level(none_if_not_known=True)
            (11, Congruence Subgroup Gamma0(33))

        Here there are multiple groups since there are in fact multiple
        newforms::

            sage: (J0(11) * J1(13)).newform_level()
            (143, [Congruence Subgroup Gamma0(11), Congruence Subgroup Gamma1(13)])
        """
    def zero_subvariety(self):
        """
        Return the zero subvariety of ``self``.

        EXAMPLES::

            sage: J = J0(37)
            sage: J.zero_subvariety()
            Simple abelian subvariety of dimension 0 of J0(37)
            sage: J.zero_subvariety().level()
            37
            sage: J.zero_subvariety().newform_level()
            (1, [])
        """
    def rational_torsion_order(self, proof: bool = True):
        """
        Return the order of the rational torsion subgroup of this modular
        abelian variety.

        This function is really an alias for
        :meth:`~sage.modular.abvar.torsion_subgroup.RationalTorsionSubgroup.order`
        See the docstring there for a more in-depth reference and more
        interesting examples.

        INPUT:

        - ``proof`` -- boolean (default: ``True``)

        OUTPUT:

        The order of the rational torsion subgroup of this modular abelian
        variety.

        EXAMPLES::

            sage: J0(11).rational_torsion_subgroup().order()
            5
            sage: J0(11).rational_torsion_order()
            5
        """
    def number_of_rational_points(self):
        """
        Return the number of rational points of this modular abelian variety.

        It is not always possible to compute the order of the torsion
        subgroup. The BSD conjecture is assumed to compute the algebraic rank.

        OUTPUT: a positive integer or infinity

        EXAMPLES::

            sage: J0(23).number_of_rational_points()
            11
            sage: J0(29).number_of_rational_points()
            7
            sage: J0(37).number_of_rational_points()
            +Infinity

            sage: J0(12); J0(12).number_of_rational_points()
            Abelian variety J0(12) of dimension 0
            1

            sage: J1(17).number_of_rational_points()
            584

            sage: J1(16).number_of_rational_points()
            Traceback (most recent call last):
            ...
            RuntimeError: Unable to compute order of torsion subgroup (it is in [1, 2, 4, 5, 10, 20])
        """
    def frobenius_polynomial(self, p, var: str = 'x'):
        """
        Compute the frobenius polynomial at `p`.

        INPUT:

        - ``p`` -- prime number

        OUTPUT: a monic integral polynomial

        EXAMPLES::

            sage: f = Newform('39b','a')
            sage: A = AbelianVariety(f)
            sage: A.frobenius_polynomial(5)
            x^4 + 2*x^2 + 25

            sage: J = J0(23)
            sage: J.frobenius_polynomial(997)
            x^4 + 20*x^3 + 1374*x^2 + 19940*x + 994009

            sage: J = J0(33)
            sage: J.frobenius_polynomial(7)
            x^6 + 9*x^4 - 16*x^3 + 63*x^2 + 343

            sage: J = J0(19)
            sage: J.frobenius_polynomial(3, var='y')
            y^2 + 2*y + 3

            sage: J = J0(3); J
            Abelian variety J0(3) of dimension 0
            sage: J.frobenius_polynomial(11)
            1

            sage: A = J1(27)[1]; A
            Simple abelian subvariety 27bG1(1,27) of dimension 12 of J1(27)
            sage: A.frobenius_polynomial(11)
            x^24 - 3*x^23 - 15*x^22 + 126*x^21 - 201*x^20 - 1488*x^19 + 7145*x^18 - 1530*x^17 - 61974*x^16 + 202716*x^15 - 19692*x^14 - 1304451*x^13 + 4526883*x^12 - 14348961*x^11 - 2382732*x^10 + 269814996*x^9 - 907361334*x^8 - 246408030*x^7 + 12657803345*x^6 - 28996910448*x^5 - 43086135081*x^4 + 297101409066*x^3 - 389061369015*x^2 - 855935011833*x + 3138428376721

            sage: J = J1(33)
            sage: J.frobenius_polynomial(11)
            Traceback (most recent call last):
            ...
            ValueError: p must not divide the level of self
            sage: J.frobenius_polynomial(4)
            Traceback (most recent call last):
            ...
            ValueError: p must be prime
        """
    def homology(self, base_ring=...):
        """
        Return the homology of this modular abelian variety.

        .. warning::

           For efficiency reasons the basis of the integral homology
           need not be the same as the basis for the rational
           homology.

        EXAMPLES::

            sage: J0(389).homology(GF(7))
            Homology with coefficients in Finite Field of size 7 of Abelian variety J0(389) of dimension 32
            sage: J0(389).homology(QQ)
            Rational Homology of Abelian variety J0(389) of dimension 32
            sage: J0(389).homology(ZZ)
            Integral Homology of Abelian variety J0(389) of dimension 32
        """
    def integral_homology(self):
        """
        Return the integral homology of this modular abelian variety.

        EXAMPLES::

            sage: H = J0(43).integral_homology(); H
            Integral Homology of Abelian variety J0(43) of dimension 3
            sage: H.rank()
            6
            sage: H = J1(17).integral_homology(); H
            Integral Homology of Abelian variety J1(17) of dimension 5
            sage: H.rank()
            10

        If you just ask for the rank of the homology, no serious
        calculations are done, so the following is fast::

            sage: H = J0(50000).integral_homology(); H
            Integral Homology of Abelian variety J0(50000) of dimension 7351
            sage: H.rank()
            14702

        A product::

            sage: H = (J0(11) * J1(13)).integral_homology()
            sage: H.hecke_operator(2)
            Hecke operator T_2 on Integral Homology of Abelian variety J0(11) x J1(13) of dimension 3
            sage: H.hecke_operator(2).matrix()
            [-2  0  0  0  0  0]
            [ 0 -2  0  0  0  0]
            [ 0  0 -1 -1 -1  1]
            [ 0  0  1 -2 -1  0]
            [ 0  0  0  0 -2  1]
            [ 0  0  0  0 -1 -1]
        """
    def rational_homology(self):
        """
        Return the rational homology of this modular abelian variety.

        EXAMPLES::

            sage: H = J0(37).rational_homology(); H
            Rational Homology of Abelian variety J0(37) of dimension 2
            sage: H.rank()
            4
            sage: H.base_ring()
            Rational Field
            sage: H = J1(17).rational_homology(); H
            Rational Homology of Abelian variety J1(17) of dimension 5
            sage: H.rank()
            10
            sage: H.base_ring()
            Rational Field
        """
    def lseries(self):
        """
        Return the complex `L`-series of this modular abelian
        variety.

        EXAMPLES::

            sage: A = J0(37)
            sage: A.lseries()
            Complex L-series attached to Abelian variety J0(37) of dimension 2
        """
    def padic_lseries(self, p):
        """
        Return the `p`-adic `L`-series of this modular
        abelian variety.

        EXAMPLES::

            sage: A = J0(37)
            sage: A.padic_lseries(7)
            7-adic L-series attached to Abelian variety J0(37) of dimension 2
        """
    def hecke_operator(self, n):
        """
        Return the `n`-th Hecke operator on the modular abelian
        variety, if this makes sense [[elaborate]]. Otherwise raise a
        :exc:`ValueError`.

        EXAMPLES: We compute `T_2` on `J_0(37)`.

        ::

            sage: t2 = J0(37).hecke_operator(2); t2
            Hecke operator T_2 on Abelian variety J0(37) of dimension 2
            sage: t2.charpoly().factor()
            x * (x + 2)
            sage: t2.index()
            2

        Note that there is no matrix associated to Hecke operators on
        modular abelian varieties. For a matrix, instead consider, e.g.,
        the Hecke operator on integral or rational homology.

        ::

            sage: t2.action_on_homology().matrix()
            [-1  1  1 -1]
            [ 1 -1  1  0]
            [ 0  0 -2  1]
            [ 0  0  0  0]
        """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Return the characteristic polynomial of the `n`-th Hecke
        operator `T_n` acting on ``self``. Raises an :exc:`ArithmeticError`
        if ``self`` is not Hecke equivariant.

        INPUT:

        - ``n`` -- integer `\\geq 1`

        - ``var`` -- string (default: ``'x'``); valid variable name

        EXAMPLES::

            sage: J0(33).hecke_polynomial(2)
            x^3 + 3*x^2 - 4
            sage: f = J0(33).hecke_polynomial(2, 'y'); f
            y^3 + 3*y^2 - 4
            sage: f.parent()
            Univariate Polynomial Ring in y over Rational Field
            sage: J0(33)[2].hecke_polynomial(3)
            x + 1
            sage: J0(33)[0].hecke_polynomial(5)
            x - 1
            sage: J0(33)[0].hecke_polynomial(11)
            x - 1
            sage: J0(33)[0].hecke_polynomial(3)
            Traceback (most recent call last):
            ...
            ArithmeticError: subspace is not invariant under matrix
        """
    def qbar_torsion_subgroup(self):
        """
        Return the group of all points of finite order in the algebraic
        closure of this abelian variety.

        EXAMPLES::

            sage: T = J0(33).qbar_torsion_subgroup(); T
            Group of all torsion points in QQbar on Abelian variety J0(33) of dimension 3

        The field of definition is the same as the base field of the
        abelian variety.

        ::

            sage: T.field_of_definition()
            Rational Field

        On the other hand, T is a module over `\\ZZ`.

        ::

            sage: T.base_ring()
            Integer Ring
        """
    def rational_torsion_subgroup(self):
        """
        Return the maximal torsion subgroup of ``self`` defined over `\\QQ`.

        EXAMPLES::

            sage: J = J0(33)
            sage: A = J.new_subvariety()
            sage: A
            Abelian subvariety of dimension 1 of J0(33)
            sage: t = A.rational_torsion_subgroup(); t
            Torsion subgroup of Abelian subvariety of dimension 1 of J0(33)
            sage: t.multiple_of_order()
            4
            sage: t.divisor_of_order()
            4
            sage: t.order()
            4
            sage: t.gens()
            ([(1/2, 0, 0, -1/2, 0, 0)], [(0, 0, 1/2, 0, 1/2, -1/2)])
        """
    def cuspidal_subgroup(self):
        """
        Return the cuspidal subgroup of this modular abelian variety. This
        is the subgroup generated by rational cusps.

        EXAMPLES::

            sage: J = J0(54)
            sage: C = J.cuspidal_subgroup()
            sage: C.gens()
            ([(1/3, 0, 0, 0, 0, 1/3, 0, 2/3)], [(0, 1/3, 0, 0, 0, 2/3, 0, 1/3)], [(0, 0, 1/9, 1/9, 1/9, 1/9, 1/9, 2/9)], [(0, 0, 0, 1/3, 0, 1/3, 0, 0)], [(0, 0, 0, 0, 1/3, 1/3, 0, 1/3)], [(0, 0, 0, 0, 0, 0, 1/3, 2/3)])
            sage: C.invariants()
            [3, 3, 3, 3, 3, 9]
            sage: J1(13).cuspidal_subgroup()
            Finite subgroup with invariants [19, 19] over QQ of Abelian variety J1(13) of dimension 2
            sage: A = J0(33)[0]
            sage: A.cuspidal_subgroup()
            Finite subgroup with invariants [5] over QQ of Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
        """
    def shimura_subgroup(self):
        """
        Return the Shimura subgroup of this modular abelian variety.

        This is the kernel of `J_0(N) \\rightarrow J_1(N)` under the
        natural map.

        Here we compute the Shimura subgroup as the kernel of `J_0(N)
        \\rightarrow J_0(Np)` where the map is the difference between
        the two degeneracy maps.

        EXAMPLES::

            sage: J = J0(11)
            sage: J.shimura_subgroup()
            Finite subgroup with invariants [5] over QQ of Abelian variety J0(11) of dimension 1

            sage: J = J0(17)
            sage: G = J.cuspidal_subgroup(); G
            Finite subgroup with invariants [4] over QQ of Abelian variety J0(17) of dimension 1
            sage: S = J.shimura_subgroup(); S
            Finite subgroup with invariants [4] over QQ of Abelian variety J0(17) of dimension 1
            sage: G.intersection(S)
            Finite subgroup with invariants [2] over QQ of Abelian variety J0(17) of dimension 1

            sage: J = J0(33)
            sage: A = J.decomposition()[0]
            sage: A.shimura_subgroup()
            Finite subgroup with invariants [5] over QQ of Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: J.shimura_subgroup()
            Finite subgroup with invariants [10] over QQ of Abelian variety J0(33) of dimension 3
        """
    def rational_cusp_subgroup(self):
        """
        Return the subgroup of this modular abelian variety generated by
        rational cusps.

        This is a subgroup of the group of rational points in the cuspidal
        subgroup.

        .. warning::

           This is only currently implemented for
           `\\Gamma_0(N)`.

        EXAMPLES::

            sage: J = J0(54)
            sage: CQ = J.rational_cusp_subgroup(); CQ
            Finite subgroup with invariants [3, 3, 9] over QQ of Abelian variety J0(54) of dimension 4
            sage: CQ.gens()
            ([(1/3, 0, 0, 1/3, 2/3, 1/3, 0, 1/3)], [(0, 0, 1/9, 1/9, 7/9, 7/9, 1/9, 8/9)], [(0, 0, 0, 0, 0, 0, 1/3, 2/3)])
            sage: factor(CQ.order())
            3^4
            sage: CQ.invariants()
            [3, 3, 9]

        In this example the rational cuspidal subgroup and the cuspidal
        subgroup differ by a lot.

        ::

            sage: J = J0(49)
            sage: J.cuspidal_subgroup()
            Finite subgroup with invariants [2, 14] over QQ of Abelian variety J0(49) of dimension 1
            sage: J.rational_cusp_subgroup()
            Finite subgroup with invariants [2] over QQ of Abelian variety J0(49) of dimension 1

        Note that computation of the rational cusp subgroup isn't
        implemented for `\\Gamma_1`.

        ::

            sage: J = J1(13)
            sage: J.cuspidal_subgroup()
            Finite subgroup with invariants [19, 19] over QQ of Abelian variety J1(13) of dimension 2
            sage: J.rational_cusp_subgroup()
            Traceback (most recent call last):
            ...
            NotImplementedError: computation of rational cusps only implemented in Gamma0 case.
        """
    def rational_cuspidal_subgroup(self):
        """
        Return the rational subgroup of the cuspidal subgroup of this
        modular abelian variety.

        This is a subgroup of the group of rational points in the
        cuspidal subgroup.

        .. warning::

           This is only currently implemented for
           `\\Gamma_0(N)`.

        EXAMPLES::

            sage: J = J0(54)
            sage: CQ = J.rational_cuspidal_subgroup(); CQ
            Finite subgroup with invariants [3, 3, 9] over QQ of Abelian variety J0(54) of dimension 4
            sage: CQ.gens()
            ([(1/3, 0, 0, 1/3, 2/3, 1/3, 0, 1/3)], [(0, 0, 1/9, 1/9, 7/9, 7/9, 1/9, 8/9)], [(0, 0, 0, 0, 0, 0, 1/3, 2/3)])
            sage: factor(CQ.order())
            3^4
            sage: CQ.invariants()
            [3, 3, 9]

        In this example the rational cuspidal subgroup and the cuspidal
        subgroup differ by a lot.

        ::

            sage: J = J0(49)
            sage: J.cuspidal_subgroup()
            Finite subgroup with invariants [2, 14] over QQ of Abelian variety J0(49) of dimension 1
            sage: J.rational_cuspidal_subgroup()
            Finite subgroup with invariants [2] over QQ of Abelian variety J0(49) of dimension 1

        Note that computation of the rational cusp subgroup isn't
        implemented for `\\Gamma_1`.

        ::

            sage: J = J1(13)
            sage: J.cuspidal_subgroup()
            Finite subgroup with invariants [19, 19] over QQ of Abelian variety J1(13) of dimension 2
            sage: J.rational_cuspidal_subgroup()
            Traceback (most recent call last):
            ...
            NotImplementedError: only implemented when group is Gamma0
        """
    def zero_subgroup(self):
        """
        Return the zero subgroup of this modular abelian variety, as a
        finite group.

        EXAMPLES::

            sage: A =J0(54); G = A.zero_subgroup(); G
            Finite subgroup with invariants [] over QQ of Abelian variety J0(54) of dimension 4
            sage: G.is_subgroup(A)
            True
        """
    def finite_subgroup(self, X, field_of_definition=None, check: bool = True):
        """
        Return a finite subgroup of this modular abelian variety.

        INPUT:

        - ``X`` -- list of elements of other finite subgroups
          of this modular abelian variety or elements that coerce into the
          rational homology (viewed as a rational vector space); also X could
          be a finite subgroup itself that is contained in this abelian
          variety.

        - ``field_of_definition`` -- (default: ``None``) field
          over which this group is defined. If ``None`` try to figure out the
          best base field.

        OUTPUT: a finite subgroup of a modular abelian variety

        EXAMPLES::

            sage: J = J0(11)
            sage: J.finite_subgroup([[1/5,0], [0,1/3]])
            Finite subgroup with invariants [15] over QQbar of Abelian variety J0(11) of dimension 1

        ::

            sage: J = J0(33); C = J[0].cuspidal_subgroup(); C
            Finite subgroup with invariants [5] over QQ of Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33)
            sage: J.finite_subgroup([[0,0,0,0,0,1/6]])
            Finite subgroup with invariants [6] over QQbar of Abelian variety J0(33) of dimension 3
            sage: J.finite_subgroup(C)
            Finite subgroup with invariants [5] over QQ of Abelian variety J0(33) of dimension 3

        This method gives a way of changing the ambient abelian variety of a
        finite subgroup. This caused an issue in :issue:`6392` but should be
        fixed now. ::

            sage: A, B = J0(43)
            sage: G, _ = A.intersection(B)
            sage: G
            Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 43a(1,43) of dimension 1 of J0(43)
            sage: B.finite_subgroup(G)
            Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 43b(1,43) of dimension 2 of J0(43)
        """
    def torsion_subgroup(self, n):
        """
        If `n` is an integer, return the subgroup of points of order `n`.
        Return the `n`-torsion subgroup of elements of order dividing `n` of
        this modular abelian variety `A`, i.e., the group `A[n]`.

        EXAMPLES::

            sage: J1(13).torsion_subgroup(19)
            Finite subgroup with invariants [19, 19, 19, 19] over QQ of Abelian variety J1(13) of dimension 2

        ::

            sage: A = J0(23)
            sage: G = A.torsion_subgroup(5); G
            Finite subgroup with invariants [5, 5, 5, 5] over QQ of Abelian variety J0(23) of dimension 2
            sage: G.order()
            625
            sage: G.gens()
            ([(1/5, 0, 0, 0)], [(0, 1/5, 0, 0)], [(0, 0, 1/5, 0)], [(0, 0, 0, 1/5)])
            sage: A = J0(23)
            sage: A.torsion_subgroup(2).order()
            16
        """
    def degen_t(self, none_if_not_known: bool = False):
        """
        If this abelian variety is obtained via decomposition then it gets
        labeled with the newform label along with some information about
        degeneracy maps. In particular, the label ends in a pair `(t,N)`, where
        `N` is the ambient level and `t` is an integer that divides the
        quotient of `N` by the newform level. This function returns the tuple
        `(t,N)`, or raises a :exc:`ValueError` if ``self`` is not simple.

        .. NOTE::

           It need not be the case that ``self`` is literally equal to the
           image of the newform abelian variety under the `t`-th degeneracy
           map. See the documentation for the label method for more details.

        INPUT:

        - ``none_if_not_known`` -- (default: ``False``) if ``True``, return
          ``None`` instead of attempting to compute the degen map's `t`, if it
          isn't known. This ``None`` result is not cached.

        OUTPUT: a pair (integer, integer)

        EXAMPLES::

            sage: D = J0(33).decomposition(); D
            [Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33),
             Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33),
             Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)]
            sage: D[0].degen_t()
            (1, 33)
            sage: D[1].degen_t()
            (3, 33)
            sage: D[2].degen_t()
            (1, 33)
            sage: J0(33).degen_t()
            Traceback (most recent call last):
            ...
            ValueError: self must be simple
        """
    def isogeny_number(self, none_if_not_known: bool = False):
        """
        Return the number (starting at 0) of the isogeny class of new
        simple abelian varieties that ``self`` is in.

        If ``self`` is not simple,
        this raises a :exc:`ValueError` exception.

        INPUT:

        - ``none_if_not_known`` -- boolean (default: ``False``); if
          ``True`` then this function may return ``None`` instead of ``True``
          or ``False`` if we do not already know the isogeny number of ``self``.

        EXAMPLES: We test the ``none_if_not_known`` flag first::

            sage: J0(33).isogeny_number(none_if_not_known=True) is None
            True

        Of course, `J_0(33)` is not simple, so this function
        raises a :exc:`ValueError`::

            sage: J0(33).isogeny_number()
            Traceback (most recent call last):
            ...
            ValueError: self must be simple

        Each simple factor has isogeny number 1, since that's the number at
        which the factor is new.

        ::

            sage: J0(33)[1].isogeny_number()
            0
            sage: J0(33)[2].isogeny_number()
            0

        Next consider `J_0(37)` where there are two distinct
        newform factors::

            sage: J0(37)[1].isogeny_number()
            1
        """
    def is_simple(self, none_if_not_known: bool = False) -> bool:
        """
        Return whether or not this modular abelian variety is simple.

        This means that it has no proper nonzero abelian subvarieties.

        INPUT:

        - ``none_if_not_known`` -- boolean (default: ``False``); if ``True``
          then this function may return ``None`` instead of ``True`` of
          ``False`` if we don't already know whether or not ``self`` is simple.

        EXAMPLES::

            sage: J0(5).is_simple(none_if_not_known=True) is None  # this may fail if J0(5) comes up elsewhere...
            True
            sage: J0(33).is_simple()
            False
            sage: J0(33).is_simple(none_if_not_known=True)
            False
            sage: J0(33)[1].is_simple()
            True
            sage: J1(17).is_simple()
            False
        """
    def decomposition(self, simple: bool = True, bound=None):
        """
        Return a sequence of abelian subvarieties of ``self`` that are all
        simple, have finite intersection and sum to ``self``.

        INPUT:

        - ``simple`` -- boolean (default: ``True``); if ``True``, all factors
          are simple. If ``False``, each factor returned is isogenous to a
          power of a simple and the simples in each factor are distinct.


        - ``bound`` -- integer (default: ``None``); if given, only use
          Hecke operators up to this bound when decomposing. This can give
          wrong answers, so use with caution!

        EXAMPLES::

            sage: m = ModularSymbols(11).cuspidal_submodule()
            sage: d1 = m.degeneracy_map(33,1).matrix(); d3=m.degeneracy_map(33,3).matrix()
            sage: w = ModularSymbols(33).submodule((d1 + d3).image(), check=False)
            sage: A = w.abelian_variety(); A
            Abelian subvariety of dimension 1 of J0(33)
            sage: D = A.decomposition(); D
            [Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33)]
            sage: D[0] == A
            True
            sage: B = A + J0(33)[0]; B
            Abelian subvariety of dimension 2 of J0(33)
            sage: dd = B.decomposition(simple=False); dd
            [Abelian subvariety of dimension 2 of J0(33)]
            sage: dd[0] == B
            True
            sage: dd = B.decomposition(); dd
            [Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33),
             Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33)]
            sage: sum(dd) == B
            True

        We decompose a product of two Jacobians::

            sage: (J0(33) * J0(11)).decomposition()
            [Simple abelian subvariety 11a(1,11) of dimension 1 of J0(33) x J0(11),
             Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33) x J0(11),
             Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33) x J0(11),
             Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33) x J0(11)]
        """
    def complement(self, A=None):
        """
        Return a complement of this abelian variety.

        INPUT:

        - ``A`` -- (default: ``None``) if given, ``A`` must be an
          abelian variety that contains ``self``, in which case the complement of
          ``self`` is taken inside ``A``. Otherwise the complement is taken in the
          ambient product Jacobian.

        OUTPUT: abelian variety

        EXAMPLES::

            sage: a,b,c = J0(33)
            sage: (a+b).complement()
            Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)
            sage: (a+b).complement() == c
            True
            sage: a.complement(a+b)
            Abelian subvariety of dimension 1 of J0(33)
        """
    def dual(self):
        """
        Return the dual of this abelian variety.

        OUTPUT:

        - dual abelian variety
        - morphism from ``self`` to dual
        - covering morphism from J to dual

        .. warning::

           This is currently only implemented when ``self`` is an abelian
           subvariety of the ambient Jacobian product, and the
           complement of ``self`` in the ambient product Jacobian share no
           common factors. A more general implementation will require
           implementing computation of the intersection pairing on
           integral homology and the resulting Weil pairing on
           torsion.

        EXAMPLES: We compute the dual of the elliptic curve newform abelian
        variety of level `33`, and find the kernel of the modular
        map, which has structure `(\\ZZ/3)^2`.

        ::

            sage: A,B,C = J0(33)
            sage: C
            Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)
            sage: Cd, f, pi = C.dual()
            sage: f.matrix()
            [3 0]
            [0 3]
            sage: f.kernel()[0]
            Finite subgroup with invariants [3, 3] over QQ of Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)

        By a theorem the modular degree must thus be `3`::

            sage: E = EllipticCurve('33a')
            sage: E.modular_degree()
            3

        Next we compute the dual of a `2`-dimensional new simple
        abelian subvariety of `J_0(43)`.

        ::

            sage: A = AbelianVariety('43b'); A
            Newform abelian subvariety 43b of dimension 2 of J0(43)
            sage: Ad, f, pi = A.dual()

        The kernel shows that the modular degree is `2`::

            sage: f.kernel()[0]
            Finite subgroup with invariants [2, 2] over QQ of Newform abelian subvariety 43b of dimension 2 of J0(43)

        Unfortunately, the dual is not implemented in general::

            sage: A = J0(22)[0]; A
            Simple abelian subvariety 11a(1,22) of dimension 1 of J0(22)
            sage: A.dual()
            Traceback (most recent call last):
            ...
            NotImplementedError: dual not implemented unless complement shares no simple factors with self.
        """
    def __getitem__(self, i):
        """
        Return the `i`-th decomposition factor of self
        or return the slice `i` of decompositions of ``self``.

        EXAMPLES::

            sage: J = J0(389)
            sage: J.decomposition()
            [Simple abelian subvariety 389a(1,389) of dimension 1 of J0(389),
             Simple abelian subvariety 389b(1,389) of dimension 2 of J0(389),
             Simple abelian subvariety 389c(1,389) of dimension 3 of J0(389),
             Simple abelian subvariety 389d(1,389) of dimension 6 of J0(389),
             Simple abelian subvariety 389e(1,389) of dimension 20 of J0(389)]
            sage: J[2]
            Simple abelian subvariety 389c(1,389) of dimension 3 of J0(389)
            sage: J[-1]
            Simple abelian subvariety 389e(1,389) of dimension 20 of J0(389)
            sage: J = J0(125); J.decomposition()
            [Simple abelian subvariety 125a(1,125) of dimension 2 of J0(125),
             Simple abelian subvariety 125b(1,125) of dimension 2 of J0(125),
             Simple abelian subvariety 125c(1,125) of dimension 4 of J0(125)]
            sage: J[:2]
            [Simple abelian subvariety 125a(1,125) of dimension 2 of J0(125),
             Simple abelian subvariety 125b(1,125) of dimension 2 of J0(125)]
        """

class ModularAbelianVariety(ModularAbelianVariety_abstract):
    def __init__(self, groups, lattice=None, base_field=..., is_simple=None, newform_level=None, isogeny_number=None, number=None, check: bool = True) -> None:
        """
        Create a modular abelian variety with given level and base field.

        INPUT:

        - ``groups`` -- tuple of congruence subgroups

        - ``lattice`` -- (default: `\\ZZ^n`) a full lattice in `\\ZZ^n`, where
          `n` is the sum of the dimensions of the spaces of cuspidal modular
          symbols corresponding to each `\\Gamma \\in` groups

        - ``base_field`` -- a field (default: `\\QQ`)

        EXAMPLES::

            sage: J0(23)
            Abelian variety J0(23) of dimension 2
        """
    def lattice(self):
        """
        Return the lattice that defines this abelian variety.

        OUTPUT:

        - ``lattice`` -- a lattice embedded in the rational
          homology of the ambient product Jacobian

        EXAMPLES::

            sage: A = (J0(11) * J0(37))[1]; A
            Simple abelian subvariety 37a(1,37) of dimension 1 of J0(11) x J0(37)
            sage: type(A)
            <class 'sage.modular.abvar.abvar.ModularAbelianVariety_with_category'>
            sage: A.lattice()
            Free module of degree 6 and rank 2 over Integer Ring
            Echelon basis matrix:
            [ 0  0  1 -1  1  0]
            [ 0  0  0  0  2 -1]
        """

class ModularAbelianVariety_modsym_abstract(ModularAbelianVariety_abstract):
    def __add__(self, other):
        """
        Add two modular abelian variety factors.

        EXAMPLES::

            sage: A = J0(42); D = A.decomposition(); D
            [Simple abelian subvariety 14a(1,42) of dimension 1 of J0(42),
             Simple abelian subvariety 14a(3,42) of dimension 1 of J0(42),
             Simple abelian subvariety 21a(1,42) of dimension 1 of J0(42),
             Simple abelian subvariety 21a(2,42) of dimension 1 of J0(42),
             Simple abelian subvariety 42a(1,42) of dimension 1 of J0(42)]
            sage: D[0] + D[1]
            Abelian subvariety of dimension 2 of J0(42)
            sage: D[1].is_subvariety(D[0] + D[1])
            True
            sage: D[0] + D[1] + D[2]
            Abelian subvariety of dimension 3 of J0(42)
            sage: D[0] + D[0]
            Abelian subvariety of dimension 1 of J0(42)
            sage: D[0] + D[0] == D[0]
            True
            sage: sum(D, D[0]) == A
            True
        """
    def groups(self):
        """
        Return the tuple of groups associated to the modular symbols
        abelian variety. This is always a 1-tuple.

        OUTPUT: tuple

        EXAMPLES::

            sage: A = ModularSymbols(33).cuspidal_submodule().abelian_variety(); A
            Abelian variety J0(33) of dimension 3
            sage: A.groups()
            (Congruence Subgroup Gamma0(33),)
            sage: type(A)
            <class 'sage.modular.abvar.abvar.ModularAbelianVariety_modsym_with_category'>
        """
    def lattice(self):
        """
        Return the lattice defining this modular abelian variety.

        OUTPUT:

        A free `\\ZZ`-module embedded in an ambient `\\QQ`-vector space.

        EXAMPLES::

            sage: A = ModularSymbols(33).cuspidal_submodule()[0].abelian_variety(); A
            Abelian subvariety of dimension 1 of J0(33)
            sage: A.lattice()
            Free module of degree 6 and rank 2 over Integer Ring
            User basis matrix:
            [ 1  0  0 -1  0  0]
            [ 0  0  1  0  1 -1]
            sage: type(A)
            <class 'sage.modular.abvar.abvar.ModularAbelianVariety_modsym_with_category'>
        """
    def modular_symbols(self, sign: int = 0):
        """
        Return space of modular symbols (with given sign) associated to
        this modular abelian variety, if it can be found by cutting down
        using Hecke operators. Otherwise raise a :exc:`RuntimeError`
        exception.

        EXAMPLES::

            sage: A = J0(37)
            sage: A.modular_symbols()
            Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field
            sage: A.modular_symbols(1)
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(37) of weight 2 with sign 1 over Rational Field

        More examples::

            sage: J0(11).modular_symbols()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: J0(11).modular_symbols(sign=1)
            Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field
            sage: J0(11).modular_symbols(sign=0)
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: J0(11).modular_symbols(sign=-1)
            Modular Symbols space of dimension 1 for Gamma_0(11) of weight 2 with sign -1 over Rational Field

        Even more examples::

            sage: A = J0(33)[1]; A
            Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33)
            sage: A.modular_symbols()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field

        It is not always possible to determine the sign subspaces::

            sage: A.modular_symbols(1)
            Traceback (most recent call last):
            ...
            RuntimeError: unable to determine sign (=1) space of modular symbols

        ::

            sage: A.modular_symbols(-1)
            Traceback (most recent call last):
            ...
            RuntimeError: unable to determine sign (=-1) space of modular symbols
        """
    def group(self):
        """
        Return the congruence subgroup associated that this modular abelian
        variety is associated to.

        EXAMPLES::

            sage: J0(13).group()
            Congruence Subgroup Gamma0(13)
            sage: J1(997).group()
            Congruence Subgroup Gamma1(997)
            sage: JH(37,[3]).group()
            Congruence Subgroup Gamma_H(37) with H generated by [3]
            sage: J0(37)[1].groups()
            (Congruence Subgroup Gamma0(37),)
        """
    def is_subvariety(self, other) -> bool:
        """
        Return ``True`` if ``self`` is a subvariety of ``other``.

        EXAMPLES::

            sage: J = J0(37); J
            Abelian variety J0(37) of dimension 2
            sage: A = J[0]; A
            Simple abelian subvariety 37a(1,37) of dimension 1 of J0(37)
            sage: A.is_subvariety(J)
            True
            sage: A.is_subvariety(J0(11))
            False

        There may be a way to map `A` into `J_0(74)`, but
        `A` is not equipped with any special structure of an
        embedding.

        ::

            sage: A.is_subvariety(J0(74))
            False

        Some ambient examples::

            sage: J = J0(37)
            sage: J.is_subvariety(J)
            True
            sage: J.is_subvariety(25)
            False

        More examples::

            sage: A = J0(42); D = A.decomposition(); D
            [Simple abelian subvariety 14a(1,42) of dimension 1 of J0(42),
             Simple abelian subvariety 14a(3,42) of dimension 1 of J0(42),
             Simple abelian subvariety 21a(1,42) of dimension 1 of J0(42),
             Simple abelian subvariety 21a(2,42) of dimension 1 of J0(42),
             Simple abelian subvariety 42a(1,42) of dimension 1 of J0(42)]
            sage: D[0].is_subvariety(A)
            True
            sage: D[1].is_subvariety(D[0] + D[1])
            True
            sage: D[2].is_subvariety(D[0] + D[1])
            False
        """
    def is_ambient(self) -> bool:
        """
        Return ``True`` if this abelian variety attached to a modular symbols
        space is attached to the cuspidal subspace of the ambient
        modular symbols space.

        OUTPUT: boolean

        EXAMPLES::

            sage: A = ModularSymbols(43).cuspidal_subspace().abelian_variety(); A
            Abelian variety J0(43) of dimension 3
            sage: A.is_ambient()
            True
            sage: type(A)
            <class 'sage.modular.abvar.abvar.ModularAbelianVariety_modsym_with_category'>
            sage: A = ModularSymbols(43).cuspidal_subspace()[1].abelian_variety(); A
            Abelian subvariety of dimension 2 of J0(43)
            sage: A.is_ambient()
            False
        """
    def dimension(self):
        """
        Return the dimension of this modular abelian variety.

        EXAMPLES::

            sage: J0(37)[0].dimension()
            1
            sage: J0(43)[1].dimension()
            2
            sage: J1(17)[1].dimension()
            4
        """
    def new_subvariety(self, p=None):
        """
        Return the new or `p`-new subvariety of ``self``.

        INPUT:

        - ``self`` -- a modular abelian variety

        - ``p`` -- prime number or None (default); if `p` is a
          prime, return the `p`-new subvariety. Otherwise return the full new
          subvariety.

        EXAMPLES::

            sage: J0(34).new_subvariety()
            Abelian subvariety of dimension 1 of J0(34)
            sage: J0(100).new_subvariety()
            Abelian subvariety of dimension 1 of J0(100)
            sage: J1(13).new_subvariety()
            Abelian variety J1(13) of dimension 2
        """
    def old_subvariety(self, p=None):
        """
        Return the old or `p`-old abelian variety of ``self``.

        INPUT:

        - ``self`` -- a modular abelian variety

        - ``p`` -- prime number or ``None`` (default); if `p` is a
          prime, return the `p`-old subvariety. Otherwise return the full old
          subvariety.

        EXAMPLES::

            sage: J0(33).old_subvariety()
            Abelian subvariety of dimension 2 of J0(33)
            sage: J0(100).old_subvariety()
            Abelian subvariety of dimension 6 of J0(100)
            sage: J1(13).old_subvariety()
            Abelian subvariety of dimension 0 of J1(13)
        """
    def decomposition(self, simple: bool = True, bound=None):
        """
        Decompose this modular abelian variety as a product of abelian
        subvarieties, up to isogeny.

        INPUT:

        - ``simple`` -- boolean (default: ``True``); if ``True``, all factors
          are simple. If ``False``, each factor returned is isogenous to a
          power of a simple and the simples in each factor are distinct.


        - ``bound`` -- integer (default: ``None``); if given, only use
          Hecke operators up to this bound when decomposing. This can give
          wrong answers, so use with caution!

        EXAMPLES::

            sage: J = J0(33)
            sage: J.decomposition()
            [Simple abelian subvariety 11a(1,33) of dimension 1 of J0(33),
             Simple abelian subvariety 11a(3,33) of dimension 1 of J0(33),
             Simple abelian subvariety 33a(1,33) of dimension 1 of J0(33)]
            sage: J1(17).decomposition()
            [Simple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17),
             Simple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)]
        """

class ModularAbelianVariety_modsym(ModularAbelianVariety_modsym_abstract):
    def __init__(self, modsym, lattice=None, newform_level=None, is_simple=None, isogeny_number=None, number=None, check: bool = True) -> None:
        """
        Modular abelian variety that corresponds to a Hecke stable space of
        cuspidal modular symbols.

        EXAMPLES: We create a modular abelian variety attached to a space
        of modular symbols.

        ::

            sage: M = ModularSymbols(23).cuspidal_submodule()
            sage: A = M.abelian_variety(); A
            Abelian variety J0(23) of dimension 2
        """
    def component_group_order(self, p):
        '''
        Return the order of the component group of the special fiber
        at `p` of the Neron model of ``self``.

        .. NOTE::

            For bad primes, this is only implemented when the group
            is `\\Gamma_0` and `p` exactly divides the level.

        .. NOTE::

            The input abelian variety must be simple.

        ALGORITHM: See "Component Groups of Quotients of J0(N)" by Kohel and Stein.  That
        paper is about optimal quotients; however, section 4.1 of Conrad-Stein "Component
        Groups of Purely Toric Quotients", one sees that the component group of an optimal
        quotient is the same as the component group of its dual (which is the subvariety).

        INPUT:

        - ``p`` -- a prime number

        OUTPUT: integer

        EXAMPLES::

            sage: A = J0(37)[1]
            sage: A.component_group_order(37)
            3
            sage: A = J0(43)[1]
            sage: A.component_group_order(37)
            1
            sage: A.component_group_order(43)
            7
            sage: A = J0(23)[0]
            sage: A.component_group_order(23)
            11
        '''
    def tamagawa_number(self, p):
        """
        Return the Tamagawa number of this abelian variety at p.

        NOTE: For bad primes, this is only implemented when the group
        if Gamma0 and p exactly divides the level and Atkin-Lehner
        acts diagonally on this abelian variety (e.g., if this variety
        is new and simple).  See the self.component_group command for
        more information.

        NOTE: the input abelian variety must be simple

        In cases where this function doesn't work, consider using the
        self.tamagawa_number_bounds functions.

        INPUT:

        - ``p`` -- a prime number

        OUTPUT: integer

        EXAMPLES::

            sage: A = J0(37)[1]
            sage: A.tamagawa_number(37)
            3
            sage: A = J0(43)[1]
            sage: A.tamagawa_number(37)
            1
            sage: A.tamagawa_number(43)
            7
            sage: A = J0(23)[0]
            sage: A.tamagawa_number(23)
            11
        """
    def tamagawa_number_bounds(self, p):
        """
        Return a divisor and multiple of the Tamagawa number of ``self`` at `p`.

        NOTE: the input abelian variety must be simple.

        INPUT:

        - ``p`` -- a prime number

        OUTPUT:

        - ``div`` -- integer; divisor of Tamagawa number at `p`
        - ``mul`` -- integer; multiple of Tamagawa number at `p`
        - ``mul_primes`` -- tuple; in case ``mul==0``, a list of all
          primes that can possibly divide the Tamagawa number at `p`

        EXAMPLES::

            sage: A = J0(63).new_subvariety()[1]; A
            Simple abelian subvariety 63b(1,63) of dimension 2 of J0(63)
            sage: A.tamagawa_number_bounds(7)
            (3, 3, ())
            sage: A.tamagawa_number_bounds(3)
            (1, 0, (2, 3, 5))
        """
    def brandt_module(self, p):
        """
        Return the Brandt module at p that corresponds to ``self``.  This
        is the factor of the vector space on the ideal class set in an
        order of level `N` in the quaternion algebra ramified at `p` and
        infinity.

        INPUT:

        - ``p`` -- prime that exactly divides the level

        OUTPUT: Brandt module space that corresponds to self

        EXAMPLES::

            sage: J0(43)[1].brandt_module(43)
            Subspace of dimension 2 of Brandt module of dimension 4 of level 43 of weight 2 over Rational Field
            sage: J0(43)[1].brandt_module(43).basis()
            ((1, 0, -1/2, -1/2), (0, 1, -1/2, -1/2))
            sage: J0(43)[0].brandt_module(43).basis()
            ((0, 0, 1, -1),)
            sage: J0(35)[0].brandt_module(5).basis()
            ((1, 0, -1, 0),)
            sage: J0(35)[0].brandt_module(7).basis()
            ((1, -1, 1, -1),)
        """

def sqrt_poly(f):
    """
    Return the square root of the polynomial `f`.

    .. NOTE::

        At some point something like this should be a member of the
        polynomial class. For now this is just used internally by some
        charpoly functions above.

    EXAMPLES::

        sage: R.<x> = QQ[]
        sage: f = (x-1)*(x+2)*(x^2 + 1/3*x + 5)
        sage: f
        x^4 + 4/3*x^3 + 10/3*x^2 + 13/3*x - 10
        sage: sage.modular.abvar.abvar.sqrt_poly(f^2)
        x^4 + 4/3*x^3 + 10/3*x^2 + 13/3*x - 10
        sage: sage.modular.abvar.abvar.sqrt_poly(f)
        Traceback (most recent call last):
        ...
        ValueError: f must be a perfect square
        sage: sage.modular.abvar.abvar.sqrt_poly(2*f^2)
        Traceback (most recent call last):
        ...
        ValueError: f must be monic
    """
def random_hecke_operator(M, t=None, p: int = 2):
    """
    Return a random Hecke operator acting on `M`, got by adding
    to `t` a random multiple of `T_p`

    INPUT:

    - ``M`` -- modular symbols space

    - ``t`` -- ``None`` or a Hecke operator

    - ``p`` -- a prime

    OUTPUT: Hecke operator prime

    EXAMPLES::

        sage: M = ModularSymbols(11).cuspidal_subspace()
        sage: t, p = sage.modular.abvar.abvar.random_hecke_operator(M)
        sage: p
        3
        sage: t, p = sage.modular.abvar.abvar.random_hecke_operator(M, t, p)
        sage: p
        5
    """
def factor_new_space(M):
    """
    Given a new space `M` of modular symbols, return the
    decomposition into simple of `M` under the Hecke
    operators.

    INPUT:

    - ``M`` -- modular symbols space

    OUTPUT: list of factors

    EXAMPLES::

        sage: M = ModularSymbols(37).cuspidal_subspace()
        sage: sage.modular.abvar.abvar.factor_new_space(M)
        [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field,
         Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(37) of weight 2 with sign 0 over Rational Field]
    """
def factor_modsym_space_new_factors(M):
    """
    Return the factorizations of all the new subspaces of `M`.

    INPUT:

    - ``M`` -- ambient modular symbols space

    OUTPUT: list of decompositions corresponding to each new space

    EXAMPLES::

        sage: M = ModularSymbols(33)
        sage: sage.modular.abvar.abvar.factor_modsym_space_new_factors(M)
        [[Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field],
         [Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field]]
    """
def simple_factorization_of_modsym_space(M, simple: bool = True):
    """
    Return the canonical factorization of `M` into (simple) subspaces.

    INPUT:

    - ``M`` -- ambient modular symbols space

    - ``simple`` -- boolean (default: ``True``); if set to ``False``,
      isogenous simple factors are grouped together

    OUTPUT: sequence

    EXAMPLES::

        sage: M = ModularSymbols(33)
        sage: sage.modular.abvar.abvar.simple_factorization_of_modsym_space(M)
        [(11,
          0,
          1,
          Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field),
         (11,
          0,
          3,
          Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field),
         (33,
          0,
          1,
          Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field)]
        sage: sage.modular.abvar.abvar.simple_factorization_of_modsym_space(M, simple=False)
        [(11,
          0,
          None,
          Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field),
         (33,
          0,
          None,
          Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field)]

    TESTS:

    Check that :issue:`21799` is fixed::

        sage: JH(28, [15]).decomposition()
        [Simple abelian subvariety 14aGH[15](1,28) of dimension 1 of JH(28,[15]),
         Simple abelian subvariety 14aGH[15](2,28) of dimension 1 of JH(28,[15]),
         Simple abelian subvariety 28aGH[15](1,28) of dimension 2 of JH(28,[15])]
    """
def modsym_lattices(M, factors):
    """
    Append lattice information to the output of
    simple_factorization_of_modsym_space.

    INPUT:

    - ``M`` -- modular symbols spaces

    - ``factors`` -- sequence (simple_factorization_of_modsym_space)

    OUTPUT: sequence with more information for each factor (the
    lattice)

    EXAMPLES::

        sage: M = ModularSymbols(33)
        sage: factors = sage.modular.abvar.abvar.simple_factorization_of_modsym_space(M, simple=False)
        sage: sage.modular.abvar.abvar.modsym_lattices(M, factors)
        [(11,
          0,
          None,
          Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field,
          Free module of degree 6 and rank 4 over Integer Ring
          Echelon basis matrix:
          [ 1  0  0  0 -1  2]
          [ 0  1  0  0 -1  1]
          [ 0  0  1  0 -2  2]
          [ 0  0  0  1 -1 -1]),
         (33,
          0,
          None,
          Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 9 for Gamma_0(33) of weight 2 with sign 0 over Rational Field,
          Free module of degree 6 and rank 2 over Integer Ring
          Echelon basis matrix:
          [ 1  0  0 -1  0  0]
          [ 0  0  1  0  1 -1])]
    """
