from _typeshed import Incomplete
from sage.misc.latex import latex as latex

class ElementWithLabel:
    '''
    Auxiliary class for showing/viewing :class:`Poset`s with
    non-injective labelings.
    For hashing and equality testing the resulting object behaves
    like a tuple ``(element, label)``.
    For any presentation purposes it appears just as ``label`` would.

    EXAMPLES::

        sage: # needs sage.combinat sage.graphs
        sage: P = Poset({1: [2,3]})
        sage: labs = {i: P.rank(i) for i in range(1, 4)}
        sage: print(labs)
        {1: 0, 2: 1, 3: 1}
        sage: print(P.plot(element_labels=labs))                                        # needs sage.plot
        Graphics object consisting of 6 graphics primitives

        sage: # needs sage.combinat sage.graphs sage.modules
        sage: from sage.misc.element_with_label import ElementWithLabel
        sage: W = WeylGroup("A1")
        sage: P = W.bruhat_poset(facade=True)
        sage: D = W.domain()
        sage: v = D.rho() - D.fundamental_weight(1)
        sage: nP = P.relabel(lambda w: ElementWithLabel(w, w.action(v)))
        sage: list(nP)
        [(0, 0), (0, 0)]
    '''
    element: Incomplete
    label: Incomplete
    def __init__(self, element, label) -> None:
        """
        Construct an object that wraps ``element`` but presents itself
        as ``label``.

        TESTS::

            sage: from sage.misc.element_with_label import ElementWithLabel
            sage: e = ElementWithLabel(1, 'a')
            sage: e
            'a'
            sage: e.element
            1
        """
    def __hash__(self):
        '''
        Return the hash of the labeled element ``self``,
        which is just the hash of ``self.element``.

        TESTS::

            sage: from sage.misc.element_with_label import ElementWithLabel
            sage: a = ElementWithLabel(1, \'a\')
            sage: b = ElementWithLabel(1, \'b\')
            sage: d = {}
            sage: d[a] = \'element 1\'
            sage: d[b] = \'element 2\'
            sage: print(d)
            {\'a\': \'element 1\', \'b\': \'element 2\'}
            sage: a = ElementWithLabel("a", [2,3])
            sage: hash(a) == hash(a.element)
            True
        '''
    def __eq__(self, other):
        """
        Two labeled elements are equal if and only if both of their
        constituents are equal.

        TESTS::

            sage: from sage.misc.element_with_label import ElementWithLabel
            sage: a = ElementWithLabel(1, 'a')
            sage: b = ElementWithLabel(1, 'b')
            sage: x = ElementWithLabel(1, 'a')
            sage: a == b
            False
            sage: a == x
            True
            sage: 1 == a
            False
            sage: b == 1
            False
        """
    def __ne__(self, other):
        """
        Two labeled elements are not equal if and only if first or second
        constituents are not equal.

        TESTS::

            sage: from sage.misc.element_with_label import ElementWithLabel
            sage: a = ElementWithLabel(1, 'a')
            sage: b = ElementWithLabel(1, 'b')
            sage: x = ElementWithLabel(1, 'a')
            sage: a != b
            True
            sage: a != x
            False
        """
