from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import Element as Element
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method, richcmp_not_equal as richcmp_not_equal
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.sequence import Sequence as Sequence

class Factorization(SageObject):
    """
    A formal factorization of an object.

    EXAMPLES::

        sage: N = 2006
        sage: F = N.factor(); F
        2 * 17 * 59
        sage: F.unit()
        1
        sage: F = factor(-2006); F
        -1 * 2 * 17 * 59
        sage: F.unit()
        -1
        sage: loads(F.dumps()) == F
        True
        sage: F = Factorization([(x, 1/3)])                                             # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer
    """
    def __init__(self, x, unit=None, cr: bool = False, sort: bool = True, simplify: bool = True) -> None:
        """
        Create a :class:`Factorization` object.

        INPUT:

        - ``x`` -- list of pairs (p, e) with e an integer
          otherwise a :exc:`TypeError` is raised

        - ``unit`` -- (default: 1) the unit part of the factorization

        - ``cr`` -- (default: ``False``) if ``True``, print the factorization
          with carriage returns between factors

        - ``sort`` -- (default: ``True``) if ``True``, sort the factors by
          calling the sort function ``self.sort()`` after creating
          the factorization

        - ``simplify`` -- (default: ``True``) if ``True``, remove duplicate
          factors from the factorization.  See the documentation for
          self.simplify.

        OUTPUT: a Factorization object

        EXAMPLES:

        We create a factorization with all the default options::

            sage: Factorization([(2,3), (5, 1)])
            2^3 * 5

        We create a factorization with a specified unit part::

            sage: Factorization([(2,3), (5, 1)], unit=-1)
            -1 * 2^3 * 5

        We try to create a factorization but with a string an exponent, which
        results in a TypeError::

            sage: Factorization([(2,3), (5, 'x')])
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 'x' to an integer

        We create a factorization that puts newlines after each multiply sign
        when printing.  This is mainly useful when the primes are large::

            sage: Factorization([(2,3), (5, 2)], cr=True)
            2^3 *
            5^2

        Another factorization with newlines and nontrivial unit part, which
        appears on a line by itself::

            sage: Factorization([(2,3), (5, 2)], cr=True, unit=-2)
            -2 *
            2^3 *
            5^2

        A factorization, but where we do not sort the factors::

            sage: Factorization([(5,3), (2, 3)], sort=False)
            5^3 * 2^3

        By default, in the commutative case, factorizations are sorted by the
        prime base::

            sage: Factorization([(2, 7), (5,2), (2, 5)])
            2^12 * 5^2
            sage: R.<a,b> = FreeAlgebra(QQ, 2)                                          # needs sage.combinat sage.modules
            sage: Factorization([(a,1), (b,1), (a,2)])                                  # needs sage.combinat sage.modules
            a * b * a^2

        Autosorting (the default) swaps around the factors below::

            sage: F = Factorization([(ZZ^3, 2), (ZZ^2, 5)], cr=True); F                 # needs sage.modules
            (Ambient free module of rank 2 over the principal ideal domain Integer Ring)^5 *
            (Ambient free module of rank 3 over the principal ideal domain Integer Ring)^2
        """
    def __getitem__(self, i):
        """
        Return `i`-th factor of ``self``.

        EXAMPLES::

            sage: a = factor(-75); a
            -1 * 3 * 5^2
            sage: a[0]
            (3, 1)
            sage: a[1]
            (5, 2)
            sage: a[-1]
            (5, 2)
            sage: a[5]
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
        """
    def __setitem__(self, i, v) -> None:
        """
        Set the `i`-th factor of ``self``.

        .. warning::

           NOT ALLOWED -- Factorizations are immutable.

        EXAMPLES::

            sage: a = factor(-75); a
            -1 * 3 * 5^2
            sage: a[0] = (2,3)
            Traceback (most recent call last):
            ...
            TypeError: 'Factorization' object does not support item assignment
        """
    def __len__(self) -> int:
        """
        Return the number of prime factors of ``self``, not counting
        the unit part.

        EXAMPLES::

            sage: len(factor(15))
            2

        Note that the unit part is not included in the count::

            sage: a = factor(-75); a
            -1 * 3 * 5^2
            sage: len(a)
            2
            sage: list(a)
            [(3, 1), (5, 2)]
            sage: len(list(a))
            2
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        This first compares the values.

        If values are equal, this compares the units.

        If units are equal, this compares the underlying lists of
        ``self`` and ``other``.

        EXAMPLES:

        We compare two contrived formal factorizations::

            sage: a = Factorization([(2, 7), (5,2), (2, 5)])
            sage: b = Factorization([(2, 7), (5,10), (7, 3)])
            sage: a
            2^12 * 5^2
            sage: b
            2^7 * 5^10 * 7^3
            sage: a < b
            True
            sage: b < a
            False
            sage: a.value()
            102400
            sage: b.value()
            428750000000

        We compare factorizations of some polynomials::

            sage: x = polygen(QQ)
            sage: x^2 - 1 > x^2 - 4
            True
            sage: factor(x^2 - 1) > factor(x^2 - 4)                                     # needs sage.libs.pari
            True
        """
    def __copy__(self):
        '''
        Return a copy of ``self``.

        This is *not* a deepcopy -- only references to the factors are
        returned, not copies of them.  Use ``deepcopy(self)`` if you need
        a deep copy of ``self``.

        EXAMPLES:

        We create a factorization that has mutable primes::

            sage: F = Factorization([([1,2], 5), ([5,6], 10)]); F
            ([1, 2])^5 * ([5, 6])^10

        We make a copy of it::

            sage: G = copy(F); G
            ([1, 2])^5 * ([5, 6])^10
            sage: G is F
            False

        Note that if we change one of the mutable "primes" of F, this does
        change G::

            sage: F[1][0][0] = \'hello\'
            sage: G
            ([1, 2])^5 * ([\'hello\', 6])^10
        '''
    def __deepcopy__(self, memo):
        """
        Return a deep copy of ``self``.

        EXAMPLES:

        We make a factorization that has mutable entries::

            sage: F = Factorization([([1,2], 5), ([5,6], 10)]); F
            ([1, 2])^5 * ([5, 6])^10

        Now we make a copy of it and a deep copy::

            sage: K = copy(F)
            sage: G = deepcopy(F); G
            ([1, 2])^5 * ([5, 6])^10

        We change one of the mutable entries of F::

            sage: F[0][0][0] = 10

        This of course changes F::

            sage: F
            ([10, 2])^5 * ([5, 6])^10

        It also changes the copy K of F::

            sage: K
            ([10, 2])^5 * ([5, 6])^10

        It does *not* change the deep copy G::

            sage: G
            ([1, 2])^5 * ([5, 6])^10
        """
    def universe(self):
        """
        Return the parent structure of my factors.

        .. NOTE::

           This used to be called ``base_ring``, but the universe
           of a factorization need not be a ring.

        EXAMPLES::

            sage: F = factor(2006)
            sage: F.universe()
            Integer Ring

            sage: R.<x,y,z> = FreeAlgebra(QQ, 3)                                        # needs sage.combinat sage.modules
            sage: F = Factorization([(z, 2)], 3)                                        # needs sage.combinat sage.modules
            sage: (F*F^-1).universe()                                                   # needs sage.combinat sage.modules
            Free Algebra on 3 generators (x, y, z) over Rational Field

            sage: F = ModularSymbols(11,4).factorization()                              # needs sage.modular
            sage: F.universe()                                                          # needs sage.modular
        """
    def base_change(self, U):
        """
        Return the factorization ``self``, with its factors (including the
        unit part) coerced into the universe `U`.

        EXAMPLES::

            sage: F = factor(2006)
            sage: F.universe()
            Integer Ring
            sage: P.<x> = ZZ[]
            sage: F.base_change(P).universe()
            Univariate Polynomial Ring in x over Integer Ring

        This method will return a :exc:`TypeError` if the coercion is not
        possible::

            sage: g = x^2 - 1
            sage: F = factor(g); F                                                      # needs sage.libs.pari
            (x - 1) * (x + 1)
            sage: F.universe()                                                          # needs sage.libs.pari
            Univariate Polynomial Ring in x over Integer Ring
            sage: F.base_change(ZZ)                                                     # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            TypeError: Impossible to coerce the factors of (x - 1) * (x + 1) into Integer Ring
        """
    def is_commutative(self) -> bool:
        """
        Return whether the factors commute.

        EXAMPLES::

            sage: F = factor(2006)
            sage: F.is_commutative()
            True

            sage: # needs sage.rings.number_field
            sage: K = QuadraticField(23, 'a')
            sage: F = K.factor(13)
            sage: F.is_commutative()
            True

            sage: # needs sage.combinat sage.modules
            sage: R.<x,y,z> = FreeAlgebra(QQ, 3)
            sage: F = Factorization([(z, 2)], 3)
            sage: F.is_commutative()
            False
            sage: (F*F^-1).is_commutative()
            False
        """
    def simplify(self):
        """
        Combine adjacent products as much as possible.

        TESTS::

            sage: # needs sage.combinat sage.modules
            sage: R.<x,y> = FreeAlgebra(ZZ, 2)
            sage: F = Factorization([(x,3), (y, 2), (y,2)], simplify=False); F
            x^3 * y^2 * y^2
            sage: F.simplify(); F
            x^3 * y^4
            sage: F * Factorization([(y, -2)], 2)
            (2) * x^3 * y^2
        """
    def sort(self, key=None):
        """
        Sort the factors in this factorization.

        INPUT:

        - ``key`` -- (default: ``None``) comparison key

        OUTPUT: changes this factorization to be sorted (inplace)

        If ``key`` is ``None``, we determine the comparison key as
        follows:

        If the prime in the first factor has a dimension
        method, then we sort based first on *dimension* then on
        the exponent.

        If there is no dimension method, we next
        attempt to sort based on a degree method, in which case, we
        sort based first on *degree*, then exponent to break ties
        when two factors have the same degree, and if those match
        break ties based on the actual prime itself.

        Otherwise, we sort according to the prime itself.

        EXAMPLES:

        We create a factored polynomial::

            sage: x = polygen(QQ, 'x')
            sage: F = factor(x^3 + 1); F                                                # needs sage.libs.pari
            (x + 1) * (x^2 - x + 1)

        We sort it by decreasing degree::

            sage: F.sort(key=lambda x: (-x[0].degree(), x))                             # needs sage.libs.pari
            sage: F                                                                     # needs sage.libs.pari
            (x^2 - x + 1) * (x + 1)
        """
    def unit(self):
        """
        Return the unit part of this factorization.

        EXAMPLES:

        We create a polynomial over the real double field and factor it::

            sage: x = polygen(RDF, 'x')
            sage: F = factor(-2*x^2 - 1); F                                             # needs numpy
            (-2.0) * (x^2 + 0.5000000000000001)

        Note that the unit part of the factorization is `-2.0`::

            sage: F.unit()                                                              # needs numpy
            -2.0

            sage: F = factor(-2006); F
            -1 * 2 * 17 * 59
            sage: F.unit()
            -1
        """
    @cached_method
    def __pari__(self):
        """
        Return the PARI factorization matrix corresponding to ``self``.

        EXAMPLES::

            sage: f = factor(-24)
            sage: pari(f)                                                               # needs sage.libs.pari
            [-1, 1; 2, 3; 3, 1]

            sage: R.<x> = QQ[]
            sage: g = factor(x^10 - 1)                                                  # needs sage.libs.pari
            sage: pari(g)                                                               # needs sage.libs.pari
            [x - 1, 1; x + 1, 1; x^4 - x^3 + x^2 - x + 1, 1; x^4 + x^3 + x^2 + x + 1, 1]
        """
    def __add__(self, other):
        """
        Return the (unfactored) sum of ``self`` and ``other``.

        EXAMPLES::

            sage: factor(-10) + 16
            6
            sage: factor(10) - 16
            -6
            sage: factor(100) + factor(19)
            119
        """
    def __sub__(self, other):
        """
        Return the (unfactored) difference of ``self`` and ``other``.

        EXAMPLES::

            sage: factor(-10) + 16
            6
            sage: factor(10) - 16
            -6
        """
    def __radd__(self, left):
        """
        Return the (unfactored) sum of ``self`` and ``left``.

        EXAMPLES::

            sage: 16 + factor(-10)
            6
        """
    def __rsub__(self, left):
        """
        Return the (unfactored) difference of ``left`` and ``self``.

        EXAMPLES::

            sage: 16 - factor(10)
            6
        """
    def __neg__(self):
        """
        Return negative of this factorization.

        EXAMPLES::

            sage: a = factor(-75); a
            -1 * 3 * 5^2
            sage: -a
            3 * 5^2
            sage: (-a).unit()
            1
        """
    def __rmul__(self, left):
        """
        Return the product ``left * self``, where ``left`` is not a Factorization.

        EXAMPLES::

            sage: a = factor(15); a
            3 * 5
            sage: -2 * a
            -2 * 3 * 5
            sage: a * -2
            -2 * 3 * 5
            sage: R.<x,y> = FreeAlgebra(QQ, 2)                                          # needs sage.combinat sage.modules
            sage: f = Factorization([(x,2), (y,3)]); f                                  # needs sage.combinat sage.modules
            x^2 * y^3
            sage: x * f                                                                 # needs sage.combinat sage.modules
            x^3 * y^3
            sage: f * x                                                                 # needs sage.combinat sage.modules
            x^2 * y^3 * x

        Note that this does not automatically factor ``left``::

            sage: F = Factorization([(5,3), (2,3)])
            sage: 46 * F
            2^3 * 5^3 * 46
        """
    def __mul__(self, other):
        """
        Return the product of two factorizations, which is obtained by
        combining together like factors.

        If the two factorizations have different universes, this
        method will attempt to find a common universe for the
        product.  A :exc:`TypeError` is raised if this is impossible.

        EXAMPLES::

            sage: factor(-10) * factor(-16)
            2^5 * 5
            sage: factor(-10) * factor(16)
            -1 * 2^5 * 5

            sage: # needs sage.combinat sage.modules
            sage: R.<x,y> = FreeAlgebra(ZZ, 2)
            sage: F = Factorization([(x,3), (y, 2), (x,1)]); F
            x^3 * y^2 * x
            sage: F*F
            x^3 * y^2 * x^4 * y^2 * x
            sage: -1 * F
            (-1) * x^3 * y^2 * x

            sage: P.<x> = ZZ[]
            sage: f = 2*x + 2
            sage: c = f.content(); g = f//c
            sage: Fc = factor(c); Fc.universe()
            Integer Ring
            sage: Fg = factor(g); Fg.universe()
            Univariate Polynomial Ring in x over Integer Ring
            sage: F = Fc * Fg; F.universe()
            Univariate Polynomial Ring in x over Integer Ring
            sage: [type(a[0]) for a in F]
            [<... 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>,
             <... 'sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint'>]
        """
    def __pow__(self, n):
        """
        Return the `n`-th power of a factorization, which is got by
        combining together like factors.

        EXAMPLES::

            sage: f = factor(-100); f
            -1 * 2^2 * 5^2
            sage: f^3
            -1 * 2^6 * 5^6
            sage: f^4
            2^8 * 5^8

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 39*x - 91)                                  # needs sage.rings.number_field
            sage: F = K.factor(7); F                                                    # needs sage.rings.number_field
            (Fractional ideal (7, a)) * (Fractional ideal (7, a + 2)) * (Fractional ideal (7, a - 2))
            sage: F^9                                                                   # needs sage.rings.number_field
            (Fractional ideal (7, a))^9 * (Fractional ideal (7, a + 2))^9 * (Fractional ideal (7, a - 2))^9

            sage: R.<x,y> = FreeAlgebra(ZZ, 2)                                          # needs sage.combinat sage.modules
            sage: F = Factorization([(x,3), (y, 2), (x,1)]); F                          # needs sage.combinat sage.modules
            x^3 * y^2 * x
            sage: F**2                                                                  # needs sage.combinat sage.modules
            x^3 * y^2 * x^4 * y^2 * x
        """
    def __invert__(self):
        """
        Return the formal inverse of the factors in the factorization.

        EXAMPLES::

            sage: F = factor(2006); F
            2 * 17 * 59
            sage: F^-1
            2^-1 * 17^-1 * 59^-1

            sage: R.<x,y> = FreeAlgebra(QQ, 2)                                          # needs sage.combinat sage.modules
            sage: F = Factorization([(x,3), (y, 2), (x,1)], 2); F                       # needs sage.combinat sage.modules
            (2) * x^3 * y^2 * x
            sage: F^-1                                                                  # needs sage.combinat sage.modules
            (1/2) * x^-1 * y^-2 * x^-3
        """
    def __truediv__(self, other):
        """
        Return the quotient of two factorizations, which is obtained by
        multiplying the first by the inverse of the second.

        EXAMPLES::

            sage: factor(-10) / factor(-16)
            2^-3 * 5
            sage: factor(-10) / factor(16)
            -1 * 2^-3 * 5

            sage: # needs sage.combinat sage.modules
            sage: R.<x,y> = FreeAlgebra(QQ, 2)
            sage: F = Factorization([(x,3), (y, 2), (x,1)]); F
            x^3 * y^2 * x
            sage: G = Factorization([(y, 1), (x,1)],1); G
            y * x
            sage: F / G
            x^3 * y
        """
    def __call__(self, *args, **kwds):
        """
        Implement the substitution.

        This is assuming that each term can be substituted.

        There is another mechanism for substitution
        in symbolic products.

        EXAMPLES::

            sage: # needs sage.combinat sage.modules
            sage: R.<x,y> = FreeAlgebra(QQ, 2)
            sage: F = Factorization([(x,3), (y, 2), (x,1)])
            sage: F(x=4)
            4^3 * y^2 * 4
            sage: F.subs({y:2})
            x^3 * 2^2 * x

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: F = Factorization([(x,3), (y, 2), (x,1)])
            sage: F(x=4)
            4 * 4^3 * y^2
            sage: F.subs({y:x})
            x * x^2 * x^3
            sage: F(x=y+x)
            (x + y) * y^2 * (x + y)^3

        TESTS::

            sage: R.<x,y> = PolynomialRing(QQ, 2)
            sage: F = Factorization([(x-2,3), (y+3, 2)])
            sage: F(x=2)
            0

            sage: QQt = QQ['t'].fraction_field()
            sage: t = QQt.gen()
            sage: R.<x> = PolynomialRing(QQt, 1)
            sage: F = Factorization([(x,3), (x+t, 2)], unit=QQt.gen())
            sage: F(t=0)
            0

            sage: # needs sage.libs.pari sage.modules
            sage: R.<x> = LaurentPolynomialRing(QQ, 1)
            sage: F = ((x+2)/x**3).factor()
            sage: F(x=4)
            1/64 * 6
        """
    subs = __call__
    def value(self):
        """
        Return the product of the factors in the factorization, multiplied out.

        EXAMPLES::

            sage: F = factor(-2006); F
            -1 * 2 * 17 * 59
            sage: F.value()
            -2006

            sage: R.<x,y> = FreeAlgebra(ZZ, 2)                                          # needs sage.combinat sage.modules
            sage: F = Factorization([(x,3), (y, 2), (x,1)]); F                          # needs sage.combinat sage.modules
            x^3 * y^2 * x
            sage: F.value()                                                             # needs sage.combinat sage.modules
            x^3*y^2*x
        """
    expand = value
    prod = value
    def gcd(self, other):
        """
        Return the gcd of two factorizations.

        If the two factorizations have different universes, this
        method will attempt to find a common universe for the
        gcd.  A :exc:`TypeError` is raised if this is impossible.

        EXAMPLES::

            sage: factor(-30).gcd(factor(-160))
            2 * 5
            sage: factor(gcd(-30,160))
            2 * 5

            sage: R.<x> = ZZ[]
            sage: (factor(-20).gcd(factor(5*x+10))).universe()                          # needs sage.libs.pari
            Univariate Polynomial Ring in x over Integer Ring
        """
    def lcm(self, other):
        """
        Return the lcm of two factorizations.

        If the two factorizations have different universes, this
        method will attempt to find a common universe for the
        lcm.  A :exc:`TypeError` is raised if this is impossible.

        EXAMPLES::

            sage: factor(-10).lcm(factor(-16))
            2^4 * 5
            sage: factor(lcm(-10,16))
            2^4 * 5

            sage: R.<x> = ZZ[]
            sage: (factor(-20).lcm(factor(5*x + 10))).universe()                        # needs sage.libs.pari
            Univariate Polynomial Ring in x over Integer Ring
        """
    def is_integral(self) -> bool:
        """
        Return whether all exponents of this Factorization are nonnegative.

        EXAMPLES::

            sage: F = factor(-10); F
            -1 * 2 * 5
            sage: F.is_integral()
            True

            sage: F = factor(-10) / factor(16); F
            -1 * 2^-3 * 5
            sage: F.is_integral()
            False
        """
    def radical(self):
        """
        Return the factorization of the radical of the value of ``self``.

        First, check that all exponents in the factorization are
        positive, raise :exc:`ValueError` otherwise.  If all exponents are
        positive, return ``self`` with all exponents set to 1 and with the
        unit set to 1.

        EXAMPLES::

            sage: F = factor(-100); F
            -1 * 2^2 * 5^2
            sage: F.radical()
            2 * 5
            sage: factor(1/2).radical()
            Traceback (most recent call last):
            ...
            ValueError: all exponents in the factorization must be positive
        """
    def radical_value(self):
        """
        Return the product of the prime factors in ``self``.

        First, check that all exponents in the factorization are
        positive, raise :exc:`ValueError` otherwise.  If all exponents are
        positive, return the product of the prime factors in ``self``.
        This should be functionally equivalent to
        ``self.radical().value()``.

        EXAMPLES::

            sage: F = factor(-100); F
            -1 * 2^2 * 5^2
            sage: F.radical_value()
            10
            sage: factor(1/2).radical_value()
            Traceback (most recent call last):
            ...
            ValueError: all exponents in the factorization must be positive
        """
