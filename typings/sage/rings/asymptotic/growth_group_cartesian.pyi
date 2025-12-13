from .growth_group import GenericGrowthGroup as GenericGrowthGroup
from _typeshed import Incomplete
from sage.combinat.posets.cartesian_product import CartesianProductPoset as CartesianProductPoset
from sage.structure.factory import UniqueFactory as UniqueFactory

class CartesianProductFactory(UniqueFactory):
    """
    Create various types of Cartesian products depending on its input.

    INPUT:

    - ``growth_groups`` -- tuple (or other iterable) of growth groups

    - ``order`` -- (default: ``None``) if specified, then this order
      is taken for comparing two Cartesian product elements. If ``order`` is
      ``None`` this is determined automatically.

    .. NOTE::

        The Cartesian product of growth groups is again a growth
        group. In particular, the resulting structure is partially
        ordered.

        The order on the product is determined as follows:

        - Cartesian factors with respect to the same variable are
          ordered lexicographically. This causes
          ``GrowthGroup('x^ZZ * log(x)^ZZ')`` and
          ``GrowthGroup('log(x)^ZZ * x^ZZ')`` to produce two
          different growth groups.

        - Factors over different variables are equipped with the
          product order (i.e. the comparison is component-wise).

        Also, note that the sets of variables of the Cartesian
        factors have to be either equal or disjoint.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: A = GrowthGroup('x^ZZ'); A
        Growth Group x^ZZ
        sage: B = GrowthGroup('log(x)^ZZ'); B
        Growth Group log(x)^ZZ
        sage: C = cartesian_product([A, B]); C  # indirect doctest
        Growth Group x^ZZ * log(x)^ZZ
        sage: C._le_ == C.le_lex
        True
        sage: D = GrowthGroup('y^ZZ'); D
        Growth Group y^ZZ
        sage: E = cartesian_product([A, D]); E  # indirect doctest
        Growth Group x^ZZ * y^ZZ
        sage: E._le_ == E.le_product
        True
        sage: F = cartesian_product([C, D]); F  # indirect doctest
        Growth Group x^ZZ * log(x)^ZZ * y^ZZ
        sage: F._le_ == F.le_product
        True
        sage: cartesian_product([A, E]); G  # indirect doctest
        Traceback (most recent call last):
        ...
        ValueError: The growth groups (Growth Group x^ZZ, Growth Group x^ZZ * y^ZZ)
        need to have pairwise disjoint or equal variables.
        sage: cartesian_product([A, B, D])  # indirect doctest
        Growth Group x^ZZ * log(x)^ZZ * y^ZZ

    TESTS::

        sage: from sage.rings.asymptotic.growth_group_cartesian import CartesianProductFactory
        sage: CartesianProductFactory('factory')([A, B], category=Groups() & Posets())
        Growth Group x^ZZ * log(x)^ZZ
        sage: CartesianProductFactory('factory')([], category=Sets())
        Traceback (most recent call last):
        ...
        TypeError: Cannot create Cartesian product without factors.

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: G1 = GrowthGroup('x^QQ')
        sage: G2 = GrowthGroup('log(x)^ZZ')
        sage: G = cartesian_product([G1, G2])
        sage: cartesian_product([G1, G2], category=G.category()) is G
        True
    """
    def create_key_and_extra_args(self, growth_groups, category, **kwds):
        """
        Given the arguments and keywords, create a key that uniquely
        determines this object.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group_cartesian import CartesianProductFactory
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: A = GrowthGroup('x^ZZ')
            sage: CartesianProductFactory('factory').create_key_and_extra_args(
            ....:     [A], category=Sets(), order='blub')
            (((Growth Group x^ZZ,), Category of posets), {'order': 'blub'})
        """
    def create_object(self, version, args, **kwds):
        """
        Create an object from the given arguments.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: cartesian_product([GrowthGroup('x^ZZ')])  # indirect doctest
            Growth Group x^ZZ
        """

CartesianProductGrowthGroups: Incomplete

class GenericProduct(CartesianProductPoset, GenericGrowthGroup):
    """
    A Cartesian product of growth groups.

    EXAMPLES::

        sage: from sage.rings.asymptotic.growth_group import GrowthGroup
        sage: P = GrowthGroup('x^QQ')
        sage: L = GrowthGroup('log(x)^ZZ')
        sage: C = cartesian_product([P, L], order='lex'); C  # indirect doctest
        Growth Group x^QQ * log(x)^ZZ
        sage: C.an_element()
        x^(1/2)*log(x)

    ::

        sage: Px = GrowthGroup('x^QQ')
        sage: Lx = GrowthGroup('log(x)^ZZ')
        sage: Cx = cartesian_product([Px, Lx], order='lex')  # indirect doctest
        sage: Py = GrowthGroup('y^QQ')
        sage: C = cartesian_product([Cx, Py], order='product'); C  # indirect doctest
        Growth Group x^QQ * log(x)^ZZ * y^QQ
        sage: C.an_element()
        x^(1/2)*log(x)*y^(1/2)

    .. SEEALSO::

        :class:`~sage.sets.cartesian_product.CartesianProduct`,
        :class:`~sage.combinat.posets.cartesian_product.CartesianProductPoset`.
    """
    __classcall__: Incomplete
    def __init__(self, sets, category, **kwds) -> None:
        """
        See :class:`GenericProduct` for details.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^ZZ * y^ZZ')  # indirect doctest
            Growth Group x^ZZ * y^ZZ

        Check :issue:`26452`::

            sage: from sage.rings.asymptotic.growth_group import MonomialGrowthGroup
            sage: R = QQ.extension(x^2+1, 'i')
            sage: P = MonomialGrowthGroup(R, 'w')
            sage: L = MonomialGrowthGroup(ZZ, 'log(w)')
            sage: cartesian_product([P, L])
            Growth Group w^(Number Field in i with defining polynomial x^2 + 1) * log(w)^ZZ
        """
    __hash__: Incomplete
    def some_elements(self):
        """
        Return some elements of this Cartesian product of growth groups.

        See :class:`TestSuite` for a typical use case.

        OUTPUT: an iterator

        EXAMPLES::

            sage: from itertools import islice
            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('(QQ_+)^y * x^QQ * log(x)^ZZ')
            sage: tuple(islice(G.some_elements(), 10r))
            (x^(1/2)*(1/2)^y,
             x^(-1/2)*log(x)*2^y,
             x^2*log(x)^(-1),
             x^(-2)*log(x)^2*42^y,
             log(x)^(-2)*(2/3)^y,
             x*log(x)^3*(3/2)^y,
             x^(-1)*log(x)^(-3)*(4/5)^y,
             x^42*log(x)^4*(5/4)^y,
             x^(2/3)*log(x)^(-4)*(6/7)^y,
             x^(-2/3)*log(x)^5*(7/6)^y)
        """
    def cartesian_injection(self, factor, element):
        """
        Inject the given element into this Cartesian product at the given factor.

        INPUT:

        - ``factor`` -- a growth group (a factor of this Cartesian product)

        - ``element`` -- an element of ``factor``

        OUTPUT: an element of this Cartesian product

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('x^ZZ * y^QQ')
            sage: G.cartesian_injection(G.cartesian_factors()[1], 'y^7')
            y^7
        """
    def gens_monomial(self) -> tuple:
        """
        Return a tuple containing monomial generators of this growth group.

        OUTPUT: a tuple containing elements of this growth group

        .. NOTE::

            This method calls the ``gens_monomial()`` method on the
            individual factors of this Cartesian product and
            concatenates the respective outputs.

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: G = GrowthGroup('x^ZZ * log(x)^ZZ * y^QQ * log(z)^ZZ')
            sage: G.gens_monomial()
            (x, y)

        TESTS::

            sage: all(g.parent() == G for g in G.gens_monomial())
            True
        """
    def variable_names(self):
        """
        Return the names of the variables.

        OUTPUT: a tuple of strings

        EXAMPLES::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: GrowthGroup('x^ZZ * log(x)^ZZ * y^QQ * log(z)^ZZ').variable_names()
            ('x', 'y', 'z')
        """
    class Element(CartesianProductPoset.Element):
        is_lt_one: Incomplete
        def __pow__(self, exponent):
            """
            Calculate the power of this growth element to the given
            ``exponent``.

            INPUT:

            - ``exponent`` -- a number

            OUTPUT: a growth element

            EXAMPLES::

                sage: from sage.rings.asymptotic.growth_group import GrowthGroup
                sage: G = GrowthGroup('x^ZZ * y^QQ * z^ZZ')
                sage: x, y, z = G.gens_monomial()
                sage: (x^5 * y * z^5)^(1/5)  # indirect doctest
                x*y^(1/5)*z

            ::

                sage: G = GrowthGroup('x^QQ * log(x)^QQ'); x = G('x')
                sage: (x^(21/5) * log(x)^7)^(1/42)  # indirect doctest
                x^(1/10)*log(x)^(1/6)
            """
        def factors(self):
            """
            Return the atomic factors of this growth element. An atomic factor
            cannot be split further and is not the identity (`1`).

            OUTPUT: a tuple of growth elements

            EXAMPLES::

                sage: from sage.rings.asymptotic.growth_group import GrowthGroup
                sage: G = GrowthGroup('x^ZZ * log(x)^ZZ * y^ZZ')
                sage: x, y = G.gens_monomial()
                sage: x.factors()
                (x,)
                sage: f = (x * y).factors(); f
                (x, y)
                sage: tuple(factor.parent() for factor in f)
                (Growth Group x^ZZ, Growth Group y^ZZ)
                sage: f = (x * log(x)).factors(); f
                (x, log(x))
                sage: tuple(factor.parent() for factor in f)
                (Growth Group x^ZZ, Growth Group log(x)^ZZ)

            ::

                sage: G = GrowthGroup('x^ZZ * log(x)^ZZ * log(log(x))^ZZ * y^QQ')
                sage: x, y = G.gens_monomial()
                sage: f = (x * log(x) * y).factors(); f
                (x, log(x), y)
                sage: tuple(factor.parent() for factor in f)
                (Growth Group x^ZZ, Growth Group log(x)^ZZ, Growth Group y^QQ)

            ::

                sage: G.one().factors()
                ()
            """
        log: Incomplete
        log_factor: Incomplete
        rpow: Incomplete
        def exp(self):
            '''
            The exponential of this element.

            OUTPUT: a growth element

            EXAMPLES::

                sage: from sage.rings.asymptotic.growth_group import GrowthGroup
                sage: G = GrowthGroup(\'x^ZZ * log(x)^ZZ * log(log(x))^ZZ\')
                sage: x = G(\'x\')
                sage: exp(log(x))
                x
                sage: exp(log(log(x)))
                log(x)

            ::

                sage: exp(x)
                Traceback (most recent call last):
                ...
                ArithmeticError: Cannot construct e^x in
                Growth Group x^ZZ * log(x)^ZZ * log(log(x))^ZZ
                > *previous* TypeError: unsupported operand parent(s) for *:
                \'Growth Group x^ZZ * log(x)^ZZ * log(log(x))^ZZ\' and
                \'Growth Group (e^x)^ZZ\'

            TESTS::

                sage: E = GrowthGroup("(e^y)^QQ * y^QQ * log(y)^QQ")
                sage: y = E(\'y\')
                sage: log(exp(y))
                y
                sage: exp(log(y))
                y
            '''
        def __invert__(self):
            """
            Return the multiplicative inverse of this Cartesian product.

            OUTPUT: a growth element

            .. NOTE::

                The result may live in a larger parent than we started with.

            TESTS::

                 sage: from sage.rings.asymptotic.growth_group import GrowthGroup
                 sage: G = GrowthGroup('(ZZ_+)^x * x^ZZ')
                 sage: g = G('2^x * x^3')
                 sage: (~g).parent()
                 Growth Group QQ^x * x^ZZ
            """
        def variable_names(self):
            """
            Return the names of the variables of this growth element.

            OUTPUT: a tuple of strings

            EXAMPLES::

                sage: from sage.rings.asymptotic.growth_group import GrowthGroup
                sage: G = GrowthGroup('QQ^m * m^QQ * log(n)^ZZ')
                sage: G('2^m * m^4 * log(n)').variable_names()
                ('m', 'n')
                sage: G('2^m * m^4').variable_names()
                ('m',)
                sage: G('log(n)').variable_names()
                ('n',)
                sage: G('m^3').variable_names()
                ('m',)
                sage: G('m^0').variable_names()
                ()
            """
    CartesianProduct = CartesianProductGrowthGroups

class UnivariateProduct(GenericProduct):
    """
    A Cartesian product of growth groups with the same variables.

    .. NOTE::

        A univariate product of growth groups is ordered
        lexicographically. This is motivated by the assumption
        that univariate growth groups can be ordered in a chain
        with respect to the growth they model (e.g.
        ``x^ZZ * log(x)^ZZ``: polynomial growth dominates
        logarithmic growth).

    .. SEEALSO::

        :class:`MultivariateProduct`,
        :class:`GenericProduct`.
    """
    def __init__(self, sets, category, **kwargs) -> None:
        """
        See :class:`UnivariateProduct` for details.

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: type(GrowthGroup('x^ZZ * log(x)^ZZ'))  # indirect doctest
            <class 'sage.rings.asymptotic.growth_group_cartesian.UnivariateProduct_with_category'>
        """
    CartesianProduct = CartesianProductGrowthGroups

class MultivariateProduct(GenericProduct):
    """
    A Cartesian product of growth groups with pairwise disjoint
    (or equal) variable sets.

    .. NOTE::

        A multivariate product of growth groups is ordered by
        means of the product order, i.e. component-wise. This is
        motivated by the assumption that different variables are
        considered to be independent (e.g. ``x^ZZ * y^ZZ``).

    .. SEEALSO::

        :class:`UnivariateProduct`,
        :class:`GenericProduct`.
    """
    def __init__(self, sets, category, **kwargs) -> None:
        """

        TESTS::

            sage: from sage.rings.asymptotic.growth_group import GrowthGroup
            sage: type(GrowthGroup('x^ZZ * y^ZZ'))  # indirect doctest
            <class 'sage.rings.asymptotic.growth_group_cartesian.MultivariateProduct_with_category'>
        """
    CartesianProduct = CartesianProductGrowthGroups
