from .misc import WithLocals as WithLocals
from _typeshed import Incomplete
from sage.categories.pushout import ConstructionFunctor as ConstructionFunctor
from sage.misc.defaults import series_precision as series_precision
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.real_mpfi import RIF as RIF
from sage.structure.element import CommutativeAlgebraElement as CommutativeAlgebraElement
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NoConvergenceError(RuntimeError):
    """
    A special :python:`RuntimeError<library/exceptions.html#exceptions.RuntimeError>`
    which is raised when an algorithm does not converge/stop.
    """

class AsymptoticExpansion(CommutativeAlgebraElement):
    """
    Class for asymptotic expansions, i.e., the elements of an
    :class:`AsymptoticRing`.

    INPUT:

    - ``parent`` -- the parent of the asymptotic expansion

    - ``summands`` -- the summands as a
      :class:`~sage.data_structures.mutable_poset.MutablePoset`, which
      represents the underlying structure

    - ``simplify`` -- boolean (default: ``True``); it controls
      automatic simplification (absorption) of the asymptotic expansion

    - ``convert`` -- boolean (default: ``True``); if set, then the
      ``summands`` are converted to the asymptotic ring (the parent of this
      expansion). If not, then the summands are taken as they are. In
      that case, the caller must ensure that the parent of the terms is
      set correctly.

    EXAMPLES:

    There are several ways to create asymptotic expansions; usually
    this is done by using the corresponding :class:`asymptotic rings <AsymptoticRing>`::

        sage: R_x.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=QQ); R_x
        Asymptotic Ring <x^QQ> over Rational Field
        sage: R_y.<y> = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=ZZ); R_y
        Asymptotic Ring <y^ZZ> over Integer Ring

    At this point, `x` and `y` are already asymptotic expansions::

        sage: type(x)
        <class 'sage.rings.asymptotic.asymptotic_ring.AsymptoticRing_with_category.element_class'>

    The usual ring operations, but allowing rational exponents (growth
    group ``x^QQ``) can be performed::

        sage: x^2 + 3*(x - x^(2/5))
        x^2 + 3*x - 3*x^(2/5)
        sage: (3*x^(1/3) + 2)^3
        27*x + 54*x^(2/3) + 36*x^(1/3) + 8

    One of the central ideas behind computing with asymptotic
    expansions is that the `O`-notation (see
    :wikipedia:`Big_O_notation`) can be used. For example, we have::

        sage: (x+2*x^2+3*x^3+4*x^4) * (O(x)+x^2)
        4*x^6 + O(x^5)

    In particular, :func:`~sage.rings.big_oh.O` can be used to
    construct the asymptotic expansions. With the help of the
    :meth:`summands`, we can also have a look at the inner structure
    of an asymptotic expansion::

        sage: expr1 = x + 2*x^2 + 3*x^3 + 4*x^4; expr2 = O(x) + x^2
        sage: print(expr1.summands.repr_full())
        poset(x, 2*x^2, 3*x^3, 4*x^4)
        +-- null
        |   +-- no predecessors
        |   +-- successors:   x
        +-- x
        |   +-- predecessors:   null
        |   +-- successors:   2*x^2
        +-- 2*x^2
        |   +-- predecessors:   x
        |   +-- successors:   3*x^3
        +-- 3*x^3
        |   +-- predecessors:   2*x^2
        |   +-- successors:   4*x^4
        +-- 4*x^4
        |   +-- predecessors:   3*x^3
        |   +-- successors:   oo
        +-- oo
        |   +-- predecessors:   4*x^4
        |   +-- no successors
        sage: print(expr2.summands.repr_full())
        poset(O(x), x^2)
        +-- null
        |   +-- no predecessors
        |   +-- successors:   O(x)
        +-- O(x)
        |   +-- predecessors:   null
        |   +-- successors:   x^2
        +-- x^2
        |   +-- predecessors:   O(x)
        |   +-- successors:   oo
        +-- oo
        |   +-- predecessors:   x^2
        |   +-- no successors
        sage: print((expr1 * expr2).summands.repr_full())
        poset(O(x^5), 4*x^6)
        +-- null
        |   +-- no predecessors
        |   +-- successors:   O(x^5)
        +-- O(x^5)
        |   +-- predecessors:   null
        |   +-- successors:   4*x^6
        +-- 4*x^6
        |   +-- predecessors:   O(x^5)
        |   +-- successors:   oo
        +-- oo
        |   +-- predecessors:   4*x^6
        |   +-- no successors

    In addition to the monomial growth elements from above, we can
    also compute with logarithmic terms (simply by constructing the
    appropriate growth group)::

        sage: R_log = AsymptoticRing(growth_group='log(x)^QQ', coefficient_ring=QQ)
        sage: lx = R_log(log(SR.var('x')))
        sage: (O(lx) + lx^3)^4
        log(x)^12 + O(log(x)^10)

    .. SEEALSO::

        :doc:`growth_group`,
        :doc:`term_monoid`,
        :mod:`~sage.data_structures.mutable_poset`.
    """
    def __init__(self, parent, summands, simplify: bool = True, convert: bool = True) -> None:
        """
        See :class:`AsymptoticExpansion` for more information.

        TESTS::

            sage: R_x.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: R_y.<y> = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=ZZ)
            sage: R_x is R_y
            False
            sage: ex1 = x + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
            sage: ex2 = x + O(R_x(1))
            sage: ex1 * ex2
            5*x^6 + O(x^5)

        ::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory as TermMonoid
            sage: G = GrowthGroup('x^ZZ'); x = G.gen()
            sage: OT = TermMonoid('O', G, ZZ); ET = TermMonoid('exact', G, ZZ)
            sage: R = AsymptoticRing(G, ZZ)
            sage: lst = [ET(x, coefficient=1), ET(x^2, coefficient=2), OT(x^3), ET(x^4, coefficient=4)]
            sage: expr = R(lst, simplify=False); expr  # indirect doctest
            4*x^4 + O(x^3) + 2*x^2 + x
            sage: print(expr.summands.repr_full())
            poset(x, 2*x^2, O(x^3), 4*x^4)
            +-- null
            |   +-- no predecessors
            |   +-- successors:   x
            +-- x
            |   +-- predecessors:   null
            |   +-- successors:   2*x^2
            +-- 2*x^2
            |   +-- predecessors:   x
            |   +-- successors:   O(x^3)
            +-- O(x^3)
            |   +-- predecessors:   2*x^2
            |   +-- successors:   4*x^4
            +-- 4*x^4
            |   +-- predecessors:   O(x^3)
            |   +-- successors:   oo
            +-- oo
            |   +-- predecessors:   4*x^4
            |   +-- no successors
            sage: expr._simplify_(); expr
            4*x^4 + O(x^3)
            sage: print(expr.summands.repr_full())
            poset(O(x^3), 4*x^4)
            +-- null
            |   +-- no predecessors
            |   +-- successors:   O(x^3)
            +-- O(x^3)
            |   +-- predecessors:   null
            |   +-- successors:   4*x^4
            +-- 4*x^4
            |   +-- predecessors:   O(x^3)
            |   +-- successors:   oo
            +-- oo
            |   +-- predecessors:   4*x^4
            |   +-- no successors
            sage: R(lst, simplify=True) # indirect doctest
            4*x^4 + O(x^3)

        ::

            sage: R.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=QQ)
            sage: e = R(x^2 + O(x))
            sage: from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion
            sage: S = AsymptoticRing(growth_group='x^QQ', coefficient_ring=ZZ)
            sage: for s in AsymptoticExpansion(S, e.summands).summands.elements_topological():
            ....:     print(s.parent())
            O-Term Monoid x^QQ with implicit coefficients in Integer Ring
            Exact Term Monoid x^QQ with coefficients in Integer Ring
            sage: for s in AsymptoticExpansion(S, e.summands,
            ....:         convert=False).summands.elements_topological():
            ....:     print(s.parent())
            O-Term Monoid x^QQ with implicit coefficients in Rational Field
            Exact Term Monoid x^QQ with coefficients in Rational Field

        ::

            sage: AsymptoticExpansion(S, R(1/2).summands)
            Traceback (most recent call last):
            ...
            ValueError: Cannot include 1/2 with parent
            Exact Term Monoid x^QQ with coefficients in Rational Field in
            Asymptotic Ring <x^QQ> over Integer Ring
            > *previous* ValueError: Cannot create ExactTerm(1)
              since given coefficient 1/2 is not valid in
              Exact Term Monoid x^QQ with coefficients in Integer Ring.
            >> *previous* TypeError: no conversion of this rational to integer

        Check :issue:`19921`::

            sage: CR.<Z> = QQ['Z']
            sage: CR_mod = CR.quotient((Z^2 - 1)*CR)
            sage: R.<x> = AsymptoticRing(growth_group='x^NN', coefficient_ring=CR)
            sage: R_mod = R.change_parameter(coefficient_ring=CR_mod)
            sage: e = 1 + x*(Z^2-1)
            sage: R_mod(e)
            1

        Check that :issue:`19999` is resolved::

            sage: A.<x> = AsymptoticRing('(QQ_+)^x * x^QQ * UU^x', QQ)
            sage: 1 + (-1)^x + 2^x + (-2)^x
            2^x + 2^x*(-1)^x + (-1)^x + 1

            sage: A.<x> = AsymptoticRing('QQ^x * x^QQ', QQ)
            sage: 1 + (-1)^x + 2^x + (-2)^x
            2^x + 2^x*(-1)^x + (-1)^x + 1
        """
    @property
    def summands(self):
        """
        The summands of this asymptotic expansion stored in the
        underlying data structure (a
        :class:`~sage.data_structures.mutable_poset.MutablePoset`).

        EXAMPLES::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: expr = 7*x^12 + x^5 + O(x^3)
            sage: expr.summands
            poset(O(x^3), x^5, 7*x^12)

        .. SEEALSO::

            :class:`sage.data_structures.mutable_poset.MutablePoset`
        """
    def __hash__(self):
        """
        A hash value for this element.

        .. WARNING::

            This hash value uses the string representation and might not be
            always right.

        TESTS::

            sage: R_log = AsymptoticRing(growth_group='log(x)^QQ', coefficient_ring=QQ)
            sage: lx = R_log(log(SR.var('x')))
            sage: elt = (O(lx) + lx^3)^4
            sage: hash(elt) # random
            -4395085054568712393
        """
    def __bool__(self) -> bool:
        """
        Return whether this asymptotic expansion is not identically zero.

        OUTPUT: boolean

        TESTS::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: bool(R(0))  # indirect doctest
            False
            sage: bool(x)  # indirect doctest
            True
            sage: bool(7*x^12 + x^5 + O(x^3))  # indirect doctest
            True
        """
    def __eq__(self, other) -> bool:
        """
        Return whether this asymptotic expansion is equal to ``other``.

        INPUT:

        - ``other`` -- an object

        OUTPUT: boolean

        .. NOTE::

            This function uses the coercion model to find a common
            parent for the two operands.

        EXAMPLES::

            sage: R.<x> = AsymptoticRing('x^ZZ', QQ)
            sage: (1 + 2*x + 3*x^2) == (3*x^2 + 2*x + 1)  # indirect doctest
            True
            sage: O(x) == O(x)
            False

        TESTS::

            sage: x == None
            False

        ::

            sage: x == 'x'
            False
        """
    def __ne__(self, other) -> bool:
        """
        Return whether this asymptotic expansion is not equal to ``other``.

        INPUT:

        - ``other`` -- an object

        OUTPUT: boolean

        .. NOTE::

            This function uses the coercion model to find a common
            parent for the two operands.

        EXAMPLES::

            sage: R.<x> = AsymptoticRing('x^ZZ', QQ)
            sage: (1 + 2*x + 3*x^2) != (3*x^2 + 2*x + 1)  # indirect doctest
            False
            sage: O(x) != O(x)
            True

        TESTS::

            sage: x != None
            True
        """
    def has_same_summands(self, other) -> bool:
        """
        Return whether this asymptotic expansion and ``other`` have the
        same summands.

        INPUT:

        - ``other`` -- an asymptotic expansion

        OUTPUT: boolean

        .. NOTE::

            While for example ``O(x) == O(x)`` yields ``False``,
            these expansions *do* have the same summands and this method
            returns ``True``.

            Moreover, this method uses the coercion model in order to
            find a common parent for this asymptotic expansion and
            ``other``.

        EXAMPLES::

            sage: R_ZZ.<x_ZZ> = AsymptoticRing('x^ZZ', ZZ)
            sage: R_QQ.<x_QQ> = AsymptoticRing('x^ZZ', QQ)
            sage: sum(x_ZZ^k for k in range(5)) == sum(x_QQ^k for k in range(5))  # indirect doctest
            True
            sage: O(x_ZZ) == O(x_QQ)
            False

        TESTS::

            sage: x_ZZ.has_same_summands(None)
            False
        """
    def show(self) -> None:
        """
        Pretty-print this asymptotic expansion.

        OUTPUT:

        Nothing, the representation is printed directly on the
        screen.

        EXAMPLES::

            sage: A.<x> = AsymptoticRing('QQ^x * x^QQ * log(x)^QQ', SR.subring(no_variables=True))
            sage: (pi/2 * 5^x * x^(42/17) - sqrt(euler_gamma) * log(x)^(-7/8)).show()
            1/2*pi*5^x*x^(42/17) - sqrt(euler_gamma)*log(x)^(-7/8)

        TESTS::

            sage: A.<x> = AsymptoticRing('(e^x)^QQ * x^QQ', SR.subring(no_variables=True))
            sage: (zeta(3) * (e^x)^(-1/2) * x^42).show()
            zeta(3)*(e^x)^(-1/2)*x^42
        """
    def monomial_coefficient(self, monomial):
        '''
        Return the coefficient in the base ring of the given monomial
        in this expansion.

        INPUT:

        - ``monomial`` -- a monomial element which can be converted
          into the asymptotic ring of this element

        OUTPUT: an element of the coefficient ring

        EXAMPLES::

            sage: R.<m, n> = AsymptoticRing("m^QQ*n^QQ", QQ)
            sage: ae = 13 + 42/n + 2/n/m + O(n^-2)
            sage: ae.monomial_coefficient(1/n)
            42
            sage: ae.monomial_coefficient(1/n^3)
            0
            sage: R.<n> = AsymptoticRing("n^QQ", ZZ)
            sage: ae.monomial_coefficient(1/n)
            42
            sage: ae.monomial_coefficient(1)
            13

        TESTS:

        Conversion of ``monomial`` the parent of this element must be
        possible::

            sage: R.<m> = AsymptoticRing("m^QQ", QQ)
            sage: S.<n> = AsymptoticRing("n^QQ", QQ)
            sage: m.monomial_coefficient(n)
            Traceback (most recent call last):
            ...
            ValueError: Cannot include n with parent Exact Term Monoid
            n^QQ with coefficients in Rational Field in Asymptotic Ring
            <m^QQ> over Rational Field
            > *previous* ValueError: Growth n is not valid in
              Exact Term Monoid m^QQ with coefficients in Rational Field.
            >> *previous* ValueError: n is not in Growth Group m^QQ.

        Only monomials are allowed::

            sage: R.<n> = AsymptoticRing("n^QQ", QQ)
            sage: (n + 4).monomial_coefficient(n + 5)
            Traceback (most recent call last):
            ...
            ValueError: n + 5 not a monomial
            sage: n.monomial_coefficient(0)
            Traceback (most recent call last):
            ...
            ValueError: 0 not a monomial

        Cannot extract the coefficient of an O term::

            sage: O(n).monomial_coefficient(n)
            Traceback (most recent call last):
            ...
            AttributeError: \'OTermMonoid_with_category.element_class\' object has no attribute \'coefficient\'...

        The ``monomial`` must be exact::

            sage: n.monomial_coefficient(O(n))
            Traceback (most recent call last):
            ...
            ValueError: non-exact monomial O(n)
        '''
    def __invert__(self, precision=None):
        """
        Return the multiplicative inverse of this element.

        INPUT:

        - ``precision`` -- the precision used for truncating the
          expansion. If ``None`` (default value) is used, the
          default precision of the parent is used.

        OUTPUT: an asymptotic expansion

        .. WARNING::

            Due to truncation of infinite expansions, the element
            returned by this method might not fulfill
            ``el * ~el == 1``.

        .. TODO::

            As soon as `L`-terms are implemented, this
            implementation has to be adapted as well in order to
            yield correct results.

        EXAMPLES::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ, default_prec=4)
            sage: ~x
            x^(-1)
            sage: ~(x^42)
            x^(-42)
            sage: ex = ~(1 + x); ex
            x^(-1) - x^(-2) + x^(-3) - x^(-4) + O(x^(-5))
            sage: ex * (1+x)
            1 + O(x^(-4))
            sage: ~(1 + O(1/x))
            1 + O(x^(-1))

        TESTS::

            sage: A.<a> = AsymptoticRing(growth_group='a^ZZ', coefficient_ring=ZZ)
            sage: (1 / a).parent()
            Asymptotic Ring <a^ZZ> over Rational Field
            sage: (a / 2).parent()
            Asymptotic Ring <a^ZZ> over Rational Field

        ::

            sage: ~A(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot invert 0 in
            Asymptotic Ring <a^ZZ> over Integer Ring.

        ::

            sage: B.<s, t> = AsymptoticRing(growth_group='s^ZZ * t^ZZ', coefficient_ring=QQ)
            sage: ~(s + t)
            Traceback (most recent call last):
            ...
            ValueError: Cannot determine main term of s + t since there
            are several maximal elements s, t.
        """
    invert = __invert__
    def truncate(self, precision=None):
        """
        Truncate this asymptotic expansion.

        INPUT:

        - ``precision`` -- positive integer or ``None``. Number of
          summands that are kept. If ``None`` (default value) is
          given, then ``default_prec`` from the parent is used.

        OUTPUT: an asymptotic expansion

        .. NOTE::

            For example, truncating an asymptotic expansion with
            ``precision=20`` does not yield an expansion with exactly 20
            summands! Rather than that, it keeps the 20 summands
            with the largest growth, and adds appropriate
            `O`-Terms.

        EXAMPLES::

            sage: R.<x> = AsymptoticRing('x^ZZ', QQ)
            sage: ex = sum(x^k for k in range(5)); ex
            x^4 + x^3 + x^2 + x + 1
            sage: ex.truncate(precision=2)
            x^4 + x^3 + O(x^2)
            sage: ex.truncate(precision=0)
            O(x^4)
            sage: ex.truncate()
            x^4 + x^3 + x^2 + x + 1
        """
    def exact_part(self):
        """
        Return the expansion consisting of all exact terms of this
        expansion.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: R.<x> = AsymptoticRing('x^QQ * log(x)^QQ', QQ)
            sage: (x^2 + O(x)).exact_part()
            x^2
            sage: (x + log(x)/2 + O(log(x)/x)).exact_part()
            x + 1/2*log(x)

        TESTS::

            sage: R.<x, y> = AsymptoticRing('x^QQ * y^QQ', QQ)
            sage: (x + y + O(1/(x*y))).exact_part()
            x + y
            sage: O(x).exact_part()
            0
        """
    def error_part(self):
        """
        Return the expansion consisting of all error terms of this
        expansion.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: R.<x,y> = AsymptoticRing('x^QQ * log(x)^QQ * y^QQ', QQ)
            sage: (x*log(x) + y^2 + O(x) + O(y)).error_part()
            O(x) + O(y)
        """
    def __pow__(self, exponent, precision=None):
        """
        Calculate the power of this asymptotic expansion to the given ``exponent``.

        INPUT:

        - ``exponent`` -- an element

        - ``precision`` -- the precision used for truncating the
          expansion. If ``None`` (default value) is used, the
          default precision of the parent is used.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: Q.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=QQ)
            sage: x^(1/7)
            x^(1/7)
            sage: (x^(1/2) + O(x^0))^15
            x^(15/2) + O(x^7)

        ::

            sage: Z.<y> = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=ZZ)
            sage: y^(1/7)
            y^(1/7)
            sage: _.parent()
            Asymptotic Ring <y^QQ> over Rational Field
            sage: (y^2 + O(y))^(1/2)
            y + O(1)
            sage: (y^2 + O(y))^(-2)
            y^(-4) + O(y^(-5))
            sage: (1 + 1/y + O(1/y^3))^pi
            1 + pi*y^(-1) + (1/2*pi*(pi - 1))*y^(-2) + O(y^(-3))

        ::

            sage: B.<z> = AsymptoticRing(growth_group='z^QQ * log(z)^QQ', coefficient_ring=QQ)
            sage: (z^2 + O(z))^(1/2)
            z + O(1)

        ::

            sage: A.<x> = AsymptoticRing('QQ^x * x^SR * log(x)^ZZ', QQ)
            sage: x * 2^x
            2^x*x
            sage: 5^x * 2^x
            10^x
            sage: 2^log(x)
            x^(log(2))
            sage: 2^(x + 1/x)
            2^x + log(2)*2^x*x^(-1) + 1/2*log(2)^2*2^x*x^(-2) + ... + O(2^x*x^(-20))
            sage: _.parent()
            Asymptotic Ring <QQ^x * x^SR * log(x)^QQ * Signs^x> over Symbolic Ring

        ::

            sage: C.<c> = AsymptoticRing(growth_group='QQ^c * c^QQ', coefficient_ring=QQ, default_prec=5)
            sage: (3 + 1/c^2)^c
            3^c + 1/3*3^c*c^(-1) + 1/18*3^c*c^(-2) - 4/81*3^c*c^(-3)
            - 35/1944*3^c*c^(-4) + O(3^c*c^(-5))
            sage: _.parent()
            Asymptotic Ring <QQ^c * c^QQ * Signs^c> over Rational Field
            sage: (2 + (1/3)^c)^c
            2^c + 1/2*(2/3)^c*c + 1/8*(2/9)^c*c^2 - 1/8*(2/9)^c*c
            + 1/48*(2/27)^c*c^3 + O((2/27)^c*c^2)
            sage: _.parent()
            Asymptotic Ring <QQ^c * c^QQ * Signs^c> over Rational Field

        TESTS:

        See :issue:`19110`::

            sage: O(x)^(-1)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot take O(x) to exponent -1.
            > *previous* ZeroDivisionError: rational division by zero

        ::

            sage: B.<z> = AsymptoticRing(growth_group='z^QQ * log(z)^QQ', coefficient_ring=QQ, default_prec=5)
            sage: z^(1+1/z)
            z + log(z) + 1/2*z^(-1)*log(z)^2 + 1/6*z^(-2)*log(z)^3 +
            1/24*z^(-3)*log(z)^4 + O(z^(-4)*log(z)^5)
            sage: _.parent()
            Asymptotic Ring <z^QQ * log(z)^QQ> over Rational Field

        ::

            sage: B(0)^(-7)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot take 0 to the negative exponent -7.
            sage: B(0)^SR.var('a')
            Traceback (most recent call last):
            ...
            NotImplementedError: Taking 0 to the exponent a not implemented.

        ::

            sage: C.<s, t> = AsymptoticRing(growth_group='s^QQ * t^QQ', coefficient_ring=QQ)
            sage: (s + t)^s
            Traceback (most recent call last):
            ...
            ValueError: Cannot take s + t to the exponent s.
            > *previous* ValueError: Cannot determine main term of s + t
            since there are several maximal elements s, t.

        Check that :issue:`19945` is fixed::

            sage: A.<n> = AsymptoticRing('QQ^n * n^QQ', ZZ)
            sage: (1/2)^n
            (1/2)^n

        Check that :issue:`19946` is fixed::

            sage: assume(SR.an_element() > 0)
            sage: A.<n> = AsymptoticRing('QQ^n * n^QQ', SR)
            sage: e = 2^n; e
            2^n
            sage: e.parent()
            Asymptotic Ring <SR^n * n^QQ * Signs^n> over Symbolic Ring
            sage: e = A(e); e
            2^n
            sage: e.parent()
            Asymptotic Ring <QQ^n * n^QQ * Signs^n> over Symbolic Ring
            sage: forget()

        :issue:`22120`::

            sage: A.<w> = AsymptoticRing('w^QQbar', QQ)
            sage: w^QQbar(sqrt(2))
            w^(1.414213562373095?)
        """
    pow = __pow__
    def __pow_number__(self, exponent, precision=None, check_convergence: bool = False):
        """
        Return the power of this asymptotic expansion to some
        number (``exponent``).

        Let `m` be the maximal element of this asymptotic expansion
        and `r` the remaining summands. This method calculates

        .. MATH::

            (m + r)^{\\mathit{exponent}}
            = m^{\\mathit{exponent}} \\sum_{k=0}^K
            \\binom{\\mathit{exponent}}{k} (r/m)^k

        where `K` is chosen such that adding an additional summand
        does not change the result.

        INPUT:

        - ``exponent`` -- a numerical value (e.g. integer, rational)
          or other constant

        - ``precision`` -- nonnegative integer

        - ``check_convergence`` -- boolean (default: ``False``); if set,
          then an additional check on the input is performed to ensure
          that the calculated sum converges

        OUTPUT: an asymptotic expansion

        .. SEEALSO::

            :meth:`pow`

        TESTS::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: (1 + x).__pow_number__(4)
            x^4 + 4*x^3 + 6*x^2 + 4*x + 1
            sage: _.parent()
            Asymptotic Ring <x^ZZ> over Rational Field
            sage: (x + 1).__pow_number__(1/2, precision=5)
            x^(1/2) + 1/2*x^(-1/2) - 1/8*x^(-3/2) + 1/16*x^(-5/2)
            - 5/128*x^(-7/2) + O(x^(-9/2))
            sage: _.parent()
            Asymptotic Ring <x^QQ> over Rational Field
            sage: (8 + 1/x).__pow_number__(1/3, precision=5)
            2 + 1/12*x^(-1) - 1/288*x^(-2) + 5/20736*x^(-3)
            - 5/248832*x^(-4) + O(x^(-5))
            sage: _.parent()
            Asymptotic Ring <x^QQ> over Rational Field

        ::

            sage: R(0).__pow_number__(-3/2)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Cannot take 0 to the negative exponent -3/2.
            sage: R(0).__pow_number__(RIF(-1,1))
            Traceback (most recent call last):
            ...
            ValueError: Possible division by zero, since sign of
            the exponent 0.? cannot be determined.
            sage: R(0)^0
            1

        ::

            sage: A.<a, b> = AsymptoticRing(growth_group='a^ZZ * b^ZZ', coefficient_ring=QQ)
            sage: (a + b).__pow_number__(3/2)
            Traceback (most recent call last):
            ...
            ValueError: Cannot determine main term of a + b since
            there are several maximal elements a, b.

        ::

            sage: S.<s> = AsymptoticRing(growth_group='QQ^s * s^ZZ', coefficient_ring=QQ)
            sage: (2 + 2/s^2).__pow_number__(s, precision=7)
            2^s + 2^s*s^(-1) + 1/2*2^s*s^(-2) - 1/3*2^s*s^(-3)
            - 11/24*2^s*s^(-4) + 11/120*2^s*s^(-5)
            + 271/720*2^s*s^(-6) + O(2^s*s^(-7))
            sage: _.parent()
            Asymptotic Ring <QQ^s * s^QQ * Signs^s> over Rational Field

            sage: S.<s> = AsymptoticRing(growth_group='(QQ_+)^s * s^ZZ', coefficient_ring=QQ)
            sage: (2 + 2/s^2).__pow_number__(s, precision=7)
            2^s + 2^s*s^(-1) + 1/2*2^s*s^(-2) - 1/3*2^s*s^(-3)
            - 11/24*2^s*s^(-4) + 11/120*2^s*s^(-5)
            + 271/720*2^s*s^(-6) + O(2^s*s^(-7))
            sage: _.parent()
            Asymptotic Ring <QQ^s * s^QQ> over Rational Field
        """
    def sqrt(self, precision=None):
        """
        Return the square root of this asymptotic expansion.

        INPUT:

        - ``precision`` -- the precision used for truncating the
          expansion. If ``None`` (default value) is used, the
          default precision of the parent is used.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: A.<s> = AsymptoticRing(growth_group='s^QQ', coefficient_ring=QQ)
            sage: s.sqrt()
            s^(1/2)
            sage: a = (1 + 1/s).sqrt(precision=6); a
            1 + 1/2*s^(-1) - 1/8*s^(-2) + 1/16*s^(-3)
            - 5/128*s^(-4) + 7/256*s^(-5) + O(s^(-6))

        .. SEEALSO::

            :meth:`pow`, :meth:`rpow`, :meth:`exp`.

        TESTS::

            sage: P.<p> = PowerSeriesRing(QQ, default_prec=6)
            sage: bool(SR(a.exact_part()).subs(s=1/x) -
            ....:      SR((1+p).sqrt().polynomial()).subs(p=x) == 0)
            True
        """
    def O(self):
        """
        Convert all terms in this asymptotic expansion to `O`-terms.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: AR.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: O(x)
            O(x)
            sage: type(O(x))
            <class 'sage.rings.asymptotic.asymptotic_ring.AsymptoticRing_with_category.element_class'>
            sage: expr = 42*x^42 + x^10 + O(x^2); expr
            42*x^42 + x^10 + O(x^2)
            sage: expr.O()
            O(x^42)
            sage: (2*x).O()
            O(x)

        .. SEEALSO::

            :func:`sage.rings.power_series_ring.PowerSeriesRing`,
            :func:`sage.rings.laurent_series_ring.LaurentSeriesRing`.

        TESTS::

            sage: AR(0).O()
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got O(0)
            The error term O(0) means 0 for sufficiently large x.
        """
    def log(self, base=None, precision=None, locals=None):
        """
        The logarithm of this asymptotic expansion.

        INPUT:

        - ``base`` -- the base of the logarithm. If ``None``
          (default value) is used, the natural logarithm is taken.

        - ``precision`` -- the precision used for truncating the
          expansion. If ``None`` (default value) is used, the
          default precision of the parent is used.

        - ``locals`` -- dictionary which may contain the following keys and values:

          - ``'log'`` -- value: a function. If not used, then the usual
            :class:`log <sage.functions.log.Function_log>` is taken.

        OUTPUT: an asymptotic expansion

        .. NOTE::

            Computing the logarithm of an asymptotic expansion
            is possible if and only if there is exactly one maximal
            summand in the expansion.

        ALGORITHM:

        If the expansion has more than one summand,
        the asymptotic expansion for `\\log(1+t)` as `t` tends to `0`
        is used.

        .. TODO::

            As soon as `L`-terms are implemented, this
            implementation has to be adapted as well in order to
            yield correct results.

        EXAMPLES::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ * log(x)^ZZ', coefficient_ring=QQ)
            sage: log(x)
            log(x)
            sage: log(x^2)
            2*log(x)
            sage: log(x-1)
            log(x) - x^(-1) - 1/2*x^(-2) - 1/3*x^(-3) - ... + O(x^(-21))

        The coefficient ring is automatically extended if needed::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ * log(x)^ZZ', coefficient_ring=ZZ, default_prec=3)
            sage: (49*x^3-1).log()
            3*log(x) + 2*log(7) - 1/49*x^(-3) - 1/4802*x^(-6) ... + O(x^(-12))
            sage: _.parent()
            Asymptotic Ring <x^ZZ * log(x)^ZZ> over Symbolic Ring

        If one wants to avoid this extending to the Symbolic Ring, then
        the following helps::

            sage: L.<log7> = ZZ[]
            sage: def mylog(z, base=None):
            ....:     try:
            ....:         if ZZ(z).is_power_of(7):
            ....:             return log(ZZ(z), 7) * log7
            ....:     except (TypeError, ValueError):
            ....:         pass
            ....:     return log(z, base)
            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ * log(x)^ZZ', coefficient_ring=L, default_prec=3)
            sage: (49*x^3-1).log(locals={'log': mylog})
            3*log(x) + 2*log7 - 1/49*x^(-3) - 1/4802*x^(-6) ... + O(x^(-12))

        A ``log``-function can also be specified to always be used with the
        asymptotic ring::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ * log(x)^ZZ', coefficient_ring=L, default_prec=3, locals={'log': mylog})
            sage: log(49*x^3-1)
            3*log(x) + 2*log7 - 1/49*x^(-3) - 1/4802*x^(-6) - 1/352947*x^(-9) + O(x^(-12))

        TESTS::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ * log(x)^ZZ', coefficient_ring=QQ)
            sage: log(R(1))
            0
            sage: log(R(0))
            Traceback (most recent call last):
            ...
            ArithmeticError: Cannot compute log(0) in
            Asymptotic Ring <x^ZZ * log(x)^ZZ> over Rational Field.
            sage: C.<s, t> = AsymptoticRing(growth_group='s^ZZ * t^ZZ', coefficient_ring=QQ)
            sage: log(s + t)
            Traceback (most recent call last):
            ...
            ValueError: Cannot determine main term of s + t since
            there are several maximal elements s, t.
        """
    def is_exact(self) -> bool:
        """
        Return whether all terms of this expansion are exact.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<x> = AsymptoticRing('x^QQ * log(x)^QQ', QQ)
            sage: (x^2 + O(x)).is_exact()
            False
            sage: (x^2 - x).is_exact()
            True

        TESTS::

            sage: A(0).is_exact()
            True
            sage: A.one().is_exact()
            True
        """
    def is_little_o_of_one(self) -> bool:
        """
        Return whether this expansion is of order `o(1)`.

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<x> = AsymptoticRing('x^ZZ * log(x)^ZZ', QQ)
            sage: (x^4 * log(x)^(-2) + x^(-4) * log(x)^2).is_little_o_of_one()
            False
            sage: (x^(-1) * log(x)^1234 + x^(-2) + O(x^(-3))).is_little_o_of_one()
            True
            sage: (log(x) - log(x-1)).is_little_o_of_one()
            True

        ::

            sage: A.<x, y> = AsymptoticRing('x^QQ * y^QQ * log(y)^ZZ', QQ)
            sage: (x^(-1/16) * y^32 + x^32 * y^(-1/16)).is_little_o_of_one()
            False
            sage: (x^(-1) * y^(-3) + x^(-3) * y^(-1)).is_little_o_of_one()
            True
            sage: (x^(-1) * y / log(y)).is_little_o_of_one()
            False
            sage: (log(y-1)/log(y) - 1).is_little_o_of_one()
            True

        .. SEEALSO::

            :meth:`limit`
        """
    def rpow(self, base, precision=None, locals=None):
        """
        Return the power of ``base`` to this asymptotic expansion.

        INPUT:

        - ``base`` -- an element or ``'e'``

        - ``precision`` -- the precision used for truncating the
          expansion. If ``None`` (default value) is used, the
          default precision of the parent is used.

        - ``locals`` -- dictionary which may contain the following keys and values:

          - ``'log'`` -- value: a function. If not used, then the usual
            :class:`log <sage.functions.log.Function_log>` is taken.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: A.<x> = AsymptoticRing('x^ZZ', QQ)
            sage: (1/x).rpow('e', precision=5)
            1 + x^(-1) + 1/2*x^(-2) + 1/6*x^(-3) + 1/24*x^(-4) + O(x^(-5))

        TESTS::

            sage: assume(SR.an_element() > 0)
            sage: y = SR.var('y')
            sage: x.rpow(y)
            Traceback (most recent call last):
            ...
            ArithmeticError: Cannot construct y^x in Growth Group x^ZZ
            > *previous* TypeError: unsupported operand parent(s) for *:
              'Growth Group x^ZZ' and 'Growth Group SR^x * Arg_SR^x'
            sage: assume(y > 0)
            sage: x.rpow(y)
            Traceback (most recent call last):
            ...
            ArithmeticError: Cannot construct y^x in Growth Group x^ZZ
            > *previous* TypeError: unsupported operand parent(s) for *:
              'Growth Group x^ZZ' and 'Growth Group SR^x'
            sage: forget()

        Check that :issue:`19946` is fixed::

            sage: A.<n> = AsymptoticRing('(QQ_+)^n * n^QQ', SR)
            sage: n.rpow(2)
            2^n
            sage: _.parent()
            Asymptotic Ring <QQ^n * n^QQ> over Symbolic Ring
        """
    def exp(self, precision=None):
        """
        Return the exponential of (i.e., the power of `e` to) this asymptotic expansion.

        INPUT:

        - ``precision`` -- the precision used for truncating the
          expansion. If ``None`` (default value) is used, the
          default precision of the parent is used.

        OUTPUT: an asymptotic expansion

        .. NOTE::

            The exponential function of this expansion can only be
            computed exactly if the respective growth element can be
            constructed in the underlying growth group.

        ALGORITHM:

        If the corresponding growth can be constructed, return
        the exact exponential function. Otherwise, if this term
        is `o(1)`, try to expand the series and truncate
        according to the given precision.

        .. TODO::

            As soon as `L`-terms are implemented, this
            implementation has to be adapted as well in order to
            yield correct results.

        EXAMPLES::

            sage: A.<x> = AsymptoticRing('(e^x)^ZZ * x^ZZ * log(x)^ZZ', SR)
            sage: exp(x)
            e^x
            sage: exp(2*x)
            (e^x)^2
            sage: exp(x + log(x))
            e^x*x

        ::

            sage: (x^(-1)).exp(precision=7)
            1 + x^(-1) + 1/2*x^(-2) + 1/6*x^(-3) + ... + O(x^(-7))

        TESTS::

            sage: A.<x> = AsymptoticRing('(e^x)^ZZ * x^QQ * log(x)^QQ', SR)
            sage: exp(log(x))
            x
            sage: log(exp(x))
            x

        ::

            sage: exp(x+1)
            e*e^x

        See :issue:`19521`::

            sage: A.<n> = AsymptoticRing('n^ZZ', SR.subring(no_variables=True))
            sage: exp(O(n^(-3))).parent()
            Asymptotic Ring <n^ZZ> over Symbolic Constants Subring
        """
    def subs(self, rules=None, domain=None, **kwds):
        """
        Substitute the given ``rules`` in this asymptotic expansion.

        INPUT:

        - ``rules`` -- dictionary

        - ``kwds`` -- keyword arguments will be added to the
          substitution ``rules``

        - ``domain`` -- (default: ``None``) a parent. The neutral
          elements `0` and `1` (rules for the keys ``'_zero_'`` and
          ``'_one_'``, see note box below) are taken out of this
          domain. If ``None``, then this is determined automatically.

        OUTPUT: an object

        .. NOTE::

          The neutral element of the asymptotic ring is replaced by
          the value to the key ``'_zero_'``; the neutral element of
          the growth group is replaced by the value to the key
          ``'_one_'``.

        EXAMPLES::

            sage: A.<x> = AsymptoticRing(growth_group='(e^x)^QQ * x^ZZ * log(x)^ZZ', coefficient_ring=QQ, default_prec=5)

        ::

            sage: (e^x * x^2 + log(x)).subs(x=SR('s'))
            s^2*e^s + log(s)
            sage: _.parent()
            Symbolic Ring

        ::

            sage: (x^3 + x + log(x)).subs(x=x+5).truncate(5)
            x^3 + 15*x^2 + 76*x + log(x) + 130 + O(x^(-1))
            sage: _.parent()
            Asymptotic Ring <(e^x)^QQ * x^ZZ * log(x)^ZZ> over Rational Field

        ::

            sage: (e^x * x^2 + log(x)).subs(x=2*x)
            4*(e^x)^2*x^2 + log(x) + log(2)
            sage: _.parent()
            Asymptotic Ring <(e^x)^QQ * x^QQ * log(x)^QQ> over Symbolic Ring

        ::

            sage: (x^2 + log(x)).subs(x=4*x+2).truncate(5)
            16*x^2 + 16*x + log(x) + 2*log(2) + 4 + 1/2*x^(-1) + O(x^(-2))
            sage: _.parent()
            Asymptotic Ring <(e^x)^QQ * x^ZZ * log(x)^ZZ> over Symbolic Ring

        ::

            sage: (e^x * x^2 + log(x)).subs(x=RIF(pi))
            229.534211738584?
            sage: _.parent()
            Real Interval Field with 53 bits of precision

        .. SEEALSO::

            :meth:`sage.symbolic.expression.Expression.subs`

        TESTS::

            sage: x.subs({'y': -1})
            Traceback (most recent call last):
            ...
            ValueError: Cannot substitute y in x since it is not a generator of
            Asymptotic Ring <(e^x)^QQ * x^ZZ * log(x)^ZZ> over Rational Field.
            sage: B.<u, v, w> = AsymptoticRing(growth_group='u^QQ * v^QQ * w^QQ', coefficient_ring=QQ)
            sage: (1/u).subs({'u': 0})
            Traceback (most recent call last):
            ...
            TypeError: Cannot apply the substitution rules {u: 0} on u^(-1) in
            Asymptotic Ring <u^QQ * v^QQ * w^QQ> over Rational Field.
            > *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Asymptotic Ring <u^QQ * v^QQ * w^QQ> over Rational Field.
            >> *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Exact Term Monoid u^QQ * v^QQ * w^QQ with coefficients in Rational Field.
            >...> *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Growth Group u^QQ * v^QQ * w^QQ.
            >...> *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Growth Group u^QQ.
            >...> *previous* ZeroDivisionError: rational division by zero
            sage: (1/u).subs({'u': 0, 'v': SR.var('v')})
            Traceback (most recent call last):
            ...
            TypeError: Cannot apply the substitution rules {u: 0, v: v} on u^(-1) in
            Asymptotic Ring <u^QQ * v^QQ * w^QQ> over Rational Field.
            > *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Asymptotic Ring <u^QQ * v^QQ * w^QQ> over Rational Field.
            >> *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Exact Term Monoid u^QQ * v^QQ * w^QQ with coefficients in Rational Field.
            >...> *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Growth Group u^QQ * v^QQ * w^QQ.
            >...> *previous* ZeroDivisionError: Cannot substitute in u^(-1) in
            Growth Group u^QQ.
            >...> *previous* ZeroDivisionError: rational division by zero

        ::

            sage: u.subs({u: 0, 'v': SR.var('v')})
            0
            sage: v.subs({u: 0, 'v': SR.var('v')})
            v
            sage: _.parent()
            Symbolic Ring

        ::

            sage: u.subs({SR.var('u'): -1})
            Traceback (most recent call last):
            ...
            TypeError: Cannot substitute u in u since it is neither an
            asymptotic expansion nor a string
            (but a <class 'sage.symbolic.expression.Expression'>).

        ::

            sage: u.subs({u: 1, 'u': 1})
            1
            sage: u.subs({u: 1}, u=1)
            1
            sage: u.subs({u: 1, 'u': 2})
            Traceback (most recent call last):
            ...
            ValueError: Cannot substitute in u: duplicate key u.
            sage: u.subs({u: 1}, u=3)
            Traceback (most recent call last):
            ...
            ValueError: Cannot substitute in u: duplicate key u.

        ::

            sage: B(0).subs({'_zero_': None}) is None
            True
            sage: B(1).subs({'_one_': AA(1)}).parent() is AA
            True

        ::

            sage: Asy.<n> = AsymptoticRing('n^QQ', RBF)
            sage: asy = n^(2/3) + 1/3*n^(1/3)
            sage: asy.subs(n=RBF(10))
            [5.359733730290...]
        """
    def compare_with_values(self, variable, function, values, rescaled: bool = True, ring=...):
        """
        Compute the (rescaled) difference between this asymptotic
        expansion and the given values.

        INPUT:

        - ``variable`` -- an asymptotic expansion or a string

        - ``function`` -- a callable or symbolic expression giving the
          comparison values

        - ``values`` -- list or iterable of values where the comparison
          shall be carried out

        - ``rescaled`` -- boolean (default: ``True``); determines whether
          the difference is divided by the error term of the asymptotic
          expansion

        - ``ring`` -- (default: ``RIF``) the parent into which the
          difference is converted

        OUTPUT:

        A list of pairs containing comparison points and (rescaled)
        difference values.

        EXAMPLES::

            sage: assume(SR.an_element() > 0)
            sage: A.<n> = AsymptoticRing('QQ^n * n^ZZ', SR)
            sage: catalan = binomial(2*x, x)/(x+1)
            sage: expansion = 4^n*(1/sqrt(pi)*n^(-3/2)
            ....:     - 9/8/sqrt(pi)*n^(-5/2)
            ....:     + 145/128/sqrt(pi)*n^(-7/2) + O(n^(-9/2)))
            sage: expansion.compare_with_values(n, catalan, srange(5, 10))
            [(5, 0.5303924444775?),
             (6, 0.5455279498787?),
             (7, 0.556880411050?),
             (8, 0.565710587724?),
             (9, 0.572775029098?)]
            sage: expansion.exact_part().compare_with_values(n, catalan, [5, 10, 20])
            Traceback (most recent call last):
            ...
            NotImplementedError: exactly one error term required
            sage: expansion.exact_part().compare_with_values(n, catalan, [5, 10, 20], rescaled=False)
            [(5, 0.3886263699387?), (10, 19.1842458318?), (20, 931314.63637?)]
            sage: expansion.compare_with_values(n, catalan, [5, 10, 20], rescaled=False, ring=SR)
            [(5, 168/5*sqrt(5)/sqrt(pi) - 42),
             (10, 1178112/125*sqrt(10)/sqrt(pi) - 16796),
             (20, 650486218752/125*sqrt(5)/sqrt(pi) - 6564120420)]

        Instead of a symbolic expression, a callable function can
        be specified as well::

            sage: A.<n> = AsymptoticRing('n^ZZ * log(n)^ZZ', SR)
            sage: def H(n):
            ....:     return sum(1/k for k in srange(1, n+1))
            sage: H_expansion = (log(n) + euler_gamma + 1/(2*n)
            ....:                - 1/(12*n^2) + O(n^-4))
            sage: H_expansion.compare_with_values(n, H, srange(25, 30)) # rel tol 1e-6
            [(25, -0.008326995?),
             (26, -0.008327472?),
             (27, -0.008327898?),
             (28, -0.00832828?),
             (29, -0.00832862?)]
            sage: forget()

        .. SEEALSO::

            :meth:`plot_comparison`

        TESTS::

            sage: A.<x, y> = AsymptoticRing('x^ZZ*y^ZZ', QQ)
            sage: expansion = x^2 + O(x) + O(y)
            sage: expansion.compare_with_values(y, lambda z: z^2, srange(20, 30))
            Traceback (most recent call last):
            ....
            NotImplementedError: exactly one error term required
            sage: expansion = x^2
            sage: expansion.compare_with_values(y, lambda z: z^2, srange(20, 30))
            Traceback (most recent call last):
            ....
            NotImplementedError: exactly one error term required
            sage: expansion = x^2 + O(x)
            sage: expansion.compare_with_values(y, lambda z: z^2, srange(20, 30))
            Traceback (most recent call last):
            ....
            NameError: name 'x' is not defined
            sage: expansion.compare_with_values(x, lambda z: z^2, srange(20, 30))
            [(20, 0), (21, 0), ..., (29, 0)]
            sage: expansion.compare_with_values(x, SR('x*y'), srange(20, 30))
            Traceback (most recent call last):
            ....
            NotImplementedError: expression x*y has more than one variable

        ::

            sage: A.<n> = AsymptoticRing('n^ZZ', RBF)
            sage: asy = (1 - 1/n + 1/n^2)/3 + O(1/n^3)
            sage: asy.compare_with_values('n', lambda k: 1/(3+3/k), srange(5,10))
            [(5, 0.2777...), (6, 0.28571...), (7, 0.29166...), (8, 0.29629...),
            (9, 0.30000...)]
            sage: basy = asy.exact_part() + 1/3*A.B(asy.error_part())
            doctest:warning
            ...
            FutureWarning: This class/method/function is marked as experimental.
            It, its functionality or its interface might change without a formal deprecation.
            See https://github.com/sagemath/sage/issues/31922 for details.
            sage: basy.compare_with_values('n', lambda k: 1/(3+3/k), [2^k for k in srange(8)])
            [(1, 0.500...), (2, 0.666...), (4, 0.800...), (8, 0.888...),
            (16, 0.941...), (32, 0.969...), (64, 0.984...), (128, 0.992...)]
        """
    def plot_comparison(self, variable, function, values, rescaled: bool = True, ring=..., relative_tolerance: float = 0.025, **kwargs):
        """
        Plot the (rescaled) difference between this asymptotic
        expansion and the given values.

        INPUT:

        - ``variable`` -- an asymptotic expansion or a string

        - ``function`` -- a callable or symbolic expression giving the
          comparison values

        - ``values`` -- list or iterable of values where the comparison
          shall be carried out

        - ``rescaled`` -- boolean (default: ``True``); determines whether
          the difference is divided by the error term of the asymptotic
          expansion

        - ``ring`` -- (default: ``RIF``) the parent into which the
          difference is converted

        - ``relative_tolerance`` -- (default: ``0.025``) raise error
          when relative error exceeds this tolerance

        Other keyword arguments are passed to :func:`list_plot`.

        OUTPUT: a graphics object

        .. NOTE::

            If rescaled (i.e. divided by the error term), the output
            should be bounded.

            This method is mainly meant to have an easily usable
            plausibility check for asymptotic expansion created in
            some way.

        EXAMPLES:

        We want to check the quality of the asymptotic expansion of
        the harmonic numbers::

            sage: A.<n> = AsymptoticRing('n^ZZ * log(n)^ZZ', SR)
            sage: def H(n):
            ....:     return sum(1/k for k in srange(1, n+1))
            sage: H_expansion = (log(n) + euler_gamma + 1/(2*n)
            ....:                - 1/(12*n^2) + O(n^-4))
            sage: H_expansion.plot_comparison(n, H, srange(1, 30))
            Graphics object consisting of 1 graphics primitive

        Alternatively, the unscaled (absolute) difference can be
        plotted as well::

            sage: H_expansion.plot_comparison(n, H, srange(1, 30),
            ....:                             rescaled=False)
            Graphics object consisting of 1 graphics primitive

        Additional keywords are passed to :func:`list_plot`::

            sage: H_expansion.plot_comparison(n, H, srange(1, 30),
            ....:                             plotjoined=True, marker='o',
            ....:                             color='green')
            Graphics object consisting of 1 graphics primitive

        .. SEEALSO::

            :meth:`compare_with_values`

        TESTS::

            sage: H_expansion.plot_comparison(n, H, [600])
            Traceback (most recent call last):
            ...
            ValueError: Numerical noise is too high, the comparison is inaccurate
            sage: H_expansion.plot_comparison(n, H, [600], relative_tolerance=2)
            Graphics object consisting of 1 graphics primitive
        """
    def symbolic_expression(self, R=None):
        """
        Return this asymptotic expansion as a symbolic expression.

        INPUT:

        - ``R`` -- (a subring of) the symbolic ring or ``None``.
          The output will be an element of ``R``. If ``None``,
          then the symbolic ring is used.

        OUTPUT: a symbolic expression

        EXAMPLES::

            sage: A.<x, y, z> = AsymptoticRing(growth_group='x^ZZ * y^QQ * log(y)^QQ * (QQ_+)^z * z^QQ', coefficient_ring=QQ)
            sage: SR(A.an_element())  # indirect doctest
            1/8*(1/8)^z*x^3*y^(3/2)*z^(3/2)*log(y)^(3/2) +
            Order((1/2)^z*x*sqrt(y)*sqrt(z)*sqrt(log(y)))

            sage: A.<x, y, z> = AsymptoticRing(growth_group='x^ZZ * y^QQ * log(y)^QQ * (QQ_+)^z * z^QQ', coefficient_ring=QQ)
            sage: SR(A.an_element())  # indirect doctest
            1/8*(1/8)^z*x^3*y^(3/2)*z^(3/2)*log(y)^(3/2) +
            Order((1/2)^z*x*sqrt(y)*sqrt(z)*sqrt(log(y)))

        TESTS::

            sage: a = A.an_element(); a
            1/8*x^3*y^(3/2)*log(y)^(3/2)*(1/8)^z*z^(3/2) +
            O(x*y^(1/2)*log(y)^(1/2)*(1/2)^z*z^(1/2))
            sage: a.symbolic_expression()
            1/8*(1/8)^z*x^3*y^(3/2)*z^(3/2)*log(y)^(3/2) +
            Order((1/2)^z*x*sqrt(y)*sqrt(z)*sqrt(log(y)))
            sage: _.parent()
            Symbolic Ring

        ::

            sage: from sage.symbolic.ring import SymbolicRing
            sage: class MySymbolicRing(SymbolicRing):
            ....:     pass
            sage: mySR = MySymbolicRing()
            sage: a.symbolic_expression(mySR).parent() is mySR
            True
        """
    def map_coefficients(self, f, new_coefficient_ring=None):
        """
        Return the asymptotic expansion obtained by applying ``f`` to
        each coefficient of this asymptotic expansion.

        INPUT:

        - ``f`` -- a callable; a coefficient `c` will be mapped to `f(c)`

        - ``new_coefficient_ring`` -- (default: ``None``) a ring

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: A.<n> = AsymptoticRing(growth_group='n^ZZ', coefficient_ring=ZZ)
            sage: a = n^4 + 2*n^3 + 3*n^2 + O(n)
            sage: a.map_coefficients(lambda c: c+1)
            2*n^4 + 3*n^3 + 4*n^2 + O(n)
            sage: a.map_coefficients(lambda c: c-2)
            -n^4 + n^2 + O(n)

        TESTS::

            sage: a.map_coefficients(lambda c: 1/c, new_coefficient_ring=QQ)
            n^4 + 1/2*n^3 + 1/3*n^2 + O(n)
            sage: _.parent()
            Asymptotic Ring <n^ZZ> over Rational Field
            sage: a.map_coefficients(lambda c: 1/c)
            Traceback (most recent call last):
            ...
            ValueError: Cannot create ExactTerm(n^3) since
            given coefficient 1/2 is not valid in
            Exact Term Monoid n^ZZ with coefficients in Integer Ring.
            > *previous* TypeError: no conversion of this rational to integer
        """
    def factorial(self):
        """
        Return the factorial of this asymptotic expansion.

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: A.<n> = AsymptoticRing(growth_group='n^ZZ * log(n)^ZZ', coefficient_ring=ZZ, default_prec=5)
            sage: n.factorial()
            sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(1/2)
            + 1/12*sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(-1/2)
            + 1/288*sqrt(2)*sqrt(pi)*e^(n*log(n))*(e^n)^(-1)*n^(-3/2)
            + O(e^(n*log(n))*(e^n)^(-1)*n^(-5/2))
            sage: _.parent()
            Asymptotic Ring <(e^(n*log(n)))^QQ * (e^n)^QQ * n^QQ * log(n)^QQ>
            over Symbolic Constants Subring

        :wikipedia:`Catalan numbers <Catalan_number>`
        `\\frac{1}{n+1}\\binom{2n}{n}`::

            sage: (2*n).factorial() / n.factorial()^2 / (n+1)  # long time
            1/sqrt(pi)*(e^n)^(2*log(2))*n^(-3/2)
            - 9/8/sqrt(pi)*(e^n)^(2*log(2))*n^(-5/2)
            + 145/128/sqrt(pi)*(e^n)^(2*log(2))*n^(-7/2)
            + O((e^n)^(2*log(2))*n^(-9/2))

        Note that this method substitutes the asymptotic expansion into
        Stirling's formula. This substitution has to be possible which is
        not always guaranteed::

            sage: S.<s> = AsymptoticRing(growth_group='s^QQ * log(s)^QQ', coefficient_ring=QQ, default_prec=4)
            sage: log(s).factorial()
            Traceback (most recent call last):
            ...
            TypeError: Cannot apply the substitution rules {s: log(s)} on
            sqrt(2)*sqrt(pi)*e^(s*log(s))*(e^s)^(-1)*s^(1/2)
            + O(e^(s*log(s))*(e^s)^(-1)*s^(-1/2)) in
            Asymptotic Ring <(e^(s*log(s)))^QQ * (e^s)^QQ * s^QQ * log(s)^QQ>
            over Symbolic Constants Subring.
            ...

        .. SEEALSO::

            :meth:`~sage.rings.asymptotic.asymptotic_expansion_generators.AsymptoticExpansionGenerators.Stirling`

        TESTS::

            sage: A.<m> = AsymptoticRing(growth_group='m^ZZ * log(m)^ZZ', coefficient_ring=QQ, default_prec=5)
            sage: m.factorial()
            sqrt(2)*sqrt(pi)*e^(m*log(m))*(e^m)^(-1)*m^(1/2)
            + 1/12*sqrt(2)*sqrt(pi)*e^(m*log(m))*(e^m)^(-1)*m^(-1/2)
            + 1/288*sqrt(2)*sqrt(pi)*e^(m*log(m))*(e^m)^(-1)*m^(-3/2)
            + O(e^(m*log(m))*(e^m)^(-1)*m^(-5/2))

        ::

            sage: A(1/2).factorial()
            1/2*sqrt(pi)
            sage: _.parent()
            Asymptotic Ring <m^ZZ * log(m)^ZZ> over Symbolic Ring

        ::

            sage: B.<a, b> = AsymptoticRing('a^ZZ * b^ZZ', QQ, default_prec=3)
            sage: b.factorial()
            O(e^(b*log(b))*(e^b)^(-1)*b^(1/2))
            sage: (a*b).factorial()
            Traceback (most recent call last):
            ...
            ValueError: Cannot build the factorial of a*b
            since it is not univariate.
        """
    def variable_names(self):
        """
        Return the names of the variables of this asymptotic expansion.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: A.<m, n> = AsymptoticRing('QQ^m * m^QQ * n^ZZ * log(n)^ZZ', QQ)
            sage: (4*2^m*m^4*log(n)).variable_names()
            ('m', 'n')
            sage: (4*2^m*m^4).variable_names()
            ('m',)
            sage: (4*log(n)).variable_names()
            ('n',)
            sage: (4*m^3).variable_names()
            ('m',)
            sage: (4*m^0).variable_names()
            ()
            sage: (4*2^m*m^4 + log(n)).variable_names()
            ('m', 'n')
            sage: (2^m + m^4 + log(n)).variable_names()
            ('m', 'n')
            sage: (2^m + m^4).variable_names()
            ('m',)
        """
    def limit(self):
        '''
        Compute the limit of this asymptotic expansion.

        OUTPUT: an element of the coefficient ring

        EXAMPLES::

            sage: A.<s> = AsymptoticRing("s^ZZ", SR, default_prec=3)
            sage: (3 + 1/s + O(1/s^2)).limit()
            3
            sage: ((1+1/s)^s).limit()
            e
            sage: (1/s).limit()
            0
            sage: (s + 3 + 1/s + O(1/s^2)).limit()
            Traceback (most recent call last):
            ...
            ValueError: Cannot determine limit of s + 3 + s^(-1) + O(s^(-2))
            sage: (O(s^0)).limit()
            Traceback (most recent call last):
            ...
            ValueError: Cannot determine limit of O(1)

        .. SEEALSO::

            :meth:`is_little_o_of_one`
        '''
    def B(self, valid_from: int = 0):
        """
        Convert all terms in this asymptotic expansion to `B`-terms.

        INPUT:

        - ``valid_from`` -- dictionary mapping variable names to lower bounds
          for the corresponding variable. The bound implied by this term is valid when
          all variables are at least their corresponding lower bound. If a number
          is passed to ``valid_from``, then the lower bounds for all variables of
          the asymptotic expansion are set to this number

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: AR.<x, z> = AsymptoticRing(growth_group='x^ZZ * z^ZZ', coefficient_ring=ZZ)
            sage: AR.B(2*x^2, {x: 10}) # indirect doctest
            B(2*x^2, x >= 10)
            sage: expr = 42*x^42 + x^10 + AR.B(x^2, 20); expr # indirect doctest
            42*x^42 + x^10 + B(x^2, x >= 20, z >= 20)
            sage: type(AR.B(x, 10)) # indirect doctest
            <class 'sage.rings.asymptotic.asymptotic_ring.AsymptoticRing_with_category.element_class'>
            sage: 2*z^3 + AR.B(5*z^2, {z: 20}) # indirect doctest
            2*z^3 + B(5*z^2, z >= 20)
            sage: (2*x).B({x: 20})
            B(2*x, x >= 20)
            sage: AR.B(4*x^2*z^3, valid_from=10) # indirect doctest
            B(4*x^2*z^3, x >= 10, z >= 10)
            sage: AR.B(42*x^2) # indirect doctest
            B(42*x^2, x >= 0, z >= 0)

        TESTS::
            sage: AR(0).B(20) # indirect doctest
            Traceback (most recent call last):
            ...
            NotImplementedBZero: got B(0)
            The error term B(0) means 0 for sufficiently large x, z.
        """

class AsymptoticRing(Parent, UniqueRepresentation, WithLocals):
    """
    A ring consisting of :class:`asymptotic expansions <AsymptoticExpansion>`.

    INPUT:

    - ``growth_group`` -- either a partially ordered group (see
      :doc:`growth_group`) or a string
      describing such a growth group (see
      :class:`~sage.rings.asymptotic.growth_group.GrowthGroupFactory`).

    - ``coefficient_ring`` -- the ring which contains the
      coefficients of the expansions

    - ``default_prec`` -- positive integer; this is the number of
      summands that are kept before truncating an infinite series

    - ``category`` -- the category of the parent can be specified
      in order to broaden the base structure. It has to be a
      subcategory of ``Category of rings``. This is also the default
      category if ``None`` is specified.

    - ``term_monoid_factory`` -- a :class:`~sage.rings.asymptotic.term_monoid.TermMonoidFactory`.
      If ``None``, then :class:`~sage.rings.asymptotic.term_monoid.DefaultTermMonoidFactory`
      is used.

    - ``locals`` -- dictionary which may contain the following keys and values:

      - ``'log'`` -- value: a function. If not given, then the usual
        :class:`log <sage.functions.log.Function_log>` is taken.
        (See also :meth:`AsymptoticExpansion.log`.)

    EXAMPLES:

    We begin with the construction of an asymptotic ring in various
    ways. First, we simply pass a string specifying the underlying
    growth group::

        sage: R1_x.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=QQ); R1_x
        Asymptotic Ring <x^QQ> over Rational Field
        sage: x
        x

    This is equivalent to the following code, which explicitly
    specifies the underlying growth group::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: G_QQ = GrowthGroup('x^QQ')
        sage: R2_x.<x> = AsymptoticRing(growth_group=G_QQ, coefficient_ring=QQ); R2_x
        Asymptotic Ring <x^QQ> over Rational Field

    Of course, the coefficient ring of the asymptotic ring and the
    base ring of the underlying growth group do not need to
    coincide::

        sage: R_ZZ_x.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=ZZ); R_ZZ_x
        Asymptotic Ring <x^QQ> over Integer Ring

    Note, we can also create and use logarithmic growth groups::

        sage: R_log = AsymptoticRing(growth_group='log(x)^ZZ', coefficient_ring=QQ); R_log
        Asymptotic Ring <log(x)^ZZ> over Rational Field

    Other growth groups are available. See :doc:`asymptotic_ring` for
    more examples.

    Below there are some technical details.

    According to the conventions for parents, uniqueness is ensured::

        sage: R1_x is R2_x
        True

    Furthermore, the coercion framework is also involved. Coercion
    between two asymptotic rings is possible (given that the
    underlying growth groups and coefficient rings are chosen
    appropriately)::

        sage: R1_x.has_coerce_map_from(R_ZZ_x)
        True

    Additionally, for the sake of convenience, the coefficient ring
    also coerces into the asymptotic ring (representing constant
    quantities)::

        sage: R1_x.has_coerce_map_from(QQ)
        True

    It is possible to customize the terms in an asymptotic expansion::

        sage: from sage.rings.asymptotic.term_monoid import ExactTermMonoid, OTermMonoid
        sage: from sage.rings.asymptotic.term_monoid import TermMonoidFactory
        sage: class MyExactTermMonoid(ExactTermMonoid):
        ....:     pass
        sage: class MyOTermMonoid(OTermMonoid):
        ....:     pass
        sage: MyTermMonoid = TermMonoidFactory('MyTermMonoid',
        ....:                                  exact_term_monoid_class=MyExactTermMonoid,
        ....:                                  O_term_monoid_class=MyOTermMonoid)
        sage: G = GrowthGroup('x^ZZ')
        sage: A.<n> = AsymptoticRing(growth_group=G, coefficient_ring=QQ, term_monoid_factory=MyTermMonoid)
        sage: a = A.an_element(); a
        1/8*x^3 + O(x)
        sage: for t in a.summands.elements_topological(reverse=True):
        ....:     print(t, type(t))
        1/8*x^3 <class '__main__.MyExactTermMonoid_with_category.element_class'>
        O(x) <class '__main__.MyOTermMonoid_with_category.element_class'>

    TESTS::

        sage: from sage.rings.asymptotic.asymptotic_ring import AsymptoticRing as AR_class
        sage: class AR(AR_class):
        ....:     class Element(AR_class.Element):
        ....:         __eq__ = AR_class.Element.has_same_summands
        sage: A = AR(growth_group='z^QQ', coefficient_ring=QQ)
        sage: from itertools import islice
        sage: TestSuite(A).run(  # not tested  # long time  # see #19424
        ....:     verbose=True,
        ....:     elements=tuple(islice(A.some_elements(), int(10))),
        ....:     skip=('_test_some_elements',  # to many elements
        ....:           '_test_distributivity'))  # due to cancellations: O(z) != O(z^2)
    """
    Element = AsymptoticExpansion
    @staticmethod
    def __classcall__(cls, growth_group=None, coefficient_ring=None, names=None, category=None, default_prec=None, term_monoid_factory=None, locals=None):
        """
        Normalize the input in order to ensure a unique
        representation of the parent.

        For more information see :class:`AsymptoticRing`.

        EXAMPLES:

        ``__classcall__`` unifies the input to the constructor of
        :class:`AsymptoticRing` such that the instances generated
        are unique. Also, this enables the use of the generation
        framework::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: MG = GrowthGroup('x^ZZ')
            sage: AR1 = AsymptoticRing(growth_group=MG, coefficient_ring=ZZ)
            sage: AR2.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR1 is AR2
            True

        The bracket notation can only be used if the growth group
        has a generator::

            sage: AR.<lx> = AsymptoticRing(growth_group='log(x)^ZZ', coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError:  Growth Group log(x)^ZZ does not provide any
            generators but name 'lx' given.

        The names of the generators have to agree with the names used in
        the growth group except for univariate rings::

            sage: A.<icecream> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ); A
            Asymptotic Ring <x^ZZ> over Integer Ring
            sage: icecream
            x
            sage: A.<x, y> = AsymptoticRing(growth_group='x^ZZ * y^ZZ', coefficient_ring=ZZ); A
            Asymptotic Ring <x^ZZ * y^ZZ> over Integer Ring
            sage: A.<y, x> = AsymptoticRing(growth_group='x^ZZ * y^ZZ', coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Names 'y', 'x' do not coincide with
            generators 'x', 'y' of Growth Group x^ZZ * y^ZZ.
            sage: A.<a, b> = AsymptoticRing(growth_group='x^ZZ * y^ZZ', coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Names 'a', 'b' do not coincide with
            generators 'x', 'y' of Growth Group x^ZZ * y^ZZ.
            sage: A.<x, b> = AsymptoticRing(growth_group='x^ZZ * y^ZZ', coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Names 'x', 'b' do not coincide with
            generators 'x', 'y' of Growth Group x^ZZ * y^ZZ.
            sage: A.<x> = AsymptoticRing(growth_group='x^ZZ * y^ZZ', coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Name 'x' do not coincide with
            generators 'x', 'y' of Growth Group x^ZZ * y^ZZ.
            sage: A.<x, y, z> = AsymptoticRing(growth_group='x^ZZ * y^ZZ', coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Names 'x', 'y', 'z' do not coincide with
            generators 'x', 'y' of Growth Group x^ZZ * y^ZZ.

        TESTS::

            sage: AsymptoticRing(growth_group=None, coefficient_ring=ZZ)
            Traceback (most recent call last):
            ...
            ValueError: Growth group not specified. Cannot continue.
            sage: AsymptoticRing(growth_group='x^ZZ', coefficient_ring=None)
            Traceback (most recent call last):
            ...
            ValueError: Coefficient ring not specified. Cannot continue.
            sage: AsymptoticRing(growth_group='x^ZZ', coefficient_ring='icecream')
            Traceback (most recent call last):
            ...
            ValueError: icecream is not a ring. Cannot continue.

        ::

            sage: A.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=ZZ)
            sage: from sage.rings.asymptotic.term_monoid import DefaultTermMonoidFactory
            sage: A.term_monoid_factory is DefaultTermMonoidFactory
            True
        """
    def __init__(self, growth_group, coefficient_ring, category, default_prec, term_monoid_factory, locals) -> None:
        """
        See :class:`AsymptoticRing` for more information.

        TESTS::

            sage: R1 = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ); R1
            Asymptotic Ring <x^ZZ> over Integer Ring
            sage: R2.<x> = AsymptoticRing(growth_group='x^QQ', coefficient_ring=QQ); R2
            Asymptotic Ring <x^QQ> over Rational Field
            sage: R1 is R2
            False

        ::

            sage: R3 = AsymptoticRing('x^ZZ')
            Traceback (most recent call last):
            ...
            ValueError: Coefficient ring not specified. Cannot continue.
        """
    @property
    def growth_group(self):
        """
        The growth group of this asymptotic ring.

        EXAMPLES::

            sage: AR = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.growth_group
            Growth Group x^ZZ

        .. SEEALSO::

            :doc:`growth_group`
        """
    @property
    def coefficient_ring(self):
        """
        The coefficient ring of this asymptotic ring.

        EXAMPLES::

            sage: AR = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.coefficient_ring
            Integer Ring
        """
    @property
    def default_prec(self):
        """
        The default precision of this asymptotic ring.

        This is the parameter used to determine how many summands
        are kept before truncating an infinite series (which occur
        when inverting asymptotic expansions).

        EXAMPLES::

            sage: AR = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.default_prec
            20
            sage: AR = AsymptoticRing('x^ZZ', ZZ, default_prec=123)
            sage: AR.default_prec
            123
        """
    @property
    def term_monoid_factory(self):
        """
        The term monoid factory of this asymptotic ring.

        EXAMPLES::

            sage: AR = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.term_monoid_factory
            Term Monoid Factory 'sage.rings.asymptotic.term_monoid.DefaultTermMonoidFactory'

        .. SEEALSO::

            :doc:`term_monoid`
        """
    def term_monoid(self, type):
        """
        Return the term monoid of this asymptotic ring of specified ``type``.

        INPUT:

        - ``type`` -- ``'O'`` or ``'exact'``, or an instance of an existing
          term monoid.
          See :class:`~sage.rings.asymptotic.term_monoid.TermMonoidFactory`
          for more details.

        OUTPUT:

        A term monoid object derived from
        :class:`~sage.rings.asymptotic.term_monoid.GenericTermMonoid`.

        EXAMPLES::

            sage: AR = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.term_monoid('exact')
            Exact Term Monoid x^ZZ with coefficients in Integer Ring
            sage: AR.term_monoid('O')
            O-Term Monoid x^ZZ with implicit coefficients in Integer Ring
            sage: AR.term_monoid(AR.term_monoid('exact'))
            Exact Term Monoid x^ZZ with coefficients in Integer Ring
        """
    def change_parameter(self, **kwds):
        """
        Return an asymptotic ring with a change in one or more of the given parameters.

        INPUT:

        - ``growth_group`` -- (default: ``None``) the new growth group

        - ``coefficient_ring`` -- (default: ``None``) the new coefficient ring

        - ``category`` -- (default: ``None``) the new category

        - ``default_prec`` -- (default: ``None``) the new default precision

        OUTPUT: an asymptotic ring

        EXAMPLES::

            sage: A = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: A.change_parameter(coefficient_ring=QQ)
            Asymptotic Ring <x^ZZ> over Rational Field

        TESTS::

            sage: A.change_parameter(coefficient_ring=ZZ) is A
            True
            sage: A.change_parameter(coefficient_ring=None) is A
            True
        """
    def some_elements(self):
        """
        Return some elements of this term monoid.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from itertools import islice
            sage: A = AsymptoticRing(growth_group='z^QQ', coefficient_ring=ZZ)
            sage: tuple(islice(A.some_elements(), int(10)))
            (z^(3/2) + O(z^(1/2)),
             O(z^(1/2)),
             z^(3/2) + O(z^(-1/2)),
             -z^(3/2) + O(z^(1/2)),
             O(z^(-1/2)),
             O(z^2),
             z^6 + O(z^(1/2)),
             -z^(3/2) + O(z^(-1/2)),
             O(z^2),
             z^(3/2) + O(z^(-2)))
        """
    def gens(self) -> tuple:
        """
        Return a tuple with generators of this asymptotic ring.

        OUTPUT: a tuple of asymptotic expansions

        .. NOTE::

            Generators do not necessarily exist. This depends on the
            underlying growth group. For example,
            :class:`monomial growth groups <sage.rings.asymptotic.growth_group.MonomialGrowthGroup>`
            have a generator, and exponential growth groups
            do not.

        EXAMPLES::

            sage: AR.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.gens()
            (x,)
            sage: B.<y,z> = AsymptoticRing(growth_group='y^ZZ * z^ZZ', coefficient_ring=QQ)
            sage: B.gens()
            (y, z)
        """
    def gen(self, n: int = 0):
        """
        Return the ``n``-th generator of this asymptotic ring.

        INPUT:

        - ``n`` -- (default: `0`) a nonnegative integer

        OUTPUT: an asymptotic expansion

        EXAMPLES::

            sage: R.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: R.gen()
            x
        """
    def ngens(self):
        """
        Return the number of generators of this asymptotic ring.

        OUTPUT: integer

        EXAMPLES::

            sage: AR.<x> = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: AR.ngens()
            1
        """
    def coefficients_of_generating_function(self, function, singularities, precision=None, return_singular_expansions: bool = False, error_term=None):
        """
        Return the asymptotic growth of the coefficients of some
        generating function by means of Singularity Analysis.

        INPUT:

        - ``function`` -- a callable function in one variable

        - ``singularities`` -- list of dominant singularities of the function

        - ``precision`` -- integer (default: ``None``); if ``None``, then
          the default precision of the asymptotic ring is used

        - ``return_singular_expansions`` -- boolean (default: ``False``);
          if set, the singular expansions are also returned

        - ``error_term`` -- (default: ``None``) an asymptotic expansion.
          If ``None``, then this is interpreted as zero.
          The contributions of the coefficients are added to ``error_term``
          during Singularity Analysis.

        OUTPUT:

        - If ``return_singular_expansions=False``: An asymptotic expansion from
          this ring.

        - If ``return_singular_expansions=True``: A named tuple with
          components ``asymptotic_expansion`` and
          ``singular_expansions``. The former contains an asymptotic
          expansion from this ring, the latter is a dictionary which
          contains the singular expansions around the singularities.

        .. TODO::

            Make this method more usable by implementing the
            processing of symbolic expressions.

        EXAMPLES:

        Catalan numbers::

            sage: def catalan(z):
            ....:     return (1-(1-4*z)^(1/2))/(2*z)
            sage: B.<n> = AsymptoticRing('QQ^n * n^QQ', QQ)
            sage: B.coefficients_of_generating_function(catalan, (1/4,), precision=3)
            1/sqrt(pi)*4^n*n^(-3/2) - 9/8/sqrt(pi)*4^n*n^(-5/2)
            + 145/128/sqrt(pi)*4^n*n^(-7/2) + O(4^n*n^(-4))
            sage: B.coefficients_of_generating_function(catalan, (1/4,), precision=2,
            ....:                        return_singular_expansions=True)
            SingularityAnalysisResult(asymptotic_expansion=1/sqrt(pi)*4^n*n^(-3/2)
            - 9/8/sqrt(pi)*4^n*n^(-5/2) + O(4^n*n^(-3)),
            singular_expansions={1/4: 2 - 2*T^(-1/2)
            + 2*T^(-1) - 2*T^(-3/2) + O(T^(-2))})

        Unit fractions::

            sage: def logarithmic(z):
            ....:     return -log(1-z)
            sage: B.coefficients_of_generating_function(logarithmic, (1,), precision=5)
            n^(-1) + O(n^(-3))

        Harmonic numbers::

            sage: def harmonic(z):
            ....:     return -log(1-z)/(1-z)
            sage: B.<n> = AsymptoticRing('QQ^n * n^QQ * log(n)^QQ', QQ)
            sage: ex = B.coefficients_of_generating_function(harmonic, (1,), precision=13); ex
            log(n) + euler_gamma + 1/2*n^(-1) - 1/12*n^(-2) + 1/120*n^(-4)
            + O(n^(-6))
            sage: ex.has_same_summands(asymptotic_expansions.HarmonicNumber(
            ....:    'n', precision=5))
            True

        Positive and negative singularities::

            sage: def permutations_odd_cycles(z):
            ....:     return sqrt((1+z) / (1-z))
            sage: ex = B.coefficients_of_generating_function(
            ....:     permutations_odd_cycles, (1, -1,), precision=2,
            ....: ); ex
            sqrt(2)/sqrt(pi)*n^(-1/2) - 1/2*sqrt(1/2)/sqrt(pi)*n^(-3/2)*(-1)^n
            + O(n^(-5/2))

        .. WARNING::

            Once singular expansions around points other than infinity
            are implemented (:issue:`20050`), the output in the case
            ``return_singular_expansions`` will change to return singular
            expansions around the singularities.

        In the following example, the result is an exact asymptotic expression
        for sufficiently large `n` (i.e., there might be finitely many
        exceptional values). This is encoded by an `O(0)` error term::

            sage: def f(z):
            ....:     return z/(1-z)
            sage: B.coefficients_of_generating_function(f, (1,), precision=3)
            Traceback (most recent call last):
            ...
            NotImplementedOZero: got 1 + O(0)
            The error term O(0) means 0 for sufficiently large n.

        In this case, we can manually intervene by adding an error term
        that suits us::

            sage: B.coefficients_of_generating_function(f, (1,), precision=3,
            ....:                                       error_term=O(n^-100))
            1 + O(n^(-100))
        """
    def create_summand(self, type, data=None, **kwds):
        """
        Create a simple asymptotic expansion consisting of a single
        summand.

        INPUT:

        - ``type`` -- 'O' or 'exact'

        - ``data`` -- the element out of which a summand has to be created

        - ``growth`` -- an element of the :meth:`growth_group`

        - ``coefficient`` -- an element of the :meth:`coefficient_ring`

        .. NOTE::

            Either ``growth`` and ``coefficient`` or ``data`` have to
            be specified.

        OUTPUT: an asymptotic expansion

        .. NOTE::

            This method calls the factory :class:`TermMonoid
            <sage.rings.asymptotic.term_monoid.TermMonoidFactory>`
            with the appropriate arguments.

        EXAMPLES::

            sage: R = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ)
            sage: R.create_summand('O', x^2)
            O(x^2)
            sage: R.create_summand('exact', growth=x^456, coefficient=123)
            123*x^456
            sage: R.create_summand('exact', data=12*x^13)
            12*x^13

        TESTS::

            sage: R.create_summand('exact', data='12*x^13')
            12*x^13
            sage: R.create_summand('exact', data='x^13 * 12')
            12*x^13
            sage: R.create_summand('exact', data='x^13')
            x^13
            sage: R.create_summand('exact', data='12')
            12
            sage: R.create_summand('exact', data=12)
            12

        ::

            sage: Z = R.change_parameter(coefficient_ring=Zmod(3))
            sage: Z.create_summand('exact', data=42)
            0

        ::

            sage: R.create_summand('O', growth=42*x^2, coefficient=1)
            Traceback (most recent call last):
            ...
            ValueError: Growth 42*x^2 is not valid in O-Term Monoid x^ZZ with implicit coefficients in Integer Ring.
            > *previous* ValueError: 42*x^2 is not in Growth Group x^ZZ.

        ::

            sage: AR.<z> = AsymptoticRing('z^QQ', QQ)
            sage: AR.create_summand('exact', growth='z^2')
            Traceback (most recent call last):
            ...
            TypeError: Cannot create exact term: only 'growth' but
            no 'coefficient' specified.
        """
    def variable_names(self):
        """
        Return the names of the variables.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: A = AsymptoticRing(growth_group='x^ZZ * QQ^y', coefficient_ring=QQ)
            sage: A.variable_names()
            ('x', 'y')
        """
    def construction(self):
        """
        Return the construction of this asymptotic ring.

        OUTPUT:

        A pair whose first entry is an
        :class:`asymptotic ring construction functor <AsymptoticRingFunctor>`
        and its second entry the coefficient ring.

        EXAMPLES::

            sage: A = AsymptoticRing(growth_group='x^ZZ * QQ^y', coefficient_ring=QQ)
            sage: A.construction()
            (AsymptoticRing<x^ZZ * QQ^y * Signs^y>, Rational Field)

        .. SEEALSO::

            :doc:`asymptotic_ring`,
            :class:`AsymptoticRing`,
            :class:`AsymptoticRingFunctor`.

        TESTS:

        :issue:`22392`::

            sage: from sage.rings.asymptotic.asymptotic_ring import AsymptoticRing
            sage: class MyAsymptoticRing(AsymptoticRing):
            ....:     pass
            sage: A = MyAsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ)
            sage: A.construction()[0].cls
            <class '__main__.MyAsymptoticRing'>
        """
    @staticmethod
    def B(expression, valid_from: int = 0):
        """
        Create a B-term.

        INPUT:

        - ``valid_from`` -- dictionary mapping variable names to lower bounds
          for the corresponding variable. The bound implied by this term is valid when
          all variables are at least their corresponding lower bound. If a number
          is passed to ``valid_from``, then the lower bounds for all variables of
          the asymptotic expansion are set to this number

        OUTPUT: a B-term

        EXAMPLES::

            sage: A.<x> = AsymptoticRing(growth_group='x^ZZ * QQ^y', coefficient_ring=QQ)
            sage: A.B(2*x^3, {x: 5})
            B(2*x^3, x >= 5)
        """

class AsymptoticRingFunctor(ConstructionFunctor):
    """
    A :class:`construction functor <sage.categories.pushout.ConstructionFunctor>`
    for :class:`asymptotic rings <AsymptoticRing>`.

    INPUT:

    - ``growth_group`` -- a partially ordered group (see
      :class:`AsymptoticRing` or
      :doc:`growth_group` for details).

    - ``default_prec`` -- ``None`` (default) or integer

    - ``category`` -- ``None`` (default) or a category

    - ``cls`` -- :class:`AsymptoticRing` (default) or a derived class

    EXAMPLES::

        sage: AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ).construction()  # indirect doctest
        (AsymptoticRing<x^ZZ>, Rational Field)

    .. SEEALSO::

        :doc:`asymptotic_ring`,
        :class:`AsymptoticRing`,
        :class:`sage.rings.asymptotic.growth_group.AbstractGrowthGroupFunctor`,
        :class:`sage.rings.asymptotic.growth_group.ExponentialGrowthGroupFunctor`,
        :class:`sage.rings.asymptotic.growth_group.MonomialGrowthGroupFunctor`,
        :class:`sage.categories.pushout.ConstructionFunctor`.

    TESTS::

        sage: X = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ)
        sage: Y = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=QQ)
        sage: cm = sage.structure.element.get_coercion_model()
        sage: cm.record_exceptions()
        sage: cm.common_parent(X, Y)
        Asymptotic Ring <x^ZZ * y^ZZ> over Rational Field
        sage: sage.structure.element.coercion_traceback()  # not tested

    ::

        sage: from sage.categories.pushout import pushout
        sage: pushout(AsymptoticRing(growth_group='x^ZZ', coefficient_ring=ZZ), QQ)
        Asymptotic Ring <x^ZZ> over Rational Field
    """
    rank: int
    growth_group: Incomplete
    cls: Incomplete
    def __init__(self, growth_group, default_prec=None, category=None, term_monoid_factory=None, locals=None, cls=None) -> None:
        """
        See :class:`AsymptoticRingFunctor` for details.

        TESTS::

            sage: from sage.rings.asymptotic.asymptotic_ring import AsymptoticRingFunctor
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: AsymptoticRingFunctor(GrowthGroup('x^ZZ'))
            AsymptoticRing<x^ZZ>
        """
    def merge(self, other):
        """
        Merge this functor with ``other`` if possible.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: a functor or ``None``

        EXAMPLES::

            sage: X = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ)
            sage: Y = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=QQ)
            sage: F_X = X.construction()[0]
            sage: F_Y = Y.construction()[0]
            sage: F_X.merge(F_X)
            AsymptoticRing<x^ZZ>
            sage: F_X.merge(F_Y)
            AsymptoticRing<x^ZZ * y^ZZ>

        TESTS:

        :issue:`22396`::

            sage: AN = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=QQ)
            sage: F_AN = AN.construction()[0]; F_AN._default_prec_ = None
            sage: A3 = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ, default_prec=3)
            sage: F_A3 = A3.construction()[0]
            sage: A5 = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ, default_prec=5)
            sage: F_A5 = A5.construction()[0]

            sage: F_AN.merge(F_AN)(ZZ).default_prec
            20
            sage: F_AN.merge(F_A3)(ZZ).default_prec
            3
            sage: F_AN.merge(F_A5)(ZZ).default_prec
            5
            sage: F_A3.merge(F_AN)(ZZ).default_prec
            3
            sage: F_A3.merge(F_A3)(ZZ).default_prec
            3
            sage: F_A3.merge(F_A5)(ZZ).default_prec
            3
            sage: F_A5.merge(F_AN)(ZZ).default_prec
            5
            sage: F_A5.merge(F_A3)(ZZ).default_prec
            3
            sage: F_A5.merge(F_A5)(ZZ).default_prec
            5

            sage: A = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=QQ)
            sage: F1 = A.construction()[0]
            sage: F2 = A.construction()[0]; F2._category_ = Rings()
            sage: F1.merge(F2)._category_
            Category of rings
        """
    def __eq__(self, other) -> bool:
        """
        Return whether this functor is equal to ``other``.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: boolean

        EXAMPLES::

            sage: X = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ)
            sage: Y = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=QQ)
            sage: F_X = X.construction()[0]
            sage: F_Y = Y.construction()[0]
            sage: F_X == F_X
            True
            sage: F_X == F_Y
            False
        """
    def __ne__(self, other) -> bool:
        """
        Return whether this functor is not equal to ``other``.

        INPUT:

        - ``other`` -- a functor

        OUTPUT: boolean

        EXAMPLES::

            sage: X = AsymptoticRing(growth_group='x^ZZ', coefficient_ring=QQ)
            sage: Y = AsymptoticRing(growth_group='y^ZZ', coefficient_ring=QQ)
            sage: F_X = X.construction()[0]
            sage: F_Y = Y.construction()[0]
            sage: F_X != F_X
            False
            sage: F_X != F_Y
            True
        """
