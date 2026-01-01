r"""
A subset of sage.categories.all with just the basic categories needed
for sage startup (i.e. to define ZZ, QQ, ...).
"""
from sage.categories.additive_magmas import AdditiveMagmas as AdditiveMagmas
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups as CommutativeAdditiveGroups
from sage.categories.commutative_additive_monoids import CommutativeAdditiveMonoids as CommutativeAdditiveMonoids
from sage.categories.commutative_additive_semigroups import CommutativeAdditiveSemigroups as CommutativeAdditiveSemigroups
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.complete_discrete_valuation import CompleteDiscreteValuationFields as CompleteDiscreteValuationFields, CompleteDiscreteValuationRings as CompleteDiscreteValuationRings
from sage.categories.dedekind_domains import DedekindDomains as DedekindDomains
from sage.categories.discrete_valuation import DiscreteValuationFields as DiscreteValuationFields, DiscreteValuationRings as DiscreteValuationRings
from sage.categories.division_rings import DivisionRings as DivisionRings
from sage.categories.domains import Domains as Domains
from sage.categories.euclidean_domains import EuclideanDomains as EuclideanDomains
from sage.categories.fields import Fields as Fields
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.categories.gcd_domains import GcdDomains as GcdDomains
from sage.categories.groups import Groups as Groups
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.magmas import Magmas as Magmas
from sage.categories.monoids import Monoids as Monoids
from sage.categories.objects import Objects as Objects
from sage.categories.partially_ordered_monoids import PartiallyOrderedMonoids as PartiallyOrderedMonoids
from sage.categories.posets import Posets as Posets
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as PrincipalIdealDomains
from sage.categories.quotient_fields import QuotientFields as QuotientFields
from sage.categories.rings import Rings as Rings
from sage.categories.rngs import Rngs as Rngs
from sage.categories.semigroups import Semigroups as Semigroups
from sage.categories.semirings import Semirings as Semirings
from sage.categories.sets_cat import EmptySetError as EmptySetError, Sets as Sets
from sage.categories.unique_factorization_domains import UniqueFactorizationDomains as UniqueFactorizationDomains

PartiallyOrderedSets = Posets
OrderedSets = Posets
OrderedMonoids = PartiallyOrderedMonoids
