from . import sfa as sfa
from _typeshed import Incomplete
from sage.categories.homset import Hom as Hom
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.libs.symmetrica.all import hall_littlewood as hall_littlewood
from sage.matrix.constructor import matrix as matrix
from sage.rings.rational_field import QQ as QQ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

p_to_s_cache: Incomplete
s_to_p_cache: Incomplete
qp_to_s_cache: Incomplete
s_to_qp_cache: Incomplete
QQt: Incomplete

class HallLittlewood(UniqueRepresentation):
    """
    The family of Hall-Littlewood symmetric function bases.

    The Hall-Littlewood symmetric functions are a family of symmetric
    functions that depend on a parameter `t`.

    INPUT:

    By default the parameter for these functions is `t`, and
    whatever the parameter is, it must be in the base ring.

    EXAMPLES::

        sage: SymmetricFunctions(QQ).hall_littlewood(1)
        Hall-Littlewood polynomials with t=1 over Rational Field
        sage: SymmetricFunctions(QQ['t'].fraction_field()).hall_littlewood()
        Hall-Littlewood polynomials over Fraction Field of Univariate Polynomial Ring in t over Rational Field
    """
    @staticmethod
    def __classcall__(cls, Sym, t: str = 't'):
        """
        Normalize the arguments.

        TESTS::

            sage: R.<q, t> = QQ[]
            sage: B1 = SymmetricFunctions(R).hall_littlewood()
            sage: B2 = SymmetricFunctions(R).hall_littlewood(t)
            sage: B3 = SymmetricFunctions(R).hall_littlewood(q)
            sage: B1 is B2
            True
            sage: B1 == B3
            False
        """
    t: Incomplete
    def __init__(self, Sym, t) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: HL = SymmetricFunctions(FractionField(QQ['t'])).hall_littlewood()
            sage: TestSuite(HL).run()
        """
    def symmetric_function_ring(self):
        """
        Return the ring of symmetric functions associated to the class of
        Hall-Littlewood symmetric functions.

        INPUT:

        - ``self`` -- a class of Hall-Littlewood symmetric function bases

        EXAMPLES::

            sage: HL = SymmetricFunctions(FractionField(QQ['t'])).hall_littlewood()
            sage: HL.symmetric_function_ring()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def base_ring(self):
        """
        Return the base ring of the symmetric functions where the
        Hall-Littlewood symmetric functions live.

        INPUT:

        - ``self`` -- a class of Hall-Littlewood symmetric function bases

        EXAMPLES::

            sage: HL = SymmetricFunctions(QQ['t'].fraction_field()).hall_littlewood(t=1)
            sage: HL.base_ring()
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def P(self):
        """
        Return the algebra of symmetric functions in the Hall-Littlewood
        `P` basis. This is the same as the `HL` basis in John Stembridge's
        SF examples file.

        INPUT:

        - ``self`` -- a class of Hall-Littlewood symmetric function bases

        OUTPUT: the class of the Hall-Littlewood `P` basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLP = Sym.hall_littlewood().P(); HLP
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Hall-Littlewood P basis
            sage: SP = Sym.hall_littlewood(t=-1).P(); SP
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Hall-Littlewood P with t=-1 basis
            sage: s = Sym.schur()
            sage: s(HLP([2,1]))
            (-t^2-t)*s[1, 1, 1] + s[2, 1]

        The Hall-Littlewood polynomials in the `P` basis at `t = 0` are the
        Schur functions::

            sage: Sym = SymmetricFunctions(QQ)
            sage: HLP = Sym.hall_littlewood(t=0).P()
            sage: s = Sym.schur()
            sage: s(HLP([2,1])) == s([2,1])
            True

        The Hall-Littlewood polynomials in the `P` basis at `t = 1` are the
        monomial symmetric functions::

            sage: Sym = SymmetricFunctions(QQ)
            sage: HLP = Sym.hall_littlewood(t=1).P()
            sage: m = Sym.monomial()
            sage: m(HLP([2,2,1])) == m([2,2,1])
            True

        We end with some examples of coercions between:

            1. Hall-Littlewood `P` basis.

            2. Hall-Littlewood polynomials in the `Q` basis

            3. Hall-Littlewood polynomials in the `Q^\\prime` basis (via the Schurs)

            4. Classical symmetric functions

        ::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLP  = Sym.hall_littlewood().P()
            sage: HLQ  = Sym.hall_littlewood().Q()
            sage: HLQp = Sym.hall_littlewood().Qp()
            sage: s = Sym.schur()
            sage: p = Sym.power()
            sage: HLP(HLQ([2])) # indirect doctest
            (-t+1)*HLP[2]
            sage: HLP(HLQp([2]))
            t*HLP[1, 1] + HLP[2]
            sage: HLP(s([2]))
            t*HLP[1, 1] + HLP[2]
            sage: HLP(p([2]))
            (t-1)*HLP[1, 1] + HLP[2]
            sage: s = HLQp.symmetric_function_ring().s()
            sage: HLQp.transition_matrix(s,3)
            [      1       0       0]
            [      t       1       0]
            [    t^3 t^2 + t       1]
            sage: s.transition_matrix(HLP,3)
            [      1       t     t^3]
            [      0       1 t^2 + t]
            [      0       0       1]

        The method :meth:`sage.combinat.sf.sfa.SymmetricFunctionAlgebra_generic_Element.hl_creation_operator`
        is a creation operator for the `Q` basis::

            sage: HLQp[1].hl_creation_operator([3]).hl_creation_operator([3])
            HLQp[3, 3, 1]

        Transitions between bases with the parameter `t` specialized::

            sage: Sym = SymmetricFunctions(FractionField(QQ['y','z']))
            sage: (y,z) = Sym.base_ring().gens()
            sage: HLy = Sym.hall_littlewood(t=y)
            sage: HLz = Sym.hall_littlewood(t=z)
            sage: Qpy = HLy.Qp()
            sage: Qpz = HLz.Qp()
            sage: s = Sym.schur()
            sage: s( Qpy[3,1] + z*Qpy[2,2] )
            z*s[2, 2] + (y*z+1)*s[3, 1] + (y^2*z+y)*s[4]
            sage: s( Qpy[3,1] + y*Qpz[2,2] )
            y*s[2, 2] + (y*z+1)*s[3, 1] + (y*z^2+y)*s[4]
            sage: s( Qpy[3,1] + y*Qpy[2,2] )
            y*s[2, 2] + (y^2+1)*s[3, 1] + (y^3+y)*s[4]

            sage: Qy = HLy.Q()
            sage: Qz = HLz.Q()
            sage: Py = HLy.P()
            sage: Pz = HLz.P()
            sage: Pz(Qpy[2,1])
            (y*z^3+z^2+z)*HLP[1, 1, 1] + (y*z+1)*HLP[2, 1] + y*HLP[3]
            sage: Pz(Qz[2,1])
            (z^2-2*z+1)*HLP[2, 1]
            sage: Qz(Py[2])
            -((y-z)/(z^3-z^2-z+1))*HLQ[1, 1] + (1/(-z+1))*HLQ[2]
            sage: Qy(Pz[2])
            ((y-z)/(y^3-y^2-y+1))*HLQ[1, 1] + (1/(-y+1))*HLQ[2]
            sage: Qy.hall_littlewood_family() == HLy
            True
            sage: Qy.hall_littlewood_family() == HLz
            False
            sage: Qz.symmetric_function_ring() == Qy.symmetric_function_ring()
            True

            sage: Sym = SymmetricFunctions(FractionField(QQ['q']))
            sage: q = Sym.base_ring().gen()
            sage: HL = Sym.hall_littlewood(t=q)
            sage: HLQp = HL.Qp()
            sage: HLQ = HL.Q()
            sage: HLP = HL.P()
            sage: s = Sym.schur()
            sage: s(HLQp[3,2].plethysm((1-q)*s[1]))/(1-q)^2
            (-q^5-q^4)*s[1, 1, 1, 1, 1] + (q^3+q^2)*s[2, 1, 1, 1] - q*s[2, 2, 1] - q*s[3, 1, 1] + s[3, 2]
            sage: s(HLP[3,2])
            (-q^5-q^4)*s[1, 1, 1, 1, 1] + (q^3+q^2)*s[2, 1, 1, 1] - q*s[2, 2, 1] - q*s[3, 1, 1] + s[3, 2]

        The `P` and `Q`-Schur at `t=-1` indexed by strict partitions are a basis for
        the space algebraically generated by the odd power sum symmetric functions::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q']))
            sage: SP = Sym.hall_littlewood(t=-1).P()
            sage: SQ = Sym.hall_littlewood(t=-1).Q()
            sage: p = Sym.power()
            sage: SP(SQ[3,2,1])
            8*HLP[3, 2, 1]
            sage: SP(SQ[2,2,1])
            0
            sage: p(SP[3,2,1])
            1/45*p[1, 1, 1, 1, 1, 1] - 1/9*p[3, 1, 1, 1] - 1/9*p[3, 3] + 1/5*p[5, 1]
            sage: SP(p[3,3])
            -4*HLP[3, 2, 1] + 2*HLP[4, 2] - 2*HLP[5, 1] + HLP[6]
            sage: SQ( SQ[1]*SQ[3] -2*(1-q)*SQ[4] )
            HLQ[3, 1] + 2*q*HLQ[4]

        TESTS::

            sage: HLP(s[[]])
            HLP[]
            sage: HLQ(s[[]])
            HLQ[]
            sage: HLQp(s[[]])
            HLQp[]
        """
    def Q(self):
        """
        Return the algebra of symmetric functions in Hall-Littlewood `Q`
        basis. This is the same as the `Q` basis in John Stembridge's SF
        examples file.

        More extensive examples can be found in the documentation for the
        Hall-Littlewood `P` basis.

        INPUT:

        - ``self`` -- a class of Hall-Littlewood symmetric function bases

        OUTPUT: the class of the Hall-Littlewood `Q` basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLQ = Sym.hall_littlewood().Q(); HLQ
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Hall-Littlewood Q basis
            sage: SQ = SymmetricFunctions(QQ).hall_littlewood(t=-1).Q(); SQ
            Symmetric Functions over Rational Field in the Hall-Littlewood Q with t=-1 basis
        """
    def Qp(self):
        """
        Return the algebra of symmetric functions in Hall-Littlewood `Q^\\prime` (Qp)
        basis. This is dual to the Hall-Littlewood `P` basis with respect to
        the standard scalar product.

        More extensive examples can be found in the documentation for the
        Hall-Littlewood P basis.

        INPUT:

        - ``self`` -- a class of Hall-Littlewood symmetric function bases

        OUTPUT: the class of the Hall-Littlewood `Qp`-basis

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLQp = Sym.hall_littlewood().Qp(); HLQp
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Hall-Littlewood Qp basis
        """

class HallLittlewood_generic(sfa.SymmetricFunctionAlgebra_generic):
    t: Incomplete
    def __init__(self, hall_littlewood) -> None:
        """
        A class with methods for working with Hall-Littlewood symmetric functions which
        are common to all bases.

        INPUT:

        - ``self`` -- a Hall-Littlewood symmetric function basis
        - ``hall_littlewood`` -- a class of Hall-Littlewood bases

        TESTS::

            sage: SymmetricFunctions(QQ['t'].fraction_field()).hall_littlewood().P()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Hall-Littlewood P basis
            sage: SymmetricFunctions(QQ).hall_littlewood(t=2).P()
            Symmetric Functions over Rational Field in the Hall-Littlewood P with t=2 basis
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: P = SymmetricFunctions(QQ).hall_littlewood(t=2).P()
            sage: P.construction()
            (SymmetricFunctionsFunctor[Hall-Littlewood P with t=2], Rational Field)
        """
    def transition_matrix(self, basis, n):
        """
        Return the transitions matrix between ``self`` and ``basis`` for the
        homogeneous component of degree ``n``.

        INPUT:

        - ``self`` -- a Hall-Littlewood symmetric function basis
        - ``basis`` -- another symmetric function basis
        - ``n`` -- nonnegative integer representing the degree

        OUTPUT:

        - Returns a `r \\times r` matrix of elements of the base ring of ``self``
          where `r` is the number of partitions of ``n``.
          The entry corresponding to row `\\mu`, column `\\nu` is the
          coefficient of ``basis`` `(\\nu)` in ``self`` `(\\mu)`

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLP = Sym.hall_littlewood().P()
            sage: s   = Sym.schur()
            sage: HLP.transition_matrix(s, 4)
            [             1             -t              0            t^2           -t^3]
            [             0              1             -t             -t      t^3 + t^2]
            [             0              0              1             -t            t^3]
            [             0              0              0              1 -t^3 - t^2 - t]
            [             0              0              0              0              1]
            sage: HLQ = Sym.hall_littlewood().Q()
            sage: HLQ.transition_matrix(s,3)
            [                        -t + 1                        t^2 - t                     -t^3 + t^2]
            [                             0                  t^2 - 2*t + 1           -t^4 + t^3 + t^2 - t]
            [                             0                              0 -t^6 + t^5 + t^4 - t^2 - t + 1]
            sage: HLQp = Sym.hall_littlewood().Qp()
            sage: HLQp.transition_matrix(s,3)
            [      1       0       0]
            [      t       1       0]
            [    t^3 t^2 + t       1]
        """
    def product(self, left, right):
        """
        Multiply an element of the Hall-Littlewood symmetric function
        basis ``self`` and another symmetric function

        Convert to the Schur basis, do the multiplication there, and
        convert back to ``self`` basis.

        INPUT:

        - ``self`` -- a Hall-Littlewood symmetric function basis
        - ``left`` -- an element of the basis ``self``
        - ``right`` -- another symmetric function

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLP = Sym.hall_littlewood().P()
            sage: HLP([2])^2 # indirect doctest
            (t+1)*HLP[2, 2] + (-t+1)*HLP[3, 1] + HLP[4]

            sage: HLQ = Sym.hall_littlewood().Q()
            sage: HLQ([2])^2 # indirect doctest
            HLQ[2, 2] + (-t+1)*HLQ[3, 1] + (-t+1)*HLQ[4]

            sage: HLQp = Sym.hall_littlewood().Qp()
            sage: HLQp([2])^2 # indirect doctest
            HLQp[2, 2] + (-t+1)*HLQp[3, 1] + (-t+1)*HLQp[4]
        """
    def hall_littlewood_family(self):
        """
        The family of Hall-Littlewood bases associated to ``self``.

        INPUT:

        - ``self`` -- a Hall-Littlewood symmetric function basis

        OUTPUT: the class of Hall-Littlewood bases

        EXAMPLES::

            sage: HLP = SymmetricFunctions(FractionField(QQ['t'])).hall_littlewood(1).P()
            sage: HLP.hall_littlewood_family()
            Hall-Littlewood polynomials with t=1 over Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element):
        """
        Methods for elements of a Hall-Littlewood basis that are common to all bases.
        """
        def expand(self, n, alphabet: str = 'x'):
            """
            Expand the symmetric function as a symmetric polynomial in ``n`` variables.

            INPUT:

            - ``self`` -- an element of a Hall-Littlewood basis
            - ``n`` -- positive integer
            - ``alphabet`` -- string representing a variable name (default: ``'x'``)

            OUTPUT: a symmetric polynomial of ``self`` in ``n`` variables

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
                sage: HLP = Sym.hall_littlewood().P()
                sage: HLQ = Sym.hall_littlewood().Q()
                sage: HLQp = Sym.hall_littlewood().Qp()
                sage: HLP([2]).expand(2)
                x0^2 + (-t + 1)*x0*x1 + x1^2
                sage: HLQ([2]).expand(2)
                (-t + 1)*x0^2 + (t^2 - 2*t + 1)*x0*x1 + (-t + 1)*x1^2
                sage: HLQp([2]).expand(2)
                x0^2 + x0*x1 + x1^2
                sage: HLQp([2]).expand(2, 'y')
                y0^2 + y0*y1 + y1^2
                sage: HLQp([2]).expand(1)
                x^2
            """
        def scalar(self, x, zee=None):
            """
            Return standard scalar product between ``self`` and ``x``.

            This is the default implementation that converts both ``self`` and ``x``
            into Schur functions and performs the scalar product that basis.

            The Hall-Littlewood `P` basis is dual to the `Qp` basis with respect to
            this scalar product.

            INPUT:

            - ``self`` -- an element of a Hall-Littlewood basis
            - ``x`` -- another symmetric element of the symmetric functions

            OUTPUT: the scalar product between ``self`` and ``x``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
                sage: HLP = Sym.hall_littlewood().P()
                sage: HLQ = Sym.hall_littlewood().Q()
                sage: HLQp = Sym.hall_littlewood().Qp()
                sage: HLP([2]).scalar(HLQp([2]))
                1
                sage: HLP([2]).scalar(HLQp([1,1]))
                0
                sage: HLP([2]).scalar(HLQ([2]), lambda mu: mu.centralizer_size(t = HLP.t))
                1
                sage: HLP([2]).scalar(HLQ([1,1]), lambda mu: mu.centralizer_size(t = HLP.t))
                0
            """
        def scalar_hl(self, x, t=None):
            """
            Return the Hall-Littlewood (with parameter ``t``) scalar product
            of ``self`` and ``x``.

            The Hall-Littlewood scalar product is defined in Macdonald's
            book [Mac1995]_.  The power sum basis is orthogonal and
            `\\langle p_\\mu, p_\\mu \\rangle = z_\\mu \\prod_{i} 1/(1-t^{\\mu_i})`

            The Hall-Littlewood `P` basis is dual to the `Q` basis with respect to
            this scalar product.

            INPUT:

            - ``self`` -- an element of a Hall-Littlewood basis
            - ``x`` -- another symmetric element of the symmetric functions
            - ``t`` -- an optional parameter, if this parameter is not specified then
              the value of the ``t`` from the basis is used in the calculation

            OUTPUT: the Hall-Littlewood scalar product between ``self`` and ``x``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
                sage: HLP = Sym.hall_littlewood().P()
                sage: HLQ = Sym.hall_littlewood().Q()
                sage: HLP([2]).scalar_hl(HLQ([2]))
                1
                sage: HLP([2]).scalar_hl(HLQ([1,1]))
                0
                sage: HLQ([2]).scalar_hl(HLQ([2]))
                -t + 1
                sage: HLQ([2]).scalar_hl(HLQ([1,1]))
                0
                sage: HLP([2]).scalar_hl(HLP([2]))
                -1/(t - 1)
            """

class HallLittlewood_p(HallLittlewood_generic):
    """
    A class representing the Hall-Littlewood `P` basis of symmetric functions
    """
    class Element(HallLittlewood_generic.Element): ...
    def __init__(self, hall_littlewood) -> None:
        """
        A class with methods for working with the Hall-Littlewood `P` basis.

        The `P` basis is calculated from the Schur basis using the functions
        in :meth:`sage.combinat.sf.kfpoly`.  These functions calculate Kostka-Foulkes polynomials
        using rigged configuration formulas.

        This change of basis is inverted to convert to the Schur basis.

        INPUT:

        - ``self`` -- an instance of the Hall-Littlewood `P` basis
        - ``hall_littlewood`` -- a class for the family of Hall-Littlewood bases

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: P = Sym.hall_littlewood().P()
            sage: TestSuite(P).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive
            sage: TestSuite(P).run(elements = [P.t*P[1,1]+P[2], P[1]+(1+P.t)*P[1,1]])
        """

class HallLittlewood_q(HallLittlewood_generic):
    class Element(HallLittlewood_generic.Element): ...
    def __init__(self, hall_littlewood) -> None:
        """
        The `Q` basis is defined as a normalization of the `P` basis.

        INPUT:

        - ``self`` -- an instance of the Hall-Littlewood `P` basis
        - ``hall_littlewood`` -- a class for the family of Hall-Littlewood bases

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: Q = Sym.hall_littlewood().Q()
            sage: TestSuite(Q).run(skip=['_test_associativity', '_test_distributivity', '_test_prod']) # products are too expensive, long time (3s on sage.math, 2012)
            sage: TestSuite(Q).run(elements = [Q.t*Q[1,1]+Q[2], Q[1]+(1+Q.t)*Q[1,1]])  # long time (depends on previous)

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLP = Sym.hall_littlewood().P()
            sage: HLQ = Sym.hall_littlewood().Q()
            sage: HLQp = Sym.hall_littlewood().Qp()
            sage: s = Sym.schur(); p = Sym.power()
            sage: HLQ( HLP([2,1]) + HLP([3]) )
            (1/(t^2-2*t+1))*HLQ[2, 1] - (1/(t-1))*HLQ[3]
            sage: HLQ(HLQp([2])) # indirect doctest
            (t/(t^3-t^2-t+1))*HLQ[1, 1] - (1/(t-1))*HLQ[2]
            sage: HLQ(s([2]))
            (t/(t^3-t^2-t+1))*HLQ[1, 1] - (1/(t-1))*HLQ[2]
            sage: HLQ(p([2]))
            (1/(t^2-1))*HLQ[1, 1] - (1/(t-1))*HLQ[2]
        """

class HallLittlewood_qp(HallLittlewood_generic):
    class Element(HallLittlewood_generic.Element): ...
    def __init__(self, hall_littlewood) -> None:
        """
        The Hall-Littlewood `Qp` basis is calculated through the symmetrica
        library (see the function :meth:`HallLittlewood_qp._to_s`).

        INPUT:

        - ``self`` -- an instance of the Hall-Littlewood `P` basis
        - ``hall_littlewood`` -- a class for the family of Hall-Littlewood bases

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: Qp = Sym.hall_littlewood().Q()
            sage: TestSuite(Qp).run(skip=['_test_passociativity', '_test_distributivity', '_test_prod']) # products are too expensive, long time (3s on sage.math, 2012)
            sage: TestSuite(Qp).run(elements = [Qp.t*Qp[1,1]+Qp[2], Qp[1]+(1+Qp.t)*Qp[1,1]])  # long time (depends on previous)

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: HLP = Sym.hall_littlewood().P()
            sage: HLQ = Sym.hall_littlewood().Q()
            sage: HLQp = Sym.hall_littlewood().Qp()
            sage: s = Sym.schur(); p = Sym.power()
            sage: HLQp(HLP([2])) # indirect doctest
            -t*HLQp[1, 1] + (t^2+1)*HLQp[2]
            sage: HLQp(s(HLQ([2]))) # work around bug reported in issue #12969
            (t^2-t)*HLQp[1, 1] + (-t^3+t^2-t+1)*HLQp[2]
            sage: HLQp(s([2]))
            HLQp[2]
            sage: HLQp(p([2]))
            -HLQp[1, 1] + (t+1)*HLQp[2]
            sage: s = HLQp.symmetric_function_ring().s()
            sage: HLQp.transition_matrix(s,3)
            [      1       0       0]
            [      t       1       0]
            [    t^3 t^2 + t       1]
            sage: s.transition_matrix(HLP,3)
            [      1       t     t^3]
            [      0       1 t^2 + t]
            [      0       0       1]
        """
