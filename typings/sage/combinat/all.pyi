r"""
Combinatorics

Introduction
------------

- :ref:`sage.combinat.quickref`
- :ref:`sage.combinat.tutorial`

Topics
------

- :ref:`sage.combinat.algebraic_combinatorics`

  - :ref:`sage.combinat.chas.all`
  - :ref:`sage.combinat.cluster_algebra_quiver.all`
  - :ref:`sage.combinat.crystals.all`
  - :ref:`sage.combinat.root_system.all`
  - :ref:`sage.combinat.sf.all`
  - :ref:`sage.combinat.fully_commutative_elements`

- :ref:`sage.combinat.counting`
- :ref:`sage.combinat.enumerated_sets`
- :ref:`sage.combinat.catalog_partitions`
- :ref:`sage.combinat.finite_state_machine`
- :ref:`sage.combinat.posets.all`
- :ref:`sage.combinat.species.all`
- :ref:`sage.combinat.designs.all`
- :ref:`sage.combinat.words.all`
- :ref:`sage.combinat.bijectionist`

Utilities
---------

- :ref:`sage.combinat.output`
- :ref:`sage.combinat.ranker`
- :ref:`sage.combinat.combinatorial_map`
- :ref:`sage.combinat.misc`
"""
from sage.misc.namespace_package import install_dict as install_dict, install_doc as install_doc

from sage.combinat.combinat import (
    CombinatorialObject as CombinatorialObject,
    bell_number as bell_number,
    bell_polynomial as bell_polynomial,
    bernoulli_polynomial as bernoulli_polynomial,
    catalan_number as catalan_number,
    euler_number as euler_number,
    fibonacci as fibonacci,
    fibonacci_sequence as fibonacci_sequence,
    fibonacci_xrange as fibonacci_xrange,
    lucas_number1 as lucas_number1,
    lucas_number2 as lucas_number2,
    number_of_tuples as number_of_tuples,
    number_of_unordered_tuples as number_of_unordered_tuples,
    polygonal_number as polygonal_number,
    stirling_number1 as stirling_number1,
    stirling_number2 as stirling_number2,
    tuples as tuples,
    unordered_tuples as unordered_tuples,
)

from sage.combinat.expnums import expnums as expnums
from sage.combinat.chas.all import *
from sage.combinat.crystals.all import *
from sage.combinat.rigged_configurations.all import *

from sage.combinat.dlx import (
    DLXMatrix as DLXMatrix,
    AllExactCovers as AllExactCovers,
    OneExactCover as OneExactCover,
)

# block designs, etc.
from sage.combinat.designs.all import *

# Free modules and friends
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.debruijn_sequence import DeBruijnSequences as DeBruijnSequences

from sage.combinat.schubert_polynomial import SchubertPolynomialRing as SchubertPolynomialRing
from sage.combinat.key_polynomial import KeyPolynomialBasis
KeyPolynomials = KeyPolynomialBasis
from sage.combinat.key_polynomial import AtomPolynomialBasis
AtomPolynomials = AtomPolynomialBasis
from sage.combinat.symmetric_group_algebra import (
    SymmetricGroupAlgebra as SymmetricGroupAlgebra,
    HeckeAlgebraSymmetricGroupT as HeckeAlgebraSymmetricGroupT,
)
from sage.combinat.symmetric_group_representations import (
    SymmetricGroupRepresentation as SymmetricGroupRepresentation,
    SymmetricGroupRepresentations as SymmetricGroupRepresentations,
)
from sage.combinat.yang_baxter_graph import YangBaxterGraph as YangBaxterGraph

# Permutations
from sage.combinat.permutation import (
    Permutation as Permutation,
    Permutations as Permutations,
    Arrangements as Arrangements,
    CyclicPermutations as CyclicPermutations,
    CyclicPermutationsOfPartition as CyclicPermutationsOfPartition,
)
from sage.combinat.affine_permutation import AffinePermutationGroup as AffinePermutationGroup
from sage.combinat.colored_permutations import (
    ColoredPermutations as ColoredPermutations,
    SignedPermutation as SignedPermutation,
    SignedPermutations as SignedPermutations,
)
from sage.combinat.derangements import Derangements as Derangements
from sage.combinat.baxter_permutations import BaxterPermutations as BaxterPermutations
# RSK
from sage.combinat.rsk import (
    RSK as RSK,
    RSK_inverse as RSK_inverse,
    robinson_schensted_knuth as robinson_schensted_knuth,
    robinson_schensted_knuth_inverse as robinson_schensted_knuth_inverse,
    InsertionRules as InsertionRules,
)
# HillmanGrassl
from sage.combinat.hillman_grassl import (
    WeakReversePlanePartition as WeakReversePlanePartition,
    WeakReversePlanePartitions as WeakReversePlanePartitions,
)
# PerfectMatchings
from sage.combinat.perfect_matching import (
    PerfectMatching as PerfectMatching,
    PerfectMatchings as PerfectMatchings,
)

# Integer lists
from sage.combinat.integer_lists import IntegerListsLex as IntegerListsLex

# Compositions
from sage.combinat.composition import (
    Composition as Composition,
    Compositions as Compositions,
)
from sage.combinat.composition_signed import SignedCompositions as SignedCompositions

# Partitions
from sage.combinat.partition import (
    Partition as Partition,
    Partitions as Partitions,
    PartitionsInBox as PartitionsInBox,
    OrderedPartitions as OrderedPartitions,
    PartitionsGreatestLE as PartitionsGreatestLE,
    PartitionsGreatestEQ as PartitionsGreatestEQ,
    number_of_partitions as number_of_partitions,
)
from sage.combinat.partition_tuple import PartitionTuple as PartitionTuple, PartitionTuples as PartitionTuples
from sage.combinat.partition_kleshchev import KleshchevPartitions as KleshchevPartitions
from sage.combinat.skew_partition import SkewPartition as SkewPartition, SkewPartitions as SkewPartitions

# Partition algebra
from sage.combinat.partition_algebra import (
    SetPartitionsAk as SetPartitionsAk,
    SetPartitionsPk as SetPartitionsPk,
    SetPartitionsTk as SetPartitionsTk,
    SetPartitionsIk as SetPartitionsIk,
    SetPartitionsBk as SetPartitionsBk,
    SetPartitionsSk as SetPartitionsSk,
    SetPartitionsRk as SetPartitionsRk,
    SetPartitionsPRk as SetPartitionsPRk,
)
# Raising operators
from sage.combinat.partition_shifting_algebras import ShiftingOperatorAlgebra as ShiftingOperatorAlgebra

# Diagram algebra
from sage.combinat.diagram_algebras import (
    PartitionAlgebra as PartitionAlgebra,
    BrauerAlgebra as BrauerAlgebra,
    TemperleyLiebAlgebra as TemperleyLiebAlgebra,
    PlanarAlgebra as PlanarAlgebra,
    PropagatingIdeal as PropagatingIdeal,
)
# Descent algebra
from sage.combinat.descent_algebra import DescentAlgebra as DescentAlgebra
# Vector Partitions
from sage.combinat.vector_partition import (
    VectorPartition as VectorPartition,
    VectorPartitions as VectorPartitions,
)

# Similarity class types
from sage.combinat.similarity_class_type import (
    PrimarySimilarityClassType as PrimarySimilarityClassType,
    PrimarySimilarityClassTypes as PrimarySimilarityClassTypes,
    SimilarityClassType as SimilarityClassType,
    SimilarityClassTypes as SimilarityClassTypes,
)
# Cores
from sage.combinat.core import Core as Core, Cores as Cores

# Tableaux
from sage.combinat.tableau import (
    Tableau as Tableau,
    SemistandardTableau as SemistandardTableau,
    StandardTableau as StandardTableau,
    RowStandardTableau as RowStandardTableau,
    IncreasingTableau as IncreasingTableau,
    Tableaux as Tableaux,
    SemistandardTableaux as SemistandardTableaux,
    StandardTableaux as StandardTableaux,
    RowStandardTableaux as RowStandardTableaux,
    IncreasingTableaux as IncreasingTableaux,
)
from sage.combinat.skew_tableau import (
    SkewTableau as SkewTableau,
    SkewTableaux as SkewTableaux,
    StandardSkewTableaux as StandardSkewTableaux,
    SemistandardSkewTableaux as SemistandardSkewTableaux,
)
from sage.combinat.ribbon_shaped_tableau import (
    RibbonShapedTableau as RibbonShapedTableau,
    RibbonShapedTableaux as RibbonShapedTableaux,
    StandardRibbonShapedTableaux as StandardRibbonShapedTableaux,
)
from sage.combinat.ribbon_tableau import (
    RibbonTableaux as RibbonTableaux,
    RibbonTableau as RibbonTableau,
    MultiSkewTableaux as MultiSkewTableaux,
    MultiSkewTableau as MultiSkewTableau,
    SemistandardMultiSkewTableaux as SemistandardMultiSkewTableaux,
)
from sage.combinat.composition_tableau import CompositionTableau as CompositionTableau, CompositionTableaux as CompositionTableaux

from sage.combinat.tableau_tuple import (
    TableauTuple as TableauTuple,
    StandardTableauTuple as StandardTableauTuple,
    RowStandardTableauTuple as RowStandardTableauTuple,
    TableauTuples as TableauTuples,
    StandardTableauTuples as StandardTableauTuples,
    RowStandardTableauTuples as RowStandardTableauTuples,
)
from sage.combinat.k_tableau import (
    WeakTableau as WeakTableau,
    WeakTableaux as WeakTableaux,
    StrongTableau as StrongTableau,
    StrongTableaux as StrongTableaux,
)
from sage.combinat.lr_tableau import (
    LittlewoodRichardsonTableau as LittlewoodRichardsonTableau,
    LittlewoodRichardsonTableaux as LittlewoodRichardsonTableaux,
)
from sage.combinat.shifted_primed_tableau import (
    ShiftedPrimedTableaux as ShiftedPrimedTableaux,
    ShiftedPrimedTableau as ShiftedPrimedTableau,
)
# SuperTableaux
from sage.combinat.super_tableau import (
    StandardSuperTableau as StandardSuperTableau,
    SemistandardSuperTableau as SemistandardSuperTableau,
    StandardSuperTableaux as StandardSuperTableaux,
    SemistandardSuperTableaux as SemistandardSuperTableaux,
)
# Words
from sage.combinat.words.all import *

from sage.combinat.subword import Subwords as Subwords
from sage.combinat.graph_path import GraphPaths as GraphPaths

# Tuples
from sage.combinat.tuple import (
    Tuples as Tuples,
    UnorderedTuples as UnorderedTuples,
)

# Alternating sign matrices
from sage.combinat.alternating_sign_matrix import (
    AlternatingSignMatrix as AlternatingSignMatrix,
    AlternatingSignMatrices as AlternatingSignMatrices,
    MonotoneTriangles as MonotoneTriangles,
    ContreTableaux as ContreTableaux,
    TruncatedStaircases as TruncatedStaircases,
)
# Decorated Permutations
from sage.combinat.decorated_permutation import (
    DecoratedPermutation as DecoratedPermutation,
    DecoratedPermutations as DecoratedPermutations,
)
# Plane Partitions
from sage.combinat.plane_partition import (
    PlanePartition as PlanePartition,
    PlanePartitions as PlanePartitions,
)
# Parking Functions
from sage.combinat.non_decreasing_parking_function import (
    NonDecreasingParkingFunctions as NonDecreasingParkingFunctions,
    NonDecreasingParkingFunction as NonDecreasingParkingFunction,
)
from sage.combinat.parking_functions import (
    ParkingFunctions as ParkingFunctions,
    ParkingFunction as ParkingFunction,
)

# Trees and Tamari interval posets
from sage.combinat.ordered_tree import (
    OrderedTree as OrderedTree,
    OrderedTrees as OrderedTrees,
    LabelledOrderedTree as LabelledOrderedTree,
    LabelledOrderedTrees as LabelledOrderedTrees,
)
from sage.combinat.binary_tree import (
    BinaryTree as BinaryTree,
    BinaryTrees as BinaryTrees,
    LabelledBinaryTree as LabelledBinaryTree,
    LabelledBinaryTrees as LabelledBinaryTrees,
)
from sage.combinat.interval_posets import (
    TamariIntervalPoset as TamariIntervalPoset,
    TamariIntervalPosets as TamariIntervalPosets,
)
from sage.combinat.rooted_tree import (
    RootedTree as RootedTree,
    RootedTrees as RootedTrees,
    LabelledRootedTree as LabelledRootedTree,
    LabelledRootedTrees as LabelledRootedTrees,
)
from sage.combinat.combination import Combinations as Combinations

from sage.combinat.set_partition import (
    SetPartition as SetPartition,
    SetPartitions as SetPartitions,
)
from sage.combinat.set_partition_ordered import (
    OrderedSetPartition as OrderedSetPartition,
    OrderedSetPartitions as OrderedSetPartitions,
)
from sage.combinat.multiset_partition_into_sets_ordered import (
    OrderedMultisetPartitionIntoSets as OrderedMultisetPartitionIntoSets,
    OrderedMultisetPartitionsIntoSets as OrderedMultisetPartitionsIntoSets,
)
from sage.combinat.subset import (
    Subsets as Subsets,
    subsets as subsets,
    powerset as powerset,
    uniq as uniq,
)
from sage.combinat.necklace import Necklaces as Necklaces
from sage.combinat.dyck_word import (
    DyckWords as DyckWords,
    DyckWord as DyckWord,
)
from sage.combinat.nu_dyck_word import (
    NuDyckWords as NuDyckWords,
    NuDyckWord as NuDyckWord,
)
from sage.combinat.sloane_functions import sloane as sloane
from sage.combinat.superpartition import (
    SuperPartition as SuperPartition,
    SuperPartitions as SuperPartitions,
)

from sage.combinat.parallelogram_polyomino import (
    ParallelogramPolyomino as ParallelogramPolyomino,
    ParallelogramPolyominoes as ParallelogramPolyominoes,
)

from sage.combinat.root_system.all import *
from sage.combinat.sf.all import *
from sage.combinat.ncsf_qsym.all import *
from sage.combinat.ncsym.all import *
from sage.combinat.fqsym import FreeQuasisymmetricFunctions as FreeQuasisymmetricFunctions
from sage.combinat.matrices.all import *
# Posets
from sage.combinat.posets.all import *

# Cluster Algebras and Quivers
from sage.combinat.cluster_algebra_quiver.all import *

from sage.combinat import ranker as ranker

from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.combinat.integer_vectors_mod_permgroup import IntegerVectorsModPermutationGroup as IntegerVectorsModPermutationGroup

from sage.combinat.q_analogues import (
    gaussian_binomial as gaussian_binomial,
    q_binomial as q_binomial,
    number_of_irreducible_polynomials as number_of_irreducible_polynomials,
)

from sage.combinat.species.all import *

from sage.combinat.kazhdan_lusztig import KazhdanLusztigPolynomial as KazhdanLusztigPolynomial

from sage.combinat.degree_sequences import DegreeSequences as DegreeSequences

from sage.combinat.cyclic_sieving_phenomenon import (
    CyclicSievingPolynomial as CyclicSievingPolynomial,
    CyclicSievingCheck as CyclicSievingCheck,
)

from sage.combinat.sidon_sets import sidon_sets as sidon_sets
# Puzzles
from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver as KnutsonTaoPuzzleSolver
# Gelfand-Tsetlin patterns
from sage.combinat.gelfand_tsetlin_patterns import (
    GelfandTsetlinPattern as GelfandTsetlinPattern,
    GelfandTsetlinPatterns as GelfandTsetlinPatterns,
)

# Finite State Machines (Automaton, Transducer)
from sage.combinat.finite_state_machine import (
    Automaton as Automaton,
    Transducer as Transducer,
    FiniteStateMachine as FiniteStateMachine,
)
from sage.combinat.finite_state_machine_generators import (
    automata as automata,
    transducers as transducers,
)
# Sequences
from sage.combinat.binary_recurrence_sequences import BinaryRecurrenceSequence as BinaryRecurrenceSequence
from sage.combinat.recognizable_series import RecognizableSeriesSpace as RecognizableSeriesSpace
from sage.combinat.regular_sequence import RegularSequenceRing as RegularSequenceRing
# Six Vertex Model
from sage.combinat.six_vertex_model import SixVertexModel as SixVertexModel
# sine-Gordon Y-systems
from sage.combinat.sine_gordon import SineGordonYsystem as SineGordonYsystem
# Fully Packed Loop
from sage.combinat.fully_packed_loop import (
    FullyPackedLoop as FullyPackedLoop,
    FullyPackedLoops as FullyPackedLoops,
)
# Subword complex and cluster complex
from sage.combinat.subword_complex import SubwordComplex as SubwordComplex
from sage.combinat.cluster_complex import ClusterComplex as ClusterComplex
# Constellations
from sage.combinat.constellation import (
    Constellation as Constellation,
    Constellations as Constellations,
)
# Growth diagrams
from sage.combinat.growth import GrowthDiagram as GrowthDiagram
# Path Tableaux
from sage.combinat.path_tableaux import catalog as _path_tableaux_catalog
path_tableaux = _path_tableaux_catalog

# Bijectionist
from sage.combinat.bijectionist import Bijectionist as Bijectionist
