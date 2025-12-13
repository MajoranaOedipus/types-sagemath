from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.words.word import Word as Word
from sage.combinat.words.words import Words as Words
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.sets.set import Set as Set
from sage.structure.sage_object import SageObject as SageObject

class SuffixTrie(SageObject):
    def __init__(self, word) -> None:
        '''
        Construct the suffix trie of the word w.

        The suffix trie of a finite word w is a data structure representing
        the factors of w. It is a tree whose edges are labelled with
        letters of w, and whose leafs correspond to suffixes of w.

        This is a straightforward implementation of Algorithm 1 from
        [Ukko1995]_.  It constructs the suffix trie of w[:i] from that
        of w[:i-1].

        A suffix trie is modelled as a deterministic finite-state automaton
        together with the suffix_link map. The set of states corresponds to
        factors of the word (below we write x\' for the state corresponding
        to x); these are always 0, 1, .... The state 0 is the initial
        state, and it corresponds to the empty word.  For the purposes of
        the algorithm, there is also an auxiliary state -1. The transition
        function t is defined as::

                t(-1,a) = 0 for all letters a; and
                t(x\',a) = y\' for all x\',y\' \\in Q such that y = xa,

        and the suffix link function is defined as::

                suffix_link(0) = -1;
                suffix_link(x\') = y\', if x = ay for some letter a.

        REFERENCES:

        - [Ukko1995]_

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w); t
            Suffix Trie of the word: cacao

        ::

            sage: e = Words("ab")()
            sage: t = SuffixTrie(e); t
            Suffix Trie of the word:
            sage: t.process_letter("a"); t
            Suffix Trie of the word: a
            sage: t.process_letter("b"); t
            Suffix Trie of the word: ab
            sage: t.process_letter("a"); t
            Suffix Trie of the word: aba

        TESTS::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: s = SuffixTrie(w)
            sage: loads(dumps(s))
            Suffix Trie of the word: cacao
        '''
    def process_letter(self, letter) -> None:
        '''
        Modify ``self`` to produce the suffix trie for ``self.word() +
        letter``.

        .. NOTE::

           ``letter`` must occur within the alphabet of the word.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("ab")("ababba")
            sage: t = SuffixTrie(w); t
            Suffix Trie of the word: ababba
            sage: t.process_letter("a"); t
            Suffix Trie of the word: ababbaa

        TESTS::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w); t
            Suffix Trie of the word: cacao
            sage: t.process_letter("d")
            Traceback (most recent call last):
            ...
            ValueError: d not in alphabet
        '''
    def node_to_word(self, state: int = 0):
        '''
        Return the word obtained by reading the edge labels from 0 to
        ``state``.

        INPUT:

        - ``state`` -- (default: 0) a state

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("abc")("abcba")
            sage: t = SuffixTrie(w)
            sage: t.node_to_word(10)
            word: abcba
            sage: t.node_to_word(7)
            word: abcb
        '''
    def word(self):
        '''
        Return the word whose suffix tree this is.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("abc")("abcba")
            sage: t = SuffixTrie(w)
            sage: t.word()
            word: abcba
            sage: t.word() == w
            True
        '''
    def __eq__(self, other) -> bool:
        '''
        If ``self`` and ``other`` have the same transition function,
        the same suffix link, and the same word, then they are equal.

        TESTS::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: SuffixTrie(Word("cacao")) == SuffixTrie(Word("ababc"))
            False
            sage: W = Words("cao")
            sage: s = SuffixTrie(W("cacao"))
            sage: t = SuffixTrie(W())
            sage: t.process_letter("c")
            sage: t.process_letter("a")
            sage: t.process_letter("c")
            sage: t.process_letter("a")
            sage: t.process_letter("o")
            sage: t == s
            True
        '''
    def transition_function(self, node, word):
        """
        Return the state reached by beginning at ``node`` and following the
        arrows in the transition graph labelled by the letters of ``word``.

        INPUT:

        - ``node`` -- a node
        - ``word`` -- a word

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words([0,1])([0,1,0,1,1])
            sage: t = SuffixTrie(w)
            sage: all(t.transition_function(u, letter) == v
            ....:     for (u, letter), v in t._transition_function.items())
            True
        """
    def states(self):
        '''
        Return the states of the automaton defined by the suffix trie.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words([0,1])([0,1,1])
            sage: t = SuffixTrie(w)
            sage: t.states()
            [0, 1, 2, 3, 4]

        ::

            sage: u = Words("aco")("cacao")
            sage: s = SuffixTrie(u)
            sage: s.states()
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        '''
    def suffix_link(self, state):
        '''
        Evaluate the suffix link map of the suffix trie on ``state``.

        Note that the suffix link map is not defined on -1.

        INPUT:

        - ``state`` -- a state

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w)
            sage: list(map(t.suffix_link, range(13)))
            [-1, 0, 3, 0, 5, 1, 7, 2, 9, 10, 11, 12, 0]
            sage: t.suffix_link(0)
            -1

        TESTS::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w)
            sage: t.suffix_link([1])
            Traceback (most recent call last):
            ...
            TypeError: [1] is not an integer
            sage: t.suffix_link(-1)
            Traceback (most recent call last):
            ...
            TypeError: suffix link is not defined for -1
            sage: t.suffix_link(17)
            Traceback (most recent call last):
            ...
            TypeError: 17 is not a state
        '''
    def active_state(self):
        '''
        Return the active state of the suffix trie.

        This is the state corresponding to the word as a suffix of
        itself.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w)
            sage: t.active_state()
            8

        ::

            sage: u = Words([0,1])([0,1,1,0,1,0,0,1])
            sage: s = SuffixTrie(u)
            sage: s.active_state()
            22
        '''
    def final_states(self):
        '''
        Return the set of final states of the suffix trie.

        These are the states corresponding to the suffixes of
        ``self.word()``. They are obtained be repeatedly following the
        suffix link from the active state until we reach 0.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w)
            sage: t.final_states() == Set([8, 9, 10, 11, 12, 0])
            True
        '''
    def has_suffix(self, word) -> bool:
        '''
        Return ``True`` if and only if ``word`` is a suffix of ``self.word()``.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cacao")
            sage: t = SuffixTrie(w)
            sage: [t.has_suffix(w[i:]) for i in range(w.length()+1)]
            [True, True, True, True, True, True]
            sage: [t.has_suffix(w[:i]) for i in range(w.length()+1)]
            [True, False, False, False, False, True]
        '''
    def to_digraph(self):
        '''
        Return a ``DiGraph`` object of the transition graph of the suffix
        trie.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cac")
            sage: t = SuffixTrie(w)
            sage: d = t.to_digraph(); d                                                 # needs sage.graphs
            Digraph on 6 vertices
            sage: d.adjacency_matrix()                                                  # needs sage.graphs sage.modules
            [0 1 0 1 0 0]
            [0 0 1 0 0 0]
            [0 0 0 0 1 0]
            [0 0 0 0 0 1]
            [0 0 0 0 0 0]
            [0 0 0 0 0 0]
        '''
    def plot(self, layout: str = 'tree', tree_root: int = 0, tree_orientation: str = 'up', vertex_colors=None, edge_labels: bool = True, *args, **kwds):
        '''
        Return a Graphics object corresponding to the transition graph of
        the suffix trie.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: SuffixTrie(Word("cacao")).plot()                                      # needs sage.plot
            Graphics object consisting of 38 graphics primitives

        TESTS::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: type(SuffixTrie(Word("cacao")).plot())                                # needs sage.plot
            <class \'sage.plot.graphics.Graphics\'>
        '''
    def show(self, *args, **kwds) -> None:
        '''
        Display the output of :meth:`plot`.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import SuffixTrie
            sage: w = Words("cao")("cac")
            sage: t = SuffixTrie(w)
            sage: t.show()                                                              # needs sage.plot
        '''

class ImplicitSuffixTree(SageObject):
    def __init__(self, word) -> None:
        '''
        Construct the implicit suffix tree of a word w.

        The suffix tree of a word w is a compactification of the suffix
        trie for w. The compactification removes all nodes that have
        exactly one incoming edge and exactly one outgoing edge. It
        consists of two components: a tree and a word. Thus, instead of
        labelling the edges by factors of w, we can labelled them by
        indices of the occurrence of the factors in w.

        The following is a straightforward implementation of Ukkonen\'s
        on-line algorithm for constructing the
        implicit suffix tree [Ukko1995]_.  It constructs the suffix tree for
        w[:i] from that of w[:i-1].

        GENERAL IDEA. The suffix tree of w[:i+1] can be obtained from that
        of w[:i] by visiting each node corresponding to a suffix of w[:i]
        and modifying the tree by applying one of two rules (either append
        a new node to the tree, or split an edge into two). The "active
        state" is the node where the algorithm begins and the "suffix link"
        carries us to the next node that needs to be dealt with.

        TREE. The tree is modelled as an automaton, which is stored as a
        dictionary of dictionaries: it is keyed by the nodes of the tree,
        and the corresponding dictionary is keyed by pairs `(i,j)` of
        integers representing the word w[i-1:j]. This makes it faster to
        look up a particular transition beginning at a specific node.

        STATES/NODES. The states will always be -1, 0, 1, ..., n. The state
        -1 is special and is only used for the purposes of the algorithm.
        All transitions map -1 to 0, so this information is not explicitly
        stored in the transition function.

        EXPLICIT/IMPLICIT NODES. By definition, some of the nodes will not
        be states, but merely locations along an edge; these are called
        implicit nodes. A node r (implicit or explicit) is referenced as a
        pair (s,(k,p)) where s is an ancestor of r and w[k-1:p] is the word
        read by transitioning from s to r in the suffix trie. A reference
        pair is canonical if s is the closest ancestor of r.

        SUFFIX LINK. The algorithm makes use of a map from (some) nodes to
        other nodes, called the suffix link. This is stored as a
        dictionary.

        ACTIVE STATE. We store as ._active_state the active state of the
        tree, the state where the algorithm will begin when processing the
        next letter.

        RUNNING TIME. The running time and storage space of the algorithm
        is linear in the length of the word w (whereas for a suffix tree it
        is quadratic).

        REFERENCES:

        - [Ukko1995]_

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: w = Words("aco")("cacao")
            sage: t = ImplicitSuffixTree(w); t
            Implicit Suffix Tree of the word: cacao
            sage: ababb = Words([0,1])([0,1,0,1,1])
            sage: s = ImplicitSuffixTree(ababb); s
            Implicit Suffix Tree of the word: 01011

        TESTS::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: w = Words("cao")("cacao")
            sage: s = ImplicitSuffixTree(w)
            sage: loads(dumps(s))
            Implicit Suffix Tree of the word: cacao
        '''
    def word(self):
        """
        Return the word whose implicit suffix tree this is.

        TESTS::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: ImplicitSuffixTree(Word([0,1,0,1,0])).word() == Word([0,1,0,1,0])
            True
        """
    def transition_function_dictionary(self) -> dict:
        '''
        Return the transition function as a dictionary of dictionaries.

        The format is consistent with the input format for ``DiGraph``.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: W = Words("aco")
            sage: t = ImplicitSuffixTree(W("cac"))
            sage: t.transition_function_dictionary()
            {0: {1: (0, None), 2: (1, None)}}

        ::

            sage: W = Words([0,1])
            sage: t = ImplicitSuffixTree(W([0,1,0]))
            sage: t.transition_function_dictionary()
            {0: {1: (0, None), 2: (1, None)}}
        '''
    def to_digraph(self, word_labels: bool = False):
        """
        Return a ``DiGraph`` object of the transition graph of the suffix tree.

        INPUT:

        - ``word_labels`` -- boolean (default: ``False``); if ``False``, labels
          the edges by pairs `(i, j)`. If ``True``, labels the edges by ``word[i:j]``

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: W = Words([0,1,2])
            sage: t = ImplicitSuffixTree(W([0,1,0,1,2]))
            sage: t.to_digraph()                                                        # needs sage.graphs
            Digraph on 8 vertices
        """
    def plot(self, word_labels: bool = False, layout: str = 'tree', tree_root: int = 0, tree_orientation: str = 'up', vertex_colors=None, edge_labels: bool = True, *args, **kwds):
        """
        Return a Graphics object corresponding to the transition graph of
        the suffix tree.

        INPUT:

        - ``word_labels`` -- boolean (default: ``False``); if ``False``, labels
          the edges by pairs `(i, j)`; if ``True``, labels the edges by ``word[i:j]``
        - ``layout`` -- (default: ``'tree'``)
        - ``tree_root`` -- (default: 0)
        - ``tree_orientation`` -- (default: ``'up'``)
        - ``vertex_colors`` -- (default: ``None``)
        - ``edge_labels`` -- (default: ``True``)

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: ImplicitSuffixTree(Word('cacao')).plot(word_labels=True)              # needs sage.graphs sage.plot
            Graphics object consisting of 23 graphics primitives
            sage: ImplicitSuffixTree(Word('cacao')).plot(word_labels=False)             # needs sage.graphs sage.plot
            Graphics object consisting of 23 graphics primitives

        TESTS::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: type(ImplicitSuffixTree(Word('cacao')).plot(word_labels=True))        # needs sage.graphs sage.plot
            <class 'sage.plot.graphics.Graphics'>
            sage: type(ImplicitSuffixTree(Word('cacao')).plot(word_labels=False))       # needs sage.graphs sage.plot
            <class 'sage.plot.graphics.Graphics'>
        """
    def show(self, word_labels=None, *args, **kwds) -> None:
        '''
        Display the output of :meth:`plot`.

        INPUT:

        - ``word_labels`` -- (default: ``None``) if ``False``, labels the edges
          by pairs `(i, j)`; if ``True``, labels the edges by ``word[i:j]``

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: w = Words("cao")("cacao")
            sage: t = ImplicitSuffixTree(w)
            sage: t.show(word_labels=True)                                              # needs sage.plot
            sage: t.show(word_labels=False)                                             # needs sage.plot
        '''
    def __eq__(self, other) -> bool:
        """
        If ``self`` and ``other`` have the same transition function
        and the same word, then they are equal.

        TESTS::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: w = Words([0,1,2])([0,1,0,1,2])
            sage: u = Words([0,1,2])(iter([0,1,0,1,2]))[:5]
            sage: ImplicitSuffixTree(w) == ImplicitSuffixTree(u)
            True
        """
    def transition_function(self, word, node: int = 0):
        '''
        Return the node obtained by starting from ``node`` and following the
        edges labelled by the letters of ``word``.

        OUTPUT:

        ``("explicit", end_node)`` if we end at ``end_node``, or
        ``("implicit", edge, d)`` if we end `d` spots along an edge.

        INPUT:

        - ``word`` -- a word
        - ``node`` -- (default: 0) starting node

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: W = Words([0,1,2])
            sage: t = ImplicitSuffixTree(W([0,1,0,1,2]))
            sage: t.transition_function(W([0,1,0]))
            (\'implicit\', (3, 1), 1)
            sage: t.transition_function(W([0,1,2]))
            (\'explicit\', 4)
            sage: t.transition_function(W([0,1,2]), 5)
            (\'explicit\', 2)
            sage: t.transition_function(W([0,1]), 5)
            (\'implicit\', (5, 2), 2)
        '''
    def states(self) -> list:
        """
        Return the states (explicit nodes) of the suffix tree.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: W = Words([0,1,2])
            sage: t = ImplicitSuffixTree(W([0,1,0,1,2]))
            sage: t.states()
            [0, 1, 2, 3, 4, 5, 6, 7]
        """
    def suffix_link(self, state):
        """
        Evaluate the suffix link map of the implicit suffix tree on ``state``.

        Note that the suffix link is not defined for all states.

        The suffix link of a state `x'` that corresponds to the suffix `x` is
        defined to be -1 is `x'` is the root (0) and `y'` otherwise, where `y'`
        is the state corresponding to the suffix ``x[1:]``.

        INPUT:

        - ``state`` -- a state

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: W = Words([0,1,2])
            sage: t = ImplicitSuffixTree(W([0,1,0,1,2]))
            sage: t.suffix_link(3)
            5
            sage: t.suffix_link(5)
            0
            sage: t.suffix_link(0)
            -1
            sage: t.suffix_link(-1)
            Traceback (most recent call last):
                ...
            TypeError: there is no suffix link from -1
        """
    def active_state(self):
        """
        Return the active state of the suffix tree.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: W = Words([0,1,2])
            sage: t = ImplicitSuffixTree(W([0,1,0,1,2]))
            sage: t.active_state()
            (0, (6, 6))
        """
    def process_letter(self, letter) -> None:
        '''
        Modify the current implicit suffix tree producing the implicit
        suffix tree for ``self.word() + letter``.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: w = Words("aco")("cacao")
            sage: t = ImplicitSuffixTree(w[:-1]); t
            Implicit Suffix Tree of the word: caca
            sage: t.process_letter(w[-1]); t
            Implicit Suffix Tree of the word: cacao

        ::

            sage: W = Words([0,1])
            sage: s = ImplicitSuffixTree(W([0,1,0,1])); s
            Implicit Suffix Tree of the word: 0101
            sage: s.process_letter(W([1])[0]); s
            Implicit Suffix Tree of the word: 01011
        '''
    def to_explicit_suffix_tree(self) -> None:
        '''
        Convert ``self`` to an explicit suffix tree.

        It is obtained by processing an end of string letter as if it
        were a regular letter, except that no new leaf nodes are
        created (thus, the only thing that happens is that some
        implicit nodes become explicit).

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: w = Words("aco")("cacao")
            sage: t = ImplicitSuffixTree(w)
            sage: t.to_explicit_suffix_tree()

        ::

            sage: W = Words([0,1])
            sage: s = ImplicitSuffixTree(W([0,1,0,1,1]))
            sage: s.to_explicit_suffix_tree()
        '''
    def edge_iterator(self) -> Generator[Incomplete]:
        '''
        Return an iterator over the edges of the suffix tree.

        The edge from `u` to `v` labelled by `(i,j)` is yielded as
        the tuple `(u,v,(i,j))`.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: sorted( ImplicitSuffixTree(Word("aaaaa")).edge_iterator() )
            [(0, 1, (0, None))]
            sage: sorted( ImplicitSuffixTree(Word([0,1,0,1])).edge_iterator() )
            [(0, 1, (0, None)), (0, 2, (1, None))]
            sage: sorted( ImplicitSuffixTree(Word()).edge_iterator() )
            []
        '''
    def number_of_factors(self, n=None):
        '''
        Count the number of distinct factors of ``self.word()``.

        INPUT:

        - ``n`` -- integer or ``None``

        OUTPUT:

        If ``n`` is an integer, returns the number of distinct factors
        of length ``n``. If ``n`` is ``None``, returns the total number of
        distinct factors.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: t = ImplicitSuffixTree(Word([1,2,1,3,1,2,1]))
            sage: t.number_of_factors()
            22
            sage: t.number_of_factors(1)
            3
            sage: t.number_of_factors(9)
            0
            sage: t.number_of_factors(0)
            1

        ::

            sage: t = ImplicitSuffixTree(Word("cacao"))
            sage: t.number_of_factors()
            13
            sage: list(map(t.number_of_factors, range(10)))
            [1, 3, 3, 3, 2, 1, 0, 0, 0, 0]

        ::

            sage: t = ImplicitSuffixTree(Word("c"*1000))
            sage: t.number_of_factors()
            1001
            sage: t.number_of_factors(17)
            1
            sage: t.number_of_factors(0)
            1

        ::

            sage: ImplicitSuffixTree(Word()).number_of_factors()
            1

        ::

            sage: blueberry = ImplicitSuffixTree(Word("blueberry"))
            sage: blueberry.number_of_factors()
            43
            sage: list(map(blueberry.number_of_factors, range(10)))
            [1, 6, 8, 7, 6, 5, 4, 3, 2, 1]
        '''
    def factor_iterator(self, n=None) -> Generator[Incomplete]:
        '''
        Generate distinct factors of ``self``.

        INPUT:

        - ``n`` -- integer or ``None``

        OUTPUT:

        If ``n`` is an integer, returns an iterator over all distinct
        factors of length ``n``. If ``n`` is ``None``, returns an iterator
        generating all distinct factors.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree
            sage: sorted( ImplicitSuffixTree(Word("cacao")).factor_iterator() )
            [word: , word: a, word: ac, word: aca, word: acao, word: ao, word: c, word: ca, word: cac, word: caca, word: cacao, word: cao, word: o]
            sage: sorted( ImplicitSuffixTree(Word("cacao")).factor_iterator(1) )
            [word: a, word: c, word: o]
            sage: sorted( ImplicitSuffixTree(Word("cacao")).factor_iterator(2) )
            [word: ac, word: ao, word: ca]
            sage: sorted( ImplicitSuffixTree(Word([0,0,0])).factor_iterator() )
            [word: , word: 0, word: 00, word: 000]
            sage: sorted( ImplicitSuffixTree(Word([0,0,0])).factor_iterator(2) )
            [word: 00]
            sage: sorted( ImplicitSuffixTree(Word([0,0,0])).factor_iterator(0) )
            [word: ]
            sage: sorted( ImplicitSuffixTree(Word()).factor_iterator() )
            [word: ]
            sage: sorted( ImplicitSuffixTree(Word()).factor_iterator(2) )
            []
        '''
    def LZ_decomposition(self):
        """
        Return a list of index of the beginning of the block of the Lempel-Ziv
        decomposition of ``self.word``

        The *Lempel-Ziv decomposition* is the factorisation `u_1...u_k` of a
        word `w=x_1...x_n` such that `u_i` is the longest prefix of `u_i...u_k`
        that has an occurrence starting before `u_i` or a letter if this prefix
        is empty.

        OUTPUT:

        Return a list ``iB`` of index such that the blocks of the decomposition
        are ``self.word()[iB[k]:iB[k+1]]``

        EXAMPLES::

            sage: w = Word('abababb')
            sage: T = w.suffix_tree()
            sage: T.LZ_decomposition()
            [0, 1, 2, 6, 7]
            sage: w = Word('abaababacabba')
            sage: T = w.suffix_tree()
            sage: T.LZ_decomposition()
            [0, 1, 2, 3, 6, 8, 9, 11, 13]
            sage: w = Word([0, 0, 0, 1, 1, 0, 1])
            sage: T = w.suffix_tree()
            sage: T.LZ_decomposition()
            [0, 1, 3, 4, 5, 7]
            sage: w = Word('0000100101')
            sage: T = w.suffix_tree()
            sage: T.LZ_decomposition()
            [0, 1, 4, 5, 9, 10]
        """
    def suffix_walk(self, edge, l):
        '''
        Return the state of "w" if the input state is "aw".

        If the input state ``(edge, l)`` is path labeled "aw" with "a" a letter, the output is
        the state which is path labeled "w".

        INPUT:

        - ``edge`` -- the edge containing the state
        - ``l`` -- the string-depth of the state on edge (``l``>0)

        OUTPUT:

        Return ``("explicit", end_node)`` if the state of w is an explicit
        state and ``("implicit", edge, d)`` is obtained by reading ``d``
        letters on ``edge``.

        EXAMPLES::

            sage: T = Word(\'00110111011\').suffix_tree()
            sage: T.suffix_walk((0, 5), 1)
            (\'explicit\', 0)
            sage: T.suffix_walk((7, 3), 1)
            (\'implicit\', (9, 4), 1)
        '''
    def leftmost_covering_set(self):
        """
        Compute the leftmost covering set of square pairs in ``self.word()``.
        Return a square as a pair ``(i,l)`` designating factor
        ``self.word()[i:i+l]``.

        A  leftmost covering set is a set such that the leftmost occurrence
        `(j,l)` of a square in ``self.word()`` is covered by a pair
        `(i,l)` in the set for all types of squares. We say that `(j,l)` is
        covered by `(i,l)` if `(i,l)` (i+1,l), \\ldots, (j,l)` are all
        squares.

        The set is returned in the form of a list ``P`` such that ``P[i]``
        contains all the lengths of squares starting at ``i`` in the set.
        The lists ``P[i]`` are sorted in decreasing order.

        The algorithm used is described in [DS2004]_.

        EXAMPLES::

            sage: w = Word('abaabaabbaaabaaba')
            sage: T = w.suffix_tree()
            sage: T.leftmost_covering_set()
            [[6], [6], [2], [], [], [], [], [2], [], [], [6, 2], [], [], [], [], [], []]
            sage: w = Word('abaca')
            sage: T = w.suffix_tree()
            sage: T.leftmost_covering_set()
            [[], [], [], [], []]
            sage: T = Word('aaaaa').suffix_tree()
            sage: T.leftmost_covering_set()
            [[4, 2], [], [], [], []]
        """
    def uncompactify(self):
        '''
        Return the tree obtained from ``self`` by splitting edges so that they
        are labelled by exactly one letter.

        The resulting tree is isomorphic to the suffix trie.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie
            sage: abbab = Words("ab")("abbab")
            sage: s = SuffixTrie(abbab)
            sage: t = ImplicitSuffixTree(abbab)
            sage: t.uncompactify().is_isomorphic(s.to_digraph())                        # needs sage.graphs
            True
        '''
    def trie_type_dict(self):
        '''
        Return a dictionary in a format compatible with that of the suffix
        trie transition function.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie
            sage: W = Words("ab")
            sage: t = ImplicitSuffixTree(W("aba"))
            sage: d = t.trie_type_dict()
            sage: len(d)
            5
            sage: d                     # random
            {(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
        '''

class DecoratedSuffixTree(ImplicitSuffixTree):
    """
    The decorated suffix tree of a word.

    A *decorated suffix tree* of a word `w` is the suffix tree of `w`
    marked with the end point of all squares in the `w`.

    The symbol ``$`` is appended to ``w`` to ensure that each final
    state is a leaf of the suffix tree.

    INPUT:

    - ``w`` -- a finite word

    EXAMPLES::

        sage: from sage.combinat.words.suffix_trees import DecoratedSuffixTree
        sage: w = Word('0011001')
        sage: DecoratedSuffixTree(w)
        Decorated suffix tree of : 0011001$
        sage: w = Word('0011001', '01')
        sage: DecoratedSuffixTree(w)
        Decorated suffix tree of : 0011001$

    ALGORITHM:

    When using ``'pair'`` as output, the squares are retrieved in linear
    time. The algorithm is an implementation of the one proposed in
    [DS2004]_.
    """
    labeling: Incomplete
    def __init__(self, w) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import DecoratedSuffixTree
            sage: w = Word('0011001')
            sage: DST = DecoratedSuffixTree(w)

        We skip the ``_test_and_split`` test because it is not a test meant
        for the ``TestSuite``::

            sage: TestSuite(DST).run(skip='_test_and_split')

        Test that we do not allow ``'$'`` to appear in the word::

            sage: w = Word('0011001$')
            sage: DecoratedSuffixTree(w)
            Traceback (most recent call last):
            ...
            ValueError: the symbol '$' is reserved for this class
        """
    def square_vocabulary(self, output: str = 'pair'):
        """
        Return the list of distinct squares of ``self.word``.

        Two types of outputs are available `pair` and `word`. The algorithm
        is only truly linear if `output` is set to `pair`. A pair is a tuple
        `(i, l)` that indicates the factor ``self.word()[i:i+l]``.
        The option ``'word'`` return word objects.

        INPUT:

        - ``output`` -- (default: ``'pair'``) either ``'pair'`` or ``'word'``

        EXAMPLES::

            sage: from sage.combinat.words.suffix_trees import DecoratedSuffixTree
            sage: w = Word('aabb')
            sage: sorted(DecoratedSuffixTree(w).square_vocabulary())
            [(0, 0), (0, 2), (2, 2)]
            sage: w = Word('00110011010')
            sage: sorted(DecoratedSuffixTree(w).square_vocabulary(output='word'))
            [word: , word: 00, word: 00110011, word: 01100110, word: 1010, word: 11]
        """
