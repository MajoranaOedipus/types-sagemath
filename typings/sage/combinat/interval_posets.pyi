from _typeshed import Incomplete
from collections.abc import Iterator
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.finite_posets import FinitePosets as FinitePosets
from sage.categories.monoids import Monoids as Monoids
from sage.categories.posets import Posets as Posets
from sage.combinat.binary_tree import BinaryTrees as BinaryTrees, LabelledBinaryTree as LabelledBinaryTree, LabelledBinaryTrees as LabelledBinaryTrees
from sage.combinat.permutation import Permutation as Permutation
from sage.combinat.posets.posets import FinitePoset as FinitePoset, Poset as Poset
from sage.graphs.digraph import DiGraph as DiGraph
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.latex import latex as latex
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.semirings.non_negative_integer_semiring import NN as NN
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.element import Element as Element
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TamariIntervalPoset(Element, metaclass=InheritComparisonClasscallMetaclass):
    '''
    The class of Tamari interval-posets.

    An interval-poset is a labelled poset of size `n`, with labels
    `1, 2, \\ldots, n`, satisfying the following conditions:

    - if `a < c` (as integers) and `a` precedes `c` in the poset, then,
      for all `b` such that `a < b < c`, `b` precedes `c`,

    - if `a < c` (as integers) and `c` precedes `a` in the poset, then,
      for all `b` such that `a < b < c`, `b` precedes `a`.

    We use the word "precedes" here to distinguish the poset order and
    the natural order on numbers. "Precedes" means "is smaller than
    with respect to the poset structure"; this does not imply a
    covering relation.

    Interval-posets of size `n` are in bijection with intervals of
    the Tamari lattice of binary trees of size `n`. Specifically, if
    `P` is an interval-poset of size `n`, then the set of linear
    extensions of `P` (as permutations in `S_n`) is an interval in the
    right weak order (see
    :meth:`~sage.combinat.permutation.Permutation.permutohedron_lequal`),
    and is in fact the preimage of an interval in the Tamari lattice (of
    binary trees of size `n`) under the operation which sends a
    permutation to its right-to-left binary search tree
    (:meth:`~sage.combinat.permutation.Permutation.binary_search_tree`
    with the ``left_to_right`` variable set to ``False``)
    without its labelling.

    INPUT:

    - ``size`` -- integer; the size of the interval-posets (number of
      vertices)

    - ``relations`` -- list (or tuple) of pairs ``(a,b)`` (themselves
      lists or tuples), each representing a relation of the form
      \'`a` precedes `b`\' in the poset

    - ``check`` -- boolean (default: ``True``); whether to check the
      interval-poset condition or not

    .. WARNING::

        The ``relations`` input can be a list or tuple, but not an
        iterator (nor should its entries be iterators).

    NOTATION:

    Here and in the following, the signs `<` and `>` always refer to
    the natural ordering on integers, whereas the word "precedes" refers
    to the order of the interval-poset. "Minimal" and "maximal" refer
    to the natural ordering on integers.

    The *increasing relations* of an interval-poset `P` mean the pairs
    `(a, b)` of elements of `P` such that `a < b` as integers and `a`
    precedes `b` in `P`. The *initial forest* of `P` is the poset
    obtained by imposing (only) the increasing relations on the ground
    set of `P`. It is a sub-interval poset of `P`, and is a forest with
    its roots on top. This forest is usually given the structure of a
    planar forest by ordering brother nodes by their labels; it then has
    the property that if its nodes are traversed in post-order
    (see :meth:`~sage.combinat.abstract_tree.AbstractTree.post_order_traversal`,
    and traverse the trees of the forest from left to right as well),
    then the labels encountered are `1, 2, \\ldots, n` in this order.

    The *decreasing relations* of an interval-poset `P` mean the pairs
    `(a, b)` of elements of `P` such that `b < a` as integers and `a`
    precedes `b` in `P`. The *final forest* of `P` is the poset
    obtained by imposing (only) the decreasing relations on the ground
    set of `P`. It is a sub-interval poset of `P`, and is a forest with
    its roots on top. This forest is usually given the structure of a
    planar forest by ordering brother nodes by their labels; it then has
    the property that if its nodes are traversed in pre-order
    (see :meth:`~sage.combinat.abstract_tree.AbstractTree.pre_order_traversal`,
    and traverse the trees of the forest from left to right as well),
    then the labels encountered are `1, 2, \\ldots, n` in this order.

    EXAMPLES::

        sage: TamariIntervalPoset(0,[])
        The Tamari interval of size 0 induced by relations []
        sage: TamariIntervalPoset(3,[])
        The Tamari interval of size 3 induced by relations []
        sage: TamariIntervalPoset(3,[(1,2)])
        The Tamari interval of size 3 induced by relations [(1, 2)]
        sage: TamariIntervalPoset(3,[(1,2),(2,3)])
        The Tamari interval of size 3 induced by relations [(1, 2), (2, 3)]
        sage: TamariIntervalPoset(3,[(1,2),(2,3),(1,3)])
        The Tamari interval of size 3 induced by relations [(1, 2), (2, 3)]
        sage: TamariIntervalPoset(3,[(1,2),(3,2)])
        The Tamari interval of size 3 induced by relations [(1, 2), (3, 2)]
        sage: TamariIntervalPoset(3,[[1,2],[2,3]])
        The Tamari interval of size 3 induced by relations [(1, 2), (2, 3)]
        sage: TamariIntervalPoset(3,[[1,2],[2,3],[1,2],[1,3]])
        The Tamari interval of size 3 induced by relations [(1, 2), (2, 3)]

        sage: TamariIntervalPoset(3,[(3,4)])
        Traceback (most recent call last):
        ...
        ValueError: the relations do not correspond to the size of the poset

        sage: TamariIntervalPoset(2,[(2,1),(1,2)])
        Traceback (most recent call last):
        ...
        ValueError: The graph is not directed acyclic

        sage: TamariIntervalPoset(3,[(1,3)])
        Traceback (most recent call last):
        ...
        ValueError: this does not satisfy the Tamari interval-poset condition

    It is also possible to transform a poset directly into an interval-poset::

        sage: TIP = TamariIntervalPosets()
        sage: p = Poset(([1,2,3], [(1,2)]))
        sage: TIP(p)
        The Tamari interval of size 3 induced by relations [(1, 2)]
        sage: TIP(Poset({1: []}))
        The Tamari interval of size 1 induced by relations []
        sage: TIP(Poset({}))
        The Tamari interval of size 0 induced by relations []
    '''
    @staticmethod
    def __classcall_private__(cls, *args, **opts) -> TIP:
        """
        Ensure that interval-posets created by the enumerated sets and
        directly are the same and that they are instances of
        :class:`TamariIntervalPoset`.

        TESTS::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.parent()
            Interval-posets
            sage: type(ip)
            <class 'sage.combinat.interval_posets.TamariIntervalPosets_all_with_category.element_class'>

            sage: ip2 = TamariIntervalPosets()(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip2.parent() is ip.parent()
            True
            sage: type(ip) is type(ip2)
            True

            sage: ip3 = TamariIntervalPosets(4)([(2,4),(3,4),(2,1),(3,1)])
            sage: ip3.parent() is ip.parent()
            False
            sage: type(ip3) is type(ip)
            True
        """
    def __init__(self, parent, size, relations=None, check: bool = True) -> None:
        """
        TESTS::

            sage: TamariIntervalPoset(3,[(1,2),(3,2)]).parent()
            Interval-posets
            sage: P = Poset(DiGraph([(4,1),(3,1),(2,1)]))
            sage: TamariIntervalPoset(P).parent()
            Interval-posets
        """
    def set_latex_options(self, D) -> None:
        '''
        Set the latex options for use in the ``_latex_`` function.

        The default values are set in the ``__init__`` function.

        - ``tikz_scale`` -- (default: 1) scale for use with the tikz package

        - ``line_width`` -- (default: 1 * ``tikz_scale``) value representing the
          line width

        - ``color_decreasing`` -- (default: red) the color for decreasing
          relations

        - ``color_increasing`` -- (default: blue) the color for increasing
          relations

        - ``hspace`` -- (default: 1) the difference between horizontal
          coordinates of adjacent vertices

        - ``vspace`` -- (default: 1) the difference between vertical
          coordinates of adjacent vertices

        INPUT:

        - ``D`` -- dictionary with a list of latex parameters to change

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.latex_options()["color_decreasing"]
            \'red\'
            sage: ip.set_latex_options({"color_decreasing":\'green\'})
            sage: ip.latex_options()["color_decreasing"]
            \'green\'
            sage: ip.set_latex_options({"color_increasing":\'black\'})
            sage: ip.latex_options()["color_increasing"]
            \'black\'

        To change the default options for all interval-posets, use the
        parent\'s latex options::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip2 = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.latex_options()["color_decreasing"]
            \'red\'
            sage: ip2.latex_options()["color_decreasing"]
            \'red\'
            sage: TamariIntervalPosets.options(latex_color_decreasing=\'green\')
            sage: ip.latex_options()["color_decreasing"]
            \'green\'
            sage: ip2.latex_options()["color_decreasing"]
            \'green\'

        Next we set a local latex option and show the global option does not
        override it::

            sage: ip.set_latex_options({"color_decreasing": \'black\'})
            sage: ip.latex_options()["color_decreasing"]
            \'black\'
            sage: TamariIntervalPosets.options(latex_color_decreasing=\'blue\')
            sage: ip.latex_options()["color_decreasing"]
            \'black\'
            sage: ip2.latex_options()["color_decreasing"]
            \'blue\'
            sage: TamariIntervalPosets.options._reset()
        '''
    def latex_options(self) -> dict:
        """
        Return the latex options for use in the ``_latex_`` function as a
        dictionary.

        The default values are set using the options.

        - ``tikz_scale`` -- (default: 1) scale for use with the tikz package

        - ``line_width`` -- (default: 1) value representing the line width
          (additionally scaled by ``tikz_scale``)

        - ``color_decreasing`` -- (default: ``'red'``) the color for
          decreasing relations

        - ``color_increasing`` -- (default: ``'blue'``) the color for
          increasing relations

        - ``hspace`` -- (default: 1) the difference between horizontal
          coordinates of adjacent vertices

        - ``vspace`` -- (default: 1) the difference between vertical
          coordinates of adjacent vertices

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.latex_options()['color_decreasing']
            'red'
            sage: ip.latex_options()['hspace']
            1
        """
    def plot(self, **kwds):
        """
        Return a picture.

        The picture represents the Hasse diagram, where the covers are
        colored in blue if they are increasing and in red if they are
        decreasing.

        This uses the same coordinates as the latex view.

        EXAMPLES::

            sage: ti = TamariIntervalPosets(4)[2]
            sage: ti.plot()                                                             # needs sage.plot
            Graphics object consisting of 6 graphics primitives

        TESTS::

            sage: ti = TamariIntervalPoset(3, [[2,1], [2,3]])
            sage: ti.plot()                                                             # needs sage.plot
            Graphics object consisting of 6 graphics primitives
        """
    def poset(self) -> FinitePoset:
        """
        Return ``self`` as a labelled poset.

        An interval-poset is indeed constructed from a labelled poset which
        is stored internally. This method allows to access the poset and
        all the associated methods.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(3,2),(2,4),(3,4)])
            sage: pos = ip.poset(); pos
            Finite poset containing 4 elements
            sage: pos.maximal_chains()
            [[3, 2, 4], [1, 2, 4]]
            sage: pos.maximal_elements()
            [4]
            sage: pos.is_lattice()
            False
        """
    def factor(self) -> list[TamariIntervalPoset]:
        """
        Return the unique decomposition as a list of connected components.

        EXAMPLES::

            sage: factor(TamariIntervalPoset(2,[]))  # indirect doctest
            [The Tamari interval of size 1 induced by relations [],
             The Tamari interval of size 1 induced by relations []]

        .. SEEALSO:: :meth:`is_connected`

        TESTS::

            sage: # needs sage.combinat
            sage: T = TamariIntervalPosets(20).random_element()
            sage: facs = factor(T)
            sage: all(U.is_connected() for U in facs)
            True
            sage: T == prod(facs)
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: len(set(hash(u) for u in TamariIntervalPosets(4)))
            68
        """
    @cached_method
    def increasing_cover_relations(self) -> list[tuple[int, int]]:
        """
        Return the cover relations of the initial forest of ``self``.

        This is the poset formed by keeping only the relations of the form
        `a` precedes `b` with `a < b`.

        The initial forest of ``self`` is a forest with its roots
        being on top. It is also called the increasing poset of ``self``.

        .. WARNING::

            This method computes the cover relations of the initial
            forest. This is not identical with the cover relations of
            ``self`` which happen to be increasing!

        .. SEEALSO::

            :meth:`initial_forest`

        EXAMPLES::

            sage: TamariIntervalPoset(4,[(1,2),(3,2),(2,4),(3,4)]).increasing_cover_relations()
            [(1, 2), (2, 4), (3, 4)]
            sage: TamariIntervalPoset(3,[(1,2),(1,3),(2,3)]).increasing_cover_relations()
            [(1, 2), (2, 3)]
        """
    def increasing_roots(self) -> list[int]:
        """
        Return the root vertices of the initial forest of ``self``.

        These are the vertices `a` of ``self`` such that there is no
        `b > a` with `a` precedes `b`.

        OUTPUT:

        The list of all roots of the initial forest of ``self``, in
        decreasing order.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.increasing_roots()
            [6, 5, 2]
            sage: ip.initial_forest().increasing_roots()
            [6, 5, 2]

        TESTS::

            sage: TamariIntervalPoset(0,[]).increasing_roots()
            []
        """
    def increasing_children(self, v) -> list[int]:
        """
        Return the children of ``v`` in the initial forest of ``self``.

        INPUT:

        - ``v`` -- integer representing a vertex of ``self``
          (between 1 and ``size``)

        OUTPUT:

        The list of all children of ``v`` in the initial forest of
        ``self``, in decreasing order.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.increasing_children(2)
            [1]
            sage: ip.increasing_children(5)
            [4, 3]
            sage: ip.increasing_children(1)
            []
        """
    def increasing_parent(self, v) -> None | int:
        """
        Return the vertex parent of ``v`` in the initial forest of ``self``.

        This is the lowest (as integer!) vertex `b > v` such that `v`
        precedes `b`. If there is no such vertex (that is, `v` is an
        increasing root), then ``None`` is returned.

        INPUT:

        - ``v`` -- integer representing a vertex of ``self``
          (between 1 and ``size``)

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.increasing_parent(1)
            2
            sage: ip.increasing_parent(3)
            5
            sage: ip.increasing_parent(4)
            5
            sage: ip.increasing_parent(5) is None
            True
        """
    @cached_method
    def decreasing_cover_relations(self) -> list[tuple[int, int]]:
        """
        Return the cover relations of the final forest of ``self``.

        This is the poset formed by keeping only the relations of the form
        `a` precedes `b` with `a > b`.

        The final forest of ``self`` is a forest with its roots
        being on top. It is also called the decreasing poset of ``self``.

        .. WARNING::

            This method computes the cover relations of the final
            forest. This is not identical with the cover relations of
            ``self`` which happen to be decreasing!

        .. SEEALSO::

            :meth:`final_forest`

        EXAMPLES::

            sage: TamariIntervalPoset(4,[(2,1),(3,2),(3,4),(4,2)]).decreasing_cover_relations()
            [(4, 2), (3, 2), (2, 1)]
            sage: TamariIntervalPoset(4,[(2,1),(4,3),(2,3)]).decreasing_cover_relations()
            [(4, 3), (2, 1)]
            sage: TamariIntervalPoset(3,[(2,1),(3,1),(3,2)]).decreasing_cover_relations()
            [(3, 2), (2, 1)]
        """
    def decreasing_roots(self) -> list[int]:
        """
        Return the root vertices of the final forest of ``self``.

        These are the vertices `b` such that there is no `a < b` with `b`
        preceding `a`.

        OUTPUT:

        The list of all roots of the final forest of ``self``, in
        increasing order.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.decreasing_roots()
            [1, 2]
            sage: ip.final_forest().decreasing_roots()
            [1, 2]
        """
    def decreasing_children(self, v) -> list[int]:
        """
        Return the children of ``v`` in the final forest of ``self``.

        INPUT:

        - ``v`` -- integer representing a vertex of ``self``
          (between 1 and ``size``)

        OUTPUT:

        The list of all children of ``v`` in the final forest of ``self``,
        in increasing order.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.decreasing_children(2)
            [3, 5]
            sage: ip.decreasing_children(3)
            [4]
            sage: ip.decreasing_children(1)
            []
        """
    def decreasing_parent(self, v) -> None | int:
        """
        Return the vertex parent of ``v`` in the final forest of ``self``.

        This is the highest (as integer!) vertex `a < v` such that ``v``
        precedes ``a``. If there is no such vertex (that is, `v` is a
        decreasing root), then ``None`` is returned.

        INPUT:

        - ``v`` -- integer representing a vertex of ``self`` (between
          1 and ``size``)

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.decreasing_parent(4)
            3
            sage: ip.decreasing_parent(3)
            2
            sage: ip.decreasing_parent(5)
            2
            sage: ip.decreasing_parent(2) is None
            True
        """
    def le(self, e1, e2) -> bool:
        """
        Return whether ``e1`` precedes or equals ``e2`` in ``self``.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.le(1,2)
            True
            sage: ip.le(1,3)
            True
            sage: ip.le(2,3)
            True
            sage: ip.le(3,4)
            False
            sage: ip.le(1,1)
            True
        """
    def lt(self, e1, e2) -> bool:
        """
        Return whether ``e1`` strictly precedes ``e2`` in ``self``.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.lt(1,2)
            True
            sage: ip.lt(1,3)
            True
            sage: ip.lt(2,3)
            True
            sage: ip.lt(3,4)
            False
            sage: ip.lt(1,1)
            False
        """
    def ge(self, e1, e2) -> bool:
        """
        Return whether ``e2`` precedes or equals ``e1`` in ``self``.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.ge(2,1)
            True
            sage: ip.ge(3,1)
            True
            sage: ip.ge(3,2)
            True
            sage: ip.ge(4,3)
            False
            sage: ip.ge(1,1)
            True
        """
    def gt(self, e1, e2) -> bool:
        """
        Return whether ``e2`` strictly precedes ``e1`` in ``self``.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.gt(2,1)
            True
            sage: ip.gt(3,1)
            True
            sage: ip.gt(3,2)
            True
            sage: ip.gt(4,3)
            False
            sage: ip.gt(1,1)
            False
        """
    def size(self) -> Integer:
        """
        Return the size (number of vertices) of the interval-poset.

        EXAMPLES::

            sage: TamariIntervalPoset(3,[(2,1),(3,1)]).size()
            3
        """
    @cached_method
    def cubical_coordinates(self) -> tuple[int, ...]:
        """
        Return the cubical coordinates of ``self``.

        This provides a fast and natural way to order
        the set of interval-posets of a given size.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.cubical_coordinates()
            (-1, -2, 0)

        TESTS::

            sage: ip = TamariIntervalPoset(1,[])
            sage: ip.cubical_coordinates()
            ()
            sage: ip = TamariIntervalPoset(3,[])
            sage: ip.cubical_coordinates()
            (0, 0)
            sage: ip = TamariIntervalPosets(10).random_element()                        # needs sage.combinat
            sage: len(ip.cubical_coordinates())                                         # needs sage.combinat
            9
            sage: sorted(ip.cubical_coordinates() for ip in TamariIntervalPosets(2))    # needs sage.combinat
            [(-1,), (0,), (1,)]

        REFERENCES:

        - [Com2019]_
        """
    def complement(self) -> TIP:
        """
        Return the complement of the interval-poset ``self``.

        If `P` is a Tamari interval-poset of size `n`, then the
        *complement* of `P` is defined as the interval-poset `Q` whose
        base set is `[n] = \\{1, 2, \\ldots, n\\}` (just as for `P`), but
        whose order relation has `a` precede `b` if and only if
        `n + 1 - a` precedes `n + 1 - b` in `P`.

        In terms of the Tamari lattice, the *complement* is the symmetric
        of ``self``. It is formed from the left-right symmetrized of
        the binary trees of the interval (switching left and right
        subtrees, see
        :meth:`~sage.combinat.binary_tree.BinaryTree.left_right_symmetry`).
        In particular, initial intervals are sent to final intervals and
        vice-versa.

        EXAMPLES::

            sage: TamariIntervalPoset(3, [(2, 1), (3, 1)]).complement()
            The Tamari interval of size 3 induced by relations [(1, 3), (2, 3)]
            sage: TamariIntervalPoset(0, []).complement()
            The Tamari interval of size 0 induced by relations []
            sage: ip = TamariIntervalPoset(4, [(1, 2), (2, 4), (3, 4)])
            sage: ip.complement() == TamariIntervalPoset(4, [(2, 1), (3, 1), (4, 3)])
            True
            sage: ip.lower_binary_tree() == ip.complement().upper_binary_tree().left_right_symmetry()
            True
            sage: ip.upper_binary_tree() == ip.complement().lower_binary_tree().left_right_symmetry()
            True
            sage: ip.is_initial_interval()
            True
            sage: ip.complement().is_final_interval()
            True
        """
    def left_branch_involution(self) -> TIP:
        """
        Return the image of ``self`` by the left-branch involution.

        OUTPUT: an interval-poset

        .. SEEALSO:: :meth:`rise_contact_involution`

        EXAMPLES::

            sage: tip = TamariIntervalPoset(8, [(1,2), (2,4), (3,4), (6,7), (3,2), (5,4), (6,4), (8,7)])
            sage: t = tip.left_branch_involution(); t
            The Tamari interval of size 8 induced by relations [(1, 6), (2, 6),
            (3, 5), (4, 5), (5, 6), (6, 8), (7, 8), (7, 6), (4, 3), (3, 1),
            (2, 1)]
            sage: t.left_branch_involution() == tip
            True

        REFERENCES:

        - [Pons2018]_
        """
    def rise_contact_involution(self) -> TIP:
        """
        Return the image of ``self`` by the rise-contact involution.

        OUTPUT: an interval-poset

        This is defined by conjugating the complement involution
        by the left-branch involution.

        .. SEEALSO:: :meth:`left_branch_involution`, :meth:`complement`

        EXAMPLES::

            sage: tip = TamariIntervalPoset(8, [(1,2), (2,4), (3,4), (6,7),
            ....:                               (3,2), (5,4), (6,4), (8,7)])
            sage: t = tip.rise_contact_involution(); t
            The Tamari interval of size 8 induced by relations [(2, 8), (3, 8),
            (4, 5), (5, 7), (6, 7), (7, 8), (8, 1), (7, 2), (6, 2), (5, 3),
            (4, 3), (3, 2), (2, 1)]
            sage: t.rise_contact_involution() == tip
            True
            sage: (tip.lower_dyck_word().number_of_touch_points()                       # needs sage.combinat
            ....:     == t.upper_dyck_word().number_of_initial_rises())
            True
            sage: tip.number_of_tamari_inversions() == t.number_of_tamari_inversions()
            True

        REFERENCES:

        - [Pons2018]_
        """
    def insertion(self, i) -> TIP:
        '''
        Return the Tamari insertion of an integer `i` into the
        interval-poset ``self``.

        If `P` is a Tamari interval-poset of size `n` and `i` is an
        integer with `1 \\leq i \\leq n+1`, then the Tamari insertion of
        `i` into `P` is defined as the Tamari interval-poset of size
        `n+1` which corresponds to the interval `[C_1, C_2]` on the
        Tamari lattice, where the binary trees `C_1` and `C_2` are
        defined as follows: We write the interval-poset `P` as
        `[B_1, B_2]` for two binary trees `B_1` and `B_2`. We label
        the vertices of each of these two trees with the integers
        `1, 2, \\ldots, i-1, i+1, i+2, \\ldots, n+1` in such a way that
        the trees are binary search trees (this labelling is unique).
        Then, we insert `i` into each of these trees (in the way as
        explained in
        :meth:`~sage.combinat.binary_tree.LabelledBinaryTree.binary_search_insert`).
        The shapes of the resulting two trees are denoted `C_1` and
        `C_2`.

        An alternative way to construct the insertion of `i` into
        `P` is by relabeling each vertex `u` of `P` satisfying
        `u \\geq i` (as integers) as `u+1`, and then adding a vertex
        `i` which should precede `i-1` and `i+1`.

        .. TODO::

            To study this, it would be more natural to define
            interval-posets on arbitrary ordered sets rather than just
            on `\\{1, 2, \\ldots, n\\}`.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4, [(2, 3), (4, 3)]); ip
            The Tamari interval of size 4 induced by relations [(2, 3), (4, 3)]
            sage: ip.insertion(1)
            The Tamari interval of size 5 induced by relations [(1, 2), (3, 4), (5, 4)]
            sage: ip.insertion(2)
            The Tamari interval of size 5 induced by relations [(2, 3), (3, 4), (5, 4), (2, 1)]
            sage: ip.insertion(3)
            The Tamari interval of size 5 induced by relations [(2, 4), (3, 4), (5, 4), (3, 2)]
            sage: ip.insertion(4)
            The Tamari interval of size 5 induced by relations [(2, 3), (4, 5), (5, 3), (4, 3)]
            sage: ip.insertion(5)
            The Tamari interval of size 5 induced by relations [(2, 3), (5, 4), (4, 3)]

            sage: ip = TamariIntervalPoset(0, [])
            sage: ip.insertion(1)
            The Tamari interval of size 1 induced by relations []

            sage: ip = TamariIntervalPoset(1, [])
            sage: ip.insertion(1)
            The Tamari interval of size 2 induced by relations [(1, 2)]
            sage: ip.insertion(2)
            The Tamari interval of size 2 induced by relations [(2, 1)]

        TESTS:

        Verifying that the two ways of computing insertion are
        equivalent::

            sage: def insert_alternative(T, i):
            ....:     # Just another way to compute the insertion of i into T.
            ....:     from sage.combinat.binary_tree import LabelledBinaryTree
            ....:     B1 = T.lower_binary_tree().canonical_labelling()
            ....:     B2 = T.upper_binary_tree().canonical_labelling()
            ....:     C1 = B1.binary_search_insert(i)
            ....:     C2 = B2.binary_search_insert(i)
            ....:     return TamariIntervalPosets.from_binary_trees(C1, C2)

        We should have relabelled the trees to "make space" for a label i,
        but we did not, because it does not make a difference: The
        binary search insertion will go precisely the same, because
        an integer equal to the label of the root gets sent onto
        the left branch.

            sage: def test_equivalence(n):
            ....:     for T in TamariIntervalPosets(n):
            ....:         for i in range(1, n + 2):
            ....:             if insert_alternative(T, i) != T.insertion(i):
            ....:                 print(T, i)
            ....:                 return False
            ....:     return True
            sage: test_equivalence(3)                                                   # needs sage.combinat
            True

            sage: ti = TamariIntervalPosets(3).an_element()
            sage: ti.insertion(6)
            Traceback (most recent call last):
            ...
            ValueError: integer to be inserted not in the appropriate interval
        '''
    def __iter__(self) -> Iterator[int]:
        """
        Iterate through the vertices of ``self``.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(3,2)])
            sage: [i for i in ip]
            [1, 2, 3, 4]
        """
    def contains_interval(self, other) -> bool:
        """
        Return whether the interval represented by ``other`` is contained
        in ``self`` as an interval of the Tamari lattice.

        In terms of interval-posets, it means that all relations of ``self``
        are relations of ``other``.

        INPUT:

        - ``other`` -- an interval-poset

        EXAMPLES::

            sage: ip1 = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip2 = TamariIntervalPoset(4,[(2,3)])
            sage: ip2.contains_interval(ip1)
            True
            sage: ip3 = TamariIntervalPoset(4,[(2,1)])
            sage: ip2.contains_interval(ip3)
            False
            sage: ip4 = TamariIntervalPoset(3,[(2,3)])
            sage: ip2.contains_interval(ip4)
            False
        """
    def lower_contains_interval(self, other) -> bool:
        """
        Return whether the interval represented by ``other`` is contained
        in ``self`` as an interval of the Tamari lattice and if they share
        the same lower bound.

        As interval-posets, it means that ``other`` contains the relations
        of ``self`` plus some extra increasing relations.

        INPUT:

        - ``other`` -- an interval-poset

        EXAMPLES::

            sage: ip1 = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip2 = TamariIntervalPoset(4,[(4,3)])
            sage: ip2.lower_contains_interval(ip1)
            True
            sage: ip2.contains_interval(ip1) and ip2.lower_binary_tree() == ip1.lower_binary_tree()
            True
            sage: ip3 = TamariIntervalPoset(4,[(4,3),(2,1)])
            sage: ip2.contains_interval(ip3)
            True
            sage: ip2.lower_binary_tree() == ip3.lower_binary_tree()
            False
            sage: ip2.lower_contains_interval(ip3)
            False

        TESTS::

            sage: ip1 = TamariIntervalPoset(3,[(1,2),(2,3)])
            sage: ip2 = TamariIntervalPoset(3,[(2,1),(3,2)])
            sage: ip2.lower_contains_interval(ip1)
            False
        """
    def upper_contains_interval(self, other) -> bool:
        """
        Return whether the interval represented by ``other`` is contained
        in ``self`` as an interval of the Tamari lattice and if they share
        the same upper bound.

        As interval-posets, it means that ``other`` contains the relations
        of ``self`` plus some extra decreasing relations.

        INPUT:

        - ``other`` -- an interval-poset

        EXAMPLES::

            sage: ip1 = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip2 = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip2.upper_contains_interval(ip1)
            True
            sage: ip2.contains_interval(ip1) and ip2.upper_binary_tree() == ip1.upper_binary_tree()
            True
            sage: ip3 = TamariIntervalPoset(4,[(1,2),(2,3),(3,4)])
            sage: ip2.upper_contains_interval(ip3)
            False
            sage: ip2.contains_interval(ip3)
            True
            sage: ip2.upper_binary_tree() == ip3.upper_binary_tree()
            False

        TESTS::

            sage: ip1 = TamariIntervalPoset(3,[(1,2),(2,3)])
            sage: ip2 = TamariIntervalPoset(3,[(2,1),(3,2)])
            sage: ip2.lower_contains_interval(ip1)
            False
        """
    def is_linear_extension(self, perm) -> bool:
        """
        Return whether the permutation ``perm`` is a linear extension
        of ``self``.

        INPUT:

        - ``perm`` -- a permutation of the size of ``self``

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip.is_linear_extension([1,4,2,3])
            True
            sage: ip.is_linear_extension(Permutation([1,4,2,3]))
            True
            sage: ip.is_linear_extension(Permutation([1,4,3,2]))
            False
        """
    def contains_binary_tree(self, binary_tree) -> bool:
        """
        Return whether the interval represented by ``self`` contains
        the binary tree ``binary_tree``.

        INPUT:

        - ``binary_tree`` -- a binary tree

        .. SEEALSO:: :meth:`contains_dyck_word`

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.contains_binary_tree(BinaryTree([[None,[None,[]]],None]))
            True
            sage: ip.contains_binary_tree(BinaryTree([None,[[[],None],None]]))
            True
            sage: ip.contains_binary_tree(BinaryTree([[],[[],None]]))
            False
            sage: ip.contains_binary_tree(ip.lower_binary_tree())
            True
            sage: ip.contains_binary_tree(ip.upper_binary_tree())
            True
            sage: all(ip.contains_binary_tree(bt) for bt in ip.binary_trees())
            True
        """
    def contains_dyck_word(self, dyck_word) -> bool:
        """
        Return whether the interval represented by ``self`` contains
        the Dyck word ``dyck_word``.

        INPUT:

        - ``dyck_word`` -- a Dyck word

        .. SEEALSO:: :meth:`contains_binary_tree`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.contains_dyck_word(DyckWord([1,1,1,0,0,0,1,0]))
            True
            sage: ip.contains_dyck_word(DyckWord([1,1,0,1,0,1,0,0]))
            True
            sage: ip.contains_dyck_word(DyckWord([1,0,1,1,0,1,0,0]))
            False
            sage: ip.contains_dyck_word(ip.lower_dyck_word())
            True
            sage: ip.contains_dyck_word(ip.upper_dyck_word())
            True
            sage: all(ip.contains_dyck_word(bt) for bt in ip.dyck_words())
            True
        """
    def intersection(self, other: TIP) -> TIP:
        """
        Return the interval-poset formed by combining the relations from
        both ``self`` and ``other``. It corresponds to the intersection
        of the two corresponding intervals of the Tamari lattice.

        INPUT:

        - ``other`` -- an interval-poset of the same size as ``self``

        EXAMPLES::

            sage: ip1 = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip2 = TamariIntervalPoset(4,[(4,3)])
            sage: ip1.intersection(ip2)
            The Tamari interval of size 4 induced by relations [(1, 2), (2, 3), (4, 3)]
            sage: ip3 = TamariIntervalPoset(4,[(2,1)])
            sage: ip1.intersection(ip3)
            Traceback (most recent call last):
            ...
            ValueError: this intersection is empty, it does not correspond to an interval-poset
            sage: ip4 = TamariIntervalPoset(3,[(2,3)])
            sage: ip2.intersection(ip4)
            Traceback (most recent call last):
            ...
            ValueError: intersections are only possible on interval-posets of the same size
        """
    def initial_forest(self) -> TIP:
        """
        Return the initial forest of ``self``, i.e., the interval-poset
        formed from only the increasing relations of ``self``.

        .. SEEALSO:: :meth:`final_forest`

        EXAMPLES::

            sage: TamariIntervalPoset(4,[(1,2),(3,2),(2,4),(3,4)]).initial_forest()
            The Tamari interval of size 4 induced by relations [(1, 2), (2, 4), (3, 4)]
            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: ip.initial_forest() == ip
            True
        """
    def final_forest(self) -> TIP:
        """
        Return the final forest of ``self``, i.e., the interval-poset
        formed with only the decreasing relations of ``self``.

        .. SEEALSO:: :meth:`initial_forest`

        EXAMPLES::

            sage: TamariIntervalPoset(4,[(2,1),(3,2),(3,4),(4,2)]).final_forest()
            The Tamari interval of size 4 induced by relations [(4, 2), (3, 2), (2, 1)]
            sage: ip = TamariIntervalPoset(3,[(2,1),(3,1)])
            sage: ip.final_forest() == ip
            True
        """
    def is_initial_interval(self) -> bool:
        """
        Return if ``self`` corresponds to an initial interval of the Tamari
        lattice.

        This means that its lower end is the smallest element of the lattice.
        It consists of checking that ``self`` does not contain any decreasing
        relations.

        .. SEEALSO:: :meth:`is_final_interval`

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4, [(1, 2), (2, 4), (3, 4)])
            sage: ip.is_initial_interval()
            True
            sage: ip.lower_dyck_word()                                                  # needs sage.combinat
            [1, 0, 1, 0, 1, 0, 1, 0]
            sage: ip = TamariIntervalPoset(4, [(1, 2), (2, 4), (3, 4), (3, 2)])
            sage: ip.is_initial_interval()
            False
            sage: ip.lower_dyck_word()                                                  # needs sage.combinat
            [1, 0, 1, 1, 0, 0, 1, 0]
            sage: all(DyckWord([1,0,1,0,1,0]).tamari_interval(dw)                       # needs sage.combinat
            ....:         .is_initial_interval()
            ....:     for dw in DyckWords(3))
            True
        """
    def is_final_interval(self) -> bool:
        """
        Return if ``self`` corresponds to a final interval of the Tamari
        lattice.

        This means that its upper end is the largest element of the lattice.
        It consists of checking that ``self`` does not contain any increasing
        relations.

        .. SEEALSO:: :meth:`is_initial_interval`

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4, [(4, 3), (3, 1), (2, 1)])
            sage: ip.is_final_interval()
            True
            sage: ip.upper_dyck_word()                                                  # needs sage.combinat
            [1, 1, 1, 1, 0, 0, 0, 0]
            sage: ip = TamariIntervalPoset(4, [(4, 3), (3, 1), (2, 1), (2, 3)])
            sage: ip.is_final_interval()
            False
            sage: ip.upper_dyck_word()                                                  # needs sage.combinat
            [1, 1, 0, 1, 1, 0, 0, 0]
            sage: all(dw.tamari_interval(DyckWord([1, 1, 1, 0, 0, 0]))                  # needs sage.combinat
            ....:            .is_final_interval()
            ....:     for dw in DyckWords(3))
            True
        """
    def lower_binary_tree(self):
        """
        Return the lowest binary tree in the interval of the Tamari
        lattice represented by ``self``.

        This is a binary tree. It is the shape of the unique binary
        search tree whose left-branch ordered forest (i.e., the result
        of applying
        :meth:`~sage.combinat.binary_tree.BinaryTree.to_ordered_tree_left_branch`
        and cutting off the root) is the final forest of ``self``.

        .. SEEALSO:: :meth:`lower_dyck_word`

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6, [(3,2),(4,3),(5,2),(6,5),(1,2),(4,5)]); ip
            The Tamari interval of size 6 induced by relations
             [(1, 2), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.lower_binary_tree()
            [[., .], [[., [., .]], [., .]]]
            sage: ff = TamariIntervalPosets.final_forest(ip.lower_binary_tree())
            sage: ff == ip.final_forest()
            True
            sage: ip == TamariIntervalPosets.from_binary_trees(ip.lower_binary_tree(),
            ....:                                              ip.upper_binary_tree())
            True
        """
    def lower_dyck_word(self):
        """
        Return the lowest Dyck word in the interval of the Tamari lattice
        represented by ``self``.

        .. SEEALSO:: :meth:`lower_binary_tree`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: ip = TamariIntervalPoset(6, [(3,2),(4,3),(5,2),(6,5),(1,2),(4,5)]); ip
            The Tamari interval of size 6 induced by relations
             [(1, 2), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.lower_dyck_word()
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0]
            sage: ldw_ff = TamariIntervalPosets.final_forest(ip.lower_dyck_word())
            sage: ldw_ff == ip.final_forest()
            True
            sage: ip == TamariIntervalPosets.from_dyck_words(ip.lower_dyck_word(),
            ....:                                            ip.upper_dyck_word())
            True
        """
    def upper_binary_tree(self):
        """
        Return the highest binary tree in the interval of the Tamari
        lattice represented by ``self``.

        This is a binary tree. It is the shape of the unique binary
        search tree whose right-branch ordered forest (i.e., the result
        of applying
        :meth:`~sage.combinat.binary_tree.BinaryTree.to_ordered_tree_right_branch`
        and cutting off the root) is the initial forest of ``self``.

        .. SEEALSO:: :meth:`upper_dyck_word`

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(4,5)]); ip
            The Tamari interval of size 6 induced by relations
             [(1, 2), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.upper_binary_tree()
            [[., .], [., [[., .], [., .]]]]

            sage: TamariIntervalPosets.initial_forest(ip.upper_binary_tree()) == ip.initial_forest()
            True
            sage: ip == TamariIntervalPosets.from_binary_trees(ip.lower_binary_tree(),ip.upper_binary_tree())
            True
        """
    def upper_dyck_word(self):
        """
        Return the highest Dyck word in the interval of the Tamari lattice
        represented by ``self``.

        .. SEEALSO:: :meth:`upper_binary_tree`

        EXAMPLES::

            sage: # needs sage.combinat
            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(4,5)]); ip
            The Tamari interval of size 6 induced by relations
             [(1, 2), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.upper_dyck_word()
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
            sage: udw_if = TamariIntervalPosets.initial_forest(ip.upper_dyck_word())
            sage: udw_if == ip.initial_forest()
            True
            sage: ip == TamariIntervalPosets.from_dyck_words(ip.lower_dyck_word(),
            ....:                                            ip.upper_dyck_word())
            True
        """
    def subposet(self, start, end) -> TIP:
        '''
        Return the renormalized subposet of ``self`` consisting solely
        of integers from ``start`` (inclusive) to ``end`` (not inclusive).

        "Renormalized" means that these integers are relabelled
        `1,2,\\ldots,k` in the obvious way (i.e., by subtracting
        ``start - 1``).

        INPUT:

        - ``start`` -- integer; the starting vertex (inclusive)
        - ``end`` -- integer; the ending vertex (not inclusive)

        EXAMPLES::

            sage: ip = TamariIntervalPoset(6, [(3,2),(4,3),(5,2),(6,5),(1,2),(3,5),(4,5)]); ip
            The Tamari interval of size 6 induced by relations
             [(1, 2), (3, 5), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.subposet(1,3)
            The Tamari interval of size 2 induced by relations [(1, 2)]
            sage: ip.subposet(1,4)
            The Tamari interval of size 3 induced by relations [(1, 2), (3, 2)]
            sage: ip.subposet(1,5)
            The Tamari interval of size 4 induced by relations [(1, 2), (4, 3), (3, 2)]
            sage: ip.subposet(1,7) == ip
            True
            sage: ip.subposet(1,1)
            The Tamari interval of size 0 induced by relations []

        TESTS::

            sage: ip.sub_poset(1,1)
            The Tamari interval of size 0 induced by relations []
            sage: ip = TamariIntervalPosets(4).an_element()
            sage: ip.subposet(2,9)
            Traceback (most recent call last):
            ...
            ValueError: invalid starting or ending value
        '''
    sub_poset = subposet
    def min_linear_extension(self) -> Permutation:
        """
        Return the minimal permutation for the right weak order which is
        a linear extension of ``self``.

        This is also the minimal permutation in the sylvester
        class of ``self.lower_binary_tree()`` and is a 312-avoiding
        permutation.

        The right weak order is also known as the right permutohedron
        order. See
        :meth:`~sage.combinat.permutation.Permutation.permutohedron_lequal`
        for its definition.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip.min_linear_extension()
            [1, 2, 4, 3]
            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(4,5)])
            sage: ip.min_linear_extension()
            [1, 4, 3, 6, 5, 2]
            sage: ip = TamariIntervalPoset(0,[])
            sage: ip.min_linear_extension()
            []
            sage: ip = TamariIntervalPoset(5, [(1, 4), (2, 4), (3, 4), (5, 4)]); ip
            The Tamari interval of size 5 induced by relations [(1, 4), (2, 4), (3, 4), (5, 4)]
            sage: ip.min_linear_extension()
            [1, 2, 3, 5, 4]
        """
    def max_linear_extension(self) -> Permutation:
        """
        Return the maximal permutation for the right weak order which is
        a linear extension of ``self``.

        This is also the maximal permutation in the sylvester
        class of ``self.upper_binary_tree()`` and is a 132-avoiding
        permutation.

        The right weak order is also known as the right permutohedron
        order. See
        :meth:`~sage.combinat.permutation.Permutation.permutohedron_lequal`
        for its definition.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip.max_linear_extension()
            [4, 1, 2, 3]
            sage: ip = TamariIntervalPoset(6,[(3,2),(4,3),(5,2),(6,5),(1,2),(4,5)]); ip
            The Tamari interval of size 6 induced by relations [(1, 2), (4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: ip.max_linear_extension()
            [6, 4, 5, 3, 1, 2]
            sage: ip = TamariIntervalPoset(0,[]); ip
            The Tamari interval of size 0 induced by relations []
            sage: ip.max_linear_extension()
            []
            sage: ip = TamariIntervalPoset(5, [(1, 4), (2, 4), (3, 4), (5, 4)]); ip
            The Tamari interval of size 5 induced by relations [(1, 4), (2, 4), (3, 4), (5, 4)]
            sage: ip.max_linear_extension()
            [5, 3, 2, 1, 4]
        """
    def linear_extensions(self) -> Iterator[Permutation]:
        """
        Return an iterator on the permutations which are linear
        extensions of ``self``.

        They form an interval of the right weak order (also called the
        right permutohedron order -- see
        :meth:`~sage.combinat.permutation.Permutation.permutohedron_lequal`
        for a definition).

        EXAMPLES::

            sage: ip = TamariIntervalPoset(3, [(1,2),(3,2)])
            sage: list(ip.linear_extensions())                                          # needs sage.modules sage.rings.finite_rings
            [[3, 1, 2], [1, 3, 2]]
            sage: ip = TamariIntervalPoset(4, [(1,2),(2,3),(4,3)])
            sage: list(ip.linear_extensions())                                          # needs sage.modules sage.rings.finite_rings
            [[4, 1, 2, 3], [1, 2, 4, 3], [1, 4, 2, 3]]
        """
    def lower_contained_intervals(self) -> Iterator[TIP]:
        """
        If ``self`` represents the interval `[t_1, t_2]` of the Tamari
        lattice, return an iterator on all intervals `[t_1,t]` with
        `t \\leq t_2` for the Tamari lattice.

        In terms of interval-posets, it corresponds to adding all possible
        relations of the form `n` precedes `m` with `n<m`.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4, [(2,4),(3,4),(2,1),(3,1)])
            sage: list(ip.lower_contained_intervals())
            [The Tamari interval of size 4 induced by relations
              [(2, 4), (3, 4), (3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations
              [(1, 4), (2, 4), (3, 4), (3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations
              [(2, 3), (3, 4), (3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations
              [(1, 4), (2, 3), (3, 4), (3, 1), (2, 1)]]
            sage: ip = TamariIntervalPoset(4,[])
            sage: len(list(ip.lower_contained_intervals()))
            14
        """
    def interval_cardinality(self) -> Integer:
        """
        Return the cardinality of the interval, i.e., the number of elements
        (binary trees or Dyck words) in the interval represented by ``self``.

        Not to be confused with :meth:`size` which is the number of
        vertices.

        .. SEEALSO:: :meth:`binary_trees`

        EXAMPLES::

            sage: TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)]).interval_cardinality()
            4
            sage: TamariIntervalPoset(4,[]).interval_cardinality()
            14
            sage: TamariIntervalPoset(4,[(1,2),(2,3),(3,4)]).interval_cardinality()
            1
        """
    def binary_trees(self) -> Iterator:
        """
        Return an iterator on all the binary trees in the interval
        represented by ``self``.

        .. SEEALSO:: :meth:`interval_cardinality`

        EXAMPLES::

            sage: list(TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)]).binary_trees())
            [[., [[., [., .]], .]],
             [[., [., [., .]]], .],
             [., [[[., .], .], .]],
             [[., [[., .], .]], .]]
            sage: set(TamariIntervalPoset(4,[]).binary_trees()) == set(BinaryTrees(4))
            True
        """
    def dyck_words(self) -> Iterator:
        """
        Return an iterator on all the Dyck words in the interval
        represented by ``self``.

        EXAMPLES::

            sage: list(TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)]).dyck_words())   # needs sage.combinat
            [[1, 1, 1, 0, 0, 1, 0, 0],
             [1, 1, 1, 0, 0, 0, 1, 0],
             [1, 1, 0, 1, 0, 1, 0, 0],
             [1, 1, 0, 1, 0, 0, 1, 0]]
            sage: set(TamariIntervalPoset(4,[]).dyck_words()) == set(DyckWords(4))      # needs sage.combinat
            True
        """
    def maximal_chain_tamari_intervals(self) -> Iterator[TIP]:
        """
        Return an iterator on the upper contained intervals of one
        longest chain of the Tamari interval represented by ``self``.

        If ``self`` represents the interval `[T_1,T_2]` of the Tamari
        lattice, this returns intervals `[T',T_2]` with `T'` following
        one longest chain between `T_1` and `T_2`.

        To obtain a longest chain, we use the Tamari inversions of ``self``.
        The elements of the chain are obtained by adding one by one the
        relations `(b,a)` from each Tamari inversion `(a,b)` to ``self``,
        where the Tamari inversions are taken in lexicographic order.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4, [(2,4),(3,4),(2,1),(3,1)])
            sage: list(ip.maximal_chain_tamari_intervals())
            [The Tamari interval of size 4 induced by relations
              [(2, 4), (3, 4), (3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations
              [(2, 4), (3, 4), (4, 1), (3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations
              [(2, 4), (3, 4), (4, 1), (3, 2), (2, 1)]]
            sage: ip = TamariIntervalPoset(4, [])
            sage: list(ip.maximal_chain_tamari_intervals())
            [The Tamari interval of size 4 induced by relations [],
             The Tamari interval of size 4 induced by relations [(2, 1)],
             The Tamari interval of size 4 induced by relations [(3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations [(4, 1), (3, 1), (2, 1)],
             The Tamari interval of size 4 induced by relations [(4, 1), (3, 2), (2, 1)],
             The Tamari interval of size 4 induced by relations [(4, 2), (3, 2), (2, 1)],
             The Tamari interval of size 4 induced by relations [(4, 3), (3, 2), (2, 1)]]
        """
    def maximal_chain_binary_trees(self) -> Iterator:
        """
        Return an iterator on the binary trees forming a longest chain of
        ``self`` (regarding ``self`` as an interval of the Tamari
        lattice).

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: list(ip.maximal_chain_binary_trees())
            [[[., [[., .], .]], .], [., [[[., .], .], .]], [., [[., [., .]], .]]]
            sage: ip = TamariIntervalPoset(4,[])
            sage: list(ip.maximal_chain_binary_trees())
            [[[[[., .], .], .], .],
             [[[., [., .]], .], .],
             [[., [[., .], .]], .],
             [., [[[., .], .], .]],
             [., [[., [., .]], .]],
             [., [., [[., .], .]]],
             [., [., [., [., .]]]]]
        """
    def maximal_chain_dyck_words(self) -> Iterator:
        """
        Return an iterator on the Dyck words forming a longest chain of
        ``self`` (regarding ``self`` as an interval of the Tamari
        lattice).

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: list(ip.maximal_chain_dyck_words())                                   # needs sage.combinat
            [[1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 0]]
            sage: ip = TamariIntervalPoset(4,[])
            sage: list(ip.maximal_chain_dyck_words())                                   # needs sage.combinat
            [[1, 0, 1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 1, 0, 1, 0],
             [1, 1, 0, 1, 0, 0, 1, 0],
             [1, 1, 0, 1, 0, 1, 0, 0],
             [1, 1, 1, 0, 0, 1, 0, 0],
             [1, 1, 1, 0, 1, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0]]
        """
    def tamari_inversions(self) -> list[tuple[int, int]]:
        '''
        Return the Tamari inversions of ``self``.

        A Tamari inversion is
        a pair of vertices `(a,b)` with `a < b` such that:

        - the decreasing parent of `b` is strictly smaller than `a` (or
          does not exist), and
        - the increasing parent of `a` is strictly bigger than `b` (or
          does not exist).

        "Smaller" and "bigger" refer to the numerical values of the
        elements, not to the poset order.

        This method returns the list of all Tamari inversions in
        lexicographic order.

        The number of Tamari inversions is the length of the
        longest chain of the Tamari interval represented by ``self``.

        Indeed, when an interval consists of just one binary tree, it has
        no inversion. One can also prove that if a Tamari interval
        `I\' = [T_1\', T_2\']` is a proper subset of a Tamari interval
        `I = [T_1, T_2]`, then the inversion number of `I\'` is strictly
        lower than the inversion number of `I`. And finally, by adding
        the relation `(b,a)` to the interval-poset where `(a,b)` is the
        first inversion of `I` in lexicographic order, one reduces the
        inversion number by exactly `1`.

        .. SEEALSO::

            :meth:`tamari_inversions_iter`, :meth:`number_of_tamari_inversions`

        EXAMPLES::

            sage: ip = TamariIntervalPoset(3,[])
            sage: ip.tamari_inversions()
            [(1, 2), (1, 3), (2, 3)]
            sage: ip = TamariIntervalPoset(3,[(2,1)])
            sage: ip.tamari_inversions()
            [(1, 3), (2, 3)]
            sage: ip = TamariIntervalPoset(3,[(1,2)])
            sage: ip.tamari_inversions()
            [(2, 3)]
            sage: ip = TamariIntervalPoset(3,[(1,2),(3,2)])
            sage: ip.tamari_inversions()
            []
            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.tamari_inversions()
            [(1, 4), (2, 3)]
            sage: ip = TamariIntervalPoset(4,[])
            sage: ip.tamari_inversions()
            [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
            sage: all(not TamariIntervalPosets.from_binary_trees(bt,bt)                 # needs sage.combinat
            ....:                                  .tamari_inversions()
            ....:     for bt in BinaryTrees(3))
            True
            sage: all(not TamariIntervalPosets.from_binary_trees(bt,bt)                 # needs sage.combinat
            ....:                                  .tamari_inversions()
            ....:     for bt in BinaryTrees(4))
            True
        '''
    def tamari_inversions_iter(self) -> Iterator[tuple[int, int]]:
        """
        Iterate over the Tamari inversions of ``self``, in
        lexicographic order.

        See :meth:`tamari_inversions` for the definition of the terms
        involved.

        EXAMPLES::

            sage: T = TamariIntervalPoset(5, [[1,2],[3,4],[3,2],[5,2],[4,2]])
            sage: list(T.tamari_inversions_iter())
            [(4, 5)]

            sage: T = TamariIntervalPoset(8, [(2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
            ....:                             (8, 7), (6, 4), (5, 4), (4, 3), (3, 2)])
            sage: list(T.tamari_inversions_iter())
            [(1, 2), (1, 7), (5, 6)]

            sage: T = TamariIntervalPoset(1, [])
            sage: list(T.tamari_inversions_iter())
            []

            sage: T = TamariIntervalPoset(0, [])
            sage: list(T.tamari_inversions_iter())
            []
        """
    def number_of_tamari_inversions(self) -> Integer:
        """
        Return the number of Tamari inversions of ``self``.

        This is also the length the longest chain of the Tamari
        interval represented by ``self``.

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(2,4),(3,4),(2,1),(3,1)])
            sage: ip.number_of_tamari_inversions()
            2
            sage: ip = TamariIntervalPoset(4,[])
            sage: ip.number_of_tamari_inversions()
            6
            sage: ip = TamariIntervalPoset(3,[])
            sage: ip.number_of_tamari_inversions()
            3
        """
    def number_of_new_components(self) -> Integer:
        """
        Return the number of terms in the decomposition in new interval-posets.

        Every interval-poset has a unique decomposition as a planar tree
        of new interval-posets, as explained in [Cha2008]_. This function
        just computes the number of terms, not the planar tree nor
        the terms themselves.

        .. SEEALSO:: :meth:`is_new`, :meth:`new_decomposition`

        EXAMPLES::

            sage: TIP4 = TamariIntervalPosets(4)
            sage: nb = [u.number_of_new_components() for u in TIP4]
            sage: [nb.count(i) for i in range(1, 5)]
            [12, 21, 21, 14]
        """
    def new_decomposition(self) -> list[TIP]:
        """
        Return the decomposition of the interval-poset into
        new interval-posets.

        Every interval-poset has a unique decomposition as a planar
        tree of new interval-posets, as explained in
        [Cha2008]_. This function computes the terms of this
        decomposition, but not the planar tree.

        For the number of terms, you can use instead the method
        :meth:`number_of_new_components`.

        OUTPUT: list of new interval-posets

        .. SEEALSO::

            :meth:`number_of_new_components`, :meth:`is_new`

        EXAMPLES::

            sage: ex = TamariIntervalPosets(4)[11]
            sage: ex.number_of_new_components()
            3
            sage: ex.new_decomposition()                                                # needs sage.combinat
            [The Tamari interval of size 1 induced by relations [],
             The Tamari interval of size 2 induced by relations [],
             The Tamari interval of size 1 induced by relations []]

        TESTS::

            sage: # needs sage.combinat
            sage: ex = TamariIntervalPosets(4).random_element()
            sage: dec = ex.new_decomposition()
            sage: len(dec) == ex.number_of_new_components()
            True
            sage: all(u.is_new() for u in dec)
            True
        """
    def decomposition_to_triple(self) -> None | tuple[TIP, TIP, int]:
        """
        Decompose an interval-poset into a triple (``left``, ``right``, ``r``).

        For the inverse method, see
        :meth:`TamariIntervalPosets.recomposition_from_triple`.

        OUTPUT:

        a triple (``left``, ``right``, ``r``) where ``left`` and
        ``right`` are interval-posets and ``r`` (an integer) is the
        parameter of the decomposition.

        EXAMPLES::

            sage: tip = TamariIntervalPoset(8, [(1,2), (2,4), (3,4), (6,7),
            ....:                               (3,2), (5,4), (6,4), (8,7)])
            sage: tip.decomposition_to_triple()
            (The Tamari interval of size 3 induced by relations [(1, 2), (3, 2)],
             The Tamari interval of size 4 induced by relations [(2, 3), (4, 3)],
             2)
            sage: tip == TamariIntervalPosets.recomposition_from_triple(
            ....:            *tip.decomposition_to_triple())
            True

        TESTS::

            sage: tip = TamariIntervalPoset(0, [])
            sage: tip.decomposition_to_triple()

        REFERENCES:

        - [CP2015]_
        """
    def grafting_tree(self) -> LabelledBinaryTree:
        """
        Return the grafting tree of the interval-poset.

        For the inverse method,
        see :meth:`TamariIntervalPosets.from_grafting_tree`.

        EXAMPLES::

            sage: tip = TamariIntervalPoset(8, [(1,2), (2,4), (3,4), (6,7),
            ....:                               (3,2), (5,4), (6,4), (8,7)])
            sage: tip.grafting_tree()
            2[1[0[., .], 0[., .]], 0[., 1[0[., .], 0[., .]]]]
            sage: tip == TamariIntervalPosets.from_grafting_tree(tip.grafting_tree())
            True

        REFERENCES:

        - [Pons2018]_
        """
    def is_new(self) -> bool:
        """
        Return whether ``self`` is a new Tamari interval.

        Here 'new' means that the interval is not contained in any
        facet of the associahedron.
        This condition is invariant under complementation.

        They have been considered in section 9 of [Cha2008]_.

        .. SEEALSO:: :meth:`is_modern`

        EXAMPLES::

            sage: TIP4 = TamariIntervalPosets(4)
            sage: len([u for u in TIP4 if u.is_new()])
            12

            sage: TIP3 = TamariIntervalPosets(3)
            sage: len([u for u in TIP3 if u.is_new()])
            3
        """
    def is_simple(self) -> bool:
        """
        Return whether ``self`` is a simple Tamari interval.

        Here 'simple' means that the interval contains a unique binary tree.

        These intervals define the simple modules over the
        incidence algebras of the Tamari lattices.

        .. SEEALSO:: :meth:`is_final_interval`, :meth:`is_initial_interval`

        EXAMPLES::

            sage: TIP4 = TamariIntervalPosets(4)
            sage: len([u for u in TIP4 if u.is_simple()])
            14

            sage: TIP3 = TamariIntervalPosets(3)
            sage: len([u for u in TIP3 if u.is_simple()])
            5
        """
    def is_synchronized(self) -> bool:
        """
        Return whether ``self`` is a synchronized Tamari interval.

        This means that the upper and lower binary trees have the same canopee.
        This condition is invariant under complementation.

        This has been considered in [FPR2015]_. The numbers of
        synchronized intervals are given by the sequence :oeis:`A000139`.

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3)
            ....:     if T.is_synchronized()])
            6
        """
    def is_modern(self) -> bool:
        """
        Return whether ``self`` is a modern Tamari interval.

        This is defined by exclusion of a simple pattern in the Hasse diagram,
        namely there is no configuration `y \\rightarrow x \\leftarrow z`
        with `1 \\leq y < x < z \\leq n`.

        This condition is invariant under complementation.

        .. SEEALSO:: :meth:`is_new`, :meth:`is_infinitely_modern`

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3) if T.is_modern()])
            12

        REFERENCES:

        - [Rog2018]_
        """
    def is_infinitely_modern(self) -> bool:
        """
        Return whether ``self`` is an infinitely-modern Tamari interval.

        This is defined by the exclusion of the configuration
        `i \\rightarrow i + 1` and `j + 1 \\rightarrow j` with `i < j`.

        This condition is invariant under complementation.

        .. SEEALSO:: :meth:`is_new`, :meth:`is_modern`

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3)
            ....:     if T.is_infinitely_modern()])
            12

        REFERENCES:

        - [Rog2018]_
        """
    def is_exceptional(self) -> bool:
        """
        Return whether ``self`` is an exceptional Tamari interval.

        This is defined by exclusion of a simple pattern in the Hasse diagram,
        namely there is no configuration ``y <-- x --> z``
        with `1 \\leq y < x < z \\leq n`.

        This condition is invariant under complementation.

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3)
            ....:     if T.is_exceptional()])
            12
        """
    def is_dexter(self) -> bool:
        """
        Return whether ``self`` is a dexter Tamari interval.

        This is defined by an exclusion pattern in the Hasse diagram.
        See the code for the exact description.

        This condition is not invariant under complementation.

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3) if T.is_dexter()])
            12
        """
    def is_indecomposable(self) -> bool:
        """
        Return whether ``self`` is an indecomposable Tamari interval.

        This is the terminology of [Cha2008]_.

        This means that the upper binary tree has an empty left subtree.

        This condition is not invariant under complementation.

        .. SEEALSO:: :meth:`is_connected`

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3)
            ....:      if T.is_indecomposable()])
            8
        """
    def is_connected(self) -> bool:
        """
        Return whether ``self`` is a connected Tamari interval.

        This means that the Hasse diagram is connected.

        This condition is invariant under complementation.

        .. SEEALSO:: :meth:`is_indecomposable`, :meth:`factor`

        EXAMPLES::

            sage: len([T for T in TamariIntervalPosets(3) if T.is_connected()])
            8
        """

class TamariIntervalPosets(UniqueRepresentation, Parent):
    """
    Factory for interval-posets.

    INPUT:

    - ``size`` -- integer (optional)

    OUTPUT:

    - the set of all interval-posets (of the given ``size`` if specified)

    EXAMPLES::

        sage: TamariIntervalPosets()
        Interval-posets

        sage: TamariIntervalPosets(2)
        Interval-posets of size 2

    .. NOTE::

        This is a factory class whose constructor returns instances of
        subclasses.
    """
    @staticmethod
    def __classcall_private__(cls, n=None):
        """
        TESTS::

            sage: from sage.combinat.interval_posets import TamariIntervalPosets_all, TamariIntervalPosets_size
            sage: isinstance(TamariIntervalPosets(2), TamariIntervalPosets_size)
            True
            sage: isinstance(TamariIntervalPosets(), TamariIntervalPosets_all)
            True
            sage: TamariIntervalPosets(2) is TamariIntervalPosets_size(2)
            True
            sage: TamariIntervalPosets() is TamariIntervalPosets_all()
            True

            sage: TamariIntervalPosets(-2)
            Traceback (most recent call last):
            ...
            ValueError: n must be a nonnegative integer
        """
    class options(GlobalOptions):
        """
        Set and display the options for Tamari interval-posets.

        If no parameters are set, then the function returns a copy of
        the options dictionary.

        The ``options`` to Tamari interval-posets can be accessed as the method
        :meth:`TamariIntervalPosets.options` of :class:`TamariIntervalPosets`
        and related parent classes.

        @OPTIONS@

        EXAMPLES::

            sage: TIP = TamariIntervalPosets
            sage: TIP.options.latex_color_decreasing
            red
            sage: TIP.options.latex_color_decreasing = 'green'
            sage: TIP.options.latex_color_decreasing
            green
            sage: TIP.options._reset()
            sage: TIP.options.latex_color_decreasing
            red
        """
        NAME: str
        module: str
        latex_tikz_scale: Incomplete
        latex_line_width_scalar: Incomplete
        latex_color_decreasing: Incomplete
        latex_color_increasing: Incomplete
        latex_hspace: Incomplete
        latex_vspace: Incomplete
    @staticmethod
    def check_poset(poset) -> bool:
        """
        Check if the given poset ``poset`` is a interval-poset, that is,
        if it satisfies the following properties:

        - Its labels are exactly `1, \\ldots, n` where `n` is its size.
        - If `a < c` (as numbers) and `a` precedes `c`, then `b` precedes
          `c` for all `b` such that `a < b < c`.
        - If `a < c` (as numbers) and `c` precedes `a`, then `b` precedes
          `a` for all `b` such that `a < b < c`.

        INPUT:

        - ``poset`` -- a finite labeled poset

        EXAMPLES::

            sage: p = Poset(([1,2,3],[(1,2),(3,2)]))
            sage: TamariIntervalPosets.check_poset(p)
            True
            sage: p = Poset(([2,3],[(3,2)]))
            sage: TamariIntervalPosets.check_poset(p)
            False
            sage: p = Poset(([1,2,3],[(3,1)]))
            sage: TamariIntervalPosets.check_poset(p)
            False
            sage: p = Poset(([1,2,3],[(1,3)]))
            sage: TamariIntervalPosets.check_poset(p)
            False
        """
    @staticmethod
    def final_forest(element) -> TIP:
        """
        Return the final forest of a binary tree, an interval-poset or a
        Dyck word.

        A final forest is an interval-poset corresponding to a final
        interval of the Tamari lattice, i.e., containing only decreasing
        relations.

        It can be constructed from a binary tree by its binary
        search tree labeling with the rule: `b` precedes
        `a` in the final forest iff `b` is in the right subtree of `a`
        in the binary search tree.

        INPUT:

        - ``element`` -- a binary tree, a Dyck word or an interval-poset

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: TamariIntervalPosets.final_forest(ip)
            The Tamari interval of size 4 induced by relations [(4, 3)]

        From binary trees::

            sage: bt = BinaryTree(); bt
            .
            sage: TamariIntervalPosets.final_forest(bt)
            The Tamari interval of size 0 induced by relations []
            sage: bt = BinaryTree([]); bt
            [., .]
            sage: TamariIntervalPosets.final_forest(bt)
            The Tamari interval of size 1 induced by relations []
            sage: bt = BinaryTree([[],None]); bt
            [[., .], .]
            sage: TamariIntervalPosets.final_forest(bt)
            The Tamari interval of size 2 induced by relations []
            sage: bt = BinaryTree([None,[]]); bt
            [., [., .]]
            sage: TamariIntervalPosets.final_forest(bt)
            The Tamari interval of size 2 induced by relations [(2, 1)]
            sage: bt = BinaryTree([[],[]]); bt
            [[., .], [., .]]
            sage: TamariIntervalPosets.final_forest(bt)
            The Tamari interval of size 3 induced by relations [(3, 2)]
            sage: bt = BinaryTree([[None,[[],None]],[]]); bt
            [[., [[., .], .]], [., .]]
            sage: TamariIntervalPosets.final_forest(bt)
            The Tamari interval of size 5 induced by relations [(5, 4), (3, 1), (2, 1)]

        From Dyck words::

            sage: # needs sage.combinat
            sage: dw = DyckWord([1,0])
            sage: TamariIntervalPosets.final_forest(dw)
            The Tamari interval of size 1 induced by relations []
            sage: dw = DyckWord([1,1,0,1,0,0,1,1,0,0])
            sage: TamariIntervalPosets.final_forest(dw)
            The Tamari interval of size 5 induced by relations [(5, 4), (3, 1), (2, 1)]

        TESTS::

            sage: TamariIntervalPosets.final_forest('mont')
            Traceback (most recent call last):
            ...
            ValueError: do not know how to construct the final forest of mont
        """
    @staticmethod
    def initial_forest(element) -> TIP:
        """
        Return the initial forest of a binary tree, an interval-poset or
        a Dyck word.

        An initial forest is an interval-poset corresponding to an initial
        interval of the Tamari lattice, i.e., containing only increasing
        relations.

        It can be constructed from a binary tree by its binary
        search tree labeling with the rule: `a` precedes `b` in the
        initial forest iff `a` is in the left subtree of `b` in the
        binary search tree.

        INPUT:

        - ``element`` -- a binary tree, a Dyck word or an interval-poset

        EXAMPLES::

            sage: ip = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: TamariIntervalPosets.initial_forest(ip)
            The Tamari interval of size 4 induced by relations [(1, 2), (2, 3)]

        with binary trees::

            sage: bt = BinaryTree(); bt
            .
            sage: TamariIntervalPosets.initial_forest(bt)
            The Tamari interval of size 0 induced by relations []
            sage: bt = BinaryTree([]); bt
            [., .]
            sage: TamariIntervalPosets.initial_forest(bt)
            The Tamari interval of size 1 induced by relations []
            sage: bt = BinaryTree([[],None]); bt
            [[., .], .]
            sage: TamariIntervalPosets.initial_forest(bt)
            The Tamari interval of size 2 induced by relations [(1, 2)]
            sage: bt = BinaryTree([None,[]]); bt
            [., [., .]]
            sage: TamariIntervalPosets.initial_forest(bt)
            The Tamari interval of size 2 induced by relations []
            sage: bt = BinaryTree([[],[]]); bt
            [[., .], [., .]]
            sage: TamariIntervalPosets.initial_forest(bt)
            The Tamari interval of size 3 induced by relations [(1, 2)]
            sage: bt = BinaryTree([[None,[[],None]],[]]); bt
            [[., [[., .], .]], [., .]]
            sage: TamariIntervalPosets.initial_forest(bt)
            The Tamari interval of size 5 induced by relations [(1, 4), (2, 3), (3, 4)]

        from Dyck words::

            sage: # needs sage.combinat
            sage: dw = DyckWord([1,0])
            sage: TamariIntervalPosets.initial_forest(dw)
            The Tamari interval of size 1 induced by relations []
            sage: dw = DyckWord([1,1,0,1,0,0,1,1,0,0])
            sage: TamariIntervalPosets.initial_forest(dw)
            The Tamari interval of size 5 induced by relations [(1, 4), (2, 3), (3, 4)]

        TESTS::

            sage: TamariIntervalPosets.initial_forest('mont')
            Traceback (most recent call last):
            ...
            ValueError: do not know how to construct the initial forest of mont
        """
    @staticmethod
    def from_binary_trees(tree1, tree2) -> TIP:
        """
        Return the interval-poset corresponding to the interval
        [``tree1``, ``tree2``] of the Tamari lattice.

        Raise an exception if
        ``tree1`` is not `\\leq` ``tree2`` in the Tamari lattice.

        INPUT:

        - ``tree1`` -- a binary tree
        - ``tree2`` -- a binary tree greater or equal than ``tree1`` for
          the Tamari lattice

        EXAMPLES::

            sage: tree1 = BinaryTree([[],None])
            sage: tree2 = BinaryTree([None,[]])
            sage: TamariIntervalPosets.from_binary_trees(tree1,tree2)
            The Tamari interval of size 2 induced by relations []
            sage: TamariIntervalPosets.from_binary_trees(tree1,tree1)
            The Tamari interval of size 2 induced by relations [(1, 2)]
            sage: TamariIntervalPosets.from_binary_trees(tree2,tree2)
            The Tamari interval of size 2 induced by relations [(2, 1)]

            sage: tree1 = BinaryTree([[],[[None,[]],[]]])
            sage: tree2 = BinaryTree([None,[None,[None,[[],[]]]]])
            sage: TamariIntervalPosets.from_binary_trees(tree1,tree2)
            The Tamari interval of size 6 induced by relations
             [(4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]

            sage: tree3 = BinaryTree([None,[None,[[],[None,[]]]]])
            sage: TamariIntervalPosets.from_binary_trees(tree1,tree3)
            Traceback (most recent call last):
            ...
            ValueError: the two binary trees are not comparable on the Tamari lattice
            sage: TamariIntervalPosets.from_binary_trees(tree1,BinaryTree())
            Traceback (most recent call last):
            ...
            ValueError: the two binary trees are not comparable on the Tamari lattice
        """
    @staticmethod
    def from_dyck_words(dw1, dw2) -> TIP:
        """
        Return the interval-poset corresponding to the interval
        [``dw1``, ``dw2``] of the Tamari lattice.

        Raise an exception if the
        two Dyck words ``dw1`` and ``dw2`` do not satisfy
        ``dw1`` `\\leq` ``dw2`` in the Tamari lattice.

        INPUT:

        - ``dw1`` -- a Dyck word
        - ``dw2`` -- a Dyck word greater or equal than ``dw1`` for
          the Tamari lattice

        EXAMPLES::

            sage: # needs sage.combinat
            sage: dw1 = DyckWord([1,0,1,0])
            sage: dw2 = DyckWord([1,1,0,0])
            sage: TamariIntervalPosets.from_dyck_words(dw1, dw2)
            The Tamari interval of size 2 induced by relations []
            sage: TamariIntervalPosets.from_dyck_words(dw1,dw1)
            The Tamari interval of size 2 induced by relations [(1, 2)]
            sage: TamariIntervalPosets.from_dyck_words(dw2,dw2)
            The Tamari interval of size 2 induced by relations [(2, 1)]

            sage: # needs sage.combinat
            sage: dw1 = DyckWord([1,0,1,1,1,0,0,1,1,0,0,0])
            sage: dw2 = DyckWord([1,1,1,1,0,1,1,0,0,0,0,0])
            sage: TamariIntervalPosets.from_dyck_words(dw1,dw2)
            The Tamari interval of size 6 induced by relations
             [(4, 5), (6, 5), (5, 2), (4, 3), (3, 2)]
            sage: dw3 = DyckWord([1,1,1,0,1,1,1,0,0,0,0,0])
            sage: TamariIntervalPosets.from_dyck_words(dw1,dw3)
            Traceback (most recent call last):
            ...
            ValueError: the two Dyck words are not comparable on the Tamari lattice
            sage: TamariIntervalPosets.from_dyck_words(dw1,DyckWord([1,0]))
            Traceback (most recent call last):
            ...
            ValueError: the two Dyck words are not comparable on the Tamari lattice
        """
    @staticmethod
    def recomposition_from_triple(left: TIP, right: TIP, r) -> TIP:
        """
        Recompose an interval-poset from a triple (``left``, ``right``, ``r``).

        For the inverse method,
        see :meth:`TamariIntervalPoset.decomposition_to_triple`.

        INPUT:

        - ``left`` -- an interval-poset
        - ``right`` -- an interval-poset
        - ``r`` -- the parameter of the decomposition, an integer

        OUTPUT: an interval-poset

        EXAMPLES::

            sage: T1 = TamariIntervalPoset(3, [(1, 2), (3, 2)])
            sage: T2 = TamariIntervalPoset(4, [(2, 3), (4, 3)])
            sage: TamariIntervalPosets.recomposition_from_triple(T1, T2, 2)
            The Tamari interval of size 8 induced by relations [(1, 2), (2, 4),
            (3, 4), (6, 7), (8, 7), (6, 4), (5, 4), (3, 2)]

        REFERENCES:

        - [Pons2018]_
        """
    @staticmethod
    def from_grafting_tree(tree) -> TIP:
        """
        Return an interval-poset from a grafting tree.

        For the inverse method,
        see :meth:`TamariIntervalPoset.grafting_tree`.

        EXAMPLES::

            sage: tip = TamariIntervalPoset(8, [(1,2), (2,4), (3,4), (6,7), (3,2), (5,4), (6,4), (8,7)])
            sage: t = tip.grafting_tree()
            sage: TamariIntervalPosets.from_grafting_tree(t) == tip
            True

        REFERENCES:

        - [Pons2018]_
        """
    @staticmethod
    def from_minimal_schnyder_wood(graph) -> TIP:
        """
        Return a Tamari interval built from a minimal Schnyder wood.

        This is an implementation of Bernardi and Bonichon's bijection
        [BeBo2009]_.

        INPUT:

        - ``graph`` -- a minimal Schnyder wood, given as a graph with colored
          and oriented edges, without the three exterior unoriented edges

        The three boundary vertices must be -1, -2 and -3.

        One assumes moreover that the embedding around -1 is the
        list of neighbors of -1 and not just a cyclic permutation of that.

        Beware that the embedding convention used here is the opposite of
        the one used by the plot method.

        OUTPUT: a Tamari interval-poset

        EXAMPLES:

        A small example::

            sage: TIP = TamariIntervalPosets
            sage: G = DiGraph([(0,-1,0),(0,-2,1),(0,-3,2)], format='list_of_edges')
            sage: G.set_embedding({-1:[0],-2:[0],-3:[0],0:[-1,-2,-3]})
            sage: TIP.from_minimal_schnyder_wood(G)                                     # needs sage.combinat
            The Tamari interval of size 1 induced by relations []

        An example from page 14 of [BeBo2009]_::

            sage: c0 = [(0,-1),(1,0),(2,0),(4,3),(3,-1),(5,3)]
            sage: c1 = [(5,-2),(3,-2),(4,5),(1,3),(2,3),(0,3)]
            sage: c2 = [(0,-3),(1,-3),(3,-3),(4,-3),(5,-3),(2,1)]
            sage: ed = [(u,v,0) for u,v in c0]
            sage: ed += [(u,v,1) for u,v in c1]
            sage: ed += [(u,v,2) for u,v in c2]
            sage: G = DiGraph(ed, format='list_of_edges')
            sage: embed = {-1:[3,0],-2:[5,3],-3:[0,1,3,4,5]}
            sage: data_emb = [[3,2,1,-3,-1],[2,3,-3,0],[3,1,0]]
            sage: data_emb += [[-2,5,4,-3,1,2,0,-1],[5,-3,3],[-2,-3,4,3]]
            sage: for k in range(6):
            ....:     embed[k] = data_emb[k]
            sage: G.set_embedding(embed)
            sage: TIP.from_minimal_schnyder_wood(G)                                     # needs sage.combinat
            The Tamari interval of size 6 induced by relations
             [(1, 4), (2, 4), (3, 4), (5, 6), (6, 4), (5, 4), (3, 1), (2, 1)]

        An example from page 18 of [BeBo2009]_::

            sage: c0 = [(0,-1),(1,0),(2,-1),(3,2),(4,2),(5,-1)]
            sage: c1 = [(5,-2),(2,-2),(4,-2),(3,4),(1,2),(0,2)]
            sage: c2 = [(0,-3),(1,-3),(3,-3),(4,-3),(2,-3),(5,2)]
            sage: ed = [(u,v,0) for u,v in c0]
            sage: ed += [(u,v,1) for u,v in c1]
            sage: ed += [(u,v,2) for u,v in c2]
            sage: G = DiGraph(ed, format='list_of_edges')
            sage: embed = {-1:[5,2,0],-2:[4,2,5],-3:[0,1,2,3,4]}
            sage: data_emb = [[2,1,-3,-1],[2,-3,0],[3,-3,1,0,-1,5,-2,4]]
            sage: data_emb += [[4,-3,2],[-2,-3,3,2],[-2,2,-1]]
            sage: for k in range(6):
            ....:     embed[k] = data_emb[k]
            sage: G.set_embedding(embed)
            sage: TIP.from_minimal_schnyder_wood(G)                                     # needs sage.combinat
            The Tamari interval of size 6 induced by relations
             [(1, 3), (2, 3), (4, 5), (5, 3), (4, 3), (2, 1)]

        Another small example::

            sage: c0 = [(0,-1),(2,-1),(1,0)]
            sage: c1 = [(2,-2),(1,-2),(0,2)]
            sage: c2 = [(0,-3),(1,-3),(2,1)]
            sage: ed = [(u,v,0) for u,v in c0]
            sage: ed += [(u,v,1) for u,v in c1]
            sage: ed += [(u,v,2) for u,v in c2]
            sage: G = DiGraph(ed, format='list_of_edges')
            sage: embed = {-1:[2,0],-2:[1,2],-3:[0,1]}
            sage: data_emb = [[2,1,-3,-1],[-3,0,2,-2],[-2,1,0,-1]]
            sage: for k in range(3):
            ....:     embed[k] = data_emb[k]
            sage: G.set_embedding(embed)
            sage: TIP.from_minimal_schnyder_wood(G)                                     # needs sage.combinat
            The Tamari interval of size 3 induced by relations [(2, 3), (2, 1)]
        """
    def __call__(self, *args, **keywords):
        """
        Allow for a poset to be directly transformed into an interval-poset.

        It is some kind of coercion but cannot be made through the coercion
        system because posets do not have parents.

        EXAMPLES::

            sage: TIP = TamariIntervalPosets()
            sage: p = Poset( ([1,2,3], [(1,2)]))
            sage: TIP(p)
            The Tamari interval of size 3 induced by relations [(1, 2)]
            sage: TIP(TIP(p))
            The Tamari interval of size 3 induced by relations [(1, 2)]
            sage: TIP(3,[(1,2)])
            The Tamari interval of size 3 induced by relations [(1, 2)]
            sage: p = Poset(([1,2,3],[(1,3)]))
            sage: TIP(p)
            Traceback (most recent call last):
            ...
            ValueError: this does not satisfy the Tamari interval-poset condition
        """
    def le(self, el1, el2) -> bool:
        """
        Poset structure on the set of interval-posets.

        The comparison is first by size, then using the
        cubical coordinates.

        .. SEEALSO:: :meth:`~TamariIntervalPoset.cubical_coordinates`

        INPUT:

        - ``el1`` -- an interval-poset
        - ``el2`` -- an interval-poset

        EXAMPLES::

            sage: ip1 = TamariIntervalPoset(4,[(1,2),(2,3),(4,3)])
            sage: ip2 = TamariIntervalPoset(4,[(1,2),(2,3)])
            sage: TamariIntervalPosets().le(ip1,ip2)
            False
            sage: TamariIntervalPosets().le(ip2,ip1)
            True
        """

class TamariIntervalPosets_all(DisjointUnionEnumeratedSets, TamariIntervalPosets):
    """
    The enumerated set of all Tamari interval-posets.
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.combinat.interval_posets import TamariIntervalPosets_all
            sage: S = TamariIntervalPosets_all()
            sage: S.cardinality()
            +Infinity

            sage: it = iter(S)
            sage: [next(it) for i in range(5)]
            [The Tamari interval of size 0 induced by relations [],
             The Tamari interval of size 1 induced by relations [],
             The Tamari interval of size 2 induced by relations [],
             The Tamari interval of size 2 induced by relations [(2, 1)],
             The Tamari interval of size 2 induced by relations [(1, 2)]]
            sage: next(it).parent()
            Interval-posets
            sage: S(0,[])
            The Tamari interval of size 0 induced by relations []

            sage: S is TamariIntervalPosets_all()
            True
            sage: TestSuite(S).run()  # long time (7s)
        """
    def one(self) -> TIP:
        """
        Return the unit of the monoid.

        This is the empty interval poset, of size 0.

        EXAMPLES::

            sage: TamariIntervalPosets().one()
            The Tamari interval of size 0 induced by relations []
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = TamariIntervalPosets()
            sage: 1 in S
            False
            sage: S(0,[]) in S
            True
        """
    Element = TamariIntervalPoset
TIP = TamariIntervalPoset

class TamariIntervalPosets_size(TamariIntervalPosets):
    """
    The enumerated set of interval-posets of a given size.
    """
    def __init__(self, size) -> None:
        """
        TESTS::

            sage: S = TamariIntervalPosets(3)
            sage: assert S is TamariIntervalPosets(3)
            sage: for i in range(5): TestSuite(TamariIntervalPosets(i)).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = TamariIntervalPosets(3)
            sage: 1 in S
            False
            sage: S([]) in S
            True
        """
    def cardinality(self) -> Integer:
        """
        The cardinality of ``self``. That is, the number of
        interval-posets of size `n`.

        The formula was given in [Cha2008]_:

        .. MATH::

            \\frac{2(4n+1)!}{(n+1)!(3n+2)!}
            = \\frac{2}{n(n+1)} \\binom{4n+1}{n-1}.

        EXAMPLES::

            sage: [TamariIntervalPosets(i).cardinality() for i in range(6)]
            [1, 1, 3, 13, 68, 399]
        """
    def __iter__(self) -> Iterator[TIP]:
        """
        Recursive generation: we iterate through all interval-posets of
        size ``size - 1`` and add all possible relations to the last
        vertex.

        This works thanks to the fact that the restriction of an
        interval-poset of size `n` to the subset `\\{1, 2, \\ldots, k\\}` for
        a fixed `k \\leq n` is an interval-poset.

        TESTS::

            sage: TIP1 = TamariIntervalPosets(1)
            sage: list(TIP1)
            [The Tamari interval of size 1 induced by relations []]
            sage: TIP2 = TamariIntervalPosets(2)
            sage: list(TIP2)
            [The Tamari interval of size 2 induced by relations [],
             The Tamari interval of size 2 induced by relations [(2, 1)],
             The Tamari interval of size 2 induced by relations [(1, 2)]]
            sage: TIP3 = TamariIntervalPosets(3)
            sage: list(TIP3)
            [The Tamari interval of size 3 induced by relations [],
             The Tamari interval of size 3 induced by relations [(3, 2)],
             The Tamari interval of size 3 induced by relations [(2, 3)],
             The Tamari interval of size 3 induced by relations [(1, 3), (2, 3)],
             The Tamari interval of size 3 induced by relations [(2, 1)],
             The Tamari interval of size 3 induced by relations [(3, 2), (2, 1)],
             The Tamari interval of size 3 induced by relations [(3, 1), (2, 1)],
             The Tamari interval of size 3 induced by relations [(2, 3), (2, 1)],
             The Tamari interval of size 3 induced by relations [(2, 3), (3, 1), (2, 1)],
             The Tamari interval of size 3 induced by relations [(1, 3), (2, 3), (2, 1)],
             The Tamari interval of size 3 induced by relations [(1, 2)],
             The Tamari interval of size 3 induced by relations [(1, 2), (3, 2)],
             The Tamari interval of size 3 induced by relations [(1, 2), (2, 3)]]
            sage: all(len(list(TamariIntervalPosets(i)))==TamariIntervalPosets(i).cardinality() for i in range(6))
            True
        """
    def random_element(self) -> TIP:
        """
        Return a random Tamari interval of fixed size.

        This is obtained by first creating a random rooted
        planar triangulation, then computing its unique
        minimal Schnyder wood, then applying a bijection
        of Bernardi and Bonichon [BeBo2009]_.

        Because the random rooted planar triangulation is
        chosen uniformly at random, the Tamari interval is
        also chosen according to the uniform distribution.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: T = TamariIntervalPosets(4).random_element()
            sage: T.parent()
            Interval-posets
            sage: u = T.lower_dyck_word(); u   # random
            [1, 1, 0, 1, 0, 0, 1, 0]
            sage: v = T.lower_dyck_word(); v   # random
            [1, 1, 0, 1, 0, 0, 1, 0]
            sage: len(u)
            8
        """
    @lazy_attribute
    def element_class(self):
        """
        TESTS::

            sage: S = TamariIntervalPosets(3)
            sage: S.element_class
            <class 'sage.combinat.interval_posets.TamariIntervalPosets_all_with_category.element_class'>
            sage: S.first().__class__ == TamariIntervalPosets().first().__class__
            True
        """
