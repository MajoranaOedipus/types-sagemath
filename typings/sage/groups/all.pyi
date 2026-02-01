from sage.groups.matrix_gps.all import *
from sage.groups.abelian_gps.all import *
from sage.groups.perm_gps.all import *
from sage.groups.additive_abelian.all import *
from sage.groups.generic import discrete_log as discrete_log, discrete_log_lambda as discrete_log_lambda, discrete_log_rho as discrete_log_rho, linear_relation as linear_relation, multiple as multiple, multiples as multiples, order_from_multiple as order_from_multiple
from sage.groups.pari_group import PariGroup as PariGroup

from sage.groups.class_function import ClassFunction as ClassFunction
from sage.groups.conjugacy_classes import (
    ConjugacyClass as ConjugacyClass,
    ConjugacyClassGAP as ConjugacyClassGAP,
)

from sage.groups.free_group import FreeGroup as FreeGroup
from sage.groups.braid import BraidGroup as BraidGroup
from sage.groups.cubic_braid import (
    CubicBraidGroup as CubicBraidGroup,
    AssionGroupU as AssionGroupU,
    AssionGroupS as AssionGroupS,
)

from sage.groups.affine_gps.affine_group import AffineGroup as AffineGroup
from sage.groups.affine_gps.euclidean_group import EuclideanGroup as EuclideanGroup

from sage.groups.artin import ArtinGroup as ArtinGroup
from sage.groups.raag import RightAngledArtinGroup as RightAngledArtinGroup

from sage.groups import groups_catalog
groups = groups_catalog

from sage.groups.semimonomial_transformations.semimonomial_transformation_group import SemimonomialTransformationGroup as SemimonomialTransformationGroup

from sage.groups.group_exp import GroupExp as GroupExp
from sage.groups.group_exp import (
    GroupExp_Class as GroupExp_Class,
    GroupExpElement as GroupExpElement,
)

from sage.groups.group_semidirect_product import GroupSemidirectProduct as GroupSemidirectProduct
from sage.groups.group_semidirect_product import GroupSemidirectProductElement as GroupSemidirectProductElement
