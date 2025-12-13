from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationFields as CompleteDiscreteValuationFields, CompleteDiscreteValuationRings as CompleteDiscreteValuationRings
from sage.categories.fields import Fields as Fields
from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.rings import Rings as Rings
from sage.categories.unique_factorization_domains import UniqueFactorizationDomains as UniqueFactorizationDomains
from sage.data_structures.stream import Stream_exact as Stream_exact, Stream_function as Stream_function, Stream_iterator as Stream_iterator, Stream_taylor as Stream_taylor, Stream_uninitialized as Stream_uninitialized, Stream_zero as Stream_zero
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.lazy_series import LazyCompletionGradedAlgebraElement as LazyCompletionGradedAlgebraElement, LazyDirichletSeries as LazyDirichletSeries, LazyLaurentSeries as LazyLaurentSeries, LazyModuleElement as LazyModuleElement, LazyPowerSeries as LazyPowerSeries, LazyPowerSeries_gcd_mixin as LazyPowerSeries_gcd_mixin, LazySymmetricFunction as LazySymmetricFunction
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.element import parent as parent
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class LazySeriesRing(UniqueRepresentation, Parent):
    """
    Abstract base class for lazy series.
    """
    @staticmethod
    def __classcall_private__(cls, base_ring, names, sparse: bool = True, *args, **kwds):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: Lp = LazyLaurentSeriesRing(QQ, 'z')
            sage: L is Lp
            True
        """
    def undefined(self, valuation=None, name=None):
        """
        Return an uninitialized series.

        INPUT:

        - ``valuation`` -- integer; a lower bound for the valuation
          of the series
        - ``name`` -- string; a name that refers to the undefined
          stream in error messages

        Power series can be defined recursively (see
        :meth:`sage.rings.lazy_series.LazyModuleElement.define` for
        more examples).

        .. SEEALSO::

            :meth:`sage.rings.padics.generic_nodes.pAdicRelaxedGeneric.unknown`

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: s = L.undefined(1)
            sage: s.define(z + (s^2+s(z^2))/2)
            sage: s
            z + z^2 + z^3 + 2*z^4 + 3*z^5 + 6*z^6 + 11*z^7 + O(z^8)

        Alternatively::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: f = L(None, valuation=-1)
            sage: f.define(z^-1 + z^2*f^2)
            sage: f
            z^-1 + 1 + 2*z + 5*z^2 + 14*z^3 + 42*z^4 + 132*z^5 + O(z^6)
        """
    unknown = undefined
    def define_implicitly(self, series, equations, max_lookahead: int = 1) -> None:
        '''
        Define series by solving functional equations.

        INPUT:

        - ``series`` -- list of undefined series or pairs each
          consisting of a series and its initial values
        - ``equations`` -- list of equations defining the series
        - ``max_lookahead``-- (default: ``1``); a positive integer
          specifying how many elements beyond the currently known
          (i.e., approximate) order of each equation to extract
          linear equations from

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = L.undefined(0)
            sage: F = diff(f, 2)
            sage: L.define_implicitly([(f, [1, 0])], [F + f])
            sage: f
            1 - 1/2*z^2 + 1/24*z^4 - 1/720*z^6 + O(z^7)
            sage: cos(z)
            1 - 1/2*z^2 + 1/24*z^4 - 1/720*z^6 + O(z^7)
            sage: F
            -1 + 1/2*z^2 - 1/24*z^4 + 1/720*z^6 + O(z^7)

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = L.undefined(0)
            sage: L.define_implicitly([f], [2*z*f(z^3) + z*f^3 - 3*f + 3])
            sage: f
            1 + z + z^2 + 2*z^3 + 5*z^4 + 11*z^5 + 28*z^6 + O(z^7)

        From Exercise 6.63b in [EnumComb2]_::

            sage: g = L.undefined()
            sage: z1 = z*diff(g, z)
            sage: z2 = z1 + z^2 * diff(g, z, 2)
            sage: z3 = z1 + 3 * z^2 * diff(g, z, 2) + z^3 * diff(g, z, 3)
            sage: e1 = g^2 * z3 - 15*g*z1*z2 + 30*z1^3
            sage: e2 = g * z2 - 3 * z1^2
            sage: e3 = g * z2 - 3 * z1^2
            sage: e = e1^2 + 32 * e2^3 - g^10 * e3^2
            sage: L.define_implicitly([(g, [1, 2])], [e])

            sage: sol = L(lambda n: 1 if not n else (2 if is_square(n) else 0)); sol
            1 + 2*z + 2*z^4 + O(z^7)
            sage: all(g[i] == sol[i] for i in range(50))
            True

        Some more examples over different rings::

            sage: # needs sage.symbolic
            sage: L.<z> = LazyPowerSeriesRing(SR)
            sage: G = L.undefined(0)
            sage: L.define_implicitly([(G, [ln(2)])], [diff(G) - exp(-G(-z))])
            sage: G
            log(2) + z + 1/2*z^2 + (-1/12*z^4) + 1/45*z^6 + O(z^7)

            sage: L.<z> = LazyPowerSeriesRing(RR)
            sage: G = L.undefined(0)
            sage: L.define_implicitly([(G, [log(2)])], [diff(G) - exp(-G(-z))])
            sage: G
            0.693147180559945 + 1.00000000000000*z + 0.500000000000000*z^2
             - 0.0833333333333333*z^4 + 0.0222222222222222*z^6 + O(1.00000000000000*z^7)

        We solve the recurrence relation in (3.12) of Prellberg and Brak
        :doi:`10.1007/BF02183685`::

            sage: q, y = QQ[\'q,y\'].fraction_field().gens()
            sage: L.<x> = LazyPowerSeriesRing(q.parent())
            sage: R = L.undefined()
            sage: L.define_implicitly([(R, [0])], [(1-q*x)*R - (y*q*x+y)*R(q*x) - q*x*R*R(q*x) - x*y*q])
            sage: R[0]
            0
            sage: R[1]
            (-q*y)/(q*y - 1)
            sage: R[2]
            (q^3*y^2 + q^2*y)/(q^3*y^2 - q^2*y - q*y + 1)
            sage: R[3].factor()
            (-1) * y * q^3 * (q*y - 1)^-2 * (q^2*y - 1)^-1 * (q^3*y - 1)^-1
             * (q^4*y^3 + q^3*y^2 + q^2*y^2 - q^2*y - q*y - 1)

            sage: Rp = L.undefined(1)
            sage: L.define_implicitly([Rp], [(y*q*x+y)*Rp(q*x) + q*x*Rp*Rp(q*x) + x*y*q - (1-q*x)*Rp])
            sage: all(R[n] == Rp[n] for n in range(7))
            True

        Another example::

            sage: L.<z> = LazyPowerSeriesRing(QQ["x,y,f1,f2"].fraction_field())
            sage: L.base_ring().inject_variables()
            Defining x, y, f1, f2
            sage: F = L.undefined()
            sage: L.define_implicitly([(F, [0, f1, f2])], [F(2*z) - (1+exp(x*z)+exp(y*z))*F - exp((x+y)*z)*F(-z)])
            sage: F
            f1*z + f2*z^2 + ((-1/6*x*y*f1+1/3*x*f2+1/3*y*f2)*z^3)
             + ((-1/24*x^2*y*f1-1/24*x*y^2*f1+1/12*x^2*f2+1/12*x*y*f2+1/12*y^2*f2)*z^4)
             + ... + O(z^8)
            sage: sol = 1/(x-y)*((2*f2-y*f1)*(exp(x*z)-1)/x - (2*f2-x*f1)*(exp(y*z)-1)/y)
            sage: F - sol
            O(z^7)

        We need to specify the initial values for the degree 1 and 2
        components to get a unique solution in the previous example::

            sage: L.<z> = LazyPowerSeriesRing(QQ[\'x\',\'y\',\'f1\'].fraction_field())
            sage: L.base_ring().inject_variables()
            Defining x, y, f1
            sage: F = L.undefined()
            sage: L.define_implicitly([F], [F(2*z) - (1+exp(x*z)+exp(y*z))*F - exp((x+y)*z)*F(-z)])
            sage: F
            <repr(...) failed: ValueError: could not determine any coefficients:
                coefficient [3]: 6*series[3] + (-2*x - 2*y)*series[2] + (x*y)*series[1] == 0>

        Let us now try to only specify the degree 0 and degree 1
        components.  We will see that this is still not enough to
        remove the ambiguity, so an error is raised.  However, we
        will see that the dependence on ``series[1]`` disappears.
        The equation which has no unique solution is now
        ``6*series[3] + (-2*x - 2*y)*series[2] + (x*y*f1) == 0``.::

            sage: F = L.undefined()
            sage: L.define_implicitly([(F, [0, f1])], [F(2*z) - (1+exp(x*z)+exp(y*z))*F - exp((x+y)*z)*F(-z)])
            sage: F
            <repr(...) failed: ValueError: could not determine any coefficients:
                coefficient [3]: ... == 0>

        (Note that the order of summands of the equation in the error
        message is not deterministic.)

        Laurent series examples::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: f = L.undefined(-1)
            sage: L.define_implicitly([(f, [5])], [2+z*f(z^2) - f])
            sage: f
            5*z^-1 + 2 + 2*z + 2*z^3 + O(z^6)
            sage: 2 + z*f(z^2) - f
            O(z^6)

            sage: g = L.undefined(-2)
            sage: L.define_implicitly([(g, [5])], [2+z*g(z^2) - g])
            sage: g
            <repr(...) failed: ValueError: no solution as the coefficient in degree -3 of the equation is 5 != 0>

        A bivariate example::

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: B = L.undefined()
            sage: eq = y*B^2 + 1 - B(x, x-y)
            sage: L.define_implicitly([B], [eq])
            sage: B
            1 + (x-y) + (2*x*y-2*y^2) + (4*x^2*y-7*x*y^2+3*y^3)
             + (2*x^3*y+6*x^2*y^2-18*x*y^3+10*y^4)
             + (30*x^3*y^2-78*x^2*y^3+66*x*y^4-18*y^5)
             + (28*x^4*y^2-12*x^3*y^3-128*x^2*y^4+180*x*y^5-68*y^6) + O(x,y)^7

        Knödel walks::

             sage: L.<z, x> = LazyPowerSeriesRing(QQ)
             sage: F = L.undefined()
             sage: eq = F(z, x)*(x^2*z-x+z) - (z - x*z^2 - x^2*z^2)*F(z, 0) + x
             sage: L.define_implicitly([F], [eq])
             sage: F
             1 + (2*z^2+z*x) + (z^3+z^2*x) + (5*z^4+3*z^3*x+z^2*x^2)
              + (5*z^5+4*z^4*x+z^3*x^2) + (15*z^6+10*z^5*x+4*z^4*x^2+z^3*x^3)
              + O(z,x)^7

        Bicolored rooted trees with black and white roots::

            sage: L.<x, y> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: B = L.undefined()
            sage: L.define_implicitly([A, B], [A - x*exp(B), B - y*exp(A)])
            sage: A
            x + x*y + (x^2*y+1/2*x*y^2) + (1/2*x^3*y+2*x^2*y^2+1/6*x*y^3)
            + (1/6*x^4*y+3*x^3*y^2+2*x^2*y^3+1/24*x*y^4)
            + (1/24*x^5*y+8/3*x^4*y^2+27/4*x^3*y^3+4/3*x^2*y^4+1/120*x*y^5)
            + O(x,y)^7

            sage: h = SymmetricFunctions(QQ).h()
            sage: S = LazySymmetricFunctions(h)
            sage: E = S(lambda n: h[n])
            sage: T = LazySymmetricFunctions(tensor([h, h]))
            sage: X = tensor([h[1],h[[]]])
            sage: Y = tensor([h[[]],h[1]])
            sage: A = T.undefined()
            sage: B = T.undefined()
            sage: T.define_implicitly([A, B], [A - X*E(B), B - Y*E(A)])
            sage: A[:3]
            [h[1] # h[], h[1] # h[1]]

        Permutations with two kinds of labels such that each cycle
        contains at least one element of each kind (defined
        implicitly to have a test)::

            sage: p = SymmetricFunctions(QQ).p()
            sage: S = LazySymmetricFunctions(p)
            sage: P = S(lambda n: sum(p[la] for la in Partitions(n)))
            sage: T = LazySymmetricFunctions(tensor([p, p]))
            sage: X = tensor([p[1],p[[]]])
            sage: Y = tensor([p[[]],p[1]])
            sage: A = T.undefined()
            sage: T.define_implicitly([A], [P(X)*P(Y)*A - P(X+Y)])
            sage: A[:4]
            [p[] # p[], 0, p[1] # p[1], p[1] # p[1, 1] + p[1, 1] # p[1]]

        The Frobenius character of labelled Dyck words::

            sage: h = SymmetricFunctions(QQ).h()
            sage: L.<t, u> = LazyPowerSeriesRing(h.fraction_field())
            sage: D = L.undefined()
            sage: s1 = L.sum(lambda n: h[n]*t^(n+1)*u^(n-1), 1)
            sage: L.define_implicitly([D], [u*D - u - u*s1*D - t*(D - D(t, 0))])
            sage: D
            h[] + h[1]*t^2 + ((h[1,1]+h[2])*t^4+h[2]*t^3*u)
             + ((h[1,1,1]+3*h[2,1]+h[3])*t^6+(2*h[2,1]+h[3])*t^5*u+h[3]*t^4*u^2)
             + O(t,u)^7

        TESTS::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: f = L.undefined(1)
            sage: L.define_implicitly([f], [log(1+f) - ~(1 + f) + 1])
            sage: f
            O(z^8)

            sage: f = L.undefined(0)
            sage: fp = f.derivative()
            sage: g = L(lambda n: 0 if n < 10 else 1, 0)
            sage: L.define_implicitly([f], [f.derivative() * g + f])
            sage: f[0]
            0
            sage: fp[0]
            0
            sage: fp[1]
            0
            sage: fp[2]
            0
            sage: f[1]
            0

        Some systems of coupled functional equations::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: B = L.undefined()
            sage: L.define_implicitly([A, B], [A - B, A + B + 2])
            sage: A
            -1 + O(z^7)
            sage: B
            -1 + O(z^7)

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: B = L.undefined()
            sage: FA = A^2 + B - 2 - z*B
            sage: FB = B^2 - A
            sage: L.define_implicitly([(A, [1]), (B, [1])], [FA, FB])
            sage: A^2 + B - 2 - z*B
            O(z^7)
            sage: B^2 - A
            O(z^7)

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: B = L.undefined()
            sage: FA = A^2 + B^2 - 2 - z*B
            sage: FB = B^3 + 2*A^3 - 3 - z*(A + B)
            sage: L.define_implicitly([(A, [1]), (B, [1])], [FA, FB])
            sage: A^2 + B^2 - 2 - z*B
            O(z^7)
            sage: B^3 + 2*A^3 - 3 - z*(A + B)
            O(z^7)

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined(valuation=3)
            sage: B = L.undefined(valuation=2)
            sage: C = L.undefined(valuation=2)
            sage: FA = (A^2 + B^2)*z^2
            sage: FB = A*B*z
            sage: FC = (A + B + C)*z^2
            sage: L.define_implicitly([A, B, C], [FA, FB, FC])
            sage: A
            O(z^10)
            sage: B
            O(z^16)
            sage: C
            O(z^23)

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: B = L.undefined()
            sage: C = L.undefined()
            sage: L.define_implicitly([A, B, C], [B - C - 1, B*z + 2*C + 1, A + 2*C + 1])
            sage: A + 2*C + 1
            O(z^7)

        The following system does not determine `B`, but the solver
        will inductively discover that each coefficient of `A` must
        be zero.  Therefore, asking for a coefficient of `B` will
        loop forever::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: B = L.undefined()
            sage: C = L.undefined()
            sage: D = L.undefined()
            sage: L.define_implicitly([(A, [0,0,0]), (B, [0,0]), (C, [0,0]), (D, [0,0])], [C^2 + D^2, A + B + C + D, A*D])
            sage: B[2]  # not tested

        A bivariate example involving composition of series::

            sage: R.<z,q> = LazyPowerSeriesRing(QQ)
            sage: g = R.undefined()
            sage: R.define_implicitly([g], [g - (z*q + z*g*~(1-g))])
            sage: g
            z*q + z^2*q + z^3*q + (z^4*q+z^3*q^2) + (z^5*q+3*z^4*q^2) + O(z,q)^7

        The following does not work, because the equations
        determining the coefficients come in bad order::

            sage: L.<x,y,t> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined(name="A")
            sage: B = L.undefined(name="B")
            sage: eq0 = t*x*y*B(0, 0, t) + (t - x*y)*A(x, y, t) + x*y - t*A(0, y, t)
            sage: eq1 = (t*x-t)*B(0, y, t) + (t - x*y)*B(x, y, t)
            sage: L.define_implicitly([A, B], [eq0, eq1])
            sage: A[1]
            Traceback (most recent call last):
            ...
            ValueError: could not determine any coefficients:
            equation 0:
                coefficient [x*y*t]: A[x*y] - A[t] == 0
            equation 1:
                coefficient [x*t^2]: B[x*t] + B[t] == 0
                coefficient [x*y*t]: B[x*y] - B[t] == 0

        Check the error message in the case of symmetric functions::

            sage: p = SymmetricFunctions(QQ).p()
            sage: T = LazySymmetricFunctions(tensor([p, p]))
            sage: X = tensor([p[1],p[[]]])
            sage: Y = tensor([p[[]],p[1]])
            sage: A = T.undefined(name="A")
            sage: B = T.undefined(name="B")
            sage: T.define_implicitly([A, B], [X*A - Y*B])
            sage: A
            <repr(...) failed: ValueError: could not determine any coefficients:
                coefficient [p[1] # p[1]]: -B[p[1] # p[]] + A[p[] # p[1]] == 0>

        An example we cannot solve because we only look at the next
        non-vanishing equations::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: A = L.undefined()
            sage: eq1 = diff(A, x) + diff(A, x, 2)
            sage: eq2 = A + diff(A, x) + diff(A, x, 2)
            sage: L.define_implicitly([A], [eq1, eq2])
            sage: A[1]
            Traceback (most recent call last):
            ...
            ValueError: could not determine any coefficients:
            equation 0:
                coefficient [0]: 2*series[2] + series[1] == 0
            equation 1:
                coefficient [0]: 2*series[2] + series[1] == 0

            sage: A = L.undefined()
            sage: eq1 = diff(A, x) + diff(A, x, 2)
            sage: eq2 = A + diff(A, x) + diff(A, x, 2)
            sage: L.define_implicitly([A], [eq1, eq2], max_lookahead=2)
            sage: A
            O(x^7)
        '''
    class options(GlobalOptions):
        """
        Set and display the options for lazy series.

        If no parameters are set, then the function returns a copy of
        the options dictionary.

        The ``options`` to lazy series can be accessed as using
        :class:`LazySeriesRing.options`.

        @OPTIONS@

        EXAMPLES::

            sage: LLS.<z> = LazyLaurentSeriesRing(QQ)
            sage: LLS.options
            Current options for lazy series rings
              - constant_length:   3
              - display_length:    7
              - halting_precision: None
              - secure:            False

            sage: LLS.options.display_length
            7
            sage: f = 1 / (1 + z)
            sage: f
            1 - z + z^2 - z^3 + z^4 - z^5 + z^6 + O(z^7)
            sage: LLS.options.display_length = 10
            sage: f
            1 - z + z^2 - z^3 + z^4 - z^5 + z^6 - z^7 + z^8 - z^9 + O(z^10)
            sage: g = LLS(lambda n: n^2, valuation=-2, degree=5, constant=42)
            sage: g
            4*z^-2 + z^-1 + z + 4*z^2 + 9*z^3 + 16*z^4 + 42*z^5 + 42*z^6 + 42*z^7 + O(z^8)
            sage: h = 1 / (1 - z)  # This is exact
            sage: h
            1 + z + z^2 + O(z^3)
            sage: LLS.options.constant_length = 1
            sage: g
            4*z^-2 + z^-1 + z + 4*z^2 + 9*z^3 + 16*z^4 + 42*z^5 + O(z^6)
            sage: h
            1 + O(z)
            sage: LazyLaurentSeriesRing.options._reset()
            sage: LazyLaurentSeriesRing.options.display_length
            7
        """
        NAME: str
        module: str
        display_length: Incomplete
        constant_length: Incomplete
        halting_precision: Incomplete
        secure: Incomplete
    @cached_method
    def one(self):
        """
        Return the constant series `1`.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: L.one()
            1

            sage: L = LazyPowerSeriesRing(ZZ, 'z')
            sage: L.one()
            1

            sage: m = SymmetricFunctions(ZZ).m()                                        # needs sage.modules
            sage: L = LazySymmetricFunctions(m)                                         # needs sage.modules
            sage: L.one()                                                               # needs sage.modules
            m[]
        """
    @cached_method
    def zero(self):
        """
        Return the zero series.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: L.zero()
            0

            sage: s = SymmetricFunctions(ZZ).s()                                        # needs sage.modules
            sage: L = LazySymmetricFunctions(s)                                         # needs sage.modules
            sage: L.zero()                                                              # needs sage.modules
            0

            sage: L = LazyDirichletSeriesRing(ZZ, 'z')
            sage: L.zero()
            0

            sage: L = LazyPowerSeriesRing(ZZ, 'z')
            sage: L.zero()
            0
        """
    def characteristic(self):
        '''
        Return the characteristic of this lazy power series ring, which
        is the same as the characteristic of its base ring.

        EXAMPLES::

            sage: L.<t> = LazyLaurentSeriesRing(ZZ)
            sage: L.characteristic()
            0

            sage: R.<w> = LazyLaurentSeriesRing(GF(11)); R
            Lazy Laurent Series Ring in w over Finite Field of size 11
            sage: R.characteristic()
            11

            sage: R.<x, y> = LazyPowerSeriesRing(GF(7)); R
            Multivariate Lazy Taylor Series Ring in x, y over Finite Field of size 7
            sage: R.characteristic()
            7

            sage: L = LazyDirichletSeriesRing(ZZ, "s")
            sage: L.characteristic()
            0
        '''
    def is_sparse(self):
        """
        Return whether ``self`` is sparse or not.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z', sparse=False)
            sage: L.is_sparse()
            False

            sage: L = LazyLaurentSeriesRing(ZZ, 'z', sparse=True)
            sage: L.is_sparse()
            True
        """
    def is_exact(self):
        """
        Return if ``self`` is exact or not.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: L.is_exact()
            True
            sage: L = LazyLaurentSeriesRing(RR, 'z')
            sage: L.is_exact()
            False
        """
    def prod(self, f, a=None, b=..., add_one: bool = False):
        '''
        The product of elements of ``self``.

        INPUT:

        - ``f`` -- list (or iterable) of elements of ``self``
        - ``a``, ``b`` -- optional arguments
        - ``add_one`` -- (default: ``False``) if ``True``, then converts a
          lazy series `p_i` from ``args`` into `1 + p_i` for the product

        If ``a`` and ``b`` are both integers, then this returns the product
        `\\prod_{i=a}^b f(i)`, where `f(i) = p_i` if ``add_one=False`` or
        `f(i) = 1 + p_i` otherwise. If ``b`` is not specified, then we consider
        `b = \\infty`. Note this corresponds to the Python ``range(a, b+1)``.

        If `a` is any other iterable, then this returns the product
        `\\prod_{i \\in a} f(i)`, where `f(i) = p_i` if ``add_one=False`` or
        `f(i) = 1 + p_i`.

        .. NOTE::

            For infinite products, it is faster to use ``add_one=True`` since
            the implementation is based on `p_i` in `\\prod_i (1 + p_i)`.

        .. WARNING::

            When ``f`` is an infinite generator, then the first argument
            ``a`` must be ``True``. Otherwise this will loop forever.

        .. WARNING::

            For an *infinite* product of the form `\\prod_i (1 + p_i)`,
            if `p_i = 0`, then this will loop forever.

        EXAMPLES::

            sage: L.<t> = LazyLaurentSeriesRing(QQ)
            sage: euler = L.prod(lambda n: 1 - t^n, PositiveIntegers())
            sage: euler
            1 - t - t^2 + t^5 + O(t^7)
            sage: 1 / euler
            1 + t + 2*t^2 + 3*t^3 + 5*t^4 + 7*t^5 + 11*t^6 + O(t^7)
            sage: euler - L.euler()
            O(t^7)
            sage: L.prod(lambda n: -t^n, 1, add_one=True)
            1 - t - t^2 + t^5 + O(t^7)

            sage: L.prod((1 - t^n for n in PositiveIntegers()), True)
            1 - t - t^2 + t^5 + O(t^7)
            sage: L.prod((-t^n for n in PositiveIntegers()), True, add_one=True)
            1 - t - t^2 + t^5 + O(t^7)

            sage: L.prod((1 + t^(n-3) for n in PositiveIntegers()), True)
            2*t^-3 + 4*t^-2 + 4*t^-1 + 4 + 6*t + 10*t^2 + 16*t^3 + O(t^4)

            sage: L.prod(lambda n: 2 + t^n, -3, 5)
            96*t^-6 + 240*t^-5 + 336*t^-4 + 840*t^-3 + 984*t^-2 + 1248*t^-1
             + 1980 + 1668*t + 1824*t^2 + 1872*t^3 + 1782*t^4 + 1710*t^5
             + 1314*t^6 + 1122*t^7 + 858*t^8 + 711*t^9 + 438*t^10 + 282*t^11
             + 210*t^12 + 84*t^13 + 60*t^14 + 24*t^15
            sage: L.prod(lambda n: t^n / (1 + abs(n)), -2, 2, add_one=True)
            1/3*t^-3 + 5/6*t^-2 + 13/9*t^-1 + 25/9 + 13/9*t + 5/6*t^2 + 1/3*t^3
            sage: L.prod(lambda n: t^-2 + t^n / n, -4, -2)
            1/24*t^-9 - 1/8*t^-8 - 1/6*t^-7 + 1/2*t^-6

            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: D.prod(lambda p: (1+D(1, valuation=p)).inverse(), Primes())
            1 - 1/(2^s) - 1/(3^s) + 1/(4^s) - 1/(5^s) + 1/(6^s) - 1/(7^s) + O(1/(8^s))

            sage: D.prod(lambda p: D(1, valuation=p), Primes(), add_one=True)
            1 + 1/(2^s) + 1/(3^s) + 1/(5^s) + 1/(6^s) + 1/(7^s) + O(1/(8^s))
        '''
    def sum(self, f, a=None, b=...):
        '''
        The sum of elements of ``self``.

        INPUT:

        - ``f`` -- list (or iterable or function) of elements of ``self``
        - ``a``, ``b`` -- optional arguments

        If ``a`` and ``b`` are both integers, then this returns the sum
        `\\sum_{i=a}^b f(i)`. If ``b`` is not specified, then we consider
        `b = \\infty`. Note this corresponds to the Python ``range(a, b+1)``.

        If `a` is any other iterable, then this returns the sum
        `\\sum{i \\in a} f(i)`.

        .. WARNING::

            When ``f`` is an infinite generator, then the first argument
            ``a`` must be ``True``. Otherwise this will loop forever.

        .. WARNING::

            For an *infinite* sum of the form `\\sum_i s_i`,
            if `s_i = 0`, then this will loop forever.

        EXAMPLES::

            sage: L.<t> = LazyLaurentSeriesRing(QQ)
            sage: L.sum(lambda n: t^n / (n+1), PositiveIntegers())
            1/2*t + 1/3*t^2 + 1/4*t^3 + 1/5*t^4 + 1/6*t^5 + 1/7*t^6 + 1/8*t^7 + O(t^8)

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: T = L.undefined(1)
            sage: D = L.undefined(0)
            sage: H = L.sum(lambda k: T(z^k)/k, 2)
            sage: T.define(z*exp(T)*D)
            sage: D.define(exp(H))
            sage: T
            z + z^2 + 2*z^3 + 4*z^4 + 9*z^5 + 20*z^6 + 48*z^7 + O(z^8)
            sage: D
            1 + 1/2*z^2 + 1/3*z^3 + 7/8*z^4 + 11/30*z^5 + 281/144*z^6 + O(z^7)

        We verify the Rogers-Ramanujan identities up to degree 100::

            sage: L.<q> = LazyPowerSeriesRing(QQ)
            sage: Gpi = L.prod(lambda k: -q^(1+5*k), 0, oo, add_one=True)
            sage: Gpi *= L.prod(lambda k: -q^(4+5*k), 0, oo, add_one=True)
            sage: Gp = 1 / Gpi
            sage: G = L.sum(lambda n: q^(n^2) / prod(1 - q^(k+1) for k in range(n)), 0, oo)
            sage: G - Gp
            O(q^7)
            sage: all(G[k] == Gp[k] for k in range(100))
            True

            sage: Hpi = L.prod(lambda k: -q^(2+5*k), 0, oo, add_one=True)
            sage: Hpi *= L.prod(lambda k: -q^(3+5*k), 0, oo, add_one=True)
            sage: Hp = 1 / Hpi
            sage: H = L.sum(lambda n: q^(n^2+n) / prod(1 - q^(k+1) for k in range(n)), 0, oo)
            sage: H - Hp
            O(q^7)
            sage: all(H[k] == Hp[k] for k in range(100))
            True

        ::

            sage: D = LazyDirichletSeriesRing(QQ, "s")
            sage: D.sum(lambda p: D(1, valuation=p), Primes())
            1/(2^s) + 1/(3^s) + 1/(5^s) + 1/(7^s) + O(1/(9^s))
        '''

class LazyLaurentSeriesRing(LazySeriesRing):
    """
    The ring of lazy Laurent series.

    The ring of Laurent series over a ring with the usual arithmetic
    where the coefficients are computed lazily.

    INPUT:

    - ``base_ring`` -- base ring
    - ``names`` -- name of the generator
    - ``sparse`` -- boolean (default: ``True``); whether the implementation of
      the series is sparse or not

    EXAMPLES::

        sage: L.<z> = LazyLaurentSeriesRing(QQ)
        sage: 1 / (1 - z)
        1 + z + z^2 + O(z^3)
        sage: 1 / (1 - z) == 1 / (1 - z)
        True
        sage: L in Fields
        True

    Lazy Laurent series ring over a finite field::

        sage: # needs sage.rings.finite_rings
        sage: L.<z> = LazyLaurentSeriesRing(GF(3)); L
        Lazy Laurent Series Ring in z over Finite Field of size 3
        sage: e = 1 / (1 + z)
        sage: e.coefficient(100)
        1
        sage: e.coefficient(100).parent()
        Finite Field of size 3

    Series can be defined by specifying a coefficient function
    and a valuation::

        sage: R.<x,y> = QQ[]
        sage: L.<z> = LazyLaurentSeriesRing(R)
        sage: def coeff(n):
        ....:     if n < 0:
        ....:         return -2 + n
        ....:     if n == 0:
        ....:         return 6
        ....:     return x + y^n
        sage: f = L(coeff, valuation=-5)
        sage: f
        -7*z^-5 - 6*z^-4 - 5*z^-3 - 4*z^-2 - 3*z^-1 + 6 + (x + y)*z + O(z^2)
        sage: 1 / (1 - f)
        1/7*z^5 - 6/49*z^6 + 1/343*z^7 + 8/2401*z^8 + 64/16807*z^9
         + 17319/117649*z^10 + (1/49*x + 1/49*y - 180781/823543)*z^11 + O(z^12)
        sage: L(coeff, valuation=-3, degree=3, constant=x)
        -5*z^-3 - 4*z^-2 - 3*z^-1 + 6 + (x + y)*z + (y^2 + x)*z^2
         + x*z^3 + x*z^4 + x*z^5 + O(z^6)

    We can also specify a polynomial or the initial coefficients.
    Additionally, we may specify that all coefficients are equal to a
    given constant, beginning at a given degree::

        sage: L([1, x, y, 0, x+y])
        1 + x*z + y*z^2 + (x + y)*z^4
        sage: L([1, x, y, 0, x+y], constant=2)
        1 + x*z + y*z^2 + (x + y)*z^4 + 2*z^5 + 2*z^6 + 2*z^7 + O(z^8)
        sage: L([1, x, y, 0, x+y], degree=7, constant=2)
        1 + x*z + y*z^2 + (x + y)*z^4 + 2*z^7 + 2*z^8 + 2*z^9 + O(z^10)
        sage: L([1, x, y, 0, x+y], valuation=-2)
        z^-2 + x*z^-1 + y + (x + y)*z^2
        sage: L([1, x, y, 0, x+y], valuation=-2, constant=3)
        z^-2 + x*z^-1 + y + (x + y)*z^2 + 3*z^3 + 3*z^4 + 3*z^5 + O(z^6)
        sage: L([1, x, y, 0, x+y], valuation=-2, degree=4, constant=3)
        z^-2 + x*z^-1 + y + (x + y)*z^2 + 3*z^4 + 3*z^5 + 3*z^6 + O(z^7)

    Some additional examples over the integer ring::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ)
        sage: L in Fields
        False
        sage: 1 / (1 - 2*z)^3
        1 + 6*z + 24*z^2 + 80*z^3 + 240*z^4 + 672*z^5 + 1792*z^6 + O(z^7)

        sage: R.<x> = LaurentPolynomialRing(ZZ)
        sage: L(x^-2 + 3 + x)
        z^-2 + 3 + z
        sage: L(x^-2 + 3 + x, valuation=-5, constant=2)
        z^-5 + 3*z^-3 + z^-2 + 2*z^-1 + 2 + 2*z + O(z^2)
        sage: L(x^-2 + 3 + x, valuation=-5, degree=0, constant=2)
        z^-5 + 3*z^-3 + z^-2 + 2 + 2*z + 2*z^2 + O(z^3)

    We can truncate a series, shift its coefficients, or replace all
    coefficients beginning with a given degree by a constant::

        sage: f = 1 / (z + z^2)
        sage: f
        z^-1 - 1 + z - z^2 + z^3 - z^4 + z^5 + O(z^6)
        sage: L(f, valuation=2)
        z^2 - z^3 + z^4 - z^5 + z^6 - z^7 + z^8 + O(z^9)
        sage: L(f, degree=3)
        z^-1 - 1 + z - z^2
        sage: L(f, degree=3, constant=2)
        z^-1 - 1 + z - z^2 + 2*z^3 + 2*z^4 + 2*z^5 + O(z^6)
        sage: L(f, valuation=1, degree=4)
        z - z^2 + z^3
        sage: L(f, valuation=1, degree=4, constant=5)
        z - z^2 + z^3 + 5*z^4 + 5*z^5 + 5*z^6 + O(z^7)

    Power series can be defined recursively (see
    :meth:`sage.rings.lazy_series.LazyModuleElement.define` for
    more examples)::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ)
        sage: s = L.undefined(valuation=0)
        sage: s.define(1 + z*s^2)
        sage: s
        1 + z + 2*z^2 + 5*z^3 + 14*z^4 + 42*z^5 + 132*z^6 + O(z^7)

    By default, any two series ``f`` and ``g`` that are not known to
    be equal are considered to be different::

        sage: f = L(lambda n: 0, valuation=0)
        sage: f == 0
        False

        sage: f = L(constant=1, valuation=0).derivative(); f
        1 + 2*z + 3*z^2 + 4*z^3 + 5*z^4 + 6*z^5 + 7*z^6 + O(z^7)
        sage: g = L(lambda n: (n+1), valuation=0); g
        1 + 2*z + 3*z^2 + 4*z^3 + 5*z^4 + 6*z^5 + 7*z^6 + O(z^7)
        sage: f == g
        False

    .. WARNING::

        We have imposed that ``(f == g) == not (f != g)``, and so
        ``f != g`` returning ``True`` might not mean that the two
        series are actually different::

            sage: f = L(lambda n: 0, valuation=0)
            sage: g = L.zero()
            sage: f != g
            True

        This can be verified by :meth:`~sage.rings.lazy_series.is_nonzero()`,
        which only returns ``True`` if the series is known to be nonzero::

            sage: (f - g).is_nonzero()
            False

    The implementation of the ring can be either be a sparse or a dense one.
    The default is a sparse implementation::

        sage: L.<z> = LazyLaurentSeriesRing(ZZ)
        sage: L.is_sparse()
        True
        sage: L.<z> = LazyLaurentSeriesRing(ZZ, sparse=False)
        sage: L.is_sparse()
        False

    We additionally provide two other methods of performing comparisons.
    The first is raising a :exc:`ValueError` and the second uses a check
    up to a (user set) finite precision. These behaviors are set using the
    options ``secure`` and ``halting_precision``. In particular,
    this applies to series that are not specified by a finite number
    of initial coefficients and a constant for the remaining coefficients.
    Equality checking will depend on the coefficients which have
    already been computed. If this information is not enough to
    check that two series are different, then if ``L.options.secure``
    is set to ``True``, then we raise a :exc:`ValueError`::

        sage: L.options.secure = True
        sage: f = 1 / (z + z^2); f
        z^-1 - 1 + z - z^2 + z^3 - z^4 + z^5 + O(z^6)
        sage: f2 = f * 2  # currently no coefficients computed
        sage: f3 = f * 3  # currently no coefficients computed
        sage: f2 == f3
        Traceback (most recent call last):
        ...
        ValueError: undecidable
        sage: f2  # computes some of the coefficients of f2
        2*z^-1 - 2 + 2*z - 2*z^2 + 2*z^3 - 2*z^4 + 2*z^5 + O(z^6)
        sage: f3  # computes some of the coefficients of f3
        3*z^-1 - 3 + 3*z - 3*z^2 + 3*z^3 - 3*z^4 + 3*z^5 + O(z^6)
        sage: f2 == f3
        False
        sage: f2a = f + f
        sage: f2 == f2a
        Traceback (most recent call last):
        ...
        ValueError: undecidable
        sage: zf = L(lambda n: 0, valuation=0)
        sage: zf == 0
        Traceback (most recent call last):
        ...
        ValueError: undecidable

    For boolean checks, an error is raised when it is not known to be nonzero::

        sage: bool(zf)
        Traceback (most recent call last):
        ...
        ValueError: undecidable

    If the halting precision is set to a finite number `p` (for unlimited
    precision, it is set to ``None``), then it will check up to `p` values
    from the current position::

        sage: L.options.halting_precision = 20
        sage: f2 = f * 2  # currently no coefficients computed
        sage: f3 = f * 3  # currently no coefficients computed
        sage: f2 == f3
        False
        sage: f2a = f + f
        sage: f2 == f2a
        True
        sage: zf = L(lambda n: 0, valuation=0)
        sage: zf == 0
        True

    TESTS:

    We reset the options::

        sage: L.options._reset()
    """
    Element = LazyLaurentSeries
    __classcall_private__: Incomplete
    def __init__(self, base_ring, names, sparse: bool = True, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: LazyLaurentSeriesRing.options.halting_precision(12)

            sage: L = LazyLaurentSeriesRing(ZZ, 't')
            sage: TestSuite(L).run()
            sage: L.category()
            Category of infinite commutative no zero divisors algebras over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)

            sage: L = LazyLaurentSeriesRing(QQ, 't')
            sage: TestSuite(L).run()
            sage: L.category()
            Join of Category of complete discrete valuation fields
             and Category of commutative algebras over (number fields and quotient fields and metric spaces)
             and Category of infinite sets

            sage: L = LazyLaurentSeriesRing(ZZ['x, y'], 't')
            sage: TestSuite(L).run()                                                    # needs sage.libs.singular
            sage: L.category()
            Category of infinite commutative no zero divisors algebras over
             (unique factorization domains and algebras with basis over
              (Dedekind domains and euclidean domains
               and noetherian rings
               and infinite enumerated sets and metric spaces)
              and commutative algebras over
               (Dedekind domains and euclidean domains
                and noetherian rings
                and infinite enumerated sets and metric spaces)
              and infinite sets)

            sage: L = LazyLaurentSeriesRing(GF(5), 't')
            sage: TestSuite(L).run()

            sage: L = LazyLaurentSeriesRing(GF(5)['x'], 't')
            sage: TestSuite(L).run()

            sage: L = LazyLaurentSeriesRing(GF(5)['x, y'], 't')
            sage: TestSuite(L).run()

            sage: L = LazyLaurentSeriesRing(Zmod(6), 't')
            sage: TestSuite(L).run(skip=['_test_revert'])
            sage: L.category()
            Category of infinite commutative algebras over
             (finite commutative rings and subquotients of monoids
              and quotients of semigroups and finite enumerated sets)

            sage: E.<x,y> = ExteriorAlgebra(QQ)                                         # needs sage.modules
            sage: L = LazyLaurentSeriesRing(E, 't')     # not tested                    # needs sage.modules

            sage: LazyLaurentSeriesRing.options._reset()  # reset the options
        """
    @cached_method
    def gen(self, n: int = 0):
        """
        Return the ``n``-th generator of ``self``.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: L.gen()
            z
            sage: L.gen(3)
            Traceback (most recent call last):
            ...
            IndexError: there is only one generator
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        This is always 1.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: L.ngens()
            1
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(ZZ)
            sage: L.gens()
            (z,)
            sage: 1/(1 - z)
            1 + z + z^2 + O(z^3)
        """
    def some_elements(self):
        """
        Return a list of elements of ``self``.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: L.some_elements()[:7]
            [0, 1, z,
             -3*z^-4 + z^-3 - 12*z^-2 - 2*z^-1 - 10 - 8*z + z^2 + z^3,
             z^-2 + z^3 + z^4 + z^5 + O(z^6),
             -2*z^-3 - 2*z^-2 + 4*z^-1 + 11 - z - 34*z^2 - 31*z^3 + O(z^4),
             4*z^-2 + z^-1 + z + 4*z^2 + 9*z^3 + 16*z^4 + O(z^5)]

            sage: L = LazyLaurentSeriesRing(GF(2), 'z')
            sage: L.some_elements()[:7]
            [0, 1, z,
             z^-4 + z^-3 + z^2 + z^3,
             z^-2,
             1 + z + z^3 + z^4 + z^6 + O(z^7),
             z^-1 + z + z^3 + O(z^5)]

            sage: L = LazyLaurentSeriesRing(GF(3), 'z')
            sage: L.some_elements()[:7]
            [0, 1, z,
             z^-3 + z^-1 + 2 + z + z^2 + z^3,
             z^-2,
             z^-3 + z^-2 + z^-1 + 2 + 2*z + 2*z^2 + O(z^3),
             z^-2 + z^-1 + z + z^2 + z^4 + O(z^5)]
        """
    def series(self, coefficient, valuation, degree=None, constant=None):
        """
        Return a lazy Laurent series.

        INPUT:

        - ``coefficient`` -- Python function that computes coefficients or a list
        - ``valuation`` -- integer; approximate valuation of the series
        - ``degree`` -- (optional) integer
        - ``constant`` -- (optional) an element of the base ring

        Let the coefficient of index `i` mean the coefficient of the term
        of the series with exponent `i`.

        Python function ``coefficient`` returns the value of the coefficient
        of index `i` from input `s` and `i` where `s` is the series itself.

        Let ``valuation`` be `n`. All coefficients of index below `n` are zero.
        If ``constant`` is not specified, then the ``coefficient`` function is
        responsible to compute the values of all coefficients of index `\\ge n`.
        If ``degree`` or ``constant`` is a pair `(c,m)`, then the ``coefficient``
        function is responsible to compute the values of all coefficients of
        index `\\ge n` and `< m` and all the coefficients of index `\\ge m`
        is the constant `c`.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: L.series(lambda s, i: i, 5, (1,10))
            5*z^5 + 6*z^6 + 7*z^7 + 8*z^8 + 9*z^9 + z^10 + z^11 + z^12 + O(z^13)

            sage: def g(s, i):
            ....:     if i < 0:
            ....:         return 1
            ....:     else:
            ....:         return s.coefficient(i - 1) + i
            sage: e = L.series(g, -5); e
            z^-5 + z^-4 + z^-3 + z^-2 + z^-1 + 1 + 2*z + O(z^2)
            sage: f = e^-1; f
            z^5 - z^6 - z^11 + O(z^12)
            sage: f.coefficient(10)
            0
            sage: f.coefficient(20)
            9
            sage: f.coefficient(30)
            -219

        Alternatively, the ``coefficient`` can be a list of elements of the
        base ring. Then these elements are read as coefficients of the terms of
        degrees starting from the ``valuation``. In this case, ``constant``
        may be just an element of the base ring instead of a tuple or can be
        simply omitted if it is zero. ::

            sage: L = LazyLaurentSeriesRing(ZZ, 'z')
            sage: f = L.series([1,2,3,4], -5); f
            z^-5 + 2*z^-4 + 3*z^-3 + 4*z^-2
            sage: g = L.series([1,3,5,7,9], 5, constant=-1); g
            z^5 + 3*z^6 + 5*z^7 + 7*z^8 + 9*z^9 - z^10 - z^11 - z^12 + O(z^13)
        """
    def uniformizer(self):
        """
        Return a uniformizer of ``self``..

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(QQ, 'z')
            sage: L.uniformizer()
            z
        """
    def residue_field(self):
        """
        Return the residue field of the ring of integers of ``self``.

        EXAMPLES::

            sage: L = LazyLaurentSeriesRing(QQ, 'z')
            sage: L.residue_field()
            Rational Field
        """
    def taylor(self, f):
        """
        Return the Taylor expansion around `0` of the function ``f``.

        INPUT:

        - ``f`` -- a function such that one of the following works:

          * the substitution `f(z)`, where `z` is a generator of ``self``
          * `f` is a function of a single variable with no poles at `0`
            and has a ``derivative`` method

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: x = SR.var('x')
            sage: f(x) = (1 + x) / (1 - x^2)
            sage: L.taylor(f)
            1 + z + z^2 + z^3 + z^4 + z^5 + z^6 + O(z^7)

        For inputs as symbolic functions/expressions, the function must
        not have any poles at `0`::

            sage: f(x) = (1 + x^2) / sin(x^2)
            sage: L.taylor(f)
            <repr(...) failed: ValueError: power::eval(): division by zero>
            sage: def g(a): return (1 + a^2) / sin(a^2)
            sage: L.taylor(g)
            z^-2 + 1 + 1/6*z^2 + 1/6*z^4 + O(z^5)
        """
    def q_pochhammer(self, q=None):
        '''
        Return the infinite ``q``-Pochhammer symbol `(a; q)_{\\infty}`,
        where `a` is the variable of ``self``.

        This is also one version of the quantum dilogarithm or
        the `q`-Exponential function.

        INPUT:

        - ``q`` -- (default: `q \\in \\QQ(q)`) the parameter `q`

        EXAMPLES::

            sage: q = ZZ[\'q\'].fraction_field().gen()
            sage: L.<z> = LazyLaurentSeriesRing(q.parent())
            sage: qpoch = L.q_pochhammer(q)
            sage: qpoch
            1
             + (-1/(-q + 1))*z
             + (q/(q^3 - q^2 - q + 1))*z^2
             + (-q^3/(-q^6 + q^5 + q^4 - q^2 - q + 1))*z^3
             + (q^6/(q^10 - q^9 - q^8 + 2*q^5 - q^2 - q + 1))*z^4
             + (-q^10/(-q^15 + q^14 + q^13 - q^10 - q^9 - q^8 + q^7 + q^6 + q^5 - q^2 - q + 1))*z^5
             + (q^15/(q^21 - q^20 - q^19 + q^16 + 2*q^14 - q^12 - q^11 - q^10 - q^9 + 2*q^7 + q^5 - q^2 - q + 1))*z^6
             + O(z^7)

        We show that `(z; q)_n = \\frac{(z; q)_{\\infty}}{(q^n z; q)_{\\infty}}`::

            sage: qpoch / qpoch(q*z)
            1 - z + O(z^7)
            sage: qpoch / qpoch(q^2*z)
            1 + (-q - 1)*z + q*z^2 + O(z^7)
            sage: qpoch / qpoch(q^3*z)
            1 + (-q^2 - q - 1)*z + (q^3 + q^2 + q)*z^2 - q^3*z^3 + O(z^7)
            sage: qpoch / qpoch(q^4*z)
            1 + (-q^3 - q^2 - q - 1)*z + (q^5 + q^4 + 2*q^3 + q^2 + q)*z^2
             + (-q^6 - q^5 - q^4 - q^3)*z^3 + q^6*z^4 + O(z^7)

        We can also construct part of Euler\'s function::

            sage: M.<a> = LazyLaurentSeriesRing(QQ)
            sage: phi = sum(qpoch[i](q=a)*a^i for i in range(10))
            sage: phi[:20] == M.euler()[:20]
            True

        TESTS::

            sage: R = ZZ[\'q\'].fraction_field()
            sage: q = R.gen()
            sage: L.<z> = LazyLaurentSeriesRing(LazyDirichletSeriesRing(R, "s"))
            sage: z.q_pochhammer(q)                                                     # needs sage.symbolic
            1 + ((1/(q-1)))*z + ((q/(q^3-q^2-q+1)))*z^2 + ... + O(z^7)

        REFERENCES:

        - :wikipedia:`Q-Pochhammer_symbol`
        - :wikipedia:`Quantum_dilogarithm`
        - :wikipedia:`Q-exponential`
        '''
    def euler(self):
        '''
        Return the Euler function as an element of ``self``.

        The *Euler function* is defined as

        .. MATH::

            \\phi(z) = (z; z)_{\\infty}
            = \\sum_{n=0}^{\\infty} (-1)^n q^{(3n^2-n)/2}.

        EXAMPLES::

            sage: L.<q> = LazyLaurentSeriesRing(ZZ)
            sage: phi = q.euler()
            sage: phi
            1 - q - q^2 + q^5 + O(q^7)

        We verify that `1 / phi` gives the generating function
        for all partitions::

            sage: P = 1 / phi; P
            1 + q + 2*q^2 + 3*q^3 + 5*q^4 + 7*q^5 + 11*q^6 + O(q^7)
            sage: P[:20] == [Partitions(n).cardinality() for n in range(20)]            # needs sage.libs.flint
            True

        TESTS::

            sage: L.<q> = LazyLaurentSeriesRing(LazyDirichletSeriesRing(QQ, "s"))
            sage: q.euler()                                                             # needs sage.symbolic
            1 - q - q^2 + q^5 + O(q^7)

        REFERENCES:

        - :wikipedia:`Euler_function`
        '''
    def jacobi_theta(self, w, a: int = 0, b: int = 0):
        """
        Return the Jacobi function `\\vartheta_{ab}(w; q)` as an
        element of ``self``.

        The *Jacobi theta functions* with nome `q = \\exp(\\pi i \\tau)`
        for `z \\in \\CC` and `\\tau \\in \\RR + \\RR_{>0} i`, are defined as

        .. MATH::

            \\begin{aligned}
            \\vartheta_{00}(z; \\tau) & = \\sum_{n=0}^{\\infty}
            (w^{2n} + w^{-2n}) q^{n^2},
            \\|
            \\vartheta_{01}(z; \\tau) & = \\sum_{n=0}^{\\infty}
            (-1)^n (w^{2n} + w^{-2n}) q^{n^2},
            \\\\\n            \\vartheta_{10}(z; \\tau) & = \\sum_{n=0}^{\\infty}
            (w^{2n+1} + w^{-2n+1}) q^{n^2+n},
            \\\\\n            \\vartheta_{11}(z; \\tau) & = \\sum_{n=0}^{\\infty}
            (-1)^n (w^{2n+1} + w^{-2n+1}) q^{n^2+n},
            \\end{aligned}

        where `w = \\exp(\\pi i z)`. We consider them as formal power
        series in `q` with the coefficients in the Laurent polynomial
        ring `R[w, w^{-1}]` (for a commutative ring `R`). Here, we
        deviate from the standard definition of `\\theta_{10}` and
        `\\theta_{11}` by removing the overall factor of `q^{1/4}`
        and `i q^{1/4}`, respectively.

        EXAMPLES::

            sage: R.<w> = LaurentPolynomialRing(QQ)
            sage: L.<q> = LazyPowerSeriesRing(R)
            sage: L.options.display_length = 17  # to display more coefficients
            sage: theta = q.jacobi_theta(w)
            sage: theta
            1 + ((w^-2+w^2)*q) + ((w^-4+w^4)*q^4) + ((w^-6+w^6)*q^9)
             + ((w^-8+w^8)*q^16) + O(q^17)

            sage: th3 = q.jacobi_theta(1, 0, 0); th3
            1 + 2*q + 2*q^4 + 2*q^9 + 2*q^16 + O(q^17)
            sage: th2 = q.jacobi_theta(1, 1, 0); th2
            2 + 2*q^2 + 2*q^6 + 2*q^12 + O(q^17)
            sage: th4 = q.jacobi_theta(1, 0, 1); th4
            1 + (-2*q) + 2*q^4 + (-2*q^9) + 2*q^16 + O(q^17)
            sage: th1 = -q.jacobi_theta(1, 1, 1); th1
            -2 + 2*q^2 + (-2*q^6) + 2*q^12 + O(q^17)

        We verify the Jacobi triple product formula::

            sage: JTP = L.prod(lambda n: ((1 - q^(2*n)) * (1 + w^2*q^(2*n-1))
            ....:                         * (1 + w^-2*q^(2*n-1))), 1, oo)
            sage: JTP
            1 + ((w^-2+w^2)*q) + ((w^-4+w^4)*q^4) + ((w^-6+w^6)*q^9)
             + ((w^-8+w^8)*q^16) + O(q^17)
            sage: JTP[:30] == theta[:30]
            True

        We verify the Jacobi identity::

            sage: LHS = q.jacobi_theta(1, 0, 1)^4 + q*q.jacobi_theta(1, 1, 0)^4
            sage: LHS
            1 + 8*q + 24*q^2 + 32*q^3 + 24*q^4 + 48*q^5 + 96*q^6 + 64*q^7
             + 24*q^8 + 104*q^9 + 144*q^10 + 96*q^11 + 96*q^12 + 112*q^13
             + 192*q^14 + 192*q^15 + 24*q^16 + O(q^17)
            sage: RHS = q.jacobi_theta(1, 0, 0)^4
            sage: RHS
            1 + 8*q + 24*q^2 + 32*q^3 + 24*q^4 + 48*q^5 + 96*q^6 + 64*q^7
             + 24*q^8 + 104*q^9 + 144*q^10 + 96*q^11 + 96*q^12 + 112*q^13
             + 192*q^14 + 192*q^15 + 24*q^16 + O(q^17)
            sage: LHS[:20] == RHS[:20]
            True

        We verify some relationships to the (rescaled) Dedekind eta function::

            sage: eta = q.euler()
            sage: RHS = 2 * eta(q^4)^2 / eta(q^2); RHS
            2 + 2*q^2 + 2*q^6 + 2*q^12 + O(q^17)
            sage: th2[:30] == RHS[:30]
            True

            sage: RHS = eta(q^2)^5 / (eta^2 * eta(q^4)^2); RHS
            1 + 2*q + 2*q^4 + 2*q^9 + 2*q^16 + O(q^17)
            sage: th3[:30] == RHS[:30]
            True

            sage: RHS = eta^2 / eta(q^2); RHS
            1 + (-2*q) + 2*q^4 + (-2*q^9) + 2*q^16 + O(q^17)
            sage: th4[:30] == RHS[:30]
            True

            sage: LHS = th2 * th3 * th4; LHS
            2 + (-6*q^2) + 10*q^6 + (-14*q^12) + O(q^17)
            sage: RHS = 2 * eta(q^2)^3; RHS
            2 + (-6*q^2) + 10*q^6 + (-14*q^12) + O(q^17)
            sage: LHS[:30] == RHS[:30]
            True

        We verify some derivative formulas (recall our conventions)::

            sage: LHS = th4 * th3.derivative() - th3 * th4.derivative(); LHS
            4 + (-24*q^4) + 36*q^8 + 40*q^12 + (-120*q^16) + O(q^17)
            sage: RHS = th3 * th4 * (th3^4 - th4^4) / (4*q); RHS
            4 + (-24*q^4) + 36*q^8 + 40*q^12 + O(q^16)
            sage: LHS[:30] == RHS[:30]
            True

            sage: LHS = (th2 / th3) / (4*q) + (th2 / th3).derivative(); LHS
            1/2/q - 5 + 45/2*q + (-65*q^2) + 153*q^3 + (-336*q^4) + 1375/2*q^5
             + (-1305*q^6) + 2376*q^7 + (-4181*q^8) + 7093*q^9 + (-11745*q^10)
             + 38073/2*q^11 + (-30157*q^12) + 46968*q^13 + (-72041*q^14)
             + 108810*q^15 + O(q^16)
            sage: RHS = th2 * th4^4 / (4 * q * th3); RHS
            1/2/q - 5 + 45/2*q + (-65*q^2) + 153*q^3 + (-336*q^4) + 1375/2*q^5
             + (-1305*q^6) + 2376*q^7 + (-4181*q^8) + 7093*q^9 + (-11745*q^10)
             + 38073/2*q^11 + (-30157*q^12) + 46968*q^13 + (-72041*q^14)
             + 108810*q^15 + O(q^16)
            sage: LHS[:30] == RHS[:30]
            True

            sage: LHS = (th2 / th4) / (4*q) + (th2 / th4).derivative(); LHS
            1/2/q + 5 + 45/2*q + 65*q^2 + 153*q^3 + 336*q^4 + 1375/2*q^5
             + 1305*q^6 + 2376*q^7 + 4181*q^8 + 7093*q^9 + 11745*q^10
             + 38073/2*q^11 + 30157*q^12 + 46968*q^13 + 72041*q^14
             + 108810*q^15 + O(q^16)
            sage: RHS = th2 * th3^4 / (4 * q * th4); RHS
            1/2/q + 5 + 45/2*q + 65*q^2 + 153*q^3 + 336*q^4 + 1375/2*q^5
             + 1305*q^6 + 2376*q^7 + 4181*q^8 + 7093*q^9 + 11745*q^10
             + 38073/2*q^11 + 30157*q^12 + 46968*q^13 + 72041*q^14
             + 108810*q^15 + O(q^16)
            sage: LHS[:30] == RHS[:30]
            True

            sage: LHS = (th3 / th4).derivative(); LHS
            4 + 16*q + 48*q^2 + 128*q^3 + 280*q^4 + 576*q^5 + 1120*q^6 + 2048*q^7
             + 3636*q^8 + 6240*q^9 + 10384*q^10 + 16896*q^11 + 26936*q^12
             + 42112*q^13 + 64800*q^14 + 98304*q^15 + 147016*q^16 + O(q^17)
            sage: RHS = (th3^5 - th3 * th4^4) / (4 * q * th4); RHS
            4 + 16*q + 48*q^2 + 128*q^3 + 280*q^4 + 576*q^5 + 1120*q^6 + 2048*q^7
             + 3636*q^8 + 6240*q^9 + 10384*q^10 + 16896*q^11 + 26936*q^12
             + 42112*q^13 + 64800*q^14 + 98304*q^15 + O(q^16)
            sage: LHS[:30] == RHS[:30]
            True

        We have the partition generating function::

            sage: P = th3^(-1/6) * th4^(-2/3) * ((th3^4 - th4^4)/(16*q))^(-1/24); P
            1 + q + 2*q^2 + 3*q^3 + 5*q^4 + 7*q^5 + 11*q^6 + 15*q^7 + 22*q^8
             + 30*q^9 + 42*q^10 + 56*q^11 + 77*q^12 + 101*q^13 + 135*q^14
             + 176*q^15 + 231*q^16 + O(q^17)
            sage: 1 / q.euler()
            1 + q + 2*q^2 + 3*q^3 + 5*q^4 + 7*q^5 + 11*q^6 + 15*q^7 + 22*q^8
             + 30*q^9 + 42*q^10 + 56*q^11 + 77*q^12 + 101*q^13 + 135*q^14
             + 176*q^15 + 231*q^16 + O(q^17)
            sage: oeis(P[:30])  # optional - internet
            0: A000041: a(n) is the number of partitions of n (the partition numbers).
            ...

        We have the strict partition generating function::

            sage: SP = th3^(1/6) * th4^(-1/3) * ((th3^4 - th4^4)/(16*q))^(1/24); SP
            1 + q + q^2 + 2*q^3 + 2*q^4 + 3*q^5 + 4*q^6 + 5*q^7 + 6*q^8 + 8*q^9
             + 10*q^10 + 12*q^11 + 15*q^12 + 18*q^13 + 22*q^14 + 27*q^15
             + 32*q^16 + O(q^17)
            sage: oeis(SP[:30])  # optional - internet
            0: A000009: Expansion of Product_{m >= 1} (1 + x^m);
             number of partitions of n into distinct parts;
             number of partitions of n into odd parts.
            1: A081360: Expansion of q^(-1/24) (m (1-m) / 16)^(1/24) in
             powers of q, where m = k^2 is the parameter and q is the nome
             for Jacobian elliptic functions.

        We have the overpartition generating function::

            sage: ~th4
            1 + 2*q + 4*q^2 + 8*q^3 + 14*q^4 + 24*q^5 + 40*q^6 + 64*q^7 + 100*q^8
             + 154*q^9 + 232*q^10 + 344*q^11 + 504*q^12 + 728*q^13 + 1040*q^14
             + 1472*q^15 + 2062*q^16 + O(q^17)
            sage: oeis((~th4)[:20])  # optional - internet
            0: A015128: Number of overpartitions of n: ... overlined.
            1: A004402: Expansion of 1 / Sum_{n=-oo..oo} x^(n^2).

        We give an example over the :class:`SymbolicRing` with the input
        `w = e^{\\pi i z}` and verify the periodicity::

            sage: L.<q> = LazyLaurentSeriesRing(SR)
            sage: z = SR.var('z')
            sage: theta = L.jacobi_theta(exp(pi*I*z))
            sage: theta
            1 + (e^(2*I*pi*z) + e^(-2*I*pi*z))*q
             + (e^(4*I*pi*z) + e^(-4*I*pi*z))*q^4
             + (e^(6*I*pi*z) + e^(-6*I*pi*z))*q^9
             + (e^(8*I*pi*z) + e^(-8*I*pi*z))*q^16 + O(q^17)

            sage: theta.map_coefficients(lambda c: c(z=z+1))
            1 + (e^(2*I*pi*z) + e^(-2*I*pi*z))*q
             + (e^(4*I*pi*z) + e^(-4*I*pi*z))*q^4
             + (e^(6*I*pi*z) + e^(-6*I*pi*z))*q^9
             + (e^(8*I*pi*z) + e^(-8*I*pi*z))*q^16 + O(q^17)

            sage: L.options._reset()  # reset options

        REFERENCES:

        - :wikipedia:`Theta_function`
        """
    def polylog(self, s):
        """
        Return the polylogarithm at ``s`` as an element in ``self``.

        The *polylogarithm* at `s` is the power series in `z`

        .. MATH::

            \\mathrm{Li}_s(z) = \\sum_{k=1}^{\\infty} \\frac{z^k}{k^s}.

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: L.polylog(1)
            z + 1/2*z^2 + 1/3*z^3 + 1/4*z^4 + 1/5*z^5 + 1/6*z^6 + 1/7*z^7 + O(z^8)
            sage: -log(1 - z)
            z + 1/2*z^2 + 1/3*z^3 + 1/4*z^4 + 1/5*z^5 + 1/6*z^6 + 1/7*z^7 + O(z^8)
            sage: L.polylog(2)
            z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + 1/25*z^5 + 1/36*z^6 + 1/49*z^7 + O(z^8)
            sage: (-log(1-z) / z).integral()
            z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + 1/25*z^5 + 1/36*z^6 + O(z^7)
            sage: L.polylog(0)
            z + z^2 + z^3 + O(z^4)
            sage: L.polylog(-1)
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + 7*z^7 + O(z^8)
            sage: z / (1-z)^2
            z + 2*z^2 + 3*z^3 + 4*z^4 + 5*z^5 + 6*z^6 + 7*z^7 + O(z^8)
            sage: L.polylog(-2)
            z + 4*z^2 + 9*z^3 + 16*z^4 + 25*z^5 + 36*z^6 + 49*z^7 + O(z^8)
            sage: z * (1 + z) / (1 - z)^3
            z + 4*z^2 + 9*z^3 + 16*z^4 + 25*z^5 + 36*z^6 + 49*z^7 + O(z^8)

        We can compute the Eulerian numbers::

            sage: [L.polylog(-n) * (1-z)^(n+1) for n in range(1, 6)]
            [z + O(z^8),
             z + z^2 + O(z^8),
             z + 4*z^2 + z^3 + O(z^8),
             z + 11*z^2 + 11*z^3 + z^4 + O(z^8),
             z + 26*z^2 + 66*z^3 + 26*z^4 + z^5 + O(z^8)]

        REFERENCES:

        - :wikipedia:`Polylogarithm`
        """
    def dilog(self):
        """
        Return the dilogarithm as an element in ``self``.

        .. SEEALSO::

            :meth:`polylog`

        EXAMPLES::

            sage: L.<z> = LazyLaurentSeriesRing(QQ)
            sage: L.dilog()
            z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + 1/25*z^5 + 1/36*z^6 + 1/49*z^7 + O(z^8)
            sage: L.polylog(2)
            z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + 1/25*z^5 + 1/36*z^6 + 1/49*z^7 + O(z^8)

            sage: L.<x> = LazyLaurentSeriesRing(SR)
            sage: L.dilog()
            x + 1/4*x^2 + 1/9*x^3 + 1/16*x^4 + 1/25*x^5 + 1/36*x^6 + 1/49*x^7 + O(x^8)

        REFERENCES:

        - :wikipedia:`Dilogarithm`
        """

class LazyPowerSeriesRing(LazySeriesRing):
    """
    The ring of (possibly multivariate) lazy Taylor series.

    INPUT:

    - ``base_ring`` -- base ring of this Taylor series ring
    - ``names`` -- name(s) of the generator of this Taylor series ring
    - ``sparse`` -- boolean (default: ``True``); whether this series is sparse or not

    EXAMPLES::

        sage: LazyPowerSeriesRing(ZZ, 't')
        Lazy Taylor Series Ring in t over Integer Ring

        sage: L.<x, y> = LazyPowerSeriesRing(QQ); L
        Multivariate Lazy Taylor Series Ring in x, y over Rational Field
    """
    Element = LazyPowerSeries
    __classcall_private__: Incomplete
    def __init__(self, base_ring, names, sparse: bool = True, category=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: LazyPowerSeriesRing.options.halting_precision(12)

            sage: L = LazyPowerSeriesRing(ZZ, 't')
            sage: TestSuite(L).run(skip='_test_fraction_field')
            sage: L = LazyPowerSeriesRing(ZZ, 's, t')
            sage: TestSuite(L).run(skip='_test_fraction_field')

            sage: L = LazyPowerSeriesRing(QQ, 't')
            sage: TestSuite(L).run(skip='_test_fraction_field')
            sage: L = LazyPowerSeriesRing(QQ, 's, t')
            sage: TestSuite(L).run(skip='_test_fraction_field')

            sage: L = LazyPowerSeriesRing(GF(5), 't')
            sage: TestSuite(L).run()

            sage: L = LazyPowerSeriesRing(GF(5), 's, t')
            sage: TestSuite(L).run(skip=['_test_fraction_field'])

            sage: L = LazyPowerSeriesRing(Zmod(6), 't')
            sage: TestSuite(L).run(skip=['_test_revert'])
            sage: L = LazyPowerSeriesRing(Zmod(6), 's, t')
            sage: TestSuite(L).run(skip=['_test_revert'])

            sage: L = LazyPowerSeriesRing(QQ['q'], 't')
            sage: TestSuite(L).run(skip='_test_fraction_field')
            sage: L = LazyPowerSeriesRing(QQ['q'], 's, t')
            sage: TestSuite(L).run(skip='_test_fraction_field')  # long time

            sage: L = LazyPowerSeriesRing(ZZ['q'], 't')
            sage: TestSuite(L).run(skip='_test_fraction_field')
            sage: L = LazyPowerSeriesRing(ZZ['q'], 's, t')
            sage: TestSuite(L).run(skip='_test_fraction_field')  # long time

            sage: LazyPowerSeriesRing.options._reset()  # reset the options

        Check that :issue:`34470` is fixed::

            sage: L.<t> = LazyPowerSeriesRing(QQ)
            sage: L in CompleteDiscreteValuationRings
            True
            sage: L.uniformizer()
            t
            sage: lcm(1/(1 - t^2) - 1, t)
            t^2

            sage: L.<t> = LazyPowerSeriesRing(ZZ)
            sage: L in PrincipalIdealDomains
            False

        The ideal generated by `s` and `t` is not principal::

            sage: L = LazyPowerSeriesRing(QQ, 's, t')
            sage: L in PrincipalIdealDomains
            False
        """
    def construction(self):
        """
        Return a pair ``(F, R)``, where ``F`` is a
        :class:`CompletionFunctor` and `R` is a ring, such that
        ``F(R)`` returns ``self``.

        EXAMPLES::

            sage: L = LazyPowerSeriesRing(ZZ, 't')
            sage: L.construction()
            (Completion[t, prec=+Infinity],
             Sparse Univariate Polynomial Ring in t over Integer Ring)
        """
    @cached_method
    def gen(self, n: int = 0):
        """
        Return the ``n``-th generator of ``self``.

        EXAMPLES::

            sage: L = LazyPowerSeriesRing(ZZ, 'z')
            sage: L.gen()
            z
            sage: L.gen(3)
            Traceback (most recent call last):
            ...
            IndexError: there is only one generator
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(ZZ)
            sage: L.ngens()
            1
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: L = LazyPowerSeriesRing(ZZ, 'x,y')
            sage: L.gens()
            (x, y)
        """
    def uniformizer(self):
        """
        Return a uniformizer of ``self``.

        EXAMPLES::

            sage: L = LazyPowerSeriesRing(QQ, 'x')
            sage: L.uniformizer()
            x
        """
    def residue_field(self):
        """
        Return the residue field of the ring of integers of ``self``.

        EXAMPLES::

            sage: L = LazyPowerSeriesRing(QQ, 'x')
            sage: L.residue_field()
            Rational Field
        """
    def fraction_field(self):
        """
        Return the fraction field of ``self``.

        If this is with a single variable over a field, then the fraction
        field is the field of (lazy) formal Laurent series.

        .. TODO::

            Implement other fraction fields.

        EXAMPLES::

            sage: L.<x> = LazyPowerSeriesRing(QQ)
            sage: L.fraction_field()
            Lazy Laurent Series Ring in x over Rational Field
        """
    def some_elements(self):
        '''
        Return a list of elements of ``self``.

        EXAMPLES::

            sage: L = LazyPowerSeriesRing(ZZ, \'z\')
            sage: L.some_elements()[:6]
            [0, 1, z + z^2 + z^3 + O(z^4),
             -12 - 8*z + z^2 + z^3,
             1 + z - 2*z^2 - 7*z^3 - z^4 + 20*z^5 + 23*z^6 + O(z^7),
             z + 4*z^2 + 9*z^3 + 16*z^4 + 25*z^5 + 36*z^6 + O(z^7)]

            sage: L = LazyPowerSeriesRing(GF(3)["q"], \'z\')
            sage: L.some_elements()[:6]
            [0, 1, z + q*z^2 + q*z^3 + q*z^4 + O(z^5),
             z + z^2 + z^3,
             1 + z + z^2 + 2*z^3 + 2*z^4 + 2*z^5 + O(z^6),
             z + z^2 + z^4 + z^5 + O(z^7)]

            sage: L = LazyPowerSeriesRing(GF(3), \'q, t\')
            sage: L.some_elements()[:6]
            [0, 1, q,
             q + q^2 + q^3,
             1 + q + q^2 - q^3 - q^4 - q^5 - q^6 + O(q,t)^7,
             1 + (q+t) + (q^2-q*t+t^2) + (q^3+t^3) + (q^4+q^3*t+q*t^3+t^4)
             + (q^5-q^4*t+q^3*t^2+q^2*t^3-q*t^4+t^5) + (q^6-q^3*t^3+t^6) + O(q,t)^7]
        '''
    def taylor(self, f):
        """
        Return the Taylor expansion around `0` of the function ``f``.

        INPUT:

        - ``f`` -- a function such that one of the following works:

          * the substitution `f(z_1, \\ldots, z_n)`, where `(z_1, \\ldots, z_n)`
            are the generators of ``self``
          * `f` is a function with no poles at `0` and has a ``derivative``
            method

        .. WARNING::

            For inputs as symbolic functions/expressions, this does not check
            that the function does not have poles at `0`.

        EXAMPLES::

            sage: L.<z> = LazyPowerSeriesRing(QQ)
            sage: x = SR.var('x')
            sage: f(x) = (1 + x) / (1 - x^3)
            sage: L.taylor(f)
            1 + z + z^3 + z^4 + z^6 + O(z^7)
            sage: (1 + z) / (1 - z^3)
            1 + z + z^3 + z^4 + z^6 + O(z^7)
            sage: f(x) = cos(x + pi/2)
            sage: L.taylor(f)
            -z + 1/6*z^3 - 1/120*z^5 + O(z^7)

        For inputs as symbolic functions/expressions, the function must
        not have any poles at `0`::

            sage: L.<z> = LazyPowerSeriesRing(QQ, sparse=True)
            sage: f = 1 / sin(x)
            sage: L.taylor(f)
            <repr(...) failed: ValueError: power::eval(): division by zero>

        Different multivariate inputs::

            sage: L.<a,b> = LazyPowerSeriesRing(QQ)
            sage: def f(x, y): return (1 + x) / (1 + y)
            sage: L.taylor(f)
            1 + (a-b) - (a*b-b^2) + (a*b^2-b^3) - (a*b^3-b^4) + (a*b^4-b^5) - (a*b^5-b^6) + O(a,b)^7
            sage: g(w, z) = (1 + w) / (1 + z)
            sage: L.taylor(g)
            1 + (a-b) - (a*b-b^2) + (a*b^2-b^3) - (a*b^3-b^4) + (a*b^4-b^5) - (a*b^5-b^6) + O(a,b)^7
            sage: y = SR.var('y')
            sage: h = (1 + x) / (1 + y)
            sage: L.taylor(h)
            1 + (a-b) - (a*b-b^2) + (a*b^2-b^3) - (a*b^3-b^4) + (a*b^4-b^5) - (a*b^5-b^6) + O(a,b)^7
        """

class LazyCompletionGradedAlgebra(LazySeriesRing):
    """
    The completion of a graded algebra consisting of formal series.

    For a graded algebra `A`, we can form a completion of `A` consisting of
    all formal series of `A` such that each homogeneous component is
    a finite linear combination of basis elements of `A`.

    INPUT:

    - ``basis`` -- a graded algebra
    - ``names`` -- name(s) of the alphabets
    - ``sparse`` -- boolean (default: ``True``); whether we use a sparse or
      a dense representation

    EXAMPLES::

        sage: # needs sage.modules
        sage: NCSF = NonCommutativeSymmetricFunctions(QQ)
        sage: S = NCSF.Complete()
        sage: L = S.formal_series_ring(); L
        Lazy completion of Non-Commutative Symmetric Functions
         over the Rational Field in the Complete basis
        sage: f = 1 / (1 - L(S[1])); f
        S[] + S[1] + (S[1,1]) + (S[1,1,1]) + (S[1,1,1,1]) + (S[1,1,1,1,1])
         + (S[1,1,1,1,1,1]) + O^7
        sage: g = 1 / (1 - L(S[2])); g
        S[] + S[2] + (S[2,2]) + (S[2,2,2]) + O^7
        sage: f * g
        S[] + S[1] + (S[1,1]+S[2]) + (S[1,1,1]+S[1,2])
         + (S[1,1,1,1]+S[1,1,2]+S[2,2]) + (S[1,1,1,1,1]+S[1,1,1,2]+S[1,2,2])
         + (S[1,1,1,1,1,1]+S[1,1,1,1,2]+S[1,1,2,2]+S[2,2,2]) + O^7
        sage: g * f
        S[] + S[1] + (S[1,1]+S[2]) + (S[1,1,1]+S[2,1])
         + (S[1,1,1,1]+S[2,1,1]+S[2,2]) + (S[1,1,1,1,1]+S[2,1,1,1]+S[2,2,1])
         + (S[1,1,1,1,1,1]+S[2,1,1,1,1]+S[2,2,1,1]+S[2,2,2]) + O^7
        sage: f * g - g * f
        (S[1,2]-S[2,1]) + (S[1,1,2]-S[2,1,1])
         + (S[1,1,1,2]+S[1,2,2]-S[2,1,1,1]-S[2,2,1])
         + (S[1,1,1,1,2]+S[1,1,2,2]-S[2,1,1,1,1]-S[2,2,1,1]) + O^7
    """
    Element = LazyCompletionGradedAlgebraElement
    def __init__(self, basis, sparse: bool = True, category=None) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: LazySymmetricFunctions.options.halting_precision(6)

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()
            sage: L = LazySymmetricFunctions(s)
            sage: TestSuite(L).run()                                                    # needs lrcalc_python
            sage: p = SymmetricFunctions(GF(5)).p()
            sage: L = LazySymmetricFunctions(p)
            sage: TestSuite(L).run()

        Reversion will only work when the base ring is a field::

            sage: # needs sage.modules
            sage: s = SymmetricFunctions(ZZ).s()
            sage: L = LazySymmetricFunctions(s)
            sage: TestSuite(L).run(skip=[\'_test_revert\'])                               # needs lrcalc_python
            sage: s = SymmetricFunctions(QQ["q"]).s()
            sage: L = LazySymmetricFunctions(s)
            sage: TestSuite(L).run(skip=[\'_test_revert\'])                               # needs lrcalc_python

        Options are remembered across doctests::

            sage: LazySymmetricFunctions.options._reset()

        Check that :issue:`34470` is fixed.  The ideal generated by
        `p[1]` and `p[2]` is not principal::

            sage: p = SymmetricFunctions(QQ).p()                                        # needs sage.modules
            sage: L = LazySymmetricFunctions(s)                                         # needs sage.modules
            sage: L in PrincipalIdealDomains                                            # needs sage.modules
            False

        Check that a basis which is not graded is not enough::

            sage: ht = SymmetricFunctions(ZZ).ht()                                      # needs sage.modules
            sage: L = LazySymmetricFunctions(ht)                                        # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: basis should be in GradedAlgebrasWithBasis

        Check that :issue:`37625` is fixed::

            sage: R = algebras.Free(QQ, (\'a\', \'b\'), degrees=(1, 2))
            sage: L = R.completion()
            sage: a, b = R.gens()
            sage: (L(a) + L(b))^2
            a^2 + (a*b+b*a) + b^2
        '''
    def some_elements(self):
        """
        Return a list of elements of ``self``.

        EXAMPLES::

            sage: m = SymmetricFunctions(GF(5)).m()                                     # needs sage.modules
            sage: L = LazySymmetricFunctions(m)                                         # needs sage.modules
            sage: L.some_elements()[:5]                                                 # needs sage.modules
            [0, m[], 2*m[] + 2*m[1] + 3*m[2], 2*m[1] + 3*m[2],
             3*m[] + 2*m[1] + (m[1,1]+m[2])
                   + (2*m[1,1,1]+m[3])
                   + (2*m[1,1,1,1]+4*m[2,1,1]+2*m[2,2])
                   + (3*m[2,1,1,1]+3*m[3,1,1]+4*m[3,2]+m[5])
                   + (2*m[2,2,1,1]+m[2,2,2]+2*m[3,2,1]+2*m[3,3]+m[4,1,1]+3*m[4,2]+4*m[5,1]+4*m[6])
                   + O^7]

            sage: # needs sage.modules
            sage: NCSF = NonCommutativeSymmetricFunctions(QQ)
            sage: S = NCSF.Complete()
            sage: L = S.formal_series_ring()
            sage: L.some_elements()[:4]
            [0, S[], 2*S[] + 2*S[1] + (3*S[1,1]), 2*S[1] + (3*S[1,1])]
        """

class LazySymmetricFunctions(LazyCompletionGradedAlgebra):
    """
    The ring of lazy symmetric functions.

    INPUT:

    - ``basis`` -- the ring of symmetric functions
    - ``names`` -- name(s) of the alphabets
    - ``sparse`` -- boolean (default: ``True``); whether we use a sparse or a
      dense representation

    EXAMPLES::

        sage: s = SymmetricFunctions(ZZ).s()                                            # needs sage.modules
        sage: LazySymmetricFunctions(s)                                                 # needs sage.modules
        Lazy completion of Symmetric Functions over Integer Ring in the Schur basis

        sage: m = SymmetricFunctions(ZZ).m()                                            # needs sage.modules
        sage: LazySymmetricFunctions(tensor([s, m]))                                    # needs sage.modules
        Lazy completion of
         Symmetric Functions over Integer Ring in the Schur basis
          # Symmetric Functions over Integer Ring in the monomial basis
    """
    Element = LazySymmetricFunction

class LazyDirichletSeriesRing(LazySeriesRing):
    """
    The ring of lazy Dirichlet series.

    INPUT:

    - ``base_ring`` -- base ring of this Dirichlet series ring
    - ``names`` -- name of the generator of this Dirichlet series ring
    - ``sparse`` -- boolean (default: ``True``); whether this series is sparse or not

    Unlike formal univariate Laurent/power series (over a field),
    the ring of formal Dirichlet series is not a
    :wikipedia:`discrete_valuation_ring`.  On the other hand, it
    is a :wikipedia:`local_ring`.  The unique maximal ideal
    consists of all non-invertible series, i.e., series with
    vanishing constant term.

    .. TODO::

        According to the answers in
        https://mathoverflow.net/questions/5522/dirichlet-series-with-integer-coefficients-as-a-ufd,
        (which, in particular, references :arxiv:`math/0105219`)
        the ring of formal Dirichlet series is actually a
        :wikipedia:`Unique_factorization_domain` over `\\ZZ`.

    .. NOTE::

        An interesting valuation is described in Emil Daniel
        Schwab; Gheorghe Silberberg *A note on some discrete
        valuation rings of arithmetical functions*, Archivum
        Mathematicum, Vol. 36 (2000), No. 2, 103-109,
        http://dml.cz/dmlcz/107723.  Let `J_k` be the ideal of
        Dirichlet series whose coefficient `f[n]` of `n^s`
        vanishes if `n` has less than `k` prime factors, counting
        multiplicities.  For any Dirichlet series `f`, let `D(f)`
        be the largest integer `k` such that `f` is in `J_k`.
        Then `D` is surjective, `D(f g) = D(f) + D(g)` for
        nonzero `f` and `g`, and `D(f + g) \\geq \\min(D(f), D(g))`
        provided that `f + g` is nonzero.

        For example, `J_1` are series with no constant term, and
        `J_2` are series such that `f[1]` and `f[p]` for prime
        `p` vanish.

        Since this is a chain of increasing ideals, the ring of
        formal Dirichlet series is not a
        :wikipedia:`Noetherian_ring`.

        Evidently, this valuation cannot be computed for a given
        series.

    EXAMPLES::

        sage: LazyDirichletSeriesRing(ZZ, 't')
        Lazy Dirichlet Series Ring in t over Integer Ring

    The ideal generated by `2^-s` and `3^-s` is not principal::

        sage: L = LazyDirichletSeriesRing(QQ, 's')
        sage: L in PrincipalIdealDomains
        False
    """
    Element = LazyDirichletSeries
    __classcall_private__: Incomplete
    def __init__(self, base_ring, names, sparse: bool = True, category=None) -> None:
        """
        Initialize the ring.

        TESTS::

            sage: LazyDirichletSeriesRing.options.halting_precision(12)

            sage: L = LazyDirichletSeriesRing(ZZ, 't')
            sage: TestSuite(L).run()                                                    # needs sage.symbolic

            sage: L = LazyDirichletSeriesRing(QQ, 't')
            sage: TestSuite(L).run()                                                    # needs sage.symbolic

            sage: LazyDirichletSeriesRing.options._reset()  # reset the options
        """
    @cached_method
    def one(self):
        """
        Return the constant series `1`.

        EXAMPLES::

            sage: L = LazyDirichletSeriesRing(ZZ, 'z')
            sage: L.one()                                                               # needs sage.symbolic
            1
            sage: ~L.one()                                                              # needs sage.symbolic
            1 + O(1/(8^z))
        """
    def some_elements(self):
        """
        Return a list of elements of ``self``.

        EXAMPLES::

            sage: L = LazyDirichletSeriesRing(ZZ, 'z')
            sage: l = L.some_elements()
            sage: l                                                                     # needs sage.symbolic
            [0, 1,
             1/(4^z) + 1/(5^z) + 1/(6^z) + O(1/(7^z)),
             1/(2^z) - 1/(3^z) + 2/4^z - 2/5^z + 3/6^z - 3/7^z + 4/8^z - 4/9^z,
             1/(2^z) - 1/(3^z) + 2/4^z - 2/5^z + 3/6^z - 3/7^z + 4/8^z - 4/9^z + 1/(10^z) + 1/(11^z) + 1/(12^z) + O(1/(13^z)),
             1 + 4/2^z + 9/3^z + 16/4^z + 25/5^z + 36/6^z + 49/7^z + O(1/(8^z))]

            sage: L = LazyDirichletSeriesRing(QQ, 'z')
            sage: l = L.some_elements()
            sage: l                                                                     # needs sage.symbolic
            [0, 1,
             1/2/4^z + 1/2/5^z + 1/2/6^z + O(1/(7^z)),
             1/2 - 1/2/2^z + 2/3^z - 2/4^z + 1/(6^z) - 1/(7^z) + 42/8^z + 2/3/9^z,
             1/2 - 1/2/2^z + 2/3^z - 2/4^z + 1/(6^z) - 1/(7^z) + 42/8^z + 2/3/9^z + 1/2/10^z + 1/2/11^z + 1/2/12^z + O(1/(13^z)),
             1 + 4/2^z + 9/3^z + 16/4^z + 25/5^z + 36/6^z + 49/7^z + O(1/(8^z))]
        """
    def polylogarithm(self, z):
        """
        Return the polylogarithm at `z` considered as a Dirichlet series
        in ``self``.

        The *polylogarithm* at `z` is the Dirichlet series

        .. MATH::

            \\mathrm{Li}_s(z) = \\sum_{k=1}^{\\infty} \\frac{z^k}{k^s}.

        EXAMPLES::

            sage: R.<z> = ZZ[]
            sage: L = LazyDirichletSeriesRing(R, 's')
            sage: L.polylogarithm(z)
            z + z^2/2^s + z^3/3^s + z^4/4^s + z^5/5^s + z^6/6^s + z^7/7^s + O(1/(8^s))

        At `z = 1`, this is the Riemann zeta function::

            sage: L.polylogarithm(1)
            1 + 1/(2^s) + 1/(3^s) + 1/(4^s) + 1/(5^s) + 1/(6^s) + 1/(7^s) + O(1/(8^s))

        At `z = -1`, this is the negative of the Dirichlet eta function::

            sage: -L.polylogarithm(-1)
            1 - 1/(2^s) + 1/(3^s) - 1/(4^s) + 1/(5^s) - 1/(6^s) + 1/(7^s) + O(1/(8^s))

        REFERENCES:

        - :wikipedia:`Polylogarithm`
        """
    polylog = polylogarithm
