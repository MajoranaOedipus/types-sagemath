from .lattices import FiniteJoinSemilattice as FiniteJoinSemilattice
from .linear_extensions import LinearExtensionsOfPosetWithHooks as LinearExtensionsOfPosetWithHooks
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ

class DCompletePoset(FiniteJoinSemilattice):
    """
    A d-complete poset.

    D-complete posets are a class of posets introduced by Proctor
    in [Proc1999]_. It includes common families such as shapes, shifted
    shapes, and rooted forests. Proctor showed in [PDynk1999]_ that
    d-complete posets have decompositions in *irreducible* posets,
    and showed in [Proc2014]_ that d-complete posets admit a hook-length
    formula (see :wikipedia:`Hook_length_formula`). A complete proof of
    the hook-length formula can be found in [KY2019]_.

    EXAMPLES::

        sage: from sage.combinat.posets.poset_examples import Posets
        sage: P = Posets.DoubleTailedDiamond(2)
        sage: TestSuite(P).run()
    """
    def get_hook(self, elmt):
        """
        Return the hook length of the element ``elmt``.

        EXAMPLES::

            sage: from sage.combinat.posets.d_complete import DCompletePoset
            sage: P = DCompletePoset(DiGraph({0: [1], 1: [2]}))
            sage: P.get_hook(1)
            2
        """
    def get_hooks(self) -> dict:
        """
        Return all the hook lengths as a dictionary.

        EXAMPLES::

            sage: from sage.combinat.posets.d_complete import DCompletePoset
            sage: P = DCompletePoset(DiGraph({0: [1, 2], 1: [3], 2: [3], 3: []}))
            sage: P.get_hooks()
            {0: 1, 1: 2, 2: 2, 3: 3}
            sage: from sage.combinat.posets.poset_examples import Posets
            sage: YDP321 = Posets.YoungDiagramPoset(Partition([3,2,1]))
            sage: P = DCompletePoset(YDP321._hasse_diagram.reverse())
            sage: P.get_hooks()
            {0: 5, 1: 3, 2: 1, 3: 3, 4: 1, 5: 1}
        """
    def hook_product(self):
        """
        Return the hook product for the poset.

        TESTS::

            sage: from sage.combinat.posets.d_complete import DCompletePoset
            sage: P = DCompletePoset(DiGraph({0: [1, 2], 1: [3], 2: [3], 3: []}))
            sage: P.hook_product()
            12
            sage: P = DCompletePoset(posets.YoungDiagramPoset(Partition([3,2,1]),
            ....:                    dual=True))
            sage: P.hook_product()
            45
        """
