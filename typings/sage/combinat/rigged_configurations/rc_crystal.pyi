from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.combinat.rigged_configurations.rigged_configuration_element import RCHWNonSimplyLacedElement as RCHWNonSimplyLacedElement, RCHighestWeightElement as RCHighestWeightElement, RiggedConfigurationElement as RiggedConfigurationElement
from sage.combinat.rigged_configurations.rigged_configurations import RiggedConfigurations as RiggedConfigurations
from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition as RiggedPartition
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CrystalOfRiggedConfigurations(UniqueRepresentation, Parent):
    """
    A highest weight crystal of rigged configurations.

    The crystal structure for finite simply-laced types is given
    in [CrysStructSchilling06]_. These were then shown to be the crystal
    operators in all finite types in [SS2015]_, all simply-laced and
    a large class of foldings of simply-laced types in [SS2015II]_,
    and all symmetrizable types (uniformly) in [SS2017]_.

    INPUT:

    - ``cartan_type`` -- (optional) a Cartan type or a Cartan type
      given as a folding

    - ``wt`` -- the highest weight vector in the weight lattice

    EXAMPLES:

    For simplicity, we display the rigged configurations horizontally::

        sage: RiggedConfigurations.options.display='horizontal'

    We start with a simply-laced finite type::

        sage: La = RootSystem(['A', 2]).weight_lattice().fundamental_weights()
        sage: RC = crystals.RiggedConfigurations(La[1] + La[2])
        sage: mg = RC.highest_weight_vector()
        sage: mg.f_string([1,2])
        0[ ]0   0[ ]-1
        sage: mg.f_string([1,2,2])
        0[ ]0   -2[ ][ ]-2
        sage: mg.f_string([1,2,2,2])
        sage: mg.f_string([2,1,1,2])
        -1[ ][ ]-1   -1[ ][ ]-1
        sage: RC.cardinality()
        8
        sage: T = crystals.Tableaux(['A', 2], shape=[2,1])
        sage: RC.digraph().is_isomorphic(T.digraph(), edge_labels=True)
        True

    We construct a non-simply-laced affine type::

        sage: La = RootSystem(['C', 3]).weight_lattice().fundamental_weights()
        sage: RC = crystals.RiggedConfigurations(La[2])
        sage: mg = RC.highest_weight_vector()
        sage: mg.f_string([2,3])
        (/)   1[ ]1   -1[ ]-1
        sage: T = crystals.Tableaux(['C', 3], shape=[1,1])
        sage: RC.digraph().is_isomorphic(T.digraph(), edge_labels=True)
        True

    We can construct rigged configurations using a diagram folding of
    a simply-laced type. This yields an equivalent but distinct crystal::

        sage: vct = CartanType(['C', 3]).as_folding()
        sage: RC = crystals.RiggedConfigurations(vct, La[2])
        sage: mg = RC.highest_weight_vector()
        sage: mg.f_string([2,3])
        (/)   0[ ]0   -1[ ]-1
        sage: T = crystals.Tableaux(['C', 3], shape=[1,1])
        sage: RC.digraph().is_isomorphic(T.digraph(), edge_labels=True)
        True

    We reset the global options::

        sage: RiggedConfigurations.options._reset()

    REFERENCES:

    - [SS2015]_
    - [SS2015II]_
    - [SS2017]_
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, wt=None, WLR=None):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: La = RootSystem(['A', 2]).weight_lattice().fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[1])
            sage: RC2 = crystals.RiggedConfigurations(['A', 2], La[1])
            sage: RC3 = crystals.RiggedConfigurations(['A', 2], La[1], La[1].parent())
            sage: RC is RC2 and RC2 is RC3
            True

            sage: La = RootSystem(['A',2,1]).weight_lattice().fundamental_weights()
            sage: LaE = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[1])
            sage: RCE = crystals.RiggedConfigurations(LaE[1])
            sage: RC is RCE
            False
        """
    module_generators: Incomplete
    def __init__(self, wt, WLR) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: La = RootSystem(['A', 2]).weight_lattice().fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[1] + La[2])
            sage: TestSuite(RC).run()

            sage: La = RootSystem(['A', 2, 1]).weight_lattice().fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[0])
            sage: TestSuite(RC).run() # long time
        """
    options = RiggedConfigurations.options
    def weight_lattice_realization(self):
        """
        Return the weight lattice realization used to express the weights
        of elements in ``self``.

        EXAMPLES::

            sage: La = RootSystem(['A', 2, 1]).weight_lattice(extended=True).fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[0])
            sage: RC.weight_lattice_realization()
            Extended weight lattice of the Root system of type ['A', 2, 1]
        """
    Element = RCHighestWeightElement

class CrystalOfNonSimplyLacedRC(CrystalOfRiggedConfigurations):
    """
    Highest weight crystal of rigged configurations in non-simply-laced type.
    """
    def __init__(self, vct, wt, WLR) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: La = RootSystem(['C', 3]).weight_lattice().fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[1])
            sage: TestSuite(RC).run()
        """
    @lazy_attribute
    def virtual(self):
        """
        Return the corresponding virtual crystal.

        EXAMPLES::

            sage: La = RootSystem(['C', 2, 1]).weight_lattice().fundamental_weights()
            sage: vct = CartanType(['C', 2, 1]).as_folding()
            sage: RC = crystals.RiggedConfigurations(vct, La[0])
            sage: RC
            Crystal of rigged configurations of type ['C', 2, 1] and weight Lambda[0]
            sage: RC.virtual
            Crystal of rigged configurations of type ['A', 3, 1] and weight 2*Lambda[0]
        """
    def to_virtual(self, rc):
        """
        Convert ``rc`` into a rigged configuration in the virtual crystal.

        INPUT:

        - ``rc`` -- a rigged configuration element

        EXAMPLES::

            sage: La = RootSystem(['C', 3]).weight_lattice().fundamental_weights()
            sage: vct = CartanType(['C', 3]).as_folding()
            sage: RC = crystals.RiggedConfigurations(vct, La[2])
            sage: elt = RC(partition_list=[[], [1], [1]]); elt
            <BLANKLINE>
            (/)
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            sage: RC.to_virtual(elt)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -2[ ][ ]-2
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)
            <BLANKLINE>
        """
    def from_virtual(self, vrc):
        """
        Convert ``vrc`` in the virtual crystal into a rigged configuration of
        the original Cartan type.

        INPUT:

        - ``vrc`` -- a virtual rigged configuration

        EXAMPLES::

            sage: La = RootSystem(['C', 3]).weight_lattice().fundamental_weights()
            sage: vct = CartanType(['C', 3]).as_folding()
            sage: RC = crystals.RiggedConfigurations(vct, La[2])
            sage: elt = RC(partition_list=[[0], [1], [1]])
            sage: elt == RC.from_virtual(RC.to_virtual(elt))
            True
        """
    Element = RCHWNonSimplyLacedElement
