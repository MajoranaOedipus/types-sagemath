from sage.combinat.crystals.letters import CrystalOfLetters as CrystalOfLetters
from sage.combinat.rigged_configurations.bij_abstract_class import KRTToRCBijectionAbstract as KRTToRCBijectionAbstract, RCToKRTBijectionAbstract as RCToKRTBijectionAbstract
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class KRTToRCBijectionTypeE67(KRTToRCBijectionAbstract):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `E_{6,7}^{(1)}`.
    """
    def next_state(self, val):
        """
        Build the next state for type `E_{6,7}^{(1)}`.

        TESTS::

            sage: from sage.combinat.rigged_configurations.bij_type_E67 import KRTToRCBijectionTypeE67
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['E', 6, 1], [[3,1]])
            sage: bijection = KRTToRCBijectionTypeE67(KRT.module_generators[0])
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [1, 1])
            sage: bijection.cur_path[0].insert(0, [(-3,4)])
            sage: bijection.next_state((-3,4))
        """

class RCToKRTBijectionTypeE67(RCToKRTBijectionAbstract):
    """
    Specific implementation of the bijection from rigged configurations
    to tensor products of KR tableaux for type `E_{6,7}^{(1)}`.
    """
    def next_state(self, r):
        """
        Build the next state for type `E_{6,7}^{(1)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['E', 6, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_E67 import RCToKRTBijectionTypeE67
            sage: bijection = RCToKRTBijectionTypeE67(RC(partition_list=[[1],[1,1],[1,1],[1,1,1],[1,1],[1]]))
            sage: bijection.next_state(1)
            (-2, 1)
        """

def endpoint6(r):
    """
    Return the endpoint for `B^{r,1}` in type `E_6^{(1)}`.

    EXAMPLES::

        sage: from sage.combinat.rigged_configurations.bij_type_E67 import endpoint6
        sage: endpoint6(1)
        (1,)
        sage: endpoint6(2)
        (-3, 2)
        sage: endpoint6(3)
        (-1, 3)
        sage: endpoint6(4)
        (-3, 4)
        sage: endpoint6(5)
        (-2, 5)
        sage: endpoint6(6)
        (-1, 6)
    """
def endpoint7(r):
    """
    Return the endpoint for `B^{r,1}` in type `E_7^{(1)}`.

    EXAMPLES::

        sage: from sage.combinat.rigged_configurations.bij_type_E67 import endpoint7
        sage: endpoint7(1)
        (-7, 1)
        sage: endpoint7(2)
        (-1, 2)
        sage: endpoint7(3)
        (-2, 3)
        sage: endpoint7(4)
        (-5, 4)
        sage: endpoint7(5)
        (-6, 5)
        sage: endpoint7(6)
        (-7, 6)
        sage: endpoint7(7)
        (7,)
    """
