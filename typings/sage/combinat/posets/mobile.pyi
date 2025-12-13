from .linear_extensions import LinearExtensionsOfMobile as LinearExtensionsOfMobile
from sage.combinat.posets.posets import FinitePoset as FinitePoset, Poset as Poset
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class MobilePoset(FinitePoset):
    """
    A mobile poset.

    Mobile posets are an extension of d-complete posets which permit a determinant
    formula for counting linear extensions. They are formed by having a ribbon
    poset with d-complete posets 'hanging' below it and at most one
    d-complete poset above it, known as the anchor. See [GGMM2020]_
    for the definition.

    EXAMPLES::

        sage: P = posets.MobilePoset(posets.RibbonPoset(7, [1,3]),                      # needs sage.combinat sage.modules
        ....:                        {1: [posets.YoungDiagramPoset([3, 2], dual=True)],
        ....:                         3: [posets.DoubleTailedDiamond(6)]},
        ....:                        anchor=(4, 2, posets.ChainPoset(6)))
        sage: len(P._ribbon)                                                            # needs sage.combinat sage.modules
        8
        sage: P._anchor                                                                 # needs sage.combinat sage.modules
        (4, 5)

    This example is Example 5.9 in [GGMM2020]_::

        sage: P1 = posets.MobilePoset(posets.RibbonPoset(8, [2,3,4]),
        ....:                         {4: [posets.ChainPoset(1)]},
        ....:                         anchor=(3, 0, posets.ChainPoset(1)))
        sage: sorted([P1._element_to_vertex(i) for i in P1._ribbon])
        [0, 1, 2, 6, 7, 9]
        sage: P1._anchor
        (3, 2)

        sage: P2 = posets.MobilePoset(posets.RibbonPoset(15, [1,3,5,7,9,11,13]),
        ....:                         {}, anchor=(8, 0, posets.ChainPoset(1)))
        sage: sorted(P2._ribbon)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        sage: P2._anchor
        (8, (8, 0))
        sage: P2.linear_extensions().cardinality()                                      # needs sage.modules
        21399440939

        sage: EP = posets.MobilePoset(posets.ChainPoset(0), {})
        Traceback (most recent call last):
        ...
        ValueError: the empty poset is not a mobile poset
    """
    def __init__(self, hasse_diagram, elements, category, facade, key, ribbon=None, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: P = posets.MobilePoset(posets.RibbonPoset(15, [1,3,5,7,9,11,13]),
            ....:                        {}, anchor=(8, 0, posets.ChainPoset(1)))
            sage: TestSuite(P).run()
        """
    def ribbon(self):
        """
        Return the ribbon of the mobile poset.

        EXAMPLES::

            sage: from sage.combinat.posets.mobile import MobilePoset
            sage: M3 = MobilePoset(Posets.RibbonPoset(5, [1,2]))
            sage: sorted(M3.ribbon())
            [1, 2, 3, 4]
        """
    def anchor(self):
        """
        Return the anchor of the mobile poset.

        EXAMPLES::

            sage: from sage.combinat.posets.mobile import MobilePoset
            sage: M2 = MobilePoset(Poset([[0,1,2,3,4,5,6,7,8],
            ....:          [(1,0),(3,0),(2,1),(2,3),(4,3),(5,4),(7,4),(7,8)]]))
            sage: M2.anchor()
            (4, 3)
            sage: M3 = MobilePoset(Posets.RibbonPoset(5, [1,2]))
            sage: M3.anchor() is None
            True
        """
