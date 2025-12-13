from .commutative_polynomial import CommutativePolynomial as CommutativePolynomial
from .multi_polynomial import MPolynomial as MPolynomial
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import RingElement as RingElement
from sage.structure.richcmp import richcmp as richcmp

class InfinitePolynomial(CommutativePolynomial, metaclass=InheritComparisonClasscallMetaclass):
    """
    Create an element of a Polynomial Ring with a Countably Infinite Number of Variables.

    Usually, an InfinitePolynomial is obtained by using the generators
    of an Infinite Polynomial Ring (see :mod:`~sage.rings.polynomial.infinite_polynomial_ring`)
    or by conversion.

    INPUT:

    - ``A`` -- an Infinite Polynomial Ring
    - ``p`` -- a *classical* polynomial that can be interpreted in ``A``

    ASSUMPTIONS:

    In the dense implementation, it must be ensured that the argument
    ``p`` coerces into ``A._P`` by a name preserving conversion map.

    In the sparse implementation, in the direct construction of an
    infinite polynomial, it is *not* tested whether the argument ``p``
    makes sense in ``A``.

    EXAMPLES::

        sage: from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial
        sage: X.<alpha> = InfinitePolynomialRing(ZZ)
        sage: P.<alpha_1,alpha_2> = ZZ[]

    Currently, ``P`` and ``X._P`` (the underlying polynomial ring of
    ``X``) both have two variables::

        sage: X._P
        Multivariate Polynomial Ring in alpha_1, alpha_0 over Integer Ring

    By default, a coercion from ``P`` to  ``X._P`` would not be name preserving.
    However, this is taken care for; a name preserving conversion is impossible,
    and by consequence an error is raised::

        sage: InfinitePolynomial(X, (alpha_1+alpha_2)^2)
        Traceback (most recent call last):
        ...
        TypeError: Could not find a mapping of the passed element to this ring.

    When extending the underlying polynomial ring, the construction of
    an infinite polynomial works::

        sage: alpha[2]
        alpha_2
        sage: InfinitePolynomial(X, (alpha_1+alpha_2)^2)
        alpha_2^2 + 2*alpha_2*alpha_1 + alpha_1^2

    In the sparse implementation, it is not checked whether the
    polynomial really belongs to the parent, and when it does not,
    the results may be unexpected due to coercions::

        sage: Y.<alpha,beta> = InfinitePolynomialRing(GF(2), implementation='sparse')
        sage: a = (alpha_1+alpha_2)^2
        sage: InfinitePolynomial(Y, a)
        alpha_0^2 + beta_0^2

    However, it is checked when doing a conversion::

        sage: Y(a)
        alpha_2^2 + alpha_1^2
    """
    @staticmethod
    def __classcall_private__(cls, A, p):
        """
        TESTS::

            sage: from sage.rings.polynomial.infinite_polynomial_element import InfinitePolynomial
            sage: X.<x,y> = InfinitePolynomialRing(ZZ, implementation='sparse')
            sage: xy = (x[0] + y[0]).polynomial()
            sage: xy.parent()
            Multivariate Polynomial Ring in x_1, x_0, y_1, y_0 over Integer Ring
            sage: sparse_xy = InfinitePolynomial(X, xy); sparse_xy
            x_0 + y_0
            sage: isinstance(sparse_xy, InfinitePolynomial)
            True
            sage: type(sparse_xy)
            <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_sparse'>
            sage: X.<x,y> = InfinitePolynomialRing(ZZ, implementation='dense')
            sage: dense_xy = InfinitePolynomial(X, xy); dense_xy
            x_0 + y_0
            sage: isinstance(dense_xy, InfinitePolynomial)
            True
            sage: type(dense_xy)
            <class 'sage.rings.polynomial.infinite_polynomial_element.InfinitePolynomial_dense'>
        """
    def __init__(self, A, p) -> None:
        """
        TESTS::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: a = x[1] + x[2]
            sage: a == loads(dumps(a))
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: a = x[0] + x[1]
            sage: b = 1 + 4*x[1]
            sage: hash(a) != hash(b)
            True
        """
    def polynomial(self):
        """
        Return the underlying polynomial.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(GF(7))
            sage: p = x[2]*y[1] + 3*y[0]
            sage: p
            x_2*y_1 + 3*y_0
            sage: p.polynomial()
            x_2*y_1 + 3*y_0
            sage: p.polynomial().parent()
            Multivariate Polynomial Ring in x_2, x_1, x_0, y_2, y_1, y_0
             over Finite Field of size 7
            sage: p.parent()
            Infinite polynomial ring in x, y over Finite Field of size 7
        """
    def __dir__(self):
        """
        This method implements tab completion, see :issue:`6854`.

        TESTS::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: import sage.interfaces.tab_completion as s
            sage: p = x[3]*x[2]
            sage: s.completions('p.co',globals()) # indirect doc test
            ['p.coefficient',
             'p.coefficients',
             'p.constant_coefficient',
             'p.content',
             'p.content_ideal']
            sage: 'constant_coefficient' in dir(p) # indirect doctest
            True
        """
    def __getattr__(self, s):
        """
        NOTE:

        This method will only be called if an attribute of ``self``
        is requested that is not known to Python. In that case,
        the corresponding attribute of the underlying polynomial
        of ``self`` is returned.

        EXAMPLES:

        Elements of Infinite Polynomial Rings have no genuine
        ``_latex_`` method. But the method inherited from the
        underlying polynomial suffices::

            sage: X.<alpha> = InfinitePolynomialRing(QQ)
            sage: latex(alpha[3]*alpha[2]^2) # indirect doctest
            \x07lpha_{3} \x07lpha_{2}^{2}

        Related with issues :issue:`6854` and :issue:`7580`, the attribute
        ``__methods__`` is treated in a special way, which
        makes introspection and tab completion work::

            sage: import sage.interfaces.tab_completion as s
            sage: p = alpha[3]*alpha[2]^2
            sage: s.completions('p.co',globals()) # indirect doc test
            ['p.coefficient',
             'p.coefficients',
             'p.constant_coefficient',
             'p.content',
             'p.content_ideal']
            sage: 'constant_coefficient' in dir(p) # indirect doctest
            True
        """
    def subs(self, fixed=None, **kwargs):
        """
        Substitute variables in ``self``.

        INPUT:

        - ``fixed`` -- (optional) ``dict`` with ``{variable: value}`` pairs
        - ``**kwargs`` -- named parameters

        OUTPUT: the resulting substitution

        EXAMPLES::

            sage: R.<x,y> = InfinitePolynomialRing(QQ)
            sage: f = x[1] + x[1]*x[2]*x[3]

        Passing ``fixed={x[1]: x[0]}``. Note that the keys may be given
        using the generators of the infinite polynomial ring
        or as a string::

            sage: f.subs({x[1]: x[0]})
            x_3*x_2*x_0 + x_0
            sage: f.subs({'x_1': x[0]})
            x_3*x_2*x_0 + x_0

        Passing the variables as names parameters::

            sage: f.subs(x_1=y[1])
            x_3*x_2*y_1 + y_1
            sage: f.subs(x_1=y[1], x_2=2)
            2*x_3*y_1 + y_1

        The substitution returns the original polynomial if you try
        to substitute a variable not present::

            sage: g = x[0] + x[1]
            sage: g.subs({y[0]: x[0]})
            x_1 + x_0

        The substitution can also handle matrices::

            sage: # needs sage.modules
            sage: M = matrix([[1,0], [0,2]])
            sage: N = matrix([[0,3], [4,0]])
            sage: g = x[0]^2 + 3*x[1]
            sage: g.subs({'x_0': M})
            [3*x_1 + 1         0]
            [        0 3*x_1 + 4]
            sage: g.subs({x[0]: M, x[1]: N})
            [ 1  9]
            [12  4]

        If you pass both ``fixed`` and ``kwargs``, any conflicts
        will defer to ``fixed``::

            sage: R.<x,y> = InfinitePolynomialRing(QQ)
            sage: f = x[0]
            sage: f.subs({x[0]: 1})
            1
            sage: f.subs(x_0=5)
            5
            sage: f.subs({x[0]: 1}, x_0=5)
            1

        TESTS::

            sage: # needs sage.modules
            sage: g.subs(fixed=x[0], x_1=N)
            Traceback (most recent call last):
            ...
            ValueError: fixed must be a dict
        """
    def ring(self):
        """
        The ring which ``self`` belongs to.

        This is the same as ``self.parent()``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(ZZ,implementation='sparse')
            sage: p = x[100]*y[1]^3*x[1]^2 + 2*x[10]*y[30]
            sage: p.ring()
            Infinite polynomial ring in x, y over Integer Ring
        """
    def is_unit(self):
        """
        Answer whether ``self`` is a unit.

        EXAMPLES::

            sage: R1.<x,y> = InfinitePolynomialRing(ZZ)
            sage: R2.<a,b> = InfinitePolynomialRing(QQ)
            sage: (1 + x[2]).is_unit()
            False
            sage: R1(1).is_unit()
            True
            sage: R1(2).is_unit()
            False
            sage: R2(2).is_unit()
            True
            sage: (1 + a[2]).is_unit()
            False

        Check that :issue:`22454` is fixed::

            sage: _.<x> = InfinitePolynomialRing(Zmod(4))
            sage: (1 + 2*x[0]).is_unit()
            True
            sage: (x[0]*x[1]).is_unit()
            False
            sage: _.<x> = InfinitePolynomialRing(Zmod(900))
            sage: (7+150*x[0] + 30*x[1] + 120*x[1]*x[100]).is_unit()
            True

        TESTS::

            sage: R.<x> = InfinitePolynomialRing(ZZ.quotient_ring(8))
            sage: [R(i).is_unit() for i in range(8)]
            [False, True, False, True, False, True, False, True]
        """
    def is_nilpotent(self):
        """
        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x> = InfinitePolynomialRing(QQbar)                                 # needs sage.rings.number_field
            sage: (x[0] + x[1]).is_nilpotent()                                          # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x> = InfinitePolynomialRing(Zmod(4))
            sage: (2*x[0]).is_nilpotent()
            True
            sage: (2+x[4]*x[7]).is_nilpotent()
            False
            sage: _.<y> = InfinitePolynomialRing(Zmod(100))
            sage: (5+2*y[0] + 10*(y[0]^2+y[1]^2)).is_nilpotent()
            False
            sage: (10*y[2] + 20*y[5] - 30*y[2]*y[5] + 70*(y[2]^2+y[5]^2)).is_nilpotent()
            True
        """
    def numerator(self):
        """
        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        .. WARNING::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since it is a
           polynomial.

        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: p = 2/3*x[1] + 4/9*x[2] - 2*x[1]*x[3]
            sage: num = p.numerator(); num
            -18*x_3*x_1 + 4*x_2 + 6*x_1

        TESTS::

            sage: num.parent()
            Infinite polynomial ring in x over Rational Field

        Check that :issue:`37756` is fixed::

            sage: R.<a> = InfinitePolynomialRing(QQ)
            sage: P.<x,y> = QQ[]
            sage: FF = P.fraction_field()
            sage: FF(a[0])
            Traceback (most recent call last):
            ...
            TypeError: Could not find a mapping of the passed element to this ring.
        """
    @cached_method
    def variables(self):
        """
        Return the variables occurring in ``self`` (tuple of elements of some polynomial ring).

        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: p = x[1] + x[2] - 2*x[1]*x[3]
            sage: p.variables()
            (x_3, x_2, x_1)
            sage: x[1].variables()
            (x_1,)
            sage: X(1).variables()
            ()
        """
    def monomials(self):
        """
        Return the list of monomials in ``self``.

        The returned list is decreasingly ordered by the term ordering of
        ``self.parent()``.

        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: p = x[1]^3 + x[2] - 2*x[1]*x[3]
            sage: p.monomials()
            [x_3*x_1, x_2, x_1^3]

            sage: X.<x> = InfinitePolynomialRing(QQ, order='deglex')
            sage: p = x[1]^3 + x[2] - 2*x[1]*x[3]
            sage: p.monomials()
            [x_1^3, x_3*x_1, x_2]
        """
    def monomial_coefficient(self, mon):
        """
        Return the base ring element that is the coefficient of ``mon``
        in ``self``.

        This function contrasts with the function :meth:`coefficient`,
        which returns the coefficient of a monomial viewing this
        polynomial in a polynomial ring over a base ring having fewer
        variables.

        INPUT:

        - ``mon`` -- a monomial in the parent of ``self``

        OUTPUT: coefficient in base ring

        .. SEEALSO::

            For coefficients in a base ring of fewer variables,
            look at :meth:`coefficient`.

        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: f = 2*x[0]*x[2] + 3*x[1]^2
            sage: c = f.monomial_coefficient(x[1]^2); c
            3
            sage: c.parent()
            Rational Field

            sage: c = f.coefficient(x[2]); c
            2*x_0
            sage: c.parent()
            Infinite polynomial ring in x over Rational Field
        """
    @cached_method
    def max_index(self):
        """
        Return the maximal index of a variable occurring in ``self``, or -1 if ``self`` is scalar.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = x[1]^2 + y[2]^2 + x[1]*x[2]*y[3] + x[1]*y[4]
            sage: p.max_index()
            4
            sage: x[0].max_index()
            0
            sage: X(10).max_index()
            -1
        """
    @cached_method
    def lm(self):
        """
        The leading monomial of ``self``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = 2*x[10]*y[30] + x[10]*y[1]^3*x[1]^2
            sage: p.lm()
            x_10*x_1^2*y_1^3
        """
    @cached_method
    def lc(self):
        """
        The coefficient of the leading term of ``self``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = 2*x[10]*y[30] + 3*x[10]*y[1]^3*x[1]^2
            sage: p.lc()
            3
        """
    @cached_method
    def lt(self):
        """
        The leading term (= product of coefficient and monomial) of ``self``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = 2*x[10]*y[30] + 3*x[10]*y[1]^3*x[1]^2
            sage: p.lt()
            3*x_10*x_1^2*y_1^3
        """
    def tail(self):
        """
        The tail of ``self`` (this is ``self`` minus its leading term).

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = 2*x[10]*y[30] + 3*x[10]*y[1]^3*x[1]^2
            sage: p.tail()
            2*x_10*y_30
        """
    def squeezed(self):
        """
        Reduce the variable indices occurring in ``self``.

        OUTPUT:

        Apply a permutation to ``self`` that does not change the order of
        the variable indices of ``self`` but squeezes them into the range
        1,2,...

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ,implementation='sparse')
            sage: p = x[1]*y[100] + x[50]*y[1000]
            sage: p.squeezed()
            x_2*y_4 + x_1*y_3
        """
    def footprint(self):
        """
        Leading exponents sorted by index and generator.

        OUTPUT: ``D``; dictionary whose keys are the occurring variable indices

        ``D[s]`` is a list ``[i_1,...,i_n]``, where ``i_j`` gives the
        exponent of ``self.parent().gen(j)[s]`` in the leading
        term of ``self``.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = x[30]*y[1]^3*x[1]^2 + 2*x[10]*y[30]
            sage: sorted(p.footprint().items())
            [(1, [2, 3]), (30, [1, 0])]

        TESTS:

        This is a test whether it also works when the underlying polynomial ring is
        not implemented in libsingular::

            sage: X.<x> = InfinitePolynomialRing(ZZ)
            sage: Y.<y,z> = X[]
            sage: Z.<a> = InfinitePolynomialRing(Y)
            sage: Z
            Infinite polynomial ring in a over Multivariate Polynomial Ring in y, z over Infinite polynomial ring in x over Integer Ring
            sage: type(Z._P)
            <class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_with_category'>
            sage: p = a[12]^3*a[2]^7*a[4] + a[4]*a[2]
            sage: sorted(p.footprint().items())
            [(2, [7]), (4, [1]), (12, [3])]
        """
    def symmetric_cancellation_order(self, other):
        """
        Comparison of leading terms by Symmetric Cancellation Order, `<_{sc}`.

        INPUT:

        - ``self``, ``other`` -- two Infinite Polynomials

        ASSUMPTION:

        Both Infinite Polynomials are nonzero.

        OUTPUT:

        ``(c, sigma, w)``, where

        * c = -1,0,1, or None if the leading monomial of ``self`` is smaller, equal,
          greater, or incomparable with respect to ``other`` in the monomial
          ordering of the Infinite Polynomial Ring
        * sigma is a permutation witnessing
          ``self`` `<_{sc}` ``other`` (resp. ``self`` `>_{sc}` ``other``)
          or is 1 if ``self.lm()==other.lm()``
        * w is 1 or is a term so that
          ``w*self.lt()^sigma == other.lt()`` if `c\\le 0`, and
          ``w*other.lt()^sigma == self.lt()`` if `c=1`

        THEORY:

        If the Symmetric Cancellation Order is a well-quasi-ordering
        then computation of Groebner bases always terminates. This is
        the case, e.g., if the monomial order is lexicographic. For
        that reason, lexicographic order is our default order.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: (x[2]*x[1]).symmetric_cancellation_order(x[2]^2)
            (None, 1, 1)
            sage: (x[2]*x[1]).symmetric_cancellation_order(x[2]*x[3]*y[1])
            (-1, [2, 3, 1], y_1)
            sage: (x[2]*x[1]*y[1]).symmetric_cancellation_order(x[2]*x[3]*y[1])
            (None, 1, 1)
            sage: (x[2]*x[1]*y[1]).symmetric_cancellation_order(x[2]*x[3]*y[2])
            (-1, [2, 3, 1], 1)
        """
    def coefficient(self, monomial):
        """
        Return the coefficient of a monomial in this polynomial.

        INPUT:

        - A monomial (element of the parent of self) or
        - a dictionary that describes a monomial (the keys
          are variables of the parent of self, the values
          are the corresponding exponents)

        EXAMPLES:

        We can get the coefficient in front of monomials::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: a = 2*x[0]*x[1] + x[1] + x[2]
            sage: a.coefficient(x[0])
            2*x_1
            sage: a.coefficient(x[1])
            2*x_0 + 1
            sage: a.coefficient(x[2])
            1
            sage: a.coefficient(x[0]*x[1])
            2

        We can also pass in a dictionary::

            sage: a.coefficient({x[0]:1, x[1]:1})
            2
        """
    def reduce(self, I, tailreduce: bool = False, report=None):
        """
        Symmetrical reduction of ``self`` with respect to a symmetric ideal (or list of Infinite Polynomials).

        INPUT:

        - ``I`` -- a :class:`~sage.rings.polynomial.symmetric_ideal.SymmetricIdeal` or a list
          of Infinite Polynomials
        - ``tailreduce`` -- boolean (default: ``False``); *tail reduction* is performed if this
          parameter is ``True``.
        - ``report`` -- object (default: ``None``); if not ``None``, some information on the
          progress of computation is printed, since reduction of huge polynomials may take
          a long time

        OUTPUT: symmetrical reduction of ``self`` with respect to ``I``, possibly with tail reduction

        THEORY:

        Reducing an element `p` of an Infinite Polynomial Ring `X` by
        some other element `q` means the following:

        1. Let `M` and `N` be the leading terms of `p` and `q`.
        2. Test whether there is a permutation `P` that does not does not diminish the variable
           indices occurring in `N` and preserves their order, so that there is some term `T\\in X`
           with `TN^P = M`. If there is no such permutation, return `p`
        3. Replace `p` by `p-T q^P` and continue with step 1.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: p = y[1]^2*y[3] + y[2]*x[3]^3
            sage: p.reduce([y[2]*x[1]^2])
            x_3^3*y_2 + y_3*y_1^2

        The preceding is correct: If a permutation turns
        ``y[2]*x[1]^2`` into a factor of the leading monomial
        ``y[2]*x[3]^3`` of ``p``, then it interchanges the variable
        indices 1 and 2; this is not allowed in a symmetric
        reduction. However, reduction by ``y[1]*x[2]^2`` works, since
        one can change variable index 1 into 2 and 2 into 3::

            sage: p.reduce([y[1]*x[2]^2])                                               # needs sage.libs.singular
            y_3*y_1^2

        The next example shows that tail reduction is not done, unless
        it is explicitly advised.  The input can also be a Symmetric
        Ideal::

            sage: I = (y[3])*X
            sage: p.reduce(I)
            x_3^3*y_2 + y_3*y_1^2
            sage: p.reduce(I, tailreduce=True)                                          # needs sage.libs.singular
            x_3^3*y_2

        Last, we demonstrate the ``report`` option::

            sage: p = x[1]^2 + y[2]^2 + x[1]*x[2]*y[3] + x[1]*y[4]
            sage: p.reduce(I, tailreduce=True, report=True)                             # needs sage.libs.singular
            :T[2]:>
            >
            x_1^2 + y_2^2

        The output ':' means that there was one reduction of the
        leading monomial. 'T[2]' means that a tail reduction was
        performed on a polynomial with two terms. At '>', one round of
        the reduction process is finished (there could only be several
        non-trivial rounds if `I` was generated by more than one
        polynomial).
        """
    def stretch(self, k):
        """
        Stretch ``self`` by a given factor.

        INPUT:

        - ``k`` -- integer

        OUTPUT: replace `v_n` with `v_{n\\cdot k}` for all generators `v_\\ast`
        occurring in ``self``

        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: a = x[0] + x[1] + x[2]
            sage: a.stretch(2)
            x_4 + x_2 + x_0

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: a = x[0] + x[1] + y[0]*y[1]; a
            x_1 + x_0 + y_1*y_0
            sage: a.stretch(2)
            x_2 + x_0 + y_2*y_0

        TESTS:

        The following would hardly work in a dense implementation,
        because an underlying polynomial ring with 6001 variables
        would be created. This is avoided in the sparse
        implementation::

            sage: X.<x> = InfinitePolynomialRing(QQ, implementation='sparse')
            sage: a = x[2] + x[3]
            sage: a.stretch(2000)
            x_6000 + x_4000
        """
    def __iter__(self):
        """
        Return an iterator over all pairs ``(coefficient, monomial)``
        of this polynomial.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: a = x[0] + 2*x[1] + y[0]*y[1]
            sage: list(a)
            [(2, x_1), (1, x_0), (1, y_1*y_0)]
        """
    def gcd(self, x):
        """
        Compute the greatest common divisor.

        EXAMPLES::

            sage: R.<x> = InfinitePolynomialRing(QQ)
            sage: p1 = x[0] + x[1]^2
            sage: gcd(p1, p1 + 3)
            1
            sage: gcd(p1, p1) == p1
            True
        """

class InfinitePolynomial_sparse(InfinitePolynomial):
    """
    Element of a sparse Polynomial Ring with a Countably Infinite Number of Variables.

    INPUT:

    - ``A`` -- an Infinite Polynomial Ring in sparse implementation
    - ``p`` -- a *classical* polynomial that can be interpreted in ``A``

    Of course, one should not directly invoke this class, but rather
    construct elements of ``A`` in the usual way.

    EXAMPLES::

        sage: A.<a> = QQ[]
        sage: B.<b,c> = InfinitePolynomialRing(A,implementation='sparse')
        sage: p = a*b[100] + 1/2*c[4]
        sage: p
        a*b_100 + 1/2*c_4
        sage: p.parent()
        Infinite polynomial ring in b, c
         over Univariate Polynomial Ring in a over Rational Field
        sage: p.polynomial().parent()
        Multivariate Polynomial Ring in b_100, b_0, c_4, c_0
         over Univariate Polynomial Ring in a over Rational Field
    """
    def __call__(self, *args, **kwargs):
        """
        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ,implementation='sparse')
            sage: a = x[0] + x[1]
            sage: a(x_0=2,x_1=x[1])
            x_1 + 2
            sage: _.parent()
            Infinite polynomial ring in x over Rational Field
            sage: a(x_1=3)
            x_0 + 3
            sage: _.parent()
            Infinite polynomial ring in x over Rational Field
            sage: a(x_1=x[100])
            x_100 + x_0

            sage: M = matrix([[1,1], [2,0]])                                            # needs sage.modules
            sage: a(x_1=M)                                                              # needs sage.modules
            [x_0 + 1       1]
            [      2     x_0]
        """
    def __pow__(self, n):
        """
        Exponentiation by an integer, or action by a callable object.

        NOTE:

        The callable object must accept nonnegative integers as input
        and return nonnegative integers. Typical use case is a
        permutation, that will result in the corresponding permutation
        of variables.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ, implementation='sparse')
            sage: p = x[10]*y[2] + 2*x[1]*y[3]
            sage: P = Permutation(((1,2),(3,4,5)))
            sage: p^P # indirect doctest
            x_10*y_1 + 2*x_2*y_4
        """

class InfinitePolynomial_dense(InfinitePolynomial):
    """
    Element of a dense Polynomial Ring with a Countably Infinite Number of Variables.

    INPUT:

    - ``A`` -- an Infinite Polynomial Ring in dense implementation
    - ``p`` -- a *classical* polynomial that can be interpreted in ``A``

    Of course, one should not directly invoke this class, but rather
    construct elements of ``A`` in the usual way.
    """
    def __call__(self, *args, **kwargs):
        """
        EXAMPLES::

            sage: X.<x> = InfinitePolynomialRing(QQ)
            sage: a = x[0] + x[1]
            sage: a(x_0=2, x_1=x[1])
            x_1 + 2
            sage: _.parent()
            Infinite polynomial ring in x over Rational Field
            sage: a(x_1=3)
            x_0 + 3
            sage: _.parent()
            Infinite polynomial ring in x over Rational Field

            sage: a(x_1=x[100])
            x_100 + x_0
        """
    def __pow__(self, n):
        """
        Exponentiation by an integer, or action by a callable object.

        NOTE:

        The callable object must accept nonnegative integers as input
        and return nonnegative integers. Typical use case is a
        permutation, that will result in the corresponding permutation
        of variables.

        EXAMPLES::

            sage: X.<x,y> = InfinitePolynomialRing(QQ)
            sage: x[10]^3
            x_10^3
            sage: p = x[10]*y[2] + 2*x[1]*y[3]
            sage: P = Permutation(((1,2),(3,4,5)))
            sage: p^P
            x_10*y_1 + 2*x_2*y_4
        """
