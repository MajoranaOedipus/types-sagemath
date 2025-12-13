from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.structure.element import IntegralDomainElement as IntegralDomainElement
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def normalize_extra_units(base_ring, add_units, warning: bool = True):
    """
    Function to normalize input data.

    The given list will be replaced by a list of the involved prime factors
    (if possible).

    INPUT:

    - ``base_ring`` -- a ring in the category of :class:`IntegralDomains`
    - ``add_units`` -- list of elements from base ring
    - ``warning`` -- boolean (default: ``True``); to suppress a warning which
      is thrown if no normalization was possible

    OUTPUT: list of all prime factors of the elements of the given list

    EXAMPLES::

        sage: from sage.rings.localization import normalize_extra_units
        sage: normalize_extra_units(ZZ, [3, -15, 45, 9, 2, 50])
        [2, 3, 5]
        sage: P.<x,y,z> = ZZ[]
        sage: normalize_extra_units(P,                                                  # needs sage.libs.pari
        ....:                       [3*x, z*y**2, 2*z, 18*(x*y*z)**2, x*z, 6*x*z, 5])
        [2, 3, 5, z, y, x]
        sage: P.<x,y,z> = QQ[]
        sage: normalize_extra_units(P,                                                  # needs sage.libs.pari
        ....:                       [3*x, z*y**2, 2*z, 18*(x*y*z)**2, x*z, 6*x*z, 5])
        [z, y, x]

        sage: # needs sage.libs.singular
        sage: R.<x, y> = ZZ[]
        sage: Q.<a, b> = R.quo(x**2 - 5)
        sage: p = b**2 - 5
        sage: p == (b-a)*(b+a)
        True
        sage: normalize_extra_units(Q, [p])                                             # needs sage.libs.pari
        doctest:...: UserWarning: Localization may not be represented uniquely
        [b^2 - 5]
        sage: normalize_extra_units(Q, [p], warning=False)                              # needs sage.libs.pari
        [b^2 - 5]
    """

class LocalizationElement(IntegralDomainElement):
    """
    Element class for localizations of integral domains.

    INPUT:

    - ``parent`` -- instance of :class:`Localization`
    - ``x`` -- instance of :class:`FractionFieldElement` whose parent is the
      fraction field of the parent's base ring

    EXAMPLES::

        sage: # needs sage.libs.pari
        sage: from sage.rings.localization import LocalizationElement
        sage: P.<x,y,z> = GF(5)[]
        sage: L = P.localization((x, y*z - x))
        sage: LocalizationElement(L, 4/(y*z-x)**2)
        (-1)/(y^2*z^2 - 2*x*y*z + x^2)
        sage: _.parent()
        Multivariate Polynomial Ring in x, y, z over Finite Field of size 5
         localized at (x, y*z - x)
    """
    def __init__(self, parent, x) -> None:
        """
        Python constructor for the element class for localizations of integral domains.

        EXAMPLES::

            sage: from sage.rings.localization import LocalizationElement
            sage: P.<x> = RR[]
            sage: L = Localization(P, x**2 + x + 1)                                     # needs sage.libs.pari
            sage: l = LocalizationElement(L, (x**2+1)/(x**2+x+1))                       # needs sage.libs.pari
            sage: l._value == (x**2+1)/(x**2+x+1)                                       # needs sage.libs.pari
            True
        """
    def factor(self, proof=None):
        """
        Return the factorization of this polynomial.

        INPUT:

        - ``proof`` -- (optional) if given it is passed to the
          corresponding method of the numerator of ``self``

        EXAMPLES::

            sage: P.<X, Y> = QQ['x, y']
            sage: L = P.localization(X - Y)
            sage: x, y = L.gens()
            sage: p = (x^2 - y^2)/(x-y)^2                                               # needs sage.libs.singular
            sage: p.factor()                                                            # needs sage.libs.singular
            (1/(x - y)) * (x + y)
        """
    def numerator(self):
        """
        Return the numerator of ``self``.

        EXAMPLES::

            sage: L = ZZ.localization((3,5))
            sage: L(7/15).numerator()
            7
        """
    def denominator(self):
        """
        Return the denominator of ``self``.

        EXAMPLES::

            sage: L = Localization(ZZ, (3,5))
            sage: L(7/15).denominator()
            15
        """
    def is_unit(self):
        """
        Return ``True`` if ``self`` is a unit.

        EXAMPLES::

            sage: # needs sage.libs.pari sage.singular
            sage: P.<x,y,z> = QQ[]
            sage: L = P.localization((x, y*z))
            sage: L(y*z).is_unit()
            True
            sage: L(z).is_unit()
            True
            sage: L(x*y*z).is_unit()
            True
        """
    def inverse_of_unit(self):
        """
        Return the inverse of ``self``.

        EXAMPLES::

            sage: P.<x,y,z> = ZZ[]
            sage: L = Localization(P, x*y*z)
            sage: L(x*y*z).inverse_of_unit()                                            # needs sage.libs.singular
            1/(x*y*z)
            sage: L(z).inverse_of_unit()                                                # needs sage.libs.singular
            1/z
        """
    def __hash__(self):
        """
        Return the hash of the corresponding fraction field element.

        EXAMPLES::

            sage: L = ZZ.localization(5)
            sage: l5 = L(5); l7 = L(7)
            sage: {l5: ~l5, l7: 7}              # indirect doctest
            {5: 1/5, 7: 7}
        """

class Localization(Parent, UniqueRepresentation):
    '''
    The localization generalizes the construction of the field of fractions of
    an integral domain to an arbitrary ring. Given a (not necessarily
    commutative) ring `R` and a subset `S` of `R`, there exists a ring
    `R[S^{-1}]` together with the ring homomorphism `R \\longrightarrow R[S^{-1}]`
    that "inverts" `S`; that is, the homomorphism maps elements in `S` to unit
    elements in `R[S^{-1}]` and, moreover, any ring homomorphism from `R` that
    "inverts" `S` uniquely factors through `R[S^{-1}]`.

    The ring `R[S^{-1}]` is called the *localization* of `R` with respect to
    `S`. For example, if `R` is a commutative ring and `f` an element in `R`,
    then the localization consists of elements of the form
    `r/f, r\\in R, n \\geq 0` (to be precise, `R[f^{-1}] = R[t]/(ft-1)`).

    The above text is taken from `Wikipedia`. The construction here used for
    this class relies on the construction of the field of fraction and is
    therefore restricted to integral domains.

    Accordingly, the base ring must be in the category of ``IntegralDomains``.
    Furthermore, the base ring should support
    :meth:`sage.structure.element.CommutativeRingElement.divides` and the exact
    division operator ``//`` (:meth:`sage.structure.element.Element.__floordiv__`)
    in order to guarantee a successful application.

    INPUT:

    - ``base_ring`` -- a ring in the category of ``IntegralDomains``
    - ``extra_units`` -- tuple of elements of ``base_ring`` which should be
      turned into units
    - ``category`` -- (default: ``None``) passed to :class:`Parent`
    - ``warning`` -- boolean (default: ``True``); to suppress a warning which
      is thrown if ``self`` cannot be represented uniquely

    REFERENCES:

    - :wikipedia:`Ring_(mathematics)#Localization`

    EXAMPLES::

        sage: L = Localization(ZZ, (3,5))
        sage: 1/45 in L
        True
        sage: 1/43 in L
        False

        sage: Localization(L, (7,11))
        Integer Ring localized at (3, 5, 7, 11)
        sage: _.is_subring(QQ)
        True

        sage: L(~7)
        Traceback (most recent call last):
        ...
        ValueError: factor 7 of denominator is not a unit

        sage: Localization(Zp(7), (3, 5))                                               # needs sage.rings.padics
        Traceback (most recent call last):
        ...
        ValueError: all given elements are invertible in
        7-adic Ring with capped relative precision 20

        sage: # needs sage.libs.pari
        sage: R.<x> = ZZ[]
        sage: L = R.localization(x**2 + 1)
        sage: s = (x+5)/(x**2+1)
        sage: s in L
        True
        sage: t = (x+5)/(x**2+2)
        sage: t in L
        False
        sage: L(t)
        Traceback (most recent call last):
        ...
        TypeError: fraction must have unit denominator
        sage: L(s) in R
        False
        sage: y = L(x)
        sage: g = L(s)
        sage: g.parent()
        Univariate Polynomial Ring in x over Integer Ring localized at (x^2 + 1,)
        sage: f = (y+5)/(y**2+1); f
        (x + 5)/(x^2 + 1)
        sage: f == g
        True
        sage: (y+5)/(y**2+2)
        Traceback (most recent call last):
        ...
        ValueError: factor x^2 + 2 of denominator is not a unit

        sage: Lau.<u, v> = LaurentPolynomialRing(ZZ)                                    # needs sage.modules
        sage: LauL = Lau.localization(u + 1)                                            # needs sage.modules
        sage: LauL(~u).parent()                                                         # needs sage.modules
        Multivariate Polynomial Ring in u, v over Integer Ring localized at (v, u, u + 1)

    More examples will be shown typing ``sage.rings.localization?``

    TESTS:

    Check that :issue:`33463` is fixed::

        sage: R = ZZ.localization(5)
        sage: R.localization(~5)
        Integer Ring localized at (5,)
    '''
    Element = LocalizationElement
    def __init__(self, base_ring, extra_units, names=None, normalize: bool = True, category=None, warning: bool = True) -> None:
        """
        Python constructor of Localization.

        TESTS::

            sage: L = Localization(ZZ, (3, 5))
            sage: TestSuite(L).run()

            sage: R.<x> = ZZ[]
            sage: L = R.localization(x**2 + 1)                                          # needs sage.libs.pari
            sage: TestSuite(L).run()
        """
    def ngens(self):
        """
        Return the number of generators of ``self``
        according to the same method for the base ring.

        EXAMPLES::

            sage: R.<x, y> = ZZ[]
            sage: Localization(R, (x**2 + 1, y - 1)).ngens()                            # needs sage.libs.pari
            2

            sage: Localization(ZZ, 2).ngens()
            1
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of ``self`` which is
        the ``i``-th generator of the base ring.

        EXAMPLES::

            sage: R.<x, y> = ZZ[]
            sage: R.localization((x**2 + 1, y - 1)).gen(0)                              # needs sage.libs.pari
            x

            sage: ZZ.localization(2).gen(0)
            1
        """
    def gens(self) -> tuple:
        """
        Return a tuple whose entries are the generators for this
        object, in order.

        EXAMPLES::

            sage: R.<x, y> = ZZ[]
            sage: Localization(R, (x**2 + 1, y - 1)).gens()                             # needs sage.libs.pari
            (x, y)

            sage: Localization(ZZ, 2).gens()
            (1,)
        """
    def fraction_field(self):
        """
        Return the fraction field of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<a> = GF(5)[]
            sage: L = Localization(R, (a**2 - 3, a))
            sage: L.fraction_field()
            Fraction Field of Univariate Polynomial Ring in a over Finite Field of size 5
            sage: L.is_subring(_)
            True
        """
    def characteristic(self):
        """
        Return the characteristic of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: R.<a> = GF(5)[]
            sage: L = R.localization((a**2 - 3, a))
            sage: L.characteristic()
            5
        """
    def krull_dimension(self):
        """
        Return the Krull dimension of this localization.

        Since the current implementation just allows integral domains as base ring
        and localization at a finite set of elements the spectrum of ``self``
        is open in the irreducible spectrum of its base ring.
        Therefore, by density we may take the dimension from there.

        EXAMPLES::

            sage: R = ZZ.localization((2, 3))
            sage: R.krull_dimension()
            1
        """
    def is_field(self, proof: bool = True):
        """
        Return ``True`` if this ring is a field.

        INPUT:

        - ``proof`` -- boolean (default: ``True``); determines what to do in
          unknown cases

        ALGORITHM:

        If the parameter ``proof`` is set to ``True``, the returned value is
        correct but the method might throw an error.  Otherwise, if it is set
        to ``False``, the method returns ``True`` if it can establish that
        ``self`` is a field and ``False`` otherwise.

        EXAMPLES::

            sage: R = ZZ.localization((2, 3))
            sage: R.is_field()
            False
        """
