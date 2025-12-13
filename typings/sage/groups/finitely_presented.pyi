from sage.categories.morphism import SetMorphism as SetMorphism
from sage.groups.free_group import FreeGroup as FreeGroup, FreeGroupElement as FreeGroupElement
from sage.groups.generic import structure_description as structure_description
from sage.groups.group import Group as Group
from sage.groups.libgap_mixin import GroupMixinLibGAP as GroupMixinLibGAP
from sage.groups.libgap_wrapper import ElementLibGAP as ElementLibGAP, ParentLibGAP as ParentLibGAP
from sage.libs.gap.element import GapElement as GapElement
from sage.libs.gap.libgap import libgap as libgap
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation

class GroupMorphismWithGensImages(SetMorphism):
    """
    Class used for morphisms from finitely presented groups to
    other groups. It just adds the images of the generators at the
    end of the representation.

    EXAMPLES::

        sage: F = FreeGroup(3)
        sage: G = F / [F([1, 2, 3, 1, 2, 3]), F([1, 1, 1])]
        sage: H = AlternatingGroup(3)
        sage: HS = G.Hom(H)
        sage: from sage.groups.finitely_presented import GroupMorphismWithGensImages
        sage: GroupMorphismWithGensImages(HS, lambda a: H.one())
        Generic morphism:
        From: Finitely presented group < x0, x1, x2 | (x0*x1*x2)^2, x0^3 >
        To:   Alternating group of order 3!/2 as a permutation group
        Defn: x0 |--> ()
              x1 |--> ()
              x2 |--> ()
    """

class FinitelyPresentedGroupElement(FreeGroupElement):
    """
    A wrapper of GAP's Finitely Presented Group elements.

    The elements are created by passing the Tietze list that determines them.

    EXAMPLES::

        sage: G = FreeGroup('a, b')
        sage: H = G / [G([1]), G([2, 2, 2])]
        sage: H([1, 2, 1, -1])
        a*b
        sage: H([1, 2, 1, -2])
        a*b*a*b^-1
        sage: x = H([1, 2, -1, -2])
        sage: x
        a*b*a^-1*b^-1
        sage: y = H([2, 2, 2, 1, -2, -2, -2])
        sage: y
        b^3*a*b^-3
        sage: x*y
        a*b*a^-1*b^2*a*b^-3
        sage: x^(-1)
        b*a*b^-1*a^-1
    """
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        The Python constructor.

        See :class:`FinitelyPresentedGroupElement` for details.

        TESTS::

            sage: G = FreeGroup('a, b')
            sage: H = G / [G([1]), G([2, 2, 2])]
            sage: H([1, 2, 1, -1])
            a*b

            sage: TestSuite(G).run()
            sage: TestSuite(H).run()
            sage: G.<a,b> = FreeGroup()
            sage: H = G / (G([1]), G([2, 2, 2]))
            sage: x = H([1, 2, -1, -2])
            sage: TestSuite(x).run()
            sage: TestSuite(G.one()).run()
        """
    def __reduce__(self):
        """
        Used in pickling.

        TESTS::

            sage: F.<a,b> = FreeGroup()
            sage: G = F / [a*b, a^2]
            sage: G.inject_variables()
            Defining a, b
            sage: a.__reduce__()
            (Finitely presented group < a, b | a*b, a^2 >, ((1,),))
            sage: (a*b*a^-1).__reduce__()
            (Finitely presented group < a, b | a*b, a^2 >, ((1, 2, -1),))

            sage: F.<a,b,c> = FreeGroup('a, b, c')
            sage: G = F.quotient([a*b*c/(b*c*a), a*b*c/(c*a*b)])
            sage: G.inject_variables()
            Defining a, b, c
            sage: x = a*b*c
            sage: x.__reduce__()
            (Finitely presented group < a, b, c | a*b*c*a^-1*c^-1*b^-1, a*b*c*b^-1*a^-1*c^-1 >,
             ((1, 2, 3),))
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

            sage: G = FreeGroup('a, b')
            sage: H = G / (G([1]), G([2, 2, 2]))
            sage: H.inject_variables()
            Defining a, b
            sage: a.Tietze()
            (1,)
            sage: x = a^2*b^(-3)*a^(-2)
            sage: x.Tietze()
            (1, 1, -2, -2, -2, -1, -1)
        """
    def __call__(self, *values, **kwds):
        """
        Replace the generators of the free group with ``values``.

        INPUT:

        - ``*values`` -- list/tuple/iterable of the same length as
          the number of generators

        - ``check=True`` -- boolean keyword (default: ``True``); whether to
          verify that ``values`` satisfy the relations in the finitely
          presented group

        OUTPUT: the product of ``values`` in the order and with exponents
        specified by ``self``

        EXAMPLES::

            sage: G.<a,b> = FreeGroup()
            sage: H = G / [a/b];  H
            Finitely presented group < a, b | a*b^-1 >
            sage: H.simplified()
            Finitely presented group < a |  >

        The generator `b` can be eliminated using the relation `a=b`. Any
        values that you plug into a word must satisfy this relation::

            sage: A, B = H.gens()
            sage: w = A^2 * B
            sage: w(2,2)
            8
            sage: w(3,3)
            27
            sage: w(1,2)
            Traceback (most recent call last):
            ...
            ValueError: the values do not satisfy all relations of the group
            sage: w(1, 2, check=False)    # result depends on presentation of the group element
            2
        """

class RewritingSystem:
    """
    A class that wraps GAP's rewriting systems.

    A rewriting system is a set of rules that allow to transform
    one word in the group to an equivalent one.

    If the rewriting system is confluent, then the transformed
    word is a unique reduced form of the element of the group.

    .. WARNING::

        Note that the process of making a rewriting system confluent
        might not end.

    INPUT:

    - ``G`` -- a group

    REFERENCES:

    - :wikipedia:`Knuth-Bendix_completion_algorithm`

    EXAMPLES::

        sage: F.<a,b> = FreeGroup()
        sage: G = F / [a*b/a/b]
        sage: k = G.rewriting_system()
        sage: k
        Rewriting system of Finitely presented group < a, b | a*b*a^-1*b^-1 >
        with rules:
            a*b*a^-1*b^-1    --->    1

        sage: k.reduce(a*b*a*b)
        (a*b)^2
        sage: k.make_confluent()
        sage: k
        Rewriting system of Finitely presented group < a, b | a*b*a^-1*b^-1 >
        with rules:
            b^-1*a^-1    --->    a^-1*b^-1
            b^-1*a    --->    a*b^-1
            b*a^-1    --->    a^-1*b
            b*a    --->    a*b

        sage: k.reduce(a*b*a*b)
        a^2*b^2

    .. TODO::

        - Include support for different orderings (currently only shortlex
          is used).

        - Include the GAP package kbmag for more functionalities, including
          automatic structures and faster compiled functions.

    AUTHORS:

    - Miguel Angel Marco Buzunariz (2013-12-16)
    """
    def __init__(self, G) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: F.<a,b,c> = FreeGroup()
            sage: G = F / [a^2, b^3, c^5]
            sage: k = G.rewriting_system()
            sage: k
            Rewriting system of Finitely presented group < a, b, c | a^2, b^3, c^5 >
            with rules:
                a^2    --->    1
                b^3    --->    1
                c^5    --->    1
        """
    def free_group(self):
        """
        The free group after which the rewriting system is defined.

        EXAMPLES::

            sage: F = FreeGroup(3)
            sage: G = F / [ [1,2,3], [-1,-2,-3] ]
            sage: k = G.rewriting_system()
            sage: k.free_group()
            Free Group on generators {x0, x1, x2}
        """
    def finitely_presented_group(self):
        """
        The finitely presented group where the rewriting system is defined.

        EXAMPLES::

            sage: F = FreeGroup(3)
            sage: G = F / [ [1,2,3], [-1,-2,-3], [1,1], [2,2] ]
            sage: k = G.rewriting_system()
            sage: k.make_confluent()
            sage: k
            Rewriting system of Finitely presented group < x0, x1, x2 | x0*x1*x2, x0^-1*x1^-1*x2^-1, x0^2, x1^2 >
            with rules:
                x0^-1    --->    x0
                x1^-1    --->    x1
                x2^-1    --->    x2
                x0^2    --->    1
                x0*x1    --->    x2
                x0*x2    --->    x1
                x1*x0    --->    x2
                x1^2    --->    1
                x1*x2    --->    x0
                x2*x0    --->    x1
                x2*x1    --->    x0
                x2^2    --->    1
            sage: k.finitely_presented_group()
            Finitely presented group < x0, x1, x2 | x0*x1*x2, x0^-1*x1^-1*x2^-1, x0^2, x1^2 >
        """
    def reduce(self, element):
        """
        Apply the rules in the rewriting system to the element, to obtain
        a reduced form.

        If the rewriting system is confluent, this reduced form is unique
        for all words representing the same element.

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: G = F/[a^2, b^3, (a*b/a)^3, b*a*b*a]
            sage: k = G.rewriting_system()
            sage: k.reduce(b^4)
            b
            sage: k.reduce(a*b*a)
            a*b*a
        """
    def gap(self):
        """
        The gap representation of the rewriting system.

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: G = F/[a*a,b*b]
            sage: k = G.rewriting_system()
            sage: k.gap()
            Knuth Bendix Rewriting System for Monoid( [ a, A, b, B ] ) with rules
            [ [ a*A, <identity ...> ], [ A*a, <identity ...> ],
              [ b*B, <identity ...> ], [ B*b, <identity ...> ],
              [ a^2, <identity ...> ], [ b^2, <identity ...> ] ]
        """
    def rules(self):
        """
        Return the rules that form the rewriting system.

        OUTPUT:

        A dictionary containing the rules of the rewriting system.
        Each key is a word in the free group, and its corresponding
        value is the word to which it is reduced.

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: G = F / [a*a*a,b*b*a*a]
            sage: k = G.rewriting_system()
            sage: k
            Rewriting system of Finitely presented group < a, b | a^3, b^2*a^2 >
            with rules:
                a^3    --->    1
                b^2*a^2    --->    1

            sage: k.rules()
            {a^3: 1, b^2*a^2: 1}
            sage: k.make_confluent()
            sage: sorted(k.rules().items())
            [(a^-2, a), (a^-1*b^-1, a*b), (a^-1*b, b^-1), (a^2, a^-1),
             (a*b^-1, b), (b^-1*a^-1, a*b), (b^-1*a, b), (b^-2, a^-1),
             (b*a^-1, b^-1), (b*a, a*b), (b^2, a)]
        """
    def is_confluent(self):
        """
        Return ``True`` if the system is confluent and ``False`` otherwise.

        EXAMPLES::

            sage: F = FreeGroup(3)
            sage: G = F / [F([1,2,1,2,1,3,-1]),F([2,2,2,1,1,2]),F([1,2,3])]
            sage: k = G.rewriting_system()
            sage: k.is_confluent()
            False
            sage: k
            Rewriting system of Finitely presented group < x0, x1, x2 | (x0*x1)^2*x0*x2*x0^-1, x1^3*x0^2*x1, x0*x1*x2 >
            with rules:
                x0*x1*x2    --->    1
                x1^3*x0^2*x1    --->    1
                (x0*x1)^2*x0*x2*x0^-1    --->    1

            sage: k.make_confluent()
            sage: k.is_confluent()
            True
            sage: k
            Rewriting system of Finitely presented group < x0, x1, x2 | (x0*x1)^2*x0*x2*x0^-1, x1^3*x0^2*x1, x0*x1*x2 >
            with rules:
                x0^-1    --->    x0
                x1^-1    --->    x1
                x0^2    --->    1
                x0*x1    --->    x2^-1
                x0*x2^-1    --->    x1
                x1*x0    --->    x2
                x1^2    --->    1
                x1*x2^-1    --->    x0*x2
                x1*x2    --->    x0
                x2^-1*x0    --->    x0*x2
                x2^-1*x1    --->    x0
                x2^-2    --->    x2
                x2*x0    --->    x1
                x2*x1    --->    x0*x2
                x2^2    --->    x2^-1
        """
    def make_confluent(self) -> None:
        """
        Apply the Knuth-Bendix algorithm to try to transform the rewriting
        system into a confluent one.

        Note that this method does not return any object, just changes the
        rewriting system internally.

        .. WARNING::

            This algorithm is not granted to finish. Although it may be useful
            in some occasions to run it, interrupt it manually after some time
            and use then the transformed rewriting system. Even if it is not
            confluent, it could be used to reduce some words.

        ALGORITHM:

        Uses GAP's ``MakeConfluent``.

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: G = F / [a^2,b^3,(a*b/a)^3,b*a*b*a]
            sage: k = G.rewriting_system()
            sage: k
            Rewriting system of Finitely presented group < a, b | a^2, b^3, a*b^3*a^-1, (b*a)^2 >
            with rules:
                a^2    --->    1
                b^3    --->    1
                (b*a)^2    --->    1
                a*b^3*a^-1    --->    1

            sage: k.make_confluent()
            sage: k
            Rewriting system of Finitely presented group < a, b | a^2, b^3, a*b^3*a^-1, (b*a)^2 >
            with rules:
                a^-1    --->    a
                a^2    --->    1
                b^-1*a    --->    a*b
                b^-2    --->    b
                b*a    --->    a*b^-1
                b^2    --->    b^-1
        """

class FinitelyPresentedGroup(GroupMixinLibGAP, CachedRepresentation, Group, ParentLibGAP):
    """
    A class that wraps GAP's Finitely Presented Groups.

    .. WARNING::

        You should use
        :meth:`~sage.groups.free_group.FreeGroup_class.quotient` to
        construct finitely presented groups as quotients of free
        groups. Any class inheriting this one should define
        ``__reduce__ = CachedRepresentation.__reduce__``
        after importing ``CachedRepresentation``.

    EXAMPLES::

        sage: G.<a,b> = FreeGroup()
        sage: H = G / [a, b^3]
        sage: H
        Finitely presented group < a, b | a, b^3 >
        sage: H.gens()
        (a, b)

        sage: F.<a,b> = FreeGroup('a, b')
        sage: J = F / (F([1]), F([2, 2, 2]))
        sage: J is H
        True

        sage: G = FreeGroup(2)
        sage: H = G / (G([1, 1]), G([2, 2, 2]))
        sage: H.gens()
        (x0, x1)
        sage: H.gen(0)
        x0
        sage: H.ngens()
        2
        sage: H.gap()
        <fp group on the generators [ x0, x1 ]>
        sage: type(_)
        <class 'sage.libs.gap.element.GapElement'>
    """
    Element = FinitelyPresentedGroupElement
    def __init__(self, free_group, relations, category=None, libgap_fpgroup=None) -> None:
        """
        The Python constructor.

        TESTS::

            sage: G = FreeGroup('a, b')
            sage: H = G / (G([1]), G([2])^3)
            sage: H
            Finitely presented group < a, b | a, b^3 >

            sage: F = FreeGroup('a, b')
            sage: J = F / (F([1]), F([2, 2, 2]))
            sage: J is H
            True

            sage: A5 = libgap(AlternatingGroup(5))
            sage: A5gapfp = A5.IsomorphismFpGroup().Range()
            sage: A5gapfp
            <fp group of size 60 on the generators [ A_5.1, A_5.2 ]>
            sage: A5sage = A5gapfp.sage(); A5sage;
            Finitely presented group < A_5.1, A_5.2 | A_5.1^5*A_5.2^-5, A_5.1^5*(A_5.2^-1*A_5.1^-1)^2, (A_5.1^-2*A_5.2^2)^2 >
            sage: A5sage.inject_variables()
            Traceback (most recent call last):
            ...
            ValueError: variable names have not yet been set using self._assign_names(...)

        Check that pickling works::

            sage: G = FreeGroup(2) / [2 * (1, 2, -1, -2)]
            sage: loads(dumps(G))
            Finitely presented group < x0, x1 | (x0*x1*x0^-1*x1^-1)^2 >
            sage: G.__reduce__()[1][1]
            (Free Group on generators {x0, x1}, ((x0*x1*x0^-1*x1^-1)^2,))

            sage: TestSuite(H).run()
            sage: TestSuite(J).run()
        """
    def __hash__(self):
        """
        Make hashable.

        EXAMPLES::

            sage: G = FreeGroup(2) / [(1, 2, 2, 1)]
            sage: G.__hash__() == hash((G.free_group(), G.relations()))
            True
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison of ``self`` and ``other``.

        EXAMPLES::

            sage: G1 = FreeGroup(2) / [(1, 2, 2, 1, 2, 1)]
            sage: G2 = libgap(G1).sage()
            sage: G1 == G2
            True
            sage: G1 is G2
            False
        """
    def free_group(self):
        """
        Return the free group (without relations).

        OUTPUT: a :func:`~sage.groups.free_group.FreeGroup`

        EXAMPLES::

            sage: G.<a,b,c> = FreeGroup()
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.free_group()
            Free Group on generators {a, b, c}
            sage: H.free_group() is G
            True
        """
    def relations(self):
        """
        Return the relations of the group.

        OUTPUT: the relations as a tuple of elements of :meth:`free_group`

        EXAMPLES::

            sage: F = FreeGroup(5, 'x')
            sage: F.inject_variables()
            Defining x0, x1, x2, x3, x4
            sage: G = F.quotient([x0*x2, x3*x1*x3, x2*x1*x2])
            sage: G.relations()
            (x0*x2, x3*x1*x3, x2*x1*x2)
            sage: all(rel in F for rel in G.relations())
            True
        """
    @cached_method
    def cardinality(self, limit: int = 4096000):
        """
        Compute the cardinality of ``self``.

        INPUT:

        - ``limit`` -- integer (default: 4096000); the maximal number
          of cosets before the computation is aborted

        OUTPUT: integer or ``Infinity``; the number of elements in the group

        EXAMPLES::

            sage: G.<a,b> = FreeGroup('a, b')
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.cardinality()
            6

            sage: F.<a,b,c> = FreeGroup()
            sage: J = F / (F([1]), F([2, 2, 2]))
            sage: J.cardinality()
            +Infinity

        ALGORITHM:

            Uses GAP.

        .. WARNING::

            This is in general not a decidable problem, so it is not
            guaranteed to give an answer. If the group is infinite, or
            too big, you should be prepared for a long computation
            that consumes all the memory without finishing if you do
            not set a sensible ``limit``.
        """
    order = cardinality
    def as_permutation_group(self, limit: int = 4096000):
        """
        Return an isomorphic permutation group.

        The generators of the resulting group correspond to the images
        by the isomorphism of the generators of the given group.

        INPUT:

        - ``limit`` -- integer (default: 4096000); the maximal number
          of cosets before the computation is aborted

        OUTPUT:

        A Sage
        :func:`~sage.groups.perm_gps.permgroup.PermutationGroup`. If
        the number of cosets exceeds the given ``limit``, a
        :exc:`ValueError` is returned.

        EXAMPLES::

            sage: G.<a,b> = FreeGroup()
            sage: H = G / (a^2, b^3, a*b*~a*~b)
            sage: H.as_permutation_group()
            Permutation Group with generators [(1,2)(3,5)(4,6), (1,3,4)(2,5,6)]

            sage: G.<a,b> = FreeGroup()
            sage: H = G / [a^3*b]
            sage: H.as_permutation_group(limit=1000)
            Traceback (most recent call last):
            ...
            ValueError: Coset enumeration exceeded limit, is the group finite?

        ALGORITHM:

        Uses GAP's coset enumeration on the trivial subgroup.

        .. WARNING::

            This is in general not a decidable problem (in fact, it is
            not even possible to check if the group is finite or
            not). If the group is infinite, or too big, you should be
            prepared for a long computation that consumes all the
            memory without finishing if you do not set a sensible
            ``limit``.
        """
    def direct_product(self, H, reduced: bool = False, new_names: bool = True):
        '''
        Return the direct product of ``self`` with finitely presented
        group ``H``.

        Calls GAP function ``DirectProduct``, which returns the direct
        product of a list of groups of any representation.

        From [Joh1990]_ (p. 45, proposition 4): If `G`, `H` are groups
        presented by `\\langle X \\mid R \\rangle` and `\\langle Y \\mid S \\rangle`
        respectively, then their direct product has the presentation
        `\\langle X, Y \\mid R, S, [X, Y] \\rangle` where `[X, Y]` denotes the
        set of commutators `\\{ x^{-1} y^{-1} x y \\mid x \\in X, y \\in Y \\}`.

        INPUT:

        - ``H`` -- a finitely presented group

        - ``reduced`` -- boolean (default: ``False``); if ``True``, then
          attempt to reduce the presentation of the product group

        - ``new_names`` -- boolean (default: ``True``); if ``True``, then
          lexicographical variable names are assigned to the generators of
          the group to be returned. If ``False``, the group to be returned
          keeps the generator names of the two groups forming the direct
          product. Note that one cannot ask to reduce the output and ask
          to keep the old variable names, as they may change meaning
          in the output group if its presentation is reduced.

        OUTPUT: the direct product of ``self`` with ``H`` as a finitely
        presented group

        EXAMPLES::

            sage: G = FreeGroup()
            sage: C12 =  ( G / [G([1,1,1,1])] ).direct_product( G / [G([1,1,1])]); C12
            Finitely presented group < a, b | a^4, b^3, a^-1*b^-1*a*b >
            sage: C12.order(), C12.as_permutation_group().is_cyclic()
            (12, True)
            sage: klein = ( G / [G([1,1])] ).direct_product( G / [G([1,1])]); klein
            Finitely presented group < a, b | a^2, b^2, a^-1*b^-1*a*b >
            sage: klein.order(), klein.as_permutation_group().is_cyclic()
            (4, False)

        We can keep the variable names from ``self`` and ``H`` to examine how
        new relations are formed::

            sage: F = FreeGroup("a"); G = FreeGroup("g")
            sage: X = G / [G.0^12]; A = F / [F.0^6]
            sage: X.direct_product(A, new_names=False)
            Finitely presented group < g, a | g^12, a^6, g^-1*a^-1*g*a >
            sage: A.direct_product(X, new_names=False)
            Finitely presented group < a, g | a^6, g^12, a^-1*g^-1*a*g >

        Or we can attempt to reduce the output group presentation::

            sage: F = FreeGroup("a"); G = FreeGroup("g")
            sage: X = G / [G.0]; A = F / [F.0]
            sage: X.direct_product(A, new_names=True)
            Finitely presented group < a, b | a, b, a^-1*b^-1*a*b >
            sage: X.direct_product(A, reduced=True, new_names=True)
            Finitely presented group <  |  >

        But we cannot do both::

            sage: K = FreeGroup([\'a\',\'b\'])
            sage: D = K / [K.0^5, K.1^8]
            sage: D.direct_product(D, reduced=True, new_names=False)
            Traceback (most recent call last):
            ...
            ValueError: cannot reduce output and keep old variable names

        TESTS::

            sage: G = FreeGroup()
            sage: Dp = (G / [G([1,1])]).direct_product( G / [G([1,1,1,1,1,1])] )
            sage: Dp.as_permutation_group().is_isomorphic(PermutationGroup([\'(1,2)\',\'(3,4,5,6,7,8)\']))
            True
            sage: C7 = G / [G.0**7]; C6 =  G / [G.0**6]
            sage: C14 = G / [G.0**14]; C3 =  G / [G.0**3]
            sage: C7.direct_product(C6).is_isomorphic(C14.direct_product(C3))
            True
            sage: F = FreeGroup(2); D = F / [F([1,1,1,1,1]),F([2,2]),F([1,2])**2]
            sage: D.direct_product(D).as_permutation_group().is_isomorphic(
            ....: direct_product_permgroups([DihedralGroup(5),DihedralGroup(5)]))
            True

        AUTHORS:

        - Davis Shurbert (2013-07-20): initial version
        '''
    def semidirect_product(self, H, hom, check: bool = True, reduced: bool = False):
        """
        The semidirect product of ``self`` with ``H`` via ``hom``.

        If there exists a homomorphism `\\phi` from a group `G` to the
        automorphism group of a group `H`, then we can define the semidirect
        product of `G` with `H` via `\\phi` as the Cartesian product of `G`
        and `H` with the operation

        .. MATH::

                (g_1, h_1)(g_2, h_2) = (g_1 g_2, \\phi(g_2)(h_1) h_2).

        INPUT:

        - ``H`` -- finitely presented group which is implicitly acted on
          by ``self`` and can be naturally embedded as a normal subgroup
          of the semidirect product

        - ``hom`` -- homomorphism from ``self`` to the automorphism group
          of ``H``. Given as a pair, with generators of ``self`` in the
          first slot and the images of the corresponding generators in the
          second. These images must be automorphisms of ``H``, given again
          as a pair of generators and images.

        - ``check`` -- boolean (default: ``True``); if ``False`` the defining
          homomorphism and automorphism images are not tested for validity.
          This test can be costly with large groups, so it can be bypassed
          if the user is confident that his morphisms are valid.

        - ``reduced`` -- boolean (default: ``False``); if ``True`` then the
          method attempts to reduce the presentation of the output group

        OUTPUT:

        The semidirect product of ``self`` with ``H`` via ``hom`` as a
        finitely presented group. See
        :meth:`PermutationGroup_generic.semidirect_product
        <sage.groups.perm_gps.permgroup.PermutationGroup_generic.semidirect_product>`
        for a more in depth explanation of a semidirect product.

        AUTHORS:

        - Davis Shurbert (8-1-2013)

        EXAMPLES:

        Group of order 12 as two isomorphic semidirect products::

            sage: D4 = groups.presentation.Dihedral(4)
            sage: C3 = groups.presentation.Cyclic(3)
            sage: alpha1 = ([C3.gen(0)],[C3.gen(0)])
            sage: alpha2 = ([C3.gen(0)],[C3([1,1])])
            sage: S1 = D4.semidirect_product(C3, ([D4.gen(1), D4.gen(0)],[alpha1,alpha2]))
            sage: C2 = groups.presentation.Cyclic(2)
            sage: Q = groups.presentation.DiCyclic(3)
            sage: a = Q([1]); b = Q([-2])
            sage: alpha = (Q.gens(), [a,b])
            sage: S2 = C2.semidirect_product(Q, ([C2.0],[alpha]))
            sage: S1.is_isomorphic(S2)
            True

        Dihedral groups can be constructed as semidirect products
        of cyclic groups::

            sage: C2 = groups.presentation.Cyclic(2)
            sage: C8 = groups.presentation.Cyclic(8)
            sage: hom = (C2.gens(), [ ([C8([1])], [C8([-1])]) ])
            sage: D = C2.semidirect_product(C8, hom)
            sage: D.as_permutation_group().is_isomorphic(DihedralGroup(8))
            True

        You can attempt to reduce the presentation of the output group::

            sage: D = C2.semidirect_product(C8, hom); D
            Finitely presented group < a, b | a^2, b^8, a^-1*b*a*b >
            sage: D = C2.semidirect_product(C8, hom, reduced=True); D
            Finitely presented group < a, b | a^2, a*b*a*b, b^8 >

            sage: C3 = groups.presentation.Cyclic(3)
            sage: C4 = groups.presentation.Cyclic(4)
            sage: hom = (C3.gens(), [(C4.gens(), C4.gens())])
            sage: C3.semidirect_product(C4, hom)
            Finitely presented group < a, b | a^3, b^4, a^-1*b*a*b^-1 >
            sage: D = C3.semidirect_product(C4, hom, reduced=True); D
            Finitely presented group < a, b | a^3, b^4, a^-1*b*a*b^-1 >
            sage: D.as_permutation_group().is_cyclic()
            True

        You can turn off the checks for the validity of the input morphisms.
        This check is expensive but behavior is unpredictable if inputs are
        invalid and are not caught by these tests::

            sage: C5 = groups.presentation.Cyclic(5)
            sage: C12 = groups.presentation.Cyclic(12)
            sage: hom = (C5.gens(), [(C12.gens(), C12.gens())])
            sage: sp = C5.semidirect_product(C12, hom, check=False); sp
            Finitely presented group < a, b | a^5, b^12, a^-1*b*a*b^-1 >
            sage: sp.as_permutation_group().is_cyclic(), sp.order()
            (True, 60)

        TESTS:

        The following was fixed in Gap-4.7.2::

            sage: C5.semidirect_product(C12, hom) == sp
            True

        A more complicated semidirect product::

            sage: C = groups.presentation.Cyclic(7)
            sage: D = groups.presentation.Dihedral(5)
            sage: id1 = ([C.0], [(D.gens(),D.gens())])
            sage: Se1 =  C.semidirect_product(D, id1)
            sage: id2 = (D.gens(), [(C.gens(),C.gens()),(C.gens(),C.gens())])
            sage: Se2 =  D.semidirect_product(C ,id2)
            sage: Dp1 = C.direct_product(D)
            sage: Dp1.is_isomorphic(Se1), Dp1.is_isomorphic(Se2)
            (True, True)

        Most checks for validity of input are left to GAP to handle::

            sage: bad_aut = ([C.0], [(D.gens(),[D.0, D.0])])
            sage: C.semidirect_product(D, bad_aut)
            Traceback (most recent call last):
            ...
            ValueError: images of input homomorphism must be automorphisms
            sage: bad_hom = ([D.0, D.1], [(C.gens(),C.gens())])
            sage: D.semidirect_product(C, bad_hom)
            Traceback (most recent call last):
            ...
            GAPError: Error, <gens> and <imgs> must be lists of same length
        """
    @cached_method
    def abelian_invariants(self):
        """
        Return the abelian invariants of ``self``.

        The abelian invariants are given by a list of integers
        `(i_1, \\ldots, i_j)`, such that the abelianization of the group is
        isomorphic to `\\ZZ / (i_1) \\times \\cdots \\times \\ZZ / (i_j)`.

        EXAMPLES::

            sage: G = FreeGroup(4, 'g')
            sage: G.inject_variables()
            Defining g0, g1, g2, g3
            sage: H = G.quotient([g1^2, g2*g1*g2^(-1)*g1^(-1), g1*g3^(-2), g0^4])
            sage: H.abelian_invariants()
            (0, 4, 4)

        ALGORITHM:

        Uses GAP.
        """
    @cached_method
    def abelianization_map(self):
        """
        Return the abelianization map of ``self``.

        OUTPUT: the abelianization map of ``self`` as a homomorphism of
        finitely presented groups

        EXAMPLES::

            sage: G = FreeGroup(4, 'g')
            sage: G.inject_variables(verbose=False)
            sage: H = G.quotient([g1^2, g2*g1*g2^(-1)*g1^(-1), g1*g3^(-2), g0^4])
            sage: H.abelianization_map()
            Group morphism:
              From: Finitely presented group < g0, g1, g2, g3 | g1^2, g2*g1*g2^-1*g1^-1, g1*g3^-2, g0^4 >
              To:   Finitely presented group < f1, f2, f3 | f1^4, f2^-1*f1^-1*f2*f1, f2^4, f3^-1*f1^-1*f3*f1, f3^-1*f2^-1*f3*f2 >
            sage: g = FreeGroup(0) / []
            sage: g.abelianization_map()
            Group endomorphism of Finitely presented group  <  |  >
        """
    @cached_method
    def abelianization_to_algebra(self, ring=...):
        """
        Return the group algebra of the abelianization of ``self``
        together with the monomials representing the generators of ``self``.

        INPUT:

        - ``ring`` -- (default: ``QQ``) the base ring for
          the group algebra of ``self``

        OUTPUT:

        - ``ab`` -- the abelianization  of ``self`` as a finitely presented group
          with a minimal number `n` of generators
        - ``R`` -- a Laurent polynomial ring with `n` variables with base ring ``ring``
        - ``ideal`` -- list of generators of an ideal ``I`` in ``R`` such that ``R/I``
          is the group algebra of the abelianization over ``ring``
        - ``image`` -- list  with the images of the generators of ``self`` in ``R/I``

        EXAMPLES::

            sage: G = FreeGroup(4, 'g')
            sage: G.inject_variables()
            Defining g0, g1, g2, g3
            sage: H = G.quotient([g1^2, g2*g1*g2^(-1)*g1^(-1), g1*g3^(-2), g0^4])
            sage: H.abelianization_to_algebra()
            (Finitely presented group < f1, f2, f3 | f1^4, f2^-1*f1^-1*f2*f1, f2^4, f3^-1*f1^-1*f3*f1, f3^-1*f2^-1*f3*f2 >,
             Multivariate Laurent Polynomial Ring in f1, f2, f3 over Rational Field,
             [f1^4 - 1, f2^4 - 1],
             [f1^3*f2^2, f2^2, f3, f2])
            sage: g=FreeGroup(0) / []
            sage: g.abelianization_to_algebra()
            (Finitely presented group  <  |  >, Rational Field, [], [])
        """
    def simplification_isomorphism(self):
        """
        Return an isomorphism from ``self`` to a finitely presented group with
        a (hopefully) simpler presentation.

        EXAMPLES::

            sage: G.<a,b,c> = FreeGroup()
            sage: H = G / [a*b*c, a*b^2, c*b/c^2]
            sage: I = H.simplification_isomorphism()
            sage: I
            Group morphism:
              From: Finitely presented group < a, b, c | a*b*c, a*b^2, c*b*c^-2 >
              To:   Finitely presented group < b |  >
            sage: I(a)
            b^-2
            sage: I(b)
            b
            sage: I(c)
            b

        TESTS::

            sage: F = FreeGroup(1)
            sage: G = F.quotient([F.0])
            sage: h = G.simplification_isomorphism(); h
            Group morphism:
              From: Finitely presented group < x | x >
              To:   Finitely presented group <  |  >
            sage: h(G.gen(0))
            1

        ALGORITHM:

        Uses GAP.
        """
    def simplified(self):
        """
        Return an isomorphic group with a (hopefully) simpler presentation.

        OUTPUT:

        A new finitely presented group. Use
        :meth:`simplification_isomorphism` if you want to know the
        isomorphism.

        EXAMPLES::

            sage: G.<x,y> = FreeGroup()
            sage: H = G /  [x ^5, y ^4, y*x*y^3*x ^3]
            sage: H
            Finitely presented group < x, y | x^5, y^4, y*x*y^3*x^3 >
            sage: H.simplified()
            Finitely presented group < x, y | y^4, y*x*y^-1*x^-2, x^5 >

        A more complicate example::

            sage: G.<e0, e1, e2, e3, e4, e5, e6, e7, e8, e9> = FreeGroup()
            sage: rels = [e6, e5, e3, e9, e4*e7^-1*e6, e9*e7^-1*e0,
            ....:         e0*e1^-1*e2, e5*e1^-1*e8, e4*e3^-1*e8, e2]
            sage: H = G.quotient(rels);  H
            Finitely presented group < e0, e1, e2, e3, e4, e5, e6, e7, e8, e9 |
            e6, e5, e3, e9, e4*e7^-1*e6, e9*e7^-1*e0, e0*e1^-1*e2, e5*e1^-1*e8, e4*e3^-1*e8, e2 >
            sage: H.simplified()
            Finitely presented group < e0 | e0^2 >
        """
    def sorted_presentation(self):
        """
        Return the same presentation with the relations sorted to ensure
        equality.

        OUTPUT: a new finitely presented group with the relations sorted

        EXAMPLES::

            sage: G = FreeGroup(2) / [(1, 2, -1, -2), ()]; G
            Finitely presented group < x0, x1 | x0*x1*x0^-1*x1^-1, 1 >
            sage: G.sorted_presentation()
            Finitely presented group < x0, x1 | 1, x1^-1*x0^-1*x1*x0 >
        """
    def epimorphisms(self, H):
        '''
        Return the epimorphisms from ``self`` to `H`, up to automorphism of `H`.

        INPUT:

        - ``H`` -- another group

        EXAMPLES::

            sage: F = FreeGroup(3)
            sage: G = F / [F([1, 2, 3, 1, 2, 3]), F([1, 1, 1])]
            sage: H = AlternatingGroup(3)
            sage: for quo in G.epimorphisms(H):
            ....:   for a in G.gens():
            ....:       print(a, "|-->", quo(a))
            ....:   print("-----")
            x0 |--> ()
            x1 |--> (1,3,2)
            x2 |--> (1,2,3)
            -----
            x0 |--> (1,3,2)
            x1 |--> ()
            x2 |--> (1,2,3)
            -----
            x0 |--> (1,3,2)
            x1 |--> (1,2,3)
            x2 |--> ()
            -----
            x0 |--> (1,2,3)
            x1 |--> (1,2,3)
            x2 |--> (1,2,3)
            -----

        ALGORITHM:

        Uses libgap\'s GQuotients function.
        '''
    def alexander_matrix(self, im_gens=None):
        """
        Return the Alexander matrix of the group.

        This matrix is given by the fox derivatives of the relations
        with respect to the generators.

        - ``im_gens`` -- (optional) the images of the generators

        OUTPUT:

        A matrix with coefficients in the group algebra. If ``im_gens`` is
        given, the coefficients will live in the same algebra as the given
        values. The result depends on the (fixed) choice of presentation.

        EXAMPLES::

            sage: G.<a,b,c> = FreeGroup()
            sage: H = G.quotient([a*b/a/b, a*c/a/c, c*b/c/b])
            sage: H.alexander_matrix()
            [     1 - a*b*a^-1 a - a*b*a^-1*b^-1                 0]
            [     1 - a*c*a^-1                 0 a - a*c*a^-1*c^-1]
            [                0 c - c*b*c^-1*b^-1      1 - c*b*c^-1]

        If we introduce the images of the generators, we obtain the
        result in the corresponding algebra.

        ::

            sage: G.<a,b,c,d,e> = FreeGroup()
            sage: H = G.quotient([a*b/a/b, a*c/a/c, a*d/a/d, b*c*d/(c*d*b), b*c*d/(d*b*c)])
            sage: H.alexander_matrix()
            [              1 - a*b*a^-1          a - a*b*a^-1*b^-1                          0                          0                          0]
            [              1 - a*c*a^-1                          0          a - a*c*a^-1*c^-1                          0                          0]
            [              1 - a*d*a^-1                          0                          0          a - a*d*a^-1*d^-1                          0]
            [                         0             1 - b*c*d*b^-1   b - b*c*d*b^-1*d^-1*c^-1      b*c - b*c*d*b^-1*d^-1                          0]
            [                         0        1 - b*c*d*c^-1*b^-1             b - b*c*d*c^-1 b*c - b*c*d*c^-1*b^-1*d^-1                          0]
            sage: R.<t1,t2,t3,t4> = LaurentPolynomialRing(ZZ)
            sage: H.alexander_matrix([t1,t2,t3,t4])
            [    -t2 + 1      t1 - 1           0           0           0]
            [    -t3 + 1           0      t1 - 1           0           0]
            [    -t4 + 1           0           0      t1 - 1           0]
            [          0  -t3*t4 + 1      t2 - 1  t2*t3 - t3           0]
            [          0     -t4 + 1 -t2*t4 + t2   t2*t3 - 1           0]
        """
    @cached_method
    def abelian_alexander_matrix(self, ring=..., simplified: bool = True):
        """
        Return the Alexander matrix of the group with values in the group
        algebra of the abelianized.

        INPUT:

        - ``ring`` -- (default: ``QQ``) the base ring of the
          group algebra
        - ``simplified`` -- boolean (default: ``False``); if set to
          ``True`` use Gauss elimination and erase rows and columns

        OUTPUT:

        - ``A`` -- a matrix with coefficients in ``R``
        - ``ideal`` -- an list of generators of an ideal ``I`` of
          ``R = A.base_ring()`` such that ``R/I`` is the group algebra of the
          abelianization of ``self``

        EXAMPLES::

            sage: G.<a,b,c> = FreeGroup()
            sage: H = G.quotient([a*b/a/b, a*c/a/c, c*b/c/b])
            sage: A, ideal = H.abelian_alexander_matrix()
            sage: A
            [-f2 + 1  f1 - 1       0]
            [-f3 + 1       0  f1 - 1]
            [      0  f3 - 1 -f2 + 1]
            sage: A.base_ring()
            Multivariate Laurent Polynomial Ring in f1, f2, f3 over Rational Field
            sage: ideal
            []
            sage: G = FreeGroup(3)/[(2, 1, 1), (1, 2, 2, 3, 3)]
            sage: A, ideal = G.abelian_alexander_matrix(simplified=True); A
            [-f1^2 - f1^4 - f1^6         f1^3 + f1^6]
            sage: g = FreeGroup(1) / []
            sage: g.abelian_alexander_matrix()
            ([], [])
            sage: g.abelian_alexander_matrix()[0].base_ring()
            Univariate Laurent Polynomial Ring in f1 over Rational Field
            sage: g = FreeGroup(0) / []
            sage: A, ideal = g.abelian_alexander_matrix(); A
            []
            sage: A.base_ring()
            Rational Field
        """
    def characteristic_varieties(self, ring=..., matrix_ideal=None, groebner: bool = False):
        """
        Return the characteristic varieties of the group ``self``.

        There are several definitions of the characteristic varieties of a
        group `G`, see e.g. [CS1999a]_. Let `\\Lambda` be the group algebra of
        `G/G'` and `\\mathbb{T}` its associated algebraic variety (a torus).
        Each element `\\xi\\in\\mathbb{T}` defines a local system of coefficients
        and the `k`-th characteristic variety is

        .. MATH::

            V_k(G) = \\{\\xi\\in\\mathbb{T}\\mid \\dim H^1(G;\\xi)\\geq k\\}.

        These varieties are defined by ideals in `\\Lambda`.

        INPUT:

        - ``ring`` -- (default: ``QQ``) the base ring of the group algebra
        - ``groebner`` -- boolean (default: ``False``); if set to
          ``True`` the minimal associated primes of the ideals and their
          groebner bases are computed; ignored if the base ring
          is not a field

        OUTPUT:

        A dictionary with keys the indices of the varieties. If ``groebner`` is ``False``
        the values are the ideals defining the characteristic varieties.
        If it is ``True``, lists for Gröbner bases for the ideal of each irreducible
        component, stopping when the first time a characteristic variety is empty.

        EXAMPLES::

            sage: L = [2*(i, j) + 2* (-i, -j) for i, j in ((1, 2), (2, 3), (3, 1))]
            sage: G = FreeGroup(3) / L
            sage: G.characteristic_varieties(groebner=True)
            {0: [(0,)],
             1: [(f1 - 1, f2 - 1, f3 - 1), (f1*f3 + 1, f2 - 1), (f1*f2 + 1, f3 - 1), (f2*f3 + 1, f1 - 1),
                 (f2*f3 + 1, f1 - f2), (f2*f3 + 1, f1 - f3), (f1*f3 + 1, f2 - f3)],
             2: [(f1 - 1, f2 - 1, f3 - 1), (f1 + 1, f2 - 1, f3 - 1), (f1 - 1, f2 - 1, f3 + 1),
                 (f3^2 + 1, f1 - f3, f2 - f3), (f1 - 1, f2 + 1, f3 - 1)],
             3: [(f1 - 1, f2 - 1, f3 - 1)],
             4: []}
            sage: G = FreeGroup(2)/[2*(1,2,-1,-2)]
            sage: G.characteristic_varieties()
            {0: Ideal (0) of Multivariate Laurent Polynomial Ring in f1, f2 over Rational Field,
             1: Ideal (f2 - 1, f1 - 1) of Multivariate Laurent Polynomial Ring in f1, f2 over Rational Field,
             2: Ideal (f2 - 1, f1 - 1) of Multivariate Laurent Polynomial Ring in f1, f2 over Rational Field,
             3: Ideal (1) of Multivariate Laurent Polynomial Ring in f1, f2 over Rational Field}
            sage: G.characteristic_varieties(ring=ZZ)
            {0: Ideal (0) of Multivariate Laurent Polynomial Ring in f1, f2 over Integer Ring,
             1: Ideal (2*f2 - 2, 2*f1 - 2) of Multivariate Laurent Polynomial Ring in f1, f2 over Integer Ring,
             2: Ideal (f2 - 1, f1 - 1) of Multivariate Laurent Polynomial Ring in f1, f2 over Integer Ring,
             3: Ideal (1) of Multivariate Laurent Polynomial Ring in f1, f2 over Integer Ring}
            sage: G = FreeGroup(2)/[(1,2,1,-2,-1,-2)]
            sage: G.characteristic_varieties()
            {0: Ideal (0) of Univariate Laurent Polynomial Ring in f1 over Rational Field,
             1: Ideal (-1 + 2*f1 - 2*f1^2 + f1^3) of Univariate Laurent Polynomial Ring in f1 over Rational Field,
             2: Ideal (1) of Univariate Laurent Polynomial Ring in f1 over Rational Field}
            sage: G.characteristic_varieties(groebner=True)
            {0: [0], 1: [-1 + f1, 1 - f1 + f1^2], 2: []}
            sage: G = FreeGroup(2)/[3 * (1, ), 2 * (2, )]
            sage: G.characteristic_varieties(groebner=True)
            {0: [-1 + F1, 1 + F1, 1 - F1 + F1^2, 1 + F1 + F1^2], 1: [1 - F1 + F1^2],  2: []}
            sage: G = FreeGroup(2)/[2 * (2, )]
            sage: G.characteristic_varieties(groebner=True)
            {0: [(f1 + 1,), (f1 - 1,)], 1: [(f1 + 1,), (f1 - 1, f2 - 1)], 2: []}
            sage: G = (FreeGroup(0) / [])
            sage: G.characteristic_varieties()
            {0: Principal ideal (0) of Rational Field,
             1: Principal ideal (1) of Rational Field}
            sage: G.characteristic_varieties(groebner=True)
            {0: [(0,)], 1: [(1,)]}
        """
    def rewriting_system(self):
        """
        Return the rewriting system corresponding to the finitely presented
        group. This rewriting system can be used to reduce words with respect
        to the relations.

        If the rewriting system is transformed into a confluent one, the
        reduction process will give as a result the (unique) reduced form
        of an element.

        EXAMPLES::

            sage: F.<a,b> = FreeGroup()
            sage: G = F / [a^2,b^3,(a*b/a)^3,b*a*b*a]
            sage: k = G.rewriting_system()
            sage: k
            Rewriting system of Finitely presented group < a, b | a^2, b^3, a*b^3*a^-1, b*a*b*a >
            with rules:
                a^2    --->    1
                b^3    --->    1
                b*a*b*a    --->    1
                a*b^3*a^-1    --->    1

            sage: G([1,1,2,2,2])
            a^2*b^3
            sage: k.reduce(G([1,1,2,2,2]))
            1
            sage: k.reduce(G([2,2,1]))
            b^2*a
            sage: k.make_confluent()
            sage: k.reduce(G([2,2,1]))
            a*b
        """
