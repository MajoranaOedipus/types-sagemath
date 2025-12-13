from sage.combinat.posets.linear_extensions import LinearExtensionsOfForest as LinearExtensionsOfForest
from sage.combinat.posets.posets import FinitePoset as FinitePoset

class ForestPoset(FinitePoset):
    """
    A forest poset is a poset where the underlying Hasse diagram and is
    directed acyclic graph.
    """
