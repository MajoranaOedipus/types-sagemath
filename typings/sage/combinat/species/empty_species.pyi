from .species import GenericCombinatorialSpecies as GenericCombinatorialSpecies
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class EmptySpecies(GenericCombinatorialSpecies, UniqueRepresentation):
    """
    Return the empty species. This species has no structure at all.
    It is the zero of the semi-ring of species.

    EXAMPLES::

        sage: X = species.EmptySpecies(); X
        doctest:warning...
        DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
        See https://github.com/sagemath/sage/issues/38544 for details.
        Empty species
        sage: X.structures([]).list()
        []
        sage: X.structures([1]).list()
        []
        sage: X.structures([1,2]).list()
        []
        sage: X.generating_series()[0:4]
        [0, 0, 0, 0]
        sage: X.isotype_generating_series()[0:4]
        [0, 0, 0, 0]
        sage: X.cycle_index_series()[0:4]                                               # needs sage.modules
        [0, 0, 0, 0]

    The empty species is the zero of the semi-ring of species.
    The following tests that it is neutral with respect to addition::

        sage: Empt  = species.EmptySpecies()
        sage: S = species.CharacteristicSpecies(2)
        sage: X = S + Empt
        sage: X == S    # TODO: Not Implemented
        True
        sage: (X.generating_series()[0:4] ==
        ....:  S.generating_series()[0:4])
        True
        sage: (X.isotype_generating_series()[0:4] ==
        ....:  S.isotype_generating_series()[0:4])
        True
        sage: (X.cycle_index_series()[0:4] ==                                           # needs sage.modules
        ....:  S.cycle_index_series()[0:4])
        True

    The following tests that it is the zero element with respect to
    multiplication::

        sage: Y = Empt*S
        sage: Y == Empt   # TODO: Not Implemented
        True
        sage: Y.generating_series()[0:4]
        [0, 0, 0, 0]
        sage: Y.isotype_generating_series()[0:4]
        [0, 0, 0, 0]
        sage: Y.cycle_index_series()[0:4]                                               # needs sage.modules
        [0, 0, 0, 0]

    TESTS::

        sage: Empt  = species.EmptySpecies()
        sage: Empt2 = species.EmptySpecies()
        sage: Empt is Empt2
        True
    """
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        Initializer for the empty species.

        EXAMPLES::

            sage: F = species.EmptySpecies()
            sage: F._check()
            True
            sage: F == loads(dumps(F))
            True
        """
EmptySpecies_class = EmptySpecies
