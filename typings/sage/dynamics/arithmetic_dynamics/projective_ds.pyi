from sage.arith.functions import lcm as lcm
from sage.arith.misc import binomial as binomial, gcd as gcd, is_prime as is_prime, moebius as moebius, next_prime as next_prime, primes as primes
from sage.calculus.functions import jacobian as jacobian
from sage.categories.fields import Fields as Fields
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.categories.homset import End as End
from sage.categories.number_fields import NumberFields as NumberFields
from sage.dynamics.arithmetic_dynamics.endPN_automorphism_group import automorphism_group_FF as automorphism_group_FF, automorphism_group_QQ_CRT as automorphism_group_QQ_CRT, automorphism_group_QQ_fixedpoints as automorphism_group_QQ_fixedpoints, conjugating_set_helper as conjugating_set_helper, conjugating_set_initializer as conjugating_set_initializer, is_conjugate_helper as is_conjugate_helper
from sage.dynamics.arithmetic_dynamics.generic_ds import DynamicalSystem as DynamicalSystem
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.classcall_metaclass import typecall as typecall
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.mrange import xmrange as xmrange
from sage.modules.free_module_element import vector as vector
from sage.parallel.ncpus import ncpus as ncpus
from sage.parallel.use_fork import p_iter_fork as p_iter_fork
from sage.rings.complex_mpfr import ComplexField as ComplexField
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import Zmod as Zmod
from sage.rings.fraction_field import FractionField as FractionField, FractionField_1poly_field as FractionField_1poly_field, FractionField_generic as FractionField_generic
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.morphism import RingHomomorphism_im_gens as RingHomomorphism_im_gens
from sage.rings.polynomial.flatten import FlatteningMorphism as FlatteningMorphism, UnflatteningMorphism as UnflatteningMorphism
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.qqbar import QQbar as QQbar, number_field_elements_from_algebraics as number_field_elements_from_algebraics
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RealField as RealField
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.schemes.generic.morphism import SchemeMorphism_polynomial as SchemeMorphism_polynomial
from sage.schemes.product_projective.space import ProductProjectiveSpaces_ring as ProductProjectiveSpaces_ring
from sage.schemes.projective.projective_morphism import SchemeMorphism_polynomial_projective_space as SchemeMorphism_polynomial_projective_space, SchemeMorphism_polynomial_projective_space_field as SchemeMorphism_polynomial_projective_space_field, SchemeMorphism_polynomial_projective_space_finite_field as SchemeMorphism_polynomial_projective_space_finite_field
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, ProjectiveSpace_ring as ProjectiveSpace_ring
from sage.schemes.projective.projective_subscheme import AlgebraicScheme_subscheme_projective as AlgebraicScheme_subscheme_projective
from sage.structure.element import get_coercion_model as get_coercion_model

class DynamicalSystem_projective(SchemeMorphism_polynomial_projective_space, DynamicalSystem):
    """A dynamical system of projective schemes determined by homogeneous
    polynomials that define what the morphism does on points in the
    ambient projective space.

    .. WARNING::

        You should not create objects of this class directly because
        no type or consistency checking is performed. The preferred
        method to construct such dynamical systems is to use
        :func:`~sage.dynamics.arithmetic_dynamics.generic_ds.DynamicalSystem_projective`
        function

    INPUT:

    - ``morphism_or_polys`` -- a SchemeMorphism, a polynomial, a
      rational function, or a list or tuple of homogeneous polynomials

    - ``domain`` -- (optional) projective space or projective subscheme

    - ``names`` -- tuple of strings (default: ``'X','Y'``) to be used as coordinate
      names for a projective space that is constructed

      The following combinations of ``morphism_or_polys`` and
      ``domain`` are meaningful:

      * ``morphism_or_polys`` is a SchemeMorphism; ``domain`` is
        ignored in this case.

      * ``morphism_or_polys`` is a list of homogeneous polynomials
        that define a rational endomorphism of ``domain``.

      * ``morphism_or_polys`` is a list of homogeneous polynomials and
        ``domain`` is unspecified; ``domain`` is then taken to be the
        projective space of appropriate dimension over the common base ring,
        if one exists, of the elements of ``morphism_or_polys``.

      * ``morphism_or_polys`` is a single polynomial or rational
        function; ``domain`` is ignored and taken to be a
        1-dimensional projective space over the base ring of
        ``morphism_or_polys`` with coordinate names given by ``names``.

    OUTPUT: :class:`DynamicalSystem_projective`

    EXAMPLES::

        sage: P1.<x,y> = ProjectiveSpace(QQ,1)
        sage: DynamicalSystem_projective([y, 2*x])
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (x : y) to
                (y : 2*x)

    We can define dynamical systems on `P^1` by giving a polynomial or
    rational function::

        sage: R.<t> = QQ[]
        sage: DynamicalSystem_projective(t^2 - 3)
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (X : Y) to
                (X^2 - 3*Y^2 : Y^2)
        sage: DynamicalSystem_projective(1/t^2)
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (X : Y) to
                (Y^2 : X^2)

    ::

        sage: R.<x> = PolynomialRing(QQ,1)
        sage: DynamicalSystem_projective(x^2, names=['a','b'])
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (a : b) to
                (a^2 : b^2)

    Symbolic Ring elements are not allowed::

        sage: x,y = var('x,y')                                                          # needs sage.symbolic
        sage: DynamicalSystem_projective([x^2, y^2])                                    # needs sage.symbolic
        Traceback (most recent call last):
        ...
        ValueError: [x^2, y^2] must be elements of a polynomial ring

    ::

        sage: R.<x> = PolynomialRing(QQ,1)
        sage: DynamicalSystem_projective(x^2)
        Dynamical System of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (X : Y) to
                (X^2 : Y^2)

    ::

        sage: R.<t> = PolynomialRing(QQ)
        sage: P.<x,y,z> = ProjectiveSpace(R, 2)
        sage: X = P.subscheme([x])
        sage: DynamicalSystem_projective([x^2, t*y^2, x*z], domain=X)
        Dynamical System of Closed subscheme of Projective Space of dimension
        2 over Univariate Polynomial Ring in t over Rational Field defined by:
          x
          Defn: Defined on coordinates by sending (x : y : z) to
                (x^2 : t*y^2 : x*z)

    When elements of the quotient ring are used, they are reduced::

        sage: P.<x,y,z> = ProjectiveSpace(CC, 2)
        sage: X = P.subscheme([x - y])
        sage: u,v,w = X.coordinate_ring().gens()                                        # needs sage.rings.function_field
        sage: DynamicalSystem_projective([u^2, v^2, w*u], domain=X)                     # needs sage.rings.function_field
        Dynamical System of Closed subscheme of Projective Space of dimension
        2 over Complex Field with 53 bits of precision defined by:
          x - y
          Defn: Defined on coordinates by sending (x : y : z) to
                (y^2 : y^2 : y*z)

    We can also compute the forward image of subschemes through
    elimination. In particular, let `X = V(h_1,\\ldots, h_t)` and define the ideal
    `I = (h_1,\\ldots,h_t,y_0-f_0(\\bar{x}), \\ldots, y_n-f_n(\\bar{x}))`.
    Then the elimination ideal `I_{n+1} = I \\cap K[y_0,\\ldots,y_n]` is a homogeneous
    ideal and `f(X) = V(I_{n+1})`::

        sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
        sage: f = DynamicalSystem_projective([(x-2*y)^2, (x-2*z)^2, x^2])
        sage: X = P.subscheme(y - z)
        sage: f(f(f(X)))                                                                # needs sage.rings.function_field
        Closed subscheme of Projective Space of dimension 2 over Rational Field
        defined by:
          y - z

    ::

        sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
        sage: f = DynamicalSystem_projective([(x-2*y)^2, (x-2*z)^2, (x-2*w)^2, x^2])
        sage: f(P.subscheme([x, y, z]))                                                 # needs sage.rings.function_field
        Closed subscheme of Projective Space of dimension 3 over Rational Field
        defined by:
          w,
          y,
          x

    ::

        sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
        sage: DynamicalSystem_projective([x^2*u, y^2*w, z^2*u, w^2, u^2], domain=T)
        Dynamical System of Product of projective spaces P^2 x P^1 over Rational Field
          Defn: Defined by sending (x : y : z , w : u) to
                (x^2*u : y^2*w : z^2*u , w^2 : u^2).

    ::

        sage: # needs sage.rings.number_field
        sage: K.<v> = QuadraticField(-7)
        sage: P.<x,y> = ProjectiveSpace(K, 1)
        sage: f = DynamicalSystem([x^3 + v*x*y^2, y^3])
        sage: fbar = f.change_ring(QQbar)
        sage: fbar.is_postcritically_finite()
        False
    """
    @staticmethod
    def __classcall_private__(cls, morphism_or_polys, domain=None, names=None):
        '''
        Return the appropriate dynamical system on a projective scheme.

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: P1 = ProjectiveSpace(R)
            sage: f = DynamicalSystem_projective([x - y, x*y])
            Traceback (most recent call last):
            ...
            ValueError: polys (=[x - y, x*y]) must be of the same degree
            sage: DynamicalSystem_projective([x - 1, x*y + x])
            Traceback (most recent call last):
            ...
            ValueError: polys (=[x - 1, x*y + x]) must be homogeneous

        ::

            sage: DynamicalSystem_projective([exp(x), exp(y)])                          # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: [e^x, e^y] must be elements of a polynomial ring

        ::

            sage: T.<x,y,z,w,u> = ProductProjectiveSpaces([2, 1], QQ)
            sage: DynamicalSystem_projective([x^2*u, y^2*w, z^2*u, w^2, u*z], domain=T)
            Traceback (most recent call last):
            ...
            TypeError: polys (=[x^2*u, y^2*w, z^2*u, w^2, z*u]) must be
            multi-homogeneous of the same degrees (by component)

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: DynamicalSystem_projective([x^2, y^2], A)
            Traceback (most recent call last):
            ...
            ValueError: "domain" must be a projective scheme
            sage: H = End(A)
            sage: f = H([x,y])
            sage: DynamicalSystem_projective(f)
            Traceback (most recent call last):
            ...
            ValueError: "domain" must be a projective scheme

        ::

            sage: R.<x> = PolynomialRing(QQ,1)
            sage: DynamicalSystem_projective(x^2, names=\'t\')
            Traceback (most recent call last):
            ...
            ValueError: specify 2 variable names

        ::

            sage: P1.<x,y> = ProjectiveSpace(QQ,1)
            sage: DynamicalSystem_projective([y, x, y], domain=P1)
            Traceback (most recent call last):
            ...
            ValueError: number of polys does not match dimension of Projective Space of dimension 1 over Rational Field

        ::

            sage: A.<x,y> = AffineSpace(QQ,2)
            sage: DynamicalSystem_projective([y,x], domain=A)
            Traceback (most recent call last):
            ...
            ValueError: "domain" must be a projective scheme

        ::

            sage: R.<x> = QQ[]
            sage: DynamicalSystem([x^2])
            Traceback (most recent call last):
            ...
            ValueError: list/tuple must have at least 2 polynomials

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([CC.0*x^2 + 2*y^2, 1*y^2], domain=P)
            Traceback (most recent call last):
            ...
            TypeError: coefficients of polynomial not in Rational Field
        '''
    def __init__(self, polys, domain) -> None:
        """
        The Python constructor.

        See :class:`DynamicalSystem` for details.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: DynamicalSystem_projective([3/5*x^2, y^2], domain=P)
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (3/5*x^2 : y^2)
        """
    def __copy__(self):
        """
        Return a copy of this dynamical system.

        OUTPUT: :class:`DynamicalSystem_projective`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([3/5*x^2,6*y^2])
            sage: g = copy(f)
            sage: f == g
            True
            sage: f is g
            False
        """
    def dehomogenize(self, n):
        """
        Return the standard dehomogenization at the ``n[0]`` coordinate
        for the domain and the ``n[1]`` coordinate for the codomain.

        Note that the new function is defined over the fraction field
        of the base ring of this map.

        INPUT:

        - ``n`` -- tuple of nonnegative integers; if ``n`` is an integer,
          then the two values of the tuple are assumed to be the same

        OUTPUT:

        If the dehomogenizing indices are the same for the domain and
        codomain, then a :class:`DynamicalSystem_affine` given by
        dehomogenizing the source and target of ``self`` with respect to
        the given indices is returned. If the dehomogenizing indices
        for the domain and codomain are different then the resulting
        affine patches are different and a scheme morphism is returned.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.dehomogenize(0)
            Dynamical System of Affine Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (y) to
                    (y^2/(y^2 + 1))
            sage: f.dehomogenize((0, 1))
            Scheme morphism:
              From: Affine Space of dimension 1 over Integer Ring
              To:   Affine Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (y) to
                    ((y^2 + 1)/y^2)
        """
    def dynatomic_polynomial(self, period):
        """
        For a dynamical system of `\\mathbb{P}^1` compute the dynatomic
        polynomial.

        The dynatomic polynomial is the analog of the cyclotomic
        polynomial and its roots are the points of formal period `period`.
        If possible the division is done in the coordinate ring of this
        map and a polynomial is returned. In rings where that is not
        possible, a :class:`FractionField` element will be returned.
        In certain cases, when the conversion back to a polynomial fails,
        a :class:`SymbolRing` element will be returned.

        ALGORITHM:

        For a positive integer `n`, let `[F_n,G_n]` be the coordinates of the `n`-th
        iterate of `f`. Then construct

        .. MATH::

            \\Phi^{\\ast}_n(f)(x,y) = \\sum_{d \\mid n}
                (yF_d(x,y) - xG_d(x,y))^{\\mu(n/d)},

        where `\\mu` is the Möbius function.

        For a pair `[m,n]`, let `f^m = [F_m,G_m]`. Compute

        .. MATH::

            \\Phi^{\\ast}_{m,n}(f)(x,y) = \\Phi^{\\ast}_n(f)(F_m,G_m) /
                \\Phi^{\\ast}_n(f)(F_{m-1},G_{m-1})

        REFERENCES:

        - [Hutz2015]_
        - [MoPa1994]_

        INPUT:

        - ``period`` -- positive integer or a list/tuple `[m,n]` where
          `m` is the preperiod and `n` is the period

        OUTPUT:

        If possible, a two variable polynomial in the coordinate ring
        of this map. Otherwise a fraction field element of the coordinate
        ring of this map. Or, a :class:`SymbolicRing` element.

        .. TODO::

            - Do the division when the base ring is `p`-adic so that
              the output is a polynomial.

            - Convert back to a polynomial when the base ring is a
              function field (not over `\\QQ` or `F_p`).

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.dynatomic_polynomial(2)                                             # needs sage.libs.pari
            x^2 + x*y + 2*y^2

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: f.dynatomic_polynomial(4)                                             # needs sage.libs.pari
            2*x^12 + 18*x^10*y^2 + 57*x^8*y^4 + 79*x^6*y^6 + 48*x^4*y^8 + 12*x^2*y^10 + y^12

        ::

            sage: P.<x,y> = ProjectiveSpace(CC,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, 3*x*y])
            sage: f.dynatomic_polynomial(3)                                             # needs sage.libs.pari
            13.0000000000000*x^6 + 117.000000000000*x^4*y^2 +
            78.0000000000000*x^2*y^4 + y^6

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - 10/9*y^2, y^2])
            sage: f.dynatomic_polynomial([2,1])
            x^4*y^2 - 11/9*x^2*y^4 - 80/81*y^6

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2])
            sage: f.dynatomic_polynomial([2,3])                                         # needs sage.libs.pari
            x^12 - 95/8*x^10*y^2 + 13799/256*x^8*y^4 - 119953/1024*x^6*y^6 +
            8198847/65536*x^4*y^8 - 31492431/524288*x^2*y^10 +
            172692729/16777216*y^12

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.dynatomic_polynomial([1,2])                                         # needs sage.libs.pari
            x^2 - x*y

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 - y^3, 3*x*y^2])
            sage: f.dynatomic_polynomial([0,4])==f.dynatomic_polynomial(4)              # needs sage.libs.pari
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y, z^2])
            sage: f.dynatomic_polynomial(2)
            Traceback (most recent call last):
            ...
            TypeError: does not make sense in dimension >1

        ::

            sage: P.<x,y> = ProjectiveSpace(Qp(5),1)                                    # needs sage.rings.padics
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])                      # needs sage.rings.padics
            sage: f.dynatomic_polynomial(2)                                             # needs sage.rings.padics
            (x^4*y + (2 + O(5^20))*x^2*y^3 - x*y^4 + (2 + O(5^20))*y^5)/(x^2*y - x*y^2 + y^3)

        ::

            sage: L.<t> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(L,1)
            sage: f = DynamicalSystem_projective([x^2 + t*y^2, y^2])
            sage: f.dynatomic_polynomial(2)                                             # needs sage.libs.pari
            x^2 + x*y + (t + 1)*y^2

        ::

            sage: K.<c> = PolynomialRing(ZZ)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.dynatomic_polynomial([1, 2])                                        # needs sage.libs.pari
            x^2 - x*y + (c + 1)*y^2

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.dynatomic_polynomial(2)                                             # needs sage.libs.pari
            x^2 + x*y + 2*y^2
            sage: R.<X> = PolynomialRing(QQ)
            sage: K.<c> = NumberField(X^2 + X + 2)                                      # needs sage.rings.number_field
            sage: PP = P.change_ring(K)
            sage: ff = f.change_ring(K)
            sage: p = PP((c, 1))
            sage: ff(ff(p)) == p
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: f.dynatomic_polynomial([2, 2])                                        # needs sage.libs.pari
            x^4 + 4*x^2*y^2 + y^4
            sage: R.<X> = PolynomialRing(QQ)
            sage: K.<c> = NumberField(X^4 + 4*X^2 + 1)                                  # needs sage.rings.number_field
            sage: PP = P.change_ring(K)
            sage: ff = f.change_ring(K)
            sage: p = PP((c, 1))
            sage: ff.nth_iterate(p, 4) == ff.nth_iterate(p, 2)                          # needs sage.rings.number_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(CC, 1)
            sage: f = DynamicalSystem_projective([x^2 - CC.0/3*y^2, y^2])
            sage: f.dynatomic_polynomial(2)                                             # needs sage.libs.pari
            (x^4*y + (-0.666666666666667*I)*x^2*y^3 - x*y^4
             + (-0.111111111111111 - 0.333333333333333*I)*y^5)/(x^2*y - x*y^2
                                                                 + (-0.333333333333333*I)*y^3)

        ::

            sage: P.<x,y> = ProjectiveSpace(CC, 1)
            sage: f = DynamicalSystem_projective([x^2 - CC.0/5*y^2, y^2])
            sage: f.dynatomic_polynomial(2)                                             # needs sage.libs.pari
            x^2 + x*y + (1.00000000000000 - 0.200000000000000*I)*y^2

        ::

            sage: L.<t> = PolynomialRing(QuadraticField(2).maximal_order())             # needs sage.rings.number_field
            sage: P.<x, y> = ProjectiveSpace(L.fraction_field(), 1)
            sage: f = DynamicalSystem_projective([x^2 + (t^2 + 1)*y^2, y^2])
            sage: f.dynatomic_polynomial(2)                                             # needs sage.libs.pari sage.rings.number_field
            x^2 + x*y + (t^2 + 2)*y^2

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 5*y^2, y^2])
            sage: f.dynatomic_polynomial([3,0 ])
            0

        TESTS:

        We check that the dynatomic polynomial has the right
        parent (see :issue:`18409`)::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar,1)
            sage: f = DynamicalSystem_projective([x^2 - 1/3*y^2, y^2])
            sage: f.dynatomic_polynomial(2).parent()                                    # needs sage.libs.pari
            Multivariate Polynomial Ring in x, y over Algebraic Field

        ::

            sage: # needs sage.rings.number_field
            sage: T.<v> = QuadraticField(33)
            sage: S.<t> = PolynomialRing(T)
            sage: P.<x,y> = ProjectiveSpace(FractionField(S),1)
            sage: f = DynamicalSystem_projective([t*x^2 - 1/t*y^2, y^2])
            sage: f.dynatomic_polynomial([1, 2]).parent()                               # needs sage.libs.pari
            Multivariate Polynomial Ring in x, y over Fraction Field of Univariate Polynomial
            Ring in t over Number Field in v with defining polynomial x^2 - 33 with v = 5.744562646538029?

        ::

            sage: P.<x, y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^3 - y^3*2, y^3])
            sage: f.dynatomic_polynomial(1).parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R,1)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.dynatomic_polynomial([1,2]).parent()                                # needs sage.libs.pari
            Multivariate Polynomial Ring in x, y over Univariate
            Polynomial Ring in c over Rational Field

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, (1)*y^2 + (1)*x*y])
            sage: f.dynatomic_polynomial([1,2]).parent()                                # needs sage.libs.pari
            Multivariate Polynomial Ring in x, y over Integer Ring

        ::

            sage: P.<x, y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.dynatomic_polynomial(0)
            0
            sage: f.dynatomic_polynomial([0,0])
            0
            sage: f.dynatomic_polynomial(-1)
            Traceback (most recent call last):
            ...
            TypeError: period must be a positive integer

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R,1)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.dynatomic_polynomial([1,2]).parent()                                # needs sage.libs.pari
            Multivariate Polynomial Ring in x, y over Univariate Polynomial Ring in
            c over Rational Field

        Some rings still return :class:`SymoblicRing` elements::

            sage: S.<t> = FunctionField(CC)
            sage: P.<x,y> = ProjectiveSpace(S,1)
            sage: f = DynamicalSystem_projective([t*x^2-1*y^2, t*y^2])
            sage: f.dynatomic_polynomial([1, 2]).parent()                               # needs sage.libs.pari
            Symbolic Ring

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: S = R.quo(R.ideal(y^2 - x + 1))
            sage: P.<u,v> = ProjectiveSpace(FractionField(S),1)
            sage: f = DynamicalSystem_projective([u^2 + S(x^2)*v^2, v^2])
            sage: dyn = f.dynatomic_polynomial([1,1]); dyn
            v^3*xbar^2 + u^2*v + u*v^2
            sage: dyn.parent()
            Symbolic Ring
        """
    def nth_iterate_map(self, n, normalize: bool = False):
        """
        Return the ``n``-th iterate of this dynamical system.

        ALGORITHM:

        Uses a form of successive squaring to reducing computations.

        .. TODO:: This could be improved.

        INPUT:

        - ``n`` -- positive integer

        - ``normalize`` -- boolean; remove gcd's during iteration

        OUTPUT: a projective dynamical system

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.nth_iterate_map(2)
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^4 + 2*x^2*y^2 + 2*y^4 : y^4)

        ::

            sage: P.<x,y> = ProjectiveSpace(CC,1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, x*y])
            sage: f.nth_iterate_map(3)
            Dynamical System of Projective Space of dimension 1
             over Complex Field with 53 bits of precision
              Defn: Defined on coordinates by sending (x : y) to
                    (x^8 + (-7.00000000000000)*x^6*y^2 + 13.0000000000000*x^4*y^4
                       + (-7.00000000000000)*x^2*y^6 + y^8
                     : x^7*y + (-4.00000000000000)*x^5*y^3 + 4.00000000000000*x^3*y^5 - x*y^7)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: f = DynamicalSystem_projective([x^2 - y^2, x*y, z^2 + x^2])
            sage: f.nth_iterate_map(2)
            Dynamical System of Projective Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^4 - 3*x^2*y^2 + y^4 : x^3*y - x*y^3
                     : 2*x^4 - 2*x^2*y^2 + y^4 + 2*x^2*z^2 + z^4)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: X = P.subscheme(x*z-y^2)
            sage: f = DynamicalSystem_projective([x^2, x*z, z^2], domain=X)
            sage: f.nth_iterate_map(2)                                                  # needs sage.rings.function_field
            Dynamical System of Closed subscheme of Projective Space of dimension
            2 over Rational Field defined by:
              -y^2 + x*z
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^4 : x^2*z^2 : z^4)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([y^2 * z^3, y^3 * z^2, x^5])
            sage: f.nth_iterate_map( 5, normalize=True)
            Dynamical System of Projective Space of dimension 2 over Rational Field
            Defn: Defined on coordinates by sending (x : y : z) to
            (y^202*z^443 : x^140*y^163*z^342 : x^645)
        """
    def nth_iterate(self, P, n, **kwds):
        """
        Return the ``n``-th iterate of the point ``P`` by this
        dynamical system.

        If ``normalize`` is ``True``, then the coordinates are
        automatically normalized.

        .. TODO:: Is there a more efficient way to do this?

        INPUT:

        - ``P`` -- a point in this map's domain

        - ``n`` -- positive integer

        kwds:

        - ``normalize`` -- boolean (default: ``False``)

        OUTPUT: a point in this map's codomain

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, 2*y^2])
            sage: Q = P(1,1)
            sage: f.nth_iterate(Q,4)
            (32768 : 32768)

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, 2*y^2])
            sage: Q = P(1,1)
            sage: f.nth_iterate(Q, 4, normalize=True)
            (1 : 1)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([x^2, 2*y^2, z^2 - x^2])
            sage: Q = P(2,7,1)
            sage: f.nth_iterate(Q,2)
            (-16/7 : -2744 : 1)

        ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P.<x,y,z> = ProjectiveSpace(R,2)
            sage: f = DynamicalSystem_projective([x^2 + t*y^2, (2-t)*y^2, z^2])
            sage: Q = P(2 + t, 7, t)
            sage: f.nth_iterate(Q,2)
            (t^4 + 2507*t^3 - 6787*t^2 + 10028*t + 16
             : -2401*t^3 + 14406*t^2 - 28812*t + 19208 : t^4)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: X = P.subscheme(x^2-y^2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2], domain=X)
            sage: f.nth_iterate(X(2,2,3), 3)
            (256 : 256 : 6561)

        ::

            sage: K.<c> = FunctionField(QQ)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^3 - 2*x*y^2 - c*y^3, x*y^2])
            sage: f.nth_iterate(P(c,1), 2)
            ((c^6 - 9*c^4 + 25*c^2 - c - 21)/(c^2 - 3) : 1)

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([x^2 + 3*y^2, 2*y^2, z^2])
            sage: f.nth_iterate(P(2, 7, 1), -2)
            Traceback (most recent call last):
            ...
            TypeError: must be a forward orbit

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^3, x*y^2], domain=P)
            sage: f.nth_iterate(P(0, 1), 3, check=False)
            (0 : 0)
            sage: f.nth_iterate(P(0, 1), 3)
            Traceback (most recent call last):
            ...
            ValueError: [0, 0] does not define a valid projective point since all entries are zero

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: f = DynamicalSystem_projective([x^3, x*y^2], domain=P)
            sage: f.nth_iterate(P(2,1), 3, normalize=False)
            (134217728 : 524288)
            sage: f.nth_iterate(P(2,1), 3, normalize=True)
            (256 : 1)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([x + y, y])
            sage: Q = (3,1)
            sage: f.nth_iterate(Q,0)
            (3 : 1)

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([x^2 + y^2, y^2])
            sage: f.nth_iterate(0,0)
            (0 : 1)
        """
    def arakelov_zhang_pairing(self, g, **kwds):
        '''
        Return an estimate of the Arakelov-Zhang pairing of the rational
        maps ``self`` and ``g`` on `\\mathbb{P}^1` over a number field.

        The Arakelov-Zhang pairing was introduced by Petsche, Szpiro, and
        Tucker in 2012, which measures the dynamical closeness of two rational
        maps. They prove inter alia that if one takes a sequence of small points
        for one map (for example, preperiodic points for ``self``) and measure
        their dynamical height with respect to the other map (say, ``g``), then
        the values of the height will tend to the value of the Arakelov-Zhang pairing.

        The Arakelov-Zhang pairing involves mutual energy integrals between dynamical
        measures, which are in the case of polynomials, the equilibrium measures
        of the associated Julia sets at each place. As a result, these pairings
        are very difficult to compute exactly via analytic methods. We use a
        discrete approximation to these energy integrals.

        ALGORITHM:

        We select periodic points of order `n`, or ``n``-th preimages of a
        specified starting value given by ``f_starting_point`` and ``g_starting_point``.
        At the archimedean places and the places of bad reduction of the two maps,
        we compute the discrete approximations to the energy integrals involved
        using these points.

        INPUT:

        - ``g`` -- a rational map of `\\mathbb{P}^1` given as a projective morphism
          ``g`` and ``self`` should have the same field of definition

        kwds:

        - ``n`` -- positive integer (default: 5); order of periodic points to
          use or preimages to take if starting points are specified

        - ``f_starting_point`` -- (default: ``None``) value in the base number field or None.
          If ``f_starting_point`` is None, we solve for points of period ``n`` for ``self``.
          Otherwise, we take ``n``-th preimages of the point given by ``f_starting_point``
          under ``f`` on the affine line.

        - ``g_starting_point`` -- (default: ``None``) value in the base number field or None.
          If ``g_starting_point`` is None, we solve for points of period ``n`` for ``g``.
          Otherwise, we take ``n``-th preimages of the point given by ``g_starting_point``
          under ``g`` on the affine line.

        - ``check_primes_of_bad_reduction`` -- boolean (default: ``False``);
          passed to the ``primes_of_bad_reduction`` function for ``self`` and ``g``

        - ``prec`` -- (default: ``RealField`` default);
          default precision for RealField values which are returned

        - ``noise_multiplier`` -- (default: 2) a real number.
          Discriminant terms involved in the computation at the archimedean places
          are often not needed, particularly if the capacity of the Julia sets is 1,
          and introduce a lot of error. By a well-known result of Mahler (see
          also M. Baker, ""A lower bound for averages of dynamical Green\'s
          functions") such error (for a set of `N` points) is on the order of
          `\\log(N)/N` after our normalization. We check if the value of the
          archimedean discriminant terms is within ``2*noise_multiplier`` of
          `\\log(N)/N`. If so, we discard it. In practice this greatly improves
          the accuracy of the estimate of the pairing. If desired,
          ``noise_multiplier`` can be set to 0, and no terms will be ignored.

        OUTPUT: a real number estimating the Arakelov-Zhang pairing of the two rational maps

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<k> = CyclotomicField(3)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^2 + (2*k + 2)*y^2, y^2])
            sage: g = DynamicalSystem_projective([x^2, y^2])
            sage: pairingval = f.arakelov_zhang_pairing(g, n=5); pairingval
            0.409598197761958

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 4*y^2, y^2])
            sage: g = DynamicalSystem_projective([x^2, y^2])
            sage: pairingval = f.arakelov_zhang_pairing(g, n=6); pairingval             # needs sage.rings.function_field
            0.750178391443644
            sage: # Compare to the exact value:
            sage: dynheight = f.canonical_height(P(0, 1)); dynheight                    # needs sage.libs.pari
            0.75017839144364417318023000563
            sage: dynheight - pairingval                                                # needs sage.libs.pari sage.rings.function_field
            0.000000000000000

        Notice that if we set the noise_multiplier to 0, the accuracy is diminished::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 4*y^2, y^2])
            sage: g = DynamicalSystem_projective([x^2, y^2])
            sage: pairingval = f.arakelov_zhang_pairing(g, n=6, noise_multiplier=0)     # needs sage.rings.function_field
            sage: pairingval                                                            # needs sage.rings.number_field
            0.650660018921632
            sage: dynheight = f.canonical_height(P(0, 1)); dynheight                    # needs sage.libs.pari
            0.75017839144364417318023000563
            sage: pairingval - dynheight                                                # needs sage.libs.pari sage.rings.function_field
            -0.0995183725220122

        We compute the example of Prop. 18(d) from Petsche, Szpiro and Tucker::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([y^2 - (y - x)^2, y^2])
            sage: g = DynamicalSystem_projective([x^2, y^2])
            sage: f.arakelov_zhang_pairing(g)                                           # needs sage.rings.function_field
            0.326954667248466
            sage: # Correct value should be = 0.323067...
            sage: f.arakelov_zhang_pairing(g, n=9)      # long time                     # needs sage.rings.function_field
            0.323091061918965
            sage: _ - 0.323067                          # long time                     # needs sage.rings.function_field
            0.0000240619189654789

        Also from Prop. 18 of Petsche, Szpiro and Tucker, includes places of bad reduction::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(ZZ)
            sage: K.<b> = NumberField(z^3 - 11)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: a = 7/(b - 1)
            sage: f = DynamicalSystem_projective([a*y^2 - (a*y - x)^2, y^2])
            sage: g = DynamicalSystem_projective([x^2, y^2])

        If all archimedean absolute values of a have modulus > 2,
        then the pairing should be h(a).::

            sage: f.arakelov_zhang_pairing(g, n=6)      # long time                     # needs sage.rings.number_field
            1.93846423207664
            sage: _ - a.global_height()                 # long time                     # needs sage.rings.number_field
            -0.00744591697867292
        '''
    def degree_sequence(self, iterates: int = 2):
        """
        Return sequence of degrees of normalized iterates starting with
        the degree of this dynamical system.

        INPUT:

        - ``iterates`` -- (default: 2) positive integer

        OUTPUT: list of integers

        EXAMPLES::

            sage: P2.<X,Y,Z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([Z^2, X*Y, Y^2])
            sage: f.degree_sequence(15)                                                 # needs sage.rings.function_field
            [2, 3, 5, 8, 11, 17, 24, 31, 45, 56, 68, 91, 93, 184, 275]

        ::

            sage: F.<t> = PolynomialRing(QQ)
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: f = DynamicalSystem_projective([Y*Z, X*Y, Y^2 + t*X*Z])
            sage: f.degree_sequence(5)                                                  # needs sage.rings.function_field
            [2, 3, 5, 8, 13]

        ::

            sage: P2.<X,Y,Z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([X^2, Y^2, Z^2])
            sage: f.degree_sequence(10)                                                 # needs sage.rings.function_field
            [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

        ::

            sage: P2.<X,Y,Z> = ProjectiveSpace(ZZ, 2)
            sage: f = DynamicalSystem_projective([X*Y, Y*Z+Z^2, Z^2])
            sage: f.degree_sequence(10)                                                 # needs sage.rings.function_field
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        """
    def dynamical_degree(self, N: int = 3, prec: int = 53):
        """
        Return an approximation to the dynamical degree of this dynamical
        system. The dynamical degree is defined as
        `\\lim_{n \\to \\infty} \\sqrt[n]{\\deg(f^n)}`.

        INPUT:

        - ``N`` -- (default: 3) positive integer, iterate to use
          for approximation

        - ``prec`` -- (default: 53) positive integer, real precision
          to use when computing root

        OUTPUT: real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y, y^2])
            sage: f.dynamical_degree()                                                  # needs sage.rings.function_field
            2.00000000000000

        ::

            sage: P2.<X,Y,Z> = ProjectiveSpace(ZZ, 2)
            sage: f = DynamicalSystem_projective([X*Y, Y*Z + Z^2, Z^2])
            sage: f.dynamical_degree(N=5, prec=100)                                     # needs sage.rings.function_field
            1.4309690811052555010452244131
        """
    def orbit(self, P, N, **kwds):
        """
        Return the orbit of the point ``P`` by this dynamical system.

        Let `F` be this dynamical system. If ``N`` is an integer return
        `[P,F(P),\\ldots,F^N(P)]`. If ``N`` is a list or tuple `N=[m,k]`
        return `[F^m(P),\\ldots,F^k(P)]`.
        Automatically normalize the points if ``normalize=True``. Perform
        the checks on point initialization if ``check=True``.

        INPUT:

        - ``P`` -- a point in this dynamical system's domain

        - ``n`` -- nonnegative integer or list or tuple of two
          nonnegative integers

        kwds:

        - ``check`` -- boolean (default: ``True``)

        - ``normalize`` -- boolean (default: ``False``)

        OUTPUT: list of points in this dynamical system's codomain

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2 - z^2, 2*z^2])
            sage: f.orbit(P(1,2,1), 3)
            [(1 : 2 : 1), (5 : 3 : 2), (34 : 5 : 8), (1181 : -39 : 128)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2 - z^2, 2*z^2])
            sage: f.orbit(P(1,2,1), [2,4])
            [(34 : 5 : 8), (1181 : -39 : 128), (1396282 : -14863 : 32768)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: f = DynamicalSystem_projective([x^2, y^2, x*z], domain=X)
            sage: f.orbit(X(2,2,3), 3, normalize=True)
            [(2 : 2 : 3), (2 : 2 : 3), (2 : 2 : 3), (2 : 2 : 3)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.orbit(P.point([1,2], False), 4, check=False)
            [(1 : 2), (5 : 4), (41 : 16), (1937 : 256), (3817505 : 65536)]

        ::

            sage: K.<c> = FunctionField(QQ)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.orbit(P(0,1), 3)
            [(0 : 1), (c : 1), (c^2 + c : 1), (c^4 + 2*c^3 + c^2 + c : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2], domain=P)
            sage: f.orbit(P.point([1, 2], False), 4, check=False)
            [(1 : 2), (5 : 4), (41 : 16), (1937 : 256), (3817505 : 65536)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2, 2*y^2], domain=P)
            sage: f.orbit(P(2, 1),[-1, 4])
            Traceback (most recent call last):
            ...
            TypeError: orbit bounds must be nonnegative
            sage: f.orbit(P(2, 1), 0.1)
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3, x*y^2], domain=P)
            sage: f.orbit(P(0, 1), 3)
            Traceback (most recent call last):
            ...
            ValueError: [0, 0] does not define a valid projective point since all entries are zero
            sage: f.orbit(P(0, 1), 3, check=False)
            [(0 : 1), (0 : 0), (0 : 0), (0 : 0)]

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: f = DynamicalSystem_projective([x^3, x*y^2], domain=P)
            sage: f.orbit(P(2,1), 3, normalize=False)
            [(2 : 1), (8 : 2), (512 : 32), (134217728 : 524288)]
            sage: f.orbit(P(2, 1), 3, normalize=True)
            [(2 : 1), (4 : 1), (16 : 1), (256 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([x^2, y^2, x*z])
            sage: f.orbit((2/3, 1/3), 3)
            [(2/3 : 1/3 : 1), (2/3 : 1/6 : 1), (2/3 : 1/24 : 1), (2/3 : 1/384 : 1)]

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([x^2 + y^2, y^2])
            sage: f.orbit(0, 0)
            [(0 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([x^2 - y^2, y^2])
            sage: f.orbit(0,2)
            [(0 : 1), (-1 : 1), (0 : 1)]
        """
    def resultant(self, normalize: bool = False):
        """
        Compute the resultant of the defining polynomials of
        this dynamical system.

        If ``normalize`` is ``True``, then first normalize the coordinate
        functions with :meth:`normalize_coordinates`.

        INPUT:

        - ``normalize`` -- boolean (default: ``False``)

        OUTPUT: an element of the base ring of this map

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, 6*y^2])
            sage: f.resultant()                                                         # needs sage.libs.pari
            36

        ::

            sage: R.<t> = PolynomialRing(GF(17))
            sage: P.<x,y> = ProjectiveSpace(R,1)
            sage: f = DynamicalSystem_projective([t*x^2 + t*y^2, 6*y^2])
            sage: f.resultant()                                                         # needs sage.libs.pari
            2*t^2

        ::

            sage: R.<t> = PolynomialRing(GF(17))
            sage: P.<x,y,z> = ProjectiveSpace(R,2)
            sage: f = DynamicalSystem_projective([t*x^2 + t*y^2, 6*y^2, 2*t*z^2])
            sage: f.resultant()
            13*t^8

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: F = DynamicalSystem_projective([x^2 + y^2, 6*y^2, 10*x*z + z^2 + y^2])
            sage: F.resultant()
            1296

        ::

            sage: # needs sage.rings.number_field
            sage: R.<t> = PolynomialRing(QQ)
            sage: s = (t^3 + t + 1).roots(QQbar)[0][0]
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([s*x^3 - 13*y^3, y^3 - 15*y^3])
            sage: f.resultant()
            871.6925062959149?
        """
    @cached_method
    def primes_of_bad_reduction(self, check: bool = True):
        """
        Determine the primes of bad reduction for this dynamical system.

        Must be defined over a number field.

        If ``check`` is ``True``, each prime is verified to be of
        bad reduction.

        ALGORITHM:

        `p` is a prime of bad reduction if and only if the defining
        polynomials of ``self`` have a common zero. Or stated another way,
        `p` is a prime of bad reduction if and only if the radical of
        the ideal defined by the defining polynomials of ``self`` is not
        `(x_0,x_1,\\ldots,x_N)`.  This happens if and only if some
        power of each `x_i` is not in the ideal defined by the
        defining polynomials of ``self``. This last condition is what is
        checked. The lcm of the coefficients of the monomials `x_i` in
        a Groebner basis is computed. This may return extra primes.

        INPUT:

        - ``check`` -- boolean (default: ``True``)

        OUTPUT: list of primes

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([1/3*x^2 + 1/2*y^2, y^2])
            sage: f.primes_of_bad_reduction()                                           # needs sage.rings.function_field
            [2, 3]

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ,3)
            sage: f = DynamicalSystem_projective([12*x*z - 7*y^2, 31*x^2 - y^2,
            ....:                                 26*z^2, 3*w^2 - z*w])
            sage: f.primes_of_bad_reduction()                                           # needs sage.rings.function_field
            [2, 3, 7, 13, 31]

        A number field example::

            sage: # needs sage.rings.number_field
            sage: R.<z> = QQ[]
            sage: K.<a> = NumberField(z^2 - 2)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([1/3*x^2+1/a*y^2, y^2])
            sage: f.primes_of_bad_reduction()                                           # needs sage.rings.function_field
            [Fractional ideal (-a), Fractional ideal (3)]

        This is an example where ``check=False`` returns extra primes::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: f = DynamicalSystem_projective([3*x*y^2 + 7*y^3 - 4*y^2*z + 5*z^3,
            ....:                                 -5*x^3 + x^2*y + y^3 + 2*x^2*z,
            ....:                                 -2*x^2*y + x*y^2 + y^3 - 4*y^2*z + x*z^2])
            sage: f.primes_of_bad_reduction(False)                                      # needs sage.rings.function_field
            [2, 5, 37, 2239, 304432717]
            sage: f.primes_of_bad_reduction()                                           # needs sage.rings.function_field
            [5, 37, 2239, 304432717]
        """
    def conjugate(self, M, adjugate: bool = False, normalize: bool = False):
        """
        Conjugate this dynamical system by ``M``, i.e. `M^{-1} \\circ f \\circ M`.

        If possible the new map will be defined over the same space.
        Otherwise, will try to coerce to the base ring of ``M``.

        INPUT:

        - ``M`` -- a square invertible matrix

        - ``adjugate`` -- boolean (default: ``False``); also classically called
          adjoint, takes a square matrix ``M`` and finds the transpose of its
          cofactor matrix. Used for conjugation in place of inverse when
          specified ``True``. Functionality is the same in projective space.

        - ``normalize`` -- boolean (default: ``False``); if ``normalize`` is
          ``True``, then the method ``normalize_coordinates`` is called

        OUTPUT: a dynamical system

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.conjugate(matrix([[1,2], [0,1]]))
            Dynamical System of Projective Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 + 4*x*y + 3*y^2 : y^2)

        ::

            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<i> = NumberField(x^2 + 1)                                          # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^3 + y^3, y^3])
            sage: f.conjugate(matrix([[i,0], [0,-i]]))                                  # needs sage.rings.number_field
            Dynamical System of Projective Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (x : y) to
                    (-x^3 + y^3 : -y^3)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2, y*z])
            sage: f.conjugate(matrix([[1,2,3], [0,1,2], [0,0,1]]))
            Dynamical System of Projective Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^2 + 4*x*y + 3*y^2 + 6*x*z + 9*y*z + 7*z^2 : y^2 + 2*y*z : y*z + 2*z^2)

        ::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2+y^2, y^2])
            sage: f.conjugate(matrix([[2,0], [0,1/2]]))
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (2*x^2 + 1/8*y^2 : 1/2*y^2)

        ::

            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<i> = NumberField(x^2 + 1)                                          # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([1/3*x^2 + 1/2*y^2, y^2])
            sage: f.conjugate(matrix([[i,0], [0,-i]]))                                  # needs sage.rings.number_field
            Dynamical System of Projective Space of dimension 1
             over Number Field in i with defining polynomial x^2 + 1
              Defn: Defined on coordinates by sending (x : y) to
                    ((1/3*i)*x^2 + (1/2*i)*y^2 : (-i)*y^2)

        TESTS::

            sage: R = ZZ
            sage: P.<x,y> = ProjectiveSpace(R,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: m = matrix(R, 2, [4, 3, 2, 1])
            sage: f.conjugate(m, normalize=False)
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (-4*x^2 - 8*x*y - 7/2*y^2 : 12*x^2 + 20*x*y + 8*y^2)
            sage: f.conjugate(m, adjugate=True)
            Dynamical System of Projective Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (x : y) to
                    (8*x^2 + 16*x*y + 7*y^2 : -24*x^2 - 40*x*y - 16*y^2)

        .. TODO::

            Use the left and right action functionality to replace the code below with
            #return DynamicalSystem_projective(M.inverse()*self*M, domain=self.codomain())
            once there is a function to pass to the smallest field of definition.
        """
    def green_function(self, P, v, **kwds):
        """
        Evaluate the local Green's function at the place ``v`` for ``P``
        with ``N`` terms of the series or to within a given error bound.

        Must be over a number field or order of a number field. Note that
        this is the absolute local Green's function so is scaled by the
        degree of the base field.

        Use ``v=0`` for the archimedean place over `\\QQ` or field embedding.
        Non-archimedean places are prime ideals for number fields or primes
        over `\\QQ`.

        ALGORITHM:

        See Exercise 5.29 and Figure 5.6 of [Sil2007]_.

        INPUT:

        - ``P`` -- a projective point

        - ``v`` -- nonnegative integer; a place, use ``0`` for the
          archimedean place

        kwds:

        - ``N`` -- (default: 10) positive integer; number of
          terms of the series to use

        - ``prec`` -- (default: 100) positive integer, float point or
          `p`-adic precision

        - ``error_bound`` -- (optional) a positive real number

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y]);
            sage: Q = P(5, 1)
            sage: f.green_function(Q, 0, N=30)
            1.6460930159932946233759277576

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y]);
            sage: Q = P(5, 1)
            sage: f.green_function(Q, 0, N=200, prec=200)
            1.6460930160038721802875250367738355497198064992657997569827

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(3)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([17*x^2 + 1/7*y^2, 17*w*x*y])
            sage: f.green_function(P.point([w, 2], False), K.places()[1])
            1.7236334013785676107373093775
            sage: f.green_function(P([2, 1]), K.ideal(7), N=7)
            0.48647753726382832627633818586
            sage: f.green_function(P([w, 1]), K.ideal(17), error_bound=0.001)
            -0.70821687320448199545278619351

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: f.green_function(P.point([5,2], False), 0, N=30)
            1.7315451844777407992085512000
            sage: f.green_function(P.point([2,1], False), 0, N=30)
            0.86577259223181088325226209926
            sage: f.green_function(P.point([1,1], False), 0, N=30)
            0.43288629610862338612700146098
        """
    def canonical_height(self, P, **kwds):
        """
        Evaluate the (absolute) canonical height of ``P`` with respect to
        this dynamical system.

        Must be over number field or order of a number field. Specify
        either the number of terms of the series to evaluate or the
        error bound required.

        ALGORITHM:

        The sum of the Green's function at the archimedean places and
        the places of bad reduction.

        If function is defined over `\\QQ` uses Wells' Algorithm, which
        allows us to not have to factor the resultant.

        INPUT:

        - ``P`` -- a projective point

        kwds:

        - ``badprimes`` -- (optional) a list of primes of bad reduction

        - ``N`` -- (default: 10) positive integer; number of
          terms of the series to use in the local green functions

        - ``prec`` -- (default: 100) positive integer, float point or
          `p`-adic precision

        - ``error_bound`` -- (optional) a positive real number

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, 2*x*y]);
            sage: f.canonical_height(P.point([5,4]), error_bound=0.001)                 # needs sage.libs.pari
            2.1970553519503404898926835324
            sage: f.canonical_height(P.point([2,1]), error_bound=0.001)                 # needs sage.libs.pari
            1.0984430632822307984974382955

        Notice that preperiodic points may not return exactly 0::

            sage: # needs sage.rings.number_field
            sage: R.<X> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(X^2 + X - 1)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: Q = P.point([a,1])
            sage: f.canonical_height(Q, error_bound=0.000001)  # Answer only within error_bound of 0
            5.7364919788790160119266380480e-8
            sage: f.nth_iterate(Q, 2) == Q  # but it is indeed preperiodic
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: X = P.subscheme(x^2 - y^2);
            sage: f = DynamicalSystem_projective([x^2, y^2, 4*z^2], domain=X);
            sage: Q = X([4,4,1])
            sage: f.canonical_height(Q, badprimes=[2])                                  # needs sage.rings.function_field
            0.0013538030870311431824555314882

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: X = P.subscheme(x^2 - y^2);
            sage: f = DynamicalSystem_projective([x^2, y^2, 30*z^2], domain=X)
            sage: Q = X([4, 4, 1])
            sage: f.canonical_height(Q, badprimes=[2,3,5], prec=200)                    # needs sage.rings.function_field
            2.7054056208276961889784303469356774912979228770208655455481

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([1000*x^2 - 29*y^2, 1000*y^2])
            sage: Q = P(-1/4, 1)
            sage: f.canonical_height(Q, error_bound=0.01)                               # needs sage.libs.pari
            3.7979215342343045582800170705

        ::

            sage: RSA768 = Integer('123018668453011775513049495838496272077285356959533479219732245215'
            ....: '1726400507263657518745202199786469389956474942774063845925192557326303453731548'
            ....: '2685079170261221429134616704292143116022212404792747377940806653514195974598569'
            ....: '02143413')
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([RSA768*x^2 + y^2, x*y])
            sage: Q = P(RSA768,1)
            sage: f.canonical_height(Q, error_bound=0.00000000000000001)                # needs sage.libs.pari
            931.18256422718241278672729195

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([2*(-2*x^3 + 3*(x^2*y)) + 3*y^3, 3*y^3])
            sage: f.canonical_height(P(1,0))                                            # needs sage.libs.pari
            0.00000000000000000000000000000
        """
    def height_difference_bound(self, prec=None):
        """
        Return an upper bound on the different between the canonical
        height of a point with respect to this dynamical system and the
        absolute height of the point.

        This map must be a morphism.

        ALGORITHM:

        Uses a Nullstellensatz argument to compute the constant.
        For details: see [Hutz2015]_.

        INPUT:

        - ``prec`` -- (default: :class:`RealField` default)
          positive integer, float point precision

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: f.height_difference_bound()                                           # needs sage.symbolic
            1.38629436111989

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: f = DynamicalSystem_projective([4*x^2 + 100*y^2, 210*x*y, 10000*z^2])
            sage: f.height_difference_bound()                                           # needs sage.symbolic
            10.3089526606443

        A number field example::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<c> = NumberField(x^3 - 2)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([1/(c+1)*x^2 + c*y^2, 210*x*y, 10000*z^2])
            sage: f.height_difference_bound()                                           # needs sage.symbolic
            11.3683039374269

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
            sage: f = DynamicalSystem_projective([x^2, QQbar(sqrt(-1))*y^2,
            ....:                                 QQbar(sqrt(3))*z^2])
            sage: f.height_difference_bound()
            2.89037175789616

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([5*x^2 + 3*x*y , y^2 + 3*x^2])
            sage: f.height_difference_bound(prec=100)                                   # needs sage.symbolic
            5.3375380797013179737224159274
        """
    def multiplier(self, P, n, check: bool = True):
        """
        Return the multiplier of the point ``P`` of period ``n`` with
        respect to this dynamical system.

        INPUT:

        - ``P`` -- a point on domain of this map

        - ``n`` -- positive integer, the period of ``P``

        - ``check`` -- boolean (default: ``True``); verify that ``P``
          has period ``n``

        OUTPUT:

        A square matrix of size ``self.codomain().dimension_relative()``
        in the ``base_ring`` of this dynamical system.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([x^2, y^2, 4*z^2])
            sage: Q = P.point([4,4,1], False)
            sage: f.multiplier(Q,1)
            [2 0]
            [0 2]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([7*x^2 - 28*y^2, 24*x*y])
            sage: f.multiplier(P(2,5), 4)
            [231361/20736]

        ::

            sage: P.<x,y> = ProjectiveSpace(CC,1)
            sage: f = DynamicalSystem_projective([x^3 - 25*x*y^2 + 12*y^3, 12*y^3])
            sage: f.multiplier(P(1,1), 5)  # abs tol 1e-14
            [0.389017489711934]

        ::

            sage: P.<x,y> = ProjectiveSpace(RR,1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: f.multiplier(P(2,1), 1)
            [4.00000000000000]

        ::

            sage: P.<x,y> = ProjectiveSpace(Qp(13),1)                                   # needs sage.rings.padics
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2])
            sage: f.multiplier(P(5,4), 3)                                               # needs sage.rings.padics
            [6 + 8*13 + 13^2 + 8*13^3 + 13^4 + 8*13^5 + 13^6 + 8*13^7 + 13^8 +
             8*13^9 + 13^10 + 8*13^11 + 13^12 + 8*13^13 + 13^14 + 8*13^15 + 13^16 +
             8*13^17 + 13^18 + 8*13^19 + O(13^20)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.multiplier(P(0,1), 1)
            Traceback (most recent call last):
            ...
            ValueError: (0 : 1) is not periodic of period 1
        """
    def nth_preimage_tree(self, Q, n, **kwds):
        """
        Return the ``n``-th pre-image tree rooted at ``Q``.

        This map must be an endomorphism of the projective line defined
        over a number field, algebraic field, or finite field.

        INPUT:

        - ``Q`` -- a point in the domain of this map

        - ``n`` -- positive integer, the depth of the pre-image tree

        kwds:

        - ``return_points`` -- boolean (default: ``False``); if ``True``,
          return a list of lists where the index `i` is the level of the tree
          and the elements of the list at that index are the `i`-th preimage
          points as an algebraic element of the splitting field of the
          polynomial `f^n - Q = 0`.

        - ``numerical`` -- boolean (default: ``False``); calculate pre-images
          numerically. Note if this is set to ``True``, preimage points are
          displayed as complex numbers.

        - ``prec`` -- (default: 100) positive integer; the precision of the
          ``ComplexField`` if we compute the preimage points numerically

        - ``display_labels`` -- boolean (default: ``True``); whether to display
          vertex labels. Since labels can be very cluttered, can set
          ``display_labels`` to ``False`` and use ``return_points`` to get a
          hold of the points themselves, either as algebraic or complex numbers.

        - ``display_complex`` -- boolean (default: ``False``); display vertex
          labels as complex numbers. Note if this option is chosen that we must
          choose an embedding from the splitting field ``field_def`` of the
          `n`-th-preimage equation into `\\CC`. We make the choice of the first
          embedding returned by ``field_def.embeddings(ComplexField())``.

        - ``digits`` -- positive integer; the number of decimal digits to
          display for complex numbers. This only applies if ``display_complex``
          is set to ``True``.

        OUTPUT:

        If ``return_points`` is ``False``, a :class:`GraphPlot` object representing
        the `n`-th pre-image tree.  If ``return_points`` is ``True``, a tuple
        ``(GP, points)``, where ``GP`` is a :class:`GraphPlot` object, and
        ``points`` is a list of lists as described above under
        ``return_points``.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: Q = P(0,1)
            sage: f.nth_preimage_tree(Q, 2)                                             # needs sage.plot
            GraphPlot object for Digraph on 7 vertices

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(3), 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y + y^2, y^2])
            sage: Q = P(0,1)
            sage: f.nth_preimage_tree(Q, 2, return_points=True)                         # needs sage.plot
            (GraphPlot object for Digraph on 4 vertices,
             [[(0 : 1)], [(1 : 1)], [(0 : 1), (2 : 1)]])
        """
    def possible_periods(self, **kwds):
        """
        Return the set of possible periods for rational periodic points of
        this dynamical system.

        Must be defined over `\\ZZ` or `\\QQ`.

        ALGORITHM:

        Calls ``self.possible_periods()`` modulo all primes of good reduction
        in range ``prime_bound``. Return the intersection of those lists.

        INPUT: keyword arguments:

        - ``prime_bound`` -- (default: ``[1, 20]``) a list or tuple of
          two positive integers or an integer for the upper bound

        - ``bad_primes`` -- (optional) a list or tuple of integer primes,
          the primes of bad reduction

        - ``ncpus`` -- (default: all cpus) number of cpus to use in parallel

        OUTPUT: list of positive integers

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2])
            sage: f.possible_periods(ncpus=1)                                           # needs sage.rings.function_field
            [1, 3]

        ::

            sage: PS.<x,y> = ProjectiveSpace(1,QQ)
            sage: f = DynamicalSystem_projective([5*x^3 - 53*x*y^2 + 24*y^3, 24*y^3])
            sage: f.possible_periods(prime_bound=[1,5])                                 # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: no primes of good reduction in that range
            sage: f.possible_periods(prime_bound=[1,10])                                # needs sage.rings.function_field
            [1, 4, 12]
            sage: f.possible_periods(prime_bound=[1,20])                                # needs sage.rings.function_field
            [1, 4]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: f = DynamicalSystem_projective([2*x^3 - 50*x*z^2 + 24*z^3,
            ....:                                 5*y^3 - 53*y*z^2 + 24*z^3, 24*z^3])
            sage: f.possible_periods(prime_bound=10)                                    # needs sage.rings.function_field
            [1, 2, 6, 20, 42, 60, 140, 420]
            sage: f.possible_periods(prime_bound=20) # long time
            [1, 20]
        """
    def is_PGL_minimal(self, prime_list=None):
        """
        Check if this dynamical system is a minimal model in
        its conjugacy class.

        See [BM2012]_ and [Mol2015]_ for a description of the algorithm.
        For polynomial maps it uses [HS2018]_.

        INPUT:

        - ``prime_list`` -- (optional) list of primes to check minimality

        OUTPUT: boolean

        EXAMPLES::

            sage: PS.<X,Y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([X^2 + 3*Y^2, X*Y])
            sage: f.is_PGL_minimal()                                                    # needs sage.rings.function_field
            True

        ::

            sage: PS.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([6*x^2 + 12*x*y + 7*y^2, 12*x*y])
            sage: f.is_PGL_minimal()                                                    # needs sage.rings.function_field
            False

        ::

            sage: PS.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([6*x^2 + 12*x*y + 7*y^2, y^2])
            sage: f.is_PGL_minimal()                                                    # needs sage.rings.function_field
            False
        """
    def minimal_model(self, return_transformation: bool = False, prime_list=None, algorithm=None, check_primes: bool = True):
        """
        Determine if this dynamical system is minimal.

        This dynamical system must be defined over the projective line
        over the rationals. In particular, determine if this map is affine
        minimal, which is enough to decide if it is minimal or not.
        See Proposition 2.10 in [BM2012]_.

        INPUT:

        - ``return_transformation`` -- boolean (default: ``False``); this
          signals a return of the `PGL_2` transformation to conjugate
          this map to the calculated minimal model

        - ``prime_list`` -- (optional) a list of primes, in case one
          only wants to determine minimality at those specific primes

        - ``algorithm`` -- (optional) string; can be one of the following:

        - ``check_primes`` -- (optional) boolean; this signals whether to
            check whether each element in ``prime_list`` is a prime

          * ``'BM'`` -- the Bruin-Molnar algorithm [BM2012]_
          * ``'HS'`` -- the Hutz-Stoll algorithm [HS2018]_

        OUTPUT:

        - a dynamical system on the projective line which is a minimal model
          of this map

        - a `PGL(2,\\QQ)` element which conjugates this map to a minimal model

        EXAMPLES::

            sage: PS.<X,Y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([X^2 + 3*Y^2, X*Y])
            sage: f.minimal_model(return_transformation=True)                           # needs sage.rings.function_field
            (
            Dynamical System of Projective Space of dimension 1 over Rational
            Field
              Defn: Defined on coordinates by sending (X : Y) to
                    (X^2 + 3*Y^2 : X*Y)
            ,
            [1 0]
            [0 1]
            )

        ::

            sage: PS.<X,Y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([7365/2*X^4 + 6282*X^3*Y + 4023*X^2*Y^2
            ....:                                   + 1146*X*Y^3 + 245/2*Y^4,
            ....:                                 -12329/2*X^4 - 10506*X^3*Y - 6723*X^2*Y^2
            ....:                                   - 1914*X*Y^3 - 409/2*Y^4])
            sage: f.minimal_model(return_transformation=True)                           # needs sage.rings.function_field
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (X : Y) to
                    (9847*X^4 + 28088*X^3*Y + 30048*X^2*Y^2 + 14288*X*Y^3 + 2548*Y^4
                    : -12329*X^4 - 35164*X^3*Y - 37614*X^2*Y^2 - 17884*X*Y^3 - 3189*Y^4),
            <BLANKLINE>
            [2 1]
            [0 1]
            )

        ::

            sage: PS.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([6*x^2 + 12*x*y + 7*y^2, 12*x*y])
            sage: f.minimal_model()                                                     # needs sage.rings.function_field
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 + 12*x*y + 42*y^2 : 2*x*y)

        ::

            sage: PS.<x,y> = ProjectiveSpace(ZZ,1)
            sage: f = DynamicalSystem_projective([6*x^2 + 12*x*y + 7*y^2, 12*x*y + 42*y^2])
            sage: g,M = f.minimal_model(return_transformation=True, algorithm='BM')     # needs sage.rings.function_field
            sage: f.conjugate(M) == g                                                   # needs sage.rings.function_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([2*x^2, y^2])
            sage: f.minimal_model(return_transformation=True)                           # needs sage.rings.function_field
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 : y^2)                                                    ,
            [1 0]
            [0 2]
            )
            sage: f.minimal_model(prime_list=[3])                                       # needs sage.rings.function_field
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (2*x^2 : y^2)

        TESTS::

            sage: PS.<X,Y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([X + Y, X - 3*Y])
            sage: f.minimal_model()                                                     # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: minimality is only for degree 2 or higher

        ::

            sage: PS.<X,Y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([X^2 - Y^2, X^2 + X*Y])
            sage: f.minimal_model()                                                     # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            TypeError: the function is not a morphism

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([2*x^2, y^2])
            sage: f.minimal_model(algorithm='BM')                                       # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            TypeError: affine minimality is only considered for
            maps not of the form f or 1/f for a polynomial f

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem([2*x^2, y^2])
            sage: f.minimal_model(prime_list=[0])                                       # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: prime_list contains 0 which is not prime

        REFERENCES:

        - [BM2012]_
        - [Mol2015]_
        - [HS2018]_
        """
    def all_minimal_models(self, return_transformation: bool = False, prime_list=None, algorithm=None, check_minimal: bool = True):
        """
        Determine a representative in each `SL(2,\\ZZ)`-orbit of this map.

        This can be done either with the Bruin-Molnar algorithm or the
        Hutz-Stoll algorithm. The Hutz-Stoll algorithm requires the map
        to have minimal resultant and then finds representatives in orbits
        with minimal resultant. The Bruin-Molnar algorithm finds
        representatives with the same resultant (up to sign) of the given map.

        Bruin-Molnar does not work for polynomials and is more efficient
        for large primes.

        INPUT:

        - ``return_transformation`` -- boolean (default: ``False``); this
          signals a return of the `PGL_2` transformation to conjugate
          this map to the calculated models

        - ``prime_list`` -- (optional) a list of primes, in case one
          only wants to determine minimality at those specific primes

        - ``algorithm`` -- (optional) string; can be one of the following:

          * ``'BM'`` -- the Bruin-Molnar algorithm [BM2012]_
          * ``'HS'`` -- for the Hutz-Stoll algorithm [HS2018]_

          if not specified, properties of the map are utilized to choose

        - ``check_minimal`` -- (optional) boolean; to first check if the map
          is minimal and if not, compute a minimal model before computing
          for orbit representatives

        OUTPUT:

        A list of pairs `(F,m)`, where `F` is dynamical system on the
        projective line and `m` is the associated `PGL(2,\\QQ)` element.
        Or just a list of dynamical systems if not returning the conjugation.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([2*x^2, 3*y^2])
            sage: f.all_minimal_models()                                                # needs sage.rings.function_field
            [Dynamical System of Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y) to
                     (x^2 : y^2)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: c = 2*3^6
            sage: f = DynamicalSystem([x^3 - c^2*y^3, x*y^2])
            sage: len(f.all_minimal_models(algorithm='HS'))                             # needs sage.rings.function_field
            14
            sage: len(f.all_minimal_models(prime_list=[2], algorithm='HS'))             # needs sage.rings.function_field
            2

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([237568*x^3 + 1204224*x^2*y + 2032560*x*y^2
            ....:     + 1142289*y^3, -131072*x^3 - 663552*x^2*y - 1118464*x*y^2
            ....:     - 627664*y^3])
            sage: len(f.all_minimal_models(algorithm='BM'))                             # needs sage.rings.function_field
            2

        TESTS::

            sage: # needs sage.rings.function_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: c = 2^2*5^2*11^3
            sage: f = DynamicalSystem([x^3 - c^2*y^3, x*y^2])
            sage: MM = f.all_minimal_models(return_transformation=True, algorithm='BM')
            sage: all(f.conjugate(m) == F for F, m in MM)
            True
            sage: MM = f.all_minimal_models(return_transformation=True, algorithm='HS')
            sage: all(f.conjugate(m) == F for F,m in MM)
            True

        REFERENCES:

        - [BM2012]_
        - [HS2018]_
        """
    def affine_preperiodic_model(self, m, n, return_conjugation: bool = False):
        """
        Return a dynamical system conjugate to this one with affine (n, m) preperiodic points.

        If the base ring of this dynamical system is finite, there may
        not be a model with affine preperiodic points, in which case a
        :exc:`ValueError` is raised.

        INPUT:

        - ``m`` -- the preperiod of the preperiodic points to make affine

        - ``n`` -- the period of the preperiodic points to make affine

        - ``return_conjugation`` -- boolean (default: ``False``); if ``True``, return a tuple
          ``(g, phi)`` where ``g`` is a model with affine (n, m) preperiodic points
          and ``phi`` is the matrix that moves ``f`` to ``g``.

        OUTPUT: a dynamical system conjugate to this one

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])
            sage: g = f.affine_preperiodic_model(0, 1); g                               # needs sage.rings.function_field
            Dynamical System of Projective Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-x^2 : -2*x^2 + 2*x*y - y^2 : 2*x^2 - 2*x*y + 2*y^2 + 2*y*z + z^2)

        We can check that ``g`` has affine fixed points::

            sage: g.periodic_points(1)                                                  # needs sage.rings.function_field
            [(-1 : -1 : 1),
             (-1/2 : -1 : 1),
             (-1/2 : -1/2 : 1),
             (-1/3 : -2/3 : 1),
             (0 : -1 : 1),
             (0 : -1/2 : 1),
             (0 : 0 : 1)]

        ::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(9), 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])
            sage: f.affine_preperiodic_model(0, 1)                                      # needs sage.rings.function_field
            Dynamical System of Projective Space of dimension 2
             over Finite Field in z2 of size 3^2
              Defn: Defined on coordinates by sending (x : y : z) to
                    ((-z2)*x^2 : z2*x^2 + (-z2)*x*y + (-z2)*y^2 :
                     (-z2)*x^2 + z2*x*y + (z2 + 1)*y^2 - y*z + z^2)

        ::

            sage: R.<c> = GF(3)[]
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])
            sage: f.affine_preperiodic_model(0, 1)  # long time
            Dynamical System of Projective Space of dimension 2 over
             Univariate Polynomial Ring in c over Finite Field of size 3
              Defn: Defined on coordinates by sending (x : y : z) to
                    (2*c^3*x^2 : c^3*x^2 + 2*c^3*x*y + 2*c^3*y^2 :
                     2*c^3*x^2 + c^3*x*y + (c^3 + c^2)*y^2 + 2*c^2*y*z + c^2*z^2)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<k> = CyclotomicField(3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([x^2 + k*x*y + y^2, z^2, y^2])
            sage: f.affine_preperiodic_model(1, 1)                                      # needs sage.rings.function_field
            Dynamical System of Projective Space of dimension 2
             over Cyclotomic Field of order 3 and degree 2
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-y^2 : x^2 : x^2 + (-k)*x*z + z^2)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: g, mat = f.affine_preperiodic_model(0, 1, return_conjugation=True)    # needs sage.rings.function_field
            sage: g == f.conjugate(mat)                                                 # needs sage.rings.function_field
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(2*y - z)
            sage: f = DynamicalSystem_projective([x^2 + y^2, z^2 + y^2, z^2], domain=X)
            sage: f.affine_preperiodic_model(0, 1)                                      # needs sage.rings.function_field
            Dynamical System of Closed subscheme of Projective Space of dimension 2
             over Rational Field defined by: 2*y - z
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-x^2 - y^2 : y^2 : x^2 + z^2)

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 2*y^2, x^2])
            sage: g, mat = f.affine_preperiodic_model(0, 1, return_conjugation=True)    # needs sage.rings.function_field
            sage: f.conjugate(mat) == g                                                 # needs sage.rings.function_field
            True
        """
    def automorphism_group(self, **kwds):
        """
        Calculate the subgroup of `PGL2` that is the automorphism group
        of this dynamical system.

        The automorphism group is the set of `PGL(2)` elements that fixes
        this map under conjugation.

        INPUT:

        The following keywords are used in most cases:

        - ``num_cpus`` -- (default: 2) the number of threads to use. Setting to a
          larger number can greatly speed up this function

        The following keywords are used only when the dimension of the domain is 1 and
        the base ring is the rationals, but ignored in all other cases:

        - ``starting_prime`` -- (default: 5) the first prime to use for CRT

        - ``algorithm`` -- (optional) can be one of the following:

          * ``'CRT'`` -- Chinese Remainder Theorem
          * ``'fixed_points'`` -- fixed points algorithm

        - ``return_functions`` -- boolean (default: ``False``); ``True``
          returns elements as linear fractional transformations and
          ``False`` returns elements as `PGL2` matrices

        - ``iso_type`` -- boolean (default: ``False``); ``True`` returns the
          isomorphism type of the automorphism group

        OUTPUT: list of elements in the automorphism group

        AUTHORS:

        - Original algorithm written by Xander Faber, Michelle Manes,
          Bianca Viray

        - Modified by Joao Alberto de Faria, Ben Hutz, Bianca Thompson

        REFERENCES:

        - [FMV2014]_

        EXAMPLES::

            sage: R.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, x*y])
            sage: f.automorphism_group(return_functions=True)                           # needs sage.libs.pari
            [x, -x]

        ::

            sage: R.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 5*x*y + 5*y^2, 5*x^2 + 5*x*y + y^2])
            sage: f.automorphism_group()                                                # needs sage.libs.pari
            [
            [1 0]  [0 2]
            [0 1], [2 0]
            ]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem([x^3, y^3, z^3])
            sage: len(f.automorphism_group())                                           # needs sage.rings.function_field
            24

        ::

            sage: R.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 2*x*y - 2*y^2, -2*x^2 - 2*x*y + y^2])
            sage: f.automorphism_group(return_functions=True)                           # needs sage.libs.pari
            [x, 1/x, -x - 1, -x/(x + 1), (-x - 1)/x, -1/(x + 1)]

        ::

            sage: R.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([3*x^2*y - y^3, x^3 - 3*x*y^2])
            sage: lst, label = f.automorphism_group(algorithm='CRT',                    # needs sage.libs.pari
            ....:                                   return_functions=True,
            ....:                                   iso_type=True)
            sage: sorted(lst), label                                                    # needs sage.libs.pari
            ([-1/x, 1/x, (-x - 1)/(x - 1), (-x + 1)/(x + 1), (x - 1)/(x + 1),
              (x + 1)/(x - 1), -x, x],
             'Dihedral of order 8')

        ::

            sage: A.<z> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem_affine([1/z^3])
            sage: F = f.homogenize(1)
            sage: F.automorphism_group()                                                # needs sage.libs.pari
            [
            [1 0]  [0 2]  [-1  0]  [ 0 -2]
            [0 1], [2 0], [ 0  1], [ 2  0]
            ]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x**2 + x*z, y**2, z**2])
            sage: f.automorphism_group()                                                # needs sage.rings.function_field
            [
            [1 0 0]
            [0 1 0]
            [0 0 1]
            ]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = CyclotomicField(3)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: D6 = DynamicalSystem_projective([y^2, x^2])
            sage: sorted(D6.automorphism_group())
            [
            [-w - 1      0]  [     0 -w - 1]  [w 0]  [0 w]  [0 1]  [1 0]
            [     0      1], [     1      0], [0 1], [1 0], [1 0], [0 1]
            ]
        """
    def critical_subscheme(self):
        """
        Return the critical subscheme of this dynamical system.

        OUTPUT: projective subscheme

        EXAMPLES::

            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 - 2*x*y^2 + 2*y^3, y^3])
            sage: f.critical_subscheme()                                                # needs sage.rings.function_field
            Closed subscheme of Projective Space of dimension 1 over Rational Field
            defined by:
              9*x^2*y^2 - 6*y^4

        ::

            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([2*x^2 - y^2, x*y])
            sage: f.critical_subscheme()                                                # needs sage.rings.function_field
            Closed subscheme of Projective Space of dimension 1 over Rational Field
            defined by:
              4*x^2 + 2*y^2

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([2*x^2 - y^2, x*y, z^2])
            sage: f.critical_subscheme()                                                # needs sage.rings.function_field
            Closed subscheme of Projective Space of dimension 2 over Rational Field
            defined by:
              8*x^2*z + 4*y^2*z

        ::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z,w> = ProjectiveSpace(GF(81), 3)
            sage: g = DynamicalSystem_projective([x^3 + y^3, y^3 + z^3, z^3 + x^3, w^3])
            sage: g.critical_subscheme()
            Closed subscheme of Projective Space of dimension 3 over Finite Field in
            z4 of size 3^4 defined by:
              0

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2, x*y])
            sage: f.critical_subscheme()                                                # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            TypeError: the function is not a morphism
        """
    def critical_points(self, R=None):
        """
        Return the critical points of this dynamical system defined over
        the ring `R` or the base ring of this map.

        Must be dimension 1.

        INPUT:

        - ``R`` -- (optional) a ring

        OUTPUT: list of projective space points defined over `R`

        EXAMPLES::

            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 - 2*x*y^2 + 2*y^3, y^3])
            sage: f.critical_points()                                                   # needs sage.rings.function_field
            [(1 : 0)]
            sage: K.<w> = QuadraticField(6)                                             # needs sage.rings.number_field
            sage: f.critical_points(K)                                                  # needs sage.rings.number_field
            [(-1/3*w : 1), (1/3*w : 1), (1 : 0)]

        ::

            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([2*x^2 - y^2, x*y])
            sage: f.critical_points(QQbar)                                              # needs sage.rings.number_field
            [(-0.7071067811865475?*I : 1), (0.7071067811865475?*I : 1)]
        """
    def ramification_type(self, R=None, stable: bool = True):
        """
        Return the ramification type of endomorphisms of `\\mathbb{P}^1`.

        Only branch points defined over the ring ``R`` contribute to
        the ramification type if specified, otherwise ``R`` is the
        ring of definition for ``self``.

        Note that branch points defined over ``R`` may not be
        geometric points if stable not set to ``True``.

        If ``R`` is specified, ``stable`` is ignored.

        If ``stable``, then this will return the ramification type
        over an extension which splits the Galois orbits of critical
        points.

        INPUT:

        - ``R`` -- ring or morphism (optional)
        - ``split`` -- boolean (optional)

        OUTPUT:

        list of lists, each term being the list of ramification indices
        in the pre-images of one critical value

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^4, y^4])
            sage: F.ramification_type()                                                 # needs sage.rings.number_field
            [[4], [4]]

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^3, 4*y^3 - 3*x^2*y])
            sage: F.ramification_type()                                                 # needs sage.rings.number_field
            [[2], [2], [3]]

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([(x + y)^4, 16*x*y*(x-y)^2])
            sage: F.ramification_type()                                                 # needs sage.rings.number_field
            [[2], [2, 2], [4]]

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([(x + y)*(x - y)^3, y*(2*x+y)^3])
            sage: F.ramification_type()                                                 # needs sage.rings.number_field
            [[3], [3], [3]]

            sage: F = DynamicalSystem_projective([x^3 - 2*x*y^2 + 2*y^3, y^3])
            sage: F.ramification_type()                                                 # needs sage.rings.number_field
            [[2], [2], [3]]
            sage: F.ramification_type(R=F.base_ring())                                  # needs sage.rings.function_field
            [[2], [3]]
        """
    def is_postcritically_finite(self, err: float = 0.01, use_algebraic_closure: bool = True):
        """
        Determine if this dynamical system is post-critically finite.

        Only for endomorphisms of `\\mathbb{P}^1`. It checks if each critical
        point is preperiodic. The optional parameter ``err`` is passed into
        :meth:`is_preperiodic` as part of the preperiodic check.

        The computations can be done either over the algebraic closure of the
        base field or over the minimal extension of the base field that
        contains the critical points.

        INPUT:

        - ``err`` -- (default: 0.01) positive real number

        - ``use_algebraic_closure`` -- boolean (default: ``True``); if ``True``, uses the
          algebraic closure. If ``False``, uses the smallest extension of the base field
          containing all the critical points.

        OUTPUT: boolean

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.is_postcritically_finite()                                          # needs sage.rings.number_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 - y^3, y^3])
            sage: f.is_postcritically_finite()                                          # needs sage.rings.number_field
            False

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = QQ[]
            sage: K.<v> = NumberField(z^8 + 3*z^6 + 3*z^4 + z^2 + 1)
            sage: PS.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^3 + v*y^3, y^3])
            sage: f.is_postcritically_finite()  # long time
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([6*x^2 + 16*x*y + 16*y^2,
            ....:                                 -3*x^2 - 4*x*y - 4*y^2])
            sage: f.is_postcritically_finite()                                          # needs sage.rings.number_field
            True

        ::

            sage: # needs sage.libs.gap sage.rings.number_field
            sage: K = UniversalCyclotomicField()
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: F = DynamicalSystem_projective([x^2 - y^2, y^2], domain=P)
            sage: F.is_postcritically_finite()
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([8*x^4 - 8*x^2*y^2 + y^4, y^4])
            sage: f.is_postcritically_finite(use_algebraic_closure=False)  # long time
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^4 - x^2*y^2 + y^4, y^4])
            sage: f.is_postcritically_finite(use_algebraic_closure=False)               # needs sage.rings.number_field
            False

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar,1)
            sage: f = DynamicalSystem_projective([x^4 - x^2*y^2, y^4])
            sage: f.is_postcritically_finite()
            False
        """
    def is_dynamical_belyi_map(self):
        """
        Return if this dynamical system is a dynamical Belyi map.

        We define a dynamical Belyi map to be a map conjugate to a
        dynamical system `f: \\mathbb{P}^1  \\to \\mathbb{P}^1`
        where the branch points are contained in `\\{0, 1, \\infty \\}`
        and the postcritical set is contained in `\\{0, 1, \\infty \\}`.

        Output: Boolean

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([-2*x^3 - 9*x^2*y - 12*x*y^2 - 6*y^3, y^3])
            sage: f.is_dynamical_belyi_map()                                            # needs sage.rings.number_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([5*x^7 - 7*x^6*y, -7*x*y^6 + 5*y^7])
            sage: f.is_dynamical_belyi_map()                                            # needs sage.rings.number_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.is_dynamical_belyi_map()                                            # needs sage.rings.number_field
            False

        ::

            sage: # needs sage.rings.number_field
            sage: F = QuadraticField(-7)
            sage: P.<x,y> = ProjectiveSpace(F, 1)
            sage: f = DynamicalSystem_projective([5*x^7 - 7*x^6*y, -7*x*y^6 + 5*y^7])
            sage: f.is_dynamical_belyi_map()
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([2*x^3 + 3*x^2*y - 3*x*y^2 + 2*y^3,
            ....:                                 x^3 + y^3])
            sage: f.is_dynamical_belyi_map()                                            # needs sage.rings.number_field
            False

        ::

            sage: # needs sage.rings.number_field
            sage: R.<t> = PolynomialRing(QQ)
            sage: N.<c> = NumberField(t^3 - 2)
            sage: P.<x,y> = ProjectiveSpace(N, 1)
            sage: f=DynamicalSystem_projective([x^2 + c*y^2, x*y])
            sage: f.is_dynamical_belyi_map()
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(7), 1)
            sage: f = DynamicalSystem_projective([x^3 + 6*y^3, y^3])
            sage: f.is_dynamical_belyi_map()                                            # needs sage.libs.pari
            False
        """
    def critical_point_portrait(self, check: bool = True, use_algebraic_closure: bool = True):
        """
        If this dynamical system  is post-critically finite, return its
        critical point portrait.

        This is the directed graph of iterates starting with the critical
        points. Must be dimension 1. If ``check`` is ``True``, then the
        map is first checked to see if it is postcritically finite.

        The computations can be done either over the algebraic closure of the
        base field or over the minimal extension of the base field that
        contains the critical points.

        INPUT:

        - ``check`` -- boolean (default: ``True``)

        - ``use_algebraic_closure`` -- boolean (default: ``True``); if ``True``, uses the
          algebraic closure. If ``False``, uses the smallest extension of the base field
          containing all the critical points.

        OUTPUT: a digraph

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<z> = QQ[]
            sage: K.<v> = NumberField(z^6 + 2*z^5 + 2*z^4 + 2*z^3 + z^2 + 1)
            sage: PS.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 + v*y^2, y^2])
            sage: f.critical_point_portrait(check=False)        # long time             # needs sage.graphs
            Looped digraph on 6 vertices

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^5 + 5/4*x*y^4, y^5])
            sage: f.critical_point_portrait(check=False)                                # needs sage.graphs sage.rings.number_field
            Looped digraph on 5 vertices

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + 2*y^2, y^2])
            sage: f.critical_point_portrait()                                           # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: map must be post-critically finite

        ::

            sage: # needs sage.rings.number_field
            sage: R.<t> = QQ[]
            sage: K.<v> = NumberField(t^3 + 2*t^2 + t + 1)
            sage: phi = K.embeddings(QQbar)[0]
            sage: P.<x, y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^2 + v*y^2, y^2])
            sage: f.change_ring(phi).critical_point_portrait()                          # needs sage.graphs
            Looped digraph on 4 vertices

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([8*x^4 - 8*x^2*y^2 + y^4, y^4])
            sage: f.critical_point_portrait(use_algebraic_closure=False)  # long time
            Looped digraph on 6 vertices

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar,1)
            sage: f = DynamicalSystem_projective([8*x^4 - 8*x^2*y^2 + y^4, y^4])
            sage: f.critical_point_portrait()   # long time                             # needs sage.graphs
            Looped digraph on 6 vertices

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(3),1)
            sage: f = DynamicalSystem_projective([x^2 + x*y - y^2, x*y])
            sage: f.critical_point_portrait(use_algebraic_closure=False)                # needs sage.libs.pari
            Looped digraph on 6 vertices
            sage: f.critical_point_portrait() #long time
            Looped digraph on 6 vertices
        """
    def critical_height(self, **kwds):
        """
        Compute the critical height of this dynamical system.

        The critical height is defined by J. Silverman as
        the sum of the canonical heights of the critical points.
        This must be dimension 1 and defined over a number field
        or number field order.

        The computations can be done either over the algebraic closure of the
        base field or over the minimal extension of the base field that
        contains the critical points.

        INPUT: keyword arguments:

        - ``badprimes`` -- (optional) a list of primes of bad reduction

        - ``N`` -- (default: 10) positive integer; number of terms of
          the series to use in the local green functions

        - ``prec`` -- (default: 100) positive integer, float point
          or `p`-adic precision

        - ``error_bound`` -- (optional) a positive real number

        - ``use_algebraic_closure`` -- boolean (default: ``True``); if
          ``True``, uses the algebraic closure. If ``False``, uses the
          smallest extension of the base field containing all the critical
          points.

        OUTPUT: real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 + 7*y^3, 11*y^3])
            sage: f.critical_height()                                                   # needs sage.rings.number_field
            1.1989273321156851418802151128

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(2)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 + w*y^2, y^2])
            sage: f.critical_height()
            0.16090842452312941163719755472

        Postcritically finite maps have critical height 0::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 - 3/4*x*y^2 + 3/4*y^3, y^3])
            sage: f.critical_height(error_bound=0.0001)                                 # needs sage.rings.number_field
            0.00000000000000000000000000000

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^3 + 3*x*y^2, y^3])
            sage: f.critical_height(use_algebraic_closure=False)                        # needs sage.rings.number_field
            0.000023477016733897112886491967991
            sage: f.critical_height()                                                   # needs sage.rings.number_field
            0.000023477016733897112886491967991
        """
    def preperiodic_points(self, m, n, **kwds):
        """
        Compute the preperiodic points of period ``m, n`` of this dynamical system
        defined over the ring ``R`` or the base ring of the map.

        This is done by finding the rational points on the variety
        defining the points of period ``m, n``.

        For rational maps, where there are potentially infinitely many periodic
        points of a given period, you must use the ``return_scheme`` option.
        Note that this scheme will include the indeterminacy locus.

        INPUT:

        - ``n`` -- positive integer; the period

        - ``m`` -- nonnegative integer; the preperiod

        kwds:

        - ``minimal`` -- boolean (default: ``True``); ``True`` specifies to
          find only the preperiodic points of minimal period ``m``,``n`` and
          ``False`` specifies to find all preperiodic points of period
          ``m``, ``n``

        - ``formal`` -- boolean (default: ``False``); ``True`` specifies to
          find the formal periodic points only. The formal periodic points
          are the points in the support of the dynatomic cycle.

        - ``R`` -- (default: the base ring of the dynamical system) a
          commutative ring over which to find the preperiodic points

        - ``return_scheme`` -- boolean (default: ``False``); return a
          subscheme of the ambient space that defines the ``m``,``n`` th
          preperiodic points

        OUTPUT:

        A list of preperiodic points of this map or the subscheme defining
        the preperiodic points.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)                                   # needs sage.rings.number_field
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])                      # needs sage.rings.number_field
            sage: f.preperiodic_points(0, 1)                                            # needs sage.rings.number_field
            [(-0.618033988749895? : 1), (1 : 0), (1.618033988749895? : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2])
            sage: f.preperiodic_points(1, 3)                                            # needs sage.rings.function_field
            [(-5/4 : 1), (1/4 : 1), (7/4 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2 , z^2])
            sage: f.preperiodic_points(0, 2, formal=True)                               # needs sage.rings.function_field
            [(-1/2 : 1 : 0), (-1/2 : 1 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([x^2 - x*y + 2*y^2, x^2 - y^2])
            sage: f.preperiodic_points(1, 2, minimal=False)                             # needs sage.rings.function_field
            [(-3.133185666641252? : 1),
            (-1 : 1),
            (-0.3478103847799310? - 1.028852254136693?*I : 1),
            (-0.3478103847799310? + 1.028852254136693?*I : 1),
            (0.8165928333206258? - 0.6710067557437100?*I : 1),
            (0.8165928333206258? + 0.6710067557437100?*I : 1),
            (1 : 0),
            (1 : 1),
            (1.695620769559862? : 1),
            (3 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<w> = QQ[]
            sage: K.<s> = NumberField(w^6 - 3*w^5 + 5*w^4 - 5*w^3 + 5*w^2 - 3*w + 1)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([x^2 + z^2, y^2 + x^2, z^2 + y^2])
            sage: sorted(f.preperiodic_points(0, 1), key=str)                           # needs sage.rings.function_field
            [(-2*s^5 + 4*s^4 - 5*s^3 + 3*s^2 - 4*s : -2*s^5 + 5*s^4 - 7*s^3 + 6*s^2 - 7*s + 3 : 1),
             (-s^5 + 3*s^4 - 4*s^3 + 4*s^2 - 4*s + 2 : -s^5 + 2*s^4 - 2*s^3 + s^2 - s : 1),
             (-s^5 + 3*s^4 - 5*s^3 + 4*s^2 - 3*s + 1 : s^5 - 2*s^4 + 3*s^3 - 3*s^2 + 4*s - 1 : 1),
             (1 : 1 : 1),
             (2*s^5 - 6*s^4 + 9*s^3 - 8*s^2 + 7*s - 4 : 2*s^5 - 5*s^4 + 7*s^3 - 5*s^2 + 6*s - 2 : 1),
             (s^5 - 2*s^4 + 2*s^3 + s : s^5 - 3*s^4 + 4*s^3 - 3*s^2 + 2*s - 1 : 1),
             (s^5 - 2*s^4 + 3*s^3 - 3*s^2 + 3*s - 1 : -s^5 + 3*s^4 - 5*s^3 + 4*s^2 - 4*s + 2 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 1/4*y^2, y^2])
            sage: f.preperiodic_points(1, 1, formal=True)
            [(-1/2 : 1), (1 : 0)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2])
            sage: f.preperiodic_points(0, 2, formal=True)                               # needs sage.libs.pari
            [(-1/2 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: K.<v> = QuadraticField(5)
            sage: phi = QQ.embeddings(K)[0]
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.preperiodic_points(1, 1, R=phi)
            [(-1/2*v - 1/2 : 1), (1/2*v - 1/2 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(2*x - y)
            sage: f = DynamicalSystem_projective([x^2 - y^2, 2*(x^2 - y^2), y^2 - z^2],
            ....:                                domain=X)
            sage: f.preperiodic_points(1, 1)                                            # needs sage.rings.function_field
            [(-1/4 : -1/2 : 1), (1 : 2 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, z^2, y^2])
            sage: f.preperiodic_points(1, 1)                                            # needs sage.rings.function_field
            [(-3/2 : -1 : 1), (-3/2 : 1 : 1), (-1/2 : -1 : 1), (1/2 : -1 : 1),
             (1/2 : 1 : 1), (3/2 : -1 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])
            sage: sorted(f.preperiodic_points(2, 1))                                    # needs sage.rings.function_field
            [(0 : 2 : 1), (0 : 3 : 1), (1 : 2 : 1), (1 : 3 : 1), (2 : 0 : 1), (2 : 1 : 0),
             (2 : 1 : 1), (2 : 2 : 1), (2 : 3 : 1), (2 : 4 : 1), (3 : 0 : 1), (3 : 1 : 0),
             (3 : 1 : 1), (3 : 2 : 1), (3 : 3 : 1), (3 : 4 : 1), (4 : 2 : 1), (4 : 3 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: f = DynamicalSystem_projective([x^2, x*y, z^2])
            sage: f.preperiodic_points(2, 1, return_scheme=True, minimal=False)
            Closed subscheme of
             Projective Space of dimension 2 over Finite Field of size 5 defined by:
              0,
              x^8*z^4 - x^4*z^8,
              x^7*y*z^4 - x^3*y*z^8

        When the ring over which to find the preperiodic points is a number
        field, the ordering of the preperiodic points might depend on the
        architecture (32 or 64 bits)::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: R.<z> = QQ[]
            sage: K.<v> = NumberField(z^4 - z^2 - 1)                                    # needs sage.rings.number_field
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: sorted(f.preperiodic_points(2, 1, R=K), key=str)                      # needs sage.rings.number_field
            [(-v : 1), (v : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2, z^2])
            sage: f.preperiodic_points(0, 2, formal=True)                               # needs sage.rings.function_field
            [(-1/2 : 1 : 0), (-1/2 : 1 : 1)]

        ::

            sage: S.<c> = QQ[]
            sage: R.<x,y> = PolynomialRing(S, 2)
            sage: P = ProjectiveSpace(R)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.preperiodic_points(1, 2, return_scheme=True)                        # needs sage.rings.function_field
            Closed subscheme of Projective Space of dimension 1 over Univariate
             Polynomial Ring in c over Rational Field defined by:
              x^2 - x*y + (c + 1)*y^2

        TESTS::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, x*y, z^2])
            sage: f.preperiodic_points(2, 1, minimal=False)                             # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            TypeError: use return_scheme=True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2])
            sage: f.preperiodic_points(1.2, 3)
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer
            sage: f.preperiodic_points(1, 3.1)
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem([x^2 - z^2, y^2 - 21/16*z^2, z^2])
            sage: len(f.preperiodic_points(1, 2, minimal=True, formal=False)) == 16     # needs sage.rings.function_field
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - y^2, 2*(x^2 - y^2), y^2 - z^2])
            sage: f.preperiodic_points(2, 2)                                            # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: dynamical system is not a morphism,
            cannot calculate minimal or formal preperiodic points
        """
    def periodic_points(self, n, minimal: bool = True, formal: bool = False, R=None, algorithm: str = 'variety', return_scheme: bool = False):
        """
        Compute the periodic points of period ``n`` of this dynamical system
        defined over the ring ``R`` or the base ring of the map.

        This can be done either by finding the rational points on the variety
        defining the points of period ``n``, or, for finite fields,
        finding the cycle of appropriate length in the cyclegraph. For small
        cardinality fields, the cyclegraph algorithm is effective for any
        map and length cycle, but is slow when the cyclegraph is large.
        The variety algorithm is good for small period, degree, and dimension,
        but is slow as the defining equations of the variety get more
        complicated.

        For rational maps, where there are potentially infinitely many periodic
        points of a given period, you must use the ``return_scheme`` option.
        Note that this scheme will include the indeterminacy locus.

        INPUT:

        - ``n`` -- positive integer

        - ``minimal`` -- boolean (default: ``True``); ``True`` specifies to
          find only the periodic points of minimal period ``n`` and ``False``
          specifies to find all periodic points of period ``n``

        - ``formal`` -- boolean (default: ``False``); ``True`` specifies to
          find the formal periodic points only. The formal periodic points
          are the points in the support of the dynatomic cycle.

        - ``R`` -- (optional) a commutative ring. Defaults to the base ring of
          this map

        - ``algorithm`` -- (default: ``'variety'``) must be one of
          the following:

          * ``'variety'`` -- find the rational points on the appropriate variety
          * ``'cyclegraph'`` -- find the cycles from the cycle graph

        - ``return_scheme`` -- return a subscheme of the ambient space
          that defines the ``n`` th periodic points

        OUTPUT:

        A list of periodic points of this map or the subscheme defining
        the periodic points.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([x^2 - x*y + y^2, x^2 - y^2 + x*y])
            sage: f.periodic_points(1)
            [(-0.50000000000000000? - 0.866025403784439?*I : 1),
             (-0.50000000000000000? + 0.866025403784439?*I : 1),
             (1 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y,z> = ProjectiveSpace(QuadraticField(5,'t'), 2)
            sage: f = DynamicalSystem_projective([x^2 - 21/16*z^2, y^2 - z^2, z^2])
            sage: f.periodic_points(2)
            [(-5/4 : -1 : 1), (-5/4 : -1/2*t + 1/2 : 1), (-5/4 : 0 : 1),
             (-5/4 : 1/2*t + 1/2 : 1), (-3/4 : -1 : 1), (-3/4 : 0 : 1),
             (1/4 : -1 : 1), (1/4 : -1/2*t + 1/2 : 1), (1/4 : 0 : 1),
             (1/4 : 1/2*t + 1/2 : 1), (7/4 : -1 : 1), (7/4 : 0 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2 , z^2])
            sage: f.periodic_points(2, formal=True)                                     # needs sage.rings.function_field
            [(-1/2 : 1 : 0), (-1/2 : 1 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: w = QQ['w'].0
            sage: K = NumberField(w^6 - 3*w^5 + 5*w^4 - 5*w^3 + 5*w^2 - 3*w + 1,'s')
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([x^2 + z^2, y^2 + x^2, z^2 + y^2])
            sage: sorted(f.periodic_points(1), key=str)                                 # needs sage.rings.function_field
            [(-2*s^5 + 4*s^4 - 5*s^3 + 3*s^2 - 4*s : -2*s^5 + 5*s^4 - 7*s^3 + 6*s^2 - 7*s + 3 : 1),
             (-s^5 + 3*s^4 - 4*s^3 + 4*s^2 - 4*s + 2 : -s^5 + 2*s^4 - 2*s^3 + s^2 - s : 1),
             (-s^5 + 3*s^4 - 5*s^3 + 4*s^2 - 3*s + 1 : s^5 - 2*s^4 + 3*s^3 - 3*s^2 + 4*s - 1 : 1),
             (1 : 1 : 1),
             (2*s^5 - 6*s^4 + 9*s^3 - 8*s^2 + 7*s - 4 : 2*s^5 - 5*s^4 + 7*s^3 - 5*s^2 + 6*s - 2 : 1),
             (s^5 - 2*s^4 + 2*s^3 + s : s^5 - 3*s^4 + 4*s^3 - 3*s^2 + 2*s - 1 : 1),
             (s^5 - 2*s^4 + 3*s^3 - 3*s^2 + 3*s - 1 : -s^5 + 3*s^4 - 5*s^3 + 4*s^2 - 4*s + 2 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 21/16*z^2, y^2 - 2*z^2, z^2])
            sage: f.periodic_points(2, False)                                           # needs sage.rings.function_field
            [(-5/4 : -1 : 1), (-5/4 : 2 : 1), (-3/4 : -1 : 1),
             (-3/4 : 2 : 1), (0 : 1 : 0), (1/4 : -1 : 1), (1/4 : 2 : 1),
             (1 : 0 : 0), (1 : 1 : 0), (7/4 : -1 : 1), (7/4 : 2 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 21/16*z^2, y^2 - 2*z^2, z^2])
            sage: f.periodic_points(2)                                                  # needs sage.rings.function_field
            [(-5/4 : -1 : 1), (-5/4 : 2 : 1), (1/4 : -1 : 1), (1/4 : 2 : 1)]

        ::

            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.periodic_points(2, R=QQbar, minimal=False)                          # needs sage.rings.number_field
            [(-0.50000000000000000? - 1.322875655532296?*I : 1),
             (-0.50000000000000000? + 1.322875655532296?*I : 1),
             (0.50000000000000000? - 0.866025403784439?*I : 1),
             (0.50000000000000000? + 0.866025403784439?*I : 1),
             (1 : 0)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*z^2, y^2 - 3/4*z^2, z^2])
            sage: f.periodic_points(2, formal=True)                                     # needs sage.rings.function_field
            [(-1/2 : -1/2 : 1), (-1/2 : 3/2 : 1), (3/2 : -1/2 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(307), 1)
            sage: f = DynamicalSystem_projective([x^10 + y^10, y^10])
            sage: f.periodic_points(16, minimal=True, algorithm='cyclegraph')           # needs sage.graphs
            [(69 : 1), (185 : 1), (120 : 1), (136 : 1), (97 : 1), (183 : 1),
             (170 : 1), (105 : 1), (274 : 1), (275 : 1), (154 : 1), (156 : 1),
             (87 : 1), (95 : 1), (161 : 1), (128 : 1)]

        ::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y> = ProjectiveSpace(GF(13^2, 't'), 1)
            sage: f = DynamicalSystem_projective([x^3 + 3*y^3, x^2*y])
            sage: f.periodic_points(30, minimal=True, algorithm='cyclegraph')           # needs sage.graphs
            [(t + 3 : 1), (6*t + 6 : 1), (7*t + 1 : 1), (2*t + 8 : 1),
             (3*t + 4 : 1), (10*t + 12 : 1), (8*t + 10 : 1), (5*t + 11 : 1),
             (7*t + 4 : 1), (4*t + 8 : 1), (9*t + 1 : 1), (2*t + 2 : 1),
             (11*t + 9 : 1), (5*t + 7 : 1), (t + 10 : 1), (12*t + 4 : 1),
             (7*t + 12 : 1), (6*t + 8 : 1), (11*t + 10 : 1), (10*t + 7 : 1),
             (3*t + 9 : 1), (5*t + 5 : 1), (8*t + 3 : 1), (6*t + 11 : 1),
             (9*t + 12 : 1), (4*t + 10 : 1), (11*t + 4 : 1), (2*t + 7 : 1),
             (8*t + 12 : 1), (12*t + 11 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([3*x^2 + 5*y^2, y^2])
            sage: f.periodic_points(2, R=GF(3), minimal=False)                          # needs sage.rings.function_field
            [(2 : 1)]
            sage: f.periodic_points(2, R=GF(7))                                         # needs sage.rings.function_field
            []

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, x*y, z^2])
            sage: f.periodic_points(1)                                                  # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            TypeError: use return_scheme=True

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<u> = NumberField(x^2 - x + 3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: X = P.subscheme(2*x - y)
            sage: f = DynamicalSystem_projective([x^2 - y^2, 2*(x^2 - y^2), y^2 - z^2],
            ....:                                domain=X)
            sage: f.periodic_points(2)                                                  # needs sage.rings.function_field
            [(-1/5*u - 1/5 : -2/5*u - 2/5 : 1), (1/5*u - 2/5 : 2/5*u - 4/5 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - y^2, x^2 - z^2, y^2 - z^2])
            sage: f.periodic_points(1)                                                  # needs sage.rings.function_field
            [(-1 : 0 : 1)]
            sage: f.periodic_points(1, return_scheme=True)
            Closed subscheme of Projective Space of dimension 2 over Rational Field
            defined by:
              -x^3 + x^2*y - y^3 + x*z^2,
              -x*y^2 + x^2*z - y^2*z + x*z^2,
              -y^3 + x^2*z + y*z^2 - z^3

        ::

            sage: P.<x,y>=ProjectiveSpace(GF(3), 1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: f.periodic_points(2, R=GF(3^2,'t'))                                   # needs sage.rings.finite_rings
            [(t + 2 : 1), (2*t : 1)]

        ::

            sage: S.<c> = QQ[]
            sage: R.<x,y> = PolynomialRing(S, 2)
            sage: P = ProjectiveSpace(R)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.periodic_points(2, return_scheme=True)                              # needs sage.rings.function_field
            Closed subscheme of Projective Space of dimension 1 over Univariate
            Polynomial Ring in c over Rational Field defined by:
              x^2 + x*y + (c + 1)*y^2

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: f = DynamicalSystem([x^2 - 2*y^2, y^2, z^2])
            sage: X = f.periodic_points(2, minimal=False, formal=True,  # long time
            ....:                       return_scheme=True)
            sage: len(X.defining_polynomials())                         # long time
            19

        TESTS::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 - y^2, 2*(x^2 - y^2), y^2 - z^2])
            sage: f.periodic_points(2, minimal=True)                                    # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: dynamical system is not a morphism, cannot calculate minimal or formal periodic points
        """
    def multiplier_spectra(self, n, formal: bool = False, type: str = 'point', use_algebraic_closure: bool = True, check: bool = True):
        """
        Compute the ``n`` multiplier spectra of this dynamical system.

        This is the set of multipliers of all periodic points of
        period ``n`` included with the appropriate multiplicity.
        User can also specify to compute the formal ``n`` multiplier spectra
        instead which includes the multipliers of all formal periodic points
        of period ``n`` with appropriate multiplicity. The map must be defined over
        projective space over a number field or finite field.

        By default, the computations are done over the algebraic closure of the
        base field. If the map is defined over projective space of dimension 1,
        the computation can be done over the minimal extension of the base field that
        contains the periodic points. Otherwise, it will be done over the base ring
        of the map.

        INPUT:

        - ``n`` -- positive integer, the period

        - ``formal`` -- boolean (default: ``False``); ``True`` specifies
          to find the formal ``n`` multiplier spectra of this map and
          ``False`` specifies to find the ``n`` multiplier spectra

        - ``type`` -- (default: ``'point'``) string; either ``'point'``
          or ``'cycle'`` depending on whether you compute one multiplier
          per point or one per cycle

        - ``use_algebraic_closure`` -- boolean (default: ``True``); if ``True`` uses the
          algebraic closure. Using the algebraic closure can sometimes lead to numerical instability
          and extraneous errors. For most accurate results in dimension 1, set to ``False``.
          If ``False``, and the map is defined over projective space of
          dimension 1, uses the smallest extension of the base field
          containing all the periodic points. If the map is defined over projective space
          of dimension greater than 1, then the base ring of the map is used.

        - ``check`` -- boolean (default: ``True``); whether to check if the
          full multiplier spectra was computed. If ``False``, can lead to
          mathematically incorrect answers in dimension greater than 1. Ignored
          if ``use_algebraic_closure`` is ``True`` or if this dynamical system is defined
          over projective space of dimension 1.

        OUTPUT:

        A list of field elements if the domain of the map is projective space of
        dimension 1. If the domain of the map is projective space of dimension
        greater than 1, a list of matrices

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2])
            sage: sorted(f.multiplier_spectra(2, type='point'))                         # needs sage.rings.number_field
            [0, 1, 1, 1, 9]
            sage: sorted(f.multiplier_spectra(2, type='cycle'))                         # needs sage.rings.number_field
            [0, 1, 1, 9]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, z^2, y^2])
            sage: f.multiplier_spectra(1)                                               # needs sage.rings.number_field
            [
            [                       2 1 - 1.732050807568878?*I]
            [                       0                       -2],
            [                       2 1 + 1.732050807568878?*I]  [ 0  0]  [ 0  0]
            [                       0                       -2], [ 0 -2], [ 0 -2],
            [ 0  0]  [0 0]  [ 2 -2]
            [ 0 -2], [0 0], [ 0 -2]
            ]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, z^2, y^2])
            sage: f.multiplier_spectra(2, formal=True)  # long time
            [
            [4 0]  [4 0]  [4 0]  [4 0]  [4 0]  [4 0]  [4 0]  [4 0]  [0 0]  [0 0]
            [0 4], [0 0], [0 0], [0 4], [0 4], [0 0], [0 0], [0 4], [0 0], [0 0],
            [4 0]  [4 0]  [4 0]  [4 0]
            [0 4], [0 4], [0 0], [0 0]
            ]

        ::

            sage: # needs sage.rings.number_field
            sage: set_verbose(None)
            sage: z = QQ['z'].0
            sage: K.<w> = NumberField(z^4 - 4*z^2 + 1,'z')
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^2 - w/4*y^2, y^2])
            sage: sorted(f.multiplier_spectra(2, formal=False, type='cycle'))
            [0,
             0.0681483474218635? - 1.930649271699173?*I,
             0.0681483474218635? + 1.930649271699173?*I,
             5.931851652578137? + 0.?e-49*I]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([4608*x^10 - 2910096*x^9*y + 325988068*x^8*y^2
            ....:         + 31825198932*x^7*y^3 - 4139806626613*x^6*y^4 - 44439736715486*x^5*y^5
            ....:         + 2317935971590902*x^4*y^6 - 15344764859590852*x^3*y^7
            ....:         + 2561851642765275*x^2*y^8 + 113578270285012470*x*y^9
            ....:         - 150049940203963800*y^10, 4608*y^10])
            sage: sorted(f.multiplier_spectra(1))                                       # needs sage.rings.number_field
            [-119820502365680843999,
             -7198147681176255644585/256,
             -3086380435599991/9,
             -3323781962860268721722583135/35184372088832,
             -4290991994944936653/2097152,
             0,
             529278480109921/256,
             1061953534167447403/19683,
             848446157556848459363/19683,
             82911372672808161930567/8192,
             3553497751559301575157261317/8192]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 7/4*y^2, y^2])
            sage: f.multiplier_spectra(3, formal=True, type='cycle')                    # needs sage.rings.number_field
            [1, 1]
            sage: f.multiplier_spectra(3, formal=True, type='point')                    # needs sage.rings.number_field
            [1, 1, 1, 1, 1, 1]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^4 + 3*y^4, 4*x^2*y^2])
            sage: f.multiplier_spectra(1, use_algebraic_closure=False)                  # needs sage.rings.number_field
            [0,
             -1,
             1/128*a^5 - 13/384*a^4 + 5/96*a^3 + 1/16*a^2 + 43/128*a + 303/128,
             -1/288*a^5 + 1/96*a^4 + 1/24*a^3 - 1/3*a^2 + 5/32*a - 115/32,
             -5/1152*a^5 + 3/128*a^4 - 3/32*a^3 + 13/48*a^2 - 63/128*a - 227/128]
            sage: f.multiplier_spectra(1)                                               # needs sage.rings.number_field
            [0,
             -1,
             1.951373035591442?,
             -2.475686517795721? - 0.730035681602057?*I,
             -2.475686517795721? + 0.730035681602057?*I]

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(5), 1)
            sage: f = DynamicalSystem_projective([x^4 + 2*y^4, 4*x^2*y^2])
            sage: f.multiplier_spectra(1, use_algebraic_closure=False)                  # needs sage.rings.finite_rings
            [0, 3*a + 3, 2*a + 1, 1, 1]
            sage: f.multiplier_spectra(1)
            [0, 2*z2 + 1, 3*z2 + 3, 1, 1]

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([x^5 + 3*y^5, 4*x^3*y^2])
            sage: f.multiplier_spectra(1)
            [0,
             -4.106544657178796?,
             -7/4,
             1.985176555073911?,
             -3.064315948947558? - 1.150478041113253?*I,
             -3.064315948947558? + 1.150478041113253?*I]

        ::

            sage: K = GF(3).algebraic_closure()
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^5 + 2*y^5, 4*x^3*y^2])
            sage: f.multiplier_spectra(1)
            [0, z3 + 2, z3 + 1, z3, 1, 1]

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: f.multiplier_spectra(1)                                               # needs sage.rings.number_field
            [1, 1, 1]

        ::

            sage: K = GF(3).algebraic_closure()
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([x^2 + 2*y^2, 4*x*y, z^2])
            sage: f.multiplier_spectra(1)                                               # needs sage.rings.number_field
            [
            [0 0]  [1 0]  [1 0]  [1 0]  [2 0]  [2 0]  [2 0]
            [0 0], [0 0], [0 0], [0 0], [0 1], [0 1], [0 1]
            ]

        ::

            sage: F.<a> = GF(7)
            sage: P.<x,y> = ProjectiveSpace(F, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: sorted(f.multiplier_spectra(1))
            [0, 3, 6]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, z^2, y^2])
            sage: g = f.change_ring(QQbar)                                              # needs sage.rings.number_field
            sage: f.multiplier_spectra(1) == g.multiplier_spectra(1)    # long time, needs sage.rings.number_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(5)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([x^2 + w*x*y + y^2, y^2, z^2])
            sage: f.multiplier_spectra(1)                               # long time
            [
            [1.000000000000000? - 1.572302755514847?*I                                         0]
            [1.000000000000000? - 1.572302755514847?*I 0.618033988749895? - 1.757887921270715?*I]
            [1.000000000000000? + 1.572302755514847?*I                                         0]
            [1.000000000000000? + 1.572302755514847?*I 0.618033988749895? + 1.757887921270715?*I]
            [                                        0                                         0],
            [                                        0                                         2],
            [                                        0                                         0],
            [                                        0                                         2],
            [0 0]  [0 0]  [                 2 2.236067977499790?]
            [0 0], [0 0], [                 0                  0]
            ]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, z^2, y^2])
            sage: f.multiplier_spectra(1, use_algebraic_closure=False)                  # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: failed to compute the full multiplier spectra. Try use_algebraic_closure=True
            or extend the base ring of this dynamical system
        """
    def sigma_invariants(self, n, formal: bool = False, embedding=None, type: str = 'point', return_polynomial: bool = False, chow: bool = False, deform: bool = False, check: bool = True):
        """
        Compute the values of the elementary symmetric polynomials evaluated
        on the ``n`` multiplier spectra of this dynamical system.

        The sigma invariants are the symmetric polynomials evaluated on the
        characteristic polynomial of the multipliers. See [Hutz2019]_ for
        the full definition. Spepcifically, this function returns either
        the following polynomial or its coefficients (with signs
        appropriately adjusted):

         .. MATH::

            \\prod_{P \\text{ period n}} ( w - c(P,t)),

        where `c(P,t)` is the characteristic polynomial (variable `t`) of the
        multiplier at `P`. Note that in dimension 1, only the coefficients
        of the constant term is returned.

        The invariants can be computed for points of period ``n`` or
        points of formal period ``n``. The base
        ring should be a number field, number field order, or
        a finite field or a polynomial ring or function field over a
        number field, number field order, or finite field.

        The parameter ``type`` determines if the sigma are computed from
        the multipliers calculated at one per cycle (with multiplicity)
        or one per point (with multiplicity). Only implemented
        for dimension 1. Note that in the ``cycle`` case, a map with a cycle
        which collapses into multiple smaller cycles, this is still
        considered one cycle. In other words, if a 4-cycle collapses into
        a 2-cycle with multiplicity 2, there is only one multiplier used
        for the doubled 2-cycle when computing ``n=4``.

        ALGORITHM:

        In dimension 1, we use the Poisson product of the resultant of
        two polynomials:

        .. MATH::

            res(f,g) = \\prod_{f(a)=0} g(a).

        In higher dimensions, we use elimination theory (Groebner bases)
        to compute the equivalent of the Poisson product. Letting `f` be
        the polynomial defining the periodic or formal
        periodic points and `g` the polynomial `w - F` for an auxilarly
        variable `w` and `F` the characteristic polynomial of the Jacobian matrix
        of `f`. Note that if `f` is a rational function, we clear
        denominators for `g`.

        To calculate the full polynomial defining the sigma invariants,
        we follow the algorithm outlined in section 4 of [Hutz2019]_. There
        are 4 cases:

        - multipliers and ``n`` periodic points all distinct -- in this case,
          we can use Proposition 4.1 of [Hutz2019]_ to compute the sigma invariants

        - ``n`` -- periodic points are all distinct, multipliers are repeated; here we
          can use Proposition 4.2 of [Hutz2019]_ to compute the sigma invariants.
          This corresponds to ``chow=True``.

        - ``n`` -- periodic points are repeated, multipliers are all distinct; to deal
          with this case, we deform the map by a formal parameter `k`. The deformation
          separates the ``n`` periodic points, making them distinct, and we can recover
          the ``n`` periodic points of the original map by specializing `k` to 0.
          This corresponds to ``deform=True``.

        - ``n`` -- periodic points are repeated, multipliers are repeated; here we
          can use both cases 2 and 3 together. This corresponds to ``deform=True``
          and ``chow=True``.

        As we do not want to check which case we are in beforehand, we throw a
        :exc:`ValueError` if the computed polynomial does not have the correct
        degree.

        INPUT:

        - ``n`` -- positive integer, the period

        - ``formal`` -- boolean (default: ``False``); ``True`` specifies
          to find the values of the elementary symmetric polynomials
          corresponding to the formal ``n`` multiplier spectra and ``False``
          specifies to instead find the values corresponding to the ``n``
          multiplier spectra, which includes the multipliers of all
          periodic points of period ``n``

        - ``embedding`` -- (default: ``None``) must be ``None``, passing an embedding
          is no longer supported, see :issue:`32205`

        - ``type`` -- (default: ``'point'``) string; either ``'point'``
          or ``'cycle'`` depending on whether you compute with one
          multiplier per point or one per cycle. Not implemented for
          dimension greater than 1.

        - ``return polynomial`` -- boolean (default: ``False``);
          ``True`` specifies returning the polynomial which generates
          the sigma invariants, see [Hutz2019]_ for the full definition.
          The polynomial is always a multivariate polynomial with variables
          ``w`` and ``t``.

        - ``chow`` -- boolean (default: ``False``); ``True`` specifies
          using the Chow algorithm from [Hutz2019]_ to compute the sigma
          invariants. While slower, the Chow algorithm does not lose
          information about multiplicities of the multipliers. In order
          to accurately compute the sigma polynomial when there is a
          repeated multiplier, ``chow`` must be ``True``.

        - ``deform`` -- boolean (default: ``False``); ``True`` specifies
          first deforming the map so that all periodic points are distinct
          and then calculating the sigma invariants. In order to accurately
          calculate the sigma polynomial when there is a periodic point with
          multiplicity, ``deform`` must be ``True``.

        - ``check`` -- boolean (default: ``True``); when ``True`` the degree of
          the sigma polynomial is checked against the expected degree. This is
          done as the sigma polynomial may drop degree if multiplicities of periodic
          points or multipliers are not correctly accounted for using ``chow`` or
          ``deform``.

        .. WARNING::

            Setting ``check`` to ``False`` can lead to mathematically incorrect
            answers.

        OUTPUT: list of elements in the base ring, unless ``return_polynomial``
        is ``True``, in which case a polynomial in ``w`` and ``t`` is returned.
        The variable ``t`` is the variable of the characteristic
        polynomials of the multipliers.

        If this map is defined over `\\mathbb{P}^N`, where `N > 1`, then
        the list is the coefficients of `w` and `t`, in lexographical order with `w > t`.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y + y^2, y^2 + x*y])
            sage: f.sigma_invariants(1)                                                 # needs sage.rings.number_field
            [3, 3, 1]

        If ``return_polynomial`` is ``True``, then following [Hutz2019]_
        we return a two variable polynomial in `w` and `t`::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 2*y^2, y^2])
            sage: poly = f.sigma_invariants(1, return_polynomial=True); poly
            w^3 - 3*w^2*t + 2*w^2 + 3*w*t^2 - 4*w*t + 8*w - t^3 + 2*t^2 - 8*t

        From the full polynomial, we can easily recover the one variable polynomial whose coefficients
        are symmetric functions in the multipliers, up to sign::

            sage: w, t = poly.variables()
            sage: poly.specialization({w:0}).monic()
            t^3 - 2*t^2 + 8*t
            sage: f.sigma_invariants(1)                                                 # needs sage.rings.number_field
            [2, 8, 0]

        For dynamical systems on `\\mathbb{P}^N`, where `N > 1`, the full polynomial
        is needed to distinguish the conjugacy class. We can, however, still return
        a list in this case::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, z^2, y^2])
            sage: f.sigma_invariants(1, chow=True)
            [1, 7, -6, -12, 21, -36, -60, 72, 48, 35, -90, -120, 352, 96, -288, -64, 35,
             -120, -120, 688, -96, -1056, 320, 384, 0, 21, -90, -60, 672, -384, -1440, 1344,
             768, -768, 0, 0, 7, -36, -12, 328, -336, -864, 1472, 384, -1536, 512, 0, 0, 0,
             1, -6, 0, 64, -96, -192, 512, 0, -768, 512, 0, 0, 0, 0, 0]

        When calculating the sigma invariants for `\\mathbb{P}^N`, with `N > 1`,
        the default algorithm loses information about multiplicities. Note that
        the following call to sigma invariants returns a degree 6 polynomial in `w`::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])
            sage: f.sigma_invariants(1, return_polynomial=True, check=False)
            w^6 - 6*w^5*t^2 + 8*w^5*t - 4*w^5 + 15*w^4*t^4 - 40*w^4*t^3 + 40*w^4*t^2 -
            16*w^4*t - 20*w^3*t^6 + 80*w^3*t^5 - 120*w^3*t^4 + 80*w^3*t^3 - 16*w^3*t^2 +
            15*w^2*t^8 - 80*w^2*t^7 + 160*w^2*t^6 - 144*w^2*t^5 + 48*w^2*t^4 - 6*w*t^10 +
            40*w*t^9 - 100*w*t^8 + 112*w*t^7 - 48*w*t^6 + t^12 - 8*t^11 + 24*t^10 -
            32*t^9 + 16*t^8

        Setting ``chow`` to ``True``, while much slower, accounts correctly for multiplicities.
        Note that the following returns a degree 7 polynomial in `w`::

            sage: f.sigma_invariants(1, return_polynomial=True, chow=True)
            w^7 - 7*w^6*t^2 + 10*w^6*t - 4*w^6 + 21*w^5*t^4 - 60*w^5*t^3 + 60*w^5*t^2 -
            24*w^5*t - 35*w^4*t^6 + 150*w^4*t^5 - 240*w^4*t^4 + 176*w^4*t^3 - 48*w^4*t^2 +
            35*w^3*t^8 - 200*w^3*t^7 + 440*w^3*t^6 - 464*w^3*t^5 + 224*w^3*t^4 -
            32*w^3*t^3 - 21*w^2*t^10 + 150*w^2*t^9 - 420*w^2*t^8 + 576*w^2*t^7 -
            384*w^2*t^6 + 96*w^2*t^5 + 7*w*t^12 - 60*w*t^11 + 204*w*t^10 - 344*w*t^9 +
            288*w*t^8 - 96*w*t^7 - t^14 + 10*t^13 - 40*t^12 + 80*t^11 - 80*t^10 + 32*t^9

        ::

            sage: # needs sage.rings.number_field
            sage: set_verbose(None)
            sage: z = QQ['z'].0
            sage: K = NumberField(z^4 - 4*z^2 + 1, 'z')
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^2 - 5/4*y^2, y^2])
            sage: f.sigma_invariants(2, formal=False, type='cycle')
            [13, 11, -25, 0]
            sage: f.sigma_invariants(2, formal=False, type='point')
            [12, -2, -36, 25, 0]

        check that infinity as part of a longer cycle is handled correctly::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([y^2, x^2])
            sage: f.sigma_invariants(2, type='cycle')
            [12, 48, 64, 0]
            sage: f.sigma_invariants(2, type='point')
            [12, 48, 64, 0, 0]
            sage: f.sigma_invariants(2, type='cycle', formal=True)
            [0]
            sage: f.sigma_invariants(2, type='point', formal=True)
            [0, 0]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(3)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^2 - w*y^2, (1-w)*x*y])
            sage: f.sigma_invariants(2, formal=False, type='cycle')
            [6*w + 21, 78*w + 159, 210*w + 367, 90*w + 156]
            sage: f.sigma_invariants(2, formal=False, type='point')
            [6*w + 24, 96*w + 222, 444*w + 844, 720*w + 1257, 270*w + 468]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([512*x^5 - 378128*x^4*y + 76594292*x^3*y^2
            ....:         - 4570550136*x^2*y^3 - 2630045017*x*y^4 + 28193217129*y^5, 512*y^5])
            sage: f.sigma_invariants(1)                                                 # needs sage.rings.number_field
            [19575526074450617/1048576, -9078122048145044298567432325/2147483648,
             -2622661114909099878224381377917540931367/1099511627776,
             -2622661107937102104196133701280271632423/549755813888,
             338523204830161116503153209450763500631714178825448006778305/72057594037927936, 0]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: f = DynamicalSystem([x^2, y^2, z^2])
            sage: f.sigma_invariants(1, chow=True, return_polynomial=True)
            w^7 - 2*w^6*t^2 + w^6 + w^5*t^4 + w^5*t + w^4*t^3 + 2*w^4*t^2 + w^3*t^5 -
            w^3*t^4 - 2*w^3*t^3 - w^2*t^10 + w^2*t^7 + w^2*t^6 + w^2*t^5 + 2*w*t^12 -
            w*t^10 + w*t^9 - 2*w*t^8 - w*t^7 - t^14 + 2*t^9

        ::

            sage: # needs sage.rings.number_field
            sage: R.<c> = QQ[]
            sage: Pc.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem_projective([x^2 + c*y^2, y^2])
            sage: f.sigma_invariants(1)
            [2, 4*c, 0]
            sage: f.sigma_invariants(2, formal=True, type='point')
            [8*c + 8, 16*c^2 + 32*c + 16]
            sage: f.sigma_invariants(2, formal=True, type='cycle')
            [4*c + 4]

        ::

            sage: R.<c> = QQ[]
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: f = DynamicalSystem([x^2 + c*y^2, y^2])
            sage: f.sigma_invariants(1, return_polynomial=True)
            w^3 + (-3)*w^2*t + 2*w^2 + 3*w*t^2 + (-4)*w*t + 4*c*w - t^3 + 2*t^2 + (-4*c)*t
            sage: f.sigma_invariants(2, chow=True, formal=True,                         # needs sage.libs.pari
            ....:                    return_polynomial=True)
            w^2 + (-2)*w*t + (8*c + 8)*w + t^2 + (-8*c - 8)*t + 16*c^2 + 32*c + 16

        ::

            sage: R.<c,d> = QQ[]
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: f = DynamicalSystem([x^2 + c*z^2, y^2 + d*z^2, z^2])
            sage: len(dict(f.sigma_invariants(1, return_polynomial=True)))
            51

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x^2 + 3*y^2, x*y])
            sage: f.sigma_invariants(1, deform=True, return_polynomial=True)            # needs sage.rings.function_field
            w^3 - 3*w^2*t + 3*w^2 + 3*w*t^2 - 6*w*t + 3*w - t^3 + 3*t^2 - 3*t + 1

        doubled fixed point::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2])
            sage: f.sigma_invariants(2, formal=True)                                    # needs sage.rings.number_field
            [2, 1]

        doubled 2 cycle::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 5/4*y^2, y^2])
            sage: f.sigma_invariants(4, formal=False, type='cycle')                     # needs sage.rings.number_field
            [170, 5195, 172700, 968615, 1439066, 638125, 0]

        TESTS::

            sage: F.<t> = FunctionField(GF(5))
            sage: P.<x,y> = ProjectiveSpace(F,1)
            sage: f = DynamicalSystem_projective([x^2 + (t/(t^2+1))*y^2, y^2], P)
            sage: f.sigma_invariants(1)                                                 # needs sage.rings.number_field
            [2, 4*t/(t^2 + 1), 0]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<w> = QQ[]
            sage: N.<n> = NumberField(w^2 + 1)
            sage: P.<x,y,z> = ProjectiveSpace(N, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2])
            sage: f.sigma_invariants(1, chow=True) == f.change_ring(QQ).sigma_invariants(1, chow=True)
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x^2 + 3*y^2, x*y])
            sage: f.sigma_invariants(1, formal=True, return_polynomial=True)
            Traceback (most recent call last):
            ..
            ValueError: sigma polynomial dropped degree, as multiplicities were not accounted
            for correctly; try setting chow=True and/or deform=True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x^2 + 3*y^2, x*y])
            sage: f.sigma_invariants(1, return_polynomial=True)
            Traceback (most recent call last):
            ..
            ValueError: sigma polynomial dropped degree, as multiplicities were not accounted
            for correctly; try setting chow=True and/or deform=True
        """
    def reduced_form(self, **kwds):
        """
        Return reduced form of this dynamical system.

        The reduced form is the `SL(2, \\ZZ)` equivalent morphism obtained
        by applying the binary form reduction algorithm from Stoll and
        Cremona [CS2003]_ to the homogeneous polynomial defining the periodic
        points (the dynatomic polynomial). The smallest period `n` with
        enough periodic points is used and without roots of too large
        multiplicity.

        This should also minimize the size  of the coefficients,
        but this is not always the case. By default the coefficient minimizing
        algorithm in [HS2018]_ is applied.

        See :meth:`sage.rings.polynomial.multi_polynomial.reduced_form` for
        the information on binary form reduction.

        Implemented by Rebecca Lauren Miller as part of GSOC 2016.
        Minimal height added by Ben Hutz July 2018.

        INPUT: keyword arguments:

        - ``prec`` -- integer (default: 300); desired precision

        - ``return_conjuagtion`` -- boolean (default: ``True``); return
          an element of `SL(2, \\ZZ)`

        - ``error_limit`` -- (default: 0.000001) a real number, sets
          the error tolerance

        - ``smallest_coeffs`` -- boolean (default: ``True``); whether to find the
          model with smallest coefficients

        - ``dynatomic`` -- boolean (default: ``True``); to use formal periodic points

        - ``start_n`` -- positive integer (default: 1); first period to try to find
          appropriate binary form

        - ``emb`` -- (optional) embedding of based field into CC

        - ``algorithm`` -- (optional) which algorithm to use to find all
          minimal models. Can be one of the following:

          * ``'BM'`` -- Bruin-Molnar algorithm [BM2012]_
          * ``'HS'`` -- Hutz-Stoll algorithm [HS2018]_

        - ``check_minimal`` -- boolean (default: ``True``); whether to check
          if this map is a minimal model

        - ``smallest_coeffs`` -- boolean (default: ``True``); whether to find the
          model with smallest coefficients

        OUTPUT:

        - a projective morphism

        - a matrix

        EXAMPLES::

            sage: PS.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^3 + x*y^2, y^3])
            sage: m = matrix(QQ, 2, 2, [-201221, -1, 1, 0])
            sage: f = f.conjugate(m)
            sage: f.reduced_form(prec=50, smallest_coeffs=False)  # this needs 2 periodic
            Traceback (most recent call last):
            ...
            ValueError: accuracy of Newton's root not within tolerance(0.00006... > 1e-06), increase precision
            sage: f.reduced_form(smallest_coeffs=False)
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^3 + x*y^2 : y^3)
            ,
            <BLANKLINE>
            [     0     -1]
            [     1 201221]
            )

        ::

            sage: PS.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y, y^2])  # this needs 3 periodic
            sage: m = matrix(QQ, 2, 2, [-221, -1, 1, 0])
            sage: f = f.conjugate(m)
            sage: f.reduced_form(prec=200, smallest_coeffs=False)
            (
            Dynamical System of Projective Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (x : y) to (-x^2 + x*y - y^2 : -y^2)
            ,
            [  0  -1]
            [  1 220]
            )

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^3, y^3])
            sage: f.reduced_form(smallest_coeffs=False)
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^3 : y^3)
            ,
            <BLANKLINE>
            [1 0]
            [0 1]
            )

        ::

            sage: PS.<X,Y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([7365*X^4 + 12564*X^3*Y + 8046*X^2*Y^2
            ....:                                   + 2292*X*Y^3 + 245*Y^4,
            ....:                                 -12329*X^4 - 21012*X^3*Y - 13446*X^2*Y^2
            ....:                                   - 3828*X*Y^3 - 409*Y^4])
            sage: f.reduced_form(prec=30, smallest_coeffs=False)
            Traceback (most recent call last):
            ...
            ValueError: accuracy of Newton's root not within tolerance(0.00008... > 1e-06), increase precision
            sage: f.reduced_form(smallest_coeffs=False)
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (X : Y) to
                    (-7*X^4 - 12*X^3*Y - 42*X^2*Y^2 - 12*X*Y^3 - 7*Y^4
                     : -X^4 - 4*X^3*Y - 6*X^2*Y^2 - 4*X*Y^3 - Y^4),
            <BLANKLINE>
            [-1  2]
            [ 2 -5]
            )

        ::

            sage: # needs sage.rings.real_mpfr sage.symbolic
            sage: P.<x,y> = ProjectiveSpace(RR, 1)
            sage: f = DynamicalSystem_projective([x^4, RR(sqrt(2))*y^4])
            sage: m = matrix(RR, 2, 2, [1,12,0,1])
            sage: f = f.conjugate(m)
            sage: g, m = f.reduced_form(smallest_coeffs=False); m
            [  1 -12]
            [  0   1]

        ::

            sage: # needs sage.rings.real_mpfr sage.symbolic
            sage: P.<x,y> = ProjectiveSpace(CC, 1)
            sage: f = DynamicalSystem_projective([x^4, CC(sqrt(-2))*y^4])
            sage: m = matrix(CC, 2, 2, [1,12,0,1])
            sage: f = f.conjugate(m)
            sage: g, m = f.reduced_form(smallest_coeffs=False); m
            [  1 -12]
            [  0   1]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^3, w*y^3])
            sage: m = matrix(K, 2, 2, [1,12,0,1])
            sage: f = f.conjugate(m)
            sage: f.reduced_form(smallest_coeffs=False)
            (
            Dynamical System of Projective Space of dimension 1 over Number Field in w
             with defining polynomial x^2 - 2 with w = 1.414213562373095?
              Defn: Defined on coordinates by sending (x : y) to (x^3 : w*y^3) ,
            <BLANKLINE>
            [  1 -12]
            [  0   1]
            )

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^5 + x - 3,
            ....:                     embedding=(x^5 + x - 3).roots(ring=CC)[0][0])
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([12*x^3, 2334*w*y^3])
            sage: m = matrix(K, 2, 2, [-12,1,1,0])
            sage: f = f.conjugate(m)
            sage: f.reduced_form(smallest_coeffs=False)
            (
            Dynamical System of Projective Space of dimension 1 over Number Field in w
             with defining polynomial x^5 + x - 3 with w = 1.132997565885066?
              Defn: Defined on coordinates by sending (x : y) to
                    (12*x^3 : (2334*w)*y^3) ,
            <BLANKLINE>
            [  0  -1]
            [  1 -12]
            )

        ::

            sage: P.<x,y> = QQ[]
            sage: f = DynamicalSystem([-4*y^2, 9*x^2 - 12*x*y])
            sage: f.reduced_form()
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (2*x^2 - 2*y^2 : -x^2 - 2*y^2)
            ,
            <BLANKLINE>
            [ 2 -2]
            [ 3  0]
            )

        ::

            sage: P.<x,y> = QQ[]
            sage: f = DynamicalSystem([-2*x^3 - 9*x^2*y - 12*x*y^2 - 6*y^3 , y^3])
            sage: f.reduced_form()
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^3 + 3*x^2*y : 3*x*y^2 + y^3)
            ,
            <BLANKLINE>
            [-1 -2]
            [ 1  1]
            )

        ::

            sage: P.<x,y> = QQ[]
            sage: f = DynamicalSystem([4*x^2 - 7*y^2, 4*y^2])
            sage: f.reduced_form(start_n=2, dynatomic=False) #long time
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 - x*y - y^2 : y^2)
            ,
            <BLANKLINE>
            [ 2 -1]
            [ 0  2]
            )

        ::

            sage: P.<x,y> = QQ[]
            sage: f = DynamicalSystem([4*x^2 + y^2, 4*y^2])
            sage: f.reduced_form()  # long time
            (
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 - x*y + y^2 : y^2)
            ,
            <BLANKLINE>
            [ 2 -1]
            [ 0  2]
            )
        """
    def postcritical_set(self, check: bool = True):
        """
        Return the postcritical set of this dynamical system.

        Raises an error if this dynamical system is not postcritically finite.

        The postcritical set is union of points which are in the forward orbits
        of the critical points. In other words, the set of points `Q` such that
        `f^n(P) = Q` for some positive integer `n` and critical point `P`, where
        `f` is this map.

        Note that the orbit of all critical points is found, even if the
        critical points are defined in an extension of the base ring of
        this dynamical system. We extend to the field defined by
        ``f.field_of_definition_critical()``, where ``f`` is this map.

        INPUT:

        - ``check`` -- boolean (default: ``True``); whether to check
          if this dynamical system is postcritically finite or not

        OUTPUT: the set of postcritical points

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x^3 - 3/2* x*y^2, y^3])
            sage: f.postcritical_set()                                                  # needs sage.rings.number_field
            [(1/2*a : 1), (-1/2*a : 1), (1 : 0)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([3*x^3 - 9/2* x^2*y+y^3, y^3])
            sage: f.postcritical_set(check=False)                                       # needs sage.rings.number_field
            [(1 : 1), (-1/2 : 1), (1 : 0)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([-4*y^2, 9*x^2 - 12*x*y])
            sage: f.postcritical_set()                                                  # needs sage.rings.number_field
            [(1 : 1), (4/3 : 1), (1 : 0), (0 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(2)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem([x^2 + (-2)*y^2, y^2])
            sage: m = matrix(K, 2, 2, [v, 1, 0, 1])
            sage: g = f.conjugate(m)
            sage: g.postcritical_set()
            [(-3/2*a : 1), (1/2*a : 1), (1 : 0)]

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<z> = FiniteField(9)
            sage: P.<x,y> = ProjectiveSpace(F, 1)
            sage: f = DynamicalSystem([x^2 + (-2)*y^2, y^2])
            sage: m = matrix(F, 2, 2, [z, 1, 0, 1])
            sage: g = f.conjugate(m)
            sage: g.postcritical_set()
            [(1 : 0), (0 : 1), (a + 2 : 1)]
        """
    def is_chebyshev(self):
        """
        Check if ``self`` is a Chebyshev polynomial.

        OUTPUT: ``True`` if ``self`` is Chebyshev, ``False`` otherwise

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^4, y^4])
            sage: F.is_chebyshev()
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: F.is_chebyshev()
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([2*x^2 - y^2, y^2])
            sage: F.is_chebyshev()
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^3, 4*y^3 - 3*x^2*y])
            sage: F.is_chebyshev()
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([2*x^2 - y^2, y^2])
            sage: L.<i> = CyclotomicField(4)
            sage: M = Matrix([[0,i],[-i,0]])
            sage: F.conjugate(M)
            Dynamical System of Projective Space of dimension 1 over
             Cyclotomic Field of order 4 and degree 2
              Defn: Defined on coordinates by sending (x : y) to
                    ((-i)*x^2 : (-i)*x^2 + (2*i)*y^2)
            sage: F.is_chebyshev()
            True

        REFERENCES:

        - [Mil2006]_
        """
    def is_Lattes(self):
        """
        Check if ``self`` is a Lattes map.

        OUTPUT: ``True`` if ``self`` is Lattes, ``False`` otherwise

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^3, y^3])
            sage: F.is_Lattes()
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: F.is_Lattes()
            False

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: F = DynamicalSystem_projective([x^2 + y^2 + z^2, y^2, z^2])
            sage: F.is_Lattes()
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([(x + y)*(x - y)^3, y*(2*x + y)^3])
            sage: F.is_Lattes()
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([(x + y)^4, 16*x*y*(x - y)^2])
            sage: F.is_Lattes()
            True

        ::

            sage: f = P.Lattes_map(EllipticCurve([0, 0, 0, 0, 2]),2)
            sage: f.is_Lattes()
            True

        ::

            sage: f = P.Lattes_map(EllipticCurve([0, 0, 0, 0, 2]), 2)
            sage: L.<i> = CyclotomicField(4)
            sage: M = Matrix([[i, 0], [0, -i]])
            sage: f.conjugate(M)
            Dynamical System of Projective Space of dimension 1 over
             Cyclotomic Field of order 4 and degree 2
              Defn: Defined on coordinates by sending (x : y) to
                    ((-1/4*i)*x^4 + (-4*i)*x*y^3 : (-i)*x^3*y + (2*i)*y^4)
            sage: f.is_Lattes()
            True

        REFERENCES:

        - [Mil2006]_
        """
    def Lattes_to_curve(self, return_conjugation: bool = False, check_lattes: bool = False):
        """
        Finds a Short Weierstrass Model Elliptic curve of self
        self assumed to be Lattes map and not in characteristic 2 or 3

        INPUT:

        ``return_conjugation`` -- (default: ``False``) if ``True``, then
        return the conjugation that moves self to a map that comes from a
        Short Weierstrass Model Elliptic curve
        ``check_lattes`` -- (default: ``False``) if ``True``, then  will ValueError if not Lattes

        OUTPUT: a Short Weierstrass Model Elliptic curve which is isogenous to
        the Elliptic curve of 'self',
        If ``return_conjugation`` is ``True``
        then also returns conjugation of 'self' to short form as a matrix

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = P.Lattes_map(EllipticCurve([0, 0, 0, 10, 2]), 2)
            sage: f.Lattes_to_curve()
            Elliptic Curve defined by y^2 = x^3 + 10*x + 2 over Rational Field

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: M = matrix(QQ,2,2,[[1,2],[-1,2]])
            sage: f = P.Lattes_map(EllipticCurve([1, 1, 1, 1, 2]), 2)
            sage: f = f.conjugate(M)
            sage: f.Lattes_to_curve(return_conjugation = True)
            (
            [  -7/36*a^2 + 7/12*a + 7/3 -17/18*a^2 + 17/6*a + 34/3]
            [    -1/8*a^2 + 1/4*a + 3/2        1/4*a^2 - 1/2*a - 3],
            Elliptic Curve defined by y^2 = x^3 + (-94/27*a^2+94/9*a+376/9)*x +
            12232/243 over Number Field in a with defining polynomial y^3 - 18*y - 30
            )

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = P.Lattes_map(EllipticCurve([1, 1, 1, 2, 2]), 2)
            sage: L.<i> = CyclotomicField(4)
            sage: M = Matrix([[1+i,2*i], [0, -i]])
            sage: f = f.conjugate(M)
            sage: f.Lattes_to_curve(return_conjugation = True)
            (
            [              1 19/24*a + 19/24]
            [              0               1],
            Elliptic Curve defined by y^2 = x^3 + 95/96*a*x + (-1169/3456*a+1169/3456)
            over Number Field in a with defining polynomial y^2 + 1
            )

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: M = matrix(QQ,2,2,[[1,3],[2,1]])
            sage: E = EllipticCurve([1, 1, 1, 2, 3])
            sage: f = P.Lattes_map(E, 2)
            sage: f = f.conjugate(M)
            sage: f.Lattes_to_curve(return_conjugation = True)
            (
            [11/1602*a^2 41/3204*a^2]
            [     -2/5*a      -1/5*a],
            Elliptic Curve defined by y^2 = x^3 + 2375/3421872*a^2*x + (-254125/61593696)
            over Number Field in a with defining polynomial y^3 - 267
            )

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ , 1)
            sage: M = matrix(QQ,2,2,[[1 , 3],[2 , 1]])
            sage: E = EllipticCurve([1, 1, 1, 2, 3])
            sage: f = P.Lattes_map(E , 2)
            sage: f = f.conjugate(M)
            sage: m,H = f.Lattes_to_curve(true)
            sage: J.<x,y> = ProjectiveSpace(H.base_ring(), 1)
            sage: K = J.Lattes_map(H,2)
            sage: K = K.conjugate(m)
            sage: K.scale_by(f[0].lc()/K[0].lc())
            sage: K == f.change_ring(K.base_ring())
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(RR, 1)
            sage: F = DynamicalSystem_projective([x^4, y^4])
            sage: F.Lattes_to_curve(check_lattes=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Base ring must be a number field

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^4, y^4])
            sage: F.Lattes_to_curve(check_lattes=True)
            Traceback (most recent call last):
            ...
            ValueError: Map is not Lattes

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^4, y^4])
            sage: F.Lattes_to_curve()
            Traceback (most recent call last):
            ...
            ValueError: No Solutions found. Check if map is Lattes

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([x^3, y^3])
            sage: F.Lattes_to_curve(check_lattes=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Map is not Lattes or is Complex Lattes

        ::

            sage: K.<x>=QuadraticField(2)
            sage: P.<a,y>=ProjectiveSpace(K, 1)
            sage: E=EllipticCurve([1, x])
            sage: f=P.Lattes_map(E, 2)
            sage: f.Lattes_to_curve()
            Elliptic Curve defined by y^2 = x^3 + x + a
            over Number Field in a with defining polynomial y^2 - 2

        ::

            sage: P.<x,y>=ProjectiveSpace(QQbar, 1)
            sage: E=EllipticCurve([1, 2])
            sage: f=P.Lattes_map(E, 2)
            sage: f.Lattes_to_curve(check_lattes=true)  # long time
            Elliptic Curve defined by y^2 = x^3 + x + 2 over Rational Field

        """

class DynamicalSystem_projective_field(DynamicalSystem_projective, SchemeMorphism_polynomial_projective_space_field):
    def lift_to_rational_periodic(self, points_modp, B=None):
        """
        Given a list of points in projective space over `\\GF{p}`,
        determine if they lift to `\\QQ`-rational periodic points.

        The map must be an endomorphism of projective space defined
        over `\\QQ`.

        ALGORITHM:

        Use Hensel lifting to find a `p`-adic approximation for that
        rational point. The accuracy needed is determined by the height
        bound ``B``. Then apply the LLL algorithm to determine if the
        lift corresponds to a rational point.

        If the point is a point of high multiplicity (multiplier 1), the
        procedure can be very slow.

        INPUT:

        - ``points_modp`` -- list or tuple of pairs containing a point
          in projective space over `\\GF{p}` and the possible period

        - ``B`` -- (optional) a positive integer; the height bound for
          a rational preperiodic point

        OUTPUT: list of projective points

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.lift_to_rational_periodic([[P(0,1).change_ring(GF(7)), 4]])         # needs sage.symbolic
            [[(0 : 1), 2]]

        There may be multiple points in the lift. ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([-5*x^2 + 4*y^2, 4*x*y])
            sage: f.lift_to_rational_periodic([[P(1,0).change_ring(GF(3)), 1]])  # long time
            [[(1 : 0), 1], [(2/3 : 1), 1], [(-2/3 : 1), 1]]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([16*x^2 - 29*y^2, 16*y^2])
            sage: f.lift_to_rational_periodic([[P(3,1).change_ring(GF(13)), 3]])        # needs sage.symbolic
            [[(-1/4 : 1), 3]]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([76*x^2 - 180*x*y + 45*y^2
            ....:                                   + 14*x*z + 45*y*z - 90*z^2,
            ....:                                 67*x^2 - 180*x*y - 157*x*z + 90*y*z,
            ....:                                 -90*z^2])
            sage: f.lift_to_rational_periodic([[P(14,19,1).change_ring(GF(23)), 9]])    # long time
            [[(-9 : -4 : 1), 9]]
        """
    def all_periodic_points(self, **kwds):
        """
        Determine the set of rational periodic points
        for this dynamical system.

        The map must be defined over `\\QQ` and be an endomorphism of
        projective space. If the map is a polynomial endomorphism of
        `\\mathbb{P}^1`, i.e. has a totally ramified fixed point, then
        the base ring can be an absolute number field.
        This is done by passing to the Weil restriction.

        The default parameter values are typically good choices for
        `\\mathbb{P}^1`. If you are having trouble getting a particular
        map to finish, try first computing the possible periods, then
        try various different ``lifting_prime`` values.

        ALGORITHM:

        Modulo each prime of good reduction `p` determine the set of
        periodic points modulo `p`. For each cycle modulo `p` compute
        the set of possible periods (`mrp^e`). Take the intersection
        of the list of possible periods modulo several primes of good
        reduction to get a possible list of minimal periods of rational
        periodic points. Take each point modulo `p` associated to each
        of these possible periods and try to lift it to a rational point
        with a combination of `p`-adic approximation and the LLL basis
        reduction algorithm.

        See [Hutz2015]_.

        INPUT: keyword arguments:

        - ``R`` -- (default: domain of dynamical system) the base ring
          over which the periodic points of the dynamical system are found

        - ``prime_bound`` -- (default: ``[1,20]``) a pair (list or tuple)
          of positive integers that represent the limits of primes to use
          in the reduction step or an integer that represents the upper bound

        - ``lifting_prime`` -- (default: 23) a prime integer; argument that
          specifies modulo which prime to try and perform the lifting

        - ``period_degree_bounds`` -- (default: ``[4,4]``) a pair of positive integers
          (max period, max degree) for which the dynatomic polynomial should be solved for

        - ``algorithm`` -- (optional) specifies which algorithm to use;
          current options are `dynatomic` and `lifting`; defaults to solving the
          dynatomic for low periods and degrees and lifts for everything else

        - ``periods`` -- (optional) a list of positive integers that is
          the list of possible periods

        - ``bad_primes`` -- (optional) a list or tuple of integer primes;
          the primes of bad reduction

        - ``ncpus`` -- (default: all cpus) number of cpus to use in parallel

        OUTPUT: list of rational points in projective space

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2])
            sage: sorted(f.all_periodic_points(prime_bound=20, lifting_prime=7))  # long time
            [(-1/2 : 1), (1 : 0), (3/2 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([2*x^3 - 50*x*z^2 + 24*z^3,
            ....:                                 5*y^3 - 53*y*z^2 + 24*z^3, 24*z^3])
            sage: sorted(f.all_periodic_points(prime_bound=[1,20])) # long time
            [(-3 : -1 : 1), (-3 : 0 : 1), (-3 : 1 : 1), (-3 : 3 : 1), (-1 : -1 : 1),
             (-1 : 0 : 1), (-1 : 1 : 1), (-1 : 3 : 1), (0 : 1 : 0), (1 : -1 : 1),
             (1 : 0 : 0), (1 : 0 : 1), (1 : 1 : 1), (1 : 3 : 1), (3 : -1 : 1),
             (3 : 0 : 1), (3 : 1 : 1), (3 : 3 : 1), (5 : -1 : 1), (5 : 0 : 1),
             (5 : 1 : 1), (5 : 3 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([-5*x^2 + 4*y^2, 4*x*y])
            sage: sorted(f.all_periodic_points())  # long time
            [(-2 : 1), (-2/3 : 1), (2/3 : 1), (1 : 0), (2 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^2 - x + 1)
            sage: P.<u,v> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([u^2 + v^2, v^2])
            sage: sorted(f.all_periodic_points())                                       # needs sage.rings.function_field
            [(-w + 1 : 1), (w : 1), (1 : 0)]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^2 - x + 1)
            sage: P.<u,v> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([u^2 + v^2, u*v])
            sage: f.all_periodic_points()                                               # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            NotImplementedError: rational periodic points for number fields
            only implemented for polynomials

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: K.<v> = QuadraticField(5)
            sage: phi = QQ.embeddings(K)[0]
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: sorted(f.all_periodic_points(R=phi))
            [(-1 : 1), (-1/2*v + 1/2 : 1), (0 : 1), (1 : 0), (1/2*v + 1/2 : 1)]

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: f = DynamicalSystem_projective([x^2 - (3/4)*w^2, y^2 - 3/4*w^2,
            ....:                                 z^2 - 3/4*w^2, w^2])
            sage: sorted(f.all_periodic_points(algorithm='dynatomic'))                  # needs sage.rings.function_field
            [(-1/2 : -1/2 : -1/2 : 1),
             (-1/2 : -1/2 : 3/2 : 1),
             (-1/2 : 3/2 : -1/2 : 1),
             (-1/2 : 3/2 : 3/2 : 1),
             (0 : 0 : 1 : 0),
             (0 : 1 : 0 : 0),
             (0 : 1 : 1 : 0),
             (1 : 0 : 0 : 0),
             (1 : 0 : 1 : 0),
             (1 : 1 : 0 : 0),
             (1 : 1 : 1 : 0),
             (3/2 : -1/2 : -1/2 : 1),
             (3/2 : -1/2 : 3/2 : 1),
             (3/2 : 3/2 : -1/2 : 1),
             (3/2 : 3/2 : 3/2 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 3/4*y^2, y^2])
            sage: sorted(f.all_periodic_points(period_degree_bounds=[2,2]))             # needs sage.rings.function_field
            [(-1/2 : 1), (1 : 0), (3/2 : 1)]

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([x^2 + y^2, x*y])
            sage: f.all_periodic_points(algorithm='banana')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be 'dynatomic' or 'lifting'
        """
    def all_rational_preimages(self, points):
        """
        Given a set of rational points in the domain of this
        dynamical system, return all the rational preimages of those points.

        In others words, all the rational points which have some
        iterate in the set points. This function repeatedly calls
        :meth:`rational_preimages`. If the degree is at least two,
        by Northocott, this is always a finite set. The map must be
        defined over number fields and be an endomorphism.

        INPUT:

        - ``points`` -- list of rational points in the domain of this map

        OUTPUT: list of rational points in the domain of this map

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([16*x^2 - 29*y^2, 16*y^2])
            sage: sorted(f.all_rational_preimages([P(-1,4)]))                           # needs sage.rings.function_field
            [(-7/4 : 1), (-5/4 : 1), (-3/4 : 1), (-1/4 : 1), (1/4 : 1), (3/4 : 1),
             (5/4 : 1), (7/4 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: f = DynamicalSystem_projective([76*x^2 - 180*x*y + 45*y^2 + 14*x*z
            ....:                                   + 45*y*z - 90*z^2,
            ....:                                 67*x^2 - 180*x*y - 157*x*z + 90*y*z,
            ....:                                 -90*z^2])
            sage: sorted(f.all_rational_preimages([P(-9,-4,1)]))                        # needs sage.rings.function_field
            [(-9 : -4 : 1), (0 : -1 : 1), (0 : 0 : 1), (0 : 1 : 1), (0 : 4 : 1),
             (1 : 0 : 1), (1 : 1 : 1), (1 : 2 : 1), (1 : 3 : 1)]

        A non-periodic example ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, 2*x*y])
            sage: sorted(f.all_rational_preimages([P(17,15)]))                          # needs sage.rings.function_field
            [(1/3 : 1), (3/5 : 1), (5/3 : 1), (3 : 1)]

        A number field example::

            sage: # needs sage.rings.number_field
            sage: z = QQ['z'].0
            sage: K.<w> = NumberField(z^3 + (z^2)/4 - (41/16)*z + 23/64)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([16*x^2 - 29*y^2, 16*y^2])
            sage: sorted(f.all_rational_preimages([P(16*w^2 - 29, 16)]), key=str)
            [(-w - 1/2 : 1),
             (-w : 1),
             (-w^2 + 21/16 : 1),
             (-w^2 + 29/16 : 1),
             (-w^2 - w + 25/16 : 1),
             (-w^2 - w + 33/16 : 1),
             (w + 1/2 : 1),
             (w : 1),
             (w^2 + w - 25/16 : 1),
             (w^2 + w - 33/16 : 1),
             (w^2 - 21/16 : 1),
             (w^2 - 29/16 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(3)
            sage: P.<u,v> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([u^2 + v^2, v^2])
            sage: f.all_rational_preimages(P(4))                                        # needs sage.rings.function_field
            [(-w : 1), (w : 1)]
        """
    def all_preperiodic_points(self, **kwds):
        """
        Determine the set of rational preperiodic points for
        this dynamical system.

        The map must be defined over `\\QQ` and be an endomorphism of
        projective space. If the map is a polynomial endomorphism of
        `\\mathbb{P}^1`, i.e. has a totally ramified fixed point, then
        the base ring can be an absolute number field.
        This is done by passing to the Weil restriction.

        The default parameter values are typically good choices for
        `\\mathbb{P}^1`. If you are having trouble getting a particular
        map to finish, try first computing the possible periods, then
        try various different values for ``lifting_prime``.

        ALGORITHM:

        - Determines the list of possible periods.

        - Determines the rational periodic points from the possible periods.

        - Determines the rational preperiodic points from the rational
          periodic points by determining rational preimages.

        INPUT: keyword arguments:

        - ``R`` -- (default: domain of dynamical system) the base ring
          over which the periodic points of the dynamical system are found

        - ``prime_bound`` -- (default: ``[1, 20]``) a pair (list or tuple)
          of positive integers that represent the limits of primes to use
          in the reduction step or an integer that represents the upper bound

        - ``lifting_prime`` -- (default: 23) a prime integer; specifies
          modulo which prime to try and perform the lifting

        - ``periods`` -- (optional) a list of positive integers that is
          the list of possible periods

        - ``bad_primes`` -- (optional) a list or tuple of integer primes;
          the primes of bad reduction

        - ``ncpus`` -- (default: all cpus) number of cpus to use in parallel

        - ``period_degree_bounds`` -- (default: ``[4,4]``) a pair of positive integers
          (max period, max degree) for which the dynatomic polynomial should be solved
          for when in dimension 1

        - ``algorithm`` -- (optional) specifies which algorithm to use;
          current options are `dynatomic` and `lifting`; defaults to solving the
          dynatomic for low periods and degrees and lifts for everything else

        OUTPUT: list of rational points in projective space

        EXAMPLES::

            sage: PS.<x,y> = ProjectiveSpace(1,QQ)
            sage: f = DynamicalSystem_projective([x^2 - y^2, 3*x*y])
            sage: sorted(f.all_preperiodic_points())                                    # needs sage.rings.function_field
            [(-2 : 1), (-1 : 1), (-1/2 : 1), (0 : 1), (1/2 : 1), (1 : 0), (1 : 1), (2 : 1)]

        ::

            sage: PS.<x,y> = ProjectiveSpace(1,QQ)
            sage: f = DynamicalSystem_projective([5*x^3 - 53*x*y^2 + 24*y^3, 24*y^3])
            sage: sorted(f.all_preperiodic_points(prime_bound=10))                      # needs sage.rings.function_field
            [(-1 : 1), (0 : 1), (1 : 0), (1 : 1), (3 : 1)]

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(2,QQ)
            sage: f = DynamicalSystem_projective([x^2 - 21/16*z^2, y^2 - 2*z^2, z^2])
            sage: sorted(f.all_preperiodic_points(prime_bound=[1,8],              # long time
            ....:                                 lifting_prime=7, periods=[2]))
            [(-5/4 : -2 : 1), (-5/4 : -1 : 1), (-5/4 : 0 : 1), (-5/4 : 1 : 1), (-5/4 : 2 : 1),
             (-1/4 : -2 : 1), (-1/4 : -1 : 1), (-1/4 : 0 : 1), (-1/4 : 1 : 1), (-1/4 : 2 : 1),
             (1/4 : -2 : 1), (1/4 : -1 : 1), (1/4 : 0 : 1), (1/4 : 1 : 1), (1/4 : 2 : 1),
             (5/4 : -2 : 1), (5/4 : -1 : 1), (5/4 : 0 : 1), (5/4 : 1 : 1), (5/4 : 2 : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(33)
            sage: PS.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 - 71/48*y^2, y^2])
            sage: sorted(f.all_preperiodic_points())    # long time
            [(-1/12*w - 1 : 1),
             (-1/6*w - 1/4 : 1),
             (-1/12*w - 1/2 : 1),
             (-1/6*w + 1/4 : 1),
             (1/12*w - 1 : 1),
             (1/12*w - 1/2 : 1),
             (-1/12*w + 1/2 : 1),
             (-1/12*w + 1 : 1),
             (1/6*w - 1/4 : 1),
             (1/12*w + 1/2 : 1),
             (1 : 0),
             (1/6*w + 1/4 : 1),
             (1/12*w + 1 : 1)]
        """
    def rational_preperiodic_graph(self, **kwds):
        """
        Determine the directed graph of the rational preperiodic points
        for this dynamical system.

        The map must be defined over `\\QQ` and be an endomorphism of
        projective space. If this map is a polynomial endomorphism of
        `\\mathbb{P}^1`, i.e. has a totally ramified fixed point, then
        the base ring can be an absolute number field.
        This is done by passing to the Weil restriction.

        ALGORITHM:

        - Determines the list of possible periods.

        - Determines the rational periodic points from the possible periods.

        - Determines the rational preperiodic points from the rational
          periodic points by determining rational preimages.

        INPUT: keyword arguments:

        - ``prime_bound`` -- (default: ``[1, 20]``) a pair (list or tuple)
          of positive integers that represent the limits of primes to use
          in the reduction step or an integer that represents the upper bound

        - ``lifting_prime`` -- (default: 23) a prime integer; specifies
          modulo which prime to try and perform the lifting

        - ``periods`` -- (optional) a list of positive integers that is
          the list of possible periods

        - ``bad_primes`` -- (optional) a list or tuple of integer primes;
          the primes of bad reduction

        - ``ncpus`` -- (default: all cpus) number of cpus to use in parallel

        OUTPUT:

        A digraph representing the orbits of the rational preperiodic
        points in projective space.

        EXAMPLES::

            sage: PS.<x,y> = ProjectiveSpace(1,QQ)
            sage: f = DynamicalSystem_projective([7*x^2 - 28*y^2, 24*x*y])
            sage: f.rational_preperiodic_graph()                                        # needs sage.rings.function_field
            Looped digraph on 12 vertices

        ::

            sage: PS.<x,y> = ProjectiveSpace(1,QQ)
            sage: f = DynamicalSystem_projective([-3/2*x^3 + 19/6*x*y^2, y^3])
            sage: f.rational_preperiodic_graph(prime_bound=[1,8])                       # needs sage.rings.function_field
            Looped digraph on 12 vertices

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(2,QQ)
            sage: f = DynamicalSystem_projective([2*x^3 - 50*x*z^2 + 24*z^3,
            ....:                                 5*y^3 - 53*y*z^2 + 24*z^3, 24*z^3])
            sage: f.rational_preperiodic_graph(prime_bound=[1,11],  # long time
            ....:                              lifting_prime=13)
            Looped digraph on 30 vertices

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(-3)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2])
            sage: f.rational_preperiodic_graph()        # long time
            Looped digraph on 5 vertices
        """
    def connected_rational_component(self, P, n: int = 0):
        """
        Compute the connected component of a rational preperiodic
        point ``P`` by this dynamical system.

        Will work for non-preperiodic points if ``n`` is positive.
        Otherwise this will not terminate.

        INPUT:

        - ``P`` -- a rational preperiodic point of this map

        - ``n`` -- (default: 0) integer; maximum distance from ``P`` to
          branch out; a value of 0 indicates no bound

        OUTPUT: list of points connected to ``P`` up to the specified distance

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(x^3 + 1/4*x^2 - 41/16*x + 23/64)
            sage: PS.<x,y> = ProjectiveSpace(1,K)
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2])
            sage: P = PS([w,1])
            sage: sorted(f.connected_rational_component(P), key=str)
            [(-w - 1/2 : 1),
             (-w : 1),
             (-w^2 + 21/16 : 1),
             (-w^2 + 29/16 : 1),
             (-w^2 - w + 25/16 : 1),
             (-w^2 - w + 33/16 : 1),
             (w + 1/2 : 1),
             (w : 1),
             (w^2 + w - 25/16 : 1),
             (w^2 + w - 33/16 : 1),
             (w^2 - 21/16 : 1),
             (w^2 - 29/16 : 1)]

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(2,QQ)
            sage: f = DynamicalSystem_projective([x^2 - 21/16*z^2, y^2 - 2*z^2, z^2])
            sage: P = PS([17/16, 7/4, 1])
            sage: f.connected_rational_component(P, 3)                                  # needs sage.rings.function_field
            [(17/16 : 7/4 : 1),
             (-47/256 : 17/16 : 1),
             (-83807/65536 : -223/256 : 1),
             (-17/16 : -7/4 : 1),
             (-17/16 : 7/4 : 1),
             (17/16 : -7/4 : 1),
             (1386468673/4294967296 : -81343/65536 : 1),
             (-47/256 : -17/16 : 1),
             (47/256 : -17/16 : 1),
             (47/256 : 17/16 : 1),
             (-1/2 : -1/2 : 1),
             (-1/2 : 1/2 : 1),
             (1/2 : -1/2 : 1),
             (1/2 : 1/2 : 1)]
        """
    def conjugating_set(self, other, R=None, num_cpus: int = 2):
        """
        Return the set of elements in PGL over the base ring
        that conjugates one dynamical system to the other.

        Given two nonconstant rational functions of equal degree,
        determine if there is a rational element of PGL that
        conjugates one rational function to another.

        The optional argument `R` specifies the field of definition
        of the PGL elements. The set is determined
        by taking the fixed points of one map and mapping
        them to permutations of the fixed points of the other map.
        As conjugacy preserves the multipliers as a set, fixed points
        are only mapped to fixed points with the same multiplier.
        If there are not enough fixed points the
        function compares the mapping between rational preimages of
        fixed points and the rational preimages of the preimages of
        fixed points until there are enough points; such that there
        are `n+2` points with all `n+1` subsets linearly independent.

        .. WARNING::

           For degree 1 maps that are conjugate, there is a positive dimensional
           set of conjugations. This function returns only one such element.

        ALGORITHM:

        Implementing invariant set algorithm from the paper [FMV2014]_.
        Uses the set of  `n` th preimages of fixed points, as this set is
        invariant under conjugation to find all elements of PGL that
        take one set to another. Additionally, keeps track of multiplier
        information to reduce the necessary combinatorics.

        INPUT:

        - ``other`` -- a rational function of same degree
          as this map

        - ``R`` -- a field or embedding

        - ``num_cpus`` -- (default: 2) the number of threads to run in parallel;
          increasing ``num_cpus`` can potentially greatly speed up this function

        OUTPUT: set of conjugating `n+1` by `n+1` matrices

        AUTHORS:

        - Original algorithm written by Xander Faber, Michelle Manes,
          Bianca Viray [FMV2014]_.

        - Implemented by Rebecca Lauren Miller as part of GSOC 2016.

        - Algorithmic improvement by Alexander Galarraga as part of GSOC 2021.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: m = matrix(QQbar, 2, 2, [-1, 3, 2, 1])
            sage: g = f.conjugate(m)
            sage: f.conjugating_set(g)
            [
            [-1  3]
            [ 2  1]
            ]

        Increasing ``num_cpus`` can speed up computation::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2, w^2])
            sage: len(f.conjugating_set(f, num_cpus=3))                                 # needs sage.rings.function_field
            24

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(-1)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: m = matrix(K, 2, 2, [1, 1, 2, 1])
            sage: g = f.conjugate(m)
            sage: sorted(f.conjugating_set(g))
            [
            [-1 -1]  [1 1]
            [ 2  1], [2 1]
            ]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: D8 = DynamicalSystem_projective([y^3, x^3])
            sage: sorted(D8.conjugating_set(D8))
            [
            [-1  0]  [-i  0]  [ 0 -1]  [ 0 -i]  [0 i]  [0 1]  [i 0]  [1 0]
            [ 0  1], [ 0  1], [ 1  0], [ 1  0], [1 0], [1 0], [0 1], [0 1]
            ]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: D8 = DynamicalSystem_projective([y^2, x^2])
            sage: D8.conjugating_set(D8)                                                # needs sage.rings.function_field
            Traceback (most recent call last):
            ...
            ValueError: no more rational preimages;
            try extending the base field and trying again

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(7), 1)
            sage: D6 = DynamicalSystem_projective([y^2, x^2])
            sage: sorted(D6.conjugating_set(D6))                                        # needs sage.rings.function_field
            [
            [0 1]  [0 2]  [0 4]  [1 0]  [2 0]  [4 0]
            [1 0], [1 0], [1 0], [0 1], [0 1], [0 1]
            ]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([x^2 + x*z, y^2, z^2])
            sage: f.conjugating_set(f)                                                  # needs sage.rings.function_field
            [
            [1 0 0]
            [0 1 0]
            [0 0 1]
            ]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: R = P.coordinate_ring()
            sage: f = DynamicalSystem_projective([R(3), R(4)])
            sage: g = DynamicalSystem_projective([R(5), R(2)])
            sage: m = f.conjugating_set(g)[0]
            sage: f.conjugate(m) == g
            True

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([7*x + 12*y, 8*x])
            sage: g = DynamicalSystem_projective([1645*x - 318*y, 8473*x - 1638*y])
            sage: m = f.conjugating_set(g)[0]
            sage: f.conjugate(m) == g
            True

        note that only one possible conjugation is returned::

            sage: P.<x,y,z> = ProjectiveSpace(GF(11), 2)
            sage: f = DynamicalSystem_projective([2*x + 12*y, 11*y + 2*z, x + z])
            sage: m1 = matrix(GF(11), 3, 3, [1,4,1,0,2,1,1,1,1])
            sage: g = f.conjugate(m1)
            sage: f.conjugating_set(g)
            [
            [ 1  0  0]
            [ 9  1  4]
            [ 4 10  8]
            ]

        ::

            sage: # needs sage.rings.number_field
            sage: L.<v> = CyclotomicField(8)
            sage: P.<x,y,z> = ProjectiveSpace(L, 2)
            sage: f = DynamicalSystem_projective([2*x + 12*y, 11*y + 2*z, x + z])
            sage: m1 = matrix(L, 3, 3, [1,4,v^2,0,2,1,1,1,1])
            sage: g = f.conjugate(m1)
            sage: m = f.conjugating_set(g)[0]   # long time
            sage: f.conjugate(m) == g           # long time
            True

        TESTS:

        Make sure the caching problem is fixed, see #28070 ::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: m = matrix(QQ, 2, 2, [-1, 3, 2, 1])
            sage: g = f.conjugate(m)
            sage: f.conjugating_set(g)                                                  # needs sage.rings.function_field
            [
            [-1  3]
            [ 2  1]
            ]
            sage: f = f.change_ring(K)
            sage: g = g.change_ring(K)
            sage: f.conjugating_set(g)                                                  # needs sage.rings.function_field
            [
            [-1  3]
            [ 2  1]
            ]
        """
    def is_conjugate(self, other, R=None, num_cpus: int = 2):
        """
        Return whether two dynamical systems are conjugate over their
        base ring (by default) or over the ring `R` entered as an
        optional parameter.

        ALGORITHM:

        Implementing invariant set algorithm from the paper [FMV2014]_.
        Uses the set of  `n` th preimages of fixed points, as this set is
        invariant under conjugation to find all elements of PGL that
        take one set to another. Additionally, keeps track of multiplier
        information to reduce the necessary combinatorics.

        INPUT:

        - ``other`` -- a nonconstant rational function of the same
          degree as this map

        - ``R`` -- a field or embedding

        - ``num_cpus`` -- (default: 2) the number of threads to run in parallel;
          increasing ``num_cpus`` can potentially greatly speed up this function

        OUTPUT: boolean

        AUTHORS:

        - Original algorithm written by Xander Faber, Michelle Manes,
          Bianca Viray [FMV2014]_.

        - Implemented by Rebecca Lauren Miller as part of GSOC 2016.

        - Algorithmic improvement by Alexander Galarraga as part of GSOC 2021.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<w> = CyclotomicField(3)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: D8 = DynamicalSystem_projective([y^2, x^2])
            sage: D8.is_conjugate(D8)
            True

        We can speed up computation by increasing ``num_cpus``::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ,3)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2, w^2])
            sage: f.is_conjugate(f, num_cpus=2)                                         # needs sage.rings.function_field
            True

        ::

            sage: # needs sage.rings.number_field
            sage: set_verbose(None)
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y, y^2])
            sage: m = matrix(QQbar, 2, 2, [1, 1, 2, 1])
            sage: g = f.conjugate(m)
            sage: f.is_conjugate(g)
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(5), 1)
            sage: f = DynamicalSystem_projective([x^3 + x*y^2, y^3])
            sage: m = matrix(GF(5), 2, 2, [1, 3, 2, 9])
            sage: g = f.conjugate(m)
            sage: f.is_conjugate(g)                                                     # needs sage.rings.number_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y, y^2])
            sage: g = DynamicalSystem_projective([x^3 + x^2*y, y^3])
            sage: f.is_conjugate(g)
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + x*y, y^2])
            sage: g = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: f.is_conjugate(g)                                                     # needs sage.rings.number_field
            False

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: f = DynamicalSystem_projective([7*x + 12*y, 8*x])
            sage: g = DynamicalSystem_projective([1645*x - 318*y, 8473*x - 1638*y])
            sage: f.is_conjugate(g)
            True

        Conjugation is only checked over the base field by default::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([-3*y^2, 3*x^2])
            sage: g = DynamicalSystem_projective([-x^2 - 2*x*y, 2*x*y + y^2])
            sage: f.is_conjugate(g), f.is_conjugate(g, R=QQbar)                         # needs sage.rings.number_field
            (False, True)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([7*x + 12*y, 8*y + 2*z, x + z])
            sage: m1 = matrix(QQ, 3, 3, [1,4,1,0,2,1,1,1,1])
            sage: g = f.conjugate(m1)
            sage: f.is_conjugate(g)
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: f = DynamicalSystem_projective([2*x + 12*y, 11*y + 2*z, x + z])
            sage: m1 = matrix(GF(7), 3, 3, [1,4,1,0,2,1,1,1,1])
            sage: g = f.conjugate(m1)
            sage: f.is_conjugate(g)
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([2*x^2 + 12*y*x, 11*y*x + 2*y^2, x^2 + z^2])
            sage: m1 = matrix(QQ, 3, 3, [1,4,1,0,2,1,1,1,1])
            sage: g = f.conjugate(m1)
            sage: f.is_conjugate(g)
            True

        TESTS:

        Make sure the caching problem is fixed, see #28070 ::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(5)
            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: m = matrix(QQ, 2, 2, [-1, 3, 2, 1])
            sage: g = f.conjugate(m)
            sage: f.is_conjugate(g)
            True
            sage: f = f.change_ring(K)
            sage: g = g.change_ring(K)
            sage: f.is_conjugate(g)
            True
        """
    def is_polynomial(self):
        """
        Check to see if the dynamical system has a totally ramified
        fixed point.

        The function must be defined over an absolute number field or a
        finite field.

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = QuadraticField(7)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x**2 + 2*x*y - 5*y**2, 2*x*y])
            sage: f.is_polynomial()
            False

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = QuadraticField(7)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x**2 - 7*x*y, 2*y**2])
            sage: m = matrix(K, 2, 2, [w, 1, 0, 1])
            sage: f = f.conjugate(m)
            sage: f.is_polynomial()
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(4/27)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x**3 + w*y^3, x*y**2])
            sage: f.is_polynomial()
            False

        ::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(3**2, prefix='w')
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x**2 + K.gen()*y**2, x*y])
            sage: f.is_polynomial()
            False

        ::

            sage: PS.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([6*x^2 + 12*x*y + 7*y^2, 12*x*y + 42*y^2])
            sage: f.is_polynomial()
            False

        TESTS:

        See :issue:`25242`::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem([x^2 + y^2, x*y])
            sage: F2 = F.conjugate(matrix(QQ,2,2, [1,2,3,5]))
            sage: F2.is_polynomial()                                                    # needs sage.libs.pari
            False
        """
    def normal_form(self, return_conjugation: bool = False):
        """
        Return a normal form in the moduli space of dynamical systems.

        Currently implemented only for polynomials. The totally ramified
        fixed point is moved to infinity and the map is conjugated to the form
        `x^n + a_{n-2} x^{n-2} + \\cdots + a_{0}`. Note that for finite fields
        we can only remove the `(n-1)`-st term when the characteristic
        does not divide `n`.

        INPUT:

        - ``return_conjugation`` -- boolean (default: ``False``); if ``True``,
          then return the conjugation element of PGL along with the embedding
          into the new field

        OUTPUT:

        - :class:`SchemeMorphism_polynomial`

        - (optional) an element of PGL as a matrix

        - (optional) the field embedding

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^2 + 2*x*y - 5*x^2, 2*x*y])
            sage: f.normal_form()
            Traceback (most recent call last):
            ...
            NotImplementedError: map is not a polynomial

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<w> = NumberField(x^2 - 5)
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^2 + w*x*y, y^2])
            sage: g,m,psi = f.normal_form(return_conjugation=True); m
            [     1 -1/2*w]
            [     0      1]
            sage: f.change_ring(psi).conjugate(m) == g
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([13*x^2 + 4*x*y + 3*y^2, 5*y^2])
            sage: f.normal_form()                                                       # needs sage.libs.pari
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (5*x^2 + 9*y^2 : 5*y^2)

        ::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(3^3, prefix='w')
            sage: P.<x,y> = ProjectiveSpace(K,1)
            sage: f = DynamicalSystem_projective([x^3 + 2*x^2*y + 2*x*y^2 + K.gen()*y^3, y^3])
            sage: f.normal_form()
            Dynamical System of Projective Space of dimension 1
             over Finite Field in w3 of size 3^3
              Defn: Defined on coordinates by sending (x : y) to
                    (x^3 + x^2*y + x*y^2 + (-w3)*y^3 : y^3)

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(3),1)
            sage: f = DynamicalSystem_projective([2*x**3 + x**2*y, y**3])
            sage: g,m,psi = f.normal_form(return_conjugation=True); psi                 # needs sage.rings.finite_rings
            Ring morphism:
              From: Finite Field of size 3
              To:   Finite Field in z2 of size 3^2
              Defn: 1 |--> 1

        Fixes :issue:`38012` by not forcing univariate polynomial to be univariate::

            sage: R.<z> = PolynomialRing(QQ)
            sage: f = DynamicalSystem_affine(z^2 + z + 1).homogenize(1)
            sage: f.normal_form()
            Dynamical System of Projective Space of dimension 1 over Rational Field
             Defn: Defined on coordinates by sending (x0 : x1) to
                   (x0^2 + 5/4*x1^2 : x1^2)
        """
    def potential_good_reduction(self, prime, return_conjugation: bool = False):
        """
        Return ``True`` if this dynamical system has potential good reduction at ``prime``.

        A dynamical system has good reduction at ``prime`` if after the coefficients
        are reduced modulo ``prime`` the degree remains the same. A dynamical system
        `f` has `\\textit{potential}` good reduction if there exists
        `\\phi \\in PGL(n,\\overline{K})` such that `\\phi^{-1} \\circ f \\circ \\phi`
        has good reduction.

        If this dynamical system `f` has potential good reduction at ``prime``,
        a dynamical system `g = \\phi^{-1} \\circ f \\circ \\phi` which has good
        reduction at ``prime`` is returned.

        This dynamical system must have as its domain `\\mathbb{P}^1(K)`, where
        `K` is a number field.

        INPUT:

        - ``prime`` -- a prime ideal of the field of definition of the fixed
          points of the map, or a prime number in `\\QQ` if the field of definition
          of the fixed points is `\\QQ`.

        - ``return_conjugation`` -- boolean (default: ``False``); if set to ``True``,
          the `PGL_2` map used to achieve good reduction will be returned

        OUTPUT: a tuple:

        - The first element is:
          - ``False`` if this dynamical system does not have potential good reduction.
          - ``True`` if this dynamical system does have potential good reduction.

        - The second element is:
          - ``None`` if this dynamical system does not have potential good reduction.
          - A dynamical system with good reduction at ``prime`` otherwise.

        - If ``return_conjugation`` is ``True``, then the tuple will have a third element, which is:
          - ``None`` if this dynamical system does not have potential good reduction.
          - The `PGL_2` map used to achieve good reduction otherwise.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: system = DynamicalSystem_projective([x^2 - y^2, 2*x*y])
            sage: prime = system.field_of_definition_periodic(1).prime_above(2)
            sage: new_system = system.potential_good_reduction(prime)[1]
            sage: new_system
            Dynamical System of Projective Space of dimension 1 over Number Field
             in a with defining polynomial x^2 + 1
              Defn: Defined on coordinates by sending (x : y) to
                    ((-1/2*a)*x^2 + (-5/2*a)*y^2 : (-a)*x*y + y^2)

        Note that this map has good reduction at 2::

            sage: new_system.resultant()                                                # needs sage.rings.number_field
            1

        Using ``return_conjugation``, we can get the conjugation that achieves good reduction::

            sage: conj = system.potential_good_reduction(prime, True)[2]; conj          # needs sage.rings.number_field
            [-1/2*a    1/2]
            [     0      1]

        We can check that this conjugation achieves good reduction::

            sage: system.conjugate(conj).resultant()                                    # needs sage.rings.number_field
            1

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: system = DynamicalSystem_projective([3^4*x^3 + 3*x*y^2 + y^3, 3^6*y^3])
            sage: prime = system.field_of_definition_periodic(1).prime_above(3)         # needs sage.rings.number_field
            sage: system.potential_good_reduction(prime)                                # needs sage.rings.number_field
            (False, None)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: system = DynamicalSystem_projective([x^5 - x*y^4, 5*y^5])
            sage: prime = system.field_of_definition_periodic(1).prime_above(5)         # needs sage.rings.number_field
            sage: system.potential_good_reduction(prime)                                # needs sage.rings.number_field
            (False, None)

        TESTS::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: R.<z> = QQ[]
            sage: A.<a> = NumberField(z^2 + 1)
            sage: prime = A.prime_above(2)
            sage: system = DynamicalSystem_projective([x^2 - y^2, 2*x*y])
            sage: system.potential_good_reduction(prime)
            (True,
             Dynamical System of Projective Space of dimension 1 over
              Number Field in a with defining polynomial x^2 + 1
               Defn: Defined on coordinates by sending (x : y) to
                     ((-1/2*a)*x^2 + (-5/2*a)*y^2 : (-a)*x*y + y^2))

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: system = DynamicalSystem_projective([3^5*x^3 + x^2*y - 3^5*x*y^2,
            ....:                                      -3^5*x^2*y + x*y^2 + 3^5*y^3])
            sage: system.potential_good_reduction(3, return_conjugation=True)  # long time
            (False, None, None)

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: system = DynamicalSystem_projective([x**5 - 11*y**5, x**4*y])
            sage: B, new_sys, conj = system.potential_good_reduction(11, True)
            sage: system.conjugate(conj).resultant() == 1
            True
            sage: system.conjugate(conj) == new_sys
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: system = DynamicalSystem_projective([3*x^2 + x*y + y^2, 9*y^2])
            sage: prime = system.field_of_definition_periodic(1).prime_above(3)         # needs sage.rings.number_field
            sage: system.potential_good_reduction(prime)                                # needs sage.rings.number_field
            (False, None)
        """
    def reduce_base_field(self):
        """
        Return this map defined over the field of definition of the coefficients.

        The base field of the map could be strictly larger than
        the field where all of the coefficients are defined. This function
        reduces the base field to the minimal possible. This can be done when
        the base ring is a number field, QQbar, a finite field, or algebraic
        closure of a finite field.

        OUTPUT: a dynamical system

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = GF(2^3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2, z^2+z*y])
            sage: f.reduce_base_field()
            Dynamical System of Projective Space of dimension 2 over Finite Field of size 2
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^2 + y^2 : y^2 : y*z + z^2)

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
            sage: f = DynamicalSystem_projective([x^2 + QQbar(sqrt(3))*y^2,
            ....:                                 y^2, QQbar(sqrt(2))*z^2])
            sage: f.reduce_base_field()
            Dynamical System of Projective Space of dimension 2 over Number Field in a
             with defining polynomial y^4 - 4*y^2 + 1 with a = -0.5176380902050415?
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^2 + (-a^2 + 2)*y^2 : y^2 : (a^3 - 3*a)*z^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<v> = NumberField(x^3 - 2, embedding=(x^3 - 2).roots(ring=CC)[0][0])
            sage: R.<x> = QQ[]
            sage: L.<w> = NumberField(x^6 + 9*x^4 - 4*x^3 + 27*x^2 + 36*x + 31,
            ....:                     embedding=(x^6 + 9*x^4 - 4*x^3
            ....:                                 + 27*x^2 + 36*x + 31).roots(ring=CC)[0][0])
            sage: P.<x,y> = ProjectiveSpace(L,1)
            sage: f = DynamicalSystem([L(v)*x^2 + y^2, x*y])
            sage: f.reduce_base_field().base_ring().is_isomorphic(K)
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = CyclotomicField(5)
            sage: A.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([3*x^2 + y^2, x*y])
            sage: f.reduce_base_field()
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (3*x^2 + y^2 : x*y)
        """
    def is_newton(self, return_conjugation: bool = False):
        """
        Return whether ``self`` is a Newton map.

        A map `g` is *Newton* if it is conjugate to a map of the form
        `f(z) = z - \\frac{p(z)}{p'(z)}` after dehomogenization,
        where `p(z)` is a squarefree polynomial.

        INPUT:

        - ``return_conjugation`` -- boolean (default: ``False``); if the map is Newton
          and ``True``, then return the conjugation that moves this map to
          the above form

        OUTPUT:

        A boolean. If ``return_conjugation`` is ``True``, then this also
        returns the conjugation as a matrix if ``self`` is Newton or ``None``
        otherwise.

        The conjugation may be defined over an extension if the map has
        fixed points not defined over the base field.

        EXAMPLES::

            sage: A.<z> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem_affine([z - (z^2 + 1)/(2*z)])
            sage: F = f.homogenize(1)
            sage: F.is_newton(return_conjugation=True)                                  # needs sage.rings.number_field
            (
                  [1 0]
            True, [0 1]
            )

        ::

            sage: A.<z> = AffineSpace(QQ, 1)
            sage: f = DynamicalSystem_affine([z^2 + 1])
            sage: F = f.homogenize(1)
            sage: F.is_newton()                                                         # needs sage.rings.number_field
            False
            sage: F.is_newton(return_conjugation=True)                                  # needs sage.rings.number_field
            (False, None)

        ::

            sage: PP.<x,y> = ProjectiveSpace(QQ, 1)
            sage: F = DynamicalSystem_projective([-4*x^3 - 3*x*y^2, -2*y^3])
            sage: F.is_newton(return_conjugation=True)[1]                               # needs sage.rings.number_field
            [   0    1]
            [-4*a  2*a]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<zeta> = CyclotomicField(2*4)
            sage: A.<z> = AffineSpace(K, 1)
            sage: f = DynamicalSystem_affine(z-(z^3+zeta*z)/(3*z^2+zeta))
            sage: F = f.homogenize(1)
            sage: F.is_newton()
            True
        """

class DynamicalSystem_projective_finite_field(DynamicalSystem_projective_field, SchemeMorphism_polynomial_projective_space_finite_field):
    def is_postcritically_finite(self, **kwds):
        """
        Every point is postcritically finite in a finite field.

        INPUT: None. ``kwds`` is to parallel the overridden function

        OUTPUT: the boolean ``True``

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5),2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2, z^2 + y*z], domain=P)
            sage: f.is_postcritically_finite()
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(13),1)
            sage: f = DynamicalSystem_projective([x^4 - x^2*y^2 + y^4, y^4])
            sage: f.is_postcritically_finite(use_algebraic_closure=False)
            True
        """
    def orbit_structure(self, P):
        """
        Return the pair ``(m,n)``, where ``m`` is the preperiod and ``n``
        is the period of the point ``P`` by this dynamical system.

        Every point is preperiodic over a finite field so every point
        will be preperiodic.

        INPUT:

        - ``P`` -- a point in the domain of this map

        OUTPUT: a tuple ``(m,n)`` of integers

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5),2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2, z^2 + y*z], domain=P)
            sage: f.orbit_structure(P(2,1,2))
            (0, 6)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(7),2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2], domain=X)
            sage: f.orbit_structure(X(1,1,2))                                           # needs sage.rings.function_field
            (0, 2)

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(13),1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2], domain=P)
            sage: f.orbit_structure(P(3,4))
            (2, 3)

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = GF(13^3)
            sage: P.<x,y> = ProjectiveSpace(R,1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2], domain=P)
            sage: f.orbit_structure(P(t, 4))
            (11, 6)
        """
    def cyclegraph(self):
        """
        Return the digraph of all orbits of this dynamical system.

        Over a finite field this is a finite graph. For subscheme domains, only points
        on the subscheme whose image are also on the subscheme are in the digraph.

        OUTPUT: a digraph

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(GF(13),1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 14 vertices

        ::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(3^2,'t'),2)
            sage: f = DynamicalSystem_projective([x^2 + y^2, y^2, z^2 + y*z])
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 91 vertices

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(7),2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2], domain=X)
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 15 vertices

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(3),2)
            sage: f = DynamicalSystem_projective([x*z - y^2, x^2 - y^2, y^2 - z^2])
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 13 vertices

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(3),2)
            sage: X = P.subscheme([x - y])
            sage: f = DynamicalSystem_projective([x^2 - y^2, x^2 - y^2, y^2 - z^2], domain=X)
            sage: f.cyclegraph()                                                        # needs sage.graphs
            Looped digraph on 4 vertices
        """
    def possible_periods(self, return_points: bool = False):
        """
        Return the list of possible minimal periods of a periodic point
        over `\\QQ` and (optionally) a point in each cycle.

        ALGORITHM:

        See [Hutz2009]_.

        INPUT:

        - ``return_points`` -- boolean (default: ``False``); if ``True``,
          then return the points as well as the possible periods

        OUTPUT:

        A list of positive integers, or a list of pairs of projective
        points and periods if ``return_points`` is ``True``.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(GF(23),1)
            sage: f = DynamicalSystem_projective([x^2 - 2*y^2, y^2])
            sage: f.possible_periods()                                                  # needs sage.libs.pari
            [1, 5, 11, 22, 110]

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(13),1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: sorted(f.possible_periods(True))                                      # needs sage.libs.pari
            [[(0 : 1), 2], [(1 : 0), 1], [(3 : 1), 3], [(3 : 1), 36]]

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(2,GF(7))
            sage: f = DynamicalSystem_projective([-360*x^3 + 760*x*z^2,
            ....:                                 y^3 - 604*y*z^2 + 240*z^3, 240*z^3])
            sage: f.possible_periods()                                                  # needs sage.libs.pari
            [1, 2, 4, 6, 12, 14, 28, 42, 84]

        .. TODO::

            - do not return duplicate points

            - improve hash to reduce memory of point-table
        """
    def automorphism_group(self, **kwds):
        """
        Return the subgroup of `PGL2` that is the automorphism group of this
        dynamical system.

        The automorphism group is the set of `PGL2` elements that fixed the map under conjugation.

        For dimension 1, see [FMV2014]_ for the algorithm.

        For dimension greater than 1, we compute the conjugating set of this
        dynamical system with itself.

        INPUT:

        The following keywords are used when the dimension of the domain
        is greater than 1:

        - ``num_cpus`` -- (default: 2) the number of threads to use; setting to a
          larger number can greatly speed up this function

        The following keywords are used when the dimension of the domain is 1:

        - ``absolute`` -- boolean (default: ``False``); if ``True``, then
          return the absolute automorphism group and a field of definition

        - ``iso_type`` -- boolean (default: ``False``); if ``True``, then
          return the isomorphism type of the automorphism group

        - ``return_functions`` -- boolean (default: ``False``); ``True``
          returns elements as linear fractional transformations and
          ``False`` returns elements as `PGL2` matrices

        OUTPUT: list of elements of the automorphism group

        AUTHORS:

        - Original algorithm written by Xander Faber, Michelle Manes,
          Bianca Viray

        - Modified by Joao Alberto de Faria, Ben Hutz, Bianca Thompson

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = ProjectiveSpace(GF(7^3,'t'),1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, x*y])
            sage: f.automorphism_group()
            [
            [1 0]  [6 0]
            [0 1], [0 1]
            ]

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = ProjectiveSpace(GF(3^2,'t'),1)
            sage: f = DynamicalSystem_projective([x^3, y^3])
            sage: lst, label = f.automorphism_group(return_functions=True,      # long time
            ....:                                   iso_type=True)
            sage: sorted(lst, key=str), label                                   # long time
            ([(2*x + 1)/(x + 1),
              (2*x + 1)/x,
              (2*x + 2)/(x + 2),
              (2*x + 2)/x,
              (x + 1)/(x + 2),
              (x + 1)/x,
              (x + 2)/(x + 1),
              (x + 2)/x,
              1/(x + 1),
              1/(x + 2),
              1/x,
              2*x,
              2*x + 1,
              2*x + 2,
              2*x/(x + 1),
              2*x/(x + 2),
              2/(x + 1),
              2/(x + 2),
              2/x,
              x,
              x + 1,
              x + 2,
              x/(x + 1),
              x/(x + 2)],
             'PGL(2,3)')

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = ProjectiveSpace(GF(2^5,'t'),1)
            sage: f = DynamicalSystem_projective([x^5, y^5])
            sage: f.automorphism_group(return_functions=True, iso_type=True)
            ([x, 1/x], 'Cyclic of order 2')

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = ProjectiveSpace(GF(3^4,'t'),1)
            sage: f = DynamicalSystem_projective([x^2 + 25*x*y + y^2, x*y + 3*y^2])
            sage: f.automorphism_group(absolute=True)
            [Univariate Polynomial Ring in w over Finite Field in b of size 3^4,
             [
             [1 0]
             [0 1]
             ]]

        ::

            sage: R.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: f = DynamicalSystem_projective([x^3 + x*z^2, y^3 + y*z^2, z^3])
            sage: all([f.conjugate(m) == f for m in f.automorphism_group()])            # needs sage.rings.function_field
            True
        """
    def all_periodic_points(self, **kwds):
        """
        Return a list of all periodic points over a finite field.

        INPUT: keyword arguments:

        - ``R`` -- (default: base ring of dynamical system) the base ring
          over which the periodic points of the dynamical system are found

        OUTPUT: list of elements which are periodic

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y> = ProjectiveSpace(GF(5^2),1)
            sage: f = DynamicalSystem_projective([x^2 + y^2, x*y])
            sage: f.all_periodic_points()
            [(1 : 0), (z2 + 2 : 1), (4*z2 + 3 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5),2)
            sage: f = DynamicalSystem_projective([x^2 + y^2 + z^2, x*y + x*z, z^2])
            sage: f.all_periodic_points()
            [(1 : 0 : 0),
             (0 : 0 : 1),
             (1 : 0 : 1),
             (2 : 1 : 1),
             (1 : 4 : 1),
             (3 : 0 : 1),
             (0 : 3 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(3), 1)
            sage: f = DynamicalSystem_projective([x^2 - y^2, y^2])
            sage: f.all_periodic_points(R=GF(3^2, 't'))                                 # needs sage.rings.finite_rings
            [(1 : 0), (0 : 1), (2 : 1), (t : 1), (2*t + 1 : 1)]
        """
