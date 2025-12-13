from . import sfa as sfa
from _typeshed import Incomplete
from sage.categories.homset import Hom as Hom
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.morphism import SetMorphism as SetMorphism
from sage.combinat.partition import Partitions_n as Partitions_n
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.rational_field import QQ as QQ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Macdonald(UniqueRepresentation):
    @staticmethod
    def __classcall__(cls, Sym, q: str = 'q', t: str = 't'):
        """
        Normalize the arguments.

        TESTS::

            sage: R.<q, t> = QQ[]
            sage: B1 = SymmetricFunctions(R).macdonald().P()
            sage: B2 = SymmetricFunctions(R).macdonald(q, t).P()
            sage: B3 = SymmetricFunctions(R).macdonald(t, q).P()
            sage: B1 is B2
            True
            sage: B1 == B3
            False
        """
    q: Incomplete
    t: Incomplete
    def __init__(self, Sym, q, t) -> None:
        """
        Macdonald Symmetric functions including `P`, `Q`, `J`, `H`, `Ht` bases
        also including the S basis which is the plethystic transformation
        of the Schur basis (that which is dual to the Schur basis
        with respect to the Macdonald `q,t`-scalar product)

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        EXAMPLES::

            sage: t = QQ['t'].gen(); SymmetricFunctions(QQ['t'].fraction_field()).macdonald(q=t,t=1)
            Macdonald polynomials with q=t and t=1 over Fraction Field of Univariate Polynomial Ring in t over Rational Field
            sage: Sym = SymmetricFunctions(FractionField(QQ['t'])).macdonald()
            Traceback (most recent call last):
            ...
            TypeError: unable to evaluate 'q' in Fraction Field of Univariate Polynomial Ring in t over Rational Field
        """
    def base_ring(self):
        """
        Return the base ring of the symmetric functions where the
        Macdonald symmetric functions live.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the base ring associated to the corresponding symmetric function ring

        EXAMPLES::

            sage: Sym = SymmetricFunctions(QQ['q'].fraction_field())
            sage: Mac = Sym.macdonald(t=0)
            sage: Mac.base_ring()
            Fraction Field of Univariate Polynomial Ring in q over Rational Field
        """
    def symmetric_function_ring(self):
        """
        Return the base ring of the symmetric functions where the
        Macdonald symmetric functions live.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the symmetric function ring associated to the Macdonald bases

        EXAMPLES::

            sage: Mac = SymmetricFunctions(QQ['q'].fraction_field()).macdonald(t=0)
            sage: Mac.symmetric_function_ring()
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in q over Rational Field
        """
    def P(self):
        """
        Return Macdonald polynomials in `P` basis.
        The `P` basis is defined here as a normalized form of the `J` basis.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the `P` Macdonald basis of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: P = Sym.macdonald().P(); P
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald P basis
            sage: P[2]
            McdP[2]

        The `P` Macdonald basis is upper triangularly related to the monomial symmetric functions and are
        orthogonal with respect to the `qt`-Hall scalar product::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: P = Sym.macdonald().P(); P
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald P basis
            sage: m = Sym.monomial()
            sage: P.transition_matrix(m,2)
            [                          1 (q*t - q + t - 1)/(q*t - 1)]
            [                          0                           1]
            sage: P([1,1]).scalar_qt(P([2]))
            0
            sage: P([2]).scalar_qt(P([2]))
            (-q^3 + q^2 + q - 1)/(-q*t^2 + q*t + t - 1)
            sage: P([1,1]).scalar_qt(P([1,1]))
            (-q^2*t + q*t + q - 1)/(-t^3 + t^2 + t - 1)

        When `q = 0`, the Macdonald polynomials on the `P` basis are the same
        as the Hall-Littlewood polynomials on the `P` basis.

        ::

            sage: Sym = SymmetricFunctions(FractionField(QQ['t']))
            sage: P = Sym.macdonald(q=0).P(); P
            Symmetric Functions over Fraction Field of Univariate Polynomial Ring in t over Rational Field in the Macdonald P with q=0 basis
            sage: P([2])^2
            (t+1)*McdP[2, 2] + (-t+1)*McdP[3, 1] + McdP[4]
            sage: HLP = Sym.hall_littlewood().P()
            sage: HLP([2])^2
            (t+1)*HLP[2, 2] + (-t+1)*HLP[3, 1] + HLP[4]

        Coercions from the `Q` and `J` basis (proportional) are
        implemented::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: P = Sym.macdonald().P()
            sage: Q = Sym.macdonald().Q()
            sage: J = Sym.macdonald().J()
            sage: s = Sym.schur()

        ::

            sage: P(Q([2]))
            ((q*t^2-q*t-t+1)/(q^3-q^2-q+1))*McdP[2]
            sage: P(Q([2,1]))
            -((q*t^4-2*q*t^3+q*t^2-t^2+2*t-1)/(-q^4*t+2*q^3*t-q^2*t+q^2-2*q+1))*McdP[2, 1]

        ::

            sage: P(J([2]))
            (q*t^2-q*t-t+1)*McdP[2]
            sage: P(J([2,1]))
            -(q*t^4-2*q*t^3+q*t^2-t^2+2*t-1)*McdP[2, 1]

        By transitivity, one get coercions from the classical bases::

            sage: P(s([2]))
            ((q-t)/(q*t-1))*McdP[1, 1] + McdP[2]
            sage: P(s([2,1]))
            ((q*t-t^2+q-t)/(q*t^2-1))*McdP[1, 1, 1] + McdP[2, 1]

        ::

            sage: Sym = SymmetricFunctions(QQ['x','y','z'].fraction_field())
            sage: (x,y,z) = Sym.base_ring().gens()
            sage: Macxy = Sym.macdonald(q=x,t=y)
            sage: Macyz = Sym.macdonald(q=y,t=z)
            sage: Maczx = Sym.macdonald(q=z,t=x)
            sage: P1 = Macxy.P()
            sage: P2 = Macyz.P()
            sage: P3 = Maczx.P()
            sage: m(P1[2,1])
            -((2*x*y^2-x*y+y^2-x+y-2)/(-x*y^2+1))*m[1, 1, 1] + m[2, 1]
            sage: m(P2[2,1])
            -((2*y*z^2-y*z+z^2-y+z-2)/(-y*z^2+1))*m[1, 1, 1] + m[2, 1]
            sage: m(P1(P2(P3[2,1])))
            -((2*x^2*z+x^2-x*z+x-z-2)/(-x^2*z+1))*m[1, 1, 1] + m[2, 1]
            sage: P1(P2[2])
            -((x*y^2-2*x*y*z+y^2*z+x-2*y+z)/(x*y^2*z-x*y-y*z+1))*McdP[1, 1] + McdP[2]
            sage: m(z*P1[2]+x*P2[2])
            ((x^2*y^2*z+x*y^2*z^2-x^2*y^2+x^2*y*z-x*y*z^2+y^2*z^2-x^2*y-2*x*y*z-y*z^2+x*y-y*z+x+z)/(x*y^2*z-x*y-y*z+1))*m[1, 1] + (x+z)*m[2]
        """
    def Q(self):
        """
        Return the Macdonald polynomials on the `Q` basis. These are dual to
        the Macdonald polynomials on the P basis with respect to the
        `qt`-Hall scalar product.
        The `Q` basis is defined to be a normalized form of the `J` basis.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the `Q` Macdonald basis of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: Q = Sym.macdonald().Q(); Q
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald Q basis
            sage: P = Sym.macdonald().P()
            sage: Q([2]).scalar_qt(P([2]))
            1
            sage: Q([2]).scalar_qt(P([1,1]))
            0
            sage: Q([1,1]).scalar_qt(P([2]))
            0
            sage: Q([1,1]).scalar_qt(P([1,1]))
            1
            sage: Q(P([2]))
            ((q^3-q^2-q+1)/(q*t^2-q*t-t+1))*McdQ[2]
            sage: Q(P([1,1]))
            ((q^2*t-q*t-q+1)/(t^3-t^2-t+1))*McdQ[1, 1]


        Coercions from the `P` and `J` basis (proportional) are implemented::

            sage: P = Sym.macdonald().P()
            sage: Q = Sym.macdonald().Q()
            sage: J = Sym.macdonald().J()
            sage: s = Sym.schur()

        ::

            sage: Q(J([2]))
            (q^3-q^2-q+1)*McdQ[2]

        ::

            sage: Q(P([2]))
            ((q^3-q^2-q+1)/(q*t^2-q*t-t+1))*McdQ[2]
            sage: P(Q(P([2])))
            McdP[2]
            sage: Q(P(Q([2])))
            McdQ[2]

        By transitivity, one gets coercions from the classical bases::

            sage: Q(s([2]))
            ((q^2-q*t-q+t)/(t^3-t^2-t+1))*McdQ[1, 1] + ((q^3-q^2-q+1)/(q*t^2-q*t-t+1))*McdQ[2]
        """
    def J(self):
        """
        Return the Macdonald polynomials on the `J` basis also known as the
        integral form of the Macdonald polynomials. These are scalar
        multiples of both the `P` and `Q` bases. When expressed in the `P` or `Q`
        basis, the scaling coefficients are polynomials in `q` and `t` rather
        than rational functions.

        The `J` basis is calculated using determinantal formulas of
        Lapointe-Lascoux-Morse giving the action on the S-basis [LLM1998]_.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the `J` Macdonald basis of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: J = Sym.macdonald().J(); J
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald J basis
            sage: P = Sym.macdonald().P()
            sage: Q = Sym.macdonald().Q()
            sage: P(J([2]))
            (q*t^2-q*t-t+1)*McdP[2]
            sage: P(J([1,1]))
            (t^3-t^2-t+1)*McdP[1, 1]
            sage: Q(J([2]))
            (q^3-q^2-q+1)*McdQ[2]
            sage: Q(J([1,1]))
            (q^2*t-q*t-q+1)*McdQ[1, 1]

        Coercions from the `Q` and `J` basis (proportional) and to/from
        the Schur basis are implemented::

            sage: P = Sym.macdonald().P()
            sage: Q = Sym.macdonald().Q()
            sage: J = Sym.macdonald().J()
            sage: s = Sym.schur()

        ::

            sage: J(P([2]))
            (1/(q*t^2-q*t-t+1))*McdJ[2]

        ::

            sage: J(Q([2]))
            (1/(q^3-q^2-q+1))*McdJ[2]

        ::

            sage: s(J([2]))
            -(q*t-t^2-q+t)*s[1, 1] + (q*t^2-q*t-t+1)*s[2]
            sage: J(s([2]))
            ((q-t)/(q*t^4-q*t^3-q*t^2-t^3+q*t+t^2+t-1))*McdJ[1, 1] + (1/(q*t^2-q*t-t+1))*McdJ[2]
        """
    def H(self):
        """
        Return the Macdonald polynomials on the H basis. When the `H` basis
        is expanded on the Schur basis, the coefficients are the `qt`-Kostka
        numbers.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the `H` Macdonald basis of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: H = Sym.macdonald().H(); H
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald H basis
            sage: s = Sym.schur()
            sage: s(H([2]))
            q*s[1, 1] + s[2]
            sage: s(H([1,1]))
            s[1, 1] + t*s[2]

        Coercions to/from the Schur basis are implemented::

            sage: H = Sym.macdonald().H()
            sage: s = Sym.schur()
            sage: H(s([2]))
            (q/(q*t-1))*McdH[1, 1] - (1/(q*t-1))*McdH[2]
        """
    def Ht(self):
        """
        Return the Macdonald polynomials on the `Ht` basis. The elements of
        the `Ht` basis are eigenvectors of the `nabla` operator. When expanded
        on the Schur basis, the coefficients are the modified `qt`-Kostka
        numbers.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the `Ht` Macdonald basis of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: Ht = Sym.macdonald().Ht(); Ht
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t over Rational Field in the Macdonald Ht basis
            sage: [Ht(p).nabla() for p in Partitions(3)]
            [q^3*McdHt[3], q*t*McdHt[2, 1], t^3*McdHt[1, 1, 1]]

        ::

            sage: s = Sym.schur()
            sage: from sage.combinat.sf.macdonald import qt_kostka
            sage: q,t = Ht.base_ring().gens()
            sage: s(Ht([2,1]))
            q*t*s[1, 1, 1] + (q+t)*s[2, 1] + s[3]
            sage: qt_kostka([1,1,1],[2,1]).subs(t=1/t)*t^Partition([2,1]).weighted_size()
            q*t
            sage: qt_kostka([2,1],[2,1]).subs(t=1/t)*t^Partition([2,1]).weighted_size()
            q + t
            sage: qt_kostka([3],[2,1]).subs(t=1/t)*t^Partition([2,1]).weighted_size()
            1

        Coercions to/from the Schur basis are implemented::

            sage: Ht = Sym.macdonald().Ht()
            sage: s = Sym.schur()
            sage: Ht(s([2,1]))
            (q/(q*t^2-t^3-q^2+q*t))*McdHt[1, 1, 1] - ((q^2+q*t+t^2)/(q^2*t^2-q^3-t^3+q*t))*McdHt[2, 1]
            + (t/(-q^3+q^2*t+q*t-t^2))*McdHt[3]
            sage: Ht(s([2]))
            -(q/(-q+t))*McdHt[1, 1] + (t/(-q+t))*McdHt[2]
        """
    def S(self):
        """
        Return the modified Schur functions defined by the plethystic
        substitution `S_{\\mu} = s_{\\mu}[X(1-t)/(1-q)]`. When the
        Macdonald polynomials in the J basis are expressed in terms of the
        modified Schur functions at `q=0`, the coefficients are `qt`-Kostka numbers.

        INPUT:

        - ``self`` -- a family of Macdonald symmetric function bases

        OUTPUT: the `S` Macdonald basis of symmetric functions

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: S = Sym.macdonald().S(); S
            Symmetric Functions over Fraction Field of Multivariate Polynomial Ring in q, t
            over Rational Field in the Macdonald S basis
            sage: p = Sym.power()
            sage: p(S[2,1])
            ((1/3*t^3-t^2+t-1/3)/(q^3-3*q^2+3*q-1))*p[1, 1, 1] - ((1/3*t^3-1/3)/(q^3-1))*p[3]
            sage: J = Sym.macdonald().J()
            sage: S(J([2]))
            (q^3-q^2-q+1)*McdS[2]
            sage: S(J([1,1]))
            (q^2*t-q*t-q+1)*McdS[1, 1] + (q^2-q*t-q+t)*McdS[2]
            sage: S = Sym.macdonald(q=0).S()
            sage: S(J[1,1])
            McdS[1, 1] + t*McdS[2]
            sage: S(J[2])
            q*McdS[1, 1] + McdS[2]
            sage: p(S[2,1])
            -(1/3*t^3-t^2+t-1/3)*p[1, 1, 1] + (1/3*t^3-1/3)*p[3]

            sage: from sage.combinat.sf.macdonald import qt_kostka
            sage: qt_kostka([2],[1,1])
            t
            sage: qt_kostka([1,1],[2])
            q

        Coercions to/from the Schur basis are implemented::

            sage: S = Sym.macdonald().S()
            sage: s = Sym.schur()
            sage: S(s([2]))
            ((q^2-q*t-q+t)/(t^3-t^2-t+1))*McdS[1, 1] - ((q^2*t-q*t-q+1)/(-t^3+t^2+t-1))*McdS[2]
            sage: s(S([1,1]))
            -((q*t^2-q*t-t+1)/(-q^3+q^2+q-1))*s[1, 1] + ((q*t-t^2-q+t)/(-q^3+q^2+q-1))*s[2]
        """

QQqt: Incomplete

def c1(part, q, t):
    """
    This function returns the qt-Hall scalar product between ``J(part)``
    and ``P(part)``.

    This coefficient is `c_\\lambda` in equation (8.1') p. 352 of
    Macdonald's book [Mac1995]_.

    INPUT:

    - ``part`` -- a partition
    - ``q``, ``t`` -- parameters

    OUTPUT: a polynomial of the scalar product between the `J` and `P` bases

    EXAMPLES::

        sage: from sage.combinat.sf.macdonald import c1
        sage: R.<q,t> = QQ[]
        sage: c1(Partition([2,1]),q,t)
        -q^4*t + 2*q^3*t - q^2*t + q^2 - 2*q + 1
        sage: c1(Partition([1,1]),q,t)
        q^2*t - q*t - q + 1
    """
def c2(part, q, t):
    """
    This function returns the qt-Hall scalar product between J(part)
    and Q(part).

    This coefficient is `c_\\lambda` in equation (8.1) p. 352 of
    Macdonald's book [Mac1995]_.

    INPUT:

    - ``part`` -- a partition
    - ``q``, ``t`` -- parameters

    OUTPUT: a polynomial of the scalar product between the `J` and `P` bases

    EXAMPLES::

        sage: from sage.combinat.sf.macdonald import c2
        sage: R.<q,t> = QQ[]
        sage: c2(Partition([1,1]),q,t)
        t^3 - t^2 - t + 1
        sage: c2(Partition([2,1]),q,t)
        -q*t^4 + 2*q*t^3 - q*t^2 + t^2 - 2*t + 1
    """
@cached_function
def cmunu1(mu, nu):
    """
    Return the coefficient of `{\\tilde H}_\\nu` in `h_1^\\perp {\\tilde H}_\\mu`.

    INPUT:

    - ``mu``, ``nu`` -- partitions with ``nu`` precedes ``mu``

    OUTPUT: an element of the fraction field of polynomials in `q` and `t`

    EXAMPLES::

        sage: from sage.combinat.sf.macdonald import cmunu1
        sage: cmunu1(Partition([2,1]),Partition([2]))
        (-t^2 + q)/(q - t)
        sage: cmunu1(Partition([2,1]),Partition([1,1]))
        (-q^2 + t)/(-q + t)
        sage: Sym = SymmetricFunctions(QQ['q','t'].fraction_field())
        sage: h = Sym.h()
        sage: Ht = Sym.macdonald().Ht()
        sage: all(Ht[3,2,1].skew_by(h[1]).coefficient(nu)
        ....:     == cmunu1(Partition([3,2,1]),nu)
        ....:     for nu in Partition([3,2,1]).down_list())
        True
    """
@cached_function
def cmunu(mu, nu):
    """
    Return the coefficient of `{\\tilde H}_\\nu` in `h_r^\\perp {\\tilde H}_\\mu`.

    Proposition 5 of F. Bergeron and M. Haiman [BH2013]_ states

    .. MATH::

        c_{\\mu\\nu} = \\sum_{\\alpha \\leftarrow \\nu} c_{\\mu\\alpha}
        c_{\\alpha\\nu} B_{\\alpha/\\nu}/B_{\\mu/\\nu}

    where `c_{\\mu\\nu}` is the coefficient of `{\\tilde H}_\\nu` in
    `h_r^\\perp {\\tilde H}_\\mu` and `B_{\\mu/\\nu}` is the bi-exponent generator
    implemented in the function :func:`sage.combinat.sf.macdonald.Bmu`.

    INPUT:

    - ``mu``, ``nu`` -- partitions with ``nu`` contained in ``mu``

    OUTPUT: an element of the fraction field of polynomials in `q` and `t`

    EXAMPLES::

        sage: from sage.combinat.sf.macdonald import cmunu
        sage: cmunu(Partition([2,1]),Partition([1]))
        q + t + 1
        sage: cmunu(Partition([2,2]),Partition([1,1]))
        (-q^3 - q^2 + q*t + t)/(-q + t)
        sage: Sym = SymmetricFunctions(QQ['q','t'].fraction_field())
        sage: h = Sym.h()
        sage: Ht = Sym.macdonald().Ht()
        sage: all(Ht[2,2].skew_by(h[r]).coefficient(nu)
        ....:     == cmunu(Partition([2,2]),nu)
        ....:     for r in range(1,5) for nu in Partitions(4-r))
        True
    """

class MacdonaldPolynomials_generic(sfa.SymmetricFunctionAlgebra_generic):
    q: Incomplete
    t: Incomplete
    def __init__(self, macdonald) -> None:
        """
        A class for methods for one of the Macdonald bases of the symmetric functions.

        INPUT:

        - ``self`` -- a Macdonald basis
        - ``macdonald`` -- a family of Macdonald symmetric function bases

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q,t'])); Sym.rename('Sym'); Sym
            Sym
            sage: Sym.macdonald().P()
            Sym in the Macdonald P basis
            sage: Sym.macdonald(t=2).P()
            Sym in the Macdonald P with t=2 basis
            sage: Sym.rename()

        TESTS::

            sage: Sym.macdonald().P()._prefix
            'McdP'
            sage: Sym.macdonald().Ht()._prefix
            'McdHt'
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`SymmetricFunctionsFunctor` and `R` is a ring, such
        that ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q']))
            sage: J = Sym.macdonald(t=2).J()
            sage: J.construction()
            (SymmetricFunctionsFunctor[Macdonald J with t=2],
             Fraction Field of Univariate Polynomial Ring in q over Rational Field)
        """
    def c1(self, part):
        """
        Return the `qt`-Hall scalar product between ``J(part)`` and ``P(part)``.

        INPUT:

        - ``self`` -- a Macdonald basis
        - ``part`` -- a partition

        OUTPUT:

        - returns the `qt`-Hall scalar product between ``J(part)`` and ``P(part)``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: P = Sym.macdonald().P()
            sage: P.c1(Partition([2,1]))
            -q^4*t + 2*q^3*t - q^2*t + q^2 - 2*q + 1
        """
    def c2(self, part):
        """
        Return the `qt`-Hall scalar product between ``J(part)`` and ``Q(part)``.

        INPUT:

        - ``self`` -- a Macdonald basis
        - ``part`` -- a partition

        OUTPUT:

        - returns the `qt`-Hall scalar product between ``J(part)`` and ``Q(part)``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: P = Sym.macdonald().P()
            sage: P.c2(Partition([2,1]))
            -q*t^4 + 2*q*t^3 - q*t^2 + t^2 - 2*t + 1
        """
    def product(self, left, right):
        """
        Multiply an element of the Macdonald symmetric function
        basis ``self`` and another symmetric function

        Convert to the Schur basis, do the multiplication there, and
        convert back to ``self`` basis.

        INPUT:

        - ``self`` -- a Macdonald symmetric function basis
        - ``left`` -- an element of the basis ``self``
        - ``right`` -- another symmetric function

        OUTPUT: the product of ``left`` and ``right`` expanded in the basis ``self``

        EXAMPLES::

            sage: Mac = SymmetricFunctions(FractionField(QQ['q','t'])).macdonald()
            sage: H = Mac.H()
            sage: J = Mac.J()
            sage: P = Mac.P()
            sage: Q = Mac.Q()
            sage: Ht = Mac.Ht()
            sage: J([1])^2 #indirect doctest
            ((q-1)/(q*t-1))*McdJ[1, 1] + ((t-1)/(q*t-1))*McdJ[2]
            sage: J.product( J[1], J[2] )
            -((q^2-1)/(-q^2*t+1))*McdJ[2, 1] - ((t-1)/(-q^2*t+1))*McdJ[3]
            sage: H.product( H[1], H[2] )
            ((q^2-1)/(q^2*t-1))*McdH[2, 1] - ((t-1)/(-q^2*t+1))*McdH[3]
            sage: P.product( P[1], P[2] )
            -((q^3*t^2-q*t^2-q^2+1)/(-q^3*t^2+q^2*t+q*t-1))*McdP[2, 1] + McdP[3]
            sage: Q.product(Q[1],Q[2])
            McdQ[2, 1] + ((q^2*t-q^2+q*t-q+t-1)/(q^2*t-1))*McdQ[3]
            sage: Ht.product(Ht[1],Ht[2])
            ((q^2-1)/(q^2-t))*McdHt[2, 1] + ((t-1)/(-q^2+t))*McdHt[3]
        """
    def macdonald_family(self):
        """
        Return the family of Macdonald bases associated to the basis ``self``.

        INPUT:

        - ``self`` -- a Macdonald basis

        OUTPUT: the family of Macdonald symmetric functions associated to ``self``

        EXAMPLES::

            sage: MacP = SymmetricFunctions(QQ['q'].fraction_field()).macdonald(t=0).P()
            sage: MacP.macdonald_family()
            Macdonald polynomials with t=0 over Fraction Field of Univariate Polynomial Ring in q over Rational Field
        """
    class Element(sfa.SymmetricFunctionAlgebra_generic.Element):
        def nabla(self, q=None, t=None, power: int = 1):
            """
            Return the value of the nabla operator applied to ``self``.

            The eigenvectors of the nabla operator are the Macdonald
            polynomials in the `Ht` basis.  For more information
            see: [BGHT1999]_.

            The operator nabla acts on symmetric functions and has the
            Macdonald `Ht` basis as eigenfunctions and the eigenvalues
            are `q^{n(\\mu')} t^{n(\\mu)}` where
            `n(\\mu) = \\sum_{i} (i-1) \\mu_i` and `\\mu'` is the conjugate
            shape of `\\mu`.

            If the parameter ``power`` is an integer then it calculates
            nabla to that integer.  The default value of ``power`` is 1.

            INPUT:

            - ``self`` -- an element of a Macdonald basis
            - ``q``, ``t`` -- (optional) parameters to specialize
            - ``power`` -- integer (default: 1)

            OUTPUT: the symmetric function of `\\nabla` acting on ``self``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
                sage: P = Sym.macdonald().P()
                sage: P([1,1]).nabla()
                ((q^2*t+q*t^2-2*t)/(q*t-1))*McdP[1, 1] + McdP[2]
                sage: P([1,1]).nabla(t=1)
                ((q^2*t+q*t-t-1)/(q*t-1))*McdP[1, 1] + McdP[2]
                sage: H = Sym.macdonald().H()
                sage: H([1,1]).nabla()
                t*McdH[1, 1] - (t^2-1)*McdH[2]
                sage: H([1,1]).nabla(q=1)
                ((t^2+q-t-1)/(q*t-1))*McdH[1, 1] - ((t^3-t^2-t+1)/(q*t-1))*McdH[2]
                sage: H(0).nabla()
                0
                sage: H([2,2,1]).nabla(t=1/H.t)
                -(q^2/(-t^4))*McdH[2, 2, 1]
                sage: H([2,2,1]).nabla(t=1/H.t,power=-1)
                -(t^4/(-q^2))*McdH[2, 2, 1]
            """

class MacdonaldPolynomials_p(MacdonaldPolynomials_generic):
    def __init__(self, macdonald) -> None:
        '''
        The `P` basis is defined here as the `J` basis times a
        normalizing coefficient `c2`.

        INPUT:

        - ``self`` -- a Macdonald `P` basis
        - ``macdonald`` -- a family of Macdonald bases

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
            sage: P = Sym.macdonald().P()
            sage: TestSuite(P).run(skip=["_test_associativity","_test_distributivity","_test_prod"])  # long time (20s on sage.math, 2012)
            sage: TestSuite(P).run(elements = [P.t*P[1,1]+P.q*P[2], P[1]+(P.q+P.t)*P[1,1]])  # long time (depends on previous)
        '''
    def scalar_qt_basis(self, part1, part2=None):
        """
        Return the scalar product of `P(part1)` and `P(part2)`
        This scalar product formula is given in equation (4.11) p.323
        and (6.19) p.339 of Macdonald's book [Mac1995]_.

        INPUT:

        - ``self`` -- a Macdonald `P` basis
        - ``part1``, ``part2`` -- partitions

        OUTPUT:

        - returns the scalar product of ``P(part1)`` and ``P(part2)``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: P = Sym.macdonald().P()
            sage: P.scalar_qt_basis(Partition([2,1]), Partition([1,1,1]))
            0
            sage: f = P.scalar_qt_basis(Partition([3,2,1]), Partition([3,2,1]))
            sage: factor(f.numerator())
            (q - 1)^3 * (q^2*t - 1)^2 * (q^3*t^2 - 1)
            sage: factor(f.denominator())
            (t - 1)^3 * (q*t^2 - 1)^2 * (q^2*t^3 - 1)

        With a single argument, takes `part2 = part1`::

            sage: P.scalar_qt_basis(Partition([2,1]), Partition([2,1]))
            (-q^4*t + 2*q^3*t - q^2*t + q^2 - 2*q + 1)/(-q*t^4 + 2*q*t^3 - q*t^2 + t^2 - 2*t + 1)
        """
    class Element(MacdonaldPolynomials_generic.Element): ...

class MacdonaldPolynomials_q(MacdonaldPolynomials_generic):
    def __init__(self, macdonald) -> None:
        '''
        The `Q` basis is defined here as the `J` basis times a
        normalizing coefficient.

        INPUT:

        - ``self`` -- a Macdonald `Q` basis
        - ``macdonald`` -- a family of Macdonald bases

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
            sage: Q = Sym.macdonald().Q()
            sage: TestSuite(Q).run(skip=["_test_associativity","_test_distributivity","_test_prod"])  # long time (29s on sage.math, 2012)
            sage: TestSuite(Q).run(elements = [Q.t*Q[1,1]+Q.q*Q[2], Q[1]+(Q.q+Q.t)*Q[1,1]])  # long time (depends on previous)
        '''
    class Element(MacdonaldPolynomials_generic.Element): ...

class MacdonaldPolynomials_j(MacdonaldPolynomials_generic):
    def __init__(self, macdonald) -> None:
        '''
        The `J` basis is calculated using determinantal formulas of
        Lapointe-Lascoux-Morse giving the action on the `S`-basis.

        INPUT:

        - ``self`` -- a Macdonald `J` basis
        - ``macdonald`` -- a family of Macdonald bases

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
            sage: J = Sym.macdonald().J()
            sage: TestSuite(J).run(skip=["_test_associativity","_test_distributivity","_test_prod"])  # long time (19s on sage.math, 2012)
            sage: TestSuite(J).run(elements = [J.t*J[1,1]+J.q*J[2], J[1]+(J.q+J.t)*J[1,1]])  # long time (depends on previous)
        '''
    class Element(MacdonaldPolynomials_generic.Element): ...

class MacdonaldPolynomials_h(MacdonaldPolynomials_generic):
    def __init__(self, macdonald) -> None:
        '''
        The `H` basis is defined as `H_\\mu = \\sum_{\\lambda} K_{\\lambda\\mu}(q,t) s_\\lambda`
        where `K_{\\lambda\\mu}(q,t)` are the Macdonald Kostka coefficients.

        In this implementation, it is calculated by using the Macdonald `Ht` basis and
        substituting `t \\rightarrow 1/t` and multiplying by `t^{n(\\mu)}`.

        INPUT:

        - ``self`` -- a Macdonald `H` basis
        - ``macdonald`` -- a family of Macdonald bases

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
            sage: H = Sym.macdonald().H()
            sage: TestSuite(H).run(skip=["_test_associativity","_test_distributivity","_test_prod"])
            sage: TestSuite(H).run(elements = [H.t*H[1,1]+H.q*H[2], H[1]+(H.q+H.t)*H[1,1]])  # long time (26s on sage.math, 2012)
        '''
    class Element(MacdonaldPolynomials_generic.Element): ...

class MacdonaldPolynomials_ht(MacdonaldPolynomials_generic):
    def __init__(self, macdonald) -> None:
        '''
        The `Ht` basis is defined as `{\\tilde H}_\\mu = t^{n(\\mu)} \\sum_{\\lambda}
        K_{\\lambda\\mu}(q,t^{-1}) s_\\lambda` where `K_{\\lambda\\mu}(q,t)` are the
        Macdonald `(q,t)`-Kostka coefficients and `n(\\mu) = \\sum_{i} (i-1) \\mu_i`.

        It is implemented here by using a Pieri formula due to F. Bergeron
        and M. Haiman [BH2013]_.

        INPUT:

        - ``self`` -- a Macdonald `Ht` basis
        - ``macdonald`` -- a family of Macdonald bases

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
            sage: Ht = Sym.macdonald().Ht()
            sage: TestSuite(Ht).run(skip=["_test_associativity","_test_distributivity","_test_prod"])  # long time (26s on sage.math, 2012)
            sage: TestSuite(Ht).run(elements = [Ht.t*Ht[1,1]+Ht.q*Ht[2], Ht[1]+(Ht.q+Ht.t)*Ht[1,1]])  # long time (depends on previous)
        '''
    class Element(MacdonaldPolynomials_generic.Element):
        def nabla(self, q=None, t=None, power: int = 1):
            """
            Return the value of the nabla operator applied to ``self``. The
            eigenvectors of the `nabla` operator are the Macdonald polynomials in
            the `Ht` basis.  For more information see: [BGHT1999]_.

            The operator `nabla` acts on symmetric functions and has the
            Macdonald `Ht` basis as eigenfunctions and the eigenvalues
            are `q^{n(\\mu')} t^{n(\\mu)}` where `n(\\mu) = \\sum_{i} (i-1) \\mu_i`.

            If the parameter ``power`` is an integer then it calculates
            nabla to that integer.  The default value of ``power`` is 1.

            INPUT:

            - ``self`` -- an element of the Macdonald `Ht` basis
            - ``q``, ``t`` -- (optional) parameters to specialize
            - ``power`` -- integer (default: 1)

            OUTPUT: the symmetric function of `\\nabla` acting on ``self``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
                sage: Ht = Sym.macdonald().Ht()
                sage: t = Ht.t; q = Ht.q
                sage: s = Sym.schur()
                sage: a = sum(Ht(p) for p in Partitions(3))
                sage: Ht(0).nabla()
                0
                sage: a.nabla() == t^3*Ht([1,1,1])+q*t*Ht([2,1]) + q^3*Ht([3])
                True
                sage: a.nabla(t=3) == 27*Ht([1,1,1])+3*q*Ht([2,1]) + q^3*Ht([3])
                True
                sage: a.nabla(q=3) == t^3*Ht([1,1,1])+3*t*Ht([2,1]) + 27*Ht([3])
                True
                sage: Ht[2,1].nabla(power=-1)
                1/(q*t)*McdHt[2, 1]
                sage: Ht[2,1].nabla(power=4)
                q^4*t^4*McdHt[2, 1]
                sage: s(a.nabla(q=3))
                (t^6+27*q^3+3*q*t^2)*s[1, 1, 1] + (t^5+t^4+27*q^2+3*q*t+3*t^2+27*q)*s[2, 1] + (t^3+3*t+27)*s[3]
                sage: Ht = Sym.macdonald(q=3).Ht()
                sage: a = sum(Ht(p) for p in Partitions(3))
                sage: s(a.nabla())
                (t^6+9*t^2+729)*s[1, 1, 1] + (t^5+t^4+3*t^2+9*t+324)*s[2, 1] + (t^3+3*t+27)*s[3]
            """

class MacdonaldPolynomials_s(MacdonaldPolynomials_generic):
    def __init__(self, macdonald) -> None:
        '''
        An implementation of the basis `s_\\lambda[(1-t)X/(1-q)]`.

        This is perhaps misnamed as a \'Macdonald\' basis for
        the symmetric functions but is used in the calculation
        of the Macdonald `J` basis (see method \'creation\' below)
        but does use both of the two parameters and can be
        specialized to `s_\\lambda[(1-t)X]` and `s_\\lambda[X/(1-t)]`.

        INPUT:

        - ``self`` -- a Macdonald `S` basis
        - ``macdonald`` -- a family of Macdonald bases

        TESTS::

            sage: Sym = SymmetricFunctions(FractionField(QQ[\'q\',\'t\']))
            sage: S = Sym.macdonald().S()
            sage: TestSuite(S).run(skip=["_test_associativity","_test_distributivity","_test_prod"])
            sage: TestSuite(S).run(elements = [S.t*S[1,1]+S.q*S[2], S[1]+(S.q+S.t)*S[1,1]])
        '''
    def product(self, left, right):
        """
        The multiplication of the modified Schur functions behaves the same
        as the multiplication of the Schur functions.

        INPUT:

        - ``self`` -- a Macdonald `S` basis
        - ``left``, ``right`` -- a symmetric functions

        OUTPUT: the product of ``left`` and ``right``

        EXAMPLES::

            sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
            sage: S = Sym.macdonald().S()
            sage: S([2])^2 #indirect doctest
            McdS[2, 2] + McdS[3, 1] + McdS[4]
        """
    class Element(MacdonaldPolynomials_generic.Element):
        def creation(self, k):
            """
            This function is a creation operator for the J-basis
            for which the action is known on the 'Macdonald' S-basis
            by formula from [LLM1998]_.

            INPUT:

            - ``self`` -- an element of the Macdonald `S` basis
            - ``k`` -- positive integer

            OUTPUT: the column adding operator on the `J` basis on ``self``

            EXAMPLES::

                sage: Sym = SymmetricFunctions(FractionField(QQ['q','t']))
                sage: S = Sym.macdonald().S()
                sage: a = S(1)
                sage: a.creation(1)
                -(q-1)*McdS[1]
                sage: a.creation(2)
                (q^2*t-q*t-q+1)*McdS[1, 1] + (q^2-q*t-q+t)*McdS[2]
            """

def qt_kostka(lam, mu):
    """
    Return the `K_{\\lambda\\mu}(q,t)` by computing the change
    of basis from the Macdonald H basis to the Schurs.

    INPUT:

    - ``lam``, ``mu`` -- partitions of the same size

    OUTPUT:

    - returns the `q,t`-Kostka polynomial indexed by the
      partitions ``lam`` and ``mu``

    EXAMPLES::

        sage: from sage.combinat.sf.macdonald import qt_kostka
        sage: qt_kostka([2,1,1],[1,1,1,1])
        t^3 + t^2 + t
        sage: qt_kostka([1,1,1,1],[2,1,1])
        q
        sage: qt_kostka([1,1,1,1],[3,1])
        q^3
        sage: qt_kostka([1,1,1,1],[1,1,1,1])
        1
        sage: qt_kostka([2,1,1],[2,2])
        q^2*t + q*t + q
        sage: qt_kostka([2,2],[2,2])
        q^2*t^2 + 1
        sage: qt_kostka([4],[3,1])
        t
        sage: qt_kostka([2,2],[3,1])
        q^2*t + q
        sage: qt_kostka([3,1],[2,1,1])
        q*t^3 + t^2 + t
        sage: qt_kostka([2,1,1],[2,1,1])
        q*t^2 + q*t + 1
        sage: qt_kostka([2,1],[1,1,1,1])
        0
    """
