from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.verbose import verbose as verbose
from sage.rings.polynomial.polynomial_quotient_ring import PolynomialQuotientRing_domain as PolynomialQuotientRing_domain
from sage.rings.polynomial.polynomial_quotient_ring_element import PolynomialQuotientRingElement as PolynomialQuotientRingElement

class SplittingAlgebraElement(PolynomialQuotientRingElement):
    """
    Element class for :class:`SplittingAlgebra`.

    EXAMPLES::

        sage: from sage.algebras.splitting_algebra import SplittingAlgebra
        sage: cp6 = cyclotomic_polynomial(6)
        sage: CR6.<e6> = SplittingAlgebra(cp6)
        sage: type(e6)
        <class 'sage.algebras.splitting_algebra.SplittingAlgebra_with_category.element_class'>

        sage: type(CR6(5))
        <class 'sage.algebras.splitting_algebra.SplittingAlgebra_with_category.element_class'>
    """
    def __invert__(self):
        """
        Return the inverse of ``self``.

        Support inversion of special elements attached to the construction
        of the parent and which are recorded in the list
        ``self.parent()._invertible_elements``.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: CR3.<e3> = SplittingAlgebra(cyclotomic_polynomial(3))
            sage: ~e3
            -e3 - 1
            sage: ~(e3 + 5)
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible
        """
    def is_unit(self):
        """
        Return ``True`` if ``self`` is invertible.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: CR3.<e3> = SplittingAlgebra(cyclotomic_polynomial(3))
            sage: e3.is_unit()
            True
        """
    def monomial_coefficients(self, copy: bool = True):
        """
        Return the dictionary of ``self`` according to its lift to the cover.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: CR3.<e3> = SplittingAlgebra(cyclotomic_polynomial(3))
            sage: f = e3 + 42
            sage: f.monomial_coefficients()
            {0: 42, 1: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {0: 42, 1: 1}
        """
    dict = monomial_coefficients

class SplittingAlgebra(PolynomialQuotientRing_domain):
    """
    For a given monic polynomial `p(t)` of degree `n` over a commutative
    ring `R`, the splitting algebra is the universal `R`-algebra in which
    `p(t)` has `n` roots, or, more precisely, over which `p(t)` factors,

    .. MATH::

        p(t) = (t - \\xi_1) \\cdots (t - \\xi_n).

    This class creates an algebra as extension over the base ring of a
    given polynomial `p` such that `p` splits into linear factors over
    that extension. It is assumed (and not checked in general) that the
    Galois group of `p` is the symmetric Group `S(n)`. The construction
    is recursive (following [LT2012]_, 1.3).

    INPUT:

    - ``monic_polynomial`` -- the monic polynomial which should be split
    - ``names`` -- names for the indeterminates to be adjoined to the
      base ring of ``monic_polynomial``
    - ``warning`` -- boolean (default: ``True``); can be used (by setting to
      ``False``) to suppress a warning which will be thrown whenever it cannot
      be checked that the Galois group of ``monic_polynomial`` is maximal

    EXAMPLES::

        sage: from sage.algebras.splitting_algebra import SplittingAlgebra
        sage: Lc.<w> = LaurentPolynomialRing(ZZ)
        sage: PabLc.<u,v> = Lc[]; t = polygen(PabLc)
        sage: S.<x, y> = SplittingAlgebra(t^3 - u*t^2 + v*t - w)
        doctest:...: UserWarning: Assuming x^3 - u*x^2 + v*x - w to have maximal
                                  Galois group!

        sage: roots = S.splitting_roots(); roots
        [x, y, -y - x + u]
        sage: all(t^3 -u*t^2 +v*t -w == 0 for t in roots)
        True
        sage: xi = ~x; xi
        (w^-1)*x^2 + ((-w^-1)*u)*x + (w^-1)*v
        sage: ~xi == x
        True
        sage: ~y
        ((-w^-1)*x)*y + (-w^-1)*x^2 + ((w^-1)*u)*x
        sage: zi = ((w^-1)*x)*y; ~zi
        -y - x + u

        sage: cp3 = cyclotomic_polynomial(3).change_ring(GF(5))
        sage: CR3.<e3> = SplittingAlgebra(cp3)
        sage: CR3.is_field()
        True
        sage: CR3.cardinality()
        25
        sage: F.<a> = cp3.splitting_field()
        sage: F.cardinality()
        25
        sage: E3 = cp3.change_ring(F).roots()[0][0]; E3
        3*a + 3
        sage: f = CR3.hom([E3]); f
        Ring morphism:
          From: Splitting Algebra of x^2 + x + 1
                with roots [e3, 4*e3 + 4]
                over Finite Field of size 5
          To:   Finite Field in a of size 5^2
          Defn: e3 |--> 3*a + 3

    REFERENCES:

    - [EL2002]_
    - [Lak2010]_
    - [Tho2011]_
    - [LT2012]_
    """
    Element = SplittingAlgebraElement
    def __init__(self, monic_polynomial, names: str = 'X', iterate: bool = True, warning: bool = True) -> None:
        """
        Python constructor.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: Lw.<w> = LaurentPolynomialRing(ZZ)
            sage: PuvLw.<u,v> = Lw[]; t = polygen(PuvLw)
            sage: S.<x, y> = SplittingAlgebra(t^3 - u*t^2 + v*t - w, warning=False)
            sage: TestSuite(S).run()
        """
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: L.<t, u, v, w > = LaurentPolynomialRing(ZZ); x = polygen(L)
            sage: S = SplittingAlgebra(x^4 -t*x^3 - u*x^2 - v*x + w, ('X', 'Y', 'Z'), warning=False)
            sage: S.__reduce__()
            (<class 'sage.algebras.splitting_algebra.SplittingAlgebra_with_category'>,
            (x^4 - t*x^3 - u*x^2 - v*x + w, ('X', 'Y', 'Z'), True, False))
            sage: S.base_ring().__reduce__()
            (<class 'sage.algebras.splitting_algebra.SplittingAlgebra_with_category'>,
            (Y^3 + (X - t)*Y^2 + (X^2 - t*X - u)*Y + X^3 - t*X^2 - u*X - v,
            ('Y', 'Z'),
            False,
            False))

            sage: TestSuite(S).run()
        """
    def hom(self, im_gens, codomain=None, check: bool = True, base_map=None):
        """
        This version keeps track with the special recursive structure
        of :class:`SplittingAlgebra`

        Type ``Ring.hom?`` to see the general documentation of this method.
        Here you see just special examples for the current class.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: L.<u, v, w> = LaurentPolynomialRing(ZZ); x = polygen(L)
            sage: S = SplittingAlgebra(x^3 - u*x^2 + v*x - w, ('X', 'Y'))
            sage: P.<x, y, z> = PolynomialRing(ZZ)
            sage: F = FractionField(P)
            sage: im_gens = [F(g) for g in [y, x, x + y + z, x*y+x*z+y*z, x*y*z]]
            sage: f = S.hom(im_gens)
            sage: f(u), f(v), f(w)
            (x + y + z, x*y + x*z + y*z, x*y*z)
            sage: roots = S.splitting_roots(); roots
            [X, Y, -Y - X + u]
            sage: [f(r) for r in roots]
            [x, y, z]
        """
    def is_completely_split(self):
        """
        Return ``True`` if the defining polynomial of ``self`` splits into
        linear factors over ``self``.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: L.<u, v, w > = LaurentPolynomialRing(ZZ); x = polygen(L)
            sage: S.<a,b> = SplittingAlgebra(x^3 - u*x^2 + v*x - w)
            sage: S.is_completely_split()
            True
            sage: S.base_ring().is_completely_split()
            False
        """
    @cached_method
    def lifting_map(self):
        """
        Return a section map from ``self`` to the cover ring. It is implemented according
        to the same named method of :class:`~sage.rings.quotient_ring.QuotientRing_nc`.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: x = polygen(ZZ)
            sage: S = SplittingAlgebra(x^2+1, ('I',))
            sage: lift = S.lifting_map()
            sage: lift(5)
            5
            sage: r1, r2 =S.splitting_roots()
            sage: lift(r1)
            I
        """
    def splitting_roots(self):
        """
        Return the roots of the split equation.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: x = polygen(ZZ)
            sage: S = SplittingAlgebra(x^2+1, ('I',))
            sage: S.splitting_roots()
            [I, -I]
        """
    @cached_method
    def scalar_base_ring(self):
        """
        Return the ring of scalars of ``self`` (considered as an algebra).

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: L.<u, v, w > = LaurentPolynomialRing(ZZ)
            sage: x = polygen(L)
            sage: S = SplittingAlgebra(x^3 - u*x^2 + v*x - w, ('X', 'Y'))
            sage: S.base_ring()
            Factorization Algebra of x^3 - u*x^2 + v*x - w with roots [X]
             over Multivariate Laurent Polynomial Ring in u, v, w over Integer Ring
            sage: S.scalar_base_ring()
            Multivariate Laurent Polynomial Ring in u, v, w over Integer Ring
        """
    @cached_method
    def defining_polynomial(self):
        """
        Return the defining polynomial of ``self``.

        EXAMPLES::

            sage: from sage.algebras.splitting_algebra import SplittingAlgebra
            sage: L.<u, v, w > = LaurentPolynomialRing(ZZ)
            sage: x = polygen(L)
            sage: S = SplittingAlgebra(x^3 - u*x^2 + v*x - w, ('X', 'Y'))
            sage: S.defining_polynomial()
            x^3 - u*x^2 + v*x - w
        """

def solve_with_extension(monic_polynomial, root_names=None, var: str = 'x', flatten: bool = False, warning: bool = True):
    """
    Return all roots of a monic polynomial in its base ring or in an appropriate
    extension ring, as far as possible.

    INPUT:

    - ``monic_polynomial`` -- the monic polynomial whose roots should be created
    - ``root_names`` -- names for the indeterminates needed to define the
      splitting algebra of the ``monic_polynomial`` (if necessary and possible)
    - ``var`` -- (default: ``'x'``) for the indeterminate needed to define the
      splitting field of the ``monic_polynomial`` (if necessary and possible)
    - ``flatten`` -- boolean (default: ``True``); if ``True`` the roots will
      not be given as a list of pairs ``(root, multiplicity)`` but as a list of
      roots repeated according to their multiplicity
    - ``warning`` -- boolean (default: ``True``); can be used (by setting to
      ``False``) to suppress a warning which will be thrown whenever it cannot
      be checked that the Galois group of ``monic_polynomial`` is maximal

    OUTPUT:

    List of tuples ``(root, multiplicity)`` respectively list of roots repeated
    according to their multiplicity if option ``flatten`` is ``True``.

    EXAMPLES::

        sage: from sage.algebras.splitting_algebra import solve_with_extension
        sage: t = polygen(ZZ)
        sage: p = t^2 -2*t +1
        sage: solve_with_extension(p, flatten=True )
        [1, 1]
        sage: solve_with_extension(p)
        [(1, 2)]

        sage: cp5 = cyclotomic_polynomial(5, var='T').change_ring(UniversalCyclotomicField())
        sage: solve_with_extension(cp5)
        [(E(5), 1), (E(5)^4, 1), (E(5)^2, 1), (E(5)^3, 1)]
        sage: _[0][0].parent()
        Universal Cyclotomic Field
    """
