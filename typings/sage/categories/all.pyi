r"""
Sage categories quickref

- ``sage.categories.primer?``                      a primer on Elements, Parents, and Categories
- ``sage.categories.tutorial?``                    a tutorial on Elements, Parents, and Categories
- ``Category?``                                    technical background on categories
- ``Sets()``, ``Semigroups()``, ``Algebras(QQ)``   some categories
- ``SemiGroups().example()??``                     sample implementation of a semigroup
- ``Hom(A, B)``, ``End(A, Algebras())``            homomorphisms sets
- ``tensor``, ``cartesian_product``                functorial constructions

Module layout:

- :mod:`sage.categories.basic`                the basic categories
- :mod:`sage.categories.all`                  all categories
- :mod:`sage.categories.semigroups`           the ``Semigroups()`` category
- :mod:`sage.categories.examples.semigroups`  the example of ``Semigroups()``
- :mod:`sage.categories.homset`               morphisms, ...
- :mod:`sage.categories.map`
- :mod:`sage.categories.morphism`
- :mod:`sage.categories.functors`
- :mod:`sage.categories.cartesian_product`    functorial constructions
- :mod:`sage.categories.tensor`
- :mod:`sage.categories.dual`
"""


from sage.categories import primer as primer

from sage.categories.objects import Objects as Objects
from sage.categories.sets_cat import (
    Sets as Sets, 
    EmptySetError as EmptySetError
)
from sage.categories.category import Category as Category
from sage.categories.category_types import Elements as Elements
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.functor import (ForgetfulFunctor as ForgetfulFunctor,
                                     IdentityFunctor as IdentityFunctor)
from sage.categories.homset import (
    Hom as Hom, hom as hom,
    End as End, end as end,
    Homset as Homset, HomsetWithBase as HomsetWithBase
)
from sage.categories.morphism import Morphism as Morphism
from sage.categories.realizations import Realizations as Realizations
from sage.categories.sets_with_partial_maps import SetsWithPartialMaps as SetsWithPartialMaps

from sage.categories.basic import *

from sage.categories.affine_weyl_groups import AffineWeylGroups as AffineWeylGroups
from sage.categories.algebra_ideals import AlgebraIdeals as AlgebraIdeals
from sage.categories.algebra_modules import AlgebraModules as AlgebraModules
from sage.categories.algebras import Algebras as Algebras
from sage.categories.algebras_with_basis import AlgebrasWithBasis as AlgebrasWithBasis
from sage.categories.bialgebras import Bialgebras as Bialgebras
from sage.categories.bialgebras_with_basis import BialgebrasWithBasis as BialgebrasWithBasis
from sage.categories.bimodules import Bimodules as Bimodules
from sage.categories.chain_complexes import ChainComplexes as ChainComplexes, HomologyFunctor as HomologyFunctor
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.coalgebras import Coalgebras as Coalgebras
from sage.categories.coalgebras_with_basis import CoalgebrasWithBasis as CoalgebrasWithBasis
from sage.categories.commutative_algebra_ideals import CommutativeAlgebraIdeals as CommutativeAlgebraIdeals
from sage.categories.commutative_algebras import CommutativeAlgebras as CommutativeAlgebras
from sage.categories.commutative_ring_ideals import CommutativeRingIdeals as CommutativeRingIdeals
from sage.categories.coxeter_groups import CoxeterGroups as CoxeterGroups
from sage.categories.crystals import Crystals as Crystals
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.finite_coxeter_groups import FiniteCoxeterGroups as FiniteCoxeterGroups
from sage.categories.finite_crystals import FiniteCrystals as FiniteCrystals
from sage.categories.finite_dimensional_algebras_with_basis import FiniteDimensionalAlgebrasWithBasis as FiniteDimensionalAlgebrasWithBasis
from sage.categories.finite_dimensional_bialgebras_with_basis import FiniteDimensionalBialgebrasWithBasis as FiniteDimensionalBialgebrasWithBasis
from sage.categories.finite_dimensional_coalgebras_with_basis import FiniteDimensionalCoalgebrasWithBasis as FiniteDimensionalCoalgebrasWithBasis
from sage.categories.finite_dimensional_hopf_algebras_with_basis import FiniteDimensionalHopfAlgebrasWithBasis as FiniteDimensionalHopfAlgebrasWithBasis
from sage.categories.finite_dimensional_modules_with_basis import FiniteDimensionalModulesWithBasis as FiniteDimensionalModulesWithBasis
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.finite_groups import FiniteGroups as FiniteGroups
from sage.categories.finite_lattice_posets import FiniteLatticePosets as FiniteLatticePosets
from sage.categories.finite_monoids import FiniteMonoids as FiniteMonoids
from sage.categories.finite_permutation_groups import FinitePermutationGroups as FinitePermutationGroups
from sage.categories.finite_posets import FinitePosets as FinitePosets
from sage.categories.finite_semigroups import FiniteSemigroups as FiniteSemigroups
from sage.categories.finite_sets import FiniteSets as FiniteSets
from sage.categories.finite_weyl_groups import FiniteWeylGroups as FiniteWeylGroups
from sage.categories.function_fields import FunctionFields as FunctionFields
from sage.categories.g_sets import GSets as GSets
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
from sage.categories.hecke_modules import HeckeModules as HeckeModules
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.hopf_algebras_with_basis import HopfAlgebrasWithBasis as HopfAlgebrasWithBasis
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.lattice_posets import LatticePosets as LatticePosets
from sage.categories.left_modules import LeftModules as LeftModules
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.matrix_algebras import MatrixAlgebras as MatrixAlgebras
from sage.categories.modular_abelian_varieties import ModularAbelianVarieties as ModularAbelianVarieties
from sage.categories.modules import Modules as Modules
from sage.categories.modules_with_basis import ModulesWithBasis as ModulesWithBasis
from sage.categories.monoid_algebras import MonoidAlgebras as MonoidAlgebras
from sage.categories.number_fields import NumberFields as NumberFields
from sage.categories.permutation_groups import PermutationGroups as PermutationGroups
from sage.categories.pointed_sets import PointedSets as PointedSets
from sage.categories.posets import Posets as Posets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.categories.right_modules import RightModules as RightModules
from sage.categories.ring_ideals import RingIdeals as RingIdeals
from sage.categories.schemes import AbelianVarieties as AbelianVarieties, Jacobians as Jacobians, Schemes as Schemes
from sage.categories.sets_with_grading import SetsWithGrading as SetsWithGrading
from sage.categories.signed_tensor import tensor_signed as tensor_signed
from sage.categories.simplicial_complexes import SimplicialComplexes as SimplicialComplexes
from sage.categories.tensor import tensor as tensor
from sage.categories.vector_spaces import VectorSpaces as VectorSpaces
from sage.categories.weyl_groups import WeylGroups as WeylGroups

from sage.categories.polyhedra import PolyhedralSets as PolyhedralSets
from sage.categories.lie_conformal_algebras import LieConformalAlgebras as LieConformalAlgebras

RingModules = Modules
Ideals = RingIdeals
FreeModules = ModulesWithBasis
