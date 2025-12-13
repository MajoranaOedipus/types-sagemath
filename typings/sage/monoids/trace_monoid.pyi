from sage.combinat.words.alphabet import Alphabet as Alphabet
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.monoids.free_monoid import FreeMonoid as FreeMonoid
from sage.monoids.monoid import Monoid_class as Monoid_class
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.structure.element import MonoidElement as MonoidElement
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TraceMonoidElement(ElementWrapper, MonoidElement):
    """
    Element of a trace monoid, also known as a trace.

    Elements of trace monoid is actually a equivalence classes
    of related free monoid over some equivalence relation
    that in the case is presented as independence relation.

    .. RUBRIC:: Representative

    We transform each trace to its lexicographic form for the
    representative in the ambient free monoid. This is also used
    for comparisons.

    EXAMPLES::

        sage: from sage.monoids.trace_monoid import TraceMonoid
        sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
        sage: M.<a,b,c,d> = TraceMonoid(I=I)
        sage: x = b * a * d * a * c * b
        sage: x^3
        [b*a^2*d*b^2*c*a^2*d*b^2*c*a^2*d*b*c]
        sage: x^0
        1
        sage: x.lex_normal_form()
        b*a^2*d*b*c
        sage: x.foata_normal_form()
        (b, a*d, a, b*c)
    """
    def lex_normal_form(self):
        """
        Return the lexicographic normal form of ``self``.

        OUTPUT: a free monoid element

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: (a*b).lex_normal_form()
            a*b
            sage: (b*a).lex_normal_form()
            b*a
            sage: (d*a).lex_normal_form()
            a*d
        """
    def foata_normal_form(self) -> tuple:
        """
        Return the Foata normal form of ``self``.

        OUTPUT: tuple of free monoid elements

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b * a * d * a * c * b
            sage: x.foata_normal_form()
            (b, a*d, a, b*c)
        """
    @cached_method
    def dependence_graph(self):
        """
        Return dependence graph of the trace.

        It is a directed graph where all dependent (non-commutative)
        generators are connected by edges which
        direction depend on the generator position in the trace.

        OUTPUT: directed graph of generator indexes

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b * a * d * a * c * b
            sage: x.dependence_graph()                                                  # needs sage.graphs
            Digraph on 6 vertices
        """
    @cached_method
    def hasse_diagram(self, algorithm: str = 'naive'):
        """
        Return Hasse diagram of the trace.

        Hasse diagram is a dependence graph without transitive edges.

        INPUT:

        - ``algorithm`` -- string (default: ``'naive'``); defines algorithm
          that will be used to compute Hasse diagram; there are two
          variants: ``'naive'`` and ``'min'``.

        OUTPUT: directed graph of generator indexes

        .. SEEALSO::

            :meth:`~sage.monoids.trace_monoid.TraceMonoidElement.naive_hasse_digram`,
            :meth:`~sage.monoids.trace_monoid.TraceMonoidElement.min_hasse_diagram`.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b * a * d * a * c * b
            sage: x.hasse_diagram()                                                     # needs sage.graphs
            Digraph on 6 vertices

        TESTS::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b * a * d * a * c * b
            sage: x.hasse_diagram(algorithm='naive') == x.hasse_diagram(algorithm='min')            # needs sage.graphs
            True
            sage: y = b * a^3 * d * a * c * b^2
            sage: y.hasse_diagram(algorithm='naive') == y.hasse_diagram(algorithm='min')            # needs sage.graphs
            True
        """
    def min_hasse_diagram(self):
        """
        Return Hasse diagram of the trace.

        OUTPUT: directed graph of generator indexes

        .. SEEALSO::

            :meth:`~sage.monoids.trace_monoid.TraceMonoidElement.hasse_digram`,
            :meth:`~sage.monoids.trace_monoid.TraceMonoidElement.naive_hasse_diagram`.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b * a * d * a * c * b
            sage: x.min_hasse_diagram()                                                 # needs sage.graphs
            Digraph on 6 vertices
        """
    def naive_hasse_diagram(self):
        """
        Return Hasse diagram of ``self``.

        ALGORITHM:

        In loop check for every two pair of edges if they
        have common vertex, remove their transitive edge.

        OUTPUT: directed graph of generator indexes

        .. SEEALSO::

            :meth:`~sage.monoids.trace_monoid.TraceMonoidElement.hasse_digram`,
            :meth:`~sage.monoids.trace_monoid.TraceMonoidElement.min_hasse_diagram`.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b * a * d * a * c * b
            sage: x.naive_hasse_diagram()                                               # needs sage.graphs
            Digraph on 6 vertices
        """
    def alphabet(self):
        """
        Return alphabet of ``self``.

        OUTPUT: a set of free monoid generators

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: x = b*a*d*a*c*b
            sage: x.alphabet()
            {b, a, d, c}
        """
    def projection(self, letters):
        """
        Return a trace that formed from ``self`` by erasing ``letters``.

        INPUT:

        - ``letters`` -- set of generators; defines set of letters that will be
          used to filter the trace

        OUTPUT: a trace

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: F.<a,b,c,d> = FreeMonoid()
            sage: I = ((a,d), (d,a), (b,c), (c,b))
            sage: M.<ac,bc,cc,dc> = TraceMonoid(F, I=I)
            sage: x = M(b*a*d*a*c*b)
            sage: x.projection({a,b})
            [b*a^2*b]
            sage: x.projection({b,d,c})
            [b*d*b*c]
        """
    def multiplicative_order(self):
        """
        Return the multiplicative order of ``self``, which is `\\infty`
        for any element not the identity.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: a.multiplicative_order()
            +Infinity
            sage: M.one().multiplicative_order()
            1
        """

class TraceMonoid(UniqueRepresentation, Monoid_class):
    """
    Return a free partially commuting monoid (trace monoid) on `n` generators
    over independence relation `I`.

    We construct a trace monoid by specifying:

    - a free monoid and independence relation
    - or generator names and independence relation,
      FreeMonoid is constructed automatically then.

    INPUT:

    - ``M`` -- a free monoid

    - ``I`` -- commutation relation between generators
      (or their names if the ``names`` are given)

    - ``names`` -- names of generators

    EXAMPLES::

        sage: from sage.monoids.trace_monoid import TraceMonoid
        sage: F = TraceMonoid(names=('a', 'b', 'c'), I={('a','c'), ('c','a')}); F
        Trace monoid on 3 generators ([a], [b], [c]) with independence relation {{a, c}}
        sage: x = F.gens()
        sage: x[0]*x[1]**5 * (x[0]*x[2])
        [a*b^5*a*c]

        sage: from sage.monoids.trace_monoid import TraceMonoid
        sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
        sage: latex(M)
        \\langle a, b, c \\mid ac=ca \\rangle

    TESTS::

        sage: from sage.monoids.trace_monoid import TraceMonoid
        sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
        sage: M.number_of_words(3) == len(M.words(3))                                   # needs sage.graphs
        True
    """
    Element = TraceMonoidElement
    @staticmethod
    def __classcall_private__(cls, M=None, I=..., names=None):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M1.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: M2.<a,b,c> = TraceMonoid(I=[('a','c')])
            sage: M3 = TraceMonoid(I=[{'a','c'}], names=('a', 'b', 'c'))
            sage: M1 is M2 and M2 is M3
            True
        """
    def __init__(self, M, I, names) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: TestSuite(M).run()
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: M.ngens()
            3
        """
    def one(self):
        """
        Return the neutral element of ``self``.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: M.one()
            1
        """
    def gen(self, i: int = 0):
        """
        Return the `i`-th generator of the monoid.

        INPUT:

        - ``i`` -- integer (default: 0)

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: M.gen(1)
            [b]
            sage: M.gen(4)
            Traceback (most recent call last):
            ...
            IndexError: argument i (= 4) must be between 0 and 2
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is infinite except for
        the trivial monoid.

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: M.cardinality()
            +Infinity
        """
    @cached_method
    def independence(self):
        """
        Return independence relation over the monoid.

        OUTPUT: set of commuting generator pairs

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: F.<a,b,c> = FreeMonoid()
            sage: I = frozenset(((a,c), (c,a)))
            sage: M.<ac,bc,cc> = TraceMonoid(F, I=I)
            sage: M.independence() == frozenset([frozenset([a,c])])
            True
        """
    @cached_method
    def dependence(self):
        """
        Return dependence relation over the monoid.

        OUTPUT: set of non-commuting generator pairs

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','c'), ('c','a')))
            sage: sorted(M.dependence())
            [(a, a), (a, b), (b, a), (b, b), (b, c), (c, b), (c, c)]
        """
    @cached_method
    def dependence_graph(self):
        """
        Return graph of dependence relation.

        OUTPUT: dependence graph with generators as vertices

        TESTS::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: F.<a,b,c> = FreeMonoid()
            sage: M.<ai,bi,ci> = TraceMonoid(F, I=((a,c), (c,a)))
            sage: M.dependence_graph() == Graph({a:[a,b], b:[b], c:[c,b]})              # needs sage.graphs
            True
        """
    @cached_method
    def independence_graph(self):
        """
        Return the digraph of independence relations.

        OUTPUT: independence graph with generators as vertices

        TESTS::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: F.<a,b,c> = FreeMonoid()
            sage: M.<ai,bi,ci> = TraceMonoid(F, I=((a,c), (c,a)))
            sage: M.independence_graph() == Graph({a:[c], b:[], c:[]})                  # needs sage.graphs
            True
        """
    @cached_method
    def dependence_polynomial(self, t=None):
        """
        Return dependence polynomial.

        The polynomial is defined as follows: `\\sum{i}{(-1)^i c_i t^i}`,
        where `c_i` equals to number of full subgraphs
        of size `i` in the independence graph.

        OUTPUT: a rational function in ``t`` with coefficients in the integer ring

        EXAMPLES::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: M.dependence_polynomial()                                             # needs sage.graphs
            1/(2*t^2 - 4*t + 1)
        """
    @cached_method
    def number_of_words(self, length):
        """
        Return number of unique words of defined length.

        INPUT:

        - ``length`` -- integer; defines size of words what number should be computed

        OUTPUT: words number as integer

        EXAMPLES:

        Get number of words of size 3 ::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: M.number_of_words(3)                                                  # needs sage.graphs
            48
        """
    @cached_method
    def words(self, length):
        """
        Return all lexicographic forms of defined length.

        INPUT:

        - ``length`` -- integer; defines size of words

        OUTPUT: set of traces of size ``length``

        EXAMPLES:

        All words of size 2::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: sorted(M.words(2))
            [[a^2], [a*b], [a*c], [a*d], [b*a], [b^2], [b*c],
             [b*d], [c*a], [c^2], [c*d], [d*b], [d*c], [d^2]]

        Get number of words of size 3::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: I = (('a','d'), ('d','a'), ('b','c'), ('c','b'))
            sage: M.<a,b,c,d> = TraceMonoid(I=I)
            sage: len(M.words(3))
            48

        TESTS::

            sage: from sage.monoids.trace_monoid import TraceMonoid
            sage: M.<a,b,c> = TraceMonoid(I=(('a','b'), ('b','a'), ('b', 'c'), ('c', 'b')))
            sage: for i in range(10):                                                   # needs sage.graphs
            ....:    assert len(M.words(i)) == M.number_of_words(i)
        """
