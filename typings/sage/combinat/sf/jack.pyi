from . import sfa as sfa
from _typeshed import Incomplete
from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.categories.homset import End as End, Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.fraction_field import FractionField as FractionField, FractionField_generic as FractionField_generic
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

QQt: Incomplete
p_to_m_cache: Incomplete
m_to_p_cache: Incomplete

class Jack(UniqueRepresentation):
    @staticmethod
    def __classcall__(cls, Sym, t: str = 't'):
        """
        Normalize the arguments.

        TESTS::

            sage: R.<q, t> = QQ[]
            sage: B1 = SymmetricFunctions(R).jack().P()
            sage: B2 = SymmetricFunctions(R).jack(t).P()
            sage: B3 = SymmetricFunctions(R).jack(q).P()
            sage: B1 is B2
            True
            sage: B1 == B3
            False
        """
    t: Incomplete
    def __init__(self, Sym, t) -> None:
        """
        The family of Jack symmetric functions including the `P`, `Q`, `J`, `Qp`
        bases.  The default parameter is ``t``.

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases
        - ``Sym`` -- a ring of symmetric functions
        - ``t`` -- an optional parameter (default: ``'t'``)

        EXAMPLES::

            sage: SymmetricFunctions(FractionField(QQ['t'])).jack()
            Jack polynomials over Fraction Field of Univariate Polynomial Ring in t over Rational Field
            sage: SymmetricFunctions(QQ).jack(1)
            Jack polynomials with t=1 over Rational Field
        """
    def base_ring(self):
        """
        Return the base ring of the symmetric functions in which the
        Jack symmetric functions live.

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases

        OUTPUT: the base ring of the symmetric functions ring of ``self``

        EXAMPLES::

            sage: J2 = SymmetricFunctions(QQ).jack(t=2)
            sage: J2.base_ring()
            Rational Field
        """
    def symmetric_function_ring(self):
        """
        Return the base ring of the symmetric functions of the Jack symmetric
        function bases

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases

        OUTPUT: the symmetric functions ring of ``self``

        EXAMPLES::

            sage: Jacks = SymmetricFunctions(FractionField(QQ['t'])).jack()
            sage: Jacks.symmetric_function_ring()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def P(self):
        """
        Return the algebra of Jack polynomials in the `P` basis.

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases

        OUTPUT: the `P` basis of the Jack symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JP = Sym.jack().P(); JP
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Jack P basis
            sage: Sym.jack(t=-1).P()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Jack P with t=-1 basis

        At `t = 1`, the Jack polynomials in the `P` basis are the Schur
        symmetric functions.

        ::

            sage: Sym = SymmetricFunctions(QQ)
            sage: JP = Sym.jack(t=1).P()
            sage: s = Sym.schur()
            sage: s(JP([2,2,1]))
            s[2, 2, 1]
            sage: JP(s([2,2,1]))
            JackP[2, 2, 1]
            sage: JP([2,1])^2
            JackP[2, 2, 1, 1] + JackP[2, 2, 2] + JackP[3, 1, 1, 1] + 2*JackP[3, 2, 1] + JackP[3, 3] + JackP[4, 1, 1] + JackP[4, 2]

        At `t = 2`, the Jack polynomials in the `P` basis are the zonal
        polynomials.

        ::

            sage: Sym = SymmetricFunctions(QQ)
            sage: JP = Sym.jack(t=2).P()
            sage: Z = Sym.zonal()
            sage: Z(JP([2,2,1]))
            Z[2, 2, 1]
            sage: JP(Z[2, 2, 1])
            JackP[2, 2, 1]
            sage: JP([2])^2
            64/45*JackP[2, 2] + 16/21*JackP[3, 1] + JackP[4]
            sage: Z([2])^2
            64/45*Z[2, 2] + 16/21*Z[3, 1] + Z[4]

        ::

            sage: Sym = SymmetricFunctions(QQ['a','b'].fraction_field())
            sage: (a,b) = Sym.base_ring().gens()
            sage: Jacka = Sym.jack(t=a)
            sage: Jackb = Sym.jack(t=b)
            sage: m = Sym.monomial()
            sage: JPa = Jacka.P()
            sage: JPb = Jackb.P()
            sage: m(JPa[2,1])
            (6/(a+2))*m[1, 1, 1] + m[2, 1]
            sage: m(JPb[2,1])
            (6/(b+2))*m[1, 1, 1] + m[2, 1]
            sage: m(a*JPb([2,1]) + b*JPa([2,1]))
            ((6*a^2+6*b^2+12*a+12*b)/(a*b+2*a+2*b+4))*m[1, 1, 1] + (a+b)*m[2, 1]
            sage: JPa(JPb([2,1]))
            ((6*a-6*b)/(a*b+2*a+2*b+4))*JackP[1, 1, 1] + JackP[2, 1]

        ::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JQ = Sym.jack().Q()
            sage: JP = Sym.jack().P()
            sage: JJ = Sym.jack().J()

        ::

            sage: JP(JQ([2,1]))
            ((1/2*t+1)/(t^3+1/2*t^2))*JackP[2, 1]
            sage: JP(JQ([3]))
            ((1/3*t^2+1/2*t+1/6)/t^3)*JackP[3]
            sage: JP(JQ([1,1,1]))
            (6/(t^3+3*t^2+2*t))*JackP[1, 1, 1]

        ::

            sage: JP(JJ([3]))
            (2*t^2+3*t+1)*JackP[3]
            sage: JP(JJ([2,1]))
            (t+2)*JackP[2, 1]
            sage: JP(JJ([1,1,1]))
            6*JackP[1, 1, 1]

        ::

            sage: s = Sym.schur()
            sage: JP(s([2,1]))
            ((2*t-2)/(t+2))*JackP[1, 1, 1] + JackP[2, 1]
            sage: s(_)
            s[2, 1]
        """
    def Q(self):
        """
        Return the algebra of Jack polynomials in the `Q` basis.

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases

        OUTPUT: the `Q` basis of the Jack symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JQ = Sym.jack().Q(); JQ
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Jack Q basis
            sage: Sym = SymmetricFunctions(QQ)
            sage: Sym.jack(t=-1).Q()
            Symmetric Functions over Rational Field in the Jack Q with t=-1 basis

        ::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JQ = Sym.jack().Q()
            sage: JP = Sym.jack().P()
            sage: JQ(sum(JP(p) for p in Partitions(3)))
            (1/6*t^3+1/2*t^2+1/3*t)*JackQ[1, 1, 1] + ((2*t^3+t^2)/(t+2))*JackQ[2, 1] + (3*t^3/(t^2+3/2*t+1/2))*JackQ[3]

        ::

            sage: s = Sym.schur()
            sage: JQ(s([3])) # indirect doctest
            (1/6*t^3-1/2*t^2+1/3*t)*JackQ[1, 1, 1] + ((2*t^3-2*t^2)/(t+2))*JackQ[2, 1] + (3*t^3/(t^2+3/2*t+1/2))*JackQ[3]
            sage: JQ(s([2,1]))
            (1/3*t^3-1/3*t)*JackQ[1, 1, 1] + ((2*t^3+t^2)/(t+2))*JackQ[2, 1]
            sage: JQ(s([1,1,1]))
            (1/6*t^3+1/2*t^2+1/3*t)*JackQ[1, 1, 1]
        """
    def J(self):
        """
        Return the algebra of Jack polynomials in the `J` basis.

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases

        OUTPUT: the `J` basis of the Jack symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JJ = Sym.jack().J(); JJ
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Jack J basis
            sage: Sym = SymmetricFunctions(QQ)
            sage: Sym.jack(t=-1).J()
            Symmetric Functions over Rational Field in the Jack J with t=-1 basis

        At `t = 1`, the Jack polynomials in the `J` basis are scalar multiples
        of the Schur functions with the scalar given by a Partition's
        :meth:`~sage.combinat.partition.Partition.hook_product` method at 1::

            sage: Sym = SymmetricFunctions(QQ)
            sage: JJ = Sym.jack(t=1).J()
            sage: s = Sym.schur()
            sage: p = Partition([3,2,1,1])
            sage: s(JJ(p)) == p.hook_product(1)*s(p)  # long time (4s on sage.math, 2012)
            True

        At `t = 2`, the Jack polynomials in the `J` basis are scalar multiples
        of the zonal polynomials with the scalar given by a Partition's
        :meth:`~sage.combinat.partition.Partition.hook_product` method at 2.

        ::

            sage: Sym = SymmetricFunctions(QQ)
            sage: JJ = Sym.jack(t=2).J()
            sage: Z = Sym.zonal()
            sage: p = Partition([2,2,1])
            sage: Z(JJ(p)) == p.hook_product(2)*Z(p)
            True

        ::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JJ = Sym.jack().J()
            sage: JP = Sym.jack().P()
            sage: JJ(sum(JP(p) for p in Partitions(3)))
            1/6*JackJ[1, 1, 1] + (1/(t+2))*JackJ[2, 1] + (1/2/(t^2+3/2*t+1/2))*JackJ[3]

        ::

            sage: s = Sym.schur()
            sage: JJ(s([3])) # indirect doctest
            ((1/6*t^2-1/2*t+1/3)/(t^2+3*t+2))*JackJ[1, 1, 1] + ((t-1)/(t^2+5/2*t+1))*JackJ[2, 1] + (1/2/(t^2+3/2*t+1/2))*JackJ[3]
            sage: JJ(s([2,1]))
            ((1/3*t-1/3)/(t+2))*JackJ[1, 1, 1] + (1/(t+2))*JackJ[2, 1]
            sage: JJ(s([1,1,1]))
            1/6*JackJ[1, 1, 1]
        """
    def Qp(self):
        """
        Return the algebra of Jack polynomials in the `Qp`, which is dual to
        the `P` basis with respect to the standard scalar product.

        INPUT:

        - ``self`` -- the family of Jack symmetric function bases

        OUTPUT: the `Q'` basis of the Jack symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JP = Sym.jack().P()
            sage: JQp = Sym.jack().Qp(); JQp
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Jack Qp basis
            sage: a = JQp([2])
            sage: a.scalar(JP([2]))
            1
            sage: a.scalar(JP([1,1]))
            0
            sage: JP(JQp([2]))                        # todo: missing auto normalization
            ((t-1)/(t+1))*JackP[1, 1] + JackP[2]
            sage: JP._normalize(JP(JQp([2])))
            ((t-1)/(t+1))*JackP[1, 1] + JackP[2]
        """

def c1(part, t):
    """
    Return the `t`-Jack scalar product between ``J(part)`` and ``P(part)``.

    INPUT:

    - ``part`` -- a partition
    - ``t`` -- an optional parameter (default: uses the parameter `t` from the
      Jack basis)

    OUTPUT:

    - a polynomial in the parameter ``t`` which is equal to the scalar
      product of ``J(part)`` and ``P(part)``

    EXAMPLES::

        sage: from sage.combinat.sf.jack import c1
        sage: t = QQ['t'].gen()
        sage: [c1(p,t) for p in Partitions(3)]
        [2*t^2 + 3*t + 1, t + 2, 6]
    """
def c2(part, t):
    """
    Return the t-Jack scalar product between ``J(part)`` and ``Q(part)``.

    INPUT:

    - ``self`` -- a Jack basis of the symmetric functions
    - ``part`` -- a partition
    - ``t`` -- an optional parameter (default: uses the parameter `t` from the
      Jack basis)

    OUTPUT:

    - a polynomial in the parameter ``t`` which is equal to the scalar
      product of ``J(part)`` and ``Q(part)``

    EXAMPLES::

        sage: from sage.combinat.sf.jack import c2
        sage: t = QQ['t'].gen()
        sage: [c2(p,t) for p in Partitions(3)]
        [6*t^3, 2*t^3 + t^2, t^3 + 3*t^2 + 2*t]
    """
def normalize_coefficients(self, c):
    """
    If our coefficient ring is the field of fractions over a univariate
    polynomial ring over the rationals, then we should clear both the
    numerator and denominator of the denominators of their
    coefficients.

    INPUT:

    - ``self`` -- a Jack basis of the symmetric functions
    - ``c`` -- a coefficient in the base ring of ``self``

    OUTPUT: divide numerator and denominator by the greatest common divisor

    EXAMPLES::

        sage: JP = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
        sage: t = JP.base_ring().gen()
        sage: a = 2/(1/2*t+1/2)
        sage: JP._normalize_coefficients(a)
        4/(t + 1)
        sage: a = 1/(1/3+1/6*t)
        sage: JP._normalize_coefficients(a)
        6/(t + 2)
        sage: a = 24/(4*t^2 + 12*t + 8)
        sage: JP._normalize_coefficients(a)
        6/(t^2 + 3*t + 2)
    """

class JackPolynomials_generic(sfa.SymmetricFunctionAlgebra_generic):
    t: Incomplete
    def __init__(self, jack) -> None:
        """
        A class of methods which are common to all Jack bases of the symmetric functions.

        INPUT:

        - ``self`` -- a Jack basis of the symmetric functions
        - ``jack`` -- a family of Jack symmetric function bases

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JP = Sym.jack().P(); JP.base_ring()
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
            sage: Sym = SymmetricFunctions(QQ)
            sage: JP = Sym.jack(t=2).P(); JP.base_ring()
            Rational Field
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: JP = Sym.jack().P()
            sage: JP.construction()
            (SymmetricFunctionsFunctor[Jack P],
             Fraction Field of Univariate Polynomial Ring in t over Rational Field)
        """
    def c1(self, part):
        """
        Return the `t`-Jack scalar product between ``J(part)`` and ``P(part)``.

        INPUT:

        - ``self`` -- a Jack basis of the symmetric functions
        - ``part`` -- a partition
        - ``t`` -- an optional parameter (default: uses the parameter `t` from the
          Jack basis)

        OUTPUT:

        - a polynomial in the parameter ``t`` which is equal to the scalar
          product of ``J(part)`` and ``P(part)``

        EXAMPLES::

            sage: JP = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
            sage: JP.c1(Partition([2,1]))
            t + 2
        """
    def c2(self, part):
        """
        Return the `t`-Jack scalar product between ``J(part)`` and ``Q(part)``.

        INPUT:

        - ``self`` -- a Jack basis of the symmetric functions
        - ``part`` -- a partition
        - ``t`` -- an optional parameter (default: uses the parameter `t` from the
            Jack basis)

        OUTPUT:

        - a polynomial in the parameter ``t`` which is equal to the scalar
          product of ``J(part)`` and ``Q(part)``

        EXAMPLES::

            sage: JP = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
            sage: JP.c2(Partition([2,1]))
            2*t^3 + t^2
        """
    def product(self, left, right):
        """
        The product of two Jack symmetric functions is done by multiplying the
        elements in the `P` basis and then expressing the elements
        in the basis ``self``.

        INPUT:

        - ``self`` -- a Jack basis of the symmetric functions
        - ``left``, ``right`` -- symmetric function elements

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: JJ = SymmetricFunctions(FractionField(QQ['t'])).jack().J()
            sage: JJ([1])^2              # indirect doctest
            (t/(t+1))*JackJ[1, 1] + (1/(t+1))*JackJ[2]
            sage: JJ([2])^2
            (t^2/(t^2+3/2*t+1/2))*JackJ[2, 2] + (4/3*t/(t^2+4/3*t+1/3))*JackJ[3, 1] + ((1/6*t+1/6)/(t^2+5/6*t+1/6))*JackJ[4]
            sage: JQ = SymmetricFunctions(FractionField(QQ['t'])).jack().Q()
            sage: JQ([1])^2              # indirect doctest
            JackQ[1, 1] + (2/(t+1))*JackQ[2]
            sage: JQ([2])^2
            JackQ[2, 2] + (2/(t+1))*JackQ[3, 1] + ((t+1)/(t^2+5/6*t+1/6))*JackQ[4]
        """
    def jack_family(self):
        """
        Return the family of Jack bases associated to the basis ``self``.

        INPUT:

        - ``self`` -- a Jack basis of the symmetric functions

        EXAMPLES::

            sage: JackP = SymmetricFunctions(QQ).jack(t=2).P()
            sage: JackP.jack_family()
            Jack polynomials with t=2 over Rational Field
        """
    def coproduct_by_coercion(self, elt):
        """
        Return the coproduct of the element ``elt`` by coercion to the Schur basis.

        INPUT:

        - ``self`` -- a Jack symmetric function basis
        - ``elt`` -- an instance of this basis

        OUTPUT:

        - The coproduct acting on ``elt``, the result is an element of the
          tensor squared of the Jack symmetric function basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
            sage: Sym.jack().P()[2,2].coproduct() #indirect doctest
            JackP[] # JackP[2, 2] + (2/(t+1))*JackP[1] # JackP[2, 1] + ((8*t+4)/(t^3+4*t^2+5*t+2))*JackP[1, 1] # JackP[1, 1] + JackP[2] # JackP[2] + (2/(t+1))*JackP[2, 1] # JackP[1] + JackP[2, 2] # JackP[]
        """
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element):
        def scalar_jack(self, x, t=None):
            """
            A scalar product where the power sums are orthogonal and
            `\\langle p_\\mu, p_\\mu \\rangle = z_\\mu t^{length(\\mu)}`

            INPUT:

            - ``self`` -- an element of a Jack basis of the symmetric functions
            - ``x`` -- an element of the symmetric functions
            - ``t`` -- an optional parameter (default: ``None``; uses the
              parameter from the basis)

            OUTPUT: the Jack scalar product between ``x`` and ``self``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
                sage: JP = Sym.jack().P()
                sage: JQ = Sym.jack().Q()
                sage: p = Partitions(3).list()
                sage: matrix([[JP(a).scalar_jack(JQ(b)) for a in p] for b in p])
                [1 0 0]
                [0 1 0]
                [0 0 1]
            """

def part_scalar_jack(part1, part2, t):
    """
    Return the Jack scalar product between ``p(part1)`` and ``p(part2)`` where
    `p` is the power-sum basis.

    INPUT:

    - ``part1``, ``part2`` -- two partitions
    - ``t`` -- a parameter

    OUTPUT: the scalar product between the power sum indexed by ``part1`` and ``part2``

    EXAMPLES::

        sage: Q.<t> = QQ[]
        sage: from sage.combinat.sf.jack import part_scalar_jack
        sage: matrix([[part_scalar_jack(p1,p2,t) for p1 in Partitions(4)] for p2 in Partitions(4)])
        [   4*t      0      0      0      0]
        [     0  3*t^2      0      0      0]
        [     0      0  8*t^2      0      0]
        [     0      0      0  4*t^3      0]
        [     0      0      0      0 24*t^4]
    """

class JackPolynomials_p(JackPolynomials_generic):
    def __init__(self, jack) -> None:
        """
        The `P` basis is uni-triangularly related to the monomial basis and
        orthogonal with respect to the Jack scalar product.

        INPUT:

        - ``self`` -- an instance of the Jack `P` basis of the symmetric functions
        - ``jack`` -- a family of Jack symmetric function bases

        EXAMPLES::

            sage: P = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
            sage: TestSuite(P).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive
            sage: TestSuite(P).run(elements = [P.t*P[1,1]+P[2], P[1]+(1+P.t)*P[1,1]])
        """
    def product(self, left, right):
        """
        The product of two Jack symmetric functions is done by multiplying the
        elements in the monomial basis and then expressing the elements
        the basis ``self``.

        INPUT:

        - ``self`` -- a Jack basis of the symmetric functions
        - ``left``, ``right`` -- symmetric function elements

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: JP = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
            sage: m = JP.symmetric_function_ring().m()
            sage: JP([1])^2 # indirect doctest
            (2*t/(t+1))*JackP[1, 1] + JackP[2]
            sage: m(_)
            2*m[1, 1] + m[2]
            sage: JP = SymmetricFunctions(QQ).jack(t=2).P()
            sage: JP([2,1])^2
            125/63*JackP[2, 2, 1, 1] + 25/12*JackP[2, 2, 2] + 25/18*JackP[3, 1, 1, 1] + 12/5*JackP[3, 2, 1] + 4/3*JackP[3, 3] + 4/3*JackP[4, 1, 1] + JackP[4, 2]
            sage: m(_)
            45*m[1, 1, 1, 1, 1, 1] + 51/2*m[2, 1, 1, 1, 1] + 29/2*m[2, 2, 1, 1] + 33/4*m[2, 2, 2] + 9*m[3, 1, 1, 1] + 5*m[3, 2, 1] + 2*m[3, 3] + 2*m[4, 1, 1] + m[4, 2]
        """
    def scalar_jack_basis(self, part1, part2=None):
        """
        Return the scalar product of `P(part1)` and `P(part2)`.

        This is equation (10.16) of [Mc1995]_ on page 380.

        INPUT:

        - ``self`` -- an instance of the Jack `P` basis of the symmetric functions
        - ``part1`` -- a partition
        - ``part2`` -- an optional partition (default: ``None``)

        OUTPUT:

        - the scalar product between `P(part1)` and `P(part2)` (or itself if `part2` is None)

        REFERENCES:

        .. [Mc1995] \\I. G. Macdonald, Symmetric functions and Hall
           polynomials, second ed., The Clarendon Press, Oxford
           University Press, New York, 1995, With contributions by
           A. Zelevinsky, Oxford Science Publications.

        EXAMPLES::

            sage: JP = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
            sage: JJ = SymmetricFunctions(FractionField(QQ['t'])).jack().J()
            sage: JP.scalar_jack_basis(Partition([2,1]), Partition([1,1,1]))
            0
            sage: JP._normalize_coefficients(JP.scalar_jack_basis(Partition([3,2,1]), Partition([3,2,1])))
            (6*t^6 + 10*t^5 + 11/2*t^4 + t^3)/(t^3 + 11/2*t^2 + 10*t + 6)
            sage: JJ(JP[3,2,1]).scalar_jack(JP[3,2,1])
            (6*t^6 + 10*t^5 + 11/2*t^4 + t^3)/(t^3 + 11/2*t^2 + 10*t + 6)

        With a single argument, takes `part2 = part1`::

            sage: JP.scalar_jack_basis(Partition([2,1]), Partition([2,1]))
            (2*t^3 + t^2)/(t + 2)
            sage: JJ(JP[2,1]).scalar_jack(JP[2,1])
            (2*t^3 + t^2)/(t + 2)
        """
    class Element(JackPolynomials_generic.Element):
        def scalar_jack(self, x, t=None):
            """
            The scalar product on the symmetric functions where the power sums
            are orthogonal and `\\langle p_\\mu, p_\\mu \\rangle = z_\\mu t^{length(mu)}`
            where the t parameter from the Jack symmetric function family.

            INPUT:

            - ``self`` -- an element of the Jack `P` basis
            - ``x`` -- an element of the `P` basis

            EXAMPLES::

                sage: JP = SymmetricFunctions(FractionField(QQ['t'])).jack().P()
                sage: l = [JP(p) for p in Partitions(3)]
                sage: matrix([[a.scalar_jack(b) for a in l] for b in l])
                [3*t^3/(t^2 + 3/2*t + 1/2)                         0                         0]
                [                        0     (2*t^3 + t^2)/(t + 2)                         0]
                [                        0                         0 1/6*t^3 + 1/2*t^2 + 1/3*t]
            """

class JackPolynomials_j(JackPolynomials_generic):
    def __init__(self, jack) -> None:
        """
        The `J` basis is a defined as a normalized form of the `P` basis.

        INPUT:

        - ``self`` -- an instance of the Jack `P` basis of the symmetric functions
        - ``jack`` -- a family of Jack symmetric function bases

        EXAMPLES::

            sage: J = SymmetricFunctions(FractionField(QQ['t'])).jack().J()
            sage: TestSuite(J).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive
            sage: TestSuite(J).run(elements = [J.t*J[1,1]+J[2], J[1]+(1+J.t)*J[1,1]])  # long time (3s on sage.math, 2012)
        """
    class Element(JackPolynomials_generic.Element): ...

class JackPolynomials_q(JackPolynomials_generic):
    def __init__(self, jack) -> None:
        """
        The `Q` basis is defined as a normalized form of the `P` basis.

        INPUT:

        - ``self`` -- an instance of the Jack `Q` basis of the symmetric functions
        - ``jack`` -- a family of Jack symmetric function bases

        EXAMPLES::

            sage: Q = SymmetricFunctions(FractionField(QQ['t'])).jack().Q()
            sage: TestSuite(Q).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive
            sage: TestSuite(Q).run(elements = [Q.t*Q[1,1]+Q[2], Q[1]+(1+Q.t)*Q[1,1]])  # long time (3s on sage.math, 2012)
        """
    class Element(JackPolynomials_generic.Element): ...

qp_to_h_cache: Incomplete
h_to_qp_cache: Incomplete

class JackPolynomials_qp(JackPolynomials_generic):
    def __init__(self, jack) -> None:
        """
        The `Qp` basis is the dual basis to the `P` basis with respect to the
        standard scalar product

        INPUT:

        - ``self`` -- an instance of the Jack `Qp` basis of the symmetric functions
        - ``jack`` -- a family of Jack symmetric function bases

        EXAMPLES::

            sage: Qp = SymmetricFunctions(FractionField(QQ['t'])).jack().Qp()
            sage: TestSuite(Qp).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive
            sage: TestSuite(Qp).run(elements = [Qp.t*Qp[1,1]+Qp[2], Qp[1]+(1+Qp.t)*Qp[1,1]])  # long time (3s on sage.math, 2012)
        """
    def product(self, left, right):
        """
        The product of two Jack symmetric functions is done by multiplying the
        elements in the monomial basis and then expressing the elements
        the basis ``self``.

        INPUT:

        - ``self`` -- an instance of the Jack `Qp` basis of the symmetric functions
        - ``left``, ``right`` -- symmetric function elements

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: JQp = SymmetricFunctions(FractionField(QQ['t'])).jack().Qp()
            sage: h = JQp.symmetric_function_ring().h()
            sage: JQp([1])^2 # indirect doctest
            JackQp[1, 1] + (2/(t+1))*JackQp[2]
            sage: h(_)
            h[1, 1]
            sage: JQp = SymmetricFunctions(QQ).jack(t=2).Qp()
            sage: h = SymmetricFunctions(QQ).h()
            sage: JQp([2,1])^2
            JackQp[2, 2, 1, 1] + 2/3*JackQp[2, 2, 2] + 2/3*JackQp[3, 1, 1, 1] + 48/35*JackQp[3, 2, 1] + 28/75*JackQp[3, 3] + 128/225*JackQp[4, 1, 1] + 28/75*JackQp[4, 2]
            sage: h(_)
            h[2, 2, 1, 1] - 6/5*h[3, 2, 1] + 9/25*h[3, 3]
        """
    def coproduct_by_coercion(self, elt):
        """
        Return the coproduct of the element ``elt`` by coercion to the Schur basis.

        INPUT:

        - ``elt`` -- an instance of the ``Qp`` basis

        OUTPUT:

        - The coproduct acting on ``elt``, the result is an element of the
          tensor squared of the ``Qp`` symmetric function basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ['t'].fraction_field())
            sage: JQp = Sym.jack().Qp()
            sage: JQp[2,2].coproduct()   #indirect doctest
            JackQp[] # JackQp[2, 2] + (2*t/(t+1))*JackQp[1] # JackQp[2, 1] + JackQp[1, 1] # JackQp[1, 1] + ((2*t^3+4*t^2)/(t^3+5/2*t^2+2*t+1/2))*JackQp[2] # JackQp[2] + (2*t/(t+1))*JackQp[2, 1] # JackQp[1] + JackQp[2, 2] # JackQp[]
        """
    class Element(JackPolynomials_generic.Element): ...

class SymmetricFunctionAlgebra_zonal(sfa.SymmetricFunctionAlgebra_generic):
    def __init__(self, Sym) -> None:
        """
        Return the algebra of zonal polynomials.

        INPUT:

        - ``self`` -- a zonal basis of the symmetric functions
        - ``Sym`` -- a ring of the symmetric functions

        EXAMPLES::

            sage: Z = SymmetricFunctions(QQ).zonal()
            sage: Z([2])^2
            64/45*Z[2, 2] + 16/21*Z[3, 1] + Z[4]
            sage: Z = SymmetricFunctions(QQ).zonal()
            sage: TestSuite(Z).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive
            sage: TestSuite(Z).run(elements = [Z[1,1]+Z[2], Z[1]+2*Z[1,1]])
        """
    def product(self, left, right):
        """
        The product of two zonal symmetric functions is done by multiplying the
        elements in the monomial basis and then expressing the elements
        in the basis ``self``.

        INPUT:

        - ``self`` -- a zonal basis of the symmetric functions
        - ``left``, ``right`` -- symmetric function elements

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ)
            sage: Z = Sym.zonal()
            sage: JP = Sym.jack(t=1).P()
            sage: Z([2])*Z([3])                    # indirect doctest
            192/175*Z[3, 2] + 32/45*Z[4, 1] + Z[5]
            sage: Z([2])*JP([2])
            10/27*Z[2, 1, 1] + 64/45*Z[2, 2] + 23/21*Z[3, 1] + Z[4]
            sage: JP = Sym.jack(t=2).P()
            sage: Z([2])*JP([2])
            64/45*Z[2, 2] + 16/21*Z[3, 1] + Z[4]
        """
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element):
        def scalar_zonal(self, x):
            """
            The zonal scalar product has the power sum basis and the zonal
            symmetric functions are orthogonal. In particular,
            `\\langle p_\\mu, p_\\mu \\rangle = z_\\mu 2^{length(\\mu)}`.

            INPUT:

            - ``self`` -- an element of the zonal basis
            - ``x`` -- an element of the symmetric function

            OUTPUT: the scalar product between ``self`` and ``x``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(QQ)
                sage: Z = Sym.zonal()
                sage: parts = Partitions(3).list()
                sage: matrix([[Z(a).scalar_zonal(Z(b)) for a in parts] for b in parts])
                [16/5    0    0]
                [   0    5    0]
                [   0    0    4]
                sage: p = Z.symmetric_function_ring().power()
                sage: matrix([[Z(p(a)).scalar_zonal(p(b)) for a in parts] for b in parts])
                [ 6  0  0]
                [ 0  8  0]
                [ 0  0 48]
            """
