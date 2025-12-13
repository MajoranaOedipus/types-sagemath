from _typeshed import Incomplete
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.map import Map as Map
from sage.categories.modules import Modules as Modules
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.number_fields import NumberFields as NumberFields
from sage.categories.rings import Rings as Rings
from sage.misc.latex import latex as latex
from sage.modules.module import Module as Module
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic as IntegerModRing_generic
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.function_field.function_field import FunctionField as FunctionField
from sage.rings.function_field.function_field_rational import RationalFunctionField as RationalFunctionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.padics.padic_generic import pAdicGeneric as pAdicGeneric
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_quotient_ring import PolynomialQuotientRing_generic as PolynomialQuotientRing_generic
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing_generic as PowerSeriesRing_generic
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.sets.family import Family as Family
from sage.structure.element import ModuleElement as ModuleElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class RingDerivationModule(Module, UniqueRepresentation):
    """
    A class for modules of derivations over a commutative ring.
    """
    Element: Incomplete
    def __init__(self, domain, codomain, twist=None) -> None:
        """
        Initialize this module of derivation.

        TESTS::

            sage: A.<x,y> = QQ[]
            sage: M = A.derivation_module()
            sage: TestSuite(M).run()

            sage: from sage.rings.derivation import RingDerivationModule
            sage: R5.<x> = GF(5)[]
            sage: R25.<x> = GF(25)[]                                                    # needs sage.rings.finite_rings
            sage: R7.<x> = GF(7)[]

            sage: RingDerivationModule(R5, R25)                                         # needs sage.rings.finite_rings
            Module of derivations
             from Univariate Polynomial Ring in x over Finite Field of size 5
               to Univariate Polynomial Ring in x over Finite Field in z2 of size 5^2
            sage: RingDerivationModule(R5, R5^2)
            Traceback (most recent call last):
            ...
            TypeError: the codomain must be an algebra over the domain
             or a morphism with the correct domain
            sage: RingDerivationModule(R5, R7)                                          # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: the codomain must be an algebra over the domain
             or a morphism with the correct domain

            sage: theta = R5.hom([R5.gen()^2])
            sage: RingDerivationModule(R5, R25, twist=theta)                            # needs sage.rings.finite_rings
            Module of twisted derivations
             from Univariate Polynomial Ring in x over Finite Field of size 5
               to Univariate Polynomial Ring in x over Finite Field in z2 of size 5^2
             (twisting morphism: x |--> x^2)
            sage: RingDerivationModule(R7, R7, twist=theta)                             # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: the domain of the derivation must coerce to the domain of the twisting homomorphism
        """
    def __hash__(self):
        """
        Return a hash of ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module()
            sage: hash(M) == hash((M.domain(), M.codomain(), M.twisting_morphism()))
            True
        """
    def domain(self):
        """
        Return the domain of the derivations in this module.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module(); M
            Module of derivations over Multivariate Polynomial Ring in x, y over Integer Ring
            sage: M.domain()
            Multivariate Polynomial Ring in x, y over Integer Ring
        """
    def codomain(self):
        """
        Return the codomain of the derivations in this module.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module(); M
            Module of derivations over Multivariate Polynomial Ring in x, y over Integer Ring
            sage: M.codomain()
            Multivariate Polynomial Ring in x, y over Integer Ring
        """
    def defining_morphism(self):
        """
        Return the morphism defining the structure of algebra
        of the codomain over the domain.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: M = R.derivation_module()
            sage: M.defining_morphism()
            Identity endomorphism of Univariate Polynomial Ring in x over Rational Field

            sage: S.<y> = R[]
            sage: M = R.derivation_module(S)
            sage: M.defining_morphism()
            Polynomial base injection morphism:
              From: Univariate Polynomial Ring in x over Rational Field
              To:   Univariate Polynomial Ring in y over
                     Univariate Polynomial Ring in x over Rational Field

            sage: ev = R.hom([QQ(0)])
            sage: M = R.derivation_module(ev)
            sage: M.defining_morphism()
            Ring morphism:
              From: Univariate Polynomial Ring in x over Rational Field
              To:   Rational Field
              Defn: x |--> 0
        """
    def twisting_morphism(self):
        """
        Return the twisting homomorphism of the derivations in this module.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: theta = R.hom([y,x])
            sage: M = R.derivation_module(twist=theta); M
            Module of twisted derivations over Multivariate Polynomial Ring in x, y
             over Integer Ring (twisting morphism: x |--> y, y |--> x)
            sage: M.twisting_morphism()
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> y
                    y |--> x

        When the derivations are untwisted, this method returns nothing::

            sage: M = R.derivation_module()
            sage: M.twisting_morphism()
        """
    def ngens(self):
        """
        Return the number of generators of this module of derivations.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module(); M
            Module of derivations over Multivariate Polynomial Ring in x, y over Integer Ring
            sage: M.ngens()
            2

        Indeed, generators are::

            sage: M.gens()
            (d/dx, d/dy)

        We check that, for a nontrivial twist over a field, the module of
        twisted derivation is a vector space of dimension 1 generated by
        ``twist - id``::

            sage: K = R.fraction_field()
            sage: theta = K.hom([K(y),K(x)])
            sage: M = K.derivation_module(twist=theta); M
            Module of twisted derivations over Fraction Field of Multivariate Polynomial
             Ring in x, y over Integer Ring (twisting morphism: x |--> y, y |--> x)
            sage: M.ngens()
            1
            sage: M.gen()
            [x |--> y, y |--> x] - id
        """
    def gens(self) -> tuple:
        """
        Return the generators of this module of derivations.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module(); M
            Module of derivations over Multivariate Polynomial Ring in x, y over Integer Ring
            sage: M.gens()
            (d/dx, d/dy)

        We check that, for a nontrivial twist over a field, the module of
        twisted derivation is a vector space of dimension 1 generated by
        ``twist - id``::

            sage: K = R.fraction_field()
            sage: theta = K.hom([K(y),K(x)])
            sage: M = K.derivation_module(twist=theta); M
            Module of twisted derivations over Fraction Field of Multivariate Polynomial
             Ring in x, y over Integer Ring (twisting morphism: x |--> y, y |--> x)
            sage: M.gens()
            ([x |--> y, y |--> x] - id,)
        """
    def gen(self, n: int = 0):
        """
        Return the `n`-th generator of this module of derivations.

        INPUT:

        - ``n`` -- integer (default: `0`)

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module(); M
            Module of derivations over Multivariate Polynomial Ring in x, y over Integer Ring
            sage: M.gen()
            d/dx
            sage: M.gen(1)
            d/dy
        """
    def basis(self):
        """
        Return a basis of this module of derivations.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)
        """
    def dual_basis(self):
        """
        Return the dual basis of the canonical basis of this module of
        derivations (which is that returned by the method :meth:`basis`).

        .. NOTE::

            The dual basis of `(d_1, \\dots, d_n)` is a family
            `(x_1, \\ldots, x_n)` of elements in the domain such
            that `d_i(x_i) = 1` and `d_i(x_j) = 0` if `i \\neq j`.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)
            sage: M.dual_basis()
            Family (x, y)
        """
    def ring_of_constants(self):
        """
        Return the subring of the domain consisting of elements
        `x` such that `d(x) = 0` for all derivation `d` in this module.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: M = R.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)
            sage: M.ring_of_constants()
            Rational Field
        """
    def random_element(self, *args, **kwds):
        """
        Return a random derivation in this module.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module()
            sage: M.random_element()  # random
            (x^2 + x*y - 3*y^2 + x + 1)*d/dx + (-2*x^2 + 3*x*y + 10*y^2 + 2*x + 8)*d/dy
        """
    def some_elements(self):
        """
        Return a list of elements of this module.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: M = R.derivation_module()
            sage: M.some_elements()
            [d/dx, d/dy, x*d/dx, x*d/dy, y*d/dx, y*d/dy]
        """

class RingDerivation(ModuleElement):
    """
    An abstract class for twisted and untwisted derivations over
    commutative rings.

    TESTS::

        sage: R.<x,y> = ZZ[]
        sage: f = R.derivation(x) + 2*R.derivation(y); f
        d/dx + 2*d/dy
        sage: f(x*y)
        2*x + y
    """
    def __call__(self, x):
        """
        Return the image of ``x`` under this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = x*R.derivation(x) + y*R.derivation(y)
            sage: f(x^2 + 3*x*y - y^2)
            2*x^2 + 6*x*y - 2*y^2
        """
    def domain(self):
        """
        Return the domain of this derivation.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = R.derivation(y); f
            d/dy
            sage: f.domain()
            Multivariate Polynomial Ring in x, y over Rational Field
            sage: f.domain() is R
            True
        """
    def codomain(self):
        """
        Return the codomain of this derivation.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: f = R.derivation(); f
            d/dx
            sage: f.codomain()
            Univariate Polynomial Ring in x over Rational Field
            sage: f.codomain() is R
            True

        ::

            sage: S.<y> = R[]
            sage: M = R.derivation_module(S)
            sage: M.random_element().codomain()
            Univariate Polynomial Ring in y over
             Univariate Polynomial Ring in x over Rational Field
            sage: M.random_element().codomain() is S
            True
        """

class RingDerivationWithoutTwist(RingDerivation):
    """
    An abstract class for untwisted derivations.
    """
    def list(self):
        """
        Return the list of coefficient of this derivation
        on the canonical basis.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: M = R.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)

            sage: R.derivation(x).list()
            [1, 0]
            sage: R.derivation(y).list()
            [0, 1]

            sage: f = x*R.derivation(x) + y*R.derivation(y); f
            x*d/dx + y*d/dy
            sage: f.list()
            [x, y]
        """
    def monomial_coefficients(self, copy=None):
        """
        Return dictionary of nonzero coordinates (on the canonical
        basis) of this derivation.

        More precisely, this returns a dictionary whose keys are indices
        of basis elements and whose values are the corresponding coefficients.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: M = R.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)

            sage: R.derivation(x).monomial_coefficients()
            {0: 1}
            sage: R.derivation(y).monomial_coefficients()
            {1: 1}

            sage: f = x*R.derivation(x) + y*R.derivation(y); f
            x*d/dx + y*d/dy
            sage: f.monomial_coefficients()
            {0: x, 1: y}
        """
    def is_zero(self):
        """
        Return ``True`` if this derivation is zero.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(); f
            d/dx
            sage: f.is_zero()
            False

            sage: (f-f).is_zero()
            True
        """
    def pth_power(self):
        """
        Return the `p`-th power of this derivation where `p`
        is the characteristic of the domain.

        .. NOTE::

            Leibniz rule implies that this is again a derivation.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = GF(5)[]
            sage: Dx = R.derivation(x)
            sage: Dx.pth_power()
            0
            sage: (x*Dx).pth_power()
            x*d/dx
            sage: (x^6*Dx).pth_power()
            x^26*d/dx

            sage: Dy = R.derivation(y)                                                  # needs sage.rings.finite_rings
            sage: (x*Dx + y*Dy).pth_power()                                             # needs sage.rings.finite_rings
            x*d/dx + y*d/dy

        An error is raised if the domain has characteristic zero::

            sage: R.<x,y> = QQ[]
            sage: Dx = R.derivation(x)
            sage: Dx.pth_power()
            Traceback (most recent call last):
            ...
            TypeError: the domain of the derivation must have positive and prime characteristic

        or if the characteristic is not a prime number::

            sage: R.<x,y> = Integers(10)[]
            sage: Dx = R.derivation(x)
            sage: Dx.pth_power()
            Traceback (most recent call last):
            ...
            TypeError: the domain of the derivation must have positive and prime characteristic

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = GF(3)[]
            sage: D = R.derivation_module().random_element()
            sage: Dp = D.pth_power()
            sage: f = R.random_element()
            sage: Dp(f) == D(D(D(f)))
            True

            sage: D.bracket(Dp)                                                         # needs sage.rings.finite_rings
            0
        """
    def precompose(self, morphism):
        """
        Return the derivation obtained by applying first
        ``morphism`` and then this derivation.

        INPUT:

        - ``morphism`` -- a homomorphism of rings whose codomain is
          the domain of this derivation or a ring that coerces to
          the domain of this derivation

        EXAMPLES::

            sage: A.<x> = QQ[]
            sage: B.<x,y> = QQ[]
            sage: D = B.derivation(x) - 2*x*B.derivation(y); D
            d/dx - 2*x*d/dy

        When restricting to ``A``, the term ``d/dy`` disappears
        (since it vanishes on ``A``)::

            sage: D.precompose(A)
            d/dx

        If we restrict to another well chosen subring, the derivation vanishes::

            sage: C.<t> = QQ[]
            sage: f = C.hom([x^2 + y]); f
            Ring morphism:
              From: Univariate Polynomial Ring in t over Rational Field
              To:   Multivariate Polynomial Ring in x, y over Rational Field
              Defn: t |--> x^2 + y
            sage: D.precompose(f)
            0

        Note that this method cannot be used to compose derivations::

            sage: D.precompose(D)
            Traceback (most recent call last):
            ...
            TypeError: you must give a homomorphism of rings

        TESTS::

            sage: D.precompose(C)
            Traceback (most recent call last):
            ...
            TypeError: the given ring does not coerce to the domain of the derivation
        """
    def postcompose(self, morphism):
        """
        Return the derivation obtained by applying first
        this derivation and then ``morphism``.

        INPUT:

        - ``morphism`` -- a homomorphism of rings whose domain is
          the codomain of this derivation or a ring into which the
          codomain of this derivation coerces

        EXAMPLES::

            sage: A.<x,y>= QQ[]
            sage: ev = A.hom([QQ(0), QQ(1)])
            sage: Dx = A.derivation(x)
            sage: Dy = A.derivation(y)

        We can define the derivation at `(0,1)` just by postcomposing
        with ``ev``::

            sage: dx = Dx.postcompose(ev)
            sage: dy = Dy.postcompose(ev)
            sage: f = x^2 + y^2
            sage: dx(f)
            0
            sage: dy(f)
            2

        Note that we cannot avoid the creation of the evaluation morphism:
        if we pass in ``QQ`` instead, an error is raised since there is
        no coercion morphism from ``A`` to ``QQ``::

            sage: Dx.postcompose(QQ)
            Traceback (most recent call last):
            ...
            TypeError: the codomain of the derivation does not coerce to the given ring

        Note that this method cannot be used to compose derivations::

            sage: Dx.precompose(Dy)
            Traceback (most recent call last):
            ...
            TypeError: you must give a homomorphism of rings
        """
    def extend_to_fraction_field(self):
        """
        Return the extension of this derivation to fraction fields of
        the domain and the codomain.

        EXAMPLES::

            sage: S.<x> = QQ[]
            sage: d = S.derivation()
            sage: d
            d/dx

            sage: D = d.extend_to_fraction_field()
            sage: D
            d/dx
            sage: D.domain()
            Fraction Field of Univariate Polynomial Ring in x over Rational Field

            sage: D(1/x)
            -1/x^2
        """

class RingDerivationWithoutTwist_zero(RingDerivationWithoutTwist):
    """
    This class can only represent the zero derivation.

    It is used when the parent is the zero derivation module
    (e.g., when its domain is ``ZZ``, ``QQ``, a finite field, etc.)
    """
    def __init__(self, parent, arg=None) -> None:
        """
        Initialize this derivation.

        TESTS::

            sage: M = ZZ.derivation_module()
            sage: der = M(); der
            0

            sage: from sage.rings.derivation import RingDerivationWithoutTwist_zero
            sage: isinstance(der, RingDerivationWithoutTwist_zero)
            True

            sage: TestSuite(der).run()
        """
    def __hash__(self):
        """
        Return a hash of this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(x)
            sage: hash(f)  # random
            3713081631936575706
        """
    def is_zero(self):
        """
        Return ``True`` if this derivation vanishes.

        EXAMPLES::

            sage: M = QQ.derivation_module()
            sage: M().is_zero()
            True
        """
    def list(self):
        """
        Return the list of coefficient of this derivation
        on the canonical basis.

        EXAMPLES::

            sage: M = QQ.derivation_module()
            sage: M().list()
            []
        """

class RingDerivationWithoutTwist_wrapper(RingDerivationWithoutTwist):
    """
    This class is a wrapper for derivation.

    It is useful for changing the parent without changing the
    computation rules for derivations. It is used for derivations
    over fraction fields and quotient rings.
    """
    def __init__(self, parent, arg=None) -> None:
        """
        Initialize this derivation.

        TESTS::

            sage: # needs sage.libs.singular
            sage: from sage.rings.derivation import RingDerivationWithoutTwist_wrapper
            sage: R.<x,y> = GF(5)[]
            sage: S = R.quo([x^5, y^5])
            sage: M = S.derivation_module()
            sage: der = M.random_element()
            sage: isinstance(der, RingDerivationWithoutTwist_wrapper)
            True
            sage: TestSuite(der).run()
        """
    def __hash__(self):
        """
        Return a hash of this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(x)
            sage: hash(f)  # random
            3713081631936575706
        """
    def list(self):
        """
        Return the list of coefficient of this derivation
        on the canonical basis.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: R.<X,Y> = GF(5)[]
            sage: S.<x,y> = R.quo([X^5, Y^5])
            sage: M = S.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)
            sage: S.derivation(x).list()
            [1, 0]
            sage: S.derivation(y).list()
            [0, 1]
            sage: f = x*S.derivation(x) + y*S.derivation(y); f
            x*d/dx + y*d/dy
            sage: f.list()
            [x, y]
        """

class RingDerivationWithoutTwist_function(RingDerivationWithoutTwist):
    """
    A class for untwisted derivations over rings whose elements
    are either polynomials, rational fractions, power series or
    Laurent series.
    """
    def __init__(self, parent, arg=None) -> None:
        """
        Initialize this derivation.

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: R.derivation(x)
            d/dx
            sage: der = R.derivation([1,2])
            sage: der
            d/dx + 2*d/dy

            sage: TestSuite(der).run()
        """
    def __hash__(self):
        """
        Return a hash of this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(x)
            sage: hash(f)  # random
            3713081631936575706
        """
    def is_zero(self):
        """
        Return ``True`` if this derivation is zero.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(); f
            d/dx
            sage: f.is_zero()
            False

            sage: (f-f).is_zero()
            True
        """
    def list(self):
        """
        Return the list of coefficient of this derivation
        on the canonical basis.

        EXAMPLES::

            sage: R.<x,y> = GF(5)[[]]
            sage: M = R.derivation_module()
            sage: M.basis()
            Family (d/dx, d/dy)

            sage: R.derivation(x).list()
            [1, 0]
            sage: R.derivation(y).list()
            [0, 1]

            sage: f = x*R.derivation(x) + y*R.derivation(y); f
            x*d/dx + y*d/dy
            sage: f.list()
            [x, y]
        """

class RingDerivationWithoutTwist_fraction_field(RingDerivationWithoutTwist_wrapper):
    """
    This class handles derivations over fraction fields.
    """
    def __hash__(self):
        """
        Return a hash of this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(x)
            sage: hash(f)  # random
            3713081631936575706
        """

class RingDerivationWithoutTwist_quotient(RingDerivationWithoutTwist_wrapper):
    """
    This class handles derivations over quotient rings.
    """
    def __hash__(self):
        """
        Return a hash of this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = R.derivation(x)
            sage: hash(f)  # random
            3713081631936575706
        """

class RingDerivationWithTwist_generic(RingDerivation):
    """
    The class handles `\\theta`-derivations of the form
    `\\lambda (\\theta - \\iota)` (where `\\iota` is the defining
    morphism of the codomain over the domain) for a scalar
    `\\lambda` varying in the codomain.
    """
    def __init__(self, parent, scalar: int = 0) -> None:
        """
        Initialize this derivation.

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: theta = R.hom([y,x])
            sage: R.derivation(twist=theta)
            0
            sage: R.derivation(1, twist=theta)
            [x |--> y, y |--> x] - id

            sage: der = R.derivation(x, twist=theta)
            sage: TestSuite(der).run()
        """
    def __hash__(self):
        """
        Return a hash of this derivation.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: theta = R.hom([y,x])
            sage: f = R.derivation(1, twist=theta)
            sage: hash(f)  # random
            -6511057926760520014
        """
    def list(self):
        """
        Return the list of coefficient of this twisted derivation
        on the canonical basis.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: K = R.fraction_field()
            sage: theta = K.hom([y,x])
            sage: M = K.derivation_module(twist=theta)
            sage: M.basis()
            Family (twisting_morphism - id,)
            sage: f = (x+y) * M.gen()
            sage: f
            (x + y)*(twisting_morphism - id)
            sage: f.list()
            [x + y]
        """
    def precompose(self, morphism):
        """
        Return the twisted derivation obtained by applying first
        ``morphism`` and then this twisted derivation.

        INPUT:

        - ``morphism`` -- a homomorphism of rings whose codomain is
          the domain of this derivation or a ring that coerces to
          the domain of this derivation

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: theta = R.hom([y,x])
            sage: D = R.derivation(x, twist=theta); D
            x*([x |--> y, y |--> x] - id)

            sage: f = R.hom([x^2, y^3])
            sage: g = D.postcompose(f); g
            x^2*([x |--> y^3, y |--> x^2] - [x |--> x^2, y |--> y^3])

        Observe that the `g` is no longer a `\\theta`-derivation but
        a `(f \\circ \\theta)`-derivation::

            sage: g.parent().twisting_morphism()
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> y^3
                    y |--> x^2
        """
    def postcompose(self, morphism):
        """
        Return the twisted derivation obtained by applying first
        this twisted derivation and then ``morphism``.

        INPUT:

        - ``morphism`` -- a homomorphism of rings whose domain is
          the codomain of this derivation or a ring into which the
          codomain of this derivation

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: theta = R.hom([y,x])
            sage: D = R.derivation(x, twist=theta); D
            x*([x |--> y, y |--> x] - id)

            sage: f = R.hom([x^2, y^3])
            sage: g = D.precompose(f); g
            x*([x |--> y^2, y |--> x^3] - [x |--> x^2, y |--> y^3])

        Observe that the `g` is no longer a `\\theta`-derivation but
        a `(\\theta \\circ f)`-derivation::

            sage: g.parent().twisting_morphism()
            Ring endomorphism of Multivariate Polynomial Ring in x, y over Integer Ring
              Defn: x |--> y^2
                    y |--> x^3
        """
    def extend_to_fraction_field(self):
        """
        Return the extension of this derivation to fraction fields of
        the domain and the codomain.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: theta = R.hom([y,x])
            sage: d = R.derivation(x, twist=theta)
            sage: d
            x*([x |--> y, y |--> x] - id)

            sage: D = d.extend_to_fraction_field(); D                                   # needs sage.libs.singular
            x*([x |--> y, y |--> x] - id)
            sage: D.domain()                                                            # needs sage.libs.singular
            Fraction Field of Multivariate Polynomial Ring in x, y over Integer Ring

            sage: D(1/x)                                                                # needs sage.libs.singular
            (x - y)/y
        """
