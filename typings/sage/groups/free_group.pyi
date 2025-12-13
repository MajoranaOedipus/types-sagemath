from sage.categories.groups import Groups as Groups
from sage.groups.group import Group as Group
from sage.groups.libgap_wrapper import ElementLibGAP as ElementLibGAP, ParentLibGAP as ParentLibGAP
from sage.libs.gap.element import GapElement as GapElement
from sage.libs.gap.libgap import libgap as libgap
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import coercion_model as coercion_model, parent as parent
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sequence import Sequence as Sequence
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation

def is_FreeGroup(x):
    """
    Test whether ``x`` is a :class:`FreeGroup_class`.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.groups.free_group import is_FreeGroup
        sage: is_FreeGroup('a string')                                                  # needs sage.combinat
        False
        sage: is_FreeGroup(FreeGroup(0))
        True
        sage: is_FreeGroup(FreeGroup(index_set=ZZ))                                     # needs sage.combinat
        True
    """

class FreeGroupElement(ElementLibGAP):
    """
    A wrapper of GAP's Free Group elements.

    INPUT:

    - ``x`` -- something that determines the group element; either a
      :class:`~sage.libs.gap.element.GapElement` or the Tietze list
      (see :meth:`Tietze`) of the group element

    - ``parent`` -- the parent :class:`FreeGroup`

    EXAMPLES::

        sage: G = FreeGroup('a, b')
        sage: x = G([1, 2, -1, -2])
        sage: x
        a*b*a^-1*b^-1
        sage: y = G([2, 2, 2, 1, -2, -2, -2])
        sage: y
        b^3*a*b^-3
        sage: x*y
        a*b*a^-1*b^2*a*b^-3
        sage: y*x
        b^3*a*b^-3*a*b*a^-1*b^-1
        sage: x^(-1)
        b*a*b^-1*a^-1
        sage: x == x*y*y^(-1)
        True
    """
    def __init__(self, parent, x) -> None:
        """
        The Python constructor.

        See :class:`FreeGroupElement` for details.

        TESTS::

            sage: G.<a,b> = FreeGroup()
            sage: x = G([1, 2, -1, -1])
            sage: x # indirect doctest
            a*b*a^-2
            sage: y = G([2, 2, 2, 1, -2, -2, -1])
            sage: y # indirect doctest
            b^3*a*b^-2*a^-1

            sage: TestSuite(G).run()
            sage: TestSuite(x).run()
        """
    def __hash__(self):
        """
        TESTS::

            sage: G.<a,b> = FreeGroup()
            sage: hash(a*b*b*~a) == hash((1, 2, 2, -1))
            True
        """
    def __reduce__(self):
        """
        Implement pickling.

        TESTS::

            sage: F.<a,b> = FreeGroup()
            sage: a.__reduce__()
            (Free Group on generators {a, b}, ((1,),))
            sage: (a*b*a^-1).__reduce__()
            (Free Group on generators {a, b}, ((1, 2, -1),))
        """
    @cached_method
    def Tietze(self):
        """
        Return the Tietze list of the element.

        The Tietze list of a word is a list of integers that represent
        the letters in the word.  A positive integer `i` represents
        the letter corresponding to the `i`-th generator of the group.
        Negative integers represent the inverses of generators.

        OUTPUT: tuple of integers

        EXAMPLES::

            sage: G.<a,b> = FreeGroup()
            sage: a.Tietze()
            (1,)
            sage: x = a^2 * b^(-3) * a^(-2)
            sage: x.Tietze()
            (1, 1, -2, -2, -2, -1, -1)

        TESTS::

            sage: type(a.Tietze())
            <... 'tuple'>
            sage: type(a.Tietze()[0])
            <class 'sage.rings.integer.Integer'>
        """
    def fox_derivative(self, gen, im_gens=None, ring=None):
        """
        Return the Fox derivative of ``self`` with respect to a given
        generator ``gen`` of the free group.

        Let `F` be a free group with free generators
        `x_1, x_2, \\ldots, x_n`. Let `j \\in \\left\\{ 1, 2, \\ldots ,
        n \\right\\}`. Let `a_1, a_2, \\ldots, a_n` be `n`
        invertible elements of a ring `A`. Let `a : F \\to A^\\times`
        be the (unique) homomorphism from `F` to the multiplicative
        group of invertible elements of `A` which sends each `x_i`
        to `a_i`. Then, we can define a map `\\partial_j : F \\to A`
        by the requirements that

        .. MATH::

            \\partial_j (x_i) = \\delta_{i, j}
            \\qquad \\qquad \\text{ for all indices } i \\text{ and } j

        and

        .. MATH::

            \\partial_j (uv) = \\partial_j(u) + a(u) \\partial_j(v)
            \\qquad \\qquad \\text{ for all } u, v \\in F .

        This map `\\partial_j` is called the `j`-th Fox derivative
        on `F` induced by `(a_1, a_2, \\ldots, a_n)`.

        The most well-known case is when `A` is the group ring
        `\\ZZ [F]` of `F` over `\\ZZ`, and when `a_i = x_i \\in A`.
        In this case, `\\partial_j` is simply called the `j`-th
        Fox derivative on `F`.

        INPUT:

        - ``gen`` -- the generator with respect to which the
          derivative will be computed. If this is `x_j`, then the
          method will return `\\partial_j`.

        - ``im_gens`` -- (optional) the images of the generators
          (given as a list or iterable). This is the list
          `(a_1, a_2, \\ldots, a_n)`.
          If not provided, it defaults to
          `(x_1, x_2, \\ldots, x_n)` in the group ring
          `\\ZZ [F]`.

        - ``ring`` -- (optional) the ring in which the elements
          of the list  `(a_1, a_2, \\ldots, a_n)` lie. If not
          provided, this ring is inferred from these elements.

        OUTPUT:

        The fox derivative of ``self`` with respect to ``gen``
        (induced by ``im_gens``).
        By default, it is an element of the group algebra with
        integer coefficients.
        If ``im_gens`` are provided, the result lives in the
        algebra where ``im_gens`` live.

        EXAMPLES::

            sage: G = FreeGroup(5)
            sage: G.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: (~x0*x1*x0*x2*~x0).fox_derivative(x0)
            -x0^-1 + x0^-1*x1 - x0^-1*x1*x0*x2*x0^-1
            sage: (~x0*x1*x0*x2*~x0).fox_derivative(x1)
            x0^-1
            sage: (~x0*x1*x0*x2*~x0).fox_derivative(x2)
            x0^-1*x1*x0
            sage: (~x0*x1*x0*x2*~x0).fox_derivative(x3)
            0

        If ``im_gens`` is given, the images of the generators are
        mapped to them::

            sage: F = FreeGroup(3)
            sage: a = F([2,1,3,-1,2])
            sage: a.fox_derivative(F([1]))
            x1 - x1*x0*x2*x0^-1
            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: a.fox_derivative(F([1]),[t,t,t])
            t - t^2
            sage: S.<t1,t2,t3> = LaurentPolynomialRing(ZZ)
            sage: a.fox_derivative(F([1]),[t1,t2,t3])
            -t2*t3 + t2
            sage: R.<x,y,z> = QQ[]
            sage: a.fox_derivative(F([1]),[x,y,z])
            -y*z + y
            sage: a.inverse().fox_derivative(F([1]),[x,y,z])
            (z - 1)/(y*z)

        The optional parameter ``ring`` determines the ring `A`::

            sage: u = a.fox_derivative(F([1]), [1,2,3], ring=QQ)
            sage: u
            -4
            sage: parent(u)
            Rational Field
            sage: u = a.fox_derivative(F([1]), [1,2,3], ring=R)
            sage: u
            -4
            sage: parent(u)
            Multivariate Polynomial Ring in x, y, z over Rational Field

        TESTS::

            sage: F = FreeGroup(3)
            sage: a = F([])
            sage: a.fox_derivative(F([1]))
            0
            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: a.fox_derivative(F([1]),[t,t,t])
            0
        """
    @cached_method
    def syllables(self):
        """
        Return the syllables of the word.

        Consider a free group element `g = x_1^{n_1} x_2^{n_2} \\cdots
        x_k^{n_k}`. The uniquely-determined subwords `x_i^{e_i}`
        consisting only of powers of a single generator are called the
        syllables of `g`.

        OUTPUT:

        The tuple of syllables. Each syllable is given as a pair
        `(x_i, e_i)` consisting of a generator and a nonzero integer.

        EXAMPLES::

            sage: G.<a,b> = FreeGroup()
            sage: w = a^2 * b^-1 * a^3
            sage: w.syllables()
            ((a, 2), (b, -1), (a, 3))
        """
    def __call__(self, *values):
        """
        Replace the generators of the free group by corresponding
        elements of the iterable ``values`` in the group element
        ``self``.

        INPUT:

        - ``*values`` -- a sequence of values, or a
          list/tuple/iterable of the same length as the number of
          generators of the free group

        OUTPUT: the product of ``values`` in the order and with exponents
        specified by ``self``

        EXAMPLES::

            sage: G.<a,b> = FreeGroup()
            sage: w = a^2 * b^-1 * a^3
            sage: w(1, 2)
            1/2
            sage: w(2, 1)
            32
            sage: w.subs(b=1, a=2)   # indirect doctest
            32

        TESTS::

            sage: w([1, 2])
            1/2
            sage: w((1, 2))
            1/2
            sage: w(i+1 for i in range(2))
            1/2

        Check that :issue:`25017` is fixed::

            sage: F = FreeGroup(2)
            sage: x0, x1 = F.gens()
            sage: u = F(1)
            sage: parent(u.subs({x1:x0})) is F
            True

            sage: F = FreeGroup(2)
            sage: x0, x1 = F.gens()
            sage: u = x0*x1
            sage: u.subs({x0:3, x1:2})
            6
            sage: u.subs({x0:1r, x1:2r})
            2
            sage: M0 = matrix(ZZ,2,[1,1,0,1])
            sage: M1 = matrix(ZZ,2,[1,0,1,1])
            sage: u.subs({x0: M0, x1: M1})
            [2 1]
            [1 1]

        TESTS::

            sage: F.<x,y> = FreeGroup()
            sage: F.one().subs(x=x, y=1)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents: 'Free Group on generators {x, y}' and 'Integer Ring'
        """

def FreeGroup(n=None, names: str = 'x', index_set=None, abelian: bool = False, **kwds):
    """
    Construct a Free Group.

    INPUT:

    - ``n`` -- integer (default: ``None``); the number of
      generators (if not specified the ``names`` are counted)

    - ``names`` -- string or list/tuple/iterable of strings (default:
      ``'x'``); the generator names or name prefix

    - ``index_set`` -- (optional) an index set for the generators; if
      specified then the optional keyword ``abelian`` can be used

    - ``abelian`` -- boolean (default: ``False``); whether to construct a free
      abelian group or a free group

    .. NOTE::

        If you want to create a free group, it is currently preferential to
        use ``Groups().free(...)`` as that does not load GAP.

    EXAMPLES::

        sage: G.<a,b> = FreeGroup();  G
        Free Group on generators {a, b}
        sage: H = FreeGroup('a, b')
        sage: G is H
        True
        sage: FreeGroup(0)
        Free Group on generators {}

    The entry can be either a string with the names of the generators,
    or the number of generators and the prefix of the names to be
    given. The default prefix is ``'x'`` ::

        sage: FreeGroup(3)
        Free Group on generators {x0, x1, x2}
        sage: FreeGroup(3, 'g')
        Free Group on generators {g0, g1, g2}
        sage: FreeGroup()
        Free Group on generators {x}

    We give two examples using the ``index_set`` option::

        sage: FreeGroup(index_set=ZZ)                                                   # needs sage.combinat
        Free group indexed by Integer Ring
        sage: FreeGroup(index_set=ZZ, abelian=True)                                     # needs sage.combinat
        Free abelian group indexed by Integer Ring

    TESTS::

        sage: G1 = FreeGroup(2, 'a,b')
        sage: G2 = FreeGroup('a,b')
        sage: G3.<a,b> = FreeGroup()
        sage: G1 is G2, G2 is G3
        (True, True)
    """

class FreeGroup_class(CachedRepresentation, Group, ParentLibGAP):
    """
    A class that wraps GAP's FreeGroup.

    See :func:`FreeGroup` for details.

    TESTS::

        sage: G = FreeGroup('a, b')
        sage: TestSuite(G).run()
        sage: G.category()
        Category of infinite groups
    """
    Element = FreeGroupElement
    def __init__(self, generator_names, gap_group=None) -> None:
        """
        Python constructor.

        INPUT:

        - ``generator_names`` -- tuple of strings; the names of the
          generators

        - ``libgap_free_group`` -- a LibGAP free group (default: ``None``);
          the LibGAP free group to wrap (if ``None``, a suitable group will be
          constructed)

        TESTS::

            sage: G.<a,b> = FreeGroup() # indirect doctest
            sage: G
            Free Group on generators {a, b}
            sage: G.variable_names()
            ('a', 'b')
        """
    def __hash__(self):
        """
        Make hashable.

        EXAMPLES::

            sage: F = FreeGroup(3)
            sage: F.__hash__() == hash(F._gen_names)
            True
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison of ``self`` and ``other``.

        EXAMPLES::

            sage: G1 = FreeGroup('a, b')
            sage: gg = libgap.FreeGroup('x', 'y')
            sage: G2 = FreeGroup('a, b', gap_group=gg)
            sage: G1 == G2
            True
            sage: G1 is G2
            False
            sage: G3 = FreeGroup('x, y')
            sage: G1 == G3
            False
            sage: G2 == G3
            False
        """
    def rank(self):
        """
        Return the number of generators of ``self``.

        Alias for :meth:`ngens`.

        OUTPUT: integer

        EXAMPLES::

            sage: G = FreeGroup('a, b');  G
            Free Group on generators {a, b}
            sage: G.rank()
            2
            sage: H = FreeGroup(3, 'x')
            sage: H
            Free Group on generators {x0, x1, x2}
            sage: H.rank()
            3
        """
    def abelian_invariants(self):
        """
        Return the Abelian invariants of ``self``.

        The Abelian invariants are given by a list of integers
        `i_1 \\dots i_j`, such that the abelianization of the
        group is isomorphic to

        .. MATH::

            \\ZZ / (i_1) \\times \\dots \\times \\ZZ / (i_j)

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: F.abelian_invariants()
            (0, 0)
        """
    def quotient(self, relations, **kwds):
        """
        Return the quotient of ``self`` by the normal subgroup generated
        by the given elements.

        This quotient is a finitely presented groups with the same
        generators as ``self``, and relations given by the elements of
        ``relations``.

        INPUT:

        - ``relations`` -- list/tuple/iterable with the elements of
          the free group
        - further named arguments, that are passed to the constructor
          of a finitely presented group

        OUTPUT:

        A finitely presented group, with generators corresponding to
        the generators of the free group, and relations corresponding
        to the elements in ``relations``.

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: F.quotient([a*b^2*a, b^3])
            Finitely presented group < a, b | a*b^2*a, b^3 >

        Division is shorthand for :meth:`quotient` ::

            sage: F /  [a*b^2*a, b^3]
            Finitely presented group < a, b | a*b^2*a, b^3 >

        Relations are converted to the free group, even if they are not
        elements of it (if possible) ::

            sage: F1.<a,b,c,d> = FreeGroup()
            sage: F2.<a,b> = FreeGroup()
            sage: r = a*b/a
            sage: r.parent()
            Free Group on generators {a, b}
            sage: F1/[r]
            Finitely presented group < a, b, c, d | a*b*a^-1 >
        """
    __truediv__ = quotient
