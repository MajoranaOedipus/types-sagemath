from _typeshed import Incomplete
from sage.categories.groups import Groups as Groups
from sage.categories.monoids import Monoids as Monoids
from sage.categories.semigroups import Semigroups as Semigroups
from sage.categories.sets_cat import Sets as Sets
from sage.cpython.getattr import raw_getattr as raw_getattr
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.sets.family import Family as Family
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AutomaticSemigroup(UniqueRepresentation, Parent):
    '''
    Semigroups defined by generators living in an ambient semigroup.

    This implementation lazily constructs all the elements of the
    semigroup, and the right Cayley graph relations between them, and
    uses the latter as an automaton.

    EXAMPLES::

        sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
        sage: R = IntegerModRing(12)
        sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
        sage: M in Monoids()
        True
        sage: M.one()
        1
        sage: M.one() in M
        True
        sage: g = M._generators; g
        Finite family {1: 3, 2: 5}
        sage: g[1]*g[2]
        3
        sage: M.some_elements()
        [1, 3, 5, 9]

        sage: M.list()
        [1, 3, 5, 9]

        sage: M.idempotents()
        [1, 9]

    As can be seen above, elements are represented by default the
    corresponding element in the ambient monoid. One can also represent
    the elements by their reduced word::

        sage: M.repr_element_method("reduced_word")
        sage: M.list()
        [[], [1], [2], [1, 1]]

    In case the reduced word has not yet been calculated, the element
    will be represented by the corresponding element in the ambient
    monoid::

        sage: R = IntegerModRing(13)
        sage: N = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
        sage: N.repr_element_method("reduced_word")
        sage: n = N.an_element()
        sage: n
        [1]
        sage: n*n
        9

    Calling :meth:`construct`, :meth:`cardinality`, or :meth:`list`,
    or iterating through the monoid will trigger its full construction
    and, as a side effect, compute all the reduced words. The order of
    the elements, and the induced choice of reduced word is currently
    length-lexicographic (i.e. the chosen reduced word is of minimal
    length, and then minimal lexicographically w.r.t. the order of the
    indices of the generators)::

        sage: M.cardinality()
        4
        sage: M.list()
        [[], [1], [2], [1, 1]]
        sage: g = M._generators

        sage: g[1]*g[2]
        [1]

        sage: g[1].transition(1)
        [1, 1]
        sage: g[1] * g[1]
        [1, 1]
        sage: g[1] * g[1] * g[1]
        [1]
        sage: g[1].transition(2)
        [1]
        sage: g[1] * g[2]
        [1]

        sage: [ x.lift() for x in M.list() ]
        [1, 3, 5, 9]

        sage: # needs sage.graphs
        sage: G = M.cayley_graph(side=\'twosided\'); G
        Looped multi-digraph on 4 vertices
        sage: G.edges(sort=True, key=str)
        [([1, 1], [1, 1], (2, \'left\')),
         ([1, 1], [1, 1], (2, \'right\')),
         ([1, 1], [1], (1, \'left\')),
         ([1, 1], [1], (1, \'right\')),
         ([1], [1, 1], (1, \'left\')),
         ([1], [1, 1], (1, \'right\')),
         ([1], [1], (2, \'left\')),
         ([1], [1], (2, \'right\')),
         ([2], [1], (1, \'left\')),
         ([2], [1], (1, \'right\')),
         ([2], [], (2, \'left\')),
         ([2], [], (2, \'right\')),
         ([], [1], (1, \'left\')),
         ([], [1], (1, \'right\')),
         ([], [2], (2, \'left\')),
         ([], [2], (2, \'right\'))]
        sage: list(map(sorted, M.j_classes()))
        [[[1], [1, 1]], [[], [2]]]
        sage: M.j_classes_of_idempotents()
        [[[1, 1]], [[]]]
        sage: M.j_transversal_of_idempotents()
        [[1, 1], []]

        sage: list(map(attrcall(\'pseudo_order\'), M.list()))                             # needs sage.graphs
        [[1, 0], [3, 1], [2, 0], [2, 1]]

    We can also use it to get submonoids from groups. We check that in the
    symmetric group, a transposition and a long cycle generate the whole group::

        sage: # needs sage.groups
        sage: G5 = SymmetricGroup(5)
        sage: N = AutomaticSemigroup(Family({1: G5([2,1,3,4,5]), 2: G5([2,3,4,5,1])}),
        ....:                        one=G5.one())
        sage: N.repr_element_method("reduced_word")
        sage: N.cardinality() == G5.cardinality()
        True
        sage: N.retract(G5((1,4,3,5,2)))
        [1, 2, 1, 2, 2, 1, 2, 1, 2, 2]
        sage: N.from_reduced_word([1, 2, 1, 2, 2, 1, 2, 1, 2, 2]).lift()
        (1,4,3,5,2)

    We can also create a semigroup of matrices, where we define the
    multiplication as matrix multiplication::

        sage: # needs sage.modules
        sage: M1 = matrix([[0,0,1],[1,0,0],[0,1,0]])
        sage: M2 = matrix([[0,0,0],[1,1,0],[0,0,1]])
        sage: M1.set_immutable()
        sage: M2.set_immutable()
        sage: def prod_m(x, y):
        ....:     z=x*y
        ....:     z.set_immutable()
        ....:     return z
        sage: Mon = AutomaticSemigroup([M1,M2], mul=prod_m,
        ....:                          category=Monoids().Finite().Subobjects())
        sage: Mon.cardinality()
        24
        sage: C = Mon.cayley_graph()                                                    # needs sage.graphs
        sage: C.is_directed_acyclic()                                                   # needs sage.graphs
        False

    Let us construct and play with the 0-Hecke Monoid::

        sage: # needs sage.graphs sage.modules
        sage: W = WeylGroup([\'A\',4]); W.rename(\'W\')
        sage: ambient_monoid = FiniteSetMaps(W, action=\'right\')
        sage: pi = W.simple_projections(length_increasing=True).map(ambient_monoid)
        sage: M = AutomaticSemigroup(pi, one=ambient_monoid.one()); M
        A submonoid of (Maps from W to itself) with 4 generators
        sage: M.repr_element_method("reduced_word")
        sage: sorted(M._elements_set, key=str)
        [[1], [2], [3], [4], []]
        sage: M.construct(n=10)
        sage: sorted(M._elements_set, key=str)
        [[1, 2], [1, 3], [1, 4], [1], [2, 1], [2, 3], [2], [3], [4], []]
        sage: elt = M.from_reduced_word([3,1,2,4,2])
        sage: M.construct(up_to=elt)
        sage: len(M._elements_set)
        36
        sage: M.cardinality()
        120

    We check that the 0-Hecke monoid is `J`-trivial and contains `2^4`
    idempotents::

        sage: len(M.idempotents())                                                      # needs sage.graphs sage.modules
        16
        sage: all(len(j) == 1 for j in M.j_classes())                                   # needs sage.graphs sage.modules
        True

    TESTS::

        sage: (g[1]).__hash__() == (g[1]*g[1]*g[1]).__hash__()
        True
        sage: g[1] == g[1]*g[1]*g[1]
        True
        sage: M.__class__                                                               # needs sage.graphs sage.modules
        <class \'sage.monoids.automatic_semigroup.AutomaticMonoid_with_category\'>
        sage: TestSuite(M).run()                                                        # needs sage.graphs sage.modules

        sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
        sage: R = IntegerModRing(34)
        sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(7)}), one=R.one())
        sage: M[3] in M
        True

    We need to pass in the ambient monoid to ``__init__`` to guarantee
    :class:`UniqueRepresentation` works properly::

        sage: R1 = IntegerModRing(12)
        sage: R2 = IntegerModRing(16)
        sage: M1 = AutomaticSemigroup(Family({1: R1(3), 2: R1(5)}), one=R1.one())
        sage: M2 = AutomaticSemigroup(Family({1: R2(3), 2: R2(5)}), one=R2.one())
        sage: M1 is M2
        False

    .. NOTE::

        Unlike what the name of the class may suggest, this currently
        implements only a subclass of automatic semigroups;
        essentially the finite ones. See :wikipedia:`Automatic_semigroup`.

    .. WARNING::

        :class:`AutomaticSemigroup` is designed primarily for finite
        semigroups. This property is not checked automatically (this
        would be too costly, if not undecidable). Use with care for an
        infinite semigroup, as certain features may require
        constructing all of it::

            sage: M = AutomaticSemigroup([2], category = Monoids().Subobjects()); M
            A submonoid of (Integer Ring) with 1 generators
            sage: M.retract(2)
            2
            sage: M.retract(3)   # not tested: runs forever trying to find 3
    '''
    @staticmethod
    def __classcall_private__(cls, generators, ambient=None, one=None, mul=..., category=None):
        """
        Parse and straighten the arguments; figure out the category.

        TESTS::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(9)
            sage: M = AutomaticSemigroup((), one=R.one())
            sage: M.ambient() == R
            True
            sage: AutomaticSemigroup((0,)).category()
            Join of Category of finitely generated semigroups
                and Category of subquotients of semigroups
                and Category of commutative magmas
                and Category of subobjects of sets
            sage: AutomaticSemigroup((0,), one=1).category()
            Join of Category of subquotients of monoids and
            Category of commutative monoids and
            Category of finitely generated semigroups and
            Category of subobjects of sets
            sage: AutomaticSemigroup((0,), one=0).category()
            Join of Category of commutative monoids and
            Category of finitely generated semigroups and
            Category of subquotients of semigroups and
            Category of subobjects of sets
            sage: AutomaticSemigroup((0,), mul=operator.add).category()
            Join of Category of semigroups and Category of subobjects of sets
            sage: AutomaticSemigroup((0,), one=0, mul=operator.add).category()
            Join of Category of monoids and Category of subobjects of sets

            sage: S5 = SymmetricGroup(5)                                                # needs sage.groups
            sage: AutomaticSemigroup([S5((1,2))]).category()                            # needs sage.groups
            Join of Category of finite groups and
            Category of subquotients of monoids and
            Category of finite finitely generated semigroups and
            Category of subquotients of finite sets and
            Category of subobjects of sets

        .. TODO::

            One would want a subsemigroup of a group to be
            automatically a subgroup (in ``Groups().Subobjects()``).
        """
    def __init__(self, generators, ambient, one, mul, category) -> None:
        """
        Initialize this semigroup.

        TESTS::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(21)
            sage: M = AutomaticSemigroup(Family(()), one=R.one())
            sage: M.ambient() == R
            True
            sage: M = AutomaticSemigroup(Family(()))
            Traceback (most recent call last):
            ...
            ValueError: AutomaticSemigroup requires at least one generator or `one` to determine the ambient space
        """
    def repr_element_method(self, style: str = 'ambient') -> None:
        '''
        Set the representation of the elements of the monoid.

        INPUT:

        - ``style`` -- "ambient" or "reduced_word"

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(17)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: M.list()
            [1, 3, 5, 9, 15, 8, 10, 11, 7, 6, 13, 16, 4, 14, 12, 2]
            sage: M.repr_element_method("reduced_word")
            sage: M.list()
            [[], [1], [2], [1, 1], [1, 2], [2, 2], [1, 1, 1], [1, 1, 2], [1, 2, 2],
             [2, 2, 2], [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 2], [1, 1, 1, 1, 2],
             [1, 1, 1, 2, 2], [1, 1, 1, 1, 2, 2]]
        '''
    def an_element(self):
        """
        Return the first given generator of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(16)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: M.an_element()
            3
        """
    def ambient(self):
        """
        Return the ambient semigroup of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(12)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: M.ambient()
            Ring of integers modulo 12

            sage: # needs sage.modules
            sage: M1 = matrix([[0,0,1],[1,0,0],[0,1,0]])
            sage: M2 = matrix([[0,0,0],[1,1,0],[0,0,1]])
            sage: M1.set_immutable()
            sage: M2.set_immutable()
            sage: def prod_m(x, y):
            ....:     z=x*y
            ....:     z.set_immutable()
            ....:     return z
            sage: Mon = AutomaticSemigroup([M1,M2], mul=prod_m)
            sage: Mon.ambient()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
        """
    def retract(self, ambient_element, check: bool = True):
        """
        Retract an element of the ambient semigroup into ``self``.

        EXAMPLES::

            sage: # needs sage.groups
            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: S5 = SymmetricGroup(5); S5.rename('S5')
            sage: M = AutomaticSemigroup(Family({1:S5((1,2)), 2:S5((1,2,3,4))}),
            ....:                        one=S5.one())
            sage: m = M.retract(S5((3,1))); m
            (1,3)
            sage: m.parent() is M
            True
            sage: M.retract(S5((4,5)), check=False)
            (4,5)
            sage: M.retract(S5((4,5)))
            Traceback (most recent call last):
            ...
            ValueError: (4,5) not in A subgroup of (S5) with 2 generators

        TESTS::

            sage: len(M._retract.cache.keys())                                          # needs sage.groups
            24
        """
    def lift(self, x):
        """
        Lift an element of ``self`` into its ambient space.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(15)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: a = M.an_element()
            sage: a.lift() in R
            True
            sage: a.lift()
            3
            sage: [m.lift() for m in M]
            [1, 3, 5, 9, 0, 10, 12, 6]
        """
    def semigroup_generators(self):
        """
        Return the family of generators of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(28)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}))
            sage: M.semigroup_generators()
            Finite family {1: 3, 2: 5}
        """
    gens = semigroup_generators
    def __iter__(self):
        """
        Return iterator over elements of the semigroup.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(5)
            sage: M = AutomaticSemigroup([R(3), R(4)], one=R.one())
            sage: I = M.__iter__()
            sage: next(I)
            1
            sage: M.list()
            [1, 3, 4, 2]
            sage: next(I)
            3
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(12)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: M.cardinality()
            4

        TESTS::

            sage: assert isinstance(M.cardinality(), Integer)  # This did fail at some point
        """
    def list(self):
        '''
        Return the list of elements of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(12)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: M.repr_element_method("reduced_word")
            sage: M.list()
            [[], [1], [2], [1, 1]]

        TESTS::

            sage: assert isinstance(M.cardinality(), Integer)  # This did fail at some point
        '''
    def product(self, x, y):
        """
        Return the product of two elements in ``self``. It is done by
        retracting the multiplication in the ambient semigroup.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(12)
            sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
            sage: a = M[1]
            sage: b = M[2]
            sage: a*b
            [1]
        """
    def from_reduced_word(self, l):
        """
        Return the element of ``self`` obtained from the reduced word ``l``.

        INPUT:

        - ``l`` -- list of indices of the generators

        .. NOTE::

            We do not save the given reduced word ``l`` as an attribute of the
            element, as some elements above in the branches may have not been
            explored by the iterator yet.

        EXAMPLES::

            sage: # needs sage.groups
            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: G4 = SymmetricGroup(4)
            sage: M = AutomaticSemigroup(Family({1:G4((1,2)), 2:G4((1,2,3,4))}),
            ....:                        one=G4.one())
            sage: M.from_reduced_word([2, 1, 2, 2, 1]).lift()
            (1,3)
            sage: M.from_reduced_word([2, 1, 2, 2, 1]) == M.retract(G4((3,1)))
            True
        """
    def construct(self, up_to=None, n=None) -> None:
        '''
        Construct the elements of ``self``.

        INPUT:

        - ``up_to`` -- an element of ``self`` or of the ambient semigroup

        - ``n`` -- integer or ``None`` (default: ``None``)

        This construct all the elements of this semigroup, their
        reduced words, and the right Cayley graph. If `n` is
        specified, only the `n` first elements of the semigroup are
        constructed. If ``element`` is specified, only the elements up
        to ``ambient_element`` are constructed.

        EXAMPLES::

            sage: # needs sage.groups sage.modules
            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: W = WeylGroup([\'A\',3]); W.rename(\'W\')
            sage: ambient_monoid = FiniteSetMaps(W, action=\'right\')
            sage: pi = W.simple_projections(length_increasing=True).map(ambient_monoid)
            sage: M = AutomaticSemigroup(pi, one=ambient_monoid.one()); M
            A submonoid of (Maps from W to itself) with 3 generators
            sage: M.repr_element_method("reduced_word")
            sage: sorted(M._elements_set, key=str)
            [[1], [2], [3], []]
            sage: elt = M.from_reduced_word([2,3,1,2])
            sage: M.construct(up_to=elt)
            sage: len(M._elements_set)
            19
            sage: M.cardinality()
            24
        '''
    class Element(ElementWrapper):
        def __init__(self, ambient_element, parent) -> None:
            """
            TESTS::

                sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
                sage: R = IntegerModRing(21)
                sage: M = AutomaticSemigroup(Family([2]))
                sage: m = M(2); m
                2
                sage: type(m)
                <class 'sage.monoids.automatic_semigroup.AutomaticSemigroup_with_category.element_class'>
            """
        def reduced_word(self):
            """
            Return the length-lexicographic shortest word of ``self``.

            OUTPUT: list of indexes of the generators

            Obtaining the reduced word requires having constructed the
            Cayley graph of the semigroup up to ``self``. If this is
            not the case, an error is raised.

            EXAMPLES::

                sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
                sage: R = IntegerModRing(15)
                sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
                sage: M.construct()
                sage: for m in M: print((m, m.reduced_word()))
                (1, [])
                (3, [1])
                (5, [2])
                (9, [1, 1])
                (0, [1, 2])
                (10, [2, 2])
                (12, [1, 1, 1])
                (6, [1, 1, 1, 1])

            TESTS:

            We check that :issue:`19631` is fixed::

                sage: R = IntegerModRing(101)
                sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
                sage: e = M.from_reduced_word([1, 1, 1, 2, 2, 2])
                sage: e.reduced_word()
                [1, 1, 1, 2, 2, 2]
            """
        def lift(self):
            '''
            Lift the element ``self`` into its ambient semigroup.

            EXAMPLES::

                sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
                sage: R = IntegerModRing(18)
                sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}))
                sage: M.repr_element_method("reduced_word")
                sage: m = M.an_element(); m
                [1]
                sage: type(m)
                <class \'sage.monoids.automatic_semigroup.AutomaticSemigroup_with_category.element_class\'>
                sage: m.lift()
                3
                sage: type(m.lift())
                <class \'sage.rings.finite_rings.integer_mod.IntegerMod_int\'>
            '''
        @cached_method
        def transition(self, i):
            '''
            The multiplication on the right by a generator.

            INPUT:

            - ``i`` -- an element from the indexing set of the generators

            This method computes ``self * self._generators[i]``.

            EXAMPLES::

                sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
                sage: R = IntegerModRing(17)
                sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
                sage: M.repr_element_method("reduced_word")
                sage: M.construct()
                sage: a = M.an_element()
                sage: a.transition(1)
                [1, 1]
                sage: a.transition(2)
                [1, 2]
            '''
        def __copy__(self, memo=None):
            """
            Return ``self`` since this has unique representation.

            INPUT:

            - ``memo`` -- ignored, but required by the deepcopy API

            EXAMPLES::

                sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
                sage: R = IntegerModRing(12)
                sage: M = AutomaticSemigroup(Family({1: R(3), 2: R(5)}), one=R.one())
                sage: m = M.an_element()
                sage: copy(m) is m
                True
                sage: from copy import deepcopy
                sage: deepcopy(m) is m
                True
            """
        __deepcopy__ = __copy__

class AutomaticMonoid(AutomaticSemigroup):
    def one(self):
        """
        Return the unit of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(21)
            sage: M = R.submonoid(())
            sage: M.one()
            1
            sage: M.one().parent() is M
            True
        """
    semigroup_generators: Incomplete
    def monoid_generators(self):
        """
        Return the family of monoid generators of ``self``.

        EXAMPLES::

            sage: from sage.monoids.automatic_semigroup import AutomaticSemigroup
            sage: R = IntegerModRing(28)
            sage: M = R.submonoid(Family({1: R(3), 2: R(5)}))
            sage: M.monoid_generators()
            Finite family {1: 3, 2: 5}

        Note that the monoid generators do not include the unit,
        unlike the semigroup generators::

            sage: M.semigroup_generators()
            Family (1, 3, 5)
        """
    gens = monoid_generators
