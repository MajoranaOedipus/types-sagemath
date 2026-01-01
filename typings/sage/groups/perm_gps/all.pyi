from sage.groups.perm_gps.constructor import (
    PermutationGroupElement as PermutationGroupElement,
)
from sage.groups.perm_gps.cubegroup import (
    CubeGroup as CubeGroup,
    RubiksCube as RubiksCube,
)
from sage.groups.perm_gps.permgroup import (
    PermutationGroup as PermutationGroup,
    PermutationGroup_generic as PermutationGroup_generic,
    PermutationGroup_subgroup as PermutationGroup_subgroup,
    direct_product_permgroups as direct_product_permgroups,
)
from sage.groups.perm_gps.permgroup_morphism import (
    PermutationGroupMorphism_id as PermutationGroupMorphism_id,
    PermutationGroupMorphism_im_gens as PermutationGroupMorphism_im_gens,
)
from sage.groups.perm_gps.permgroup_named import (
    AlternatingGroup as AlternatingGroup,
    CyclicPermutationGroup as CyclicPermutationGroup,
    DiCyclicGroup as DiCyclicGroup,
    DihedralGroup as DihedralGroup,
    GeneralDihedralGroup as GeneralDihedralGroup,
    KleinFourGroup as KleinFourGroup,
    MathieuGroup as MathieuGroup,
    PGL as PGL,
    PGU as PGU,
    PSL as PSL,
    PSU as PSU,
    PSp as PSp,
    PrimitiveGroup as PrimitiveGroup,
    PrimitiveGroups as PrimitiveGroups,
    QuaternionGroup as QuaternionGroup,
    SemidihedralGroup as SemidihedralGroup,
    SmallPermutationGroup as SmallPermutationGroup,
    SplitMetacyclicGroup as SplitMetacyclicGroup,
    SuzukiGroup as SuzukiGroup,
    SymmetricGroup as SymmetricGroup,
    TransitiveGroup as TransitiveGroup,
    TransitiveGroups as TransitiveGroups,
)

PermutationGroupMorphism = PermutationGroupMorphism_im_gens
