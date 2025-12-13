from _typeshed import Incomplete
from sage.arith.misc import divisors as divisors
from sage.categories.sets_cat import Sets as Sets
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modular.dirichlet import DirichletGroup as DirichletGroup, trivial_character as trivial_character
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp

def WeightSpace_constructor(p, base_ring=None):
    '''
    Construct the `p`-adic weight space for the given prime p.

    A `p`-adic weight
    is a continuous character `\\ZZ_p^\\times \\to \\CC_p^\\times`.
    These are the `\\CC_p`-points of a rigid space over `\\QQ_p`,
    which is isomorphic to a disjoint union of copies (indexed by
    `(\\ZZ/p\\ZZ)^\\times`) of the open unit `p`-adic disc.

    Note that the "base ring" of a `p`-adic weight is the smallest ring
    containing the image of `\\ZZ`; in particular, although the default base
    ring is `\\QQ_p`, base ring `\\QQ` will also work.

    EXAMPLES::

        sage: pAdicWeightSpace(3) # indirect doctest
        Space of 3-adic weight-characters
         defined over 3-adic Field with capped relative precision 20
        sage: pAdicWeightSpace(3, QQ)
        Space of 3-adic weight-characters defined over Rational Field
        sage: pAdicWeightSpace(10)
        Traceback (most recent call last):
        ...
        ValueError: p must be prime
    '''

class WeightSpace_class(Parent):
    """
    The space of `p`-adic weight-characters `\\mathcal{W} = {\\rm
    Hom}(\\ZZ_p^\\times, \\CC_p^\\times)`.

    This is isomorphic to a
    disjoint union of `(p-1)` open discs of radius 1 (or 2 such discs if `p =
    2`), with the parameter on the open disc corresponding to the image of `1 +
    p` (or 5 if `p = 2`)

    TESTS::

        sage: W = pAdicWeightSpace(3)
        sage: W is loads(dumps(W))
        True
    """
    def __init__(self, p, base_ring) -> None:
        """
        Initialisation function.

        EXAMPLES::

            sage: pAdicWeightSpace(17)
            Space of 17-adic weight-characters defined over 17-adic Field with capped relative precision 20
        """
    def __reduce__(self):
        """
        Used for pickling.

        EXAMPLES::

            sage: pAdicWeightSpace(3).__reduce__()
            (<function WeightSpace_constructor at ...>, (3, 3-adic Field with capped relative precision 20))
        """
    @cached_method
    def zero(self):
        """
        Return the zero of this weight space.

        EXAMPLES::

            sage: W = pAdicWeightSpace(17)
            sage: W.zero()
            0
        """
    def prime(self):
        """
        Return the prime `p` such that this is a `p`-adic weight space.

        EXAMPLES::

            sage: pAdicWeightSpace(17).prime()
            17
        """
    def base_extend(self, R):
        """
        Extend scalars to the ring R.

        There must be a canonical coercion map from the present base ring to R.

        EXAMPLES::

            sage: W = pAdicWeightSpace(3, QQ)
            sage: W.base_extend(Qp(3))
            Space of 3-adic weight-characters
             defined over 3-adic Field with capped relative precision 20
            sage: W.base_extend(IntegerModRing(12))
            Traceback (most recent call last):
            ...
            TypeError: No coercion map from 'Rational Field'
            to 'Ring of integers modulo 12' is defined
        """

class WeightCharacter(Element):
    """
    Abstract base class representing an element of the `p`-adic weight space
    `Hom(\\ZZ_p^\\times, \\CC_p^\\times)`.
    """
    def __init__(self, parent) -> None:
        """
        Initialisation function.

        EXAMPLES::

            sage: pAdicWeightSpace(17)(0)
            0
        """
    def base_extend(self, R):
        """
        Extend scalars to the base ring R.

        The ring R must have a canonical map from the current base ring.

        EXAMPLES::

            sage: w = pAdicWeightSpace(17, QQ)(3)
            sage: w.base_extend(Qp(17))
            3
        """
    def is_even(self) -> bool:
        """
        Return ``True`` if this weight-character sends -1 to +1.

        EXAMPLES::

            sage: pAdicWeightSpace(17)(0).is_even()
            True
            sage: pAdicWeightSpace(17)(11).is_even()
            False
            sage: pAdicWeightSpace(17)(1 + 17 + O(17^20), 3, False).is_even()
            False
            sage: pAdicWeightSpace(17)(1 + 17 + O(17^20), 4, False).is_even()
            True
        """
    def pAdicEisensteinSeries(self, ring, prec: int = 20):
        """
        Calculate the `q`-expansion of the `p`-adic Eisenstein series of given
        weight-character, normalised so the constant term is 1.

        EXAMPLES::

            sage: kappa = pAdicWeightSpace(3)(3, DirichletGroup(3,QQ).0)
            sage: kappa.pAdicEisensteinSeries(QQ[['q']], 20)
            1 - 9*q + 27*q^2 - 9*q^3 - 117*q^4 + 216*q^5 + 27*q^6 - 450*q^7 + 459*q^8
             - 9*q^9 - 648*q^10 + 1080*q^11 - 117*q^12 - 1530*q^13 + 1350*q^14 + 216*q^15
             - 1845*q^16 + 2592*q^17 + 27*q^18 - 3258*q^19 + O(q^20)
        """
    def values_on_gens(self):
        """
        If `\\kappa` is this character, calculate the values `(\\kappa(r), t)`
        where `r` is `1 + p` (or 5 if `p = 2`) and `t` is the unique element of
        `\\ZZ/(p-1)\\ZZ` such that `\\kappa(\\mu) = \\mu^t` for `\\mu`
        a (p-1)st root of unity. (If `p = 2`, we take `t` to be 0 or 1
        according to whether `\\kappa` is odd or even.) These two values
        uniquely determine the character `\\kappa`.

        EXAMPLES::

            sage: W = pAdicWeightSpace(11); W(2).values_on_gens()
            (1 + 2*11 + 11^2 + O(11^20), 2)
            sage: W(2, DirichletGroup(11, QQ).0).values_on_gens()
            (1 + 2*11 + 11^2 + O(11^20), 7)
            sage: W(1 + 2*11 + O(11^5), 4, algebraic = False).values_on_gens()
            (1 + 2*11 + O(11^5), 4)
        """
    def is_trivial(self) -> bool:
        """
        Return ``True`` if and only if this is the trivial character.

        EXAMPLES::

            sage: pAdicWeightSpace(11)(2).is_trivial()
            False
            sage: pAdicWeightSpace(11)(2, DirichletGroup(11, QQ).0).is_trivial()
            False
            sage: pAdicWeightSpace(11)(0).is_trivial()
            True
        """
    def Lvalue(self) -> None:
        """
        Return the value of the `p`-adic `L`-function of `\\QQ`, which can be
        regarded as a rigid-analytic function on weight space, evaluated at
        this character.

        EXAMPLES::

            sage: W = pAdicWeightSpace(11)
            sage: sage.modular.overconvergent.weightspace.WeightCharacter(W).Lvalue()
            Traceback (most recent call last):
            ...
            NotImplementedError
        """
    def one_over_Lvalue(self):
        """
        Return the reciprocal of the `p`-adic `L`-function evaluated at this
        weight-character.

        If the weight-character is odd, then the `L`-function
        is zero, so an error will be raised.

        EXAMPLES::

            sage: pAdicWeightSpace(11)(4).one_over_Lvalue()
            -12/133
            sage: pAdicWeightSpace(11)(3, DirichletGroup(11, QQ).0).one_over_Lvalue()
            -1/6
            sage: pAdicWeightSpace(11)(3).one_over_Lvalue()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
            sage: pAdicWeightSpace(11)(0).one_over_Lvalue()
            0
            sage: type(_)
            <class 'sage.rings.integer.Integer'>
        """

class AlgebraicWeight(WeightCharacter):
    """
    A point in weight space corresponding to a locally algebraic character, of
    the form `x \\mapsto \\chi(x) x^k` where `k` is an integer and `\\chi` is a
    Dirichlet character modulo `p^n` for some `n`.

    TESTS::

        sage: w = pAdicWeightSpace(23)(12, DirichletGroup(23, QQ).0) # exact
        sage: w == loads(dumps(w))
        True
        sage: w = pAdicWeightSpace(23)(12, DirichletGroup(23, Qp(23)).0) # inexact
        sage: w == loads(dumps(w))
        True
        sage: w is loads(dumps(w)) # elements are not globally unique
        False
    """
    def __init__(self, parent, k, chi=None) -> None:
        """
        Create a locally algebraic weight-character.

        EXAMPLES::

            sage: pAdicWeightSpace(29)(13, DirichletGroup(29, Qp(29)).0)
            (13, 29, [2 + 2*29 + ... + O(29^20)])
        """
    def __call__(self, x):
        """
        Evaluate this character at an element of `\\ZZ_p^\\times`.

        EXAMPLES:

        Exact answers are returned when this is possible::

            sage: kappa = pAdicWeightSpace(29)(13, DirichletGroup(29, QQ).0)
            sage: kappa(1)
            1
            sage: kappa(0)
            0
            sage: kappa(12)
            -106993205379072
            sage: kappa(-1)
            -1
            sage: kappa(13 + 4*29 + 11*29^2 + O(29^3))
            9 + 21*29 + 27*29^2 + O(29^3)

        When the character chi is defined over a `p`-adic field, the results returned are inexact::

            sage: kappa = pAdicWeightSpace(29)(13, DirichletGroup(29, Qp(29)).0^14)
            sage: kappa(1)
            1 + O(29^20)
            sage: kappa(0)
            0
            sage: kappa(12)
            17 + 11*29 + 7*29^2 + 4*29^3 + 5*29^4 + 2*29^5 + 13*29^6 + 3*29^7 + 18*29^8 + 21*29^9 + 28*29^10 + 28*29^11 + 28*29^12 + 28*29^13 + 28*29^14 + 28*29^15 + 28*29^16 + 28*29^17 + 28*29^18 + 28*29^19 + O(29^20)
            sage: kappa(12) == -106993205379072
            True
            sage: kappa(-1) == -1
            True
            sage: kappa(13 + 4*29 + 11*29^2 + O(29^3))
            9 + 21*29 + 27*29^2 + O(29^3)
        """
    def k(self):
        """
        If this character is `x \\mapsto x^k \\chi(x)` for an integer `k` and a
        Dirichlet character `\\chi`, return `k`.

        EXAMPLES::

            sage: kappa = pAdicWeightSpace(29)(13, DirichletGroup(29, Qp(29)).0^14)
            sage: kappa.k()
            13
        """
    def chi(self):
        """
        If this character is `x \\mapsto x^k \\chi(x)` for an integer `k` and a
        Dirichlet character `\\chi`, return `\\chi`.

        EXAMPLES::

            sage: kappa = pAdicWeightSpace(29)(13, DirichletGroup(29, Qp(29)).0^14)
            sage: kappa.chi()
            Dirichlet character modulo 29 of conductor 29
             mapping 2 |--> 28 + 28*29 + 28*29^2 + ... + O(29^20)
        """
    def __hash__(self):
        """
        TESTS::

            sage: w = pAdicWeightSpace(23)(12, DirichletGroup(23, QQ).0)
            sage: hash(w) == hash((12, 23, (-1,)))
            True
        """
    def teichmuller_type(self):
        """
        Return the Teichmuller type of this weight-character `\\kappa`.

        This is the unique `t \\in \\ZZ/(p-1)\\ZZ` such that `\\kappa(\\mu)
        = \\mu^t` for `\\mu` a `(p-1)`-st root of 1.

        For `p = 2` this does not make sense, but we still want the Teichmuller
        type to correspond to the index of the component of weight space in
        which `\\kappa` lies, so we return 1 if `\\kappa` is odd and 0 otherwise.

        EXAMPLES::

            sage: pAdicWeightSpace(11)(2, DirichletGroup(11,QQ).0).teichmuller_type()
            7
            sage: pAdicWeightSpace(29)(13, DirichletGroup(29, Qp(29)).0).teichmuller_type()
            14
            sage: pAdicWeightSpace(2)(3, DirichletGroup(4,QQ).0).teichmuller_type()
            0
        """
    def Lvalue(self):
        """
        Return the value of the `p`-adic `L`-function of `\\QQ` evaluated at
        this weight-character.

        If the character is `x \\mapsto x^k \\chi(x)`
        where `k > 0` and `\\chi` has conductor a power of `p`, this is an
        element of the number field generated by the values of `\\chi`, equal to
        the value of the complex `L`-function `L(1-k, \\chi)`. If `\\chi` is
        trivial, it is equal to `(1 - p^{k-1})\\zeta(1-k)`.

        At present this is not implemented in any other cases, except the
        trivial character (for which the value is `\\infty`).

        .. TODO::

            Implement this more generally using the Amice transform
            machinery in
            sage/schemes/elliptic_curves/padic_lseries.py, which
            should clearly be factored out into a separate class.

        EXAMPLES::

            sage: pAdicWeightSpace(7)(4).Lvalue() == (1 - 7^3)*zeta__exact(-3)
            True
            sage: pAdicWeightSpace(7)(5, DirichletGroup(7, Qp(7)).0^4).Lvalue()
            0
            sage: pAdicWeightSpace(7)(6, DirichletGroup(7, Qp(7)).0^4).Lvalue()
            1 + 2*7 + 7^2 + 3*7^3 + 3*7^5 + 4*7^6 + 2*7^7 + 5*7^8 + 2*7^9 + 3*7^10 + 6*7^11
             + 2*7^12 + 3*7^13 + 5*7^14 + 6*7^15 + 5*7^16 + 3*7^17 + 6*7^18 + O(7^19)
        """

class ArbitraryWeight(WeightCharacter):
    t: Incomplete
    w: Incomplete
    def __init__(self, parent, w, t) -> None:
        """
        Create the element of `p`-adic weight space in the given component
        mapping 1 + p to w.

        Here w must be an element of a `p`-adic field, with finite
        precision.

        EXAMPLES::

            sage: pAdicWeightSpace(17)(1 + 17^2 + O(17^3), 11, False)
            [1 + 17^2 + O(17^3), 11]
        """
    def __call__(self, x):
        """
        Evaluate this character at an element of `\\ZZ_p^\\times`.

        EXAMPLES::

            sage: kappa = pAdicWeightSpace(23)(1 + 23^2 + O(23^20), 4, False)
            sage: kappa(2)
            16 + 7*23 + 7*23^2 + 16*23^3 + 23^4 + 20*23^5 + 15*23^7 + 11*23^8 + 12*23^9 + 8*23^10 + 22*23^11 + 16*23^12 + 13*23^13 + 4*23^14 + 19*23^15 + 6*23^16 + 7*23^17 + 11*23^19 + O(23^20)
            sage: kappa(-1)
            1 + O(23^20)
            sage: kappa(23)
            0
            sage: kappa(2 + 2*23 + 11*23^2 + O(23^3))
            16 + 7*23 + O(23^3)
        """
    def teichmuller_type(self):
        """
        Return the Teichmuller type of this weight-character `\\kappa`.

        This is
        the unique `t \\in \\ZZ/(p-1)\\ZZ` such that `\\kappa(\\mu) =
        \\mu^t` for \\mu a `(p-1)`-st root of 1.

        For `p = 2` this does not make sense, but we still want the Teichmuller
        type to correspond to the index of the component of weight space in
        which `\\kappa` lies, so we return 1 if `\\kappa` is odd and 0 otherwise.

        EXAMPLES::

            sage: pAdicWeightSpace(17)(1 + 3*17 + 2*17^2 + O(17^3), 8, False).teichmuller_type()
            8
            sage: pAdicWeightSpace(2)(1 + 2 + O(2^2), 1, False).teichmuller_type()
            1
        """
