import cypari2.pari_instance
import sage.functions.prime_pi
import sage.misc.lazy_import
import sage.structure.coerce
import sage.symbolic.expression
from sage.algebras.affine_nil_temperley_lieb import AffineNilTemperleyLiebTypeA as AffineNilTemperleyLiebTypeA
from sage.algebras.clifford_algebra import CliffordAlgebra as CliffordAlgebra, ExteriorAlgebra as ExteriorAlgebra
from sage.algebras.cluster_algebra import ClusterAlgebra as ClusterAlgebra
from sage.algebras.commutative_dga import GradedCommutativeAlgebra as GradedCommutativeAlgebra
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra import FiniteDimensionalAlgebra as FiniteDimensionalAlgebra
from sage.algebras.free_algebra import FreeAlgebra as FreeAlgebra
from sage.algebras.free_algebra_quotient import FreeAlgebraQuotient as FreeAlgebraQuotient
from sage.algebras.fusion_rings.fusion_double import FusionDouble as FusionDouble
from sage.algebras.fusion_rings.fusion_ring import FusionRing as FusionRing
from sage.algebras.group_algebra import GroupAlgebra as GroupAlgebra
from sage.algebras.hall_algebra import HallAlgebra as HallAlgebra
from sage.algebras.iwahori_hecke_algebra import IwahoriHeckeAlgebra as IwahoriHeckeAlgebra
from sage.algebras.jordan_algebra import JordanAlgebra as JordanAlgebra
from sage.algebras.lie_algebras.lie_algebra import LieAlgebra as LieAlgebra
from sage.algebras.lie_conformal_algebras.lie_conformal_algebra import LieConformalAlgebra as LieConformalAlgebra
from sage.algebras.nil_coxeter_algebra import NilCoxeterAlgebra as NilCoxeterAlgebra
from sage.algebras.octonion_algebra import OctonionAlgebra as OctonionAlgebra
from sage.algebras.q_system import QSystem as QSystem
from sage.algebras.quantum_groups.fock_space import FockSpace as FockSpace
from sage.algebras.quantum_groups.quantum_group_gap import QuantumGroup as QuantumGroup
from sage.algebras.quatalg.quaternion_algebra import QuaternionAlgebra as QuaternionAlgebra
from sage.algebras.rational_cherednik_algebra import RationalCherednikAlgebra as RationalCherednikAlgebra
from sage.algebras.schur_algebra import SchurAlgebra as SchurAlgebra, SchurTensorModule as SchurTensorModule
from sage.algebras.shuffle_algebra import ShuffleAlgebra as ShuffleAlgebra
from sage.algebras.steenrod.steenrod_algebra import Sq as Sq, SteenrodAlgebra as SteenrodAlgebra
from sage.algebras.tensor_algebra import TensorAlgebra as TensorAlgebra
from sage.algebras.weyl_algebra import DifferentialWeylAlgebra as DifferentialWeylAlgebra
from sage.algebras.yangian import Yangian as Yangian
from sage.arith.functions import LCM as LCM, lcm as lcm
from sage.arith.misc import CRT as CRT, CRT_basis as CRT_basis, CRT_list as CRT_list, CRT_vectors as CRT_vectors, GCD as GCD, algdep as algdep, algebraic_dependency as algebraic_dependency, bernoulli as bernoulli, binomial_coefficients as binomial_coefficients, carmichael_lambda as carmichael_lambda, continuant as continuant, crt as crt, dedekind_sum as dedekind_sum, differences as differences, divisors as divisors, eratosthenes as eratosthenes, euler_phi as euler_phi, factor as factor, falling_factorial as falling_factorial, four_squares as four_squares, fundamental_discriminant as fundamental_discriminant, gcd as gcd, get_gcd as get_gcd, get_inverse_mod as get_inverse_mod, hilbert_conductor as hilbert_conductor, hilbert_conductor_inverse as hilbert_conductor_inverse, hilbert_symbol as hilbert_symbol, integer_ceil as integer_ceil, integer_floor as integer_floor, inverse_mod as inverse_mod, is_power_of_two as is_power_of_two, is_prime as is_prime, is_prime_power as is_prime_power, is_pseudoprime as is_pseudoprime, is_pseudoprime_power as is_pseudoprime_power, is_square as is_square, is_squarefree as is_squarefree, jacobi_symbol as jacobi_symbol, kronecker as kronecker, kronecker_symbol as kronecker_symbol, legendre_symbol as legendre_symbol, moebius as moebius, mqrr_rational_reconstruction as mqrr_rational_reconstruction, multinomial as multinomial, multinomial_coefficients as multinomial_coefficients, next_prime as next_prime, next_prime_power as next_prime_power, next_probable_prime as next_probable_prime, nth_prime as nth_prime, number_of_divisors as number_of_divisors, odd_part as odd_part, power_mod as power_mod, previous_prime as previous_prime, previous_prime_power as previous_prime_power, prime_divisors as prime_divisors, prime_factors as prime_factors, prime_powers as prime_powers, prime_to_m_part as prime_to_m_part, primes as primes, primes_first_n as primes_first_n, primitive_root as primitive_root, quadratic_residues as quadratic_residues, radical as radical, random_prime as random_prime, rational_reconstruction as rational_reconstruction, rising_factorial as rising_factorial, sigma as sigma, sort_complex_numbers_for_display as sort_complex_numbers_for_display, squarefree_divisors as squarefree_divisors, subfactorial as subfactorial, sum_of_k_squares as sum_of_k_squares, three_squares as three_squares, trial_division as trial_division, two_squares as two_squares, valuation as valuation, xgcd as xgcd, xkcd as xkcd, xlcm as xlcm, σ as σ
from sage.arith.power import generic_power as power
from sage.arith.srange import ellipsis_iter as ellipsis_iter, ellipsis_range as ellipsis_range, srange as srange, sxrange as sxrange, xsrange as xsrange
from sage.calculus.calculus import inverse_laplace as inverse_laplace, laplace as laplace, lim as lim, limit as limit
from sage.calculus.desolvers import desolve as desolve, desolve_laplace as desolve_laplace, desolve_mintides as desolve_mintides, desolve_odeint as desolve_odeint, desolve_rk4 as desolve_rk4, desolve_system as desolve_system, desolve_system_rk4 as desolve_system_rk4, desolve_tides_mpfr as desolve_tides_mpfr, eulers_method as eulers_method, eulers_method_2x2 as eulers_method_2x2, eulers_method_2x2_plot as eulers_method_2x2_plot
from sage.calculus.expr import symbolic_expression as symbolic_expression
from sage.calculus.functional import derivative as derivative, diff as diff, expand as expand, simplify as simplify, taylor as taylor
from sage.calculus.functions import jacobian as jacobian, wronskian as wronskian
from sage.calculus.integration import integral_numerical as integral_numerical, monte_carlo_integral as monte_carlo_integral, numerical_integral as numerical_integral
from sage.calculus.interpolation import Spline as Spline, spline as spline
from sage.calculus.interpolators import complex_cubic_spline as complex_cubic_spline, polygon_spline as polygon_spline
from sage.calculus.ode import ode_solver as ode_solver, ode_system as ode_system
from sage.calculus.riemann import Riemann_Map as Riemann_Map
from sage.calculus.transforms.dft import IndexedSequence as IndexedSequence
from sage.calculus.transforms.dwt import DWT as DWT, WaveletTransform as WaveletTransform
from sage.calculus.transforms.fft import FFT as FFT, FastFourierTransform as FastFourierTransform
from sage.calculus.var import clear_vars as clear_vars, function as function, var as var
from sage.categories.additive_magmas import AdditiveMagmas as AdditiveMagmas
from sage.categories.affine_weyl_groups import AffineWeylGroups as AffineWeylGroups
from sage.categories.algebra_ideals import AlgebraIdeals as AlgebraIdeals
from sage.categories.algebra_modules import AlgebraModules as AlgebraModules
from sage.categories.algebras import Algebras as Algebras
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.categories.bialgebras import Bialgebras as Bialgebras
from sage.categories.bialgebras_with_basis import BialgebrasWithBasis as BialgebrasWithBasis
from sage.categories.bimodules import Bimodules as Bimodules
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.category import CDF as CDF, Category as Category, RDF as RDF, RIF as RIF, RR as RR, ZZ as ZZ
from sage.categories.category_types import Elements as Elements
from sage.categories.chain_complexes import ChainComplexes as ChainComplexes, HomologyFunctor as HomologyFunctor
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.coalgebras import Coalgebras as Coalgebras
from sage.categories.coalgebras_with_basis import CoalgebrasWithBasis as CoalgebrasWithBasis
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.commutative_additive_monoids import CommutativeAdditiveMonoids as CommutativeAdditiveMonoids
from sage.categories.commutative_additive_semigroups import CommutativeAdditiveSemigroups as CommutativeAdditiveSemigroups
from sage.categories.commutative_algebra_ideals import CommutativeAlgebraIdeals as CommutativeAlgebraIdeals
from sage.categories.commutative_algebras import CommutativeAlgebras as CommutativeAlgebras
from sage.categories.commutative_ring_ideals import CommutativeRingIdeals as CommutativeRingIdeals
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings, NaN as NaN, SR as SR, catalan as catalan, e as e, euler_gamma as euler_gamma, glaisher as glaisher, golden_ratio as golden_ratio, khinchin as khinchin, log2 as log2, mertens as mertens, pi as pi, twinprime as twinprime, π as π
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationFields as CompleteDiscreteValuationFields, CompleteDiscreteValuationRings as CompleteDiscreteValuationRings
from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.categories.crystals import Crystals as Crystals
from sage.categories.dedekind_domains import DedekindDomains as DedekindDomains
from sage.categories.discrete_valuation import DiscreteValuationFields as DiscreteValuationFields, DiscreteValuationRings as DiscreteValuationRings
from sage.categories.division_rings import DivisionRings as DivisionRings
from sage.categories.domains import Domains as Domains
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.euclidean_domains import EuclideanDomains as EuclideanDomains
from sage.categories.fields import Fields as Fields
from sage.categories.finite_coxeter_groups import FiniteCoxeterGroups as FiniteCoxeterGroups
from sage.categories.finite_crystals import FiniteCrystals as FiniteCrystals
from sage.categories.finite_dimensional_algebras_with_basis import FiniteDimensionalAlgebrasWithBasis as FiniteDimensionalAlgebrasWithBasis
from sage.categories.finite_dimensional_bialgebras_with_basis import FiniteDimensionalBialgebrasWithBasis as FiniteDimensionalBialgebrasWithBasis
from sage.categories.finite_dimensional_coalgebras_with_basis import FiniteDimensionalCoalgebrasWithBasis as FiniteDimensionalCoalgebrasWithBasis
from sage.categories.finite_dimensional_hopf_algebras_with_basis import FiniteDimensionalHopfAlgebrasWithBasis as FiniteDimensionalHopfAlgebrasWithBasis
from sage.categories.finite_dimensional_modules_with_basis import FiniteDimensionalModulesWithBasis as FiniteDimensionalModulesWithBasis
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.categories.finite_groups import FiniteGroups as FiniteGroups
from sage.categories.finite_lattice_posets import FiniteLatticePosets as FiniteLatticePosets
from sage.categories.finite_monoids import FiniteMonoids as FiniteMonoids
from sage.categories.finite_permutation_groups import FinitePermutationGroups as FinitePermutationGroups
from sage.categories.finite_posets import FinitePosets as FinitePosets
from sage.categories.finite_semigroups import FiniteSemigroups as FiniteSemigroups
from sage.categories.finite_sets import FiniteSets as FiniteSets
from sage.categories.finite_weyl_groups import FiniteWeylGroups as FiniteWeylGroups
from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.categories.functor import ForgetfulFunctor as ForgetfulFunctor, IdentityFunctor as IdentityFunctor
from sage.categories.g_sets import GSets as GSets
from sage.categories.gcd_domains import GcdDomains as GcdDomains
from sage.categories.graded_algebras import GradedAlgebras as GradedAlgebras
from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.categories.graded_bialgebras import GradedBialgebras as GradedBialgebras
from sage.categories.graded_bialgebras_with_basis import GradedBialgebrasWithBasis as GradedBialgebrasWithBasis
from sage.categories.graded_coalgebras import GradedCoalgebras as GradedCoalgebras
from sage.categories.graded_coalgebras_with_basis import GradedCoalgebrasWithBasis as GradedCoalgebrasWithBasis
from sage.categories.graded_hopf_algebras import GradedHopfAlgebras as GradedHopfAlgebras
from sage.categories.graded_hopf_algebras_with_basis import GradedHopfAlgebrasWithBasis as GradedHopfAlgebrasWithBasis
from sage.categories.graded_modules import GradedModules as GradedModules
from sage.categories.graded_modules_with_basis import GradedModulesWithBasis as GradedModulesWithBasis
from sage.categories.group_algebras import GroupAlgebras as GroupAlgebras
from sage.categories.groupoid import Groupoid as Groupoid
from sage.categories.groups import Groups as Groups
from sage.categories.hecke_modules import HeckeModules as HeckeModules
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.homset import End as End, Hom as Hom, Homset as Homset, HomsetWithBase as HomsetWithBase, end as end, hom as hom
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.hopf_algebras_with_basis import HopfAlgebrasWithBasis as HopfAlgebrasWithBasis
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.lattice_posets import LatticePosets as LatticePosets
from sage.categories.left_modules import LeftModules as LeftModules
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras
from sage.categories.magmas import Magmas as Magmas
from sage.categories.matrix_algebras import MatrixAlgebras as MatrixAlgebras
from sage.categories.modular_abelian_varieties import ModularAbelianVarieties as ModularAbelianVarieties
from sage.categories.modules import Modules as Modules, RingModules as RingModules
from sage.categories.modules_with_basis import FreeModules as FreeModules, ModulesWithBasis as ModulesWithBasis
from sage.categories.monoid_algebras import MonoidAlgebras as MonoidAlgebras
from sage.categories.monoids import Monoids as Monoids
from sage.categories.morphism import Morphism as Morphism
from sage.categories.number_fields import I as I, NumberFields as NumberFields, i as i
from sage.categories.objects import Objects as Objects
from sage.categories.partially_ordered_monoids import OrderedMonoids as OrderedMonoids, PartiallyOrderedMonoids as PartiallyOrderedMonoids
from sage.categories.permutation_groups import PermutationGroups as PermutationGroups
from sage.categories.pointed_sets import PointedSets as PointedSets
from sage.categories.polyhedra import PolyhedralSets as PolyhedralSets
from sage.categories.posets import OrderedSets as OrderedSets, PartiallyOrderedSets as PartiallyOrderedSets
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.categories.quotient_fields import QuotientFields as QuotientFields
from sage.categories.realizations import Realizations as Realizations
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.categories.right_modules import RightModules as RightModules
from sage.categories.ring_ideals import Ideals as Ideals, RingIdeals as RingIdeals
from sage.categories.rings import Rings as Rings
from sage.categories.rngs import Rngs as Rngs
from sage.categories.schemes import AbelianVarieties as AbelianVarieties, Jacobians as Jacobians, Schemes as Schemes
from sage.categories.semigroups import Semigroups as Semigroups
from sage.categories.semirings import Semirings as Semirings
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.categories.sets_with_partial_maps import SetsWithPartialMaps as SetsWithPartialMaps
from sage.categories.signed_tensor import tensor_signed as tensor_signed
from sage.categories.simplicial_complexes import SimplicialComplexes as SimplicialComplexes
from sage.categories.tensor import tensor as tensor
from sage.categories.unique_factorization_domains import UniqueFactorizationDomains as UniqueFactorizationDomains
from sage.categories.vector_spaces import VectorSpaces as VectorSpaces
from sage.categories.weyl_groups import WeylGroups as WeylGroups
from sage.coding.code_constructions import permutation_action as permutation_action, walsh_matrix as walsh_matrix
from sage.coding.linear_code import LinearCode as LinearCode
from sage.combinat.affine_permutation import AffinePermutationGroup as AffinePermutationGroup
from sage.combinat.alternating_sign_matrix import AlternatingSignMatrices as AlternatingSignMatrices, AlternatingSignMatrix as AlternatingSignMatrix, ContreTableaux as ContreTableaux, MonotoneTriangles as MonotoneTriangles, TruncatedStaircases as TruncatedStaircases
from sage.combinat.baxter_permutations import BaxterPermutations as BaxterPermutations
from sage.combinat.bijectionist import Bijectionist as Bijectionist
from sage.combinat.binary_recurrence_sequences import BinaryRecurrenceSequence as BinaryRecurrenceSequence
from sage.combinat.binary_tree import BinaryTree as BinaryTree, BinaryTrees as BinaryTrees, LabelledBinaryTree as LabelledBinaryTree, LabelledBinaryTrees as LabelledBinaryTrees
from sage.combinat.chas.fsym import FreeSymmetricFunctions as FreeSymmetricFunctions
from sage.combinat.chas.wqsym import WordQuasiSymmetricFunctions as WordQuasiSymmetricFunctions
from sage.combinat.cluster_algebra_quiver.cluster_seed import ClusterSeed as ClusterSeed
from sage.combinat.cluster_algebra_quiver.quiver import ClusterQuiver as ClusterQuiver
from sage.combinat.cluster_algebra_quiver.quiver_mutation_type import QuiverMutationType as QuiverMutationType
from sage.combinat.cluster_complex import ClusterComplex as ClusterComplex
from sage.combinat.colored_permutations import ColoredPermutations as ColoredPermutations, SignedPermutation as SignedPermutation, SignedPermutations as SignedPermutations
from sage.combinat.combinat import CombinatorialObject as CombinatorialObject, bell_number as bell_number, bell_polynomial as bell_polynomial, bernoulli_polynomial as bernoulli_polynomial, catalan_number as catalan_number, euler_number as euler_number, fibonacci as fibonacci, fibonacci_sequence as fibonacci_sequence, fibonacci_xrange as fibonacci_xrange, lucas_number1 as lucas_number1, lucas_number2 as lucas_number2, number_of_tuples as number_of_tuples, number_of_unordered_tuples as number_of_unordered_tuples, polygonal_number as polygonal_number, stirling_number1 as stirling_number1, stirling_number2 as stirling_number2, tuples as tuples, unordered_tuples as unordered_tuples
from sage.combinat.combination import Combinations as Combinations
from sage.combinat.composition import Composition as Composition, Compositions as Compositions
from sage.combinat.composition_signed import SignedCompositions as SignedCompositions
from sage.combinat.composition_tableau import CompositionTableau as CompositionTableau, CompositionTableaux as CompositionTableaux
from sage.combinat.constellation import Constellation as Constellation, Constellations as Constellations
from sage.combinat.core import Core as Core, Cores as Cores
from sage.combinat.cyclic_sieving_phenomenon import CyclicSievingCheck as CyclicSievingCheck, CyclicSievingPolynomial as CyclicSievingPolynomial
from sage.combinat.debruijn_sequence import DeBruijnSequences as DeBruijnSequences
from sage.combinat.decorated_permutation import DecoratedPermutation as DecoratedPermutation, DecoratedPermutations as DecoratedPermutations
from sage.combinat.degree_sequences import DegreeSequences as DegreeSequences
from sage.combinat.derangements import Derangements as Derangements
from sage.combinat.descent_algebra import DescentAlgebra as DescentAlgebra
from sage.combinat.designs.covering_design import CoveringDesign as CoveringDesign, schonheim as schonheim, trivial_covering_design as trivial_covering_design
from sage.combinat.designs.incidence_structures import BlockDesign as BlockDesign, Hypergraph as Hypergraph, IncidenceStructure as IncidenceStructure
from sage.combinat.diagram_algebras import BrauerAlgebra as BrauerAlgebra, PartitionAlgebra as PartitionAlgebra, PlanarAlgebra as PlanarAlgebra, PropagatingIdeal as PropagatingIdeal, TemperleyLiebAlgebra as TemperleyLiebAlgebra
from sage.combinat.dlx import AllExactCovers as AllExactCovers, DLXMatrix as DLXMatrix, OneExactCover as OneExactCover
from sage.combinat.dyck_word import DyckWord as DyckWord, DyckWords as DyckWords
from sage.combinat.expnums import expnums as expnums
from sage.combinat.finite_state_machine import Automaton as Automaton, FiniteStateMachine as FiniteStateMachine, Transducer as Transducer
from sage.combinat.finite_state_machine_generators import automata as automata, transducers as transducers
from sage.combinat.fqsym import FreeQuasisymmetricFunctions as FreeQuasisymmetricFunctions
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.fully_packed_loop import FullyPackedLoop as FullyPackedLoop, FullyPackedLoops as FullyPackedLoops
from sage.combinat.gelfand_tsetlin_patterns import GelfandTsetlinPattern as GelfandTsetlinPattern, GelfandTsetlinPatterns as GelfandTsetlinPatterns
from sage.combinat.graph_path import GraphPaths as GraphPaths
from sage.combinat.growth import GrowthDiagram as GrowthDiagram
from sage.combinat.hillman_grassl import WeakReversePlanePartition as WeakReversePlanePartition, WeakReversePlanePartitions as WeakReversePlanePartitions
from sage.combinat.integer_lists.invlex import IntegerListsLex as IntegerListsLex
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors as WeightedIntegerVectors
from sage.combinat.integer_vectors_mod_permgroup import IntegerVectorsModPermutationGroup as IntegerVectorsModPermutationGroup
from sage.combinat.interval_posets import TamariIntervalPoset as TamariIntervalPoset, TamariIntervalPosets as TamariIntervalPosets
from sage.combinat.k_tableau import StrongTableau as StrongTableau, StrongTableaux as StrongTableaux, WeakTableau as WeakTableau, WeakTableaux as WeakTableaux
from sage.combinat.kazhdan_lusztig import KazhdanLusztigPolynomial as KazhdanLusztigPolynomial
from sage.combinat.key_polynomial import KeyPolynomials as KeyPolynomials
from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver as KnutsonTaoPuzzleSolver
from sage.combinat.lr_tableau import LittlewoodRichardsonTableau as LittlewoodRichardsonTableau, LittlewoodRichardsonTableaux as LittlewoodRichardsonTableaux
from sage.combinat.matrices.dlxcpp import DLXCPP as DLXCPP
from sage.combinat.matrices.hadamard_matrix import hadamard_matrix as hadamard_matrix, hadamard_matrix_www as hadamard_matrix_www
from sage.combinat.matrices.latin import LatinSquare as LatinSquare, LatinSquare_generator as LatinSquare_generator
from sage.combinat.multiset_partition_into_sets_ordered import OrderedMultisetPartitionIntoSets as OrderedMultisetPartitionIntoSets, OrderedMultisetPartitionsIntoSets as OrderedMultisetPartitionsIntoSets
from sage.combinat.ncsf_qsym.ncsf import NonCommutativeSymmetricFunctions as NonCommutativeSymmetricFunctions
from sage.combinat.ncsf_qsym.qsym import QuasiSymmetricFunctions as QuasiSymmetricFunctions
from sage.combinat.ncsym.dual import SymmetricFunctionsNonCommutingVariablesDual as SymmetricFunctionsNonCommutingVariablesDual
from sage.combinat.ncsym.ncsym import SymmetricFunctionsNonCommutingVariables as SymmetricFunctionsNonCommutingVariables
from sage.combinat.necklace import Necklaces as Necklaces
from sage.combinat.non_decreasing_parking_function import NonDecreasingParkingFunction as NonDecreasingParkingFunction, NonDecreasingParkingFunctions as NonDecreasingParkingFunctions
from sage.combinat.nu_dyck_word import NuDyckWord as NuDyckWord, NuDyckWords as NuDyckWords
from sage.combinat.ordered_tree import LabelledOrderedTree as LabelledOrderedTree, LabelledOrderedTrees as LabelledOrderedTrees, OrderedTree as OrderedTree, OrderedTrees as OrderedTrees
from sage.combinat.parallelogram_polyomino import ParallelogramPolyomino as ParallelogramPolyomino, ParallelogramPolyominoes as ParallelogramPolyominoes
from sage.combinat.parking_functions import ParkingFunction as ParkingFunction, ParkingFunctions as ParkingFunctions
from sage.combinat.partition import OrderedPartitions as OrderedPartitions, Partition as Partition, Partitions as Partitions, PartitionsGreatestEQ as PartitionsGreatestEQ, PartitionsGreatestLE as PartitionsGreatestLE, PartitionsInBox as PartitionsInBox, number_of_partitions as number_of_partitions
from sage.combinat.partition_algebra import SetPartitionsAk as SetPartitionsAk, SetPartitionsBk as SetPartitionsBk, SetPartitionsIk as SetPartitionsIk, SetPartitionsPRk as SetPartitionsPRk, SetPartitionsPk as SetPartitionsPk, SetPartitionsRk as SetPartitionsRk, SetPartitionsSk as SetPartitionsSk, SetPartitionsTk as SetPartitionsTk
from sage.combinat.partition_kleshchev import KleshchevPartitions as KleshchevPartitions
from sage.combinat.partition_shifting_algebras import ShiftingOperatorAlgebra as ShiftingOperatorAlgebra
from sage.combinat.partition_tuple import PartitionTuple as PartitionTuple, PartitionTuples as PartitionTuples
from sage.combinat.perfect_matching import PerfectMatching as PerfectMatching, PerfectMatchings as PerfectMatchings
from sage.combinat.permutation import Arrangements as Arrangements, CyclicPermutations as CyclicPermutations, CyclicPermutationsOfPartition as CyclicPermutationsOfPartition, Permutation as Permutation, Permutations as Permutations
from sage.combinat.plane_partition import PlanePartition as PlanePartition, PlanePartitions as PlanePartitions
from sage.combinat.posets.lattices import JoinSemilattice as JoinSemilattice, LatticePoset as LatticePoset, MeetSemilattice as MeetSemilattice
from sage.combinat.posets.poset_examples import Posets as Posets, posets as posets
from sage.combinat.posets.posets import Poset as Poset
from sage.combinat.q_analogues import gaussian_binomial as gaussian_binomial, number_of_irreducible_polynomials as number_of_irreducible_polynomials, q_binomial as q_binomial
from sage.combinat.recognizable_series import RecognizableSeriesSpace as RecognizableSeriesSpace
from sage.combinat.regular_sequence import RegularSequenceRing as RegularSequenceRing
from sage.combinat.ribbon_shaped_tableau import RibbonShapedTableau as RibbonShapedTableau, RibbonShapedTableaux as RibbonShapedTableaux, StandardRibbonShapedTableaux as StandardRibbonShapedTableaux
from sage.combinat.ribbon_tableau import MultiSkewTableau as MultiSkewTableau, MultiSkewTableaux as MultiSkewTableaux, RibbonTableau as RibbonTableau, RibbonTableaux as RibbonTableaux, SemistandardMultiSkewTableaux as SemistandardMultiSkewTableaux
from sage.combinat.rigged_configurations.rigged_configurations import RiggedConfigurations as RiggedConfigurations
from sage.combinat.root_system.branching_rules import BranchingRule as BranchingRule, branching_rule as branching_rule, branching_rule_from_plethysm as branching_rule_from_plethysm
from sage.combinat.root_system.cartan_matrix import CartanMatrix as CartanMatrix
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.coxeter_group import CoxeterGroup as CoxeterGroup
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix as CoxeterMatrix
from sage.combinat.root_system.coxeter_type import CoxeterType as CoxeterType
from sage.combinat.root_system.dynkin_diagram import DynkinDiagram as DynkinDiagram
from sage.combinat.root_system.extended_affine_weyl_group import ExtendedAffineWeylGroup as ExtendedAffineWeylGroup
from sage.combinat.root_system.integrable_representations import IntegrableRepresentation as IntegrableRepresentation
from sage.combinat.root_system.non_symmetric_macdonald_polynomials import NonSymmetricMacdonaldPolynomials as NonSymmetricMacdonaldPolynomials
from sage.combinat.root_system.reflection_group_real import ReflectionGroup as ReflectionGroup
from sage.combinat.root_system.root_system import RootSystem as RootSystem, WeylDim as WeylDim
from sage.combinat.root_system.weyl_characters import WeightRing as WeightRing, WeylCharacterRing as WeylCharacterRing
from sage.combinat.root_system.weyl_group import WeylGroup as WeylGroup, WeylGroupElement as WeylGroupElement
from sage.combinat.rooted_tree import LabelledRootedTree as LabelledRootedTree, LabelledRootedTrees as LabelledRootedTrees, RootedTree as RootedTree, RootedTrees as RootedTrees
from sage.combinat.rsk import InsertionRules as InsertionRules, RSK as RSK, RSK_inverse as RSK_inverse, robinson_schensted_knuth as robinson_schensted_knuth, robinson_schensted_knuth_inverse as robinson_schensted_knuth_inverse
from sage.combinat.schubert_polynomial import SchubertPolynomialRing as SchubertPolynomialRing
from sage.combinat.set_partition import SetPartition as SetPartition, SetPartitions as SetPartitions
from sage.combinat.set_partition_ordered import OrderedSetPartition as OrderedSetPartition, OrderedSetPartitions as OrderedSetPartitions
from sage.combinat.sf.kfpoly import KostkaFoulkesPolynomial as KostkaFoulkesPolynomial
from sage.combinat.sf.ns_macdonald import AugmentedLatticeDiagramFilling as AugmentedLatticeDiagramFilling, LatticeDiagram as LatticeDiagram, NonattackingFillings as NonattackingFillings
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.combinat.shifted_primed_tableau import ShiftedPrimedTableau as ShiftedPrimedTableau, ShiftedPrimedTableaux as ShiftedPrimedTableaux
from sage.combinat.sidon_sets import sidon_sets as sidon_sets
from sage.combinat.similarity_class_type import PrimarySimilarityClassType as PrimarySimilarityClassType, PrimarySimilarityClassTypes as PrimarySimilarityClassTypes, SimilarityClassType as SimilarityClassType, SimilarityClassTypes as SimilarityClassTypes
from sage.combinat.sine_gordon import SineGordonYsystem as SineGordonYsystem
from sage.combinat.six_vertex_model import SixVertexModel as SixVertexModel
from sage.combinat.skew_partition import SkewPartition as SkewPartition, SkewPartitions as SkewPartitions
from sage.combinat.skew_tableau import SemistandardSkewTableaux as SemistandardSkewTableaux, SkewTableau as SkewTableau, SkewTableaux as SkewTableaux, StandardSkewTableaux as StandardSkewTableaux
from sage.combinat.sloane_functions import sloane as sloane
from sage.combinat.species.recursive_species import CombinatorialSpecies as CombinatorialSpecies
from sage.combinat.subset import Subsets as Subsets, powerset as powerset, subsets as subsets, uniq as uniq
from sage.combinat.subword import Subwords as Subwords
from sage.combinat.subword_complex import SubwordComplex as SubwordComplex
from sage.combinat.super_tableau import SemistandardSuperTableau as SemistandardSuperTableau, SemistandardSuperTableaux as SemistandardSuperTableaux, StandardSuperTableau as StandardSuperTableau, StandardSuperTableaux as StandardSuperTableaux
from sage.combinat.superpartition import SuperPartition as SuperPartition, SuperPartitions as SuperPartitions
from sage.combinat.symmetric_group_algebra import HeckeAlgebraSymmetricGroupT as HeckeAlgebraSymmetricGroupT, SymmetricGroupAlgebra as SymmetricGroupAlgebra
from sage.combinat.symmetric_group_representations import SymmetricGroupRepresentation as SymmetricGroupRepresentation, SymmetricGroupRepresentations as SymmetricGroupRepresentations
from sage.combinat.tableau import IncreasingTableau as IncreasingTableau, IncreasingTableaux as IncreasingTableaux, RowStandardTableau as RowStandardTableau, RowStandardTableaux as RowStandardTableaux, SemistandardTableau as SemistandardTableau, SemistandardTableaux as SemistandardTableaux, StandardTableau as StandardTableau, StandardTableaux as StandardTableaux, Tableau as Tableau, Tableaux as Tableaux
from sage.combinat.tableau_tuple import RowStandardTableauTuple as RowStandardTableauTuple, RowStandardTableauTuples as RowStandardTableauTuples, StandardTableauTuple as StandardTableauTuple, StandardTableauTuples as StandardTableauTuples, TableauTuple as TableauTuple, TableauTuples as TableauTuples
from sage.combinat.tuple import Tuples as Tuples, UnorderedTuples as UnorderedTuples
from sage.combinat.vector_partition import VectorPartition as VectorPartition, VectorPartitions as VectorPartitions
from sage.combinat.words.alphabet import Alphabet as Alphabet, build_alphabet as build_alphabet
from sage.combinat.words.lyndon_word import LyndonWord as LyndonWord, LyndonWords as LyndonWords, StandardBracketedLyndonWords as StandardBracketedLyndonWords
from sage.combinat.words.morphism import WordMorphism as WordMorphism
from sage.combinat.words.paths import WordPaths as WordPaths
from sage.combinat.words.word import Word as Word
from sage.combinat.words.word_generators import words as words
from sage.combinat.words.word_options import WordOptions as WordOptions
from sage.combinat.words.words import FiniteWords as FiniteWords, InfiniteWords as InfiniteWords, Words as Words
from sage.combinat.yang_baxter_graph import YangBaxterGraph as YangBaxterGraph
from sage.cpython.debug import getattr_debug as getattr_debug, type_debug as type_debug
from sage.cpython.getattr import raw_getattr as raw_getattr
from sage.crypto.classical import AffineCryptosystem as AffineCryptosystem, HillCryptosystem as HillCryptosystem, ShiftCryptosystem as ShiftCryptosystem, SubstitutionCryptosystem as SubstitutionCryptosystem, TranspositionCryptosystem as TranspositionCryptosystem, VigenereCryptosystem as VigenereCryptosystem
from sage.crypto.lfsr import lfsr_autocorrelation as lfsr_autocorrelation, lfsr_connection_polynomial as lfsr_connection_polynomial, lfsr_sequence as lfsr_sequence
from sage.crypto.stream import LFSRCryptosystem as LFSRCryptosystem, ShrinkingGeneratorCryptosystem as ShrinkingGeneratorCryptosystem
from sage.data_structures.bitset import Bitset as Bitset, FrozenBitset as FrozenBitset
from sage.databases.conway import ConwayPolynomials as ConwayPolynomials
from sage.databases.cremona import CremonaDatabase as CremonaDatabase
from sage.databases.cunningham_tables import cunningham_prime_factors as cunningham_prime_factors
from sage.databases.db_class_polynomials import HilbertClassPolynomialDatabase as HilbertClassPolynomialDatabase
from sage.databases.db_modular_polynomials import AtkinModularCorrespondenceDatabase as AtkinModularCorrespondenceDatabase, AtkinModularPolynomialDatabase as AtkinModularPolynomialDatabase, ClassicalModularPolynomialDatabase as ClassicalModularPolynomialDatabase, DedekindEtaModularCorrespondenceDatabase as DedekindEtaModularCorrespondenceDatabase, DedekindEtaModularPolynomialDatabase as DedekindEtaModularPolynomialDatabase
from sage.databases.findstat import findmap as findmap, findstat as findstat
from sage.databases.jones import JonesDatabase as JonesDatabase
from sage.databases.odlyzko import zeta_zeros as zeta_zeros
from sage.databases.oeis import oeis as oeis
from sage.databases.sloane import SloaneEncyclopedia as SloaneEncyclopedia
from sage.databases.sql_db import SQLDatabase as SQLDatabase, SQLQuery as SQLQuery
from sage.databases.stein_watkins import SteinWatkinsAllData as SteinWatkinsAllData, SteinWatkinsPrimeData as SteinWatkinsPrimeData
from sage.databases.symbolic_data import SymbolicData as SymbolicData
from sage.doctest.control import run_doctests as run_doctests
from sage.dynamics.arithmetic_dynamics.affine_ds import DynamicalSystem_affine as DynamicalSystem_affine
from sage.dynamics.arithmetic_dynamics.berkovich_ds import DynamicalSystem_Berkovich as DynamicalSystem_Berkovich
from sage.dynamics.arithmetic_dynamics.dynamical_semigroup import DynamicalSemigroup as DynamicalSemigroup, DynamicalSemigroup_affine as DynamicalSemigroup_affine, DynamicalSemigroup_projective as DynamicalSemigroup_projective
from sage.dynamics.arithmetic_dynamics.generic_ds import DynamicalSystem as DynamicalSystem
from sage.dynamics.arithmetic_dynamics.product_projective_ds import DynamicalSystem_product_projective as DynamicalSystem_product_projective
from sage.dynamics.arithmetic_dynamics.projective_ds import DynamicalSystem_projective as DynamicalSystem_projective
from sage.dynamics.arithmetic_dynamics.wehlerK3 import WehlerK3Surface as WehlerK3Surface, random_WehlerK3Surface as random_WehlerK3Surface
from sage.dynamics.cellular_automata.solitons import PeriodicSolitonCellularAutomata as PeriodicSolitonCellularAutomata, SolitonCellularAutomata as SolitonCellularAutomata
from sage.dynamics.complex_dynamics.mandel_julia import external_ray as external_ray, julia_plot as julia_plot, kneading_sequence as kneading_sequence, mandelbrot_plot as mandelbrot_plot
from sage.dynamics.finite_dynamical_system import DiscreteDynamicalSystem as DiscreteDynamicalSystem
from sage.ext.fast_callable import fast_callable as fast_callable
from sage.ext.fast_eval import fast_float as fast_float
from sage.functions.airy import airy_ai as airy_ai, airy_ai_prime as airy_ai_prime, airy_bi as airy_bi, airy_bi_prime as airy_bi_prime
from sage.functions.bessel import Bessel as Bessel, bessel_I as bessel_I, bessel_J as bessel_J, bessel_K as bessel_K, bessel_Y as bessel_Y, hankel1 as hankel1, hankel2 as hankel2, spherical_bessel_J as spherical_bessel_J, spherical_bessel_Y as spherical_bessel_Y, spherical_hankel1 as spherical_hankel1, spherical_hankel2 as spherical_hankel2, struve_H as struve_H, struve_L as struve_L
from sage.functions.error import erf as erf, erfc as erfc, erfi as erfi, erfinv as erfinv, fresnel_cos as fresnel_cos, fresnel_sin as fresnel_sin
from sage.functions.exp_integral import Chi as Chi, Ci as Ci, Ei as Ei, Li as Li, Shi as Shi, Si as Si, cos_integral as cos_integral, cosh_integral as cosh_integral, exp_integral_e as exp_integral_e, exp_integral_e1 as exp_integral_e1, exp_integral_ei as exp_integral_ei, exponential_integral_1 as exponential_integral_1, li as li, log_integral as log_integral, log_integral_offset as log_integral_offset, sin_integral as sin_integral, sinh_integral as sinh_integral
from sage.functions.gamma import beta as beta, gamma as gamma, gamma_inc as gamma_inc, gamma_inc_lower as gamma_inc_lower, log_gamma as log_gamma, psi as psi, Γ as Γ, ψ as ψ
from sage.functions.generalized import dirac_delta as dirac_delta, heaviside as heaviside, kronecker_delta as kronecker_delta, sgn as sgn, sign as sign, unit_step as unit_step
from sage.functions.hyperbolic import acosh as acosh, acoth as acoth, acsch as acsch, arccosh as arccosh, arccoth as arccoth, arccsch as arccsch, arcsech as arcsech, arcsinh as arcsinh, arctanh as arctanh, asech as asech, asinh as asinh, atanh as atanh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sage.functions.hypergeometric import hypergeometric as hypergeometric, hypergeometric_M as hypergeometric_M, hypergeometric_U as hypergeometric_U
from sage.functions.jacobi import inverse_jacobi as inverse_jacobi, inverse_jacobi_cd as inverse_jacobi_cd, inverse_jacobi_cn as inverse_jacobi_cn, inverse_jacobi_cs as inverse_jacobi_cs, inverse_jacobi_dc as inverse_jacobi_dc, inverse_jacobi_dn as inverse_jacobi_dn, inverse_jacobi_ds as inverse_jacobi_ds, inverse_jacobi_nc as inverse_jacobi_nc, inverse_jacobi_nd as inverse_jacobi_nd, inverse_jacobi_ns as inverse_jacobi_ns, inverse_jacobi_sc as inverse_jacobi_sc, inverse_jacobi_sd as inverse_jacobi_sd, inverse_jacobi_sn as inverse_jacobi_sn, jacobi as jacobi, jacobi_am as jacobi_am, jacobi_cd as jacobi_cd, jacobi_cn as jacobi_cn, jacobi_cs as jacobi_cs, jacobi_dc as jacobi_dc, jacobi_dn as jacobi_dn, jacobi_ds as jacobi_ds, jacobi_nc as jacobi_nc, jacobi_nd as jacobi_nd, jacobi_ns as jacobi_ns, jacobi_sc as jacobi_sc, jacobi_sd as jacobi_sd, jacobi_sn as jacobi_sn
from sage.functions.log import dilog as dilog, exp as exp, exp_polar as exp_polar, harmonic_number as harmonic_number, lambert_w as lambert_w, ln as ln, polylog as polylog
from sage.functions.min_max import max_symbolic as max_symbolic, min_symbolic as min_symbolic
from sage.functions.orthogonal_polys import chebyshev_T as chebyshev_T, chebyshev_U as chebyshev_U, gegenbauer as gegenbauer, gen_laguerre as gen_laguerre, gen_legendre_P as gen_legendre_P, gen_legendre_Q as gen_legendre_Q, hahn as hahn, hermite as hermite, jacobi_P as jacobi_P, krawtchouk as krawtchouk, laguerre as laguerre, legendre_P as legendre_P, legendre_Q as legendre_Q, meixner as meixner, ultraspherical as ultraspherical
from sage.functions.other import abs_symbolic as abs_symbolic, arg as arg, binomial as binomial, cases as cases, ceil as ceil, complex_root_of as complex_root_of, conjugate as conjugate, factorial as factorial, floor as floor, frac as frac, imag as imag, imag_part as imag_part, imaginary as imaginary, real as real, real_nth_root as real_nth_root, real_part as real_part
from sage.functions.piecewise import piecewise as piecewise
from sage.functions.prime_pi import legendre_phi as legendre_phi, partial_sieve_function as partial_sieve_function
from sage.functions.special import elliptic_e as elliptic_e, elliptic_ec as elliptic_ec, elliptic_eu as elliptic_eu, elliptic_f as elliptic_f, elliptic_j as elliptic_j, elliptic_kc as elliptic_kc, elliptic_pi as elliptic_pi, spherical_harmonic as spherical_harmonic
from sage.functions.spike_function import spike_function as spike_function
from sage.functions.transcendental import dickman_rho as dickman_rho, hurwitz_zeta as hurwitz_zeta, stieltjes as stieltjes, zeta as zeta, zeta_symmetric as zeta_symmetric, zetaderiv as zetaderiv, ζ as ζ
from sage.functions.trig import acos as acos, acot as acot, acsc as acsc, arccos as arccos, arccot as arccot, arccsc as arccsc, arcsec as arcsec, arcsin as arcsin, arctan as arctan, arctan2 as arctan2, asec as asec, asin as asin, atan as atan, atan2 as atan2, cos as cos, cot as cot, csc as csc, sec as sec, sin as sin, tan as tan
from sage.functions.wigner import clebsch_gordan as clebsch_gordan, gaunt as gaunt, racah as racah, wigner_3j as wigner_3j, wigner_6j as wigner_6j, wigner_9j as wigner_9j
from sage.game_theory.cooperative_game import CooperativeGame as CooperativeGame
from sage.game_theory.matching_game import MatchingGame as MatchingGame
from sage.game_theory.normal_form_game import NormalFormGame as NormalFormGame
from sage.games.hexad import Minimog as Minimog
from sage.games.sudoku import Sudoku as Sudoku, sudoku as sudoku
from sage.geometry.cone import Cone as Cone, random_cone as random_cone
from sage.geometry.fan import FaceFan as FaceFan, Fan as Fan, Fan2d as Fan2d, NormalFan as NormalFan
from sage.geometry.fan_morphism import FanMorphism as FanMorphism
from sage.geometry.hyperbolic_space.hyperbolic_interface import HyperbolicPlane as HyperbolicPlane
from sage.geometry.hyperplane_arrangement.arrangement import HyperplaneArrangements as HyperplaneArrangements
from sage.geometry.hyperplane_arrangement.library import hyperplane_arrangements as hyperplane_arrangements
from sage.geometry.hyperplane_arrangement.ordered_arrangement import OrderedHyperplaneArrangements as OrderedHyperplaneArrangements
from sage.geometry.lattice_polytope import LatticePolytope as LatticePolytope, NefPartition as NefPartition, ReflexivePolytope as ReflexivePolytope, ReflexivePolytopes as ReflexivePolytopes
from sage.geometry.polyhedral_complex import PolyhedralComplex as PolyhedralComplex
from sage.geometry.polyhedron.combinatorial_polyhedron.base import CombinatorialPolyhedron as CombinatorialPolyhedron
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.geometry.polyhedron.library import polytopes as polytopes
from sage.geometry.ribbon_graph import RibbonGraph as RibbonGraph
from sage.geometry.riemannian_manifolds.parametrized_surface3d import ParametrizedSurface3D as ParametrizedSurface3D
from sage.geometry.riemannian_manifolds.surface3d_generators import surfaces as surfaces
from sage.geometry.toric_lattice import ToricLattice as ToricLattice
from sage.geometry.triangulation.point_configuration import PointConfiguration as PointConfiguration
from sage.geometry.voronoi_diagram import VoronoiDiagram as VoronoiDiagram
from sage.graphs.bipartite_graph import BipartiteGraph as BipartiteGraph
from sage.graphs.digraph import DiGraph as DiGraph
from sage.graphs.digraph_generators import digraphs as digraphs
from sage.graphs.graph import Graph as Graph
from sage.graphs.graph_database import GenericGraphQuery as GenericGraphQuery, GraphDatabase as GraphDatabase, GraphQuery as GraphQuery, graph_db_info as graph_db_info
from sage.graphs.graph_editor import graph_editor as graph_editor
from sage.graphs.graph_generators import graphs as graphs
from sage.graphs.hypergraph_generators import hypergraphs as hypergraphs
from sage.graphs.isgci import graph_classes as graph_classes
from sage.graphs.matching_covered_graph import MatchingCoveredGraph as MatchingCoveredGraph
from sage.groups.abelian_gps.abelian_group import AbelianGroup as AbelianGroup, word_problem as word_problem
from sage.groups.abelian_gps.abelian_group_morphism import AbelianGroupMorphism as AbelianGroupMorphism
from sage.groups.abelian_gps.values import AbelianGroupWithValues as AbelianGroupWithValues
from sage.groups.additive_abelian.additive_abelian_group import AdditiveAbelianGroup as AdditiveAbelianGroup
from sage.groups.additive_abelian.additive_abelian_wrapper import AdditiveAbelianGroupWrapper as AdditiveAbelianGroupWrapper, AdditiveAbelianGroupWrapperElement as AdditiveAbelianGroupWrapperElement, UnwrappingMorphism as UnwrappingMorphism, basis_from_generators as basis_from_generators
from sage.groups.affine_gps.affine_group import AffineGroup as AffineGroup
from sage.groups.affine_gps.euclidean_group import EuclideanGroup as EuclideanGroup
from sage.groups.artin import ArtinGroup as ArtinGroup
from sage.groups.braid import BraidGroup as BraidGroup
from sage.groups.class_function import ClassFunction as ClassFunction
from sage.groups.conjugacy_classes import ConjugacyClass as ConjugacyClass, ConjugacyClassGAP as ConjugacyClassGAP
from sage.groups.cubic_braid import AssionGroupS as AssionGroupS, AssionGroupU as AssionGroupU, CubicBraidGroup as CubicBraidGroup
from sage.groups.free_group import FreeGroup as FreeGroup
from sage.groups.generic import discrete_log as discrete_log, discrete_log_lambda as discrete_log_lambda, discrete_log_rho as discrete_log_rho, linear_relation as linear_relation, multiple as multiple, multiples as multiples, order_from_multiple as order_from_multiple
from sage.groups.group_exp import GroupExp as GroupExp, GroupExpElement as GroupExpElement, GroupExp_Class as GroupExp_Class
from sage.groups.group_semidirect_product import GroupSemidirectProduct as GroupSemidirectProduct, GroupSemidirectProductElement as GroupSemidirectProductElement
from sage.groups.matrix_gps.finitely_generated import MatrixGroup as MatrixGroup, QuaternionMatrixGroupGF3 as QuaternionMatrixGroupGF3
from sage.groups.matrix_gps.linear import GL as GL, SL as SL
from sage.groups.matrix_gps.orthogonal import GO as GO, SO as SO
from sage.groups.matrix_gps.symplectic import Sp as Sp
from sage.groups.matrix_gps.unitary import GU as GU, SU as SU
from sage.groups.pari_group import PariGroup as PariGroup
from sage.groups.perm_gps.constructor import PermutationGroupElement as PermutationGroupElement
from sage.groups.perm_gps.cubegroup import CubeGroup as CubeGroup, RubiksCube as RubiksCube
from sage.groups.perm_gps.permgroup import PermutationGroup as PermutationGroup, PermutationGroup_generic as PermutationGroup_generic, PermutationGroup_subgroup as PermutationGroup_subgroup, direct_product_permgroups as direct_product_permgroups
from sage.groups.perm_gps.permgroup_morphism import PermutationGroupMap as PermutationGroupMap, PermutationGroupMorphism as PermutationGroupMorphism, PermutationGroupMorphism_id as PermutationGroupMorphism_id, PermutationGroupMorphism_im_gens as PermutationGroupMorphism_im_gens
from sage.groups.perm_gps.permgroup_named import AlternatingGroup as AlternatingGroup, CyclicPermutationGroup as CyclicPermutationGroup, DiCyclicGroup as DiCyclicGroup, DihedralGroup as DihedralGroup, GeneralDihedralGroup as GeneralDihedralGroup, KleinFourGroup as KleinFourGroup, MathieuGroup as MathieuGroup, PGL as PGL, PGU as PGU, PSL as PSL, PSU as PSU, PSp as PSp, PrimitiveGroup as PrimitiveGroup, PrimitiveGroups as PrimitiveGroups, QuaternionGroup as QuaternionGroup, SemidihedralGroup as SemidihedralGroup, SmallPermutationGroup as SmallPermutationGroup, SplitMetacyclicGroup as SplitMetacyclicGroup, SuzukiGroup as SuzukiGroup, SymmetricGroup as SymmetricGroup, TransitiveGroup as TransitiveGroup, TransitiveGroups as TransitiveGroups
from sage.groups.raag import RightAngledArtinGroup as RightAngledArtinGroup
from sage.groups.semimonomial_transformations.semimonomial_transformation_group import SemimonomialTransformationGroup as SemimonomialTransformationGroup
from sage.homology.chain_complex import ChainComplex as ChainComplex
from sage.homology.chain_complex_morphism import ChainComplexMorphism as ChainComplexMorphism
from sage.homology.koszul_complex import KoszulComplex as KoszulComplex
from sage.interfaces.axiom import Axiom as Axiom, axiom as axiom
from sage.interfaces.ecm import ECM as ECM, ecm as ecm
from sage.interfaces.four_ti_2 import four_ti_2 as four_ti_2
from sage.interfaces.fricas import FriCAS as FriCAS, fricas as fricas
from sage.interfaces.frobby import frobby as frobby
from sage.interfaces.gap import Gap as Gap, gap as gap, gap_reset_workspace as gap_reset_workspace
from sage.interfaces.gap3 import Gap3 as Gap3, gap3 as gap3, gap3_version as gap3_version
from sage.interfaces.genus2reduction import Genus2reduction as Genus2reduction, genus2reduction as genus2reduction
from sage.interfaces.gfan import Gfan as Gfan, gfan as gfan
from sage.interfaces.giac import Giac as Giac, giac as giac
from sage.interfaces.gnuplot import gnuplot as gnuplot
from sage.interfaces.gp import Gp as Gp, gp as gp, gp_version as gp_version
from sage.interfaces.kash import Kash as Kash, kash as kash, kash_version as kash_version
from sage.interfaces.lie import LiE as LiE, lie as lie
from sage.interfaces.lisp import Lisp as Lisp, lisp as lisp
from sage.interfaces.macaulay2 import Macaulay2 as Macaulay2, macaulay2 as macaulay2
from sage.interfaces.magma import Magma as Magma, magma as magma
from sage.interfaces.magma_free import magma_free as magma_free
from sage.interfaces.maple import Maple as Maple, maple as maple
from sage.interfaces.mathematica import Mathematica as Mathematica, mathematica as mathematica
from sage.interfaces.mathics import Mathics as Mathics, mathics as mathics
from sage.interfaces.matlab import Matlab as Matlab, matlab as matlab, matlab_version as matlab_version
from sage.interfaces.maxima import Maxima as Maxima, maxima as maxima
from sage.interfaces.maxima_lib import maxima_calculus as maxima_calculus
from sage.interfaces.mupad import Mupad as Mupad, mupad as mupad
from sage.interfaces.mwrank import Mwrank as Mwrank, mwrank as mwrank
from sage.interfaces.octave import Octave as Octave, octave as octave
from sage.interfaces.polymake import polymake as polymake
from sage.interfaces.povray import povray as povray
from sage.interfaces.psage import PSage as PSage
from sage.interfaces.qepcad import qepcad as qepcad, qepcad_formula as qepcad_formula, qepcad_version as qepcad_version
from sage.interfaces.r import R as R, r as r, r_version as r_version
from sage.interfaces.read_data import read_data as read_data
from sage.interfaces.sage0 import Sage as Sage, sage0 as sage0, sage0_version as sage0_version
from sage.interfaces.scilab import scilab as scilab
from sage.interfaces.singular import Singular as Singular, singular as singular, singular_version as singular_version
from sage.interfaces.tachyon import tachyon_rt as tachyon_rt
from sage.knots.knot import Knot as Knot, Knots as Knots
from sage.knots.knotinfo import KnotInfo as KnotInfo, KnotInfoSeries as KnotInfoSeries
from sage.knots.link import Link as Link
from sage.lfunctions.dokchitser import Dokchitser as Dokchitser
from sage.lfunctions.lcalc import lcalc as lcalc
from sage.lfunctions.sympow import sympow as sympow
from sage.lfunctions.zero_sums import LFunctionZeroSum as LFunctionZeroSum
from sage.libs.eclib.constructor import CremonaModularSymbols as CremonaModularSymbols
from sage.libs.eclib.interface import mwrank_EllipticCurve as mwrank_EllipticCurve, mwrank_MordellWeil as mwrank_MordellWeil
from sage.libs.eclib.mwrank import mwrank_get_precision as mwrank_get_precision, mwrank_initprimes as mwrank_initprimes, mwrank_set_precision as mwrank_set_precision
from sage.libs.flint.qsieve_sage import qsieve as qsieve
from sage.libs.gap.libgap import libgap as libgap
from sage.logic.logic import SymbolicLogic as SymbolicLogic
from sage.manifolds.differentiable.examples.euclidean import EuclideanSpace as EuclideanSpace
from sage.manifolds.manifold import Manifold as Manifold
from sage.matrix.constructor import Matrix as Matrix, matrix as matrix
from sage.matrix.matrix_space import Mat as Mat, MatrixSpace as MatrixSpace
from sage.matrix.special import block_diagonal_matrix as block_diagonal_matrix, block_matrix as block_matrix, column_matrix as column_matrix, companion_matrix as companion_matrix, diagonal_matrix as diagonal_matrix, elementary_matrix as elementary_matrix, identity_matrix as identity_matrix, jordan_block as jordan_block, ones_matrix as ones_matrix, random_matrix as random_matrix, zero_matrix as zero_matrix
from sage.matroids.constructor import Matroid as Matroid
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.banner import banner as banner, version as version
from sage.misc.benchmark import benchmark as benchmark
from sage.misc.cachefunc import CachedFunction as CachedFunction, cached_function as cached_function, cached_in_parent_method as cached_in_parent_method, cached_method as cached_method, disk_cached_function as disk_cached_function
from sage.misc.call import attrcall as attrcall
from sage.misc.classgraph import class_graph as class_graph
from sage.misc.constant_function import ConstantFunction as ConstantFunction
from sage.misc.copying import copying as copying, copyright as copyright, license as license
from sage.misc.cython import cython as cython, cython_lambda as cython_lambda
from sage.misc.decorators import infix_operator as infix_operator, sage_wraps as sage_wraps, specialize as specialize
from sage.misc.defaults import series_precision as series_precision, set_default_variable_name as set_default_variable_name, set_series_precision as set_series_precision
from sage.misc.dev_tools import import_statements as import_statements
from sage.misc.edit_module import edit as edit, set_edit_template as set_edit_template
from sage.misc.explain_pickle import explain_pickle as explain_pickle, unpickle_appends as unpickle_appends, unpickle_build as unpickle_build, unpickle_extension as unpickle_extension, unpickle_instantiate as unpickle_instantiate, unpickle_newobj as unpickle_newobj, unpickle_persistent as unpickle_persistent
from sage.misc.flatten import flatten as flatten
from sage.misc.fpickle import pickle_function as pickle_function, unpickle_function as unpickle_function
from sage.misc.func_persist import func_persist as func_persist
from sage.misc.functional import N as N, additive_order as additive_order, base_field as base_field, base_ring as base_ring, basis as basis, category as category, characteristic_polynomial as characteristic_polynomial, charpoly as charpoly, coerce as coerce, cyclotomic_polynomial as cyclotomic_polynomial, decomposition as decomposition, denominator as denominator, det as det, dim as dim, dimension as dimension, disc as disc, discriminant as discriminant, eta as eta, fcp as fcp, gen as gen, gens as gens, hecke_operator as hecke_operator, image as image, integral as integral, integral_closure as integral_closure, integrate as integrate, interval as interval, is_even as is_even, is_odd as is_odd, isqrt as isqrt, kernel as kernel, krull_dimension as krull_dimension, lift as lift, log as log, log_b as log_b, minimal_polynomial as minimal_polynomial, minpoly as minpoly, multiplicative_order as multiplicative_order, n as n, ngens as ngens, norm as norm, numerator as numerator, numerical_approx as numerical_approx, objgen as objgen, objgens as objgens, order as order, product as product, quo as quo, quotient as quotient, rank as rank, regulator as regulator, round as round, sqrt as sqrt, squarefree_part as squarefree_part, sum as sum, transpose as transpose, xinterval as xinterval
from sage.misc.html import html as html, pretty_print_default as pretty_print_default
from sage.misc.inline_fortran import fortran as fortran
from sage.misc.latex import LatexExpr as LatexExpr, latex as latex, view as view
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute, lazy_class_attribute as lazy_class_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.map_threaded import map_threaded as map_threaded
from sage.misc.mathml import mathml as mathml
from sage.misc.misc import BackslashOperator as BackslashOperator, compose as compose, exists as exists, forall as forall, is_iterator as is_iterator, nest as nest, newton_method_sizes as newton_method_sizes, pad_zeros as pad_zeros, random_sublist as random_sublist
from sage.misc.misc_c import balanced_sum as balanced_sum, mul as mul, prod as prod, running_total as running_total
from sage.misc.mrange import cartesian_product_iterator as cartesian_product_iterator, mrange as mrange, mrange_iter as mrange_iter, xmrange as xmrange, xmrange_iter as xmrange_iter
from sage.misc.namespace_package import install_dict as install_dict, install_doc as install_doc
from sage.misc.package import installed_packages as installed_packages, is_package_installed as is_package_installed, package_versions as package_versions
from sage.misc.pager import pager as pager
from sage.misc.persist import db as db, db_save as db_save, dumps as dumps, load as load, loads as loads, register_unpickle_override as register_unpickle_override, save as save, unpickle_global as unpickle_global
from sage.misc.prandom import betavariate as betavariate, choice as choice, expovariate as expovariate, gammavariate as gammavariate, gauss as gauss, getrandbits as getrandbits, lognormvariate as lognormvariate, normalvariate as normalvariate, paretovariate as paretovariate, randint as randint, random as random, randrange as randrange, sample as sample, shuffle as shuffle, uniform as uniform, vonmisesvariate as vonmisesvariate, weibullvariate as weibullvariate
from sage.misc.profiler import Profiler as Profiler
from sage.misc.randstate import current_randstate as current_randstate, initial_seed as initial_seed, seed as seed, set_random_seed as set_random_seed
from sage.misc.remote_file import get_remote_file as get_remote_file
from sage.misc.repr import repr_lincomb as repr_lincomb
from sage.misc.reset import reset as reset, restore as restore
from sage.misc.sage_eval import sage_eval as sage_eval, sageobj as sageobj
from sage.misc.sage_input import sage_input as sage_input
from sage.misc.sage_timeit_class import timeit as timeit
from sage.misc.sage_unittest import TestSuite as TestSuite
from sage.misc.sagedoc import browse_sage_doc as browse_sage_doc, constructions as constructions, developer as developer, help as help, manual as manual, reference as reference, search_def as search_def, search_doc as search_doc, search_src as search_src, tutorial as tutorial
from sage.misc.session import load_session as load_session, save_session as save_session, show_identifiers as show_identifiers
from sage.misc.sh import sh as sh
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.misc.table import table as table
from sage.misc.temporary_file import tmp_dir as tmp_dir, tmp_filename as tmp_filename
from sage.misc.timing import cputime as cputime, walltime as walltime
from sage.misc.trace import trace as trace
from sage.misc.unknown import Unknown as Unknown, UnknownError as UnknownError
from sage.misc.verbose import get_verbose as get_verbose, get_verbose_files as get_verbose_files, set_verbose as set_verbose, set_verbose_files as set_verbose_files, unset_verbose_files as unset_verbose_files, verbose as verbose
from sage.modular.abvar.constructor import AbelianVariety as AbelianVariety, J0 as J0, J1 as J1, JH as JH
from sage.modular.arithgroup.arithgroup_perm import ArithmeticSubgroup_Permutation as ArithmeticSubgroup_Permutation
from sage.modular.arithgroup.congroup_gamma import Gamma as Gamma
from sage.modular.arithgroup.congroup_gamma0 import Gamma0 as Gamma0
from sage.modular.arithgroup.congroup_gamma1 import Gamma1 as Gamma1
from sage.modular.arithgroup.congroup_gammaH import GammaH as GammaH
from sage.modular.arithgroup.congroup_generic import CongruenceSubgroup as CongruenceSubgroup
from sage.modular.arithgroup.congroup_sl2z import SL2Z as SL2Z
from sage.modular.arithgroup.farey_symbol import FareySymbol as FareySymbol
from sage.modular.btquotients.btquotient import BruhatTitsQuotient as BruhatTitsQuotient
from sage.modular.cusps import Cusp as Cusp, Cusps as Cusps
from sage.modular.cusps_nf import Gamma0_NFCusps as Gamma0_NFCusps, NFCusp as NFCusp, NFCusps as NFCusps
from sage.modular.dirichlet import DirichletGroup as DirichletGroup, kronecker_character as kronecker_character, kronecker_character_upside_down as kronecker_character_upside_down, trivial_character as trivial_character
from sage.modular.drinfeld_modform.ring import DrinfeldModularForms as DrinfeldModularForms
from sage.modular.etaproducts import AllCusps as AllCusps, CuspFamily as CuspFamily, EtaGroup as EtaGroup, EtaGroupElement as EtaGroupElement, EtaProduct as EtaProduct
from sage.modular.local_comp.local_comp import LocalComponent as LocalComponent
from sage.modular.modform.constructor import CuspForms as CuspForms, EisensteinForms as EisensteinForms, ModularForms as ModularForms, Newform as Newform, Newforms as Newforms
from sage.modular.modform.eis_series import eisenstein_series_lseries as eisenstein_series_lseries, eisenstein_series_qexp as eisenstein_series_qexp
from sage.modular.modform.element import delta_lseries as delta_lseries
from sage.modular.modform.half_integral import half_integral_weight_modform_basis as half_integral_weight_modform_basis
from sage.modular.modform.hecke_operator_on_qexp import hecke_operator_on_basis as hecke_operator_on_basis, hecke_operator_on_qexp as hecke_operator_on_qexp
from sage.modular.modform.j_invariant import j_invariant_qexp as j_invariant_qexp
from sage.modular.modform.numerical import numerical_eigenforms as numerical_eigenforms
from sage.modular.modform.ring import ModularFormsRing as ModularFormsRing
from sage.modular.modform.theta import theta2_qexp as theta2_qexp, theta_qexp as theta_qexp
from sage.modular.modform.vm_basis import delta_qexp as delta_qexp, victor_miller_basis as victor_miller_basis
from sage.modular.modsym.element import set_modsym_print_mode as set_modsym_print_mode
from sage.modular.modsym.g1list import G1list as G1list
from sage.modular.modsym.ghlist import GHlist as GHlist
from sage.modular.modsym.heilbronn import HeilbronnCremona as HeilbronnCremona, HeilbronnMerel as HeilbronnMerel
from sage.modular.modsym.modsym import ModularSymbols as ModularSymbols, ModularSymbols_clear_cache as ModularSymbols_clear_cache
from sage.modular.modsym.p1list import P1List as P1List, lift_to_sl2z as lift_to_sl2z
from sage.modular.modsym.p1list_nf import MSymbol as MSymbol, P1NFList as P1NFList
from sage.modular.multiple_zeta import Multizeta as Multizeta, Multizetas as Multizetas
from sage.modular.overconvergent.genus0 import OverconvergentModularForms as OverconvergentModularForms
from sage.modular.overconvergent.hecke_series import hecke_series as hecke_series
from sage.modular.overconvergent.weightspace import pAdicWeightSpace as pAdicWeightSpace
from sage.modular.pollack_stevens.distributions import OverconvergentDistributions as OverconvergentDistributions, Symk as Symk
from sage.modular.pollack_stevens.space import PollackStevensModularSymbols as PollackStevensModularSymbols
from sage.modular.quasimodform.ring import QuasiModularForms as QuasiModularForms
from sage.modular.quatalg.brandt import BrandtModule as BrandtModule
from sage.modular.ssmod.ssmod import SupersingularModule as SupersingularModule, dimension_supersingular_module as dimension_supersingular_module, supersingular_D as supersingular_D, supersingular_j as supersingular_j
from sage.modules.filtered_vector_space import FilteredVectorSpace as FilteredVectorSpace
from sage.modules.free_module import FreeModule as FreeModule, VectorSpace as VectorSpace, span as span
from sage.modules.free_module_element import free_module_element as free_module_element, random_vector as random_vector, vector as vector, zero_vector as zero_vector
from sage.modules.free_quadratic_module import FreeQuadraticModule as FreeQuadraticModule, InnerProductSpace as InnerProductSpace, QuadraticSpace as QuadraticSpace
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice as IntegralLattice
from sage.modules.multi_filtered_vector_space import MultiFilteredVectorSpace as MultiFilteredVectorSpace
from sage.modules.torsion_quadratic_module import TorsionQuadraticForm as TorsionQuadraticForm
from sage.modules.vector_space_morphism import linear_transformation as linear_transformation
from sage.monoids.free_abelian_monoid import FreeAbelianMonoid as FreeAbelianMonoid
from sage.monoids.free_monoid import FreeMonoid as FreeMonoid
from sage.monoids.string_monoid import AlphabeticStrings as AlphabeticStrings, BinaryStrings as BinaryStrings, HexadecimalStrings as HexadecimalStrings, OctalStrings as OctalStrings, Radix64Strings as Radix64Strings
from sage.monoids.string_ops import coincidence_discriminant as coincidence_discriminant, coincidence_index as coincidence_index, frequency_distribution as frequency_distribution, strip_encoding as strip_encoding
from sage.numerical.backends.generic_backend import default_mip_solver as default_mip_solver
from sage.numerical.backends.generic_sdp_backend import default_sdp_solver as default_sdp_solver
from sage.numerical.interactive_simplex_method import InteractiveLPProblem as InteractiveLPProblem, InteractiveLPProblemStandardForm as InteractiveLPProblemStandardForm
from sage.numerical.mip import MixedIntegerLinearProgram as MixedIntegerLinearProgram
from sage.numerical.optimize import find_fit as find_fit, find_local_maximum as find_local_maximum, find_local_minimum as find_local_minimum, find_root as find_root, minimize as minimize, minimize_constrained as minimize_constrained
from sage.numerical.sdp import SemidefiniteProgram as SemidefiniteProgram
from sage.parallel.decorate import fork as fork, parallel as parallel
from sage.parallel.parallelism import Parallelism as Parallelism
from sage.plot.animate import animate as animate
from sage.plot.arc import arc as arc
from sage.plot.arrow import arrow as arrow, arrow2d as arrow2d
from sage.plot.bar_chart import bar_chart as bar_chart
from sage.plot.bezier_path import bezier_path as bezier_path
from sage.plot.circle import circle as circle
from sage.plot.colors import Color as Color, colormaps as colormaps, colors as colors, hue as hue, rainbow as rainbow
from sage.plot.complex_plot import complex_plot as complex_plot
from sage.plot.contour_plot import contour_plot as contour_plot, implicit_plot as implicit_plot, region_plot as region_plot
from sage.plot.density_plot import density_plot as density_plot
from sage.plot.disk import disk as disk
from sage.plot.ellipse import ellipse as ellipse
from sage.plot.graphics import Graphics as Graphics
from sage.plot.histogram import histogram as histogram
from sage.plot.hyperbolic_arc import hyperbolic_arc as hyperbolic_arc
from sage.plot.hyperbolic_polygon import hyperbolic_polygon as hyperbolic_polygon, hyperbolic_triangle as hyperbolic_triangle
from sage.plot.hyperbolic_regular_polygon import hyperbolic_regular_polygon as hyperbolic_regular_polygon
from sage.plot.line import line as line, line2d as line2d
from sage.plot.matrix_plot import matrix_plot as matrix_plot
from sage.plot.plot import graphics_array as graphics_array, list_plot as list_plot, list_plot_loglog as list_plot_loglog, list_plot_semilogx as list_plot_semilogx, list_plot_semilogy as list_plot_semilogy, multi_graphics as multi_graphics, parametric_plot as parametric_plot, plot as plot, plot_loglog as plot_loglog, plot_semilogx as plot_semilogx, plot_semilogy as plot_semilogy, polar_plot as polar_plot
from sage.plot.plot3d.implicit_plot3d import implicit_plot3d as implicit_plot3d
from sage.plot.plot3d.list_plot3d import list_plot3d as list_plot3d
from sage.plot.plot3d.parametric_plot3d import parametric_plot3d as parametric_plot3d
from sage.plot.plot3d.platonic import cube as cube, dodecahedron as dodecahedron, icosahedron as icosahedron, octahedron as octahedron, tetrahedron as tetrahedron
from sage.plot.plot3d.plot3d import Cylindrical as Cylindrical, Spherical as Spherical, SphericalElevation as SphericalElevation, cylindrical_plot3d as cylindrical_plot3d, plot3d as plot3d, spherical_plot3d as spherical_plot3d
from sage.plot.plot3d.plot_field3d import plot_vector_field3d as plot_vector_field3d
from sage.plot.plot3d.revolution_plot3d import revolution_plot3d as revolution_plot3d
from sage.plot.plot3d.shapes import arrow3d as arrow3d
from sage.plot.plot3d.shapes2 import bezier3d as bezier3d, line3d as line3d, point3d as point3d, polygon3d as polygon3d, polygons3d as polygons3d, sphere as sphere, text3d as text3d
from sage.plot.plot3d.tachyon import Tachyon as Tachyon
from sage.plot.plot_field import plot_slope_field as plot_slope_field, plot_vector_field as plot_vector_field
from sage.plot.point import point as point, point2d as point2d, points as points
from sage.plot.polygon import polygon as polygon, polygon2d as polygon2d
from sage.plot.scatter_plot import scatter_plot as scatter_plot
from sage.plot.step import plot_step_function as plot_step_function
from sage.plot.streamline_plot import streamline_plot as streamline_plot
from sage.plot.text import text as text
from sage.probability.probability_distribution import GeneralDiscreteDistribution as GeneralDiscreteDistribution, RealDistribution as RealDistribution, SphericalDistribution as SphericalDistribution
from sage.probability.random_variable import DiscreteProbabilitySpace as DiscreteProbabilitySpace, DiscreteRandomVariable as DiscreteRandomVariable
from sage.quadratic_forms.binary_qf import BinaryQF as BinaryQF, BinaryQF_reduced_representatives as BinaryQF_reduced_representatives
from sage.quadratic_forms.bqf_class_group import BQFClassGroup as BQFClassGroup
from sage.quadratic_forms.constructions import BezoutianQuadraticForm as BezoutianQuadraticForm, HyperbolicPlane_quadratic_form as HyperbolicPlane_quadratic_form
from sage.quadratic_forms.extras import extend_to_primitive as extend_to_primitive, is_triangular_number as is_triangular_number, least_quadratic_nonresidue as least_quadratic_nonresidue
from sage.quadratic_forms.genera.genus import Genus as Genus
from sage.quadratic_forms.quadratic_form import DiagonalQuadraticForm as DiagonalQuadraticForm, QuadraticForm as QuadraticForm, quadratic_form_from_invariants as quadratic_form_from_invariants
from sage.quadratic_forms.random_quadraticform import random_quadraticform as random_quadraticform, random_quadraticform_with_conditions as random_quadraticform_with_conditions, random_ternaryqf as random_ternaryqf, random_ternaryqf_with_conditions as random_ternaryqf_with_conditions
from sage.quadratic_forms.special_values import QuadraticBernoulliNumber as QuadraticBernoulliNumber, gamma__exact as gamma__exact, quadratic_L_function__exact as quadratic_L_function__exact, quadratic_L_function__numerical as quadratic_L_function__numerical, zeta__exact as zeta__exact
from sage.quadratic_forms.ternary_qf import TernaryQF as TernaryQF, find_a_ternary_qf_by_level_disc as find_a_ternary_qf_by_level_disc, find_all_ternary_qf_by_level_disc as find_all_ternary_qf_by_level_disc
from sage.repl.attach import attach as attach, attached_files as attached_files, detach as detach, load_attach_mode as load_attach_mode, load_attach_path as load_attach_path, reset_load_attach_path as reset_load_attach_path
from sage.repl.interpreter import logstr as logstr, preparser as preparser
from sage.repl.preparse import implicit_multiplication as implicit_multiplication, preparse as preparse
from sage.repl.rich_output.display_manager import get_display_manager as get_display_manager
from sage.repl.rich_output.pretty_print import pretty_print as pretty_print, show as show
from sage.rings.asymptotic.asymptotic_expansion_generators import asymptotic_expansions as asymptotic_expansions
from sage.rings.asymptotic.asymptotic_ring import AsymptoticRing as AsymptoticRing
from sage.rings.bernoulli_mod_p import bernoulli_mod_p as bernoulli_mod_p, bernoulli_mod_p_single as bernoulli_mod_p_single
from sage.rings.big_oh import O as O
from sage.rings.cfinite_sequence import CFiniteSequence as CFiniteSequence, CFiniteSequences as CFiniteSequences
from sage.rings.complex_arb import CBF as CBF, ComplexBallField as ComplexBallField
from sage.rings.complex_double import ComplexDoubleElement as ComplexDoubleElement, ComplexDoubleField as ComplexDoubleField
from sage.rings.complex_interval import ComplexIntervalFieldElement as ComplexIntervalFieldElement
from sage.rings.complex_interval_field import CIF as CIF, ComplexIntervalField as ComplexIntervalField
from sage.rings.complex_mpc import MPComplexField as MPComplexField
from sage.rings.complex_mpfr import CC as CC, ComplexField as ComplexField, ComplexNumber as ComplexNumber, Complexes as Complexes
from sage.rings.continued_fraction import continued_fraction as continued_fraction, continued_fraction_list as continued_fraction_list
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.finite_rings.conway_polynomials import conway_polynomial as conway_polynomial, exists_conway_polynomial as exists_conway_polynomial
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField, GF as GF
from sage.rings.finite_rings.integer_mod import IntegerMod as IntegerMod, Mod as Mod, mod as mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing, Integers as Integers, Zmod as Zmod
from sage.rings.finite_rings.residue_field import ResidueField as ResidueField
from sage.rings.fraction_field import Frac as Frac, FractionField as FractionField
from sage.rings.function_field.constructor import FunctionField as FunctionField
from sage.rings.function_field.drinfeld_modules.drinfeld_module import DrinfeldModule as DrinfeldModule
from sage.rings.ideal import Ideal as Ideal, ideal as ideal
from sage.rings.infinity import Infinity as Infinity, InfinityRing as InfinityRing, UnsignedInfinityRing as UnsignedInfinityRing, infinity as infinity, oo as oo, unsigned_infinity as unsigned_infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing, crt_basis as crt_basis
from sage.rings.invariants.invariant_theory import invariant_theory as invariant_theory
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.lazy_series_ring import LazyDirichletSeriesRing as LazyDirichletSeriesRing, LazyLaurentSeriesRing as LazyLaurentSeriesRing, LazyPowerSeriesRing as LazyPowerSeriesRing, LazySymmetricFunctions as LazySymmetricFunctions
from sage.rings.lazy_species import LazyCombinatorialSpecies as LazyCombinatorialSpecies
from sage.rings.localization import Localization as Localization
from sage.rings.monomials import monomials as monomials
from sage.rings.number_field.number_field import CyclotomicField as CyclotomicField, NumberField as NumberField, NumberFieldTower as NumberFieldTower, QuadraticField as QuadraticField, is_fundamental_discriminant as is_fundamental_discriminant, is_real_place as is_real_place
from sage.rings.number_field.number_field_element import NumberFieldElement as NumberFieldElement
from sage.rings.number_field.order import EisensteinIntegers as EisensteinIntegers, EquationOrder as EquationOrder, GaussianIntegers as GaussianIntegers
from sage.rings.number_field.totallyreal import enumerate_totallyreal_fields_prim as enumerate_totallyreal_fields_prim
from sage.rings.number_field.totallyreal_data import hermite_constant as hermite_constant
from sage.rings.number_field.totallyreal_rel import enumerate_totallyreal_fields_all as enumerate_totallyreal_fields_all, enumerate_totallyreal_fields_rel as enumerate_totallyreal_fields_rel
from sage.rings.number_field.unit_group import UnitGroup as UnitGroup
from sage.rings.padics.factory import Qp as Qp, QpCR as QpCR, QpER as QpER, QpFP as QpFP, QpLC as QpLC, QpLF as QpLF, Qq as Qq, QqCR as QqCR, QqFP as QqFP, Zp as Zp, ZpCA as ZpCA, ZpCR as ZpCR, ZpER as ZpER, ZpFM as ZpFM, ZpFP as ZpFP, ZpLC as ZpLC, ZpLF as ZpLF, Zq as Zq, ZqCA as ZqCA, ZqCR as ZqCR, ZqFM as ZqFM, ZqFP as ZqFP, pAdicExtension as pAdicExtension, pAdicField as pAdicField, pAdicRing as pAdicRing
from sage.rings.padics.padic_generic import local_print_mode as local_print_mode
from sage.rings.padics.padic_printing import padic_printing as padic_printing
from sage.rings.padics.pow_computer import PowComputer as PowComputer
from sage.rings.padics.pow_computer_ext import PowComputer_ext_maker as PowComputer_ext_maker
from sage.rings.padics.witt_vector_ring import WittVectorRing as WittVectorRing
from sage.rings.pari_ring import Pari as Pari, PariRing as PariRing
from sage.rings.polynomial.convolution import convolution as convolution
from sage.rings.polynomial.cyclotomic import cyclotomic_value as cyclotomic_value
from sage.rings.polynomial.infinite_polynomial_ring import InfinitePolynomialRing as InfinitePolynomialRing
from sage.rings.polynomial.integer_valued_polynomials import IntegerValuedPolynomialRing as IntegerValuedPolynomialRing
from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing as LaurentPolynomialRing
from sage.rings.polynomial.multi_polynomial_element import degree_lowest_rational_function as degree_lowest_rational_function
from sage.rings.polynomial.omega import MacMahonOmega as MacMahonOmega
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing as OrePolynomialRing, SkewPolynomialRing as SkewPolynomialRing
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_quotient_ring import PolynomialQuotientRing as PolynomialQuotientRing
from sage.rings.polynomial.polynomial_quotient_ring_element import PolynomialQuotientRingElement as PolynomialQuotientRingElement
from sage.rings.polynomial.polynomial_ring import polygen as polygen, polygens as polygens
from sage.rings.polynomial.polynomial_ring_constructor import BooleanPolynomialRing as BooleanPolynomialRing, PolynomialRing as PolynomialRing
from sage.rings.polynomial.q_integer_valued_polynomials import QuantumValuedPolynomialRing as QuantumValuedPolynomialRing
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.puiseux_series_ring import PuiseuxSeriesRing as PuiseuxSeriesRing
from sage.rings.qqbar import AA as AA, AlgebraicField as AlgebraicField, AlgebraicNumber as AlgebraicNumber, AlgebraicReal as AlgebraicReal, AlgebraicRealField as AlgebraicRealField, QQbar as QQbar, number_field_elements_from_algebraics as number_field_elements_from_algebraics
from sage.rings.quotient_ring import QuotientRing as QuotientRing
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import QQ as QQ, RationalField as RationalField, Rationals as Rationals
from sage.rings.real_arb import RBF as RBF, RealBallField as RealBallField
from sage.rings.real_double import RealDoubleElement as RealDoubleElement, RealDoubleField as RealDoubleField
from sage.rings.real_lazy import CLF as CLF, ComplexLazyField as ComplexLazyField, RLF as RLF, RealLazyField as RealLazyField
from sage.rings.real_mpfi import RealInterval as RealInterval, RealIntervalField as RealIntervalField
from sage.rings.real_mpfr import RealField as RealField, RealNumber as RealNumber, Reals as Reals
from sage.rings.ring import Algebra as Algebra, CommutativeRing as CommutativeRing, DedekindDomain as DedekindDomain, Field as Field, IntegralDomain as IntegralDomain, PrincipalIdealDomain as PrincipalIdealDomain, Ring as Ring
from sage.rings.semirings.non_negative_integer_semiring import NN as NN, NonNegativeIntegerSemiring as NonNegativeIntegerSemiring
from sage.rings.semirings.tropical_semiring import TropicalSemiring as TropicalSemiring
from sage.rings.tate_algebra import TateAlgebra as TateAlgebra
from sage.rings.universal_cyclotomic_field import E as E, UniversalCyclotomicField as UniversalCyclotomicField
from sage.rings.valuation.gauss_valuation import GaussValuation as GaussValuation
from sage.rings.valuation.value_group import DiscreteValueGroup as DiscreteValueGroup
from sage.sandpiles.examples import sandpiles as sandpiles
from sage.sandpiles.sandpile import Sandpile as Sandpile, SandpileConfig as SandpileConfig, SandpileDivisor as SandpileDivisor, firing_graph as firing_graph, parallel_firing_graph as parallel_firing_graph, triangle_sandpile as triangle_sandpile, wilmes_algorithm as wilmes_algorithm
from sage.sat.solvers.satsolver import SAT as SAT
from sage.schemes.affine.affine_rational_point import enum_affine_finite_field as enum_affine_finite_field, enum_affine_rational_field as enum_affine_rational_field
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace
from sage.schemes.berkovich.berkovich_space import Berkovich_Cp_Affine as Berkovich_Cp_Affine, Berkovich_Cp_Projective as Berkovich_Cp_Projective
from sage.schemes.curves.constructor import Curve as Curve
from sage.schemes.curves.plane_curve_arrangement import AffinePlaneCurveArrangements as AffinePlaneCurveArrangements, PlaneCurveArrangements as PlaneCurveArrangements, ProjectivePlaneCurveArrangements as ProjectivePlaneCurveArrangements
from sage.schemes.curves.projective_curve import Hasse_bounds as Hasse_bounds
from sage.schemes.cyclic_covers.constructor import CyclicCover as CyclicCover
from sage.schemes.elliptic_curves.cm import cm_j_invariants as cm_j_invariants, cm_j_invariants_and_orders as cm_j_invariants_and_orders, cm_orders as cm_orders, hilbert_class_polynomial as hilbert_class_polynomial
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve, EllipticCurve_from_c4c6 as EllipticCurve_from_c4c6, EllipticCurve_from_cubic as EllipticCurve_from_cubic, EllipticCurve_from_j as EllipticCurve_from_j, EllipticCurves_with_good_reduction_outside_S as EllipticCurves_with_good_reduction_outside_S
from sage.schemes.elliptic_curves.ec_database import elliptic_curves as elliptic_curves
from sage.schemes.elliptic_curves.ell_curve_isogeny import EllipticCurveIsogeny as EllipticCurveIsogeny, isogeny_codomain_from_kernel as isogeny_codomain_from_kernel
from sage.schemes.elliptic_curves.ell_finite_field import EllipticCurve_with_prime_order as EllipticCurve_with_prime_order, special_supersingular_curve as special_supersingular_curve
from sage.schemes.elliptic_curves.ell_rational_field import cremona_curves as cremona_curves, cremona_optimal_curves as cremona_optimal_curves
from sage.schemes.elliptic_curves.heegner import heegner_point as heegner_point, heegner_points as heegner_points
from sage.schemes.elliptic_curves.jacobian import Jacobian as Jacobian
from sage.schemes.elliptic_curves.kodaira_symbol import KodairaSymbol as KodairaSymbol
from sage.schemes.elliptic_curves.mod_poly import classical_modular_polynomial as classical_modular_polynomial
from sage.schemes.generic.hypersurface import AffineHypersurface as AffineHypersurface, ProjectiveHypersurface as ProjectiveHypersurface
from sage.schemes.generic.spec import Spec as Spec
from sage.schemes.hyperelliptic_curves.constructor import HyperellipticCurve as HyperellipticCurve
from sage.schemes.hyperelliptic_curves.kummer_surface import KummerSurface as KummerSurface
from sage.schemes.hyperelliptic_curves.mestre import HyperellipticCurve_from_invariants as HyperellipticCurve_from_invariants, Mestre_conic as Mestre_conic
from sage.schemes.plane_conics.constructor import Conic as Conic
from sage.schemes.plane_quartics.quartic_constructor import QuarticCurve as QuarticCurve
from sage.schemes.product_projective.space import ProductProjectiveSpaces as ProductProjectiveSpaces, is_ProductProjectiveSpaces as is_ProductProjectiveSpaces
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, is_ProjectiveSpace as is_ProjectiveSpace
from sage.schemes.toric.fano_variety import CPRFanoToricVariety as CPRFanoToricVariety
from sage.schemes.toric.ideal import ToricIdeal as ToricIdeal
from sage.schemes.toric.library import toric_varieties as toric_varieties
from sage.schemes.toric.variety import AffineToricVariety as AffineToricVariety, ToricVariety as ToricVariety
from sage.schemes.toric.weierstrass import WeierstrassForm as WeierstrassForm
from sage.sets.condition_set import ConditionSet as ConditionSet
from sage.sets.disjoint_set import DisjointSet as DisjointSet
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.sets.finite_set_maps import FiniteSetMaps as FiniteSetMaps
from sage.sets.integer_range import IntegerRange as IntegerRange
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.sets.positive_integers import PositiveIntegers as PositiveIntegers
from sage.sets.primes import Primes as Primes
from sage.sets.real_set import RealSet as RealSet
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as RecursivelyEnumeratedSet
from sage.sets.set import Set as Set
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet as TotallyOrderedFiniteSet
from sage.stats.basic_stats import mean as mean, median as median, mode as mode, moving_average as moving_average, std as std, variance as variance
from sage.stats.intlist import IntList as IntList
from sage.stats.r import ttest as ttest
from sage.stats.time_series import TimeSeries as TimeSeries, autoregressive_fit as autoregressive_fit
from sage.structure.element import CommutativeAlgebraElement as CommutativeAlgebraElement, CommutativeRingElement as CommutativeRingElement, DedekindDomainElement as DedekindDomainElement, EuclideanDomainElement as EuclideanDomainElement, FieldElement as FieldElement, IntegralDomainElement as IntegralDomainElement, PrincipalIdealDomainElement as PrincipalIdealDomainElement, RingElement as RingElement, canonical_coercion as canonical_coercion, coercion_traceback as coercion_traceback, get_coercion_model as get_coercion_model, parent as parent
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.factorization import Factorization as Factorization
from sage.structure.formal_sum import FormalSum as FormalSum, FormalSums as FormalSums
from sage.structure.mutability import Mutability as Mutability
from sage.structure.parent import Parent as Parent
from sage.structure.parent_gens import localvars as localvars
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.sequence import Sequence as Sequence, seq as seq
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from sage.symbolic.assumptions import assume as assume, assuming as assuming, assumptions as assumptions, forget as forget
from sage.symbolic.callable import CallableSymbolicExpressionRing as CallableSymbolicExpressionRing
from sage.symbolic.expression import Expression as Expression, solve_diophantine as solve_diophantine
from sage.symbolic.operators import D as D
from sage.symbolic.relation import solve as solve, solve_ineq as solve_ineq, solve_mod as solve_mod
from sage.symbolic.units import units as units
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule as FiniteRankFreeModule
from sage.topology.cubical_complex import CubicalComplex as CubicalComplex, cubical_complexes as cubical_complexes
from sage.topology.delta_complex import DeltaComplex as DeltaComplex, delta_complexes as delta_complexes
from sage.topology.filtered_simplicial_complex import FilteredSimplicialComplex as FilteredSimplicialComplex
from sage.topology.moment_angle_complex import MomentAngleComplex as MomentAngleComplex
from sage.topology.simplicial_complex import Simplex as Simplex, SimplicialComplex as SimplicialComplex
from sage.topology.simplicial_complex_morphism import SimplicialComplexMorphism as SimplicialComplexMorphism
from sage.typeset.ascii_art import ascii_art as ascii_art
from sage.typeset.unicode_art import unicode_art as unicode_art

deprecationWarning: tuple
coercion_model: sage.structure.coerce.CoercionModel
true: bool
false: bool
SAGE_ROOT: None
SAGE_SRC: str
SAGE_DOC_SRC: str
SAGE_LOCAL: str
DOT_SAGE: str
SAGE_ENV: dict
pari: cypari2.pari_instance.Pari
valuations: sage.misc.lazy_import.LazyImport
hold: sage.symbolic.expression.hold_class
lie_algebras: sage.misc.lazy_import.LazyImport
lie_conformal_algebras: sage.misc.lazy_import.LazyImport
graph_coloring: sage.misc.lazy_import.LazyImport
groups: sage.misc.lazy_import.LazyImport
interfaces: list
reciprocal_trig_functions: dict
prime_pi: sage.functions.prime_pi.PrimePi
codes: sage.misc.lazy_import.LazyImport
channels: sage.misc.lazy_import.LazyImport
crystals: sage.misc.lazy_import.LazyImport
species: sage.misc.lazy_import.LazyImport
path_tableaux: sage.misc.lazy_import.LazyImport
cones: sage.misc.lazy_import.LazyImport
lattice_polytope: sage.misc.lazy_import.LazyImport
toric_plotter: sage.misc.lazy_import.LazyImport
finite_dynamical_systems: sage.misc.lazy_import.LazyImport
simplicial_complexes: sage.misc.lazy_import.LazyImport
simplicial_sets: sage.misc.lazy_import.LazyImport
matroids: sage.misc.lazy_import.LazyImport
game_theory: sage.misc.lazy_import.LazyImport
manifolds: sage.misc.lazy_import.LazyImport
interacts: sage.misc.lazy_import.LazyImport
def sage_globals():
    """
    Return the Sage namespace.

    EXAMPLES::

        sage: 'log' in sage_globals()
        True
        sage: 'MatrixSpace' in sage_globals()
        True
        sage: 'Permutations' in sage_globals()
        True
        sage: 'TheWholeUniverse' in sage_globals()
        False
    """
