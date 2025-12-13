from .characteristic_species import CharacteristicSpecies as CharacteristicSpecies, EmptySetSpecies as EmptySetSpecies, SingletonSpecies as SingletonSpecies
from .composition_species import CompositionSpecies as CompositionSpecies
from .cycle_species import CycleSpecies as CycleSpecies
from .empty_species import EmptySpecies as EmptySpecies
from .functorial_composition_species import FunctorialCompositionSpecies as FunctorialCompositionSpecies
from .linear_order_species import LinearOrderSpecies as LinearOrderSpecies
from .partition_species import PartitionSpecies as PartitionSpecies
from .permutation_species import PermutationSpecies as PermutationSpecies
from .product_species import ProductSpecies as ProductSpecies
from .recursive_species import CombinatorialSpecies as CombinatorialSpecies
from .set_species import SetSpecies as SetSpecies
from .subset_species import SubsetSpecies as SubsetSpecies
from .sum_species import SumSpecies as SumSpecies
from sage.misc.cachefunc import cached_function as cached_function

@cached_function
def SimpleGraphSpecies():
    """
    Return the species of simple graphs.

    EXAMPLES::

        sage: S = species.SimpleGraphSpecies()
        doctest:warning...
        DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
        See https://github.com/sagemath/sage/issues/38544 for details.
        sage: S.generating_series().counts(10)
        [1, 1, 2, 8, 64, 1024, 32768, 2097152, 268435456, 68719476736]
        sage: S.cycle_index_series()[:5]                                                # needs sage.modules
        [p[],
         p[1],
         p[1, 1] + p[2],
         4/3*p[1, 1, 1] + 2*p[2, 1] + 2/3*p[3],
         8/3*p[1, 1, 1, 1] + 4*p[2, 1, 1] + 2*p[2, 2] + 4/3*p[3, 1] + p[4]]
        sage: S.isotype_generating_series()[:6]                                         # needs sage.modules
        [1, 1, 2, 4, 11, 34]

    TESTS::

        sage: seq = S.isotype_generating_series().counts(6)[1:]                         # needs sage.modules
        sage: oeis(seq)[0]                              # optional - internet           # needs sage.modules
        A000088: ...

    ::

        sage: seq = S.generating_series().counts(10)[1:]                                # needs sage.modules
        sage: oeis(seq)[0]                              # optional - internet           # needs sage.modules
        A006125: a(n) = 2^(n*(n-1)/2).
    """
@cached_function
def BinaryTreeSpecies():
    """
    Return the species of binary trees on `n` leaves.

    The species of binary trees `B` is defined by `B = X + B \\cdot B`,
    where `X` is the singleton species.

    EXAMPLES::

        sage: B = species.BinaryTreeSpecies()
        sage: B.generating_series().counts(10)
        [0, 1, 2, 12, 120, 1680, 30240, 665280, 17297280, 518918400]
        sage: B.isotype_generating_series().counts(10)
        [0, 1, 1, 2, 5, 14, 42, 132, 429, 1430]
        sage: B._check()
        True

    ::

        sage: B = species.BinaryTreeSpecies()
        sage: a = B.structures([1,2,3,4,5])[187]; a
        2*((5*3)*(4*1))
        sage: a.automorphism_group()                                                    # needs sage.groups
        Permutation Group with generators [()]

    TESTS::

        sage: seq = B.isotype_generating_series().counts(10)[1:]
        sage: oeis(seq)[0]                              # optional -- internet
        A000108: Catalan numbers: ...
    """
@cached_function
def BinaryForestSpecies():
    """
    Return the species of binary forests.

    Binary forests are defined as sets of binary trees.

    EXAMPLES::

        sage: F = species.BinaryForestSpecies()
        sage: F.generating_series().counts(10)
        [1, 1, 3, 19, 193, 2721, 49171, 1084483, 28245729, 848456353]
        sage: F.isotype_generating_series().counts(10)                                  # needs sage.modules
        [1, 1, 2, 4, 10, 26, 77, 235, 758, 2504]
        sage: F.cycle_index_series()[:7]                                                # needs sage.modules
        [p[],
         p[1],
         3/2*p[1, 1] + 1/2*p[2],
         19/6*p[1, 1, 1] + 1/2*p[2, 1] + 1/3*p[3],
         193/24*p[1, 1, 1, 1] + 3/4*p[2, 1, 1] + 5/8*p[2, 2] + 1/3*p[3, 1] + 1/4*p[4],
         907/40*p[1, 1, 1, 1, 1] + 19/12*p[2, 1, 1, 1] + 5/8*p[2, 2, 1] + 1/2*p[3, 1, 1] + 1/6*p[3, 2] + 1/4*p[4, 1] + 1/5*p[5],
         49171/720*p[1, 1, 1, 1, 1, 1] + 193/48*p[2, 1, 1, 1, 1] + 15/16*p[2, 2, 1, 1] + 61/48*p[2, 2, 2] + 19/18*p[3, 1, 1, 1] + 1/6*p[3, 2, 1] + 7/18*p[3, 3] + 3/8*p[4, 1, 1] + 1/8*p[4, 2] + 1/5*p[5, 1] + 1/6*p[6]]

    TESTS::

        sage: seq = F.isotype_generating_series().counts(10)[1:]                        # needs sage.modules
        sage: oeis(seq)[0]                              # optional - internet           # needs sage.modules
        A052854: Number of forests of ordered trees on n total nodes.
    """
