from .finite_subgroup import FiniteSubgroup as FiniteSubgroup
from sage.arith.misc import divisors as divisors, gcd as gcd
from sage.misc.misc_c import prod as prod
from sage.modular.abvar.torsion_point import TorsionPoint as TorsionPoint
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_class as Gamma0_class
from sage.modular.arithgroup.congroup_gamma1 import Gamma1_class as Gamma1_class
from sage.modular.dirichlet import DirichletGroup as DirichletGroup
from sage.modules.module import Module as Module
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.primes import Primes as Primes
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method

class RationalTorsionSubgroup(FiniteSubgroup):
    """
    The torsion subgroup of a modular abelian variety.
    """
    def __init__(self, abvar) -> None:
        """
        Create the torsion subgroup.

        INPUT:

        - ``abvar`` -- a modular abelian variety

        EXAMPLES::

            sage: T = J0(14).rational_torsion_subgroup(); T
            Torsion subgroup of Abelian variety J0(14) of dimension 1
            sage: type(T)
            <class 'sage.modular.abvar.torsion_subgroup.RationalTorsionSubgroup_with_category'>
        """
    def __richcmp__(self, other, op):
        """
        Compare torsion subgroups.

        INPUT:

        - ``other`` -- an object

        If other is a torsion subgroup, the abelian varieties are compared.
        Otherwise, the generic behavior for finite abelian variety
        subgroups is used.

        EXAMPLES::

            sage: G = J0(11).rational_torsion_subgroup(); H = J0(13).rational_torsion_subgroup()
            sage: G == G
            True
            sage: G < H   # since 11 < 13
            True
            sage: G > H
            False
        """
    def order(self, proof: bool = True):
        """
        Return the order of the torsion subgroup of this modular abelian
        variety.

        This function may fail if the multiple obtained by counting points
        modulo `p` exceeds the divisor obtained from the rational cuspidal
        subgroup.

        The computation of the rational torsion order of J1(p) is conjectural
        and will only be used if ``proof=False``. See Section 6.2.3 of [CES2003]_.

        INPUT:

        - ``proof`` -- boolean (default: ``True``)

        OUTPUT: the order of this torsion subgroup

        EXAMPLES::

            sage: A = J0(11)
            sage: A.rational_torsion_subgroup().order()
            5
            sage: A = J0(23)
            sage: A.rational_torsion_subgroup().order()
            11
            sage: T = J0(37)[1].rational_torsion_subgroup()
            sage: T.order()
            3

            sage: J = J1(13)
            sage: J.rational_torsion_subgroup().order()
            19

        Sometimes the order can only be computed with ``proof=False``. ::

            sage: J = J1(23)
            sage: J.rational_torsion_subgroup().order()
            Traceback (most recent call last):
            ...
            RuntimeError: Unable to compute order of torsion subgroup
            (it is in [408991, 9406793])

            sage: J.rational_torsion_subgroup().order(proof=False)
            408991
        """
    def lattice(self):
        """
        Return lattice that defines this torsion subgroup, if possible.

        .. warning::

           There is no known algorithm in general to compute the
           rational torsion subgroup. Use rational_cusp_group to
           obtain a subgroup of the rational torsion subgroup in
           general.

        EXAMPLES::

            sage: J0(11).rational_torsion_subgroup().lattice()
            Free module of degree 2 and rank 2 over Integer Ring
            Echelon basis matrix:
            [  1   0]
            [  0 1/5]

        The following fails because in fact I know of no (reasonable)
        algorithm to provably compute the torsion subgroup in general.

        ::

            sage: T = J0(33).rational_torsion_subgroup()
            sage: T.lattice()
            Traceback (most recent call last):
            ...
            NotImplementedError: unable to compute the rational torsion subgroup
            in this case (there is no known general algorithm yet)

        The problem is that the multiple of the order obtained by counting
        points over finite fields is twice the divisor of the order got
        from the rational cuspidal subgroup.

        ::

            sage: T.multiple_of_order(30)
            200
            sage: J0(33).rational_cusp_subgroup().order()
            100
        """
    def possible_orders(self, proof: bool = True):
        """
        Return the possible orders of this torsion subgroup. Outside of special
        cases, this is done by computing a divisor and multiple of the order.

        INPUT:

        - ``proof`` -- boolean (default: ``True``)

        OUTPUT: an array of positive integers

        The computation of the rational torsion order of J1(p) is conjectural
        and will only be used if ``proof=False``. See Section 6.2.3 of [CES2003]_.

        EXAMPLES::

            sage: J0(11).rational_torsion_subgroup().possible_orders()
            [5]
            sage: J0(33).rational_torsion_subgroup().possible_orders()
            [100, 200]

            sage: J1(13).rational_torsion_subgroup().possible_orders()
            [19]
            sage: J1(16).rational_torsion_subgroup().possible_orders()
            [1, 2, 4, 5, 10, 20]
        """
    def divisor_of_order(self):
        """
        Return a divisor of the order of this torsion subgroup of a modular
        abelian variety.

        OUTPUT: a divisor of this torsion subgroup

        EXAMPLES::

            sage: t = J0(37)[1].rational_torsion_subgroup()
            sage: t.divisor_of_order()
            3

            sage: J = J1(19)
            sage: J.rational_torsion_subgroup().divisor_of_order()
            4383

            sage: J = J0(45)
            sage: J.rational_cusp_subgroup().order()
            32
            sage: J.rational_cuspidal_subgroup().order()
            64
            sage: J.rational_torsion_subgroup().divisor_of_order()
            64
        """
    def multiple_of_order(self, maxp=None, proof: bool = True):
        """
        Return a multiple of the order.

        INPUT:

        - ``proof`` -- boolean (default: ``True``)

        The computation of the rational torsion order of J1(p) is conjectural
        and will only be used if proof=False. See Section 6.2.3 of [CES2003]_.

        EXAMPLES::

            sage: J = J1(11); J
            Abelian variety J1(11) of dimension 1
            sage: J.rational_torsion_subgroup().multiple_of_order()
            5

            sage: J = J0(17)
            sage: J.rational_torsion_subgroup().order()
            4

        This is an example where proof=False leads to a better bound and better
        performance. ::

            sage: J = J1(23)
            sage: J.rational_torsion_subgroup().multiple_of_order()  # long time (2s)
            9406793
            sage: J.rational_torsion_subgroup().multiple_of_order(proof=False)
            408991
        """
    def multiple_of_order_using_frobp(self, maxp=None):
        """
        Return a multiple of the order of this torsion group.

        In the `Gamma_0` case, the multiple is computed using characteristic
        polynomials of Hecke operators of odd index not dividing the level. In
        the `Gamma_1` case, the multiple is computed by expressing the
        frobenius polynomial in terms of the characteristic polynomial of left
        multiplication by `a_p` for odd primes p not dividing the level.

        INPUT:

        - ``maxp`` -- (default: ``None``) if ``maxp`` is ``None``, return gcd
          of best bound computed so far with bound obtained by computing GCD's
          of orders modulo `p` until this gcd stabilizes for 3 successive
          primes. If ``maxp`` is given, just use all primes up to and including
          ``maxp``.

        EXAMPLES::

            sage: J = J0(11)
            sage: G = J.rational_torsion_subgroup()
            sage: G.multiple_of_order_using_frobp(11)
            5

        Increasing maxp may yield a tighter bound. If maxp=None, then Sage
        will use more primes until the multiple stabilizes for 3 successive
        primes.  ::

            sage: J = J0(389)
            sage: G = J.rational_torsion_subgroup(); G
            Torsion subgroup of Abelian variety J0(389) of dimension 32
            sage: G.multiple_of_order_using_frobp()
            97
            sage: [G.multiple_of_order_using_frobp(p) for p in prime_range(3,11)]
            [92645296242160800, 7275, 291]
            sage: [G.multiple_of_order_using_frobp(p) for p in prime_range(3,13)]
            [92645296242160800, 7275, 291, 97]
            sage: [G.multiple_of_order_using_frobp(p) for p in prime_range(3,19)]
            [92645296242160800, 7275, 291, 97, 97, 97]

        We can compute the multiple of order of the torsion subgroup for Gamma0
        and Gamma1 varieties, and their products. ::

            sage: A = J0(11) * J0(33)
            sage: A.rational_torsion_subgroup().multiple_of_order_using_frobp()
            1000

            sage: A = J1(23)
            sage: A.rational_torsion_subgroup().multiple_of_order_using_frobp()
            9406793
            sage: A.rational_torsion_subgroup().multiple_of_order_using_frobp(maxp=50)
            408991

            sage: A = J1(19) * J0(21)
            sage: A.rational_torsion_subgroup().multiple_of_order_using_frobp()
            35064

        The next example illustrates calling this function with a larger
        input and how the result may be cached when maxp is None::

            sage: T = J0(43)[1].rational_torsion_subgroup()
            sage: T.multiple_of_order_using_frobp()
            14
            sage: T.multiple_of_order_using_frobp(50)
            7
            sage: T.multiple_of_order_using_frobp()
            7

        This function is not implemented for general congruence subgroups
        unless the dimension is zero. ::

            sage: A = JH(13,[2]); A
            Abelian variety J0(13) of dimension 0
            sage: A.rational_torsion_subgroup().multiple_of_order_using_frobp()
            1

            sage: A = JH(15, [2]); A
            Abelian variety JH(15,[2]) of dimension 1
            sage: A.rational_torsion_subgroup().multiple_of_order_using_frobp()
            Traceback (most recent call last):
            ...
            NotImplementedError: torsion multiple only implemented for Gamma0 and Gamma1
        """

class QQbarTorsionSubgroup(Module):
    Element = TorsionPoint
    def __init__(self, abvar) -> None:
        """
        Group of all torsion points over the algebraic closure on an
        abelian variety.

        INPUT:

        - ``abvar`` -- an abelian variety

        EXAMPLES::

            sage: A = J0(23)
            sage: A.qbar_torsion_subgroup()                                             # needs sage.rings.number_field
            Group of all torsion points in QQbar on Abelian variety J0(23) of dimension 2
        """
    def field_of_definition(self):
        """
        Return the field of definition of this subgroup. Since this is the
        group of all torsion it is defined over the base field of this
        abelian variety.

        OUTPUT: a field

        EXAMPLES::

            sage: J0(23).qbar_torsion_subgroup().field_of_definition()                  # needs sage.rings.number_field
            Rational Field
        """
    def abelian_variety(self):
        """
        Return the abelian variety that this is the set of all torsion
        points on.

        OUTPUT: abelian variety

        EXAMPLES::

            sage: J0(23).qbar_torsion_subgroup().abelian_variety()                      # needs sage.rings.number_field
            Abelian variety J0(23) of dimension 2
        """
